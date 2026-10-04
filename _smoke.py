"""Prueba de humo del sitio en un navegador real.

Levanta un servidor local, carga index.html, tutorial.html y gracias.html en
Chromium y comprueba: errores de consola, recursos rotos, el flujo del
formulario (relleno, validacion, envio y red de seguridad) y la navegacion
entre el indice y la pagina de tutorial.
"""

import functools
import http.server
import socketserver
import threading
from pathlib import Path

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parent
PORT = 8931

received = []


class Handler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        length = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(length).decode("utf-8", "replace")
        received.append(body)
        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        self.end_headers()
        self.wfile.write(b"OK")

    def log_message(self, *args):
        pass


def settle(page, selector, tries=40):
    """Espera a que la caja del elemento deje de moverse.

    Las transiciones de .reveal (0.7s) y el despliegue del FAQ desplazan el
    contenido; sin esta espera, Playwright juzga el boton 'inestable'.
    """
    prev, stable = None, 0
    for _ in range(tries):
        try:
            box = page.locator(selector).first.bounding_box()
        except Exception:  # noqa: BLE001
            box = None
        if box is None:
            return False
        if prev is not None and abs(box["y"] - prev[0]) < 0.01 and abs(box["height"] - prev[1]) < 0.01:
            stable += 1
            if stable >= 3:
                return True
        else:
            stable = 0
        prev = (box["y"], box["height"])
        page.wait_for_timeout(100)
    return False


def main():
    handler = functools.partial(Handler, directory=str(ROOT))
    socketserver.TCPServer.allow_reuse_address = True
    httpd = socketserver.TCPServer(("127.0.0.1", PORT), handler)
    threading.Thread(target=httpd.serve_forever, daemon=True).start()

    base = f"http://127.0.0.1:{PORT}"
    failures = []

    with sync_playwright() as p:
        browser = p.chromium.launch()

        for name, width, height in (
            ("escritorio", 1440, 900),
            ("tablet", 834, 1000),
            ("movil", 390, 844),
        ):
            page = browser.new_page(viewport={"width": width, "height": height})
            console, failed = [], []
            page.on("console", lambda m: console.append(f"{m.type}: {m.text}")
                    if m.type == "error" else None)
            page.on("pageerror", lambda e: console.append(f"pageerror: {e}"))
            page.on("requestfailed", lambda r: failed.append(r.url))
            page.on("response", lambda r: failed.append(f"{r.status} {r.url}")
                    if r.status >= 400 else None)

            page.goto(f"{base}/index.html", wait_until="networkidle")
            page.wait_for_timeout(600)

            print(f"\n--- {name} {width}x{height} ---")
            print("titulo:", page.title())

            # Menú de navegación
            if width <= 1024:
                toggle = page.locator("#navToggle")
                toggle.click()
                page.wait_for_timeout(400)
                opened = page.evaluate("document.getElementById('nav').classList.contains('open')")
                aria = page.locator("#navToggle").get_attribute("aria-expanded")
                print("menu movil se abre:", opened, "| aria-expanded:", aria)
                if not opened or aria != "true":
                    failures.append(f"[{name}] el menú móvil no se abre")
                page.keyboard.press("Escape")
                page.wait_for_timeout(400)
                still = page.evaluate("document.getElementById('nav').classList.contains('open')")
                locked = page.evaluate("document.body.style.overflow")
                print("Escape cierra:", not still, "| body overflow:", repr(locked))
                if still or locked:
                    failures.append(f"[{name}] Escape no cierra el menú")

            # Enlaces internos rotos
            broken = page.evaluate(
                """() => [...document.querySelectorAll('a[href^="#"]')]
                     .map(a => a.getAttribute('href').slice(1))
                     .filter(id => id && !document.getElementById(id))"""
            )
            print("anclas rotas:", broken or "ninguna")
            if broken:
                failures.append(f"[{name}] anclas rotas: {broken}")

            # FAQ
            faq = page.locator(".faq-q").first
            faq.click()
            page.wait_for_timeout(250)
            print("FAQ abre:", page.locator(".faq-a").first.is_visible())
            if not page.locator(".faq-a").first.is_visible():
                failures.append(f"[{name}] el FAQ no se abre")

            # Validación: enviar vacío
            page.locator("#formSubmit").scroll_into_view_if_needed()
            settle(page, "#formSubmit")
            page.locator("#formSubmit").click()
            page.wait_for_timeout(300)
            invalids = page.locator(".field.invalid").count()
            print("campos marcados como invalidos al enviar vacio:", invalids)
            if invalids < 4:
                failures.append(f"[{name}] la validacion no marcó los campos obligatorios")

            # Relleno y envío
            page.fill("#nombre", "Ana Restrepo")
            page.fill("#empresa", "Operador de red de prueba")
            page.fill("#email", "ana@ejemplo.co")
            page.fill("#telefono", "+57 300 000 0000")
            page.select_option("#tipo", "Piloto de inspección")
            page.select_option("#red", "Transmisión")
            page.fill("#mensaje", "Tramo de prueba de 4 km en 230 kV.")

            settle(page, "#formSubmit")
            with page.expect_navigation(wait_until="domcontentloaded"):
                page.locator("#formSubmit").click()

            print("url tras enviar:", page.url)
            if "gracias" not in page.url:
                failures.append(f"[{name}] el envio no llego a la pagina de gracias")
            print("titulo pagina de gracias:", page.title())

            if console:
                print("errores de consola:", console)
                failures.extend(f"[{name}] consola: {c}" for c in console)

            external = [u for u in failed if "127.0.0.1" not in u
                        and "fonts.g" not in u and "github" not in u]
            http_fail = [u for u in failed if u.startswith(("4", "5"))]
            print("recursos locales con error:", http_fail or "ninguno")
            if http_fail:
                failures.append(f"[{name}] recursos rotos: {http_fail}")
            print("fallos externos (red bloqueada en test):", len(external))

            page.close()

        # --- UTM y honeypot ---
        print("\n--- UTM y honeypot ---")
        page = browser.new_page(viewport={"width": 1280, "height": 900})
        page.goto(f"{base}/index.html?utm_source=linkedin&utm_campaign=prensa"
                  "&utm_medium=redes&pagina=prueba#contacto",
                  wait_until="networkidle")
        page.wait_for_timeout(400)
        utm = page.evaluate(
            """() => ['utm_source','utm_medium','utm_campaign','pagina']
                 .map(k => k + '=' + document.getElementById(k).value)"""
        )
        print("  capturados:", utm)
        if "utm_source=linkedin" not in utm or "utm_campaign=prensa" not in utm:
            failures.append("los parámetros UTM no se capturan")
        if "pagina=/index.html#contacto" not in utm:
            failures.append(f"la página de origen no se captura: {utm}")

        # El honeypot debe impedir el envío sin afectar al usuario real.
        before = len(received)
        page.fill("#nombre", "Bot")
        page.fill("#empresa", "Spam SA")
        page.fill("#email", "bot@spam.co")
        page.select_option("#tipo", "Cotización de servicio")
        page.fill("#mensaje", "Mensaje de bot.")
        page.evaluate("""() => {
            document.querySelector('[name="bot-field"]').value = 'llenado'; }""")
        page.locator("#formSubmit").scroll_into_view_if_needed()
        settle(page, "#formSubmit")
        page.locator("#formSubmit").click(force=True)
        page.wait_for_timeout(700)
        print("  envíos con honeypot lleno:", len(received) - before, "(debe ser 0)")
        if len(received) != before:
            failures.append("el honeypot no bloqueó un envío de bot")
        page.close()

        # --- TUTORIAL: la pagina nueva debe cargar limpia y enlazar al programa ---
        print("\n--- tutorial.html ---")
        for label, width, height in (("escritorio", 1440, 900), ("movil", 390, 844)):
            page = browser.new_page(viewport={"width": width, "height": height})
            console, failed = [], []
            page.on("console", lambda m: console.append(f"{m.type}: {m.text}")
                    if m.type == "error" else None)
            page.on("pageerror", lambda e: console.append(f"pageerror: {e}"))
            page.on("response", lambda r: failed.append(f"{r.status} {r.url}")
                    if r.status >= 400 else None)

            page.goto(f"{base}/tutorial.html", wait_until="networkidle")
            page.wait_for_timeout(600)

            print(f"[{label}] titulo:", page.title())

            broken = page.evaluate(
                """() => [...document.querySelectorAll('a[href^="#"]')]
                     .map(a => a.getAttribute('href').slice(1))
                     .filter(id => id && !document.getElementById(id))"""
            )
            print(f"[{label}] anclas rotas:", broken or "ninguna")
            if broken:
                failures.append(f"[tutorial/{label}] anclas rotas: {broken}")

            mods = page.locator(".mod").count()
            states = page.locator(".mod-state.published").count()
            print(f"[{label}] modulos:", mods, "| publicados:", states)
            if mods != 10:
                failures.append(f"[tutorial/{label}] se esperaban 10 modulos, hay {mods}")

            # El enlace del menu debe quedar resaltado aunque no haya ancla local.
            active = page.evaluate(
                """() => { const a = document.querySelector('#nav a.active');
                          return a ? a.getAttribute('href') : null; }"""
            )
            print(f"[{label}] enlace activo del menu:", active)
            if active != "tutorial.html":
                failures.append(f"[tutorial/{label}] el menu no resalta Tutorial: {active}")

            # Navegacion desde el indice hacia el tutorial y de vuelta.
            if label == "escritorio":
                page.goto(f"{base}/index.html#tutorial", wait_until="networkidle")
                page.wait_for_timeout(400)
                settle(page, ".tut-teaser")
                page.click(".tut-teaser", position={"x": 30, "y": 30})
                page.wait_for_load_state("networkidle")
                print("[escritorio] url tras pulsar la banda:", page.url)
                if "tutorial" not in page.url:
                    failures.append("[tutorial] la banda del indice no lleva al tutorial")

                # El enlace del menu del indice tambien debe llegar.
                page.goto(f"{base}/index.html", wait_until="networkidle")
                page.click('#nav a[href="tutorial.html"]')
                page.wait_for_load_state("networkidle")
                print("[escritorio] url tras el menu:", page.url)
                if "tutorial" not in page.url:
                    failures.append("[tutorial] el enlace del menu no lleva al tutorial")

            if console:
                print(f"[{label}] errores de consola:", console)
                failures.extend(f"[tutorial/{label}] consola: {c}" for c in console)
            http_fail = [u for u in failed if "127.0.0.1" in u or u.startswith(("4", "5"))]
            print(f"[{label}] recursos con error:", http_fail or "ninguno")
            if http_fail:
                failures.append(f"[tutorial/{label}] recursos rotos: {http_fail}")

            page.close()

        # --- CURSO: indice y las 10 lecciones deben cargar limpias ---
        print("\n--- curso/ ---")
        lecciones = ["curso/index.html"] + [
            f"curso/modulo-{n:02d}.html" for n in range(1, 11)]

        for label, width, height in (("escritorio", 1440, 900), ("movil", 390, 844)):
            for ruta in lecciones:
                page = browser.new_page(viewport={"width": width, "height": height})
                console, failed = [], []
                page.on("console", lambda m: console.append(f"{m.type}: {m.text}")
                        if m.type == "error" else None)
                page.on("pageerror", lambda e: console.append(f"pageerror: {e}"))
                page.on("response", lambda r: failed.append(f"{r.status} {r.url}")
                        if r.status >= 400 else None)

                page.goto(f"{base}/{ruta}", wait_until="networkidle")
                page.wait_for_timeout(400)

                titulo = page.title()
                corto = titulo[:60]

                # Iconos: ningun <use> puede quedar sin <symbol>.
                huerfanos = page.evaluate(
                    """() => [...document.querySelectorAll('use')]
                         .map(u => u.getAttribute('href').slice(1))
                         .filter(id => !document.getElementById(id))"""
                )
                # Tablas: no deben desbordar su contenedor.
                desbordan = page.evaluate(
                    """() => [...document.querySelectorAll('.table-wrap')]
                         .filter(d => d.scrollWidth > d.clientWidth + 2)
                         .length"""
                )

                nav_ok = page.evaluate(
                    """() => { const a = document.querySelector('#nav a.active');
                              return a ? a.getAttribute('href') : null; }"""
                )
                if nav_ok != "index.html":
                    failures.append(
                        f"[curso/{label}] {ruta}: el menu no resalta Curso: {nav_ok}")

                if huerfanos:
                    failures.append(f"[curso/{label}] {ruta}: iconos sin symbol: {huerfanos}")
                if console:
                    failures.extend(f"[curso/{label}] {ruta} consola: {c}" for c in console)
                http_fail = [u for u in failed if "127.0.0.1" in u or u.startswith(("4", "5"))]
                if http_fail:
                    failures.append(f"[curso/{label}] {ruta} recursos rotos: {http_fail}")
                # Cada pagina debe traer su propio titulo, no el de otra.
                if not titulo or titulo.startswith("{") or titulo.endswith("}"):
                    failures.append(f"[curso/{label}] {ruta}: titulo sin rellenar")
                elif ruta.endswith("index.html"):
                    if "Curso de robótica" not in titulo:
                        failures.append(f"[curso/{label}] {ruta}: titulo '{corto}'")
                else:
                    num = ruta[-7:-5]
                    if not titulo.startswith(f"Módulo {num} —"):
                        failures.append(f"[curso/{label}] {ruta}: titulo '{corto}'")
                    if not titulo.endswith("ROBOTY-RED"):
                        failures.append(f"[curso/{label}] {ruta}: titulo sin la marca")

                if ruta.endswith("index.html") or label == "escritorio":
                    print(f"[{label}] {ruta:26} | {corto}")
                    print(f"           tablas que desbordan: {desbordan} | huerfanos: {huerfanos or 'ninguno'}")

                page.close()

        # Navegacion real: indice -> leccion 1 -> leccion 2.
        print("\n--- navegacion del curso ---")
        page = browser.new_page(viewport={"width": 1440, "height": 900})
        page.goto(f"{base}/curso/index.html", wait_until="networkidle")
        page.click('a[href="modulo-01.html"]')
        page.wait_for_load_state("networkidle")
        print("indice -> modulo 1:", page.url)
        if not page.url.endswith("modulo-01.html"):
            failures.append("[curso] el indice no lleva al modulo 1")

        # La navegacion interna del modulo 1 avanza al 2.
        page.click('.leccion-nav a[href="modulo-02.html"]')
        page.wait_for_load_state("networkidle")
        print("modulo 1 -> siguiente:", page.url)
        if not page.url.endswith("modulo-02.html"):
            failures.append("[curso] el boton 'siguiente' del modulo 1 no lleva al 2")

        # Y la leccion 10 vuelve al tutorial.
        page.goto(f"{base}/curso/modulo-10.html", wait_until="networkidle")
        page.click('.leccion-nav a[href="../tutorial.html"]')
        page.wait_for_load_state("networkidle")
        print("modulo 10 -> tutorial:", page.url)
        if "tutorial" not in page.url:
            failures.append("[curso] el final del curso no lleva al tutorial")
        page.close()

        browser.close()

    httpd.shutdown()

    print("\n== CUERPO RECIBIDO POR EL SERVIDOR ==")
    for body in received:
        for pair in body.split("&"):
            k, _, v = pair.partition("=")
            from urllib.parse import unquote_plus
            print(f"  {k:14} = {unquote_plus(v)}")

    print()
    if failures:
        print("FALLOS (%d):" % len(failures))
        for f in failures:
            print("  -", f)
        raise SystemExit(1)
    print("Todo correcto.")


if __name__ == "__main__":
    main()