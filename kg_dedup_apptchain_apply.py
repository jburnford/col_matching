#!/usr/bin/env python3
"""Turn appt-chain under-merge candidate PAIRS into merge-map entries.

- Union-find the pairs into components (a person may be split into 3+ records).
- SAFETY per component: all members must be edition-DISJOINT (no edition-year
  appears in two members). A within-component edition collision means two real
  people got linked transitively -> the whole component is held for review, not
  merged.
- Canonical = the member with the most attestations (tie: most events).
- Emits merge-map lines {person_id, canonical_person_id} for every non-canonical
  member, appended to the school merge map that reemit_dedup.sh applies.

Usage:
  python3 kg_dedup_apptchain_apply.py            # preview components + safety
  python3 kg_dedup_apptchain_apply.py --write     # append to merge map
"""
import json, re, sys, argparse, os
from collections import defaultdict

ROOT = os.environ.get("COL_KG_OUT", "data/kg")
CANDS = f"{ROOT}/apptchain_undermerge_candidates.jsonl"
SPINE = next(p for p in (f"{ROOT}/llm_struct_corpus.stage3.deduped.jsonl",
                         f"{ROOT}/llm_struct_corpus.stage3.jsonl") if os.path.exists(p))
MAP = f"{ROOT}/dedup_stage3_merge_map.school.jsonl"
_EDTOK = re.compile(r"((?:col|dol|iol)\d{4}(?:_[a-z0-9]+)?)")

def editions(p):
    eds = set()
    for a in (p.get("attestations") or []) + [p.get("person_id","")]:
        m = _EDTOK.search(a or "")
        if m: eds.add(m.group(1))
    return eds

class UF:
    def __init__(self): self.p = {}
    def find(self, x):
        self.p.setdefault(x, x)
        while self.p[x] != x: self.p[x] = self.p[self.p[x]]; x = self.p[x]
        return x
    def union(self, a, b): self.p[self.find(a)] = self.find(b)

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--write", action="store_true")
    args = ap.parse_args()
    cands = [json.loads(l) for l in open(CANDS)]
    spine = {p["person_id"]: p for p in (json.loads(l) for l in open(SPINE))}

    uf = UF()
    for c in cands: uf.union(c["person_a"], c["person_b"])
    comps = defaultdict(set)
    for c in cands:
        r = uf.find(c["person_a"]); comps[r].add(c["person_a"]); comps[r].add(c["person_b"])

    safe, held = [], []
    for members in comps.values():
        members = sorted(members)
        eds = {m: editions(spine[m]) for m in members}
        # whole-component edition disjointness
        seen, collision = set(), False
        for m in members:
            if eds[m] & seen: collision = True; break
            seen |= eds[m]
        (held if collision else safe).append(members)

    map_lines = []
    for members in safe:
        canon = max(members, key=lambda m: (spine[m].get("n_attestations") or 1,
                                            len(spine[m].get("events") or [])))
        for m in members:
            if m != canon:
                map_lines.append({"person_id": m, "canonical_person_id": canon})

    print(f"components: {len(comps)}  safe(edition-disjoint): {len(safe)}  "
          f"held(edition-collision): {len(held)}")
    print(f"merge-map lines to add: {len(map_lines)}  "
          f"(persons folded away: {len(map_lines)})")
    print("\n-- safe components (surname | members | given forms | edition span) --")
    for members in sorted(safe, key=lambda ms: spine[ms[0]].get("surname") or ""):
        sn = spine[members[0]].get("surname")
        givens = sorted({spine[m].get("given_names") or "?" for m in members})
        span = sorted(set().union(*[editions(spine[m]) for m in members]))
        print(f"{sn:14} n={len(members)} {givens}  eds {span[0]}-{span[-1]}")
    if held:
        print("\n-- HELD (within-component edition collision — review) --")
        for members in held:
            sn = spine[members[0]].get("surname")
            print(f"{sn:14} {[ (m, sorted(editions(spine[m]))) for m in members ]}")

    if args.write:
        existing = {json.dumps(json.loads(l), sort_keys=True) for l in open(MAP)}
        added = 0
        with open(MAP, "a") as f:
            for ml in map_lines:
                if json.dumps(ml, sort_keys=True) not in existing:
                    f.write(json.dumps(ml) + "\n"); added += 1
        print(f"\nappended {added} new lines -> {MAP}")

if __name__ == "__main__":
    main()
