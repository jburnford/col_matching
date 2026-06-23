#!/usr/bin/env python3
"""Stage-3 dedup REVIEW harness for the held pockets (thin B_place + CONFLICT).

Renders FULL evidence per group (positions, full education, qid labels, year
trajectories) and applies refined 0-FP rules. Clear-cut groups are decided by
rule; the residual UNCERTAIN groups are dumped for hand-adjudication.

  python3 kg_dedup_stage3_review.py            # summary + write review queue
  python3 kg_dedup_stage3_review.py --show UNCERTAIN   # dump full evidence
  python3 kg_dedup_stage3_review.py --show MERGE_RULE
  python3 kg_dedup_stage3_review.py --show SPLIT_RULE
"""
from __future__ import annotations
import argparse, json, re
from itertools import combinations

ap = argparse.ArgumentParser()
ap.add_argument("--cands", default="data/kg/dedup_stage3_candidates.jsonl")
ap.add_argument("--corpus", default="data/kg/llm_struct_corpus.reviewed.jsonl")
ap.add_argument("--grounding", default="data/kg/places_grounding.jsonl")
ap.add_argument("--out", default="data/kg/dedup_stage3_review_queue.jsonl")
ap.add_argument("--show", default="")
args = ap.parse_args()

lab = {}
for l in open(args.grounding):
    r = json.loads(l)
    if r.get("qid"): lab[r["qid"]] = r["label"]

# full structured records by person_id
rec_by = {}
for l in open(args.corpus):
    r = json.loads(l); rec_by[r["person_id"]] = r

def edu_tokens(s):
    return set(t for t in re.findall(r"[a-z]{4,}", (s or "").lower())
               if t not in {"college","university","school","educated","grammar"})
def jac(a, b): return len(a & b) / len(a | b) if a and b else 0.0
def pos_norm(p): return re.sub(r"[^a-z ]", "", (p or "").lower()).strip()

def appt_keys(rec):
    """set of (normalized position, start year) — a specific appointment."""
    out = set()
    for e in rec.get("events") or []:
        if e.get("position") and e.get("year_start"):
            out.add((pos_norm(e["position"]), e["year_start"]))
    return out

def appt_overlap(recs):
    keys = [appt_keys(r) for r in recs]
    inter = set.intersection(*keys) if keys else set()
    # cumulative bio: one record's appointments fully contained in another's,
    # and the contained set is itself specific (>=2 dated appointments)
    subset = False
    for i in range(len(keys)):
        for j in range(len(keys)):
            if i != j and keys[i] and len(keys[i]) >= 2 and keys[i] <= keys[j]:
                subset = True
    return len(inter), subset

def classify(c):
    members = c["members"]
    recs = [rec_by[m["person_id"]] for m in members]
    edus = [edu_tokens(r.get("education")) for r in recs]
    best_edu = max((jac(a, b) for a, b in combinations(edus, 2)), default=0.0)
    n_inter, subset = appt_overlap(recs)
    strong_career = n_inter >= 2 or subset   # >=2 shared dated appts, or cumulative chain
    n_shared_qid = len(c["shared_qids_any"])
    births = c["births"]
    bdiff = (max(births) - min(births)) if len(births) >= 2 else 0

    if c["tier"] == "CONFLICT":
        if strong_career:
            return "MERGE_RULE", f"identical dated appointment chain ({n_inter} shared, subset={subset}) overrides birth OCR conflict"
        if bdiff <= 1 and (n_shared_qid >= 2 or best_edu >= 0.5):
            return "MERGE_RULE", "OCR birth +-1 + strong corroboration (shared qids/edu)"
        if bdiff >= 3 and best_edu < 0.2 and n_inter == 0:
            return "SPLIT_RULE", "distinct birth years, no education/appointment overlap -> namesakes"
        return "UNCERTAIN", f"birthdiff={bdiff} edu={best_edu:.2f} shared_qid={n_shared_qid} inter_appt={n_inter}"
    else:  # thin B_place
        if strong_career:
            return "MERGE_RULE", f"identical dated appointment chain ({n_inter} shared, subset={subset})"
        if n_inter >= 1 and best_edu >= 0.3:
            return "MERGE_RULE", "shared dated appointment + education overlap"
        if best_edu >= 0.5:
            return "MERGE_RULE", "strong education-string overlap"
        return "UNCERTAIN", f"thin colony+year only; edu={best_edu:.2f} inter_appt={n_inter}"

cands = [json.loads(l) for l in open(args.cands)]
held = [c for c in cands if c["tier"] == "CONFLICT" or
        (c["tier"] == "B_place" and max(m["n_events"] for m in c["members"]) <= 1
         and len(c["shared_qids_any"]) <= 1)]

from collections import Counter
buckets = Counter()
for c in held:
    verdict, reason = classify(c)
    c["_verdict"], c["_reason"] = verdict, reason
    buckets[(c["tier"], verdict)] += 1

with open(args.out, "w") as fh:
    for c in held:
        fh.write(json.dumps(c, ensure_ascii=False) + "\n")

print(f"held pockets: {len(held)} groups "
      f"(CONFLICT={sum(1 for c in held if c['tier']=='CONFLICT')}, "
      f"thin B_place={sum(1 for c in held if c['tier']=='B_place')})\n")
for (tier, v), n in sorted(buckets.items()):
    print(f"  {tier:<9} {v:<13} {n}")
print(f"\nUNCERTAIN (need hand-adjudication): "
      f"{sum(1 for c in held if c['_verdict']=='UNCERTAIN')}")
print(f"wrote -> {args.out}")

if args.show:
    rows = [c for c in held if c["_verdict"] == args.show]
    print(f"\n========== {args.show}: {len(rows)} groups ==========")
    for c in rows:
        print(f"\n### {c['surname_key'].upper()}, {c['given_key']}  "
              f"tier={c['tier']} births={c['births'] or '-'}  [{c['_reason']}]")
        for m in c["members"]:
            r = rec_by[m["person_id"]]
            print(f"  {m['person_id']}  b.{r.get('birth_year') or '-'}  "
                  f"edu={ (r.get('education') or '')[:70]!r}")
            for e in (r.get("events") or []):
                q = lab.get(__import__('json').dumps and None)  # noop
            for e in (r.get("events") or []):
                pl = e.get("place")
                print(f"       {e.get('year_start')}-{e.get('year_end')}  "
                      f"{(e.get('position') or '')[:42]:<42} @ {pl}")
