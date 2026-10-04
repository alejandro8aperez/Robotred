"""Revierte SOLO el dominio y el correo a robotred.co.

Decision tomada: la marca visible es ROBOTY-RED, pero roboty-red.co todavia
no esta registrado. Hasta que exista, las etiquetas SEO, el correo y las
rutas del repositorio deben apuntar a robotred.co, que si existe.

El nombre de marca (ROBOTY-RED) NO se toca: ese cambio si es definitivo.

Ejecutar de nuevo cuando roboty-red.co este registrado y con DNS apuntando
al sitio de Netlify.
"""

from pathlib import Path

ROOT = Path(__file__).resolve().parent

# Solo lo que depende del dominio. La marca se queda como ROBOTY-RED.
REGLAS = [
    ("roboty-red.co", "robotred.co"),
    ("Roboty-red", "Robotred"),
]

EXT = {".html", ".css", ".js", ".xml", ".txt", ".py", ".toml", ".md", ".svg", ".json"}
SALTAR = {".git", "node_modules", "__pycache__", ".netlify", "assets-src", "Imagenes"}


def objetivos():
    for p in sorted(ROOT.rglob("*")):
        if not p.is_file() or p.name == Path(__file__).name:
            continue
        if any(parte in SALTAR for parte in p.parts):
            continue
        if p.suffix.lower() in EXT:
            yield p


def main():
    tocados = []
    for p in objetivos():
        try:
            original = p.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue

        nuevo = original
        cambios = []
        for viejo, replacement in REGLAS:
            if viejo in nuevo:
                n = nuevo.count(viejo)
                nuevo = nuevo.replace(viejo, replacement)
                cambios.append(f"{viejo} ({n})")

        if nuevo != original:
            p.write_text(nuevo, encoding="utf-8")
            tocados.append((p.relative_to(ROOT).as_posix(), ", ".join(cambios)))

    for nombre, cambios in tocados:
        print(f"{nombre:26} {cambios}")
    print(f"\n{len(tocados)} archivos actualizados")

    print("\n== COMPROBACION ==")
    print("nombre de marca intacto:",
          "ROBOTY-RED" in (ROOT / "index.html").read_text(encoding="utf-8"))
    restos = 0
    for p in objetivos():
        try:
            s = p.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        for viejo, _ in REGLAS:
            if viejo in s:
                print(f"  {p.relative_to(ROOT).as_posix()}: queda '{viejo}'")
                restos += 1
    print("restos:", restos or "ninguno")


if __name__ == "__main__":
    main()