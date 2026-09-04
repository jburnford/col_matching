#!/usr/bin/env python3
"""Generate data/services/kg_place_colony.json — the KG-derived place -> colony
resolver the services gazetteer consults for colony targets (E36 of the
2026-09-03 review: the volume colony gate missed 'G. Coast', 'S. Leone',
'Leeward Is.', Lagos->Nigeria, Quebec->Canada ... because it only knew the
gazetteer's own abbreviation table and the capital roll-up).

Two parts, both grounded in shipped data (never model memory):

  surfaces  {norm(place_raw): [colony_qid, ...]}  from BOTH corpora's
            graph_stage3/career_events.jsonl (place_raw -> colony_qid as the
            KG crosswalk + fixups resolved it). A QID is kept when it carries
            >=5% of the surface's events or >=3 events, so year-dependent
            surfaces (Lagos 1890 = Lagos Colony, 1920 = Nigeria) keep every
            period reading — the gate is an UPPER bound.
  colonies  {colony_qid: [roster targets]} = norm(KG colony label) plus the
            curated data/services/colony_qid_roster.json rows (period polity
            -> the COL roster header its officials are filed under).

Run:  python3 build_kg_place_colony.py     (re-run after any KG re-emit)
"""
import json
from collections import Counter, defaultdict
from pathlib import Path

from col_match.services import gazetteer as g

DD = Path("data/services")
EVENTS = [Path("data/kg/graph_stage3/career_events.jsonl"),
          Path("data/iol/graph_stage3/career_events.jsonl")]


def main():
    surf = defaultdict(Counter)
    labels = {}
    for f in EVENTS:
        if not f.exists():
            print(f"  (missing {f})"); continue
        for l in f.open(encoding="utf-8"):
            e = json.loads(l)
            q, pl = e.get("colony_qid"), e.get("place_raw")
            # backfilled colonies (kg_backfill_colony.py: org rollup / IOL
            # default = British Raj) say nothing about the PLACE surface
            if not q or e.get("grounded_colony_backfill"):
                continue
            labels.setdefault(q, e.get("colony_label"))
            if pl:
                surf[g.norm(pl)][q] += 1
    surfaces = {}
    for s, cnt in surf.items():
        tot = sum(cnt.values())
        keep = sorted(q for q, n in cnt.items() if n / tot >= 0.05 or n >= 3)
        if s and keep:
            surfaces[s] = keep
    curated = {k: v for k, v in json.loads((DD / "colony_qid_roster.json").read_text()).items()
               if k.startswith("Q")}
    colonies = {}
    for q, lbl in labels.items():
        t = set(curated.get(q, []))
        n = g.norm(lbl or "")
        if n:
            t.add(n)
        colonies[q] = sorted(t)
    for q, t in curated.items():          # curated rows for QIDs not (yet) in the KG
        colonies.setdefault(q, sorted(t))
    out = {"surfaces": dict(sorted(surfaces.items())), "colonies": dict(sorted(colonies.items()))}
    (DD / "kg_place_colony.json").write_text(json.dumps(out, indent=0, sort_keys=True))
    print(f"surfaces {len(surfaces):,}  colonies {len(colonies):,}  "
          f"(curated {len(curated)}) -> {DD/'kg_place_colony.json'}")


if __name__ == "__main__":
    main()
