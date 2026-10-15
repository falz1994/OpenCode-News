#!/usr/bin/env python3
"""Capturas dirigidas del dashboard: desplaza a un titulo y guarda el viewport.

Sirve para revisar visualmente un bloque concreto (presets, simulacion, matriz)
sin depender de una captura de pagina entera.

Uso:
  python3 captura.py --h2 "Presets de DSH" -o .rev/presets.png
  python3 captura.py --h2 "Simulación" -o .rev/sim.png --tema claro --ancho 1280
  python3 captura.py --texto "Módulos que se montan" -o .rev/modulos.png
"""
import argparse, base64, json, os, shutil, sys, tempfile, time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import audita  # noqa: E402


def captura(url, destino, h2=None, texto=None, tema="oscuro", ancho=1600, alto=1000,
            offset=170, espera=4.0, sel="main h2, main h3", full=False):
    """Espera 4 s por defecto: el dashboard pinta las secciones con JS despues de
    cargar datos.js, y con menos margen el `h2` todavia no existe cuando se
    busca. Subir la espera es mas barato que fallar la captura."""
    perfil = tempfile.mkdtemp(prefix="captura-chrome-")
    proc, puerto = audita.arranca_chrome(perfil)
    try:
        ws = audita.WS(audita.nueva_pestania(puerto, url))
        ws.call("Page.enable"); ws.call("Runtime.enable")
        ws.call("Emulation.setDeviceMetricsOverride",
                {"width": ancho, "height": alto, "deviceScaleFactor": 1, "mobile": False})
        ws.call("Page.navigate", {"url": url}); time.sleep(espera)
        if tema == "claro":
            ws.call("Runtime.evaluate", {"expression":
                    "document.body.classList.add('light');'ok'", "returnByValue": True})
            time.sleep(0.5)
        if h2 or texto:
            # Se espera a que el selector exista: el contenido lo pinta el JS.
            q = json.dumps(h2 or texto)
            for intento in range(12):
                js_busca = ("(()=>{const sel=document.querySelectorAll(%s);"
                            "const q=%s;"
                            "return [...sel].some(x=>x.textContent.includes(q));})()"
                            % (json.dumps(sel), q))
                r = ws.call("Runtime.evaluate", {"expression": js_busca, "returnByValue": True})
                if r["result"].get("value") is True:
                    break
                time.sleep(0.5)
            js = ("(()=>{const sel=document.querySelectorAll(%s);"
                  "const q=%s;"
                  "const h=[...sel].find(x=>x.textContent.includes(q));"
                  "if(!h) return 'no encontrado';"
                  "scrollTo(0,h.getBoundingClientRect().top+scrollY-%d);"
                  "return String(Math.round(scrollY));})()"
                  % (json.dumps(sel), q, offset))
            r = ws.call("Runtime.evaluate", {"expression": js, "returnByValue": True})
            if r["result"]["value"] == "no encontrado":
                raise SystemExit(f"no se encontro {h2 or texto!r} en {sel}")
            time.sleep(0.7)
        if full:
            # La pagina entera: se mide el documento y se reajusta el viewport
            # antes de capturar. Los contenedores .wrap tienen su propio scroll
            # (max-height), asi que la captura muestra su estado visible.
            r = ws.call("Runtime.evaluate", {"expression":
                        "Math.max(document.body.scrollHeight, document.documentElement.scrollHeight)",
                        "returnByValue": True})
            alto_doc = int(r["result"]["value"])
            ws.call("Emulation.setDeviceMetricsOverride",
                    {"width": ancho, "height": alto_doc, "deviceScaleFactor": 1, "mobile": False})
            time.sleep(0.8)
        shot = ws.call("Page.captureScreenshot", {"format": "png"})
        with open(destino, "wb") as f:
            f.write(base64.b64decode(shot["data"]))
        print("escrito:", destino)
    finally:
        proc.kill(); shutil.rmtree(perfil, ignore_errors=True)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--url", default="http://127.0.0.1:8765/index.html")
    ap.add_argument("--h2", default=None, help="texto del h2/h3 a encabezar")
    ap.add_argument("--texto", default=None, help="igual que --h2 (alias)")
    ap.add_argument("--sel", default="main h2, main h3",
                    help="selector donde buscar el texto (por defecto titulos)")
    ap.add_argument("-o", "--salida", required=True)
    ap.add_argument("--tema", default="oscuro", choices=["oscuro", "claro"])
    ap.add_argument("--ancho", type=int, default=1600)
    ap.add_argument("--alto", type=int, default=1000)
    ap.add_argument("--offset", type=int, default=170)
    ap.add_argument("--full", action="store_true", help="captura la pagina entera")
    a = ap.parse_args()
    captura(a.url, a.salida, a.h2, a.texto, a.tema, a.ancho, a.alto, a.offset,
            sel=a.sel, full=a.full)
