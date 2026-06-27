/* register.js — the parchment "Record of Services" panel (the signature).
   Three states: summary (default + tours), a person's career set like the printed
   List (year-rail + postings, each lighting its arc), and a place corridor view. */
(function (ATLAS) {
  const el = id => document.getElementById(id);
  const esc = s => (s || '').replace(/[&<>]/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;' }[c]));
  const CORP = ['co', 'io'], CORPN = ['Colonial Office', 'India Office'];

  const Register = {
    init() { this.body = el('reg-body'); },

    summary() {
      ATLAS.Timeline.onYear = null;
      const m = ATLAS.App.meta, c = m.counts;
      const tours = ATLAS.App.tours.map((t, i) =>
        `<li data-tour="${i}"><div class="tl-t">${esc(t.title)}</div><div class="tl-b">${esc(t.blurb)}</div></li>`).join('');
      const moved = (m.movers.co + m.movers.io);
      this.body.innerHTML = `
        <div class="reg-h">The personnel of empire</div>
        <p class="reg-lede">Two civil services ran the British Empire. This atlas plots every
          colony or presidency that changed hands on an official's record — one move, one arc.</p>
        <div class="stat-row">
          <div class="stat"><b>${m.roster.total.toLocaleString()}</b><span>officials, ${m.yearRange[0]}–${m.yearRange[1]}</span></div>
          <div class="stat"><b>${moved.toLocaleString()}</b><span>moved between posts</span></div>
        </div>
        <div class="stat-row" style="margin-top:0">
          <div class="stat"><b style="color:#4f76ad">${m.roster.co.toLocaleString()}</b><span>Colonial Office</span></div>
          <div class="stat"><b style="color:#b07d24">${m.roster.io.toLocaleString()}</b><span>India Office</span></div>
          <div class="stat"><b>${c.arcs.toLocaleString()}</b><span>transfers mapped</span></div>
        </div>
        <div class="reg-h">Guided tours</div>
        <ul class="tour-list">${tours}</ul>`;
      this.body.querySelectorAll('[data-tour]').forEach(li =>
        li.onclick = () => ATLAS.Tours.start(+li.dataset.tour));
    },

    // one career's postings as a year-railed list (shared by person + bridge views).
    // The post name is the GROUNDED role label and is a click target -> everyone who
    // held that role at that colony.
    roleName(ri) { const r = ATLAS.App.careers.roles[ri]; return (r && r[1]) || 'in service'; },
    legRows(rec) {
      const places = ATLAS.App.places;
      return rec.st.map((st, i) => {
        const [col, y0, y1, ri, ac] = st;
        const yr = y1 && y1 !== y0 ? `${y0}–${String(y1).slice(2)}` : `${y0}`;
        const place = places[col] ? places[col].label : col;
        const acting = ac ? '<em>acting </em>' : '';
        return `<li class="ros-entry" data-leg="${i}" data-qid="${col}">
            <span class="yr">${yr}</span>
            <span class="pos">${acting}<a class="role-link" data-role="${ri}" data-col="${col}"
               title="who else held this post here">${esc(this.roleName(ri))}</a><span class="pl">${esc(place)}</span></span>
          </li>`;
      }).join('');
    },

    // a cross-corpus bridge across TIME + SPACE: one person's CO career (blue) and IO
    // career (gold), merged chronologically, with a two-lane career strip + a year
    // cursor, and "Trace career" to play the whole arc of postings through time.
    BR: ['#6f97cf', '#d59a3a'],
    bridge(b) {
      const C = ATLAS.App.careers; if (!C) return;
      const co = C.persons[b.co], io = C.persons[b.io], places = ATLAS.App.places;
      const legs = [];
      if (co) co.st.forEach(s => legs.push({ s, corp: 0 }));
      if (io) io.st.forEach(s => legs.push({ s, corp: 1 }));
      legs.sort((a, x) => (a.s[1] || 0) - (x.s[1] || 0) || a.corp - x.corp);
      const ys = legs.flatMap(l => [l.s[1], l.s[2] || l.s[1]]).filter(Boolean);
      const minY = Math.min(...ys), maxY = Math.max(...ys);

      const rows = legs.map((l, k) => {
        const [col, y0, y1, ri, ac] = l.s;
        const yr = y1 && y1 !== y0 ? `${y0}–${String(y1).slice(2)}` : `${y0}`;
        const place = places[col] ? places[col].label : col;
        return `<li class="ros-entry br-leg" data-qid="${col}" data-y="${y1 || y0}"
            style="border-left-color:${this.BR[l.corp]}">
            <span class="yr" style="color:${this.BR[l.corp]}">${yr}</span>
            <span class="pos">${ac ? '<em>acting </em>' : ''}<a class="role-link" data-role="${ri}" data-col="${col}"
               title="who else held this post here">${esc(this.roleName(ri))}</a><span class="pl">${esc(place)}</span></span>
          </li>`;
      }).join('');
      const qlink = b.co_qid ? ` · <a href="https://www.wikidata.org/wiki/${b.co_qid}" target="_blank" rel="noopener">${b.co_qid}</a>` : '';
      this.body.innerHTML = `
        <p class="ros-name">${esc(b.surname)}<span class="giv">${esc(b.name)}</span></p>
        <div class="ros-meta"><span class="corp" style="background:#6f6acb">Two services</span>
          <span>${b.birth ? 'b. ' + b.birth + ' · ' : ''}<span class="cf cf-${b.conf}">${b.conf}</span> ${esc(b.ev || '')}${qlink}</span></div>
        <div class="br-legend">
          <span><i style="background:${this.BR[0]}"></i>Colonial Office <b>${co ? co.st.length : 0}</b></span>
          <span><i style="background:${this.BR[1]}"></i>India Office <b>${io ? io.st.length : 0}</b></span>
          <button id="br-trace" title="Play this career through time">▶ Trace career</button></div>
        ${this.careerStrip(legs, minY, maxY)}
        <ul class="ros-list" style="margin-top:10px">${rows}</ul>
        <div id="role-people"></div>
        <p style="margin-top:12px"><a href="#" id="br-back" style="color:var(--oxblood)">← all bridge careers</a></p>`;
      this.wireRoleLinks();

      const idx = [...ATLAS.Arcs.indicesForPerson(b.co), ...ATLAS.Arcs.indicesForPerson(b.io)];
      ATLAS.Arcs.setHighlight(idx, true, true);            // dim web + reveal up to timeline year
      ATLAS.Timeline.setYear(maxY, false);                 // show the full career to start
      ATLAS.Timeline.onYear = y => this.moveCursor(y, minY, maxY);
      this.moveCursor(maxY, minY, maxY);
      this.body.querySelectorAll('.br-leg').forEach(li => {
        li.onmouseenter = () => { ATLAS.Places.emphasize(li.dataset.qid); ATLAS.Timeline.setYear(+li.dataset.y, false); };
        li.onmouseleave = () => { ATLAS.Places.clearEmphasis(); ATLAS.Timeline.setYear(maxY, false); };
        li.onclick = () => { const p = ATLAS.App.places[li.dataset.qid]; if (p) ATLAS.App.map.panTo([p.lat, p.lon]); };
      });
      document.getElementById('br-trace').onclick = () =>
        ATLAS.Timeline.playWindow(minY, maxY, Math.max(4500, (maxY - minY) * 340));
      document.getElementById('br-back').onclick = e => { e.preventDefault(); ATLAS.Bridges.open(); };
      this.fitTo(idx);
    },
    careerStrip(legs, minY, maxY) {
      const span = Math.max(1, maxY - minY), X = y => ((y - minY) / span) * 100;
      const segs = legs.map(l => {
        const x = X(l.s[1]), w = Math.max(0.7, X(Math.max(l.s[2] || l.s[1], l.s[1] + 0.7)) - x);
        return `<rect x="${x.toFixed(2)}" y="${l.corp ? 9.5 : 1}" width="${w.toFixed(2)}" height="6" rx="0.8" fill="${this.BR[l.corp]}"/>`;
      }).join('');
      let grid = '';
      for (let d = Math.ceil(minY / 10) * 10; d < maxY; d += 10)
        grid += `<line x1="${X(d).toFixed(2)}" y1="0" x2="${X(d).toFixed(2)}" y2="16.5" stroke="rgba(42,51,64,.13)" stroke-width="0.25"/>`;
      return `<div class="br-strip"><svg viewBox="0 0 100 16.5" preserveAspectRatio="none">${grid}${segs}
        <line id="br-cursor" x1="100" y1="0" x2="100" y2="16.5" stroke="var(--oxblood)" stroke-width="0.45"/></svg>
        <span class="br-cyr" id="br-cyr"></span>
        <span class="br-yr l">${minY}</span><span class="br-yr r">${maxY}</span></div>`;
    },
    moveCursor(y, minY, maxY) {
      const cur = document.getElementById('br-cursor'); if (!cur) return;
      const xn = Math.max(0, Math.min(100, ((y - minY) / Math.max(1, maxY - minY)) * 100));
      cur.setAttribute('x1', xn.toFixed(2)); cur.setAttribute('x2', xn.toFixed(2));
      const lbl = document.getElementById('br-cyr');
      if (lbl) { lbl.style.left = xn + '%'; lbl.textContent = Math.round(y); }
    },

    person(pid) {
      ATLAS.Timeline.onYear = null;
      const C = ATLAS.App.careers; if (!C) return;
      const rec = C.persons[pid]; if (!rec) return;
      const [sur, giv] = splitName(rec.nm || '');
      const legs = rec.st;
      const hidden = rec.na - legs.length;
      const rows = this.legRows(rec);
      const qlink = rec.q ? ` · <a href="https://www.wikidata.org/wiki/${rec.q}" target="_blank" rel="noopener">${rec.q}</a>` : '';
      this.body.innerHTML = `
        <p class="ros-name">${esc(sur) || '—'}<span class="giv">${esc(giv)}</span></p>
        <div class="ros-meta"><span class="corp" style="background:${rec.c ? '#b07d24' : '#4f76ad'}">${CORPN[rec.c]}</span>
          <span>${legs.length} located posting${legs.length !== 1 ? 's' : ''}${qlink}</span></div>
        <hr class="ros-rule">
        <ul class="ros-list">${rows}</ul>
        ${hidden > 0 ? `<p class="ros-note">${hidden} further posting${hidden !== 1 ? 's' : ''} in the record had no mapped location (UK, at sea, unplaced).</p>` : ''}
        <div id="role-people"></div>`;
      this.wireRoleLinks();

      const idx = ATLAS.Arcs.indicesForPerson(pid);
      const lastYr = legs.length ? Math.max(...legs.map(s => s[1] || s[0])) : ATLAS.Timeline.y1;
      ATLAS.Arcs.setHighlight(idx, true, true);           // focus + reveal by timeline year
      ATLAS.Timeline.setYear(lastYr, false);              // clock to the end of the career
      this.body.querySelectorAll('.ros-entry').forEach(li => {
        li.onmouseenter = () => {
          ATLAS.Places.emphasize(li.dataset.qid);
          const st = legs[+li.dataset.leg];
          ATLAS.Timeline.setYear(st[1] || st[0], false);  // run the clock to this posting
        };
        li.onmouseleave = () => { ATLAS.Places.clearEmphasis(); ATLAS.Timeline.setYear(lastYr, false); };
        li.onclick = () => { const p = ATLAS.App.places[li.dataset.qid]; if (p) ATLAS.App.map.panTo([p.lat, p.lon]); };
      });
      this.fitTo(idx);
    },

    place(qid) {
      ATLAS.Timeline.onYear = null;
      const p = ATLAS.App.places[qid]; if (!p) return;
      this.placeQid = qid;
      const arcs = ATLAS.Arcs.arcs, idx = ATLAS.Arcs.indicesForPlace(qid);
      // aggregate corridors by the OTHER place; track arrivals/departures + the people
      const corr = {}, ppl = new Set();
      for (const j of idx) {
        const a = arcs[j], other = a[1] === qid ? a[2] : a[1];
        const c = corr[other] || (corr[other] = { to: 0, from: 0, idx: [] });
        if (a[2] === qid) c.to++; else c.from++;       // to qid = arrival, from qid = departure
        c.idx.push(j); ppl.add(a[3]);
      }
      const rows = Object.entries(corr).sort((a, b) => (b[1].to + b[1].from) - (a[1].to + a[1].from))
        .slice(0, 16).map(([oq, c]) => {
          const name = ATLAS.App.places[oq] ? ATLAS.App.places[oq].label : oq;
          const dir = c.to && c.from ? '⇄' : (c.to ? '←' : '→');
          return `<li class="cor-row" data-other="${oq}"><span>${dir} ${esc(name)}</span><span class="ct">${c.to + c.from}</span></li>`;
        }).join('');
      const inN = p.co_in + p.io_in, outN = p.co_out + p.io_out;
      this.body.innerHTML = `
        <div class="reg-h">Corridor</div>
        <p class="ros-name" style="font-size:21px">${esc(p.label)}</p>
        ${p.seat && p.seat !== p.label ? `<div class="ros-meta"><span>seat of government: ${esc(p.seat)}</span></div>` : ''}
        <div class="stat-row">
          <div class="stat"><b>${inN}</b><span>arrivals</span></div>
          <div class="stat"><b>${outN}</b><span>departures</span></div>
          <div class="stat"><b>${ppl.size}</b><span>officials</span></div>
        </div>
        <div class="reg-h">Busiest corridors <span class="reg-hint">— click to list officials</span></div>
        <ul class="cor-list">${rows}</ul>
        <div id="cor-people"></div>`;
      ATLAS.Arcs.setHighlight(idx);
      ATLAS.Places.emphasize(qid);
      this.body.querySelectorAll('.cor-row').forEach(li =>
        li.onclick = () => this.corridorPeople(qid, li.dataset.other, corr[li.dataset.other].idx, li));
    },

    async corridorPeople(qid, otherQid, arcIdx, row) {
      this.body.querySelectorAll('.cor-row').forEach(r => r.classList.toggle('on', r === row));
      ATLAS.Arcs.setHighlight(arcIdx);                 // light just this corridor
      ATLAS.Places.emphasize(otherQid);
      const C = await ATLAS.App.loadCareers();
      const a = ATLAS.App.places[qid].label, b = (ATLAS.App.places[otherQid] || {}).label || otherQid;
      const seen = new Map();                          // pid -> {name, yrs:[]}
      for (const j of arcIdx) {
        const arc = ATLAS.Arcs.arcs[j], pid = arc[3];
        const rec = C.persons[pid];
        if (!seen.has(pid)) seen.set(pid, { nm: rec ? rec.nm : pid, yrs: [] });
        seen.get(pid).yrs.push(arc[0]);
      }
      const list = [...seen.entries()].sort((x, y) => x[1].nm.localeCompare(y[1].nm));
      const box = document.getElementById('cor-people');
      box.innerHTML = `<div class="reg-h" style="margin-top:16px">${esc(a)} ⇄ ${esc(b)} · ${list.length} official${list.length !== 1 ? 's' : ''}</div>
        <ul class="ppl-list">${list.map(([pid, v]) =>
          `<li data-pid="${pid}">${esc(v.nm)} <span class="py">${Math.min(...v.yrs)}</span></li>`).join('')}</ul>`;
      box.querySelectorAll('li[data-pid]').forEach(li =>
        li.onclick = () => ATLAS.App.selectPerson(li.dataset.pid));
      box.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
    },

    // role label -> everyone who held that role at that colony. Clicks are wired
    // for both the person and the bridge view; stop propagation so the row's
    // pan-to-place handler doesn't also fire.
    wireRoleLinks() {
      this.body.querySelectorAll('.role-link').forEach(a =>
        a.onclick = e => {
          e.preventDefault(); e.stopPropagation();
          this.rolePeople(+a.dataset.role, a.dataset.col, a);
        });
    },
    rolePeople(ri, colQid, anchor) {
      const C = ATLAS.App.careers; if (!C) return;
      this.body.querySelectorAll('.role-link').forEach(a => a.classList.toggle('on', a === anchor));
      const role = this.roleName(ri);
      const colLabel = ATLAS.App.places[colQid] ? ATLAS.App.places[colQid].label : colQid;
      const seen = new Map();                         // pid -> earliest year
      for (const pid in C.persons) {
        for (const s of C.persons[pid].st) {
          if (s[3] === ri && s[0] === colQid) {
            const y = s[1] || s[2];
            if (!seen.has(pid) || y < seen.get(pid)) seen.set(pid, y);
          }
        }
      }
      const list = [...seen.entries()]
        .map(([pid, y]) => ({ pid, nm: (C.persons[pid].nm || pid), y }))
        .sort((a, b) => (a.y || 9999) - (b.y || 9999) || a.nm.localeCompare(b.nm));
      const box = document.getElementById('role-people');
      box.innerHTML = `<div class="reg-h" style="margin-top:16px">${esc(role)} · ${esc(colLabel)}
          <span class="reg-hint">— ${list.length} official${list.length !== 1 ? 's' : ''}</span></div>
        <ul class="ppl-list">${list.map(v =>
          `<li data-pid="${v.pid}">${esc(v.nm)}${v.y ? ` <span class="py">${v.y}</span>` : ''}</li>`).join('')}</ul>`;
      box.querySelectorAll('li[data-pid]').forEach(li =>
        li.onclick = () => ATLAS.App.selectPerson(li.dataset.pid));
      box.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
    },

    fitTo(idx) {
      if (!idx.length) return;
      const pts = [];
      for (const j of idx) { const a = ATLAS.Arcs.arcs[j], P = ATLAS.App.places; if (P[a[1]]) pts.push([P[a[1]].lat, P[a[1]].lon]); if (P[a[2]]) pts.push([P[a[2]].lat, P[a[2]].lon]); }
      if (pts.length) ATLAS.App.map.fitBounds(pts, { padding: [80, 80], maxZoom: 5, paddingTopLeft: [40, 60], paddingBottomRight: [410, 110] });
    },
  };

  function splitName(disp) {
    const i = disp.indexOf(','); return i < 0 ? [disp, ''] : [disp.slice(0, i), disp.slice(i + 1).trim()];
  }
  ATLAS.Register = Register;
})(window.ATLAS = window.ATLAS || {});
