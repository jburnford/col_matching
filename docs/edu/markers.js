/* markers.js — education-institution markers over the night-atlas, CLUSTERED.
   Hundreds of schools pack into London/Oxford/Cambridge, so we use
   Leaflet.markercluster. Markers are L.marker+divIcon (markercluster can't
   cluster vector circleMarkers) styled to match the night-atlas discs: sized by
   sqrt(alumni in the selected decade), coloured by App.color() (kind | type).
   Clusters get custom icons sized by alumni-sum + coloured by aggregated
   dominant kind, so the visual language survives at low zoom. */
(function (ATLAS) {
  const Markers = {
    init(map, institutions) {
      this.map = map; this.inst = institutions;
      this.maxTotal = Math.max(...Object.values(institutions).map(r => r.total));
      this.cluster = L.markerClusterGroup({
        maxClusterRadius: 46, showCoverageOnHover: false,
        spiderfyOnMaxZoom: true, disableClusteringAtZoom: 12, chunkedLoading: true,
        iconCreateFunction: c => this.clusterIcon(c),
      }).addTo(map);
      this.render();
    },
    radius(rec) {
      const n = ATLAS.App.countFor(rec);
      if (!n) return 0;
      return 3 + 16 * Math.sqrt(n / this.maxTotal);
    },
    discIcon(r, col, approx) {
      const d = Math.max(6, Math.round(2 * r));
      const cls = approx ? 'im im-approx' : 'im';          // approx = city-centroid, dashed/hollow
      const bg = approx ? 'transparent' : col + '33';
      return L.divIcon({
        className: 'im-wrap', iconSize: [d, d], iconAnchor: [d / 2, d / 2],
        html: `<span class="${cls}" style="width:${d}px;height:${d}px;background:${bg};border-color:${col}"></span>`,
      });
    },
    render() {
      this.cluster.clearLayers(); this.markers = {};
      const batch = [];
      for (const [id, rec] of Object.entries(this.inst)) {
        const r = this.radius(rec);
        if (!r) continue;                                 // inactive this decade
        const col = ATLAS.App.color(rec);
        const m = L.marker([rec.lat, rec.lon], { icon: this.discIcon(r, col, rec.approx) });
        m.options.rec = rec; m.options.n = ATLAS.App.countFor(rec);
        m.on('click', () => ATLAS.App.selectInstitution(id));
        const dec = ATLAS.App.decade ? ` · ${ATLAS.App.decade}s` : '';
        m.bindTooltip(`${rec.label}<span style="opacity:.7"> · ${m.options.n}${dec}</span>`,
          { direction: 'top', className: 'inst-tip', offset: [0, -2] });
        this.markers[id] = m; batch.push(m);
      }
      this.cluster.addLayers(batch);
    },
    // cluster icon: size by summed alumni, colour by aggregated dominant kind/type
    clusterIcon(cluster) {
      const kids = cluster.getAllChildMarkers();
      let sum = 0; const agg = {};
      for (const m of kids) {
        sum += m.options.n || 0;
        const rec = m.options.rec;
        if (ATLAS.App.colorBy === 'type') {
          agg[rec.type] = (agg[rec.type] || 0) + m.options.n;
        } else {
          for (const [c, v] of Object.entries(rec.cats || {})) {
            if (c === 'other' || c === 'unknown') continue;
            agg[c] = (agg[c] || 0) + v;
          }
        }
      }
      const dom = Object.entries(agg).sort((a, b) => b[1] - a[1])[0];
      const m = ATLAS.App.meta;
      const col = dom ? (ATLAS.App.colorBy === 'type' ? m.type_color[dom[0]] : m.cat_color[dom[0]]) || '#888' : '#888';
      const d = Math.round(Math.max(22, Math.min(52, 16 + 7 * Math.log2(sum + 1))));
      return L.divIcon({
        className: 'im-cluster', iconSize: [d, d], iconAnchor: [d / 2, d / 2],
        html: `<span class="imc" style="width:${d}px;height:${d}px;background:${col}cc;border-color:${col}">${kids.length}</span>`,
      });
    },
    // reveal + ring a single institution (it may be hidden inside a cluster)
    emphasize(id) {
      const m = this.markers[id]; if (!m) return;
      this.clearEmphasis();
      const show = () => { const el = m.getElement(); if (el) el.classList.add('im-on'); };
      if (this.cluster.getVisibleParent(m) === m) { this.map.panTo(m.getLatLng()); show(); }
      else this.cluster.zoomToShowLayer(m, show);
    },
    clearEmphasis() {
      document.querySelectorAll('.im-wrap.im-on').forEach(e => e.classList.remove('im-on'));
    },
  };
  ATLAS.Markers = Markers;
})(window.ATLAS = window.ATLAS || {});
