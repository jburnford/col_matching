#!/usr/bin/env python3
"""Publish the gazetteer's record IDs as one static page with an anchor per place.

Every LPF `@id` is https://jimclifford.ca/col_matching/whg/places/#<id>, so this
single page makes all of them resolve on GitHub Pages without thousands of
files. Reads the public LP-TSV only (no people, no careers).

    python3 build_whg_places_page.py   # after build_whg_gazetteer.py
"""
import argparse
import csv
import html
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
FCLASS = {"A": "administrative area", "P": "populated place", "H": "water", "T": "landform",
          "L": "region", "S": "site", "R": "route"}

STYLE = """
  :root{--ink:#0E1622;--paper:#E7DCC4;--paper-2:#DBCDAE;--oxblood:#7A2E2A;
    --slate:#2A3340;--slate-2:#5b6675;
    --serif:"Newsreader",Georgia,"Times New Roman",serif;
    --mono:"IBM Plex Mono",ui-monospace,Menlo,Consolas,monospace}
  *{box-sizing:border-box}
  html,body{margin:0;background:var(--ink);color:var(--slate);font-family:var(--serif)}
  body{display:flex;justify-content:center;padding:clamp(24px,5vw,64px) 18px}
  main{width:100%;max-width:900px;background:var(--paper);border:1px solid var(--paper-2);
    border-radius:3px;padding:clamp(26px,4vw,48px)}
  .kicker{font-family:var(--mono);font-size:11px;letter-spacing:.18em;text-transform:uppercase;
    color:var(--oxblood);margin:0 0 .5em}
  h1{font-weight:400;font-size:clamp(26px,4vw,36px);margin:0 0 .3em;color:#1c2531}
  p{font-size:16px;line-height:1.55;margin:0 0 1em}
  a{color:var(--oxblood)}
  input{font-family:var(--mono);font-size:14px;width:100%;padding:8px;margin:0 0 1.2em;
    border:1px solid var(--paper-2);background:#f3ecdc}
  article{border-top:1px solid var(--paper-2);padding:.7em 0 .6em;scroll-margin-top:12px}
  article:target{background:#f3ecdc;outline:2px solid var(--oxblood);outline-offset:4px}
  h2{font-weight:500;font-size:19px;margin:0;color:#1c2531}
  .id,.meta{font-family:var(--mono);font-size:12px;color:var(--slate-2)}
  .meta{margin:.2em 0 0}
"""


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--tsv", type=Path, default=ROOT / "out/whg/whg-places.tsv")
    parser.add_argument("--out", type=Path, default=ROOT / "docs/whg/places/index.html")
    args = parser.parse_args()
    with args.tsv.open(encoding="utf-8") as handle:
        rows = sorted(csv.DictReader(handle, delimiter="\t"), key=lambda r: (r["title"].casefold(), r["id"]))
    labels = {}
    places = args.tsv.with_name("places.jsonl")
    if places.exists():
        for line in places.open(encoding="utf-8"):
            rec = json.loads(line)
            labels[rec["id"]] = rec.get("wikidata_label")
    parts = []
    for r in rows:
        e = html.escape
        span = r["start"] + (f"–{r['end']}" if r["end"] else "") if r["start"] else ""
        kind = ", ".join(FCLASS.get(c, c) for c in r["fclasses"].split(";") if c)
        links = []
        if r["matches"]:
            q = r["matches"].split(":", 1)[1]
            links.append(f'<a href="https://www.wikidata.org/wiki/{e(q)}">Wikidata {e(q)}</a>')
        if r["lon"]:
            links.append(f'{float(r["lat"]):.3f}, {float(r["lon"]):.3f}')
        variants = ", ".join(v.rsplit("@", 1)[0] for v in r["variants"].split(";") if v)
        parent = f' · in {e(r["parent_name"])}' if r["parent_name"] else ""
        parts.append(
            f'<article id="{e(r["id"])}"><h2>{e(r["title"])}'
            f'{" <small>(" + e(labels[r["id"]]) + ")</small>" if labels.get(r["id"]) and labels[r["id"]] != r["title"] else ""}</h2>'
            f'<div class="id">{e(r["id"])}</div>'
            f'<p class="meta">{e(kind)}{parent}{" · references " + e(span) if span else ""}'
            f'{" · " + " · ".join(links) if links else ""}</p>'
            f'<p class="meta">First printed: {e(r["title_source"])}'
            f'{" · also printed as " + e(variants) if variants else ""}</p></article>')
    page = f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Places · An Atlas of Imperial Careers</title>
<meta name="description" content="Gazetteer of places named in Colonial Office and India Office List biographies, 1862–1966.">
<link href="https://fonts.googleapis.com/css2?family=Newsreader:wght@400;500&family=IBM+Plex+Mono:wght@400;600&display=swap" rel="stylesheet">
<style>{STYLE}</style></head>
<body><main>
<p class="kicker">Atlas of Imperial Careers · Gazetteer</p>
<h1>Places named in the Colonial Office and India Office Lists</h1>
<p>{len(rows):,} places named in the printed records of services, 1862–1966. Each entry is a
record of the contribution to the <a href="https://whgazetteer.org">World Historical Gazetteer</a>;
its address is this page plus <code>#id</code>. Dates are the span of dated career references, not
the place's existence. Data: CC0 · <a href="../../about.html">About the atlas</a> ·
<a href="https://github.com/jburnford/col_matching/tree/master/research/whg-gazetteer-2026-10-16">files</a>.</p>
<input id="q" type="search" placeholder="Filter by name…" aria-label="Filter places by name">
<div id="list">
{chr(10).join(parts)}
</div>
<script>
const q=document.getElementById('q'),items=[...document.querySelectorAll('article')];
q.addEventListener('input',()=>{{const t=q.value.toLowerCase();
  for(const a of items)a.hidden=t&&!a.textContent.toLowerCase().includes(t);}});
</script>
</main></body></html>
"""
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(page, encoding="utf-8")
    print(f"wrote {args.out} ({len(rows):,} places, {args.out.stat().st_size / 1e6:.1f} MB)")


if __name__ == "__main__":
    main()
