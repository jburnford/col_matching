/* tours.js — the opening sequence + replayable guided tours.
   Intro arc: (A) a ~20s cinematic build of the whole century's web, then
   (B) the web fades and Willingdon's single career draws on the clean map,
   then (C) handoff to free exploration. */
(function (ATLAS) {
  const el = id => document.getElementById(id);
  const BUILD = {
    title: 'Two services, one empire',
    caption: 'From the 1820s to the 1960s two civil services moved tens of thousands of officials ' +
             'across the British Empire — the Colonial Office in blue, the India Office in gold. ' +
             'Here a century of their careers accumulates in twenty seconds.',
  };

  function dominantCorpus(qid) {
    const p = ATLAS.App.places[qid]; if (!p) return 1;
    return (p.io_in + p.io_out) > (p.co_in + p.co_out) ? 1 : 0;
  }

  const Tours = {
    init(tours) {
      this.tours = tours; this.wrap = el('tour');
      el('tour-next').onclick = () => this.next();
      el('tour-skip').onclick = () => this.end();
      el('tour-card').addEventListener('click', e => e.stopPropagation());
    },

    // ---- the opening sequence ------------------------------------------
    startIntro() {
      const reduce = window.matchMedia('(prefers-reduced-motion:reduce)').matches;
      this.wrap.hidden = false;
      ATLAS.Arcs.setCorpus({ 0: true, 1: true });
      if (reduce) { ATLAS.Timeline.setYear(ATLAS.Timeline.y1, false); this.startWillingdon(); return; }
      // BUILD phase
      el('tour-title').textContent = BUILD.title;
      el('tour-caption').textContent = BUILD.caption;
      el('tour-dots').innerHTML = '';
      el('tour-next').style.display = 'none';
      el('tour-skip').textContent = 'Skip intro →';
      ATLAS.Arcs.clearHighlight();
      ATLAS.Timeline.setYear(ATLAS.Timeline.y0, false);   // empty map; view already set at boot
      setTimeout(() => ATLAS.Timeline.play(20000, () => this.startWillingdon()), 400);
    },

    startWillingdon() {
      const i = this.tours.findIndex(t => t.id === 'willingdon');
      this.start(i < 0 ? 0 : i);
    },

    // ---- a guided tour (Willingdon by default) -------------------------
    start(i) {
      if (ATLAS.Timeline.timer) ATLAS.Timeline.stop();
      this.t = this.tours[i]; this.k = -1; this._wk = null;
      this.wrap.hidden = false;
      el('tour-title').textContent = this.t.title;
      el('tour-next').style.display = '';
      el('tour-skip').textContent = 'Explore the full atlas →';
      el('tour-dots').innerHTML = this.t.steps.map(() => '<i></i>').join('');
      // leave the full web standing for a beat, then fade to the single thread
      this.next();
    },
    // toggle which corpus webs are drawn, only rebuilding when it changes
    setWeb(co, io) {
      const k = (co ? 1 : 0) + '' + (io ? 1 : 0);
      if (this._wk !== k) { this._wk = k; ATLAS.Arcs.setCorpus({ 0: co, 1: io }); }
    },
    next() {
      this.k++;
      const steps = this.t.steps;
      if (this.k >= steps.length) return this.end();
      const s = steps[this.k], p = ATLAS.App.places[s.qid];
      el('tour-caption').textContent = s.caption;
      [...el('tour-dots').children].forEach((d, j) => d.classList.toggle('on', j <= this.k));
      el('tour-next').textContent = this.k === steps.length - 1 ? 'Finish' : 'Next';
      if (s.yr) ATLAS.Timeline.setYear(s.yr, false);     // year clock follows the story

      // CONTEXT slide: introduce a whole web (one corpus or both), no synthetic path
      if (s.web) {
        this.setWeb(s.web !== 'io', s.web !== 'co');     // 'co' | 'io' | 'both'
        ATLAS.Arcs.clearHighlight();                     // show the real web, undimmed
        if (p) ATLAS.App.map.flyTo([p.lat, p.lon], s.zoom || 3.4, { duration: 1.1 });
        else if (s.home) ATLAS.App.map.flyTo([24, 52], 3, { duration: 1.1 });  // pull back to the whole web for the hand-off
        return;
      }

      // CAREER step: both webs available, dimmed so only this career's thread shows
      this.setWeb(true, true);
      const pairs = [];
      for (let j = 1; j <= this.k; j++) {
        const a = ATLAS.App.places[steps[j - 1].qid], b = ATLAS.App.places[steps[j].qid];
        if (a && b) pairs.push([a.lat, a.lon, b.lat, b.lon, dominantCorpus(steps[j].qid)]);
      }
      ATLAS.Arcs.setCustomHighlight(pairs, true);

      if (p) {
        const pts = steps.slice(0, this.k + 1).map(x => ATLAS.App.places[x.qid]).filter(Boolean).map(q => [q.lat, q.lon]);
        if (pts.length > 1) ATLAS.App.map.flyToBounds(pts, { padding: [90, 90], maxZoom: 5, paddingBottomRight: [410, 150], duration: 1.0 });
        else ATLAS.App.map.flyTo([p.lat, p.lon], 4.2, { duration: 1.0 });
      }
    },
    dismiss() {                                   // user interacted — get the overlay out of the way
      if (this.wrap.hidden) return;
      if (ATLAS.Timeline.timer) ATLAS.Timeline.stop();
      this.setWeb(true, true);                    // restore both webs if a context slide hid one
      this.wrap.hidden = true;
    },
    end() {
      if (ATLAS.Timeline.timer) ATLAS.Timeline.stop();
      this.setWeb(true, true);                    // both webs back on for free exploration
      this.wrap.hidden = true;
      ATLAS.Timeline.setYear(ATLAS.Timeline.y1, false);   // full web, full span
      if (this.t && this.t.pids && this.t.pids.length) ATLAS.App.selectPerson(this.t.pids);
      else { ATLAS.Arcs.clearHighlight(); ATLAS.App.reset(); }
    },
  };
  ATLAS.Tours = Tours;
})(window.ATLAS = window.ATLAS || {});
