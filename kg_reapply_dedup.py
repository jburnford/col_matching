#!/usr/bin/env python3
"""Port the 917-decision LLM dedup ledger (old OCR) onto the new KG persons.

Each fingerprinted merge group (data/services/dedup/llm_merges_fingerprinted.jsonl)
is matched, member by member, to a new-KG bio (data/kg/bios) within the same
edition, scored by surname+given+birth fuzzy + shared career YEARS (extracted
from raw_text — the new bios aren't structured yet, but year-overlap is the
OCR-robust signal `reapply_dedup_fingerprints.py` already relies on). Each matched
bio maps to a person_id in persons.jsonl. A group whose members land on >1
distinct person_id is a duplicate the new clustering MISSED that the LLM ledger
already resolved.

  python3 kg_reapply_dedup.py [--min-score 70]
"""
from __future__ import annotations
import argparse, json, re, glob
from collections import defaultdict
from rapidfuzz import fuzz

YEAR = re.compile(r"\b1[789]\d\d\b")
ap = argparse.ArgumentParser()
ap.add_argument("--min-score", type=float, default=70.0)
ap.add_argument("--examples", type=int, default=12)
args = ap.parse_args()

def edition(s):
    m = re.match(r"([a-z]+\d{4})", s); return m.group(1) if m else s.split("-")[0]

# new-KG bios indexed by edition
by_ed = defaultdict(list)
bio2pid = {}
for f in glob.glob("data/kg/bios/*.jsonl"):
    for l in open(f):
        b = json.loads(l)
        b["_years"] = set(int(y) for y in YEAR.findall(b["raw_text"]))
        by_ed[edition(b["bio_id"])].append(b)
# bio_id -> person_id
P = [json.loads(l) for l in open("data/kg/persons.jsonl")]
for p in P:
    for bid in p.get("attestation_bio_ids", []):
        bio2pid[bid] = p["person_id"]

def score(fpr, b):
    s = fuzz.token_set_ratio(fpr.get("surname") or "", b.get("surname") or "") * 0.35
    s += fuzz.token_set_ratio(fpr.get("given") or "", b.get("given_names") or "") * 0.25
    if fpr.get("birth") and b.get("birth_year"):
        s += 15 if abs(fpr["birth"] - b["birth_year"]) <= 1 else 0
    elif not fpr.get("birth") and not b.get("birth_year"):
        s += 5
    fy = {y for (y, *_), in [((e[0],),) for e in fpr.get("events", []) if e and e[0]]}
    if fy:
        s += 25 * (len(fy & b["_years"]) / len(fy))
    return s

def remap(fpr):
    ed = fpr.get("edition") or edition(fpr.get("version_id", ""))
    best, bs = None, -1.0
    for b in by_ed.get(ed, []):
        sc = score(fpr, b)
        if sc > bs:
            best, bs = b, sc
    return (best, bs) if best else (None, 0.0)

groups = [json.loads(l) for l in open("data/services/dedup/llm_merges_fingerprinted.jsonl")]
already = need = unmappable = 0
members_mapped = members_total = 0
new_merges = []
for g in groups:
    pids, low = set(), 0
    for fpr in g["fingerprints"]:
        members_total += 1
        b, sc = remap(fpr)
        if b and sc >= args.min_score:
            members_mapped += 1
            pids.add(bio2pid.get(b["bio_id"]))
        else:
            low += 1
    pids.discard(None)
    if len(pids) >= 2:
        need += 1
        new_merges.append((g, pids))
    elif len(pids) == 1 and low == 0:
        already += 1
    else:
        unmappable += 1

print(f"ledger groups: {len(groups)} | fingerprint members: {members_total} "
      f"(mapped>={args.min_score}: {members_mapped}, {100*members_mapped/members_total:.0f}%)")
print(f"  already 1 person in new KG (merge holds)     : {already}")
print(f"  NEW merge needed (>1 person_id, KG split it) : {need}")
print(f"  unmappable (members not found in new OCR)     : {unmappable}")
distinct_excess = sum(len(p) - 1 for _, p in new_merges)
print(f"  -> {distinct_excess} excess person records the ledger would collapse")
print(f"\nsample NEW merges the new clustering missed (ledger already decided these):")
for g, pids in new_merges[: args.examples]:
    print(f"  {sorted(pids)}  src={g.get('source')}  reason={(g.get('reason') or '')[:90]}")
