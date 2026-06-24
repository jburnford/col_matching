#!/usr/bin/env python3
"""Build the HONOUR / award worklist from the honours layer.

Parses every honour edge's award string into a base HONOUR (via kg_honour_norm)
and groups to distinct honours for Wikidata grounding. Branch qualifiers
(military/civil) are dropped here -- emitted as edge attributes by
kg_emit_honours.py.

Output: data/kg/honour_worklist.jsonl
  {institution: <base_honour>, type: <category>, count, person_ids, examples}
(the `institution` key lets the env-overridable kg_ground_institutions.py harness
serve this worklist unchanged: COL_WORK=data/kg/honour_worklist.jsonl)

'_unknown' is a control bucket (noise extractions), written with that id so emit
can skip it.
"""
from __future__ import annotations
import json
from pathlib import Path
from collections import defaultdict, Counter
from kg_honour_norm import parse_honour

HON = Path("data/kg/graph_stage3/honours.jsonl")
OUT = Path("data/kg/honour_worklist.jsonl")

def main():
    groups = defaultdict(lambda: {"count": 0, "person_ids": set(),
                                  "examples": Counter(), "cat": Counter()})
    for line in HON.open():
        e = json.loads(line)
        base, mods, cat = parse_honour(e.get("award"))
        g = groups[base]
        g["count"] += 1
        g["person_ids"].add(e["person_id"])
        g["examples"][(e.get("award") or "").strip()] += 1
        g["cat"][cat] += 1

    rows = []
    for base, g in groups.items():
        rows.append({
            "institution": base,
            "type": g["cat"].most_common(1)[0][0],
            "count": g["count"],
            "person_ids": sorted(g["person_ids"]),
            "examples": [s for s, _ in g["examples"].most_common(3)],
        })
    rows.sort(key=lambda r: -r["count"])
    with OUT.open("w") as fh:
        for r in rows:
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")

    tot = sum(r["count"] for r in rows)
    ctrl = {r["institution"]: r["count"] for r in rows if r["institution"].startswith("_")}
    print(f"{len(rows):,} distinct honours | {tot:,} award mentions -> {OUT}")
    print("control buckets: " + ", ".join(f"{k}={v}" for k, v in ctrl.items()))
    for k in (20, 50, 100, 200):
        cov = sum(r["count"] for r in rows[:k])
        print(f"  top {k:>4} honours cover {100*cov/tot:.0f}% of mentions")

if __name__ == "__main__":
    main()
