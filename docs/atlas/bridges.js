/* bridges.js — the "Two Services" view: officials whose careers span BOTH the
   Colonial Office and the India Office. Lists cross-corpus matches (bridges.json)
   and, on selection, draws one person's CO career (blue) and IO career (gold) on
   the same map with a combined Record of Services (Register.bridge). */
(function (ATLAS) {
  const esc = s => (s || '').replace(/[&<>]/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;' }[c]));
  const CONF = { A: 'high confidence', B: 'probable', C: 'possible' };

  const Bridges = {
    init() { this.data = null; this.items = null; },
    async load() {
      if (!this.data) this.data = await fetch('data/bridges.json').then(r => r.json());
      return this.data;
    },
    async open() {
      ATLAS.Tours.dismiss();
      const d = await this.load();
      await ATLAS.App.loadCareers();
      ATLAS.Timeline.onYear = null;
      ATLAS.Arcs.clearHighlight(); ATLAS.Places.clearEmphasis();
      // only those actually mapped in BOTH services are worth drawing
      this.items = d.bridges.filter(b => b.co_stints && b.io_stints);
      const body = ATLAS.Register.body;
      const row = (b, i) => `<li class="br-row" data-i="${i}">
          <span class="br-nm">${esc(b.surname)}<span class="giv">, ${esc(b.name)}</span>${b.birth ? ` <span class="br-b">b.${b.birth}</span>` : ''}${b.ambiguous ? ' <span class="br-amb" title="matches more than one record — verify">±</span>' : ''}</span>
          <span class="br-meta"><span class="cf cf-${b.conf}" title="${CONF[b.conf]}">${b.conf}</span>
            <span class="br-st" title="located postings — Colonial / India"><b class="co">${b.co_stints}</b><i>·</i><b class="io">${b.io_stints}</b></span></span>
        </li>`;
      body.innerHTML = `
        <div class="reg-h">Two services, one empire</div>
        <p class="reg-lede">Officials whose careers span <b style="color:#6f97cf">both</b> the Colonial Office
          <b style="color:#d59a3a">and</b> the India Office — one person serving the colonies and the Raj.
          Matched across the two corpora by name plus a corroborating signal.</p>
        <div class="stat-row" style="margin-top:2px">
          <div class="stat"><b>${this.items.length}</b><span>mapped in both services</span></div>
          <div class="stat"><b>${d.counts.total}</b><span>candidates in all</span></div>
        </div>
        <div class="reg-h">The bridge careers <span class="reg-hint">— click to trace across both services</span></div>
        <ul class="br-list">${this.items.map(row).join('')}</ul>
        <p class="ros-note">Confidence: <b>A</b> = shared dated honour or distinctive name + birth year ·
          <b>B</b> = birth year · <b>C</b> = name only. A cross-corpus link is a discovery aid, not a verified merge.</p>`;
      body.querySelectorAll('.br-row').forEach(li =>
        li.onclick = () => ATLAS.App.selectBridge(this.items[+li.dataset.i]));
    },
  };
  ATLAS.Bridges = Bridges;
})(window.ATLAS = window.ATLAS || {});
