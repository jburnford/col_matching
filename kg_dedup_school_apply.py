#!/usr/bin/env python3
"""Compose the APPROVED school-blocked merges onto the merge map.

Takes the candidate clusters from kg_dedup_school_candidates.py and folds only
the requested dispositions (default: confident,likely — the conflict/review
clusters are HELD for hand review) onto the latest full merge map, writing
dedup_stage3_merge_map.school.jsonl. Same compose contract as
kg_dedup_roleyear.py (union-find; canonical = most-attested record). Apply the
resulting map with kg_dedup_stage3_apply.py. Env COL_KG_OUT selects the corpus.

  python3 kg_dedup_school_apply.py [--accept confident,likely]
"""
import argparse, json
from collections import defaultdict
from col_match.kg.paths import KG_OUT

ap = argparse.ArgumentParser()
ap.add_argument("--accept", default="confident,likely")
args = ap.parse_args()
ACCEPT = set(args.accept.split(","))

persons = {p["person_id"]: p for p in (json.loads(l) for l in open(KG_OUT / "graph_stage3/persons.jsonl"))}
nattest = {pid: (p.get("n_attestations") or 0) for pid, p in persons.items()}

cand = [json.loads(l) for l in open(KG_OUT / "dedup_school_candidates.jsonl")]
clusters = [[m["id"] for m in c["members"]] for c in cand if c["disposition"] in ACCEPT]
held = [c for c in cand if c["disposition"] not in ACCEPT]

# compose onto the latest full map (school > roleyear > crossform > base)
for name in ("school", "roleyear", "crossform", ""):
    mapf = KG_OUT / (f"dedup_stage3_merge_map.{name}.jsonl" if name else "dedup_stage3_merge_map.jsonl")
    if mapf.exists():
        break
prior = KG_OUT / "dedup_stage3_merge_map.roleyear.jsonl"   # never compose onto our own output
base = prior if prior.exists() else mapf

uf = {}
def f2(x):
    uf.setdefault(x, x)
    while uf[x] != x: uf[x] = uf[uf[x]]; x = uf[x]
    return x
def union(a, b):
    ra, rb = f2(a), f2(b)
    if ra != rb: uf[ra] = rb

existing = [json.loads(l) for l in open(base)]
for r in existing:
    union(r["person_id"], r["canonical_person_id"])

merged_records = 0
for m in clusters:
    canon = max(m, key=lambda p: nattest.get(p, 0))   # most-attested = canonical
    for p in m:
        if p != canon:
            union(p, canon); merged_records += 1

allpids = set()
for r in existing:
    allpids.add(r["person_id"]); allpids.add(r["canonical_person_id"])
for m in clusters:
    allpids.update(m)
rows = [{"person_id": p, "canonical_person_id": f2(p)} for p in sorted(allpids) if f2(p) != p]

out = KG_OUT / "dedup_stage3_merge_map.school.jsonl"
with open(out, "w") as fh:
    for r in rows:
        fh.write(json.dumps(r) + "\n")
print(f"{KG_OUT}: accepted dispositions {sorted(ACCEPT)} -> {len(clusters)} clusters, "
      f"{merged_records} records folded; HELD {len(held)} clusters")
print(f"  composed onto {base.name}; map rows {len(existing)} -> {len(rows)}  ->  {out.name}")