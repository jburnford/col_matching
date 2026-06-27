/* places.js — presidency/province/colony markers over the night-atlas.
   Adapted from build_place_map.py: circle markers sized by sqrt(traffic),
   coloured by the dominant service. Click → corridor view + arc highlight. */
(function (ATLAS) {
  const Places = {
    init(map, places) {
      this.map = map; this.places = places;
      this.layer = L.layerGroup().addTo(map);
      const vals = Object.values(places).map(p => p.co_in + p.co_out + p.io_in + p.io_out);
      this.max = Math.max(...vals);
      this.render();
    },
    render() {
      this.layer.clearLayers(); this.markers = {};
      for (const [qid, p] of Object.entries(this.places)) {
        const co = p.co_in + p.co_out, io = p.io_in + p.io_out, tot = co + io;
        if (!tot) continue;
        const col = co >= io ? '#8FB8EE' : '#E8B24C';
        const r = 3 + 15 * Math.sqrt(tot / this.max);
        const m = L.circleMarker([p.lat, p.lon], {
          radius: r, color: col, weight: 1, opacity: .75,
          fillColor: col, fillOpacity: .14,
        }).addTo(this.layer);
        m.on('click', () => ATLAS.App.selectPlace(qid));
        m.on('mouseover', () => m.setStyle({ fillOpacity: .4, weight: 1.5 }));
        m.on('mouseout', () => m.setStyle({ fillOpacity: .14, weight: 1 }));
        const tip = p.seat && p.seat !== p.label ? `${p.label}<span style="opacity:.7"> · ${p.seat}</span>` : p.label;
        m.bindTooltip(tip, { direction: 'top', className: 'place-tip', offset: [0, -2] });
        this.markers[qid] = m;
      }
    },
    emphasize(qid) {
      for (const [q, m] of Object.entries(this.markers))
        m.setStyle({ fillOpacity: q === qid ? .55 : .07, opacity: q === qid ? 1 : .35 });
    },
    clearEmphasis() {
      const ps = this.places;
      for (const [q, m] of Object.entries(this.markers)) {
        const p = ps[q], co = p.co_in + p.co_out, io = p.io_in + p.io_out;
        m.setStyle({ fillOpacity: .14, opacity: .75, color: co >= io ? '#8FB8EE' : '#E8B24C' });
      }
    },
  };
  ATLAS.Places = Places;
})(window.ATLAS = window.ATLAS || {});
