/* app.js — Schools of Empire: bootstrap + shared state.
   Loads meta/institutions/local/stream up front; alumni.json is lazy-loaded on
   first institution click (it is ~2 MB). */
(function (ATLAS) {
  const DATA = 'data_edu/';
  const getJSON = f => fetch(DATA + f).then(r => { if (!r.ok) throw new Error(f + ' ' + r.status); return r.json(); });

  const App = {
    decade: null,          // null = all decades; else a decade int
    colorBy: 'kind',       // 'kind' (dominant role-category) | 'type'

    async boot() {
      const map = L.map('map', {
        zoomControl: true, attributionControl: true, worldCopyJump: true,
        minZoom: 2, maxZoom: 16, zoomSnap: 0.25,
      }).setView([30, 20], 3);
      L.tileLayer('https://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}{r}.png', {
        subdomains: 'abcd', maxZoom: 19, maxNativeZoom: 20,
        attribution: '&copy; OpenStreetMap, &copy; CARTO · Office List education data &amp; Wikidata',
      }).addTo(map);
      this.map = map;

      const [meta, institutions, local, stream, arcs] = await Promise.all(
        ['meta.json', 'institutions.json', 'local.json', 'stream.json', 'school_arcs.json'].map(getJSON));
      this.meta = meta; this.institutions = institutions; this.local = local; this.stream = stream;
      this.schoolArcs = arcs; this.alumni = null;

      document.getElementById('m-mapped').textContent = meta.mapped.toLocaleString();
      document.getElementById('m-local').textContent = meta.local.toLocaleString();
      document.getElementById('tab-local-n').textContent = meta.local.toLocaleString();

      ATLAS.Markers.init(map, institutions);
      ATLAS.Arcs.init(map, document.getElementById('arc-canvas'), arcs, institutions);
      ATLAS.Stream.init(stream, meta);
      ATLAS.Panel.init();

      this.buildLegend();
      this.wireRail();
      this.wireTabs();
      ATLAS.Panel.overview();
    },

    color(rec) {
      const m = this.meta;
      return this.colorBy === 'type'
        ? (m.type_color[rec.type] || '#79706E')
        : (m.cat_color[rec.dominant] || '#79706E');
    },

    // ---- legend reflects the active colour-by --------------------------
    buildLegend() {
      const m = this.meta, ul = document.getElementById('legend');
      const entries = this.colorBy === 'type'
        ? Object.keys(m.type_color).map(k => [k, m.type_color[k]])
        : m.cat_order.filter(c => c !== 'other' && c !== 'unknown').map(c => [c, m.cat_color[c]]);
      ul.innerHTML = entries.map(([k, col]) =>
        `<li><i style="background:${col}"></i>${k.replace(/_/g, ' ')}</li>`).join('');
    },

    setColorBy(by) {
      this.colorBy = by;
      document.querySelectorAll('.cb').forEach(b => b.classList.toggle('on', b.dataset.by === by));
      this.buildLegend();
      ATLAS.Markers.render();
      ATLAS.Panel.refresh();
    },

    setDecade(d) {
      this.decade = (d === this.decade) ? null : d;     // click same decade -> clear
      const sel = document.getElementById('stream-sel');
      const rst = document.getElementById('stream-reset');
      sel.textContent = this.decade ? `${this.decade}s` : '';
      rst.hidden = !this.decade;
      ATLAS.Stream.setSelected(this.decade);
      ATLAS.Markers.render();
      ATLAS.Panel.refresh();
    },

    countFor(rec) {                                     // alumni metric for current decade
      if (!this.decade) return rec.total;
      return (rec.by_decade && rec.by_decade[this.decade]) || 0;
    },

    async loadAlumni() { if (!this.alumni) this.alumni = await getJSON('alumni.json'); return this.alumni; },
    async selectInstitution(id) { await this.loadAlumni(); ATLAS.Panel.detail(id); },

    wireRail() {
      document.querySelectorAll('.cb').forEach(b => b.onclick = () => this.setColorBy(b.dataset.by));
      document.getElementById('stream-reset').onclick = () => this.setDecade(null);
      document.getElementById('rail-arcs').onclick = () => ATLAS.Arcs.toggle(!ATLAS.Arcs.visible);
    },
    wireTabs() {
      document.querySelectorAll('.tab').forEach(b => b.onclick = () => {
        document.querySelectorAll('.tab').forEach(t => t.classList.toggle('on', t === b));
        b.dataset.tab === 'local' ? ATLAS.Panel.localTab() : ATLAS.Panel.overview();
      });
    },
  };
  ATLAS.App = App;
  document.addEventListener('DOMContentLoaded', () => App.boot().catch(e => {
    console.error(e);
    document.getElementById('panel-body').innerHTML =
      '<div class="reg-h">Could not load</div><p class="reg-lede">The data failed to load. ' +
      'If you opened this file directly, serve the folder over HTTP (e.g. <code>python3 -m http.server</code>).</p>';
  }));
})(window.ATLAS = window.ATLAS || {});
