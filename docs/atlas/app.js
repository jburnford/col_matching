/* app.js — bootstrap + shared state + orchestration.
   First paint loads only meta/arcs/places/tours (~210KB gz). careers.json and
   search.json are lazy-loaded on first person interaction / search focus. */
(function (ATLAS) {
  const DATA = 'data/';
  const getJSON = f => fetch(DATA + f).then(r => { if (!r.ok) throw new Error(f + ' ' + r.status); return r.json(); });

  const App = {
    async boot() {
      const map = L.map('map', {
        zoomControl: false, attributionControl: true, worldCopyJump: true,
        minZoom: 2, maxZoom: 7, zoomSnap: 0.25,
      }).setView([24, 52], 3);
      L.tileLayer('https://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}{r}.png', {
        subdomains: 'abcd', maxZoom: 8,
        attribution: '&copy; OpenStreetMap, &copy; CARTO · Office List career data &amp; Wikidata',
      }).addTo(map);
      this.map = map;

      const [meta, arcs, places, tours] = await Promise.all(
        ['meta.json', 'arcs.json', 'places.json', 'tours.json'].map(getJSON));
      this.meta = meta; this.arcs = arcs; this.places = places; this.tours = tours;
      this.careers = null; this.search = null;

      document.getElementById('m-officials').textContent = meta.roster.total.toLocaleString();
      document.getElementById('m-transfers').textContent = meta.counts.arcs.toLocaleString();
      document.getElementById('rail-co').textContent = meta.roster.co.toLocaleString();   // full roster
      document.getElementById('rail-io').textContent = meta.roster.io.toLocaleString();

      ATLAS.Arcs.init(map, document.getElementById('arc-canvas'));
      ATLAS.Arcs.setData(arcs, places);
      ATLAS.Places.init(map, places);
      ATLAS.Timeline.init(meta);
      ATLAS.Register.init();
      ATLAS.Search.init();
      ATLAS.Tours.init(tours);
      ATLAS.DeepQuery.init(meta);

      this.wireRail();
      ATLAS.Register.summary();
      ATLAS.Timeline.setYear(meta.yearRange[0], false);        // start empty — the intro builds it

      // guided entry: cinematic build of the whole century, then Willingdon
      setTimeout(() => ATLAS.Tours.startIntro(), 500);

      document.getElementById('reg-about').onclick = e => { e.preventDefault(); this.about(); };
    },

    wireRail() {
      this.corpus = { 0: true, 1: true };
      document.querySelectorAll('.svc').forEach(btn => {
        btn.onclick = () => {
          const c = +btn.dataset.corpus;
          this.corpus[c] = !this.corpus[c];
          if (!this.corpus[0] && !this.corpus[1]) { this.corpus[c] = true; return; }  // keep ≥1
          btn.classList.toggle('on', this.corpus[c]);
          ATLAS.Arcs.setCorpus(this.corpus);
        };
      });
      document.getElementById('rail-reset').onclick = () => this.reset();
    },

    async loadCareers() { if (!this.careers) this.careers = await getJSON('careers.json'); return this.careers; },
    async loadSearch() { if (!this.search) this.search = await getJSON('search.json'); return this.search; },

    async selectPerson(pid) {
      ATLAS.Tours.dismiss();
      await this.loadCareers();
      ATLAS.Register.person(pid);
    },
    selectPlace(qid) { ATLAS.Tours.dismiss(); ATLAS.Register.place(qid); },
    reset() {
      ATLAS.Arcs.clearHighlight(); ATLAS.Places.clearEmphasis(); ATLAS.Register.summary();
    },
    about() {
      ATLAS.Register.body.innerHTML = `
        <div class="reg-h">About &amp; sources</div>
        <p class="reg-lede">This atlas plots career transfers extracted from two printed serials —
          the <b>Colonial Office List</b> and the <b>India Office List</b> — digitised, OCR'd, and
          structured into a knowledge graph of officials, postings, places and dates.</p>
        <p class="reg-lede" style="font-size:14px">A “transfer” is one official's recorded move from
          one colony, presidency or province to another. Places are grounded to Wikidata; coordinates
          via QLever (P625). Only located postings appear here; the full record — roles, honours,
          education — lives in the live graph database behind the deep-query layer.</p>
        <p class="reg-lede" style="font-size:14px">Companion films:
          <a href="combined_mobility.mp4" target="_blank">Two Services, One Empire</a> ·
          <a href="iol_mobility.mp4" target="_blank">Moving the Raj</a> ·
          <a href="empire_mobility.mp4" target="_blank">Moving the Empire</a> ·
          <a href="grounded_places_map.html" target="_blank">grounded-places map</a>.</p>
        <p style="margin-top:18px"><a href="#" id="reg-back" style="color:var(--oxblood)">← back</a></p>`;
      document.getElementById('reg-back').onclick = e => { e.preventDefault(); this.reset(); };
    },
  };
  ATLAS.App = App;
  document.addEventListener('DOMContentLoaded', () => App.boot().catch(e => {
    console.error(e);
    document.getElementById('reg-body').innerHTML =
      '<div class="reg-h">Could not load</div><p class="reg-lede">The atlas data failed to load. ' +
      'If you opened this file directly, serve the folder over HTTP (e.g. <code>python3 -m http.server</code>).</p>';
  }));
})(window.ATLAS = window.ATLAS || {});
