from pathlib import Path
import re
import sys
from html.parser import HTMLParser

root = Path(__file__).resolve().parent
html = (root / "index.html").read_text(encoding="utf-8")
css = (root / "styles.css").read_text(encoding="utf-8")
js = (root / "app.js").read_text(encoding="utf-8")

VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link",
        "meta", "param", "source", "track", "wbr", "path", "circle", "rect",
        "stop", "use", "line", "polygon", "polyline", "ellipse"}

problems = []

EXT = (".png", ".jpg", ".jpeg", ".webp", ".svg", ".css", ".js", ".xml", ".ico")


def ids_of(path):
    """Ids declarados en un archivo HTML."""
    return set(re.findall(r'\bid="([^"]+)"', path.read_text(encoding="utf-8")))


def broken_refs(refs, own_ids):
    """Refs que no apuntan a ningun id.

    Admite anclas locales (#id), paginas (otra.html) y paginas con ancla
    (otra.html#id), comprobando el ancla contra los ids de la pagina destino.
    """
    broken = set()
    for r in refs:
        if not r or r in own_ids:
            continue
        target, _, frag = r.partition("#")
        if not target:
            # Ancla local: ya cubierta por la comprobacion de own_ids.
            continue
        if "/" in target:
            continue
        if target.endswith(".html"):
            dest = root / target
            if not dest.exists():
                broken.add(r)
            elif frag and frag not in ids_of(dest):
                broken.add(r)
            continue
        if not target.endswith(tuple(EXT)):
            broken.add(r)
    return sorted(broken)


class Checker(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack, self.errors, self.ids, self.refs = [], [], [], []

    def handle_starttag(self, tag, attrs):
        d = dict(attrs)
        for k in ("id",):
            if k in d:
                self.ids.append(d[k])
        for k in ("href", "aria-controls", "for", "data-for"):
            if k in d and d[k]:
                self.refs.append(d[k].lstrip("#"))
        for k in ("aria-labelledby",):
            if k in d:
                self.refs.extend(d[k].split())
        if tag == "img":
            for k in ("src",):
                if k in d and d[k]:
                    self.refs.append(d[k])
            self.refs.extend(d.get("srcset", "").split())
        if tag not in VOID:
            self.stack.append((tag, self.getpos()))

    def handle_endtag(self, tag):
        if tag in VOID:
            return
        if self.stack and self.stack[-1][0] == tag:
            self.stack.pop()
        else:
            self.errors.append(f"</{tag}> @ {self.getpos()}")


c = Checker()
c.feed(html)

print("== HTML ==")
print("sin cerrar:", c.stack)
print("errores:", c.errors)
dupes = [i for i in set(c.ids) if c.ids.count(i) > 1]
print("ids duplicados:", dupes)

local_refs = {r for r in c.refs
              if r and not r.startswith(("http://", "https://", "mailto:", "tel:"))}
broken_index_refs = broken_refs(local_refs, set(c.ids))
print("refs rotas:", broken_index_refs)

if c.stack or c.errors or dupes or broken_index_refs:
    problems.append("HTML mal formado o referencias internas rotas")

symbols = set(re.findall(r'<symbol id="([^"]+)"', html))
uses = set(re.findall(r'<use href="#([^"]+)"', html))
orphan_uses = sorted(uses - symbols)
print("use sin symbol:", orphan_uses)
if orphan_uses:
    problems.append("Iconos <use> sin <symbol> correspondiente")

index_absolutes = sorted(set(re.findall(r'href="/([^"]*)"', html)))
print("enlaces con ruta absoluta:", index_absolutes or "ninguno")
if index_absolutes:
    problems.append(
        f"index.html usa rutas absolutas (rompen en file://): {index_absolutes}")

print("\n== CSS ==")
print("llaves:", css.count("{"), css.count("}"))
undefined_vars = sorted({v for v in re.findall(r"var\(--([a-z0-9-]+)\)", css)
                         if f"--{v}:" not in css})
print("var sin definir:", undefined_vars)
if css.count("{") != css.count("}"):
    problems.append("CSS con llaves desbalanceadas")
if undefined_vars:
    problems.append("Variables CSS usadas pero no definidas")

print("\n== JS (referencias a ids) ==")
ids = set(c.ids)
js_ids = set(re.findall(r"getElementById\('([^']+)'\)", js))
missing_ids = sorted(js_ids - ids)
print("getElementById sin id:", missing_ids)
if missing_ids:
    problems.append("app.js busca ids que no existen en el HTML")

print("\n== ASSETS ==")
for src in sorted(set(re.findall(r'(?:src|href)="([^"#]+\.(?:png|jpg|jpeg|webp|svg|css|js))"', html))):
    ok = (root / src).exists()
    print(" ", src, "->", "OK" if ok else "FALTA")
    if not ok:
        problems.append(f"Archivo referenciado que no existe: {src}")

for page in ("gracias.html", "tutorial.html"):
    if not (root / page).exists():
        problems.append(f"Falta la pagina {page}")

print("\n== FORMULARIO (Netlify) ==")
form = re.search(r"<form\b[^>]*>", html)
if not form:
    problems.append("No hay <form> en index.html")
else:
    tag = form.group(0)
    for attr in ("name=", "method=", "action=", "data-netlify=", "netlify-honeypot="):
        present = attr in tag
        print(f"  {attr:20} {'OK' if present else 'FALTA'}")
        if not present:
            problems.append(f"El formulario no declara {attr}")
    if 'name="form-name"' not in html:
        problems.append("Falta el input hidden form-name requerido por Netlify")

print("\n== CONFIG ==")
domain = "robotred.co"
head = html[:html.find("</head>")]
canonical = re.search(r'<link rel="canonical" href="([^"]+)"', head)
og_url = re.search(r'property="og:url" content="([^"]+)"', head)
if not canonical:
    problems.append("Falta link rel=canonical")
elif domain not in canonical.group(1):
    problems.append(f"El canonical no apunta a {domain}: {canonical.group(1)}")
if not og_url:
    problems.append("Falta og:url")
elif domain not in og_url.group(1):
    problems.append(f"og:url no apunta a {domain}: {og_url.group(1)}")
for f in ("netlify.toml", "robots.txt", "sitemap.xml", "gracias.html",
          "tutorial.html", "assets/og-image.png", "assets/apple-touch-icon.png",
          "assets/logo-color.webp", "assets/logo-blanco.webp",
          "assets/esquema.jpg", "assets/favicon-32.png"):
    ok = (root / f).exists()
    print(f"  {f:24} {'OK' if ok else 'FALTA'}")
    if not ok:
        problems.append(f"Falta {f}")

print("\n== PAGINAS SECUNDARIAS ==")


def check_page(name, want_robots=None, need_seo=True, need_js=True):
    """Valida una pagina distinta de index.html con las mismas reglas."""
    path = root / name
    if not path.exists():
        problems.append(f"Falta la pagina {name}")
        return

    page = path.read_text(encoding="utf-8")
    pc = Checker()
    pc.feed(page)

    issues = []
    # Enlaces con ruta absoluta: rompen al abrir el archivo con doble clic
    # (file://), donde "/" apunta a la raiz del disco. Se prefieren relativos.
    absolutes = sorted(set(re.findall(r'href="/([^"]*)"', page)))
    if absolutes:
        issues.append(f"enlaces con ruta absoluta (rompen en file://): {absolutes}")
    if pc.stack:
        issues.append(f"tags sin cerrar: {pc.stack}")
    if pc.errors:
        issues.append(f"cierres sobrantes: {pc.errors}")
    dupes = sorted(i for i in set(pc.ids) if pc.ids.count(i) > 1)
    if dupes:
        issues.append(f"ids duplicados: {dupes}")

    refs = {r for r in pc.refs
            if r and not r.startswith(("http://", "https://", "mailto:", "tel:"))}
    broken = broken_refs(refs, set(pc.ids))
    if broken:
        issues.append(f"anclas rotas: {broken}")

    symbols = set(re.findall(r'<symbol id="([^"]+)"', page))
    orphans = sorted(set(re.findall(r'<use href="#([^"]+)"', page)) - symbols)
    if orphans:
        issues.append(f"iconos <use> sin <symbol>: {orphans}")

    for src in sorted(set(re.findall(r'(?:src|href)="([^"#]+\.(?:png|jpg|jpeg|webp|svg|css|js))"', page))):
        if not (root / src).exists():
            issues.append(f"archivo inexistente: {src}")

    head = page[:page.find("</head>")]
    canonical = re.search(r'<link rel="canonical" href="([^"]+)"', head)
    if want_robots and want_robots not in page:
        issues.append(f"falta el meta robots '{want_robots}'")
    if need_seo:
        if not canonical:
            issues.append("falta link rel=canonical")
        elif "robotred.co" not in canonical.group(1):
            issues.append(f"el canonical no apunta a robotred.co: {canonical.group(1)}")
        if not re.search(r'property="og:url"', head):
            issues.append("falta og:url")
    if 'href="styles.css"' not in page:
        issues.append("no carga styles.css")
    if need_js and 'src="app.js"' not in page:
        issues.append("no carga app.js")

    print(f"  {name:18} {'OK' if not issues else 'FALLA'}")
    for i in issues:
        print(f"      - {i}")
        problems.append(f"{name}: {i}")


check_page("tutorial.html")
# La pagina de gracias es noindex y estatica: no lleva canonical, og:url ni app.js.
check_page("gracias.html", want_robots="noindex", need_seo=False, need_js=False)

print("\n== ENCUBIERTO ==")
moji = html.count("â€") + css.count("â€") + js.count("â€")
repl = html.count("\ufffd") + css.count("\ufffd") + js.count("\ufffd")
for page in ("tutorial.html", "gracias.html"):
    extra = (root / page).read_text(encoding="utf-8")
    moji += extra.count("â€")
    repl += extra.count("\ufffd")
print("mojibake 'â€':", moji, "| U+FFFD:", repl)
if moji or repl:
    problems.append("Encoding roto: hay caracteres mojibake o U+FFFD")

print()
if problems:
    print("FALLOS (%d):" % len(problems))
    for p in problems:
        print("  -", p)
    sys.exit(1)

print("Sin fallos.")
sys.exit(0)
