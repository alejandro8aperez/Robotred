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
broken_refs = sorted(
    r for r in local_refs
    if r not in c.ids and "/" not in r and not r.endswith(tuple(EXT))
)
print("refs rotas:", broken_refs)

if c.stack or c.errors or dupes or broken_refs:
    problems.append("HTML mal formado o referencias internas rotas")

symbols = set(re.findall(r'<symbol id="([^"]+)"', html))
uses = set(re.findall(r'<use href="#([^"]+)"', html))
orphan_uses = sorted(uses - symbols)
print("use sin symbol:", orphan_uses)
if orphan_uses:
    problems.append("Iconos <use> sin <symbol> correspondiente")

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

for page in ("gracias.html",):
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
          "assets/og-image.png", "assets/apple-touch-icon.png",
          "assets/logo-color.webp", "assets/logo-blanco.webp",
          "assets/esquema.jpg", "assets/favicon-32.png"):
    ok = (root / f).exists()
    print(f"  {f:24} {'OK' if ok else 'FALTA'}")
    if not ok:
        problems.append(f"Falta {f}")

print("\n== ENCUBIERTO ==")
moji = html.count("â€") + css.count("â€") + js.count("â€")
repl = html.count("\ufffd") + css.count("\ufffd") + js.count("\ufffd")
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
