/* timeline.js — decade histogram + year scrubber + play.
   The scrubber sets the "show transfers up to year Y" ceiling; play animates it,
   reusing the arc engine's incremental burn-in (the video technique). */
(function (ATLAS) {
  const Timeline = {
    init(meta) {
      this.meta = meta;
      [this.y0, this.y1] = meta.yearRange;
      this.hist = meta.decadeHist;
      this.cv = document.getElementById('tl-hist'); this.ctx = this.cv.getContext('2d');
      this.range = document.getElementById('tl-range');
      this.out = document.getElementById('tl-year');
      this.playBtn = document.getElementById('tl-play');
      this.range.min = this.y0; this.range.max = this.y1; this.range.value = this.y1;
      this.year = this.y1;
      const decades = {};
      for (const c of ['co', 'io']) for (const [d, n] of Object.entries(this.hist[c])) decades[d] = (decades[d] || 0) + n;
      this.maxDecade = Math.max(...Object.values(decades), 1);

      this.range.addEventListener('input', () => this.setYear(+this.range.value, false));
      this.playBtn.addEventListener('click', () => this.toggle());
      window.addEventListener('resize', () => { this.sizeHist(); this.drawHist(); });
      this.sizeHist(); this._dec = -1; this.drawHist();
    },
    setYear(y, fromPlay) {
      this.year = y; this.out.textContent = Math.floor(y);
      if (!fromPlay) this.range.value = y;
      ATLAS.Arcs.setYear(y);
      // only repaint the histogram when the lit decade actually changes (not every frame)
      const dec = Math.floor((y + 0.5) / 10);
      if (dec !== this._dec) { this._dec = dec; this.drawHist(); }
    },
    sizeHist() {
      const c = this.cv, dpr = window.devicePixelRatio || 1;
      this._w = c.clientWidth; this._h = c.clientHeight;
      c.width = this._w * dpr; c.height = this._h * dpr;
      this.ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    },
    drawHist() {
      if (!this._w) this.sizeHist();
      const w = this._w, h = this._h, ctx = this.ctx;
      ctx.clearRect(0, 0, w, h);
      const span = this.y1 - this.y0, bw = (w / span) * 10 - 1.5;
      const px = yr => (yr - this.y0) / span * w;
      for (let d = Math.floor(this.y0 / 10) * 10; d <= this.y1; d += 10) {
        const co = this.hist.co[d] || 0, io = this.hist.io[d] || 0;
        const x = px(d), past = d + 10 <= this.year + 0.5;
        const hco = (co / this.maxDecade) * (h - 4), hio = (io / this.maxDecade) * (h - 4);
        ctx.globalAlpha = past ? 0.9 : 0.22;
        ctx.fillStyle = '#5f86bd'; ctx.fillRect(x, h - hco, bw, hco);                 // CO from base
        ctx.fillStyle = '#cf9a3f'; ctx.fillRect(x, h - hco - hio, bw, hio);           // IO stacked
      }
      ctx.globalAlpha = 1;
    },
    toggle() { if (this.timer) this.stop(); else this.play(24000); },
    play(dur, onDone) {
      if (this.timer) this.stop();
      if (this.year >= this.y1) this.setYear(this.y0, false);   // restart from the top
      this.playBtn.textContent = '❚❚'; ATLAS.Arcs.playing = true;
      const t0 = performance.now(), startY = this.year, span = this.y1 + 2 - startY;
      this._done = onDone || null;
      const tick = (t) => {
        const k = Math.min(1, (t - t0) / dur);
        this.setYear(startY + span * k, true);
        if (k < 1) { this.raf = requestAnimationFrame(tick); }
        else { const cb = this._done; this.stop(); if (cb) cb(); }
      };
      this.timer = true; this.raf = requestAnimationFrame(tick);
    },
    stop() {
      this.timer = false; this._done = null; if (this.raf) cancelAnimationFrame(this.raf);
      ATLAS.Arcs.playing = false; this.playBtn.textContent = '▶';
      this.setYear(Math.min(this.year, this.y1), false); ATLAS.Arcs.draw();
    },
  };
  ATLAS.Timeline = Timeline;
})(window.ATLAS = window.ATLAS || {});
