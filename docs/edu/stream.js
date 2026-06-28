/* stream.js — decade streamgraph: stacked area of WHAT KIND of official the
   educated cohort became, by decade. Catch-all 'other'/'unknown' are excluded
   so the meaningful kinds read. Click a decade to filter the map + panel. */
(function (ATLAS) {
  const M = { t: 6, r: 8, b: 14, l: 30 };

  const Stream = {
    init(data, meta) {
      this.meta = meta;
      this.decades = data.decades;
      this.cats = meta.cat_order.filter(c => c !== 'other' && c !== 'unknown');
      // rows: [{decade, <cat>:v, ...}]
      this.rows = data.decades.map((dec, i) => {
        const row = { decade: dec };
        this.cats.forEach(c => row[c] = (data.series[c] || [])[i] || 0);
        return row;
      });
      this.svg = d3.select('#stream-svg');
      this.draw();
      window.addEventListener('resize', () => this.draw());
    },

    draw() {
      const el = document.getElementById('stream-svg');
      const w = el.clientWidth, h = el.clientHeight;
      if (!w || !h) return;
      const decs = this.decades, cats = this.cats, cc = this.meta.cat_color;
      const x = d3.scaleLinear().domain([decs[0], decs[decs.length - 1]]).range([M.l, w - M.r]);
      const stacked = d3.stack().keys(cats)(this.rows);
      const ymax = d3.max(stacked[stacked.length - 1], d => d[1]) || 1;
      const y = d3.scaleLinear().domain([0, ymax]).range([h - M.b, M.t]);
      const area = d3.area().x(d => x(d.data.decade)).y0(d => y(d[0])).y1(d => y(d[1])).curve(d3.curveBasis);

      const svg = this.svg; svg.selectAll('*').remove();
      this.x = x; this.w = w; this.h = h;

      // stacked areas
      svg.append('g').selectAll('path').data(stacked).join('path')
        .attr('class', 'area').attr('fill', s => cc[s.key]).attr('d', area)
        .append('title').text(s => s.key);

      // decade axis labels
      const gx = svg.append('g');
      decs.forEach(d => {
        if (d % 20 === 0)
          gx.append('text').attr('class', 'dec-label').attr('x', x(d)).attr('y', h - 3)
            .attr('text-anchor', 'middle').text(`${d}`.slice(2) === '00' ? d : `'${`${d}`.slice(2)}`);
      });

      // selection highlight (under the hit rects)
      this.selG = svg.append('g');

      // per-decade hit rects (hover + click)
      const step = (x(decs[1]) - x(decs[0]));
      svg.append('g').selectAll('rect').data(decs).join('rect')
        .attr('x', d => x(d) - step / 2).attr('y', M.t).attr('width', step).attr('height', h - M.b - M.t)
        .attr('fill', 'transparent')
        .on('mouseover', function () { d3.select(this).attr('class', 'dec-hover'); })
        .on('mouseout', function () { d3.select(this).attr('class', null).attr('fill', 'transparent'); })
        .on('click', (e, d) => ATLAS.App.setDecade(d));

      this.setSelected(ATLAS.App.decade);
    },

    setSelected(dec) {
      if (!this.selG) return;
      this.selG.selectAll('*').remove();
      if (!dec) return;
      const decs = this.decades, x = this.x;
      const step = (x(decs[1]) - x(decs[0]));
      this.selG.append('rect').attr('class', 'dec-sel')
        .attr('x', x(dec) - step / 2).attr('y', M.t)
        .attr('width', step).attr('height', this.h - M.b - M.t);
    },
  };
  ATLAS.Stream = Stream;
})(window.ATLAS = window.ATLAS || {});
