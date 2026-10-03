"""Genera og-image.png (1200x630) y apple-touch-icon.png (180x180).

Dibuja el mismo logotipo del sitio (hexagono + R + punto rojo) directamente
con Pillow, para no depender de un SVG externo ni de un binario existente.
Paleta tomada de styles.css.
"""

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent

INK = "#0A1620"
NAVY_3 = "#19384A"
RED = "#D8433E"
BLUE = "#4F9FBC"
AMBER = "#E9A93C"
WHITE = "#FFFFFF"
MUTED = "#8394A3"

DISPLAY_CANDIDATES = [
    "segoeuib.ttf", "arialbd.ttf", "segoeui.ttf", "arial.ttf",
]


def font(size: int, bold: bool = True):
    names = DISPLAY_CANDIDATES if bold else DISPLAY_CANDIDATES[::-1]
    for name in names:
        try:
            return ImageFont.truetype(str(Path("C:/Windows/Fonts") / name), size)
        except OSError:
            continue
    return ImageFont.load_default()


def hexagon(draw, cx, cy, r, stroke, width):
    """Hexagono con vertice superior, equivalente al simbolo #i-logo."""
    from math import cos, pi, sin

    pts = []
    for i in range(6):
        ang = -pi / 2 + i * pi / 3
        pts.append((cx + r * cos(ang), cy + r * sin(ang)))
    draw.polygon(pts, outline=stroke, width=width)


def robot_mark(size, stroke_color, dot_color, hex_color, width_ratio=0.15):
    """Devuelve una imagen RGBA con la marca, ajustada a `size`."""
    s = size
    img = Image.new("RGBA", (s, s), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)

    hexagon(d, s * 0.48, s * 0.5, s * 0.36, hex_color, max(2, int(s * width_ratio)))

    # Trazo de la R: vertical + curva + diagonal.
    w = max(2, int(s * 0.16))
    x0, x1 = s * 0.36, s * 0.60
    y0, y1 = s * 0.34, s * 0.66
    d.line([(x0, y1), (x0, y0)], fill=stroke_color, width=w)
    d.line([(x0, y0), (x1 * 0.86, y0)], fill=stroke_color, width=w)
    d.line([(x1 * 0.86, y0), (x1, y0 + s * 0.11)], fill=stroke_color, width=w)
    d.line([(x1, y0 + s * 0.11), (x1 * 0.86, y0 + s * 0.22)], fill=stroke_color, width=w)
    d.line([(x1 * 0.86, y0 + s * 0.22), (x0, y0 + s * 0.22)], fill=stroke_color, width=w)
    d.line([(x1 * 0.70, y0 + s * 0.22), (s * 0.70, y1)], fill=stroke_color, width=w)

    r = s * 0.085
    cx, cy = s * 0.70, s * 0.66
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=dot_color)
    r2 = r * 0.34
    d.ellipse([cx - r2, cy - r2, cx + r2, cy + r2], fill=NAVY_3)

    return img


def wordmark(img, draw, x, y, size, fg):
    f = font(size)
    draw.text((x, y), "ROBOT", font=f, fill=fg)
    w_robot = draw.textlength("ROBOT", font=f)
    draw.text((x + w_robot, y), "-RED", font=font(size), fill=RED)
    return w_robot + draw.textlength("-RED", font=f)


def build_og():
    W, H = 1200, 630
    img = Image.new("RGB", (W, H), INK)
    d = ImageDraw.Draw(img)

    for y in range(H):
        t = y / H
        c = tuple(int(int(INK[i:i + 2], 16) * (1 - t) + int(NAVY_3[i:i + 2], 16) * t)
                  for i in (1, 3, 5))
        d.line([(0, y), (W, y)], fill=c)

    for gx in range(0, W, 60):
        d.line([(gx, 0), (gx, H)], fill="#1B3242", width=1)
    for gy in range(0, H, 60):
        d.line([(0, gy), (W, gy)], fill="#1B3242", width=1)

    mark = robot_mark(132, WHITE, RED, WHITE)
    img.paste(mark, (88, 96), mark)

    d.text((244, 108), "ROBOT", font=font(62), fill=WHITE)
    d.text((244 + d.textlength("ROBOT", font=font(62)), 108), "-RED",
           font=font(62), fill=RED)

    d.rectangle([88, 268, 336, 276], fill=RED)

    d.text((88, 316), "Robótica e ingeniería para", font=font(38), fill="#C6D3E0")
    d.text((88, 362), "el mantenimiento de redes eléctricas",
           font=font(38), fill="#C6D3E0")

    d.line([(88, 448), (1112, 448)], fill="#33566C", width=2)

    items = ["Inspección autónoma", "Termografía radiométrica", "Mantenimiento en línea"]
    x = 88
    for it in items:
        d.ellipse([x, 494, x + 10, 504], fill=AMBER)
        f = font(25, bold=False)
        d.text((x + 22, 484), it, font=f, fill="#8497A6")
        x += 30 + int(d.textlength(it, font=f))

    d.text((88, 552), "robotred.co", font=font(24, bold=False), fill=MUTED)

    out = ROOT / "og-image.png"
    img.save(out, "PNG", optimize=True)
    print(f"{out.name}: {W}x{H}  {out.stat().st_size / 1024:.0f} KB")


def build_touch_icon():
    S = 180
    img = Image.new("RGB", (S, S), NAVY_3)
    rounded = Image.new("L", (S * 4, S * 4), 0)
    ImageDraw.Draw(rounded).rounded_rectangle(
        [0, 0, S * 4 - 1, S * 4 - 1], radius=S * 4 * 0.22, fill=255)
    mask = rounded.resize((S, S), Image.LANCZOS)

    mark = robot_mark(120, WHITE, RED, WHITE)
    base = Image.new("RGB", (S, S), NAVY_3)
    base.paste(mark, (30, 30), mark)

    img = Image.new("RGBA", (S, S), (0, 0, 0, 0))
    img.paste(base, (0, 0), mask)

    out = ROOT / "apple-touch-icon.png"
    img.save(out, "PNG", optimize=True)
    print(f"{out.name}: {S}x{S}  {out.stat().st_size / 1024:.0f} KB")


if __name__ == "__main__":
    build_og()
    build_touch_icon()