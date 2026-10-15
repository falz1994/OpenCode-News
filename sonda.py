#!/usr/bin/env python3
"""Sondas de layout: mide cajas y textos concretos del dashboard.

Complementa a `audita.py`: `audita.py` busca defectos automaticamente;
aqui se piden medidas concretas (una celda, un chip, un h3) para decidir
si algo esta mal alineado o recortado.

Uso:
  python3 sonda.py --url http://127.0.0.1:8765/index.html --expr cajas
  python3 sonda.py --expr h3
  python3 sonda.py --expr chips
  python3 sonda.py --expr matriz
  python3 sonda.py --expr tabla-go
  python3 sonda.py --expr raw --js "document.title"
"""
import argparse, base64, json, os, shutil, socket, subprocess, sys, tempfile, time, urllib.parse

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import audita  # noqa: E402

EXPR = {
    "h3": """[...document.querySelectorAll('.cards .card h3')].map(n=>{const r=n.getBoundingClientRect();
        return {t:n.textContent.trim(), w:Math.round(r.width), h:Math.round(r.height), sw:n.scrollWidth, cw:n.clientWidth};})""",
    "chips": """[...document.querySelectorAll('.cards .chip')].map(n=>{const r=n.getBoundingClientRect();
        return {t:n.textContent.trim(), w:Math.round(r.width), h:Math.round(r.height), sw:n.scrollWidth, cw:n.clientWidth};})""",
    "cajas": """[...document.querySelectorAll('.cards .card')].map(c=>{
        const r=c.getBoundingClientRect();
        return {titulo:(c.querySelector('h3')||{}).textContent||'', x:Math.round(r.x), y:Math.round(r.y),
                w:Math.round(r.width), h:Math.round(r.height),
                hijos:[...c.children].map(p=>{const q=p.getBoundingClientRect();
                  return {tag:p.tagName.toLowerCase(), cls:p.className, w:Math.round(q.width),
                          h:Math.round(q.height), y:Math.round(q.y), sw:p.scrollWidth, cw:p.clientWidth,
                          t:(p.textContent||'').trim().slice(0,40)};})};})""",
    "matriz": """(()=>{const th=[...document.querySelectorAll('#matriz thead th')];
        const f0=[...document.querySelectorAll('#matriz tbody tr')][0];
        return {th:th.map(n=>{const r=n.getBoundingClientRect();
                  return {t:n.textContent.trim(), w:Math.round(r.width), sw:n.scrollWidth, cw:n.clientWidth};}),
                fila0:f0?[...f0.children].map(n=>{const r=n.getBoundingClientRect();
                  return {t:n.textContent.trim().slice(0,24), w:Math.round(r.width), sw:n.scrollWidth, cw:n.clientWidth};}):[]};})()""",
    "tabla-go": """(()=>{const t=document.querySelectorAll('.wrap table')[0]; if(!t) return null;
        return {sw:t.scrollWidth, cw:t.clientWidth, wrap:[...document.querySelectorAll('.wrap')].map(w=>({sw:w.scrollWidth,cw:w.clientWidth}))};})()""",
}


def sonda(url, expr, js=None, tema="oscuro", ancho=1600, alto=1000, scroll_h2=None):
    perfil = tempfile.mkdtemp(prefix="sonda-chrome-")
    proc, puerto = audita.arranca_chrome(perfil)
    try:
        ws = audita.WS(audita.nueva_pestania(puerto, url))
        ws.call("Page.enable"); ws.call("Runtime.enable")
        ws.call("Emulation.setDeviceMetricsOverride",
                {"width": ancho, "height": alto, "deviceScaleFactor": 1, "mobile": False})
        ws.call("Page.navigate", {"url": url}); time.sleep(2.5)
        if tema == "claro":
            ws.call("Runtime.evaluate", {"expression":
                    "document.body.classList.add('light');'ok'", "returnByValue": True})
            time.sleep(0.5)
        if scroll_h2:
            ws.call("Runtime.evaluate", {"expression":
                    "(()=>{const h=[...document.querySelectorAll('main h2')].find(x=>x.textContent.includes("
                    + json.dumps(scroll_h2) + "));if(h)scrollTo(0,h.getBoundingClientRect().top+scrollY-170);return 'ok';})()",
                    "returnByValue": True})
            time.sleep(0.6)
        code = js or EXPR.get(expr)
        if not code:
            raise SystemExit("expresion desconocida: " + str(expr))
        r = ws.call("Runtime.evaluate", {"expression": code, "returnByValue": True})
        return r["result"].get("value")
    finally:
        proc.kill(); shutil.rmtree(perfil, ignore_errors=True)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--url", default="http://127.0.0.1:8765/index.html")
    ap.add_argument("--expr", default="cajas", choices=list(EXPR) + ["raw"])
    ap.add_argument("--js", default=None)
    ap.add_argument("--tema", default="oscuro", choices=["oscuro", "claro"])
    ap.add_argument("--ancho", type=int, default=1600)
    ap.add_argument("--alto", type=int, default=1000)
    ap.add_argument("--scroll-h2", default=None)
    a = ap.parse_args()
    print(json.dumps(sonda(a.url, a.expr, a.js, a.tema, a.ancho, a.alto, a.scroll_h2),
                     ensure_ascii=False, indent=1))
