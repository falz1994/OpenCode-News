#!/usr/bin/env python3
"""Barrido de anchos del frame de presets.

Corre `mide-presets.js` a varios anchos de viewport y en los dos temas, y falla
si algun ancho deja problemas. Es la comprobacion que faltaba: `audita.py` mira
contraste y solapes, y `.rev/mide.js` mira el header sticky, pero ninguno
comparaba los anchos de los bloques hermanos del frame de presets (que es donde
el `max-width` sobre la caja dejaba tres anchos distintos).

Uso:  python3 barrido-presets.py
"""
import json, os, shutil, sys, tempfile, time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import audita  # noqa: E402

URL = "http://127.0.0.1:8765/index.html"
JS = open(os.path.join(HERE, "mide-presets.js"), encoding="utf-8").read()
ANCHOS = (1600, 1440, 1280, 1080, 900, 700)
TEMAS = ("oscuro", "claro")

fallos = 0
for tema in TEMAS:
    for ancho in ANCHOS:
        perfil = tempfile.mkdtemp(prefix="barrido-")
        proc, puerto = audita.arranca_chrome(perfil)
        try:
            ws = audita.WS(audita.nueva_pestania(puerto, URL))
            ws.call("Page.enable"); ws.call("Runtime.enable")
            ws.call("Emulation.setDeviceMetricsOverride",
                    {"width": ancho, "height": 1000, "deviceScaleFactor": 1, "mobile": False})
            ws.call("Page.navigate", {"url": URL}); time.sleep(3.5)
            if tema == "claro":
                ws.call("Runtime.evaluate", {"expression":
                        "document.body.classList.add('light');'ok'", "returnByValue": True})
                time.sleep(0.4)
            r = ws.call("Runtime.evaluate", {"expression": JS, "returnByValue": True})
            d = r["result"].get("value") or {}
            probs = d.get("problemas", [])
            fallos += len(probs)
            print(f"== {tema:6} {ancho:5}px · card {d.get('cajas',{}).get('card 1',{}).get('w')}px"
                  f" · sim {len((d.get('columnas',{}).get('sim') or '').split())} col"
                  f" · medidas(ch) {d.get('columnas',{}).get('medidas_ch')}")
            for p in probs:
                print("   !", p)
            if not probs:
                print("   sin problemas")
        finally:
            proc.kill(); shutil.rmtree(perfil, ignore_errors=True)

print()
print("TOTAL PROBLEMAS:", fallos)
sys.exit(1 if fallos else 0)
