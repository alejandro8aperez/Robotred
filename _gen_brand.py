"""Genera los derivados del logotipo: header, favicon y tarjeta social.

El original en Imagenes/Logotipo.png es un cuadrado de 1.5 MB con margen
transparente. Eso no puede ir al header, asi que aqui se recortan las variantes
que el sitio realmente necesita, cada una al tamano que se muestra.

Salida en assets/:
  logo-color.png / .webp    logotipo a color, 96 px de alto (2x del header)
  logo-blanco.png / .webp   el mismo recorte en blanco, para el header oscuro
  favicon-32.png            icono de pestana
  favicon-192.png           icono de pestana en alta
  apple-touch-icon.png      icono de iOS, 180x180 opaco
  og-image.png              tarjeta 1200x630 para redes sociales
"""

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "Imagenes" / "Logotipo.png"
OUT = ROOT / "assets"

INK = "#0A1620"
NAVY_3 = "#19384A"
WHITE = "#FFFFFF"
RED = "#D8433E"
MUTED = "#8497A6"
DARK_TEXT = "#C6D3E0"

HEADER_H = 96  # 2x de los 48 px de alto que se muestran en el header


def load_trimmed():
    img = Image.open(SRC).convert("RGBA")
    alpha = img.getchannel("A")
    bbox = Image.eval(alpha, lambda v: 255 if v > 8 else 0).getbbox()
    if bbox:
        img = img.crop(bbox)
    return img


def to_white(img):
    r, g, b, a = img.split()
    white = Image.new("L", img.size, 255)
    return Image.merge("RGBA", (white, white, white, a))


def scaled(img, height):
    w = round(img.width * height / img.height)
    return img.resize((w, height), Image.LANCZOS)


def font(size, bold=True):
    names = ("segoeuib.ttf", "arialbd.ttf") if bold else (
        "segoeui.ttf", "arial.ttf")
    for name in names + ("segoeuib.ttf", "arialbd.ttf"):
        try:
            return ImageFont.truetype(str(Path("C:/Windows/Fonts") / name), size)
        except OSError:
            continue
    return ImageFont.load_default()


def save(img, name, **kw):
    path = OUT / name
    img.save(path, path.suffix[1:].upper(), **kw)
    print(f"{name:24} {img.width}x{img.height}  {path.stat().st_size / 1024:6.0f} KB")


def square_logo(base, size, bg=None):
    """Coloca el logotipo centrado en un lienzo cuadrado."""
    canvas = Image.new("RGBA", (size, size), bg if bg else (0, 0, 0, 0))
    inner = scaled(base, round(size * 0.82))
    canvas.paste(inner, ((size - inner.width) // 2, (size - inner.height) // 2), inner)
    return canvas


def build():
    if not SRC.exists():
        print(f"[skip] no existe {SRC}")
        return

    OUT.mkdir(exist_ok=True)
    base = load_trimmed()

    color = scaled(base, HEADER_H)
    save(color, "logo-color.png", optimize=True)
    save(color, "logo-color.webp", quality=92, method=6)

    white = to_white(color)
    save(white, "logo-blanco.png", optimize=True)
    save(white, "logo-blanco.webp", quality=92, method=6)

    for size in (32, 192):
        save(square_logo(base, size), f"favicon-{size}.png", optimize=True)

    save(square_logo(base, 180), "apple-touch-icon.png", optimize=True)

    build_og(base)


def build_og(base):
    W, H = 1200, 630
    img = Image.new("RGB", (W, H), INK)
    d = ImageDraw.Draw(img)

    for y in range(H):
        t = y / H
        c = tuple(
            int(int(INK[i:i + 2], 16) * (1 - t) + int(NAVY_3[i:i + 2], 16) * t)
            for i in (1, 3, 5)
        )
        d.line([(0, y), (W, y)], fill=c)

    for gx in range(0, W, 60):
        d.line([(gx, 0), (gx, H)], fill="#1B3242", width=1)
    for gy in range(0, H, 60):
        d.line([(0, gy), (W, gy)], fill="#1B3242", width=1)

    logo = to_white(scaled(base, 150))
    img.paste(logo, (90, 84), logo)

    d.text((90, 300), "Robótica e ingeniería para", font=font(40), fill=WHITE)
    d.text((90, 350), "el mantenimiento de redes eléctricas",
           font=font(40), fill=WHITE)

    d.rectangle([90, 434, 300, 442], fill=RED)

    d.text((90, 486), "Inspección autónoma · Termografía radiométrica · "
                      "Mantenimiento en línea", font=font(23, bold=False),
           fill=DARK_TEXT)
    d.text((90, 540), "robotred.co", font=font(24, bold=False), fill=MUTED)

    out = OUT / "og-image.png"
    img.save(out, "PNG", optimize=True)
    print(f"{'og-image.png':24} {W}x{H}  {out.stat().st_size / 1024:6.0f} KB")


if __name__ == "__main__":
    build()