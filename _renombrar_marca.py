"""Renombra la marca de ROBOT-RED a ROBOTY-RED en todo el proyecto.

Incluye el nombre visible, el dominio (robotred.co -> robotred.co), el
correo (info@robotred.co) y las rutas del repositorio de GitHub
(Robotred -> Robotred). Los nombres de archivo y rutas que no dependen
del dominio se dejan intactos a proposito (robots.txt, assets/...).

Script de un solo uso: ya se ejecuto, asi que las reglas de abajo son las
que quedan aplicadas. Volver a correrlo no cambia nada (es idempotente).

Este archivo no se debe volver a ejecutar tras un cambio de marca nuevo.
"""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent

# Orden importante: primero el dominio y el repo (minusculas y Title),
# despues las variantes de la marca en mayusculas.
REGLAS = [
    ("robotred.co", "robotred.co"),
    ("Robotred", "Robotred"),
    ("ROBOT-RED", "ROBOTY-RED"),
    ("ROBOTRED", "ROBOTY-RED"),
]

EXT = {".html", ".css", ".js", ".xml", ".txt", ".py", ".toml", ".md", ".svg", ".json"}

# Archivos que no se tocan (nombres propios del protocolo, etc.)
SALTAR = {".git", "node_modules", "__pycache__", ".netlify", "assets-src", "Imagenes"}


def objetivos():
    for p in sorted(ROOT.rglob("*")):
        if not p.is_file():
            continue
        if any(parte in SALTAR for parte in p.parts):
            continue
        if p.suffix.lower() in EXT:
            yield p


def main():
    total = 0
    tocados = []

    for p in objetivos():
        try:
            original = p.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue

        nuevo = original
        cambios = []
        for viejo, nuevo_txt in REGLAS:
            if viejo in nuevo:
                n = nuevo.count(viejo)
                nuevo = nuevo.replace(viejo, nuevo_txt)
                cambios.append(f"{viejo}->{nuevo_txt} ({n})")

        if nuevo != original:
            p.write_text(nuevo, encoding="utf-8")
            total += sum(nuevo.count(t) for _, t in REGLAS)
            tocados.append((p.relative_to(ROOT).as_posix(), ", ".join(cambios)))

    for nombre, cambios in tocados:
        print(f"{nombre:24} {cambios}")
    print(f"\n{len(tocados)} archivos actualizados")

    # Comprobacion: no debe quedar ninguna variante antigua.
    print("\n== RESTOS ==")
    restos = 0
    for p in objetivos():
        try:
            s = p.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        for viejo, _ in REGLAS:
            if viejo in s:
                print(f"  {p.relative_to(ROOT).as_posix()}: quedan '{viejo}'")
                restos += 1
    print("restos:", restos or "ninguno")

    # URLs finales para recordar los ajustes fuera del repo.
    print("\n== PENDIENTE FUERA DEL REPOSITORIO ==")
    print("  1. Registrar/apuntar el dominio robotred.co (aun no existe en el DNS)")
    print("  2. Cambiar el dominio primario en Netlify y adjuntar el certificado TLS")
    print("  3. Crear el buzon info@robotred.co antes de publicar el formulario")
    print("  4. Renombrar el repositorio de GitHub a Robotred")


if __name__ == "__main__":
    main()