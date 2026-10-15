(() => {
  const R = n => { const r = n.getBoundingClientRect();
    return {x: Math.round(r.x), y: Math.round(r.y), w: Math.round(r.width), h: Math.round(r.height)}; };
  const vis = n => n && n.offsetParent !== null && getComputedStyle(n).display !== 'none';
  const out = {problemas: [], cajas: {}, columnas: {}};

  // --- 1) bloques CON MARCO: comparten columna, luego mismo x y mismo ancho ---
  // Los parrafos sueltos (`.sim-intro`, `.card-preset .desc`) no entran: son
  // texto con medida de lectura, no cajas, y una medida mas corta ahi no se lee
  // como desalineacion.
  const marcos = [
    ['.intro', 'intro'], ['.grid-presets', 'grid-presets'], ['.card-preset', 'card 1'],
    ['.nota-caja', 'nota-caja'], ['.medido', 'medido'], ['.sim', 'sim'],
    ['.ens', 'ens'], ['.wrap', 'wrap/tabla'],
  ];
  marcos.forEach(([sel, nombre]) => {
    const n = document.querySelector(sel);
    if (n) out.cajas[nombre] = R(n);
  });
  const ref = out.cajas['card 1'];
  if (ref) Object.entries(out.cajas).forEach(([k, b]) => {
    if (k === 'card 1') return;
    if (b.x !== ref.x) out.problemas.push(`borde izquierdo distinto: ${k} x=${b.x} vs card x=${ref.x}`);
    if (b.w !== ref.w) out.problemas.push(`ancho distinto: ${k} w=${b.w} vs card w=${ref.w} (${b.w - ref.w}px)`);
  });

  // --- 2) medida de lectura: el MISMO token en todos los textos del frame ---
  // No se comparan anchos renderizados (dependen del ancho disponible y del
  // sangrado de la lista) sino el `max-width` declarado, medido en `ch` reales
  // del elemento. Asi se detecta que un bloque se quede con su propia medida.
  const sonda = document.createElement('span');
  sonda.style.cssText = 'position:absolute;visibility:hidden;width:1ch';
  const chDe = el => { el.appendChild(sonda); const w = sonda.getBoundingClientRect().width;
    sonda.remove(); return w; };
  const medidas = {};
  [['.intro p', 'intro p'], ['.card-preset .desc', 'desc'],
   ['.sim-intro', 'sim-intro'], ['.nota-caja ul', 'nota lista'],
   ['.nota-caja > b', 'nota titulo']].forEach(([sel, k]) => {
    const n = document.querySelector(sel);
    if (!n) return;
    const ch = chDe(n);
    const mw = parseFloat(getComputedStyle(n).maxWidth);
    // Si el elemento no declara medida (max-width:none) se anota null, no NaN:
    // un NaN se cuela en Math.max y desactiva la comprobacion en silencio.
    medidas[k] = (ch && Number.isFinite(mw)) ? +(mw / ch).toFixed(1) : null;
  });
  out.columnas.medidas_ch = medidas;
  const vals = Object.values(medidas).filter(v => v != null);
  if (vals.length > 1 && Math.max(...vals) - Math.min(...vals) > 0.5)
    out.problemas.push(`medida de lectura no uniforme (en ch): ${JSON.stringify(medidas)}`);

  // --- 3) tarjeta: columnas declaradas vs usadas, y columnas del cuerpo ---
  const card = document.querySelector('.card-preset');
  if (card) {
    const cols = getComputedStyle(card).gridTemplateColumns.split(' ');
    out.columnas.card = getComputedStyle(card).gridTemplateColumns;
    const usa2 = [...card.children].some(h => !getComputedStyle(h).gridColumn.includes('/ -1'));
    if (cols.length > 1 && !usa2)
      out.problemas.push(`card: ${cols.length} columnas declaradas y ningun hijo usa la 2a (${cols[1]} muerta)`);
  }
  const cuerpo = document.querySelector('.card-preset .cuerpo');
  if (cuerpo) {
    const cols = getComputedStyle(cuerpo).gridTemplateColumns.split(' ');
    out.columnas.cuerpo = getComputedStyle(cuerpo).gridTemplateColumns;
    const [izq, der] = cuerpo.children;
    // Solo en modo 2 columnas: por debajo de 1080px el cuerpo se pliega a 1 y
    // las dos partes se apilan, asi que compararlas seria un falso positivo.
    if (cols.length === 2 && izq && der) {
      const a = R(izq), b = R(der);
      if (a.y !== b.y) out.problemas.push(`cuerpo: columnas a distinta altura (${a.y} vs ${b.y})`);
      if (a.x + a.w > b.x + 1) out.problemas.push('cuerpo: columnas solapadas');
    }
  }

  // --- 4) grilla de la simulacion ---
  const sim = document.querySelector('.sim');
  if (sim) {
    const cols = getComputedStyle(sim).gridTemplateColumns.split(' ');
    out.columnas.sim = getComputedStyle(sim).gridTemplateColumns;
    const esperadas = window.innerWidth > 1080 ? 3 : 1;
    if (cols.length !== esperadas)
      out.problemas.push(`sim: ${cols.length} columnas a ${window.innerWidth}px (se esperaban ${esperadas})`);
    const cab = [...sim.querySelectorAll('.sim-cab')].filter(vis);
    const celdas = [...sim.querySelectorAll('.celda:not(.paso)')];
    const pasos = [...sim.querySelectorAll('.paso')];
    const porFila = pasos.length ? celdas.length / pasos.length : 0;
    // Cabeceras y divisores solo existen en modo 3 columnas; en 1 columna las
    // cabeceras estan ocultas y las celdas se apilan a proposito.
    if (cols.length === 3 && cab.length === 2 && porFila === 2) {
      const f0 = celdas.slice(0, 2);
      [0, 1].forEach(i => {
        const dx = Math.abs(R(cab[i]).x - R(f0[i]).x), dw = Math.abs(R(cab[i]).w - R(f0[i]).w);
        if (dx > 1 || dw > 1) out.problemas.push(`sim: cabecera ${i} y su celda no coinciden (dx=${dx}, dw=${dw})`);
      });
      pasos.forEach((p, i) => {
        const f = celdas.slice(i * 2, i * 2 + 2);
        if (f.length === 2 && R(f[0]).y !== R(f[1]).y)
          out.problemas.push(`sim: paso ${i} con divisores a distinta altura (${R(f[0]).y} vs ${R(f[1]).y})`);
      });
    }
  }

  // --- 5) barras medidas: los segmentos deben llenar la barra ---
  document.querySelectorAll('.stack').forEach((s, i) => {
    const suma = [...s.children].reduce((a, c) => a + c.getBoundingClientRect().width, 0);
    if (Math.abs(suma - s.clientWidth) > 2)
      out.problemas.push(`stack ${i}: segmentos ${Math.round(suma)}px vs barra ${s.clientWidth}px`);
  });

  // --- 6) nada debe desbordar ni salirse del viewport ---
  document.querySelectorAll('.intro p, .card-preset p, .card-preset li, .chip, .sim .celda p, .ens-sec .nom, .lista-aparte li, .nota-caja li, .sim-cab span').forEach(e => {
    if (e.scrollWidth > e.clientWidth + 1)
      out.problemas.push(`desborda: ${e.className || e.tagName} «${(e.textContent || '').trim().slice(0, 30)}» +${e.scrollWidth - e.clientWidth}px`);
    const r = e.getBoundingClientRect();
    if (r.width > 0 && r.right > document.documentElement.clientWidth + 1)
      out.problemas.push(`fuera del viewport: ${e.className || e.tagName} right=${Math.round(r.right)}`);
  });
  return out;
})()
