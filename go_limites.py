#!/usr/bin/env python3
"""Scrapea los limites de uso de OpenCode Go desde la documentacion oficial.

Fuente: https://opencode.ai/v2/docs/console/go/
Salida: go_limites.json  (lo consume index_datos.py -> datos.json -> index.html)

Calcula ademas el multiplicador sobre el precio del plan (x6, x8...) que es lo que
la gente compara: cuanto "valor de uso" te da cada modelo por los $10 del plan.

Uso:
  python3 go_limites.py
"""
import json, os, re, sys, urllib.request, html as H, datetime

URL = "https://opencode.ai/v2/docs/console/go/"
HERE = os.path.dirname(os.path.abspath(__file__))
PLAN_PRECIO = 10.0      # plan Go
PLUS_PRECIO = 40.0      # plan Go Plus

req = urllib.request.Request(URL, headers={"User-Agent": "Mozilla/5.0 research-script/1.0"})
try:
    raw = urllib.request.urlopen(req, timeout=60).read().decode("utf-8", "replace")
except Exception as e:
    sys.exit(f"no se pudo descargar {URL}: {e}")

def celdas(fila):
    return [H.unescape(re.sub(r"<[^>]+>", "", c)).strip()
            for c in re.findall(r"<t[hd][^>]*>(.*?)</t[hd]>", fila, re.S)]

def tablas(html):
    out = []
    for t in re.findall(r"<table.*?</table>", html, re.S):
        filas = re.findall(r"<tr.*?</tr>", t, re.S)
        if not filas:
            continue
        out.append((celdas(filas[0]), [celdas(f) for f in filas[1:]]))
    return out

def buscar(tablas_, clave):
    for cab, filas in tablas_:
        if all(any(clave.lower() in c.lower() for c in cab) for clave in [clave]):
            return cab, filas
    return None, []

T = tablas(raw)
h_lim, f_lim = buscar(T, "Monthly limit")        # primera = Go
h_lim_plus, f_lim_plus = None, []
vistas = [f for f in T if "Monthly limit" in " ".join(f[0])]
if len(vistas) > 1:
    h_lim_plus, f_lim_plus = vistas[1]
h_req, f_req = buscar(T, "Requests per month")
h_priv, f_priv = buscar(T, "Data retention")

if not f_lim:
    sys.exit("no se encontro la tabla de limites; la web cambio de formato")

def money(v):
    v = (v or "").strip()
    if v.lower().startswith("free"):
        return 0.0, "Free"
    m = re.match(r"\$?([\d.,]+)", v.replace(",", ""))
    return (float(m.group(1)), v) if m else (None, v)

def limite(v):
    v = (v or "").strip()
    if "unlimited" in v.lower():
        return None, "Unlimited"
    m = re.search(r"\$([\d.,]+)", v.replace(",", ""))
    return (float(m.group(1)), v) if m else (None, v)

def base(n):
    """'GPT 6 Luna (<= 272K tokens)' -> 'GPT 6 Luna'"""
    return re.sub(r"\s*\(.*?\)\s*$", "", n).strip()

plus_por_modelo = {f[0]: f for f in f_lim_plus}
req_por_modelo = {f[0]: f for f in f_req}
priv_por_modelo = {f[0]: f for f in f_priv}

filas = []
for f in f_lim:
    if len(f) < 6:
        continue
    modelo, inp, out, cread, cwrite, lim = f[:6]
    n_lim, lim_txt = limite(lim)
    _, inp_txt = money(inp)
    _, out_txt = money(out)
    p = plus_por_modelo.get(modelo) or plus_por_modelo.get(base(modelo))
    n_plus, plus_txt = limite(p[5]) if p and len(p) > 5 else (None, None)
    r = req_por_modelo.get(modelo) or req_por_modelo.get(base(modelo))
    filas.append({
        "modelo": modelo,
        "entrada": inp_txt, "salida": out_txt,
        "cache_lectura": cread if cread not in ("-", "") else "—",
        "cache_escritura": cwrite if cwrite not in ("-", "") else "—",
        "limite_go": n_lim if n_lim is not None else "∞",
        "limite_go_txt": lim_txt,
        "x_plan": round(n_lim / PLAN_PRECIO, 2) if n_lim else ("∞" if n_lim is None and "unlimited" in lim_txt.lower() else None),
        "limite_plus": n_plus if n_plus is not None else (plus_txt or "—"),
        "x_go_plus": round(n_plus / n_lim, 1) if (n_plus and n_lim) else "—",
        "req_mes": r[3] if r and len(r) > 3 else "—",
        "entrena": (priv_por_modelo.get(modelo) or priv_por_modelo.get(base(modelo)) or ["", "—", "—"])[1],
        "retencion": (priv_por_modelo.get(modelo) or priv_por_modelo.get(base(modelo)) or ["", "—", "—"])[2],
    })

doc = {
    "titulo": "Uso y límites de OpenCode Go (oficial)",
    "fuente": URL,
    "actualizado": datetime.datetime.now(datetime.UTC).strftime("%Y-%m-%d %H:%M UTC"),
    "plan": {"nombre": "Go", "precio": "$10/mes", "nota": "Go Plus: $40/mes con límites mayores"},
    "reglas": [
        "Límites en dólares/mes por modelo: 5 horas = 20% del límite mensual, semanal = 50%, mensual = 100%.",
        "El precio por token es el mismo en Go y en Go Plus; lo que cambia es el límite mensual.",
        "×plan = cuánto valor de uso te da cada modelo por los $10 del plan (x6 = $60).",
        "DeepSeek: horas punta 01:00-04:00 y 06:00-10:00 UTC de lunes a viernes; el resto (y fines de semana) es off-peak.",
        "Modelos gratis por tiempo limitado (LongCat 2.5 Preview, Step 5 Preview, Cat Jam) no consumen límite.",
        "Si agotas el límite puedes seguir con los modelos gratis, o activar «Use balance» para pagar por uso.",
        "«entrena» = sí significa que tus prompts y respuestas se usan para entrenar; retención en días.",
    ],
    "filas": filas,
}
with open(os.path.join(HERE, "go_limites.json"), "w", encoding="utf-8") as f:
    json.dump(doc, f, ensure_ascii=False, indent=1)

print(f"{len(filas)} modelos · fuente {URL}")
print(f"{'modelo':<34}{'lim/mes':>9}{'xplan':>7}{'plus':>9}{'req/mes':>10}  entrena")
for f in filas:
    lim = f"${f['limite_go']:.0f}" if isinstance(f["limite_go"], float) else f["limite_go"]
    xp = f"x{f['x_plan']:g}" if isinstance(f["x_plan"], float) else f["x_plan"]
    plus = f"${f['limite_plus']:.0f}" if isinstance(f["limite_plus"], float) else str(f["limite_plus"])
    print(f"{f['modelo']:<38}{lim:>8}{xp:>7}{plus:>10}{f['req_mes']:>10}  {f['entrena']:<9}{f['retencion']}")
