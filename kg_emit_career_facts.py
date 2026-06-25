#!/usr/bin/env python3
"""Fuse the grounding overlays onto the career-event spine.

The KG stores a career fact across three files that all join on (person_id, seq):
  career_events.jsonl   spine: place_qid / colony_qid / year_start..end / is_acting / position
  role_edges.jsonl      the grounded ROLE (role_id QID or colkg:) for that same event
  employment_edges.jsonl the grounded EMPLOYER org (org_id) for that same event

This emits one DENORMALISED statement per spine event so each career fact is
self-contained: person --[held ROLE]--> at [ORG] in [PLACE/COLONY] during [years].

  data/kg/graph_stage3/career_facts.jsonl

Honours / qualifications / education stay person-level (keyed by person_id only,
no seq) -- they are attributes of the person, not of a single career event, so
they are NOT fused here.  Read-only: regenerate any time after the layer emits.
"""
from __future__ import annotations
import json
from pathlib import Path
from collections import Counter

GD = Path("data/kg/graph_stage3")

def load(p):
    return [json.loads(l) for l in (GD / p).open()]

def index(rows):
    d = {}
    for r in rows:
        d[(r["person_id"], r["seq"])] = r   # emit produces one row per (person, seq)
    return d

def main():
    spine = load("career_events.jsonl")
    roles = index(load("role_edges.jsonl"))
    orgs = index(load("employment_edges.jsonl"))

    out, stat = [], Counter()
    for e in spine:
        k = (e["person_id"], e["seq"])
        r = roles.get(k) or {}
        o = orgs.get(k) or {}
        fact = {
            "person_id": e["person_id"],
            "seq": e["seq"],
            # role (grounded occupation/position)
            "role_id": r.get("role_id"),
            "role_label": r.get("role_label"),
            "role_modifiers": r.get("modifiers", []),
            "is_acting": e.get("is_acting", False),
            # employer organisation (grounded where the bio named one)
            "org_id": o.get("org_id"),
            "org_label": o.get("org_label"),
            "org_type": e.get("org_type"),
            # place / colony
            "place_qid": e.get("place_qid"),
            "place_label": e.get("place_label"),
            "colony_qid": e.get("colony_qid"),
            "colony_label": e.get("colony_label"),
            # time span
            "year_start": e.get("year_start"),
            "year_end": e.get("year_end"),
            # provenance / raw
            "position_raw": e.get("position"),
            "role_source": r.get("source"),
            "org_source": o.get("source"),
        }
        out.append(fact)
        if str(fact["role_id"] or "").startswith("Q"): stat["role_qid"] += 1
        elif fact["role_id"]: stat["role_internal"] += 1
        if fact["org_id"]: stat["org"] += 1
        if fact["place_qid"]: stat["place"] += 1
        if fact["colony_qid"]: stat["colony"] += 1
        if fact["year_start"]: stat["dated"] += 1
        if fact["role_id"] and fact["place_qid"] and fact["year_start"]:
            stat["role+place+time"] += 1

    with (GD / "career_facts.jsonl").open("w") as fh:
        for f in out:
            fh.write(json.dumps(f, ensure_ascii=False) + "\n")

    n = len(out)
    print(f"career_facts: {n:,}")
    for k in ["role_qid", "role_internal", "org", "place", "colony", "dated", "role+place+time"]:
        print(f"  {k:16} {stat[k]:>7} ({100*stat[k]/n:.0f}%)")

if __name__ == "__main__":
    main()
