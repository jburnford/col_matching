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
      }).setView([24, 52], 2);   // open zoomed out on the whole web
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
      ATLAS.Bridges.init();
      ATLAS.DeepQuery.init(meta);

      this.wireRail();

      // deep link from the Education Atlas: ?p=<person_id> opens that career
      const want = new URLSearchParams(location.search).get('p');
      if (want) {
        ATLAS.Timeline.setYear(meta.yearRange[1], false);      // show the full web
        this.openPerson(want);
      } else {
        ATLAS.Register.summary();
        ATLAS.Timeline.setYear(meta.yearRange[0], false);      // start empty — the intro builds it
        setTimeout(() => ATLAS.Tours.startIntro(), 500);       // cinematic build, then Willingdon
      }
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
      document.getElementById('rail-bridges').onclick = () => ATLAS.Bridges.open();
    },

    async loadCareers() { if (!this.careers) this.careers = await getJSON('careers.json'); return this.careers; },
    async loadSearch() { if (!this.search) this.search = await getJSON('search.json'); return this.search; },

    async selectPerson(pid) {
      ATLAS.Tours.dismiss();
      await this.loadCareers();
      // a tour may list several editions of one official; show the first that
      // survived into the careers index rather than silently falling to summary
      const pids = Array.isArray(pid) ? pid : [pid];
      const found = pids.find(p => this.careers.persons && this.careers.persons[p]);
      ATLAS.Register.person(found || pids[0]);
    },
    // entry point for the ?p= deep link — verify the id exists, else fall back
    async openPerson(pid) {
      await this.loadCareers();
      if (this.careers.persons && this.careers.persons[pid]) ATLAS.Register.person(pid);
      else ATLAS.Register.summary();
    },
    selectPlace(qid) { ATLAS.Tours.dismiss(); ATLAS.Register.place(qid); },
    async selectCorridor(a, b) { ATLAS.Tours.dismiss(); await this.loadCareers(); ATLAS.Register.openCorridor(a, b); },
    async selectBridge(b) { ATLAS.Tours.dismiss(); await this.loadCareers(); ATLAS.Register.bridge(b); },
    reset() {
      ATLAS.Timeline.onYear = null;
      if (ATLAS.Timeline.timer) ATLAS.Timeline.stop();
      ATLAS.Arcs.clearHighlight(); ATLAS.Places.clearEmphasis();
      ATLAS.Timeline.setYear(ATLAS.Timeline.y1, false);   // restore the full-span web, not just the sidebar
      ATLAS.Register.summary();
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
