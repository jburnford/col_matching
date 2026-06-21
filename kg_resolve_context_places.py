#!/usr/bin/env python3
"""Resolve ambiguous place abbreviations per person from career context.

Reads the reviewed structured corpus, and for every event whose place is an
ambiguous form (directional province/region, or S.A./W.A.) uses the person's
OTHER postings to resolve it to a precise query (``Western Province, Ceylon``,
``South Africa``…). Gated: unresolvable occurrences stay flagged.

Outputs:
  data/kg/places_resolution_map.jsonl  — one row per resolved occurrence
      {person_id, place, resolved_query, evidence}
  data/kg/places_worklist.context.jsonl — resolved queries aggregated for MCP
      grounding {query, count, n_occurrences, sample_evidence}

Usage:  python3 kg_resolve_context_places.py
"""
from __future__ import annotations

import json
from collections import Counter, defaultdict
from pathlib import Path

from col_match.kg.resolve_context import is_ambiguous, resolve

OUT = Path("data/kg")
CORPUS = OUT / "llm_struct_corpus.reviewed.jsonl"
MAP = OUT / "places_resolution_map.jsonl"
CONTEXT = OUT / "places_worklist.context.jsonl"


def main() -> None:
    resolved_rows = []
    agg: dict[str, dict] = defaultdict(lambda: {"count": 0, "evidence": []})
    n_amb_occ = n_resolved = n_flagged = 0

    for line in CORPUS.open(encoding="utf-8"):
        r = json.loads(line)
        pid = r.get("person_id")
        events = r.get("events") or []
        places = [(ev.get("place") or "").strip() for ev in events]
        for place in places:
            if not place or not is_ambiguous(place):
                continue
            n_amb_occ += 1
            siblings = [p for p in places if p and p != place]
            query, evidence = resolve(place, siblings)
            if query is None:
                n_flagged += 1
                continue
            n_resolved += 1
            resolved_rows.append({"person_id": pid, "place": place,
                                  "resolved_query": query, "evidence": evidence})
            g = agg[query]
            g["count"] += 1
            if len(g["evidence"]) < 3:
                g["evidence"].append({"place": place, "evidence": evidence})

    with MAP.open("w", encoding="utf-8") as fh:
        for row in resolved_rows:
            fh.write(json.dumps(row, ensure_ascii=False) + "\n")

    ctx = sorted(agg.items(), key=lambda x: -x[1]["count"])
    with CONTEXT.open("w", encoding="utf-8") as fh:
        fh.write(f"# {len(ctx)} context-resolved place queries for MCP grounding "
                 f"({n_resolved} occurrences resolved from career context; "
                 f"{n_flagged} ambiguous occurrences left flagged)\n")
        for q, g in ctx:
            fh.write(json.dumps({"query": q, "count": g["count"],
                                 "context_resolved": True,
                                 "sample_evidence": g["evidence"]},
                                ensure_ascii=False) + "\n")

    print(f"ambiguous occurrences:  {n_amb_occ}")
    print(f"  resolved from context: {n_resolved} ({100*n_resolved/max(1,n_amb_occ):.0f}%)")
    print(f"  left flagged:          {n_flagged}")
    print(f"distinct resolved queries: {len(ctx)}")
    print("top resolved queries:")
    for q, g in ctx[:12]:
        print(f"   {g['count']:>4}  {q}")
    print(f"wrote {MAP}\nwrote {CONTEXT}")


if __name__ == "__main__":
    main()
