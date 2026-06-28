#!/usr/bin/env python3
"""Render the school-blocked dedup candidates into a review page.

Reads data/kg + data/iol dedup_school_candidates.jsonl (from
kg_dedup_school_candidates.py) → docs/edu_dedup_review.html. Each cluster is a
card grouped by disposition (conflict → review → confident → likely); every
member links to its career in the careers atlas (index.html?p=<id>) so the
reviewer can adjudicate. Nothing here mutates the KG — apply is a later step.
"""
import json
from pathlib import Path

CORPORA = [("Colonial Office", Path("data/kg")), ("India Office", Path("data/iol"))]
OUT = Path("docs/edu_dedup_review.html")
DISP = {"conflict": ("Birth-year conflict — likely SPLIT / father–son", "#7A2E2A"),
        "review": ("Needs a ruling — edition gap, no birth/shared posting", "#b07d24"),
        "confident": ("Confident — matched birth year or shared posting", "#3f7d4e"),
        "likely": ("Likely — OCR/initials variant, overlapping editions", "#4f76ad")}


def schools_index():
    idx = {}
    for f in (Path("docs/data_edu/institutions.json"),):
        if f.exists():
            for q, r in json.load(open(f)).items():
                idx[q] = r["label"]
    return idx


def main():
    sidx = schools_index()
    cards = []
    totals = {}
    for cname, root in CORPORA:
        fn = root / "dedup_school_candidates.jsonl"
        if not fn.exists():
            continue
        clusters = [json.loads(l) for l in open(fn)]
        for c in clusters:
            totals[(cname, c["disposition"])] = totals.get((cname, c["disposition"]), 0) + 1
            cards.append((cname, c))
    order = {"conflict": 0, "review": 1, "confident": 2, "likely": 3}
    cards.sort(key=lambda cc: (order[cc[1]["disposition"]], cc[0]))

    def member_html(m):
        ed = f"{m['editions'][0]}–{m['editions'][1]}" if m.get("editions") else "—"
        return (f"<tr><td class='nm'><a href='index.html?p={m['id']}' target='_blank'>"
                f"{(m['surname'] or '?')}, <span class='giv'>{m['given'] or ''}</span></a></td>"
                f"<td>b. {m['birth'] or '—'}</td><td>{ed}</td><td>{m['n'] or 0}×</td></tr>")

    def card_html(cname, c):
        label, col = DISP[c["disposition"]]
        sch = ", ".join(sidx.get(s, s) for s in c["schools"][:3])
        rows = "".join(member_html(m) for m in c["members"])
        return (f"<div class='card' data-disp='{c['disposition']}' data-corpus='{cname}'>"
                f"<div class='cd-h' style='border-color:{col}'><span class='badge' style='background:{col}'>"
                f"{c['disposition']}</span> <span class='corp'>{cname}</span>"
                f"<span class='sch'>shared: {sch}</span></div>"
                f"<table>{rows}</table></div>")

    summary = "".join(
        f"<div class='sx'><b>{cname}</b> "
        + " · ".join(f"<span style='color:{DISP[d][1]}'>{d} {totals.get((cname, d), 0)}</span>"
                     for d in ("conflict", "review", "confident", "likely"))
        + "</div>" for cname, _ in CORPORA)

    html = f"""<!DOCTYPE html><html lang=en><head><meta charset=utf-8>
<meta name=viewport content="width=device-width,initial-scale=1">
<title>School-blocked dedup — review</title>
<style>
 body{{margin:0;background:#0E1622;color:#e7eef6;font:14px/1.5 ui-sans-serif,system-ui,sans-serif}}
 header{{padding:20px 28px;border-bottom:1px solid #243}}
 h1{{margin:0 0 6px;font:400 24px/1.1 "Newsreader",Georgia,serif;color:#fbf4e3}}
 .lede{{color:#9fb0c4;max-width:60em}}
 .sx{{margin-top:8px;font-family:ui-monospace,monospace;font-size:12px}}
 .filters{{padding:12px 28px;position:sticky;top:0;background:#0E1622;border-bottom:1px solid #243;z-index:2}}
 .filters button{{background:#16202e;color:#cdd7e3;border:1px solid #2a3a4c;border-radius:4px;
   padding:5px 11px;margin-right:6px;font-size:12px;cursor:pointer}}
 .filters button.on{{background:#243a52;color:#fff;border-color:#5a7da0}}
 main{{padding:18px 28px;display:grid;grid-template-columns:repeat(auto-fill,minmax(340px,1fr));gap:12px}}
 .card{{background:#121c28;border:1px solid #223;border-radius:6px;overflow:hidden}}
 .cd-h{{padding:8px 10px;border-left:4px solid;display:flex;align-items:center;gap:8px;flex-wrap:wrap;font-size:12px}}
 .badge{{color:#fff;font:600 10px/1 ui-monospace,monospace;text-transform:uppercase;padding:3px 6px;border-radius:3px}}
 .corp{{color:#9fb0c4}} .sch{{color:#6f8298;margin-left:auto;font-size:11px}}
 table{{width:100%;border-collapse:collapse}}
 td{{padding:5px 10px;border-top:1px solid #1c2735;font-size:13px;vertical-align:baseline}}
 td.nm{{font-family:"Newsreader",Georgia,serif}}
 .giv{{color:#9fb0c4;font-size:12px}}
 a{{color:#cfe0f5;text-decoration:none}} a:hover{{color:#fff;text-decoration:underline}}
 td:not(.nm){{font-family:ui-monospace,monospace;font-size:11px;color:#8ba}}
</style></head><body>
<header><h1>School-blocked person dedup — candidate review</h1>
 <div class=lede>Candidates the role+colony+year dedup missed, surfaced by shared school
   (peerage swaps, OCR, cross-edition splits). School spans generations, so each cluster is
   scored for father/son risk. <b>Nothing is merged</b> — this is for adjudication. Click a
   name to open that person's career.</div>
 {summary}</header>
<div class=filters>
 <button data-f="all" class=on>All</button>
 <button data-f="conflict">conflict</button>
 <button data-f="review">review</button>
 <button data-f="confident">confident</button>
 <button data-f="likely">likely</button>
</div>
<main id=cards>{''.join(card_html(cn, c) for cn, c in cards)}</main>
<script>
 const btns=document.querySelectorAll('.filters button'), cards=[...document.querySelectorAll('.card')];
 btns.forEach(b=>b.onclick=()=>{{btns.forEach(x=>x.classList.toggle('on',x===b));
   const f=b.dataset.f; cards.forEach(c=>c.style.display=(f==='all'||c.dataset.disp===f)?'':'none');}});
</script>
</body></html>"""
    OUT.write_text(html)
    n = len(cards)
    print(f"wrote {OUT}  ({n} clusters)")
    for cname, _ in CORPORA:
        print(f"  {cname}: " + ", ".join(f"{d}={totals.get((cname, d), 0)}"
              for d in ("conflict", "review", "confident", "likely")))


if __name__ == "__main__":
    main()
