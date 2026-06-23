#!/usr/bin/env python3
"""Stage-3 dedup: hand-adjudication of the 149 held UNCERTAIN groups + assembly
of the full Stage-3 merge map.

Hand verdicts below were authored by reading the full evidence of every held
group (positions, education, year trajectories) in /tmp/uncertain_dump.txt.
Decision principle (validated against all 149):
  MERGE   if members share a specific office (position+colony) in overlapping
          years -- even when birth-year or education differ (those OCR-vary; a
          shared specific posting identifies the person).
  SPLIT   if careers are in different colonies/fields with different schools and
          no shared posting (genuine namesakes).
  PARTIAL multi-record groups where only a subset is the same person.

Combined with the auto-rule buckets (A_birth, B_place non-thin, MERGE_RULE)
into a single union-find merge map over structured person_ids.

  python3 kg_dedup_stage3_adjudicate.py [--write-map data/kg/dedup_stage3_merge_map.jsonl]
"""
from __future__ import annotations
import argparse, json
from collections import defaultdict
from col_match.services.compile import _names_compatible

ap = argparse.ArgumentParser()
ap.add_argument("--cands", default="data/kg/dedup_stage3_candidates.jsonl")
ap.add_argument("--queue", default="data/kg/dedup_stage3_review_queue.jsonl")
ap.add_argument("--corpus", default="data/kg/llm_struct_corpus.reviewed.jsonl")
ap.add_argument("--adj-out", default="data/kg/dedup_stage3_adjudication.jsonl")
ap.add_argument("--write-map", default="")
args = ap.parse_args()

# ---- HAND VERDICTS on the 149 UNCERTAIN held groups, keyed by (surname,given) ----
# CONFLICT genuine namesakes -> keep all members separate
SPLIT = {
    ("anderson", "ga"), ("brown", "ronaldernest"), ("robertson", "william"),
    ("ross", "jm"), ("smith", "rw"), ("williams", "dj"), ("cole", "rv"),
    ("malherbe", "davidgabriel"), ("jones", "t"), ("stubbs", "gc"),
    ("faulkner", "de"),
}
# PARTIAL: only the listed sub-clusters are the same person (match by bio_id
# substring of person_id); members not listed stay singletons.
PARTIAL = {
    ("spence", "jb"): [["col1896-p650b12", "col1898-p540b5"]],
    ("morgappah", "nicholaswilfred"): [["col1925-p946b15", "col1932-p999b9"]],
    ("anderson", "john"): [["col1880-p344b10", "col1917-p691b13"]],
    ("anderson", "williamjohn"): [
        ["col1877-p348b10", "col1880-p344b14", "col1897-p455b21", "col1905-p605b13"],
        ["col1940-p867b12", "col1949-p414b19"],
    ],
}
# everything else in the held UNCERTAIN set -> MERGE all members

held = [json.loads(l) for l in open(args.queue)]
held_keys = {(c["surname_key"], c["given_key"]) for c in held}

def verdict_for(c):
    k = (c["surname_key"], c["given_key"])
    if k in SPLIT: return "SPLIT", "hand: namesakes (different colony/field + schools)"
    if k in PARTIAL: return "PARTIAL", "hand: subset same-person"
    if c.get("_verdict") in ("MERGE_RULE",): return "MERGE", "auto: " + c.get("_reason", "")
    if c.get("_verdict") in ("SPLIT_RULE",): return "SPLIT", "auto: " + c.get("_reason", "")
    return "MERGE", "hand: shared specific posting across editions"

# recompute _verdict for held via the review classifier is already stored? queue
# rows came from review harness WITHOUT _verdict; recompute the auto buckets here
# is unnecessary -- queue rows are exactly the held set. We classify by hand maps
# + (anything not hand-listed) MERGE. But MERGE_RULE/SPLIT_RULE autos are NOT in
# the UNCERTAIN dump; they were decided in the review harness. We re-derive them
# from the candidates file's tier + our knowledge: held rows here are the FULL
# 300 (incl auto MERGE_RULE/SPLIT_RULE). Tag each.
from itertools import combinations
import re
rec_by = {json.loads(l)["person_id"]: json.loads(l) for l in open(args.corpus)}
def edu_tok(s): return set(t for t in re.findall(r"[a-z]{4,}", (s or "").lower())
                           if t not in {"college","university","school","educated","grammar"})
def jac(a,b): return len(a&b)/len(a|b) if a and b else 0.0
def posn(p): return re.sub(r"[^a-z ]","",(p or "").lower()).strip()
def appt(r): return {(posn(e.get("position")), e.get("year_start"))
                     for e in (r.get("events") or []) if e.get("position") and e.get("year_start")}
def autobucket(c):
    members=c["members"]; recs=[rec_by[m["person_id"]] for m in members]
    keys=[appt(r) for r in recs]
    inter=set.intersection(*keys) if keys else set()
    subset=any(i!=j and keys[i] and len(keys[i])>=2 and keys[i]<=keys[j]
               for i in range(len(keys)) for j in range(len(keys)))
    strong=len(inter)>=2 or subset
    edus=[edu_tok(r.get("education")) for r in recs]
    best_edu=max((jac(a,b) for a,b in combinations(edus,2)), default=0.0)
    nq=len(c["shared_qids_any"]); bd=(max(c["births"])-min(c["births"])) if len(c["births"])>=2 else 0
    if c["tier"]=="CONFLICT":
        if strong: return "MERGE_RULE"
        if bd<=1 and (nq>=2 or best_edu>=0.5): return "MERGE_RULE"
        if bd>=3 and best_edu<0.2 and len(inter)==0: return "SPLIT_RULE"
        return "UNCERTAIN"
    else:
        if strong: return "MERGE_RULE"
        if len(inter)>=1 and best_edu>=0.3: return "MERGE_RULE"
        if best_edu>=0.5: return "MERGE_RULE"
        return "UNCERTAIN"

for c in held:
    c["_verdict"] = autobucket(c)

# ---- write adjudication ledger ----
adj = []
for c in held:
    v, reason = verdict_for(c)
    adj.append({"surname_key": c["surname_key"], "given_key": c["given_key"],
                "tier": c["tier"], "n_members": c["n_members"],
                "verdict": v, "reason": reason,
                "members": [m["person_id"] for m in c["members"]],
                "partial_clusters": None})
    if v == "PARTIAL":
        adj[-1]["partial_clusters"] = PARTIAL[(c["surname_key"], c["given_key"])]
with open(args.adj_out, "w") as fh:
    for a in adj: fh.write(json.dumps(a, ensure_ascii=False) + "\n")

# ---- assemble FULL stage-3 union-find over ALL person_ids ----
cands = [json.loads(l) for l in open(args.cands)]
all_pids = list(rec_by.keys())
idx = {p: i for i, p in enumerate(all_pids)}
parent = list(range(len(all_pids)))
def find(x):
    while parent[x] != x: parent[x] = parent[parent[x]]; x = parent[x]
    return x
def union(a, b):
    ra, rb = find(idx[a]), find(idx[b])
    if ra != rb: parent[ra] = rb

def union_all(pids):
    for i in range(1, len(pids)): union(pids[0], pids[i])

def _edition(pid):
    m = re.search(r"(col|dol)(\d{4})", pid); return int(m.group(2)) if m else 0

# bio-level edition span per structured record (from the Stage-2 cluster); a
# record's true coverage is its whole attestation run, NOT just its canonical bio.
_PROV_EDS = {}
for _l in open("data/kg/persons.deduped2.jsonl"):
    _d = json.loads(_l); _e = _d.get("editions") or []
    if _e: _PROV_EDS[_d["person_id"]] = (min(_e), max(_e))
def _interval(pid):
    lo_hi = _PROV_EDS.get(pid)
    if lo_hi: return lo_hi
    e = _edition(pid); return (e, e)

def union_temporal(pids, gap=20, maxspan=50):
    """Union pids only within temporally-coherent bands, comparing each record's
    full bio-edition INTERVAL (Stage-2 attestation span), not its single canonical
    edition. One person appears in a contiguous run of editions; recursively split
    a group where the gap BETWEEN consecutive intervals exceeds `gap`, or the merged
    span would exceed `maxspan`. (Cameron's 1896-1912 + 1913-1940 intervals abut ->
    merge; a 1867 + 1963 pairing, or 1883-1915 + 1940, is >1 namesake -> split.)"""
    items = sorted(((_interval(p), p) for p in pids), key=lambda x: x[0])
    def split(group):
        if len(group) <= 1: return [group]
        spanlo = group[0][0][0]
        best = None  # (between-interval gap, index)
        for i in range(len(group) - 1):
            g = group[i + 1][0][0] - group[i][0][1]   # next.lo - cur.hi
            if best is None or g > best[0]: best = (g, i)
        spanhi = max(iv[1] for iv, _ in group)
        if best[0] <= gap and spanhi - spanlo <= maxspan: return [group]
        return split(group[:best[1] + 1]) + split(group[best[1] + 1:])
    n = 0
    for band in split(items):
        bp = [p for _, p in band]
        if len(bp) >= 2: union_all(bp)
        if bp: n += 1
    return n

merged_groups = 0
# 1) auto-accept tiers not in held: A_birth + B_place non-thin
held_set = {(c["surname_key"], c["given_key"]) for c in held}
for c in cands:
    k = (c["surname_key"], c["given_key"])
    if k in held_set: continue
    if c["tier"] == "A_birth" or c["tier"] == "B_place":
        merged_groups += union_temporal([m["person_id"] for m in c["members"]])
# 2) held groups per adjudication
adj_by = {(a["surname_key"], a["given_key"]): a for a in adj}
for c in held:
    a = adj_by[(c["surname_key"], c["given_key"])]
    pids = [m["person_id"] for m in c["members"]]
    if a["verdict"] == "MERGE":
        merged_groups += union_temporal(pids)
    elif a["verdict"] == "PARTIAL":
        for cluster in a["partial_clusters"]:
            sel = [p for p in pids if any(sub in p for sub in cluster)]
            if len(sel) >= 2: merged_groups += union_temporal(sel)
    # SPLIT -> no union

# --- title/peerage-reformatting merges (cross given-name-form; hand-adjudicated
# from career evidence). A person ennobled mid-career gets re-headed under their
# title ("LUGARD, BARON..."), which the (surname,given) blocking never groups. ---
TITLE_MERGE = {("BRASSEY", 1836), ("BUXTON", 1853), ("FORREST", 1847),
               ("GRENFELL", 1841), ("LUGARD", 1858), ("METHUEN", 1845),
               ("TWINING", 1899)}
TITLE_PARTIAL = {("HARCOURT", 1863): "ALGERNON"}   # merge all EXCEPT given starting thus
byk = defaultdict(list)
for p, r in rec_by.items():
    if r.get("birth_year"): byk[((r.get("surname") or "").upper(), r["birth_year"])].append(p)
title_merges = 0
for key in TITLE_MERGE:
    pids = byk.get(key, [])
    if len(pids) >= 2: title_merges += union_temporal(pids)
for key, skip in TITLE_PARTIAL.items():
    pids = [p for p in byk.get(key, [])
            if not (rec_by[p].get("given_names") or "").upper().startswith(skip)]
    if len(pids) >= 2: title_merges += union_temporal(pids)
merged_groups += title_merges

# build canonical map (canonical = lexicographically smallest person_id in group)
groups = defaultdict(list)
for p in all_pids: groups[find(idx[p])].append(p)
mmap = {}
folded = 0
for g in groups.values():
    if len(g) > 1:
        canon = sorted(g)[0]
        for p in g: mmap[p] = canon
        folded += len(g) - 1

from collections import Counter
vc = Counter(a["verdict"] for a in adj)
print(f"hand+auto adjudication of {len(held)} held groups: {dict(vc)}")
print(f"  (SPLIT={vc.get('SPLIT',0)}, MERGE={vc.get('MERGE',0)}, PARTIAL={vc.get('PARTIAL',0)})")
print(f"wrote ledger -> {args.adj_out}")
print()
print(f"FULL stage-3 merge: {len(all_pids):,} structured records")
print(f"  merge groups applied: {merged_groups:,}")
print(f"  records folded into a canonical: {folded:,}")
print(f"  -> distinct persons after stage-3: {len(all_pids) - folded:,}")

if args.write_map:
    with open(args.write_map, "w") as fh:
        for p, c in sorted(mmap.items()):
            fh.write(json.dumps({"person_id": p, "canonical_person_id": c}) + "\n")
    print(f"wrote merge map -> {args.write_map} ({len(mmap):,} non-canonical members)")
