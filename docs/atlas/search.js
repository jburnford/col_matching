/* search.js — lazy person search over search.json (loaded on first focus). */
(function (ATLAS) {
  const Search = {
    init() {
      this.box = document.getElementById('search-box');
      this.list = document.getElementById('search-results');
      this.data = null; this.loading = false;
      this.box.addEventListener('focus', () => this.ensure());
      this.box.addEventListener('input', () => this.run());
      this.box.addEventListener('keydown', e => this.key(e));
      document.addEventListener('click', e => { if (!e.target.closest('#reg-search')) this.hide(); });
    },
    async ensure() {
      if (this.data || this.loading) return;
      this.loading = true;
      try { this.data = await ATLAS.App.loadSearch(); }
      finally { this.loading = false; }
    },
    run() {
      const q = this.box.value.trim().toLowerCase();
      if (!this.data || q.length < 2) return this.hide();
      const starts = [], contains = [];
      for (const r of this.data) {
        const n = r[1].toLowerCase();
        if (n.startsWith(q)) starts.push(r);
        else if (n.includes(q)) contains.push(r);
        if (starts.length > 60) break;
      }
      const res = starts.concat(contains).slice(0, 40)
        .sort((a, b) => b[3] - a[3]);                          // more postings first
      this.render(res);
    },
    render(res) {
      if (!res.length) { this.list.innerHTML = '<li style="cursor:default;color:#8a7f66">No official by that name.</li>'; this.list.hidden = false; return; }
      const C = ['co', 'io'], CN = ['CO', 'IO'];
      this.list.innerHTML = res.map((r, i) =>
        `<li data-pid="${r[0]}" data-i="${i}"><span class="nm">${r[1]}</span><span class="tag ${C[r[2]]}">${CN[r[2]]} · ${r[3]}</span></li>`).join('');
      this.list.hidden = false; this.sel = -1;
      this.list.querySelectorAll('li[data-pid]').forEach(li =>
        li.onclick = () => this.pick(li.dataset.pid));
    },
    key(e) {
      const items = [...this.list.querySelectorAll('li[data-pid]')]; if (!items.length) return;
      if (e.key === 'ArrowDown' || e.key === 'ArrowUp') {
        e.preventDefault(); this.sel = (this.sel + (e.key === 'ArrowDown' ? 1 : -1) + items.length) % items.length;
        items.forEach((li, i) => li.classList.toggle('sel', i === this.sel));
      } else if (e.key === 'Enter') {
        e.preventDefault(); const li = items[this.sel] || items[0]; if (li) this.pick(li.dataset.pid);
      } else if (e.key === 'Escape') this.hide();
    },
    pick(pid) { this.hide(); this.box.blur(); ATLAS.App.selectPerson(pid); },
    hide() { this.list.hidden = true; },
  };
  ATLAS.Search = Search;
})(window.ATLAS = window.ATLAS || {});
