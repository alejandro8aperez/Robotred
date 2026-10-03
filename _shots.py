"""Capturas de pantalla para revision visual. No es parte de la publicacion."""

import functools
import http.server
import socketserver
import threading
from pathlib import Path

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parent
OUT = ROOT / ".shots"
PORT = 8942

SHOTS = [
    ("index.html", "escritorio", 1440, 900, True),
    ("index.html", "tablet", 834, 1000, True),
    ("index.html", "movil", 390, 844, True),
    ("tutorial.html", "tutorial", 1440, 900, True),
    ("tutorial.html", "tutorial-movil", 390, 844, True),
    ("gracias.html", "gracias", 1280, 900, False),
]


def main():
    class Q(http.server.SimpleHTTPRequestHandler):
        def log_message(self, *a):
            pass

    h = functools.partial(Q, directory=str(ROOT))
    socketserver.TCPServer.allow_reuse_address = True
    httpd = socketserver.TCPServer(("127.0.0.1", PORT), h)
    threading.Thread(target=httpd.serve_forever, daemon=True).start()

    OUT.mkdir(exist_ok=True)

    with sync_playwright() as p:
        browser = p.chromium.launch()
        for page_name, label, w, h_, full in SHOTS:
            pg = browser.new_page(viewport={"width": w, "height": h_})
            pg.goto(f"http://127.0.0.1:{PORT}/{page_name}", wait_until="networkidle")
            pg.wait_for_timeout(900)
            if full:
                pg.evaluate(
                    "() => document.querySelectorAll('.reveal')"
                    ".forEach(e => e.classList.add('in'))"
                )
                pg.wait_for_timeout(600)
            path = OUT / f"{label}.png"
            pg.screenshot(path=str(path), full_page=full)
            print(f"{path.name:20} {path.stat().st_size / 1024:6.0f} KB")
            pg.close()
        browser.close()

    httpd.shutdown()
    print(f"\nEn {OUT}")


if __name__ == "__main__":
    main()