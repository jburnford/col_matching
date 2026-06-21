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

from col_match.kg.resolve_context import is_ambiguous

OUT = Path("data/kg")
FLAT = OUT / "places_worklist.jsonl"
CONTEXT = OUT / "places_worklist.context.jsonl"
GROUNDING = OUT / "places_worklist.grounding.jsonl"
FLAGGED = OUT / "places_worklist.flagged.jsonl"


def main() -> None:
    rows = [json.loads(l) for l in FLAT.open(encoding="utf-8")
            if not l.startswith("#")]
    # context-resolved queries (directional provinces, S.A./W.A.) grounded via
    # per-person career context — see kg_resolve_context_places.py.
    context = []
    if CONTEXT.exists():
        context = [json.loads(l) for l in CONTEXT.open(encoding="utf-8")
                   if not l.startswith("#")]

    groups: dict[str, dict] = defaultdict(lambda: {"count": 0, "variants": []})
    flagged = []
    n_ambiguous = 0
    for r in rows:
        if r.get("suspected_noise"):
            flagged.append(r)
            continue
        if is_ambiguous(r["place"]):
            # handled per-person by the context resolver; never ground the
            # surface form (it means different places for different people).
            n_ambiguous += 1
            continue
        g = groups[r["query"]]
        g["count"] += r["count"]
        g["variants"].append([r["place"], r["count"]])

    out = []
    for q, g in sorted(groups.items(), key=lambda x: -x[1]["count"]):
        g["variants"].sort(key=lambda x: -x[1])
        out.append({"query": q, "count": g["count"],
                    "n_variants": len(g["variants"]), "variants": g["variants"]})
    # append context-resolved queries (already deduped + per-person provenance)
    for c in sorted(context, key=lambda x: -x.get("count", 0)):
        out.append({"query": c["query"], "count": c["count"],
                    "context_resolved": True,
                    "sample_evidence": c.get("sample_evidence", [])})

    with GROUNDING.open("w", encoding="utf-8") as fh:
        fh.write(f"# {len(out)} place queries for MCP grounding "
                 f"({len(groups)} canonical surface forms + {len(context)} "
                 f"context-resolved; {n_ambiguous} ambiguous surface forms "
                 f"replaced by context; {len(flagged)} noise/institution -> .flagged)\n")
        for r in out:
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")

    with FLAGGED.open("w", encoding="utf-8") as fh:
        fh.write(f"# {len(flagged)} non-geographic values FLAGGED out of grounding "
                 f"(institutions/offices/war terms) — kept for review, never grounded\n")
        for r in sorted(flagged, key=lambda x: -x["count"]):
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")

    total = sum(r["count"] for r in out)
    multi = sum(1 for r in out if r.get("n_variants", 0) > 1)
    print(f"grounding queries:   {len(out)}  ({len(groups)} surface + {len(context)} context-resolved)")
    print(f"  surface collapse >1 variant: {multi}")
    print(f"  ambiguous forms -> context:  {n_ambiguous}")
    print(f"groundable mentions: {total}")
    print(f"flagged (skipped):   {len(flagged)}")
    print(f"wrote {GROUNDING}")
    print(f"wrote {FLAGGED}")


if __name__ == "__main__":
    main()
