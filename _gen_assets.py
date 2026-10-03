"""Prepara las imagenes para web desde los archivos de origen.

Genera versiones optimizadas en assets/ a partir de los originales, que se
quedan fuera de git (ver .gitignore). No cambia el contenido, solo el formato.
"""

import shutil
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parent
SRC_DIR = ROOT / "assets-src"
OUT = ROOT / "assets"

JOBS = [
    {
        "src": "movelty foto inicial.jpg",
        "stem": "robot-campo",
        "width": 1100,
        "jpg": 84,
        "webp": 80,
    },
    {
        "src": "Esquema robot red en chat facebook.png",
        "stem": "ecosistema",
        "width": 1100,
        "jpg": 88,
        "webp": 82,
    },
]


def process(job):
    src = SRC_DIR / job["src"]
    if not src.exists():
        print(f"[skip] no existe {src.name}")
        return

    img = Image.open(src)
    if img.mode in ("RGBA", "LA", "P"):
        img = img.convert("RGB")

    if img.width > job["width"]:
        ratio = job["width"] / img.width
        img = img.resize(
            (job["width"], round(img.height * ratio)), Image.LANCZOS
        )

    OUT.mkdir(exist_ok=True)
    jpg = OUT / f"{job['stem']}.jpg"
    img.save(jpg, "JPEG", quality=job["jpg"], optimize=True, progressive=True)
    print(f"{jpg.name:22} {img.width}x{img.height}  {jpg.stat().st_size / 1024:6.0f} KB")

    try:
        webp = OUT / f"{job['stem']}.webp"
        img.save(webp, "WEBP", quality=job["webp"], method=6)
        print(
            f"{webp.name:22} {img.width}x{img.height}  {webp.stat().st_size / 1024:6.0f} KB"
        )
    except Exception as exc:  # noqa: BLE001
        print(f"[warn] webp no disponible: {exc}")


if __name__ == "__main__":
    process_map = JOBS
    for job in process_map:
        process(job)