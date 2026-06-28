/* arcs.js — feeder-school co-attendance arcs over the night-atlas.
   A person who attended two mapped institutions links them (the prep-school →
   university pipeline). Only 608 arcs, so we reproject + redraw them all on every
   map move (cheap). Two modes: a global toggle (faint web of all pipelines) and
   per-institution highlight (its pipelines, bright) when one is selected. */
(function (ATLAS) {
  const Arcs = {
    init(map, canvas, arcs, inst) {
      this.map = map; this.cv = canvas; this.ctx = canvas.getContext('2d');
      this.arcs = arcs; this.inst = inst; this.visible = false; this.hl = null;
      this.maxW = Math.max(1, ...arcs.map(a => a[2]));
      this.adj = {};                                  // qid -> [[other,w]] for the panel
      for (const [a, b, w] of arcs) {
        (this.adj[a] = this.adj[a] || []).push([b, w]);
        (this.adj[b] = this.adj[b] || []).push([a, w]);
      }
      for (const k in this.adj) this.adj[k].sort((x, y) => y[1] - x[1]);
      map.on('move zoom moveend zoomend', () => this.draw());
      window.addEventListener('resize', () => this.resize());
      this.resize();
    },
    resize() {
      const s = this.map.getSize();
      this.cv.width = s.x; this.cv.height = s.y;
      this.draw();
    },
    toggle(on) {
      this.visible = on;
      const btn = document.getElementById('rail-arcs');
      if (btn) btn.classList.toggle('on', on);
      this.draw();
    },
    setHighlight(id) { this.hl = id; this.draw(); },

    draw() {
      const ctx = this.ctx, cv = this.cv;
      ctx.clearRect(0, 0, cv.width, cv.height);
      if (!this.visible && !this.hl) return;
      for (const [a, b, w] of this.arcs) {
        const ra = this.inst[a], rb = this.inst[b];
        if (!ra || !rb) continue;
        const isHl = this.hl && (a === this.hl || b === this.hl);
        if (this.hl && !isHl) continue;             // focus mode: only its pipelines
        if (!this.visible && !isHl) continue;
        const pa = this.map.latLngToContainerPoint([ra.lat, ra.lon]);
        const pb = this.map.latLngToContainerPoint([rb.lat, rb.lon]);
        this.curve(pa, pb, w, isHl);
      }
    },
    curve(p1, p2, w, hl) {
      const ctx = this.ctx;
      const mx = (p1.x + p2.x) / 2, my = (p1.y + p2.y) / 2;
      const dx = p2.x - p1.x, dy = p2.y - p1.y, len = Math.hypot(dx, dy) || 1;
      const lift = Math.min(len * 0.2, 130);
      const cx = mx - dy / len * lift, cy = my + dx / len * lift;
      const t = w / this.maxW;
      ctx.beginPath();
      ctx.moveTo(p1.x, p1.y);
      ctx.quadraticCurveTo(cx, cy, p2.x, p2.y);
      ctx.strokeStyle = hl ? `rgba(255,217,138,${0.45 + 0.5 * t})`
                           : `rgba(143,184,238,${0.06 + 0.20 * t})`;
      ctx.lineWidth = hl ? 1 + 3 * t : 0.5 + 1.6 * t;
      ctx.stroke();
    },
  };
  ATLAS.Arcs = Arcs;
})(window.ATLAS = window.ATLAS || {});
