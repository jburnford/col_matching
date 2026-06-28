#!/usr/bin/env python3
"""Remap person_id -> canonical in the MCP-grounded layers a spine re-emit does
NOT regenerate, after a merge-map change.

Most graph layers (persons, career_events, role/employment/honour/qualification
edges, career_facts) are re-emitted from the deduped spine and so already carry
canonical person_ids. But education_edges (institution grounding) and
person_grounding.final are keyed by the ORIGINAL person_id and must be chased to
canonical, or they orphan (the staleness the roleyear round left behind). This
step closes that gap. Also flags grounding QID conflicts (two members of one
merged cluster grounded to DIFFERENT QIDs = a likely over-merge). Env COL_KG_OUT.
"""
import json
from collections import defaultdict
from col_match.kg.paths import KG_OUT

GD = KG_OUT / "graph_stage3"
TIER = {"A": 0, "B": 1, "C": 2, "L2": 3}


def resolver():
    m = {}
    for f in KG_OUT.glob("dedup_stage3_merge_map*.jsonl"):
        if "bak" in f.name or "_v2" in f.name:
            continue
        for l in f.open():
            d = json.loads(l)
            if d["person_id"] != d["canonical_person_id"]:
                m[d["person_id"]] = d["canonical_person_id"]
    def res(pid):
        seen = set()
        while pid in m and pid not in seen:
            seen.add(pid); pid = m[pid]
        return pid
    return res


def remap_education(res, persons):
    p = GD / "education_edges.jsonl"
    rows = [json.loads(l) for l in p.open()]
    seen, out, dropped = set(), [], 0
    for d in rows:
        c = res(d["person_id"])
        if c not in persons:
            dropped += 1; continue          # person genuinely gone (shouldn't happen)
        d["person_id"] = c
        key = (c, d.get("institution_id"))
        if key in seen:                      # two members merged -> same school edge
            continue
        seen.add(key); out.append(d)
    with p.open("w") as fh:
        for d in out:
            fh.write(json.dumps(d) + "\n")
    print(f"  education_edges: {len(rows)} -> {len(out)} (deduped {len(rows)-len(out)-dropped}, dropped {dropped})")


def remap_grounding(res, persons):
    p = GD / "person_grounding.final.jsonl"
    if not p.exists():
        print("  person_grounding.final: (none)"); return
    rows = [json.loads(l) for l in p.open()]
    by = defaultdict(list)
    for d in rows:
        c = res(d["person_id"])
        if c in persons:
            d["person_id"] = c; by[c].append(d)
    conflicts, out = 0, []
    for c, ds in by.items():
        qids = {d.get("qid") for d in ds if d.get("qid")}
        if len(qids) > 1:
            conflicts += 1
            print(f"  ⚠ QID CONFLICT {c}: {qids} — keeping highest tier (review merge!)")
        out.append(min(ds, key=lambda d: TIER.get(d.get("tier"), 9)))
    with p.open("w") as fh:
        for d in out:
            fh.write(json.dumps(d) + "\n")
    print(f"  person_grounding.final: {len(rows)} -> {len(out)} rows, {conflicts} QID conflicts")


def main():
    res = resolver()
    persons = {json.loads(l)["person_id"] for l in (GD / "persons.jsonl").open()}
    print(f"{KG_OUT}: remapping MCP-grounded layers to canonical")
    remap_education(res, persons)
    remap_grounding(res, persons)


if __name__ == "__main__":
    main()
