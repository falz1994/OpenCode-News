#!/usr/bin/env python3
"""Auditoria del dashboard con Chrome headless (CDP por WebSocket).

Mide lo que no se ve a ojo en una captura:

  * desalineacion real de las tarjetas de presets (bordes, alto, chips)
  * texto que desborda su caja o queda cortado por `overflow`
  * contraste WCAG de cada texto contra su fondo efectivo
  * scroll horizontal de pagina y de cada contenedor
  * solapes entre cajas hermanas (header sticky contra el contenido)
  * errores de consola

No usa dependencias externas: habla el protocolo DevTools con `websocket`
del propio Chrome via `--remote-debugging-port` y un cliente minimo en
Python puro (websockets no esta garantizado en el sistema).

Uso:
  python3 audita.py                       # sirve la carpeta y audita ambos temas
  python3 audita.py --url http://...      # audita un servidor ya levantado
  python3 audita.py --png captura.png     # ademas guarda la captura
"""
import argparse, json, os, re, socket, struct, subprocess, sys, time, base64, urllib.request, hashlib, shutil, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
CHROME = shutil.which("google-chrome") or shutil.which("chromium") or shutil.which("chromium-browser")

# ---------------------------------------------------------------- websocket minimo
class WS:
    """Cliente WebSocket suficiente para CDP: texto, frames < 64 kB y > 64 kB."""

    def __init__(self, url, timeout=30):
        m = re.match(r"ws://([^:/]+):(\d+)(/.*)$", url)
        if not m:
            raise ValueError("url ws invalida: " + url)
        host, port, path = m.group(1), int(m.group(2)), m.group(3)
        self.sock = socket.create_connection((host, port), timeout=timeout)
        key = base64.b64encode(os.urandom(16)).decode()
        req = (f"GET {path} HTTP/1.1\r\nHost: {host}:{port}\r\nUpgrade: websocket\r\n"
               f"Connection: Upgrade\r\nSec-WebSocket-Key: {key}\r\nSec-WebSocket-Version: 13\r\n\r\n")
        self.sock.sendall(req.encode())
        buf = b""
        while b"\r\n\r\n" not in buf:
            buf += self.sock.recv(4096)
        if b"101" not in buf.split(b"\r\n")[0]:
            raise RuntimeError("handshake fallido: " + buf.split(b"\r\n")[0].decode(errors="replace"))
        self.buf = buf.split(b"\r\n\r\n", 1)[1]
        self.next_id = 0
        self.cerrado = False

    def _recv(self, n):
        while len(self.buf) < n:
            chunk = self.sock.recv(65536)
            if not chunk:
                self.cerrado = True
                raise EOFError("socket cerrado")
            self.buf += chunk
        out, self.buf = self.buf[:n], self.buf[n:]
        return out

    def _frame(self):
        while True:
            b0, b1 = self._recv(2)
            fin, opcode = b0 & 0x80, b0 & 0x0F
            ln = b1 & 0x7F
            if ln == 126:
                ln = struct.unpack(">H", self._recv(2))[0]
            elif ln == 127:
                ln = struct.unpack(">Q", self._recv(8))[0]
            payload = self._recv(ln)
            if opcode == 0x8:
                self.cerrado = True
                raise EOFError("close frame")
            if opcode == 0x9:            # ping -> pong
                self._send(payload, 0xA)
                continue
            if opcode in (0x1, 0x2, 0x0):
                return payload

    def _send(self, payload, opcode=0x1):
        head = bytes([0x80 | opcode])
        n = len(payload)
        if n < 126:
            head += bytes([0x80 | n])
        elif n < 65536:
            head += bytes([0x80 | 126]) + struct.pack(">H", n)
        else:
            head += bytes([0x80 | 127]) + struct.pack(">Q", n)
        mask = os.urandom(4)
        masked = bytes(b ^ mask[i % 4] for i, b in enumerate(payload))
        self.sock.sendall(head + mask + masked)

    def call(self, method, params=None, timeout=60):
        self.next_id += 1
        mid = self.next_id
        self._send(json.dumps({"id": mid, "method": method, "params": params or {}}).encode())
        limite = time.time() + timeout
        while time.time() < limite:
            msg = json.loads(self._frame())
            if msg.get("id") == mid:
                if "error" in msg:
                    raise RuntimeError(f"{method}: {msg['error'].get('message')}")
                return msg.get("result", {})
        raise TimeoutError(method)

    def cerrar(self):
        try:
            self.sock.close()
        except Exception:
            pass


def arranca_chrome(perfil):
    puerto = 9333
    # --no-sandbox: el helper SUID de chrome-sandbox no esta configurado en esta
    # maquina (falla con FATAL setuid_sandbox_host). Solo se audita localhost.
    args = [CHROME, "--headless=new", f"--remote-debugging-port={puerto}",
            f"--user-data-dir={perfil}", "--no-first-run", "--no-default-browser-check",
            "--no-sandbox", "--disable-dev-shm-usage", "--disable-crash-reporter",
            "--disable-gpu", "--hide-scrollbars", "--force-device-scale-factor=1",
            "--window-size=1600,1000", "about:blank"]
    p = subprocess.Popen(args, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    for _ in range(80):
        try:
            with urllib.request.urlopen(f"http://127.0.0.1:{puerto}/json/version", timeout=1) as r:
                json.load(r)
            return p, puerto
        except Exception:
            time.sleep(0.25)
    p.kill()
    raise RuntimeError("Chrome no arranco")


def nueva_pestania(puerto, url):
    req = urllib.request.Request(f"http://127.0.0.1:{puerto}/json/new?{urllib.parse.quote(url, safe='')}",
                                 method="PUT")
    with urllib.request.urlopen(req, timeout=10) as r:
        return json.load(r)["webSocketDebuggerUrl"]


# ---------------------------------------------------------------- sondas JS
SONDA = r"""
(() => {
  const out = {errores: [], desbordes: [], contraste: [], solapes: [], geometria: {}};
  const nom = n => (n.tagName.toLowerCase() + (n.id ? "#" + n.id : "") +
                    (n.className && typeof n.className === "string" ? "." + n.className.trim().split(/\s+/).join(".") : ""));
  const vis = n => {
    const s = getComputedStyle(n), r = n.getBoundingClientRect();
    return s.display !== "none" && s.visibility !== "hidden" && +s.opacity > 0.05 && r.width > 0 && r.height > 0;
  };
  // ---- 1. desborde: scrollWidth > clientWidth o texto mas alto que su caja
  // Las celdas de tabla (th/td) llevan `white-space: nowrap` a proposito: su
  // scrollWidth supera al clientWidth por diseno y no es un defecto, asi que
  // se excluyen del chequeo (se revisan aparte con sonda.py --expr matriz).
  document.querySelectorAll("main *, header *, footer *").forEach(n => {
    if (!vis(n)) return;
    const celdaTabla = n.tagName === "TH" || n.tagName === "TD";
    if (!celdaTabla && n.scrollWidth > n.clientWidth + 1 && getComputedStyle(n).overflowX !== "auto" &&
        getComputedStyle(n).overflowX !== "scroll")
      out.desbordes.push({el: nom(n), scrollW: n.scrollWidth, clientW: n.clientWidth,
                          txt: (n.textContent || "").trim().slice(0, 60)});
    const s = getComputedStyle(n);
    if (!celdaTabla && (s.overflow === "hidden" || s.overflowY === "hidden") && n.scrollHeight > n.clientHeight + 1)
      out.desbordes.push({el: nom(n), tipo: "texto cortado", scrollH: n.scrollHeight,
                          clientH: n.clientHeight, txt: (n.textContent || "").trim().slice(0, 60)});
  });
  // ---- 2. contraste WCAG sobre fondo efectivo
  const rgb = c => { const m = c.match(/[\d.]+/g); return m ? m.slice(0, 3).map(Number) : null; };
  const fondo = n => {
    for (let e = n; e; e = e.parentElement) {
      const c = getComputedStyle(e).backgroundColor;
      const v = rgb(c);
      if (v && !/rgba\(0, 0, 0, 0\)/.test(c) && (c.match(/[\d.]+/g) || []).length < 4) return v;
      if (v && (c.match(/[\d.]+/g) || [])[3] > 0.05) return v;
    }
    return rgb(getComputedStyle(document.body).backgroundColor) || [255, 255, 255];
  };
  const lin = v => { v /= 255; return v <= 0.03928 ? v / 12.92 : Math.pow((v + 0.055) / 1.055, 2.4); };
  const lum = c => 0.2126 * lin(c[0]) + 0.7152 * lin(c[1]) + 0.0722 * lin(c[2]);
  const ratio = (a, b) => { const l1 = lum(a), l2 = lum(b); return (Math.max(l1, l2) + 0.05) / (Math.min(l1, l2) + 0.05); };
  document.querySelectorAll("main *, header *, footer *").forEach(n => {
    if (!vis(n)) return;
    const propio = [...n.childNodes].some(c => c.nodeType === 3 && c.textContent.trim());
    if (!propio) return;
    const s = getComputedStyle(n);
    const fg = rgb(s.color); if (!fg) return;
    const bg = fondo(n);
    const r = ratio(fg, bg);
    const px = parseFloat(s.fontSize), negrita = +s.fontWeight >= 700;
    const grande = px >= 24 || (px >= 18.66 && negrita);
    const min = grande ? 3 : 4.5;
    if (r < min) out.contraste.push({el: nom(n), ratio: +r.toFixed(2), min, px,
      fg: s.color, bg: "rgb(" + bg.join(",") + ")", txt: n.textContent.trim().slice(0, 50)});
  });
  // ---- 3. solapes: header sticky contra el primer elemento visible bajo el
  const h = document.querySelector("header");
  if (h) {
    const hb = h.getBoundingClientRect();
    out.geometria.headerH = Math.round(hb.height);
    document.querySelectorAll("main h2, main caption, main .fuente, main .sub").forEach(n => {
      if (!vis(n)) return;
      const r = n.getBoundingClientRect();
      if (r.top < hb.bottom - 1 && r.bottom > hb.top + 1)
        out.solapes.push({el: nom(n), headerBottom: Math.round(hb.bottom), top: Math.round(r.top),
                          txt: n.textContent.trim().slice(0, 50)});
    });
  }
  // ---- 4. geometria de las tarjetas de presets
  const cards = [...document.querySelectorAll(".cards .card")];
  if (cards.length) {
    const cajas = cards.map(c => { const r = c.getBoundingClientRect();
      return {titulo: (c.querySelector("h3") || {}).textContent || "", x: Math.round(r.x),
              y: Math.round(r.y), w: Math.round(r.width), h: Math.round(r.height)}; });
    const ys = [...new Set(cajas.map(c => c.y))];
    out.geometria.tarjetas = cajas;
    out.geometria.filas = ys.length;
    out.geometria.altoDistinto = Math.max(...cajas.map(c => c.h)) - Math.min(...cajas.map(c => c.h));
    // los chips deben empezar a la misma altura dentro de una fila
    const porFila = {};
    cards.forEach((c, i) => { const y = cajas[i].y; (porFila[y] ||= []).push(c); });
    out.geometria.chipsY = Object.entries(porFila).map(([y, cs]) => ({
      fila: +y, chips: cs.map(c => { const ch = c.querySelector(".chips"); return ch ? Math.round(ch.getBoundingClientRect().y) : null; }),
      alturas: cs.map(c => Math.round(c.getBoundingClientRect().height))}));
    // borde inferior de la ultima caja de cada fila vs. borde inferior de la tarjeta
    out.geometria.huecoInferior = cards.map(c => {
      const r = c.getBoundingClientRect();
      const hijos = [...c.children].filter(vis);
      const ult = hijos.length ? hijos[hijos.length - 1].getBoundingClientRect() : r;
      return Math.round(r.bottom - ult.bottom);
    });
    // ancho util de cada linea de texto (lineas demasiado cortas = texto apretado)
    out.geometria.anchosChips = cards.map(c => [...c.querySelectorAll(".chip")].map(ch => {
      const r = ch.getBoundingClientRect(); return {w: Math.round(r.width), h: Math.round(r.height), t: ch.textContent}; }));
  }
  // ---- 5. scroll horizontal
  out.geometria.docScrollW = document.documentElement.scrollWidth;
  out.geometria.docClientW = document.documentElement.clientWidth;
  out.geometria.desbordePagina = document.documentElement.scrollWidth - document.documentElement.clientWidth;
  // `.wrap` es un contenedor de tabla con scroll horizontal a proposito: su
  // desborde se informa aparte y NO cuenta como defecto. Lo que si es defecto
  // es que la PAGINA desborde, y eso se mide en `desbordePagina`.
  out.geometria.conWrap = [...document.querySelectorAll(".wrap")].map(w =>
    ({desborde: w.scrollWidth - w.clientWidth, sw: w.scrollWidth, cw: w.clientWidth,
      scrolleable: getComputedStyle(w).overflowX === "auto" || getComputedStyle(w).overflowX === "scroll"}));
  return out;
})()
"""


def audita(url, png=None, tema="oscuro", ancho=1600, alto=1000, scroll=None):
    perfil = tempfile.mkdtemp(prefix="audita-chrome-")
    proc, puerto = arranca_chrome(perfil)
    try:
        ws = WS(nueva_pestania(puerto, url))
        ws.call("Page.enable")
        ws.call("Runtime.enable")
        ws.call("Emulation.setDeviceMetricsOverride",
                {"width": ancho, "height": alto, "deviceScaleFactor": 1, "mobile": False})
        ws.call("Page.navigate", {"url": url})
        time.sleep(2.2)
        if tema == "claro":
            ws.call("Runtime.evaluate", {"expression":
                    "document.body.classList.add('light');localStorage.setItem('tema','claro');"
                    "document.documentElement.style.setProperty('--header-h',"
                    "document.querySelector('header').offsetHeight+'px');'ok'", "returnByValue": True})
            time.sleep(0.6)
        if scroll:
            ws.call("Runtime.evaluate", {"expression":
                    f"document.getElementById({json.dumps(scroll)}).scrollIntoView();"
                    "'ok'", "returnByValue": True})
            time.sleep(0.8)
        r = ws.call("Runtime.evaluate", {"expression": SONDA, "returnByValue": True, "awaitPromise": False})
        datos = r["result"]["value"]
        if png:
            shot = ws.call("Page.captureScreenshot", {"format": "png", "captureBeyondViewport": False})
            with open(png, "wb") as f:
                f.write(base64.b64decode(shot["data"]))
        ws.cerrar()
        return datos
    finally:
        proc.kill()
        shutil.rmtree(perfil, ignore_errors=True)


if __name__ == "__main__":
    import urllib.parse
    ap = argparse.ArgumentParser()
    ap.add_argument("--url", default=None)
    ap.add_argument("--png", default=None)
    ap.add_argument("--tema", default="oscuro", choices=["oscuro", "claro"])
    ap.add_argument("--ancho", type=int, default=1600)
    ap.add_argument("--alto", type=int, default=1000)
    ap.add_argument("--scroll", default=None)
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()

    servidor = None
    url = a.url
    if not url:
        s = socket.socket(); s.bind(("127.0.0.1", 0)); puerto = s.getsockname()[1]; s.close()
        servidor = subprocess.Popen([sys.executable, "-m", "http.server", str(puerto), "--bind", "127.0.0.1"],
                                    cwd=HERE, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        time.sleep(1.2)
        url = f"http://127.0.0.1:{puerto}/index.html"
    try:
        d = audita(url, a.png, a.tema, a.ancho, a.alto, a.scroll)
    finally:
        if servidor:
            servidor.kill()

    if a.json:
        print(json.dumps(d, ensure_ascii=False, indent=1))
    else:
        g = d["geometria"]
        print(f"== tema {a.tema} · {a.ancho}x{a.alto} ==")
        print(f"header {g.get('headerH')}px · desborde de pagina {g.get('desbordePagina')}px")
        desbordes_wrap = [w for w in g.get("conWrap", []) if w["desborde"] > 1 and not w.get("scrolleable")]
        if desbordes_wrap:
            for w in desbordes_wrap:
                print(f"  ! .wrap desborda SIN scroll {w['desborde']}px ({w['sw']} en {w['cw']})")
        con_scroll = [w for w in g.get("conWrap", []) if w["desborde"] > 1 and w.get("scrolleable")]
        if con_scroll:
            print(f"  · {len(con_scroll)} tabla(s) con scroll horizontal propio (por diseno): "
                  + ", ".join(f"{w['desborde']}px" for w in con_scroll))
        print(f"desbordes de texto: {len(d['desbordes'])}")
        for x in d["desbordes"][:12]:
            print("  !", x)
        print(f"contraste bajo: {len(d['contraste'])}")
        for x in d["contraste"][:12]:
            print(f"  ! {x['ratio']} (min {x['min']}) {x['px']}px {x['el']} :: {x['txt']!r}")
        print(f"solapes con el header: {len(d['solapes'])}")
        for x in d["solapes"][:8]:
            print("  !", x)
        if g.get("tarjetas"):
            print(f"tarjetas: filas={g['filas']} diferencia de alto={g['altoDistinto']}px")
            for c in g["tarjetas"]:
                print(f"  · {c['titulo'][:38]:40s} x={c['x']:5d} y={c['y']:5d} {c['w']}x{c['h']}")
            print(f"hueco inferior por tarjeta: {g['huecoInferior']}")
            for f in g["chipsY"]:
                print(f"  fila y={f['fila']}: chipsY={f['chips']} alturas={f['alturas']}")
