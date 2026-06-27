/* arcs.js — interactive night-atlas arc engine.
   Lifted from build_combined_mobility_global.py and made filterable:
   a persistent offscreen "web" canvas accumulates faint arcs up to the current
   year for the enabled services; only highlighted / in-flight arcs redraw per
   frame. Never redraws all 25k arcs every frame. */
(function (ATLAS) {
  const WEB   = ['rgba(143,184,238,0.075)', 'rgba(232,178,76,0.080)'];
  const TRAIL = [[150, 200, 255], [255, 205, 120]];
  const HEAD  = ['rgba(220,238,255,0.95)', 'rgba(255,244,210,0.95)'];
  const FLIGHT = 1.4;                 // years an in-flight arc "flies"

  function arcCurve(x1, y1, x2, y2) {
    const mx = (x1 + x2) / 2, my = (y1 + y2) / 2, dx = x2 - x1, dy = y2 - y1;
    const len = Math.hypot(dx, dy) || 1, lift = Math.min(len * 0.22, 150);
    return [mx - dy / len * lift, my + dx / len * lift];
  }
  function pointAt(x1, y1, cx, cy, x2, y2, t) {
    const u = 1 - t;
    return [u * u * x1 + 2 * u * t * cx + t * t * x2, u * u * y1 + 2 * u * t * cy + t * t * y2];
  }

  const Arcs = {
    init(map, canvas) {
      this.map = map; this.cv = canvas; this.ctx = canvas.getContext('2d');
      this.pc = document.createElement('canvas'); this.pctx = this.pc.getContext('2d');
      this.arcs = []; this.ll = []; this.pix = null;
      this.idx = 0; this.curYear = 0; this.hl = null; this.playing = false;
      this.corpus = { 0: true, 1: true };
      const resize = () => this.resize();
      window.addEventListener('resize', resize);
      // during a pan/fly: invalidate projection; cheaply re-track the curated tour
      // arcs (they project lat/lon live) so they follow the map instead of freezing
      map.on('move zoom', () => { this.pix = null; if (this.hlc) this.draw(); });
      // after the map settles: re-project everything and repaint web + highlights
      map.on('moveend zoomend', () => { this.reproject(); this.rebuild(); this.draw(); });
      this.resize();
    },
    resize() {
      const w = this.map.getSize().x, h = this.map.getSize().y;
      for (const c of [this.cv, this.pc]) { c.width = w; c.height = h; }
      this.W = w; this.H = h; this.pix = null; this.reproject(); this.rebuild();
    },
    setData(arcs, places) {
      this.arcs = arcs;                                          // [[yr,from,to,pid,corpus]]
      this.ll = arcs.map(a => {
        const f = places[a[1]], t = places[a[2]];
        return f && t ? [f.lat, f.lon, t.lat, t.lon] : null;
      });
      this.reproject();
    },
    reproject() {
      if (!this.map || !this.ll.length) return;
      this.pix = this.ll.map(p => {
        if (!p) return null;
        const a = this.map.latLngToContainerPoint([p[0], p[1]]);
        const b = this.map.latLngToContainerPoint([p[2], p[3]]);
        return [a.x, a.y, b.x, b.y];
      });
    },
    setYear(y) {
      if (y >= this.curYear) this.burnTo(y); else this.rebuild(y);
      this.draw();
    },
    setCorpus(c) { this.corpus = c; this.rebuild(); this.draw(); },
    rebuild(year) {                                              // full rebuild of the web
      if (year != null) this._target = year; else year = this._target ?? this.curYear;
      this.pctx.clearRect(0, 0, this.W, this.H);
      this.idx = 0; this.curYear = 0; this.burnTo(year);
    },
    burnTo(year) {                                               // incremental accumulation
      if (!this.pix) this.reproject();
      this._target = year;
      while (this.idx < this.arcs.length && this.arcs[this.idx][0] <= year) {
        const a = this.arcs[this.idx], p = this.pix[this.idx];
        if (p && this.corpus[a[4]]) {
          const [cx, cy] = arcCurve(p[0], p[1], p[2], p[3]);
          this.pctx.strokeStyle = WEB[a[4]]; this.pctx.lineWidth = 0.7;
          this.pctx.beginPath(); this.pctx.moveTo(p[0], p[1]);
          this.pctx.quadraticCurveTo(cx, cy, p[2], p[3]); this.pctx.stroke();
        }
        this.idx++;
      }
      this.curYear = year;
    },
    // list of arc indices; dim=true hides the whole background web so a single
    // career reads on a clean map; yearScoped=true reveals the highlighted arcs
    // only up to the current timeline year (a career plays on the scrubber)
    setHighlight(list, dim, yearScoped) {
      this.hl = list; this.hlc = null; this.dimWeb = !!dim; this.hlYearScoped = !!yearScoped; this.draw();
    },
    // arbitrary curated arcs (tours): pairs of [lat1,lon1,lat2,lon2,corpus]
    setCustomHighlight(pairs, dim) { this.hlc = pairs; this.hl = null; this.dimWeb = !!dim; this.draw(); },
    clearHighlight() { this.hl = null; this.hlc = null; this.dimWeb = false; this.hlYearScoped = false; this.draw(); },
    draw() {
      const ctx = this.ctx; if (!ctx) return;
      ctx.clearRect(0, 0, this.W, this.H);
      if (!this.dimWeb) ctx.drawImage(this.pc, 0, 0);   // hide the full web when focused on one career
      // in-flight glowing heads while playing
      if (this.playing && !this.dimWeb && this.pix) {
        for (let i = this.idx; i < this.arcs.length; i++) {
          const yr = this.arcs[i][0]; if (yr > this.curYear) break;
        }
        // scan a small window behind curYear
        let i = this.idx;
        while (i > 0 && this.arcs[i - 1][0] > this.curYear - FLIGHT) i--;
        for (; i < this.arcs.length; i++) {
          const a = this.arcs[i]; if (a[0] > this.curYear) break;
          if (!this.corpus[a[4]] || !this.pix[i]) continue;
          const f = (this.curYear - a[0]) / FLIGHT; if (f < 0 || f > 1) continue;
          this._fly(this.pix[i], a[4], f);
        }
      }
      if (this.hl) this._drawHighlight();
      if (this.hlc) this._drawCustom();
    },
    _drawCustom() {
      const ctx = this.ctx; ctx.save();
      const ends = [];
      for (const g of this.hlc) {
        const a = this.map.latLngToContainerPoint([g[0], g[1]]);
        const b = this.map.latLngToContainerPoint([g[2], g[3]]);
        const tr = TRAIL[g[4] || 1], [cx, cy] = arcCurve(a.x, a.y, b.x, b.y);
        ctx.shadowColor = `rgba(${tr[0]},${tr[1]},${tr[2]},0.9)`; ctx.shadowBlur = 10;
        ctx.strokeStyle = `rgba(${tr[0]},${tr[1]},${tr[2]},0.95)`; ctx.lineWidth = 2;
        ctx.beginPath(); ctx.moveTo(a.x, a.y); ctx.quadraticCurveTo(cx, cy, b.x, b.y); ctx.stroke();
        ends.push([a.x, a.y], [b.x, b.y]);
      }
      ctx.shadowBlur = 0;
      for (const [x, y] of ends) { ctx.beginPath(); ctx.fillStyle = 'rgba(255,248,220,0.97)'; ctx.arc(x, y, 3.4, 0, 7); ctx.fill(); }
      ctx.restore();
    },
    _fly(p, corpus, f) {
      const ctx = this.ctx, [cx, cy] = arcCurve(p[0], p[1], p[2], p[3]), tr = TRAIL[corpus];
      ctx.strokeStyle = `rgba(${tr[0]},${tr[1]},${tr[2]},${0.5 * (1 - f) + 0.12})`; ctx.lineWidth = 1.2;
      ctx.beginPath(); ctx.moveTo(p[0], p[1]);
      const steps = 14; for (let s = 1; s <= steps * f; s++) { const q = pointAt(p[0], p[1], cx, cy, p[2], p[3], s / steps); ctx.lineTo(q[0], q[1]); }
      ctx.stroke();
      const hd = pointAt(p[0], p[1], cx, cy, p[2], p[3], f);
      ctx.beginPath(); ctx.fillStyle = HEAD[corpus]; ctx.arc(hd[0], hd[1], 2.4, 0, 7); ctx.fill();
    },
    _drawHighlight() {
      const ctx = this.ctx;
      ctx.save();
      const ends = new Set();
      for (const i of this.hl) {
        const a = this.arcs[i], p = this.pix[i]; if (!p) continue;
        if (this.hlYearScoped && a[0] > this.curYear + 0.5) continue;   // career reveals with the timeline
        const tr = TRAIL[a[4]], [cx, cy] = arcCurve(p[0], p[1], p[2], p[3]);
        ctx.shadowColor = `rgba(${tr[0]},${tr[1]},${tr[2]},0.9)`; ctx.shadowBlur = 8;
        ctx.strokeStyle = `rgba(${tr[0]},${tr[1]},${tr[2]},0.92)`; ctx.lineWidth = 1.8;
        ctx.beginPath(); ctx.moveTo(p[0], p[1]); ctx.quadraticCurveTo(cx, cy, p[2], p[3]); ctx.stroke();
        ends.add(p[0] + ',' + p[1]); ends.add(p[2] + ',' + p[3]);
      }
      ctx.shadowBlur = 0;
      for (const e of ends) {
        const [x, y] = e.split(',').map(Number);
        ctx.beginPath(); ctx.fillStyle = 'rgba(255,248,220,0.95)'; ctx.arc(x, y, 3, 0, 7); ctx.fill();
      }
      ctx.restore();
    },
    // arc indices for a person (by pid) or a place (by qid, in or out)
    indicesForPerson(pid) { const o = []; for (let i = 0; i < this.arcs.length; i++) if (this.arcs[i][3] === pid) o.push(i); return o; },
    indicesForPlace(qid) { const o = []; for (let i = 0; i < this.arcs.length; i++) { const a = this.arcs[i]; if (a[1] === qid || a[2] === qid) o.push(i); } return o; },
  };
  ATLAS.Arcs = Arcs;
})(window.ATLAS = window.ATLAS || {});
