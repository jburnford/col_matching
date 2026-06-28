/* panel.js — the parchment panel: overview (ranked feeders), institution detail
   (role-category breakdown + decades-active sparkline + alumni), and the
   local-schools tab (coverage-over-time, tail histogram, treemap, list).
   Reuses the careers-atlas register DOM idioms (.reg-h/.ppl-list/.rank). */
(function (ATLAS) {
  const A = () => ATLAS.App;
  const cap = s => s ? s.replace(/_/g, ' ') : s;
  const wdLink = id => id && id[0] === 'Q' ? ` · <a href="https://www.wikidata.org/wiki/${id}" target="_blank" rel="noopener">${id}</a>` : '';

  const Panel = {
    init() {
      this.body = document.getElementById('panel-body');
      this.view = { type: 'overview' };
      // unified index over mapped + local records (both carry cats/dominant/type)
      this.byId = Object.assign({}, A().institutions);
      A().local.forEach(r => { this.byId[r.id] = r; });
      this.wireSearch();
    },

    refresh() {
      if (this.view.type === 'detail') this.detail(this.view.id);
      else if (this.view.type === 'local') this.localTab();
      else this.overview();
    },

    // ---- colour swatch helper for a record -----------------------------
    col(rec) { return A().color(rec); },

    // ---- role-category breakdown bars ----------------------------------
    catBars(cats) {
      const cc = A().meta.cat_color;
      const ents = Object.entries(cats);
      const max = Math.max(1, ...ents.map(e => e[1]));
      return `<ul class="catbars">${ents.slice(0, 9).map(([c, n]) =>
        `<li class="catbar"><span class="cl">${cap(c)}</span>
           <span class="tr"><i style="width:${100 * n / max}%;background:${cc[c] || '#999'}"></i></span>
           <span class="vn">${n}</span></li>`).join('')}</ul>`;
    },

    // ================= OVERVIEW (mapped tab) ===========================
    overview() {
      this.view = { type: 'overview' };
      const m = A().meta;
      const top = m.top.filter(r => r.grounded).slice(0, 22);
      const maxT = top[0] ? top[0].total : 1;
      this.body.innerHTML = `
        <div class="reg-h">Educating the administrators</div>
        <p class="reg-lede">Where the officials of the <b>Colonial Office</b> and
          <b>India Office</b> were schooled — and what <em>kind</em> of official each
          institution produced. Markers are sized by alumni and coloured by their
          commonest role. Click a decade below to watch the pipeline shift.</p>
        <div class="stat-row">
          <div class="stat"><b>${m.mapped.toLocaleString()}</b><span>mapped institutions</span></div>
          <div class="stat"><b>${m.local.toLocaleString()}</b><span>local schools (tail →)</span></div>
        </div>
        <div class="sub-h">Top feeders ${A().decade ? '· ' + A().decade + 's' : ''}</div>
        <ul class="rank">${top.map(r => this.rankRow(r, maxT)).join('')}</ul>`;
      this.wireRank();
    },

    rankRow(r, maxT) {
      const rec = this.byId[r.id] || r;
      const n = A().countFor(rec) || r.total;
      return `<li data-id="${r.id}">
        <span class="nm">${r.label}<span class="ty">${cap(r.type)}</span></span>
        <span class="ct">${n}</span>
        <span class="bar"><i style="width:${100 * (n / maxT)}%;background:${this.col(rec)}"></i></span>
      </li>`;
    },
    wireRank() {
      this.body.querySelectorAll('.rank li').forEach(li =>
        li.onclick = () => A().selectInstitution(li.dataset.id));
    },

    // one alumnus -> links to the careers atlas (index.html?p=<id>)
    alumnusRow(p) {
      const named = p.name && p.name !== p.id;
      const label = named ? p.name : '⟨name not recorded⟩';
      const wd = p.qid ? ` · <a href="https://www.wikidata.org/wiki/${p.qid}" target="_blank" rel="noopener" class="wd">WD</a>` : '';
      return `<li><a class="al" href="index.html?p=${encodeURIComponent(p.id)}" target="_blank" rel="noopener"
        title="See ${named ? p.name + "'s" : 'this'} career in the Atlas of Imperial Careers">${label}</a>
        <span class="pc ${p.corpus}">${p.corpus}${p.top_cat ? ' · ' + p.top_cat : ''}${wd}</span></li>`;
    },

    // ================= INSTITUTION DETAIL ==============================
    detail(id) {
      this.view = { type: 'detail', id };
      const rec = this.byId[id]; if (!rec) return;
      const alumni = (A().alumni && A().alumni[id]) || [];
      if (rec.lat) { ATLAS.Markers.emphasize(id); ATLAS.Arcs.setHighlight(id); }

      // feeder pipeline: institutions whose alumni also attended this one
      const links = (ATLAS.Arcs.adj[id] || []).slice(0, 8);
      const inst = A().institutions;
      const linksHtml = links.length ? `
        <div class="sub-h">Shared alumni with</div>
        <ul class="rank">${links.map(([q, w]) => inst[q] ? `
          <li data-id="${q}"><span class="nm">${inst[q].label}<span class="ty">${cap(inst[q].type)}</span></span>
            <span class="ct">${w}</span>
            <span class="bar"><i style="width:${100 * w / links[0][1]}%;background:${this.col(inst[q])}"></i></span></li>` : '').join('')}</ul>` : '';

      let spark = '';
      if (rec.by_decade) {
        const decs = A().stream.decades;
        const max = Math.max(1, ...Object.values(rec.by_decade));
        spark = `<div class="sub-h">Alumni in service, by decade</div>
          <div class="spark">${decs.map(d =>
            `<div class="sb" title="${d}s: ${rec.by_decade[d] || 0}" style="height:${100 * ((rec.by_decade[d] || 0) / max)}%"></div>`).join('')}</div>
          <div class="spark-x"><span>${decs[0]}</span><span>${decs[decs.length - 1]}</span></div>`;
      }
      const back = `<span class="det-back">← back</span>`;
      this.body.innerHTML = `
        <p>${back}</p>
        <h2 class="det-name">${rec.label}</h2>
        <div class="det-meta">
          <span>${cap(rec.type)}</span>
          <span>CO ${rec.co} · IO ${rec.io}</span>
          <span>${rec.total} alumni</span>
          ${rec.approx ? '<span title="No campus coordinate in Wikidata — plotted at the city/region centroid">≈ approx. location</span>' : ''}
          ${rec.lat ? '' : '<span title="not on the map">⚑ unmapped</span>'}
          ${wdLink(id)}
        </div>
        <div class="sub-h">Kind of official produced</div>
        ${this.catBars(rec.cats)}
        ${spark}
        ${linksHtml}
        <div class="sub-h">Alumni ${alumni.length >= 60 ? '(top 60 by career length)' : ''}
          <span style="font-weight:400;text-transform:none;letter-spacing:0"> · click to see a career →</span></div>
        <ul class="ppl-list">${alumni.map(p => this.alumnusRow(p)).join('')
          || '<li style="cursor:default">—</li>'}</ul>`;
      this.body.querySelectorAll('.rank li').forEach(li =>
        li.onclick = () => A().selectInstitution(li.dataset.id));
      this.body.querySelector('.det-back').onclick = () => {
        ATLAS.Markers.clearEmphasis(); ATLAS.Arcs.setHighlight(null);
        this.view.from === 'local' ? this.localTab() : this.overview();
      };
    },

    // ================= LOCAL-SCHOOLS TAB ===============================
    localTab() {
      this.view = { type: 'local' };
      const m = A().meta, cov = A().stream.coverage, decs = A().stream.decades;
      const local = A().local;

      // coverage stacked bars (grounded vs local-school alumni, per decade)
      const covMax = Math.max(1, ...decs.map(d => (cov[d].grounded + cov[d].local)));
      const covBars = decs.map(d => {
        const g = cov[d].grounded, l = cov[d].local, h = (g + l) / covMax * 100;
        const lp = (g + l) ? l / (g + l) * 100 : 0;
        return `<div class="sb" title="${d}s — local ${l} / grounded ${g}"
          style="height:${h}%;background:linear-gradient(to top,#9a8a64 ${100 - lp}%,var(--oxblood) ${100 - lp}%)"></div>`;
      }).join('');

      // tail histogram (#institutions by alumni count)
      const hist = m.tail.hist, keys = Object.keys(hist);
      const hmax = Math.max(...Object.values(hist));
      const hbars = keys.map(k =>
        `<div class="hb ${k === '1' ? 'one' : ''}" title="${k === '10' ? '10+' : k} alumni: ${hist[k]} schools"
           style="height:${100 * hist[k] / hmax}%"></div>`).join('');

      this.body.innerHTML = `
        <div class="reg-h">The long tail of local schools</div>
        <p class="reg-lede">Beyond the famous feeders lie <b>${m.local.toLocaleString()}</b>
          schools and colleges Wikidata doesn't know — local grammar schools, colonial
          colleges, technical institutes. <b>${m.tail.singletons.toLocaleString()}</b> appear
          just once in the record.</p>
        <div class="sub-h">A tail that grows · local vs. grounded alumni, by decade</div>
        <div class="spark">${covBars}</div>
        <div class="spark-x"><span>${decs[0]}</span><span>${decs[decs.length - 1]}</span></div>
        <p class="cov-note">As the empire's bureaucracy expanded, an ever larger share of its
          officials came from schools beyond the metropolitan core.</p>
        <div class="sub-h">Schools by number of alumni</div>
        <div class="tail-hist">${hbars}</div>
        <div class="tail-x"><span>1</span><span>2</span><span>…</span><span>10+</span></div>
        <div class="sub-h">Largest local schools — click to inspect</div>
        <svg id="treemap"></svg>
        <ul class="rank">${local.slice(0, 50).map(r =>
          `<li data-id="${r.id}"><span class="nm">${r.label}<span class="ty">${cap(r.type)}</span></span>
             <span class="ct">${r.total}</span>
             <span class="bar"><i style="width:${100 * r.total / local[0].total}%;background:${this.col(r)}"></i></span></li>`).join('')}</ul>`;
      this.drawTreemap(local.slice(0, 70));
      this.body.querySelectorAll('.rank li').forEach(li =>
        li.onclick = () => { this.view.from = 'local'; A().selectInstitution(li.dataset.id).then(() => { this.view.from = 'local'; }); });
    },

    drawTreemap(items) {
      const el = document.getElementById('treemap'); if (!el || !window.d3) return;
      const w = el.clientWidth || 360, h = 200;
      const root = d3.hierarchy({ children: items }).sum(d => d.total)
        .sort((a, b) => b.value - a.value);
      d3.treemap().size([w, h]).paddingInner(1)(root);
      const svg = d3.select(el).attr('viewBox', `0 0 ${w} ${h}`);
      svg.selectAll('*').remove();
      const g = svg.selectAll('g').data(root.leaves()).join('g')
        .attr('transform', d => `translate(${d.x0},${d.y0})`)
        .style('cursor', 'pointer')
        .on('click', (e, d) => { this.view.from = 'local'; A().selectInstitution(d.data.id); });
      g.append('rect').attr('width', d => d.x1 - d.x0).attr('height', d => d.y1 - d.y0)
        .attr('fill', d => this.col(d.data))
        .append('title').text(d => `${d.data.label} — ${d.data.total}`);
      g.append('text').attr('x', 3).attr('y', 12).attr('font-size', 9)
        .text(d => (d.x1 - d.x0) > 46 && (d.y1 - d.y0) > 14 ? d.data.label.slice(0, ((d.x1 - d.x0) / 5) | 0) : '');
    },

    // ================= SEARCH ==========================================
    wireSearch() {
      const box = document.getElementById('search-box'), out = document.getElementById('search-results');
      const idx = Object.entries(this.byId).map(([id, r]) => ({ id, l: r.label, ll: r.label.toLowerCase(), t: r.type, n: r.total }));
      const run = () => {
        const q = box.value.trim().toLowerCase();
        if (q.length < 2) { out.hidden = true; return; }
        const pre = [], sub = [];
        for (const e of idx) { const i = e.ll.indexOf(q); if (i === 0) pre.push(e); else if (i > 0) sub.push(e); }
        const hits = pre.concat(sub).sort((a, b) => b.n - a.n).slice(0, 40);
        out.innerHTML = hits.map(e =>
          `<li data-id="${e.id}"><span class="nm">${e.l}</span><span class="tag">${cap(e.t)} · ${e.n}</span></li>`).join('');
        out.hidden = !hits.length;
        out.querySelectorAll('li').forEach(li => li.onclick = () => {
          box.value = ''; out.hidden = true; A().selectInstitution(li.dataset.id);
        });
      };
      box.addEventListener('input', run);
      box.addEventListener('focus', run);
      document.addEventListener('click', e => { if (!e.target.closest('#panel-search')) out.hidden = true; });
    },
  };
  ATLAS.Panel = Panel;
})(window.ATLAS = window.ATLAS || {});
