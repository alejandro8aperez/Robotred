"""Genera las paginas del curso en curso/modulo-NN.html.

El esqueleto (head, sprite, menu, pie) es identico en las diez lecciones, asi
que vive aqui una sola vez y el contenido de cada modulo esta en
_curso_datos.py. Para cambiar el diseno se edita este archivo y se regenera.

Uso:  python _gen_curso.py

Salida:
  curso/index.html            (tambien generado, para mantenerlo sincronizado)
  curso/modulo-01.html ... modulo-10.html
"""

import re
from pathlib import Path

from _curso_datos import CURSO, MODULOS as MODULOS_A
from _curso_datos_b import MODULOS_B
from _curso_datos_c import MODULOS_C

MODULOS = MODULOS_A + MODULOS_B + MODULOS_C

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "curso"

DOMAIN = "https://robotred.co"

ICONOS = {
    "clock": '<circle cx="12" cy="12" r="8.5"/><path d="M12 7v5.2l3.2 2"/>',
    "doc": '<path d="M14 3H7a1 1 0 0 0-1 1v16a1 1 0 0 0 1 1h10a1 1 0 0 0 1-1V7l-4-4Z"/><path d="M14 3v4h4M9 12h6M9 16h6"/>',
    "target": '<circle cx="12" cy="12" r="8.5"/><circle cx="12" cy="12" r="4.5"/><circle cx="12" cy="12" r="1"/>',
    "shield": '<path d="M12 3l7 3v5.5c0 4.3-2.9 8.1-7 9.5-4.1-1.4-7-5.2-7-9.5V6l7-3Z"/><path d="m9 12 2 2 4-4"/>',
    "layers": '<path d="m12 3 8.5 4.5L12 12 3.5 7.5 12 3Z"/><path d="m4 12 8 4.3 8-4.3M4 16.5 12 21l8-4.5"/>',
    "ai": '<path d="M12 4a3 3 0 0 0-3 3 3 3 0 0 0-2 5.2A3 3 0 0 0 9 18a3 3 0 0 0 3 2 3 3 0 0 0 3-2 3 3 0 0 0 2-5.8A3 3 0 0 0 15 7a3 3 0 0 0-3-3Z"/><path d="M12 8v9M9.5 11.5h5M9.5 14.5h5"/>',
    "thermal": '<path d="M12 3a3 3 0 0 1 3 3v7.5a5 5 0 1 1-6 0V6a3 3 0 0 1 3-3Z"/><path d="M12 9v6"/>',
    "wrench": '<path d="M15.5 3.5a5 5 0 0 0-6.2 6.4L3.7 15.5a2 2 0 1 0 2.8 2.8l5.6-5.6a5 5 0 0 0 6.4-6.2l-3 3-2.6-.7-.7-2.6 3-3Z"/>',
    "cpu": '<rect x="6" y="6" width="12" height="12" rx="2"/><path d="M10 3v3M14 3v3M10 18v3M14 18v3M3 10h3M3 14h3M18 10h3M18 14h3M10 10h4v4h-4z"/>',
    "arrow": '<path d="M5 12h13M12.5 6l6 6-6 6"/>',
    "mail": '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3.5 7 8.5 6 8.5-6"/>',
    "phone": '<path d="M7 3h3l1.5 4-2 1.5a11 11 0 0 0 5 5L16 11.5 20 13v3a2 2 0 0 1-2.2 2A16 16 0 0 1 5 5.2 2 2 0 0 1 7 3Z"/>',
    "pin": '<path d="M12 21s6.5-6 6.5-11a6.5 6.5 0 1 0-13 0C5.5 15 12 21 12 21Z"/><circle cx="12" cy="10" r="2.5"/>',
    "robo": '<rect x="4" y="8" width="16" height="11" rx="3"/><path d="M12 8V5M9 5h6M9 13h.01M15 13h.01M9.5 16.5h5M2 12v3M22 12v3"/>',
    "network": '<circle cx="12" cy="5" r="2.5"/><circle cx="5" cy="18" r="2.5"/><circle cx="19" cy="18" r="2.5"/><path d="M10.4 6.9 6.6 15.6M13.6 6.9l3.8 8.7M7.5 18h9"/>',
    "sensor": '<circle cx="12" cy="12" r="3"/><path d="M6.5 6.5a7.8 7.8 0 0 0 0 11M17.5 6.5a7.8 7.8 0 0 1 0 11M3.5 3.5a12 12 0 0 0 0 17M20.5 3.5a12 12 0 0 1 0 17"/>',
    "map": '<path d="M12 21s6.5-6 6.5-11a6.5 6.5 0 1 0-13 0C5.5 15 12 21 12 21Z"/><circle cx="12" cy="10" r="2.5"/>',
    "drone": '<rect x="9" y="9" width="6" height="6" rx="2"/><path d="M9 10 5 6M15 10l4-4M9 14l-4 4M15 14l4 4M3 4h4M17 4h4M3 20h4M17 20h4"/>',
}

ICONOS_POR_DEFECTO = ("clock", "doc", "target", "shield", "layers", "ai",
                      "thermal", "wrench", "cpu", "arrow", "mail", "phone",
                      "pin", "robo", "network", "sensor", "map", "drone")

NAV = [
    ("Inicio", "../index.html"),
    ("Soluciones", "../index.html#soluciones"),
    ("Robot X", "../index.html#robot"),
    ("Tutorial", "../tutorial.html"),
    ("Curso", "index.html"),
]


def sprite(extra=()):
    """Bloque <symbol> con los iconos usados en la pagina."""
    usados = list(ICONOS_POR_DEFECTO) + list(extra)
    lines = []
    for name in usados:
        path = ICONOS.get(name)
        if path is None:
            raise SystemExit(f"icono desconocido: {name}")
        lines.append(f'    <symbol id="i-{name}" viewBox="0 0 24 24">{path}</symbol>')
    return ('  <svg class="sprite" aria-hidden="true" focusable="false" '
            'xmlns="http://www.w3.org/2000/svg">\n'
            + "\n".join(lines) + "\n  </svg>")


def nav(actual):
    items = []
    for texto, href in NAV:
        cls = ' class="active" aria-current="page"' if texto == actual else ""
        items.append(f'        <a href="{href}"{cls}>{texto}</a>')
    return "\n".join(items)


def meta(entradas):
    lis = "\n".join(
        f'            <li><svg class="ico ico-sm"><use href="#i-{ico}"/></svg>{txt}</li>'
        for ico, txt in entradas)
    return f'          <ul class="leccion-meta">\n{lis}\n          </ul>'


def seccion(s):
    return f'          <section>\n            <h2>{s["h2"]}</h2>\n{s["html"]}\n          </section>'


def construir_indice():
    filas = "\n".join(
        f'              <li><a href="modulo-{m["num"]}.html">'
        f'<span class="n">{m["num"]}</span><div><strong>{m["titulo"]}</strong>'
        f'<span>{m["resumen"]}</span></div>'
        f'<svg class="ico ico-sm"><use href="#i-{m.get("icono", "arrow")}"/></svg></a></li>'
        for m in MODULOS)
    return filas


def construir_modulo(m):
    objetivo = "\n".join(f"              <li>{o}</li>" for o in m["objetivos"])
    secciones = "\n\n".join(seccion(s) for s in m["secciones"])
    taller = m.get("taller")

    if taller:
        t = (f'          <section class="taller">\n'
             f'            <h2>{taller["titulo"]}</h2>\n'
             f'{taller["html"]}\n'
             f'            <p class="entrega"><strong>Entregable</strong>'
             f'{taller["entrega"]}</p>\n'
             f'          </section>')
    else:
        t = ""

    if m.get("resumen_html"):
        resumen = (f'          <section class="resumen-eco">\n'
                   f'            <h2>Resumen para la gerencia</h2>\n'
                   f'{m["resumen_html"]}\n'
                   f'          </section>')
    else:
        resumen = ""

    return TEMPLATE.format(
        num=m["num"],
        titulo=m["titulo"],
        lead=m["lead"],
        meta_lista=meta(m["meta"]),
        objetivos=objetivo,
        secciones=secciones,
        taller=t,
        resumen=resumen,
        nav=nav("Curso"),
        sprite=sprite(),
        canon=f"{DOMAIN}/curso/modulo-{m['num']}.html",
        # El indice de modulos se resuelve en build(), asi que estos tres
        # viajan como marcadores @@ que se sustituyen al final. No pueden
        # ser campos de format(), porque se rellenan con "" y no hay forma
        # de distinguirlos despues.
        prev="@@PREV@@",
        sig_url="@@SIG_URL@@",
        sig_txt="@@SIG_TXT@@",
    )


TEMPLATE = """<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Módulo {num} — {titulo} | ROBOTY-RED</title>
  <meta name="description" content="{lead}">
  <meta name="theme-color" content="#0A1620">
  <meta name="author" content="ROBOTY-RED">
  <meta name="robots" content="index, follow">
  <link rel="canonical" href="{canon}">

  <meta property="og:type" content="article">
  <meta property="og:locale" content="es_CO">
  <meta property="og:site_name" content="ROBOTY-RED">
  <meta property="og:title" content="Módulo {num} — {titulo}">
  <meta property="og:description" content="{lead}">
  <meta property="og:url" content="{canon}">
  <meta property="og:image" content="https://robotred.co/assets/og-image.png">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="Módulo {num} — {titulo}">
  <meta name="twitter:description" content="{lead}">
  <meta name="twitter:image" content="https://robotred.co/assets/og-image.png">

  <link rel="icon" href="../assets/favicon-32.png" sizes="32x32" type="image/png">
  <link rel="icon" href="../assets/favicon-192.png" sizes="192x192" type="image/png">
  <link rel="apple-touch-icon" href="../assets/apple-touch-icon.png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;600;700&family=DM+Sans:opsz,wght@9..40,400;9..40,500;9..40,700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="../styles.css">
</head>
<body class="page-curso">
  <a class="skip-link" href="#contenido">Saltar al contenido</a>
  <div class="progress" id="progress" aria-hidden="true"><span></span></div>

{sprite}

  <header class="topbar" id="topbar">
    <div class="topbar-inner">
      <a class="brand" href="../index.html" aria-label="ROBOTY-RED — inicio">
        <img class="brand-logo" src="../assets/logo-blanco.webp" width="100" height="96" alt="" fetchpriority="high">
      </a>

      <nav class="nav" id="nav" aria-label="Navegación principal">
{nav}
      </nav>

      <div class="topbar-actions">
        <a class="link-tech" href="https://alejandro8aperez.github.io/INSTE-BOT/" target="_blank" rel="noopener">Área técnica</a>
        <a class="btn btn-primary btn-sm" href="../index.html#contacto">Solicitar demo</a>
        <button class="nav-toggle" id="navToggle" aria-label="Abrir menú" aria-expanded="false" aria-controls="nav">
          <span></span><span></span><span></span>
        </button>
      </div>
    </div>
  </header>

  <main id="contenido">
    <article class="leccion">
      <div class="container leccion-wrap">

        <header class="leccion-head">
          <p class="leccion-num">Módulo {num} de 10</p>
          <h1>{titulo}</h1>
          <p class="leccion-lead">{lead}</p>
{meta_lista}
        </header>

        <div class="leccion-body">

          <section>
            <h2>Qué va a aprender</h2>
            <ul class="ticks">
{objetivos}
            </ul>
          </section>

{secciones}

{taller}

{resumen}

        </div>

        <nav class="leccion-nav" aria-label="Navegación del curso">
{prev}
          <a class="btn btn-primary" href="{sig_url}">{sig_txt} <svg class="ico ico-sm"><use href="#i-arrow"/></svg></a>
        </nav>

      </div>
    </article>
  </main>

  <footer class="footer">
    <div class="container footer-grid">
      <div class="footer-brand">
        <a class="brand" href="../index.html" aria-label="ROBOTY-RED — inicio">
          <img class="brand-logo" src="../assets/logo-blanco.webp" width="100" height="96" alt="" loading="lazy">
        </a>
        <p>Robots autónomos para inspeccionar, diagnosticar y mantener redes eléctricas sin interrumpir el servicio.</p>
        <div class="social">
          <a href="mailto:info@robotred.co" aria-label="Correo"><svg class="ico ico-sm"><use href="#i-mail"/></svg></a>
          <a href="https://github.com/alejandro8aperez/Robotred" target="_blank" rel="noopener" aria-label="GitHub"><svg class="ico ico-sm"><use href="#i-network"/></svg></a>
        </div>
      </div>

      <nav class="footer-col" aria-label="Curso">
        <h4>Curso</h4>
        <a href="modulo-01.html">Módulo 01 — Introducción</a>
        <a href="modulo-04.html">Módulo 04 — Sensores</a>
        <a href="modulo-06.html">Módulo 06 — IA en el borde</a>
        <a href="modulo-08.html">Módulo 08 — Seguridad</a>
        <a href="modulo-10.html">Módulo 10 — Proyecto final</a>
      </nav>

      <nav class="footer-col" aria-label="Sitio">
        <h4>Sitio</h4>
        <a href="../index.html">Inicio</a>
        <a href="../index.html#soluciones">Soluciones</a>
        <a href="../tutorial.html">Tutorial</a>
        <a href="../index.html#faq">Preguntas frecuentes</a>
        <a href="../index.html#contacto">Contacto</a>
      </nav>

      <nav class="footer-col" aria-label="Aprendizaje">
        <h4>Aprendizaje</h4>
        <a href="https://alejandro8aperez.github.io/INSTE-BOT/" target="_blank" rel="noopener">Libro Blanco INSTE-BOT X</a>
        <a href="../index.html#resultados">Cumplimiento RETIE</a>
      </nav>
    </div>

    <div class="container footer-bottom">
      <p>© <span id="year">2026</span> ROBOTY-RED. Todos los derechos reservados.</p>
      <p class="foot-note">Las referencias normativas IEC/TC 129 se citan con fines formativos. Los valores técnicos se validan por tramo en cada piloto.</p>
    </div>
  </footer>

  <button class="to-top" id="toTop" aria-label="Volver arriba" hidden>
    <svg class="ico ico-sm" viewBox="0 0 24 24"><path d="M12 19V6M6 12l6-6 6 6" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>
  </button>

  <script src="../app.js" defer></script>
</body>
</html>
"""


def build():
    OUT.mkdir(exist_ok=True)
    total = 0
    for i, m in enumerate(MODULOS):
        num = m["num"]
        prev = (f'          <a class="btn btn-outline" href="modulo-{MODULOS[i-1]["num"]}.html">'
                f'← {MODULOS[i-1]["titulo"].split(" y ")[0]}</a>'
                if i else '          <span class="empty"></span>')
        sig_url = f'modulo-{MODULOS[i+1]["num"]}.html' if i + 1 < len(MODULOS) else "../tutorial.html"
        sig_txt = MODULOS[i + 1]["titulo"] if i + 1 < len(MODULOS) else "Ver el tutorial completo"

        html = construir_modulo(m)
        html = html.replace("@@PREV@@", prev)
        html = html.replace("@@SIG_URL@@", sig_url)
        html = html.replace("@@SIG_TXT@@", sig_txt)

        (OUT / f"modulo-{num}.html").write_text(html, encoding="utf-8")
        kb = (OUT / f"modulo-{num}.html").stat().st_size / 1024
        print(f"  modulo-{num}.html   {len(html.splitlines()):4} lineas  {kb:5.0f} KB")
        total += kb

    idx = INDICE_TEMPLATE.replace("{filas}", construir_indice())
    idx = idx.replace("{sprite}", sprite())
    idx = idx.replace("{nav}", nav("Curso"))
    idx = idx.replace("{indice_meta}", meta(CURSO["meta"]))
    for campo in ("titulo", "descripcion", "lead", "antes_p1", "antes_p2",
                  "regla_titulo", "regla", "programa_h2", "cierre_h2",
                  "cierre_p1", "cierre_fuerte"):
        idx = idx.replace("{" + campo + "}", CURSO[campo])
    if "{" in idx.replace("{", "{", 1) and re.search(r"\{[a-z_]+\}", idx):
        raise SystemExit("quedaron marcadores sin rellenar: "
                         + str(sorted(set(re.findall(r"\{[a-z_]+\}", idx)))))
    (OUT / "index.html").write_text(idx, encoding="utf-8")
    print(f"  index.html          {len(idx.splitlines()):4} lineas  "
          f"{(OUT / 'index.html').stat().st_size / 1024:5.0f} KB")
    print(f"\n{len(MODULOS)} modulos, {total:.0f} KB en total -> {OUT}")


INDICE_TEMPLATE = """<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{titulo}</title>
  <meta name="description" content="{descripcion}">
  <meta name="theme-color" content="#0A1620">
  <meta name="author" content="ROBOTY-RED">
  <meta name="robots" content="index, follow">
  <link rel="canonical" href="https://robotred.co/curso/">

  <meta property="og:type" content="website">
  <meta property="og:locale" content="es_CO">
  <meta property="og:site_name" content="ROBOTY-RED">
  <meta property="og:title" content="{titulo}">
  <meta property="og:description" content="{descripcion}">
  <meta property="og:url" content="https://robotred.co/curso/">
  <meta property="og:image" content="https://robotred.co/assets/og-image.png">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{titulo}">
  <meta name="twitter:description" content="{descripcion}">
  <meta name="twitter:image" content="https://robotred.co/assets/og-image.png">

  <link rel="icon" href="../assets/favicon-32.png" sizes="32x32" type="image/png">
  <link rel="icon" href="../assets/favicon-192.png" sizes="192x192" type="image/png">
  <link rel="apple-touch-icon" href="../assets/apple-touch-icon.png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;600;700&family=DM+Sans:opsz,wght@9..40,400;9..40,500;9..40,700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="../styles.css">
</head>
<body class="page-curso">
  <a class="skip-link" href="#contenido">Saltar al contenido</a>
  <div class="progress" id="progress" aria-hidden="true"><span></span></div>

{sprite}

  <header class="topbar" id="topbar">
    <div class="topbar-inner">
      <a class="brand" href="../index.html" aria-label="ROBOTY-RED — inicio">
        <img class="brand-logo" src="../assets/logo-blanco.webp" width="100" height="96" alt="" fetchpriority="high">
      </a>

      <nav class="nav" id="nav" aria-label="Navegación principal">
{nav}
      </nav>

      <div class="topbar-actions">
        <a class="link-tech" href="https://alejandro8aperez.github.io/INSTE-BOT/" target="_blank" rel="noopener">Área técnica</a>
        <a class="btn btn-primary btn-sm" href="../index.html#contacto">Solicitar demo</a>
        <button class="nav-toggle" id="navToggle" aria-label="Abrir menú" aria-expanded="false" aria-controls="nav">
          <span></span><span></span><span></span>
        </button>
      </div>
    </div>
  </header>

  <main id="contenido">
    <article class="leccion">
      <div class="container leccion-wrap">

        <header class="leccion-head">
          <p class="leccion-num">Curso completo · 10 módulos</p>
          <h1>{titulo}</h1>
          <p class="leccion-lead">{lead}</p>
{indice_meta}
        </header>

        <div class="leccion-body">

          <section>
            <h2>Antes de empezar</h2>
            <p>{antes_p1}</p>
            <p>{antes_p2}</p>

            <div class="callout callout-key">
              <p class="callout-title"><svg class="ico ico-sm"><use href="#i-shield"/></svg>{regla_titulo}</p>
              <p>{regla}</p>
            </div>
          </section>

          <section>
            <h2>{programa_h2}</h2>

            <ul class="curso-index">
{filas}
            </ul>
          </section>

          <section>
            <h2>Cómo se estudia</h2>
            <ul class="bullets">
              <li><strong>Una sesión por módulo.</strong> Cada módulo se lee de principio a fin y termina con un taller y una entrega concreta.</li>
              <li><strong>Ejemplo antes que teoría.</strong> Partimos de un despliegue real y de ahí derivamos el concepto, la norma y el procedimiento.</li>
              <li><strong>Cierre para la gerencia.</strong> Cada módulo termina con un resumen que se puede llevar a una reunión de comité.</li>
              <li><strong>Material reutilizable.</strong> Las tablas y listas de verificación sirven para especificaciones y licitaciones.</li>
            </ul>
          </section>

          <section class="resumen-eco">
            <h2>{cierre_h2}</h2>
            <p>{cierre_p1}</p>
            <p><strong>{cierre_fuerte}</strong></p>
          </section>

        </div>
      </div>
    </article>
  </main>

  <footer class="footer">
    <div class="container footer-grid">
      <div class="footer-brand">
        <a class="brand" href="../index.html" aria-label="ROBOTY-RED — inicio">
          <img class="brand-logo" src="../assets/logo-blanco.webp" width="100" height="96" alt="" loading="lazy">
        </a>
        <p>Robots autónomos para inspeccionar, diagnosticar y mantener redes eléctricas sin interrumpir el servicio.</p>
        <div class="social">
          <a href="mailto:info@robotred.co" aria-label="Correo"><svg class="ico ico-sm"><use href="#i-mail"/></svg></a>
        </div>
      </div>

      <nav class="footer-col" aria-label="Curso">
        <h4>Curso</h4>
        <a href="modulo-01.html">Módulo 01 — Introducción</a>
        <a href="modulo-04.html">Módulo 04 — Sensores</a>
        <a href="modulo-06.html">Módulo 06 — IA en el borde</a>
        <a href="modulo-08.html">Módulo 08 — Seguridad</a>
        <a href="modulo-10.html">Módulo 10 — Proyecto final</a>
      </nav>

      <nav class="footer-col" aria-label="Sitio">
        <h4>Sitio</h4>
        <a href="../index.html">Inicio</a>
        <a href="../index.html#soluciones">Soluciones</a>
        <a href="../tutorial.html">Tutorial</a>
        <a href="../index.html#faq">Preguntas frecuentes</a>
        <a href="../index.html#contacto">Contacto</a>
      </nav>

      <nav class="footer-col" aria-label="Aprendizaje">
        <h4>Aprendizaje</h4>
        <a href="https://alejandro8aperez.github.io/INSTE-BOT/" target="_blank" rel="noopener">Libro Blanco INSTE-BOT X</a>
        <a href="../index.html#resultados">Cumplimiento RETIE</a>
      </nav>
    </div>

    <div class="container footer-bottom">
      <p>© <span id="year">2026</span> ROBOTY-RED. Todos los derechos reservados.</p>
      <p class="foot-note">Las referencias normativas IEC/TC 129 se citan con fines formativos. Los valores técnicos se validan por tramo en cada piloto.</p>
    </div>
  </footer>

  <button class="to-top" id="toTop" aria-label="Volver arriba" hidden>
    <svg class="ico ico-sm" viewBox="0 0 24 24"><path d="M12 19V6M6 12l6-6 6 6" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>
  </button>

  <script src="../app.js" defer></script>
</body>
</html>
"""

if __name__ == "__main__":
    build()
