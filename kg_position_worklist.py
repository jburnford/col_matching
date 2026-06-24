#!/usr/bin/env python3
"""Build the ROLE / occupation worklist from career-event positions.

Parses every event's position_norm into a base ROLE (via kg_role_norm) and groups
to distinct roles for Wikidata-occupation grounding. Modifiers (acting/assistant/
grade) are dropped here -- they are emitted as edge attributes by kg_emit_roles.py.

Output: data/kg/position_worklist.jsonl
  {institution: <base_role>, type: <category>, count, person_ids, examples}
(the `institution` key lets the env-overridable kg_ground_institutions.py harness
serve this worklist unchanged: COL_WORK=position_worklist.jsonl)

Roles '_unknown' / '_military_service' / '_honour' are control buckets, written
with those ids so emit can treat them specially (not grounded).
"""
from __future__ import annotations
import json
from pathlib import Path
from collections import defaultdict, Counter
from kg_role_norm import parse_position

EVENTS = Path("data/kg/graph_stage3/career_events.jsonl")
OUT = Path("data/kg/position_worklist.jsonl")

def main():
    groups = defaultdict(lambda: {"count": 0, "person_ids": set(),
                                  "examples": Counter(), "cat": Counter()})
    for line in EVENTS.open():
        e = json.loads(line)
        raw = e.get("position_norm") or e.get("position")
        if not raw:
            continue
        base, mods, cat = parse_position(raw)
        g = groups[base]
        g["count"] += 1
        g["person_ids"].add(e["person_id"])
        g["examples"][raw.strip()] += 1
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
    print(f"{len(rows):,} distinct base-roles | {tot:,} positioned events -> {OUT}")
    print(f"control buckets: " + ", ".join(f"{k}={v}" for k, v in ctrl.items()))
    for k in (50, 200, 500, 1000):
        cov = sum(r["count"] for r in rows[:k])
        print(f"  top {k:>4} roles cover {100*cov/tot:.0f}% of mentions")

if __name__ == "__main__":
    main()
