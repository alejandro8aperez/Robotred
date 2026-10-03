"""Prepara las imagenes para web desde los archivos de origen.

Genera versiones optimizadas en assets/ a partir de los originales, que se
quedan fuera de git (ver .gitignore). No cambia el contenido, solo el formato.
"""

import shutil
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parent
SRC_DIR = ROOT / "Imagenes"
OUT = ROOT / "assets"

JOBS = [
    {
        "src": "Esquema.png",
        "stem": "esquema",
        "width": 1100,
        "jpg": 88,
        "webp": 82,
    },
    {
        "src": "movelty foto inicial.jpg",
        "stem": "robot-campo",
        "width": 1100,
        "jpg": 84,
        "webp": 80,
        "enabled": False,
    },
]


def process(job):
    if not job.get("enabled", True):
        return

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


def build_logo():
    """Recorta el logotipo a su contenido y genera las variantes de contraste.

    El original es un cuadrado de 1.5 MB con mucho margen transparente. Para
    el header hace falta una version en blanco (el header es azul marino
    oscuro) y otra que conserva los colores originales para fondos claros.
    """
    src = SRC_DIR / "Logotipo.png"
    if not src.exists():
        print("[skip] no existe Logotipo.png")
        return

    img = Image.open(src).convert("RGBA")
    alpha = img.getchannel("A")

    bbox = Image.eval(alpha, lambda v: 255 if v > 8 else 0).getbbox()
    if bbox:
        img = img.crop(bbox)

    OUT.mkdir(exist_ok=True)

    for name, mode in (("logotipo", "color"), ("logotipo-blanco", "blanco")):
        out_img = img
        if mode == "blanco":
            out_img = img.convert("RGBA")
            r, g, b, a_ch = out_img.split()
            blanco = Image.new("L", img.size, 255)
            out_img = Image.merge("RGBA", (blanco, blanco, blanco, a_ch))

        base = out_img
        for ext, kwargs in (("png", {"optimize": True}),
                            ("webp", {"quality": 88, "method": 6})):
            target = OUT / f"{name}.{ext}"
            base.save(target, ext.upper(), **kwargs)
            print(f"{target.name:24} {base.width}x{base.height}  "
                  f"{target.stat().st_size / 1024:6.0f} KB")


if __name__ == "__main__":
    for job in JOBS:
        process(job)