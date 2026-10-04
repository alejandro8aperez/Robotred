"""Genera los recursos gráficos del grupo de Facebook del curso.

Salida en curso/:
  banner-facebook.png    1640x856  portada del grupo (se recorta en movil)
  avatar-facebook.png     640x640  foto del grupo (se ve a 168 px)
  modulo-01..10.png       1200x630  tarjeta por módulo, para cada publicación

Reutiliza el logotipo real (Imagenes/Logotipo.png) y la paleta de styles.css.
Los textos están listos para español y no dependen de fuentes externas.
"""

from pathlib import Path

from PIL import Image, ImageChops, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "Imagenes" / "Logotipo.png"
OUT = ROOT / "curso"

INK = "#0A1620"
NAVY_3 = "#19384A"
RED = "#D8433E"
AMBER = "#E9A93C"
WHITE = "#FFFFFF"
MUTED = "#8497A6"
DARK_TEXT = "#C6D3E0"
LINE = "#1B3242"

MODULES = [
    ("01", "Introducción a la robótica eléctrica"),
    ("02", "Conocimiento de la línea eléctrica"),
    ("03", "El robot trepador y las plataformas"),
    ("04", "Sensores para inspección"),
    ("05", "Qué puede hacer ROBOTY-RED"),
    ("06", "Inteligencia artificial en el borde"),
    ("07", "Robot para mantenimiento"),
    ("08", "Seguridad eléctrica"),
    ("09", "Diseño del primer prototipo"),
    ("10", "Proyecto final"),
]


def font(size, bold=True):
    names = ("segoeuib.ttf", "arialbd.ttf") if bold else (
        "segoeui.ttf", "arial.ttf")
    for name in names + ("segoeuib.ttf", "arialbd.ttf"):
        try:
            return ImageFont.truetype(str(Path("C:/Windows/Fonts") / name), size)
        except OSError:
            continue
    return ImageFont.load_default()


def load_trimmed():
    img = Image.open(SRC).convert("RGBA")
    alpha = img.getchannel("A")
    bbox = Image.eval(alpha, lambda v: 255 if v > 8 else 0).getbbox()
    if bbox:
        img = img.crop(bbox)
    return img


def to_white(img):
    """Conserva el canal alfa y pinta todos los pixeles de blanco."""
    alpha = img.getchannel("A")
    white = Image.new("L", img.size, 255)
    return Image.merge("RGBA", (white, white, white, alpha))


def scaled(img, height):
    w = round(img.width * height / img.height)
    return img.resize((w, height), Image.LANCZOS)


def gradient(img, top=INK, bottom=NAVY_3):
    """Rellena verticalmente el lienzo con un degradado."""
    d = ImageDraw.Draw(img)
    h = img.height
    for y in range(h):
        t = y / max(1, h - 1)
        c = tuple(int(int(top[i:i + 2], 16) * (1 - t) + int(bottom[i:i + 2], 16) * t)
                  for i in (1, 3, 5))
        d.line([(0, y), (img.width, y)], fill=c)


def grid(img, step=64, color=LINE):
    d = ImageDraw.Draw(img)
    for x in range(0, img.width, step):
        d.line([(x, 0), (x, img.height)], fill=color, width=1)
    for y in range(0, img.height, step):
        d.line([(0, y), (img.width, y)], fill=color, width=1)


def glow_overlay(img, cx, cy, radius, color=RED, strength=0.30):
    """Capa de resplandor radial, para combinar con ImageChops.screen."""
    overlay = Image.new("RGB", img.size, (0, 0, 0))
    od = ImageDraw.Draw(overlay)
    steps = 44
    for i in range(steps, 0, -1):
        t = i / steps
        r = radius * t
        a = (1 - t) ** 2 * strength
        c = tuple(int(int(color[i:i + 2], 16) * a) for i in (1, 3, 5))
        od.ellipse([cx - r, cy - r, cx + r, cy + r], fill=c)
    return overlay


def text_width(d, s, f):
    box = d.textbbox((0, 0), s, font=f)
    return box[2] - box[0]


def wrap(d, s, f, max_w):
    """Parte un texto en lineas que caben en max_w."""
    words, lines, cur = s.split(), [], ""
    for w in words:
        probe = f"{cur} {w}".strip()
        if text_width(d, probe, f) <= max_w or not cur:
            cur = probe
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def build_banner(base):
    W, H = 1640, 856
    img = Image.new("RGB", (W, H), INK)
    gradient(img)
    grid(img, step=64)
    img = ImageChops.screen(img.convert("RGB"), glow_overlay(img, int(W * 0.72), int(H * 0.30),
                                               520, RED, 0.42))

    d = ImageDraw.Draw(img)

    # El logotipo no debe quedar en la zona que Facebook recorta en movil:
    # se mantiene a la izquierda, dentro del area segura.
    logo = to_white(scaled(base, 150))
    img.paste(logo, (150, 120), logo)

    d.text((150, 330), "GRUPO ABIERTO DE", font=font(30, bold=False), fill=MUTED)
    d.text((146, 372), "ROBOTY-RED", font=font(104), fill=WHITE)
    d.text((150, 502), "Robótica para el mantenimiento de redes",
           font=font(42, bold=False), fill=DARK_TEXT)
    d.text((150, 552), "de transmisión y distribución",
           font=font(42, bold=False), fill=DARK_TEXT)

    d.rectangle([150, 640, 420, 648], fill=RED)
    d.text((150, 686), "Curso en 10 módulos · IEC/TC 129 · En español",
           font=font(28, bold=False), fill=AMBER)

    OUT.mkdir(exist_ok=True)
    p = OUT / "banner-facebook.png"
    img.save(p, "PNG", optimize=True)
    print(f"{p.name:24} {W}x{H}  {p.stat().st_size / 1024:6.0f} KB")


def build_avatar(base):
    S = 640
    img = Image.new("RGB", (S, S), INK)
    gradient(img, top=NAVY_3, bottom=INK)
    img = ImageChops.screen(img.convert("RGB"), glow_overlay(img, S // 2, S // 2, S * 0.62,
                                               RED, 0.34))
    d = ImageDraw.Draw(img)

    # Anillo exterior: el hexagono de la marca.
    cx = cy = S // 2
    r = 232
    hexa = [(cx + r * 0.866 * (2 * ((i + 0.5) % 6) / 3 - 1),
             cy - r * 0.5 + r * (i % 2)) for i in range(6)]
    # pts anteriores no forman un hexagono regular; se calcula por angulo.
    import math
    hexa = [(cx + r * math.cos(math.radians(60 * i - 30)),
             cy + r * math.sin(math.radians(60 * i - 30))) for i in range(6)]
    d.polygon(hexa, outline=RED, width=10)

    logo = to_white(scaled(base, 250))
    img.paste(logo, ((S - logo.width) // 2, (S - logo.height) // 2 - 18), logo)

    d.text((cx, 500), "TUTORIAL", font=font(58), fill=WHITE, anchor="ma")

    p = OUT / "avatar-facebook.png"
    img.save(p, "PNG", optimize=True)
    print(f"{p.name:24} {S}x{S}  {p.stat().st_size / 1024:6.0f} KB")


def build_module_cards(base):
    """Una tarjeta por módulo, lista para cada publicación del grupo."""
    W, H = 1200, 630
    for num, title in MODULES:
        img = Image.new("RGB", (W, H), INK)
        gradient(img)
        grid(img, step=60)
        img = ImageChops.screen(img.convert("RGB"),
                           glow_overlay(img, int(W * 0.84), int(H * 0.22), 460, RED, 0.38))
        d = ImageDraw.Draw(img)

        logo = to_white(scaled(base, 78))
        img.paste(logo, (74, 74), logo)

        d.text((74, 176), "ROBOTY-RED", font=font(22, bold=False), fill=MUTED)
        d.text((74, 208), "TUTORIAL", font=font(34), fill=AMBER)

        d.text((70, 262), num, font=font(150), fill=RED)

        d.rectangle([232, 300, 330, 308], fill=RED)
        d.text((232, 336), f"MÓDULO {num}", font=font(24, bold=False), fill=MUTED)

        lines = wrap(d, title, font(50), W - 300)
        y = 386
        for ln in lines[:2]:
            d.text((232, y), ln, font=font(50), fill=WHITE)
            y += 62

        d.text((232, 520), "Robótica para el mantenimiento de redes",
               font=font(24, bold=False), fill=DARK_TEXT)
        d.text((232, 556), "robotred.co/tutorial.html",
               font=font(22, bold=False), fill=MUTED)

        p = OUT / f"modulo-{num}.png"
        img.save(p, "PNG", optimize=True)
        print(f"{p.name:24} {W}x{H}  {p.stat().st_size / 1024:6.0f} KB")


def build():
    if not SRC.exists():
        print(f"[skip] no existe {SRC}")
        return
    OUT.mkdir(exist_ok=True)
    base = load_trimmed()
    build_banner(base)
    build_avatar(base)
    build_module_cards(base)


if __name__ == "__main__":
    build()
