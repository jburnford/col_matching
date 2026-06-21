#!/usr/bin/env python3
"""Emit the MCP-ready, canonicalised place-grounding worklist.

Takes the flat per-surface-form worklist produced by ``kg_build.py ground``
(which already carries a canonical ``query`` and a ``suspected_noise`` flag via
col_match/kg/place_canon) and:

  1. routes non-geographic values (institutions/offices/war terms) to
     ``places_worklist.flagged.jsonl`` — kept for review, never grounded;
  2. groups the rest by canonical ``query`` so each territory is grounded ONCE
     and every printed variant inherits the same QID -> ``places_worklist.grounding.jsonl``.

Usage:
    python3 kg_build.py ground --struct data/kg/llm_struct_corpus.reviewed.jsonl \
        > data/kg/places_worklist.jsonl
    python3 kg_emit_grounding_worklist.py
"""
from __future__ import annotations

import json
from collections import defaultdict
from pathlib import Path

OUT = Path("data/kg")
FLAT = OUT / "places_worklist.jsonl"
GROUNDING = OUT / "places_worklist.grounding.jsonl"
FLAGGED = OUT / "places_worklist.flagged.jsonl"


def main() -> None:
    rows = [json.loads(l) for l in FLAT.open(encoding="utf-8")
            if not l.startswith("#")]
    groups: dict[str, dict] = defaultdict(lambda: {"count": 0, "variants": []})
    flagged = []
    for r in rows:
        if r.get("suspected_noise"):
            flagged.append(r)
            continue
        g = groups[r["query"]]
        g["count"] += r["count"]
        g["variants"].append([r["place"], r["count"]])

    out = []
    for q, g in sorted(groups.items(), key=lambda x: -x[1]["count"]):
        g["variants"].sort(key=lambda x: -x[1])
        out.append({"query": q, "count": g["count"],
                    "n_variants": len(g["variants"]), "variants": g["variants"]})

    with GROUNDING.open("w", encoding="utf-8") as fh:
        fh.write(f"# {len(out)} canonical place queries for MCP grounding "
                 f"(deduped from {len(rows) - len(flagged)} surface forms; "
                 f"{len(flagged)} noise/institution rows routed to .flagged)\n")
        for r in out:
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")

    with FLAGGED.open("w", encoding="utf-8") as fh:
        fh.write(f"# {len(flagged)} non-geographic values FLAGGED out of grounding "
                 f"(institutions/offices/war terms) — kept for review, never grounded\n")
        for r in sorted(flagged, key=lambda x: -x["count"]):
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")

    total = sum(r["count"] for r in out)
    multi = sum(1 for r in out if r["n_variants"] > 1)
    print(f"canonical queries:   {len(out)}  ({multi} collapse >1 variant)")
    print(f"groundable mentions: {total}")
    print(f"flagged (skipped):   {len(flagged)}")
    print(f"wrote {GROUNDING}")
    print(f"wrote {FLAGGED}")


if __name__ == "__main__":
    main()
