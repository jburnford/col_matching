/* deepquery.js — live Neo4j research layer (Phase 2).
   Pings the read-only Query API named in meta.neo4j.queryApiUrl; if absent or
   unreachable, the badge stays "offline" and the static core is unaffected.
   Raw-Cypher exposure is intentionally NOT wired here — the production endpoint
   should front named/parameterized queries via the TLS allowlisting proxy. */
(function (ATLAS) {
  const DeepQuery = {
    async init(meta) {
      this.url = meta && meta.neo4j && meta.neo4j.queryApiUrl;
      this.badge = document.getElementById('neo-badge');
      this.online = false;
      if (!this.url) { this.setBadge(false); return; }
      try {
        const r = await this.run('RETURN 1 AS ok', {}, 4000);
        this.online = !!r; this.setBadge(this.online);
      } catch { this.setBadge(false); }
    },
    setBadge(on) {
      this.badge.classList.toggle('on', on);
      this.badge.textContent = on ? 'deep query: live' : 'deep query: offline';
      this.badge.title = on ? 'Connected to the live graph database' :
        'Live graph database unavailable — the atlas runs fully on its precomputed data.';
    },
    async run(statement, parameters = {}, timeout = 10000) {
      if (!this.url) throw new Error('no endpoint');
      const ctrl = new AbortController(); const t = setTimeout(() => ctrl.abort(), timeout);
      try {
        const res = await fetch(this.url, {
          method: 'POST', signal: ctrl.signal,
          headers: { 'Content-Type': 'application/json', 'Accept': 'application/json' },
          body: JSON.stringify({ statement, parameters }),
        });
        if (!res.ok) throw new Error('HTTP ' + res.status);
        return await res.json();
      } finally { clearTimeout(t); }
    },
  };
  ATLAS.DeepQuery = DeepQuery;
})(window.ATLAS = window.ATLAS || {});
