#!/usr/bin/env python3
"""Find person UNDER-MERGES the birth-year veto blocked: two distinct records that
share >=3 EXACT (position-stem, year) appointments — a coincidence two different
people cannot produce — yet were kept apart (typically because a mis-extracted
"birth_year" conflicts, as with Arthur Edward Kennedy b.1862 vs b.1867, real 1809).

Signals (all required):
  - same normalised surname
  - compatible given names (equal, or initials-vs-full: "Arthur E." ~ "Arthur Edward")
  - >= MIN_SHARED shared exact (posstem, year_start) appointment pairs
  - edition-DISJOINT: the two never co-appear in one edition-year (co-listing in a
    single List = provably two different men — the killer test)

Output: data/kg/apptchain_undermerge_candidates.jsonl (review before merging).
Operates on the Stage-3 spine (each person_id is already a merged canonical, so a
distinct pair = a genuine separate person the pipeline did not fold).
"""
import json, re, sys, itertools, os
from collections import defaultdict

ROOT = os.environ.get("COL_KG_OUT", "data/kg")
# IOL canonical spine is *.stage3.deduped.jsonl (a stale *.stage3.jsonl also exists —
# prefer .deduped); CO has only *.stage3.jsonl.
SPINE = next(p for p in (f"{ROOT}/llm_struct_corpus.stage3.deduped.jsonl",
                         f"{ROOT}/llm_struct_corpus.stage3.jsonl") if os.path.exists(p))
OUT = f"{ROOT}/apptchain_undermerge_candidates.jsonl"
MIN_SHARED = 3
# edition TOKEN incl. supplement section (iol1894 != iol1894_supp): co/dol/iol volumes
_EDTOK = re.compile(r"((?:col|dol|iol)\d{4}(?:_[a-z0-9]+)?)")

def surname_norm(s): return re.sub(r"[^a-z]", "", (s or "").lower())
def posstem(p): return re.sub(r"[^a-z]", "", (p or "").lower())[:12]
def gtoks(g): return [t for t in re.split(r"[ .]+", (g or "").lower()) if t]

def given_compat(a, b):
    """equal, or one is an initials/prefix form of the other, token-aligned."""
    ta, tb = gtoks(a), gtoks(b)
    if not ta or not tb: return False
    if len(ta) > len(tb): ta, tb = tb, ta          # ta = shorter (fewer/abbrev)
    for x, y in zip(ta, tb):
        if x == y: continue
        if len(x) == 1 and y.startswith(x): continue   # initial vs full
        if len(y) == 1 and x.startswith(y): continue
        if x.startswith(y) or y.startswith(x): continue  # OCR truncation
        return False
    return True

def editions(p):
    eds = set()
    for a in (p.get("attestations") or []) + [p.get("person_id","")]:
        m = _EDTOK.search(a or "")
        if m: eds.add(m.group(1))          # e.g. "col1909", "iol1894_supp"
    return eds

def main():
    persons = [json.loads(l) for l in open(SPINE)]
    by_surname = defaultdict(list)
    for p in persons:
        p["_appts"] = {(posstem(e.get("position")), e["year_start"])
                       for e in (p.get("events") or []) if e.get("year_start") is not None
                       and posstem(e.get("position"))}
        p["_eds"] = editions(p)
        by_surname[surname_norm(p.get("surname"))].append(p)

    cands = []
    for sn, group in by_surname.items():
        if not sn or len(group) < 2: continue
        for a, b in itertools.combinations(group, 2):
            if a["person_id"] == b["person_id"]: continue
            if not given_compat(a.get("given_names"), b.get("given_names")): continue
            shared = a["_appts"] & b["_appts"]
            if len(shared) < MIN_SHARED: continue
            if a["_eds"] & b["_eds"]: continue          # co-listed => distinct people
            cands.append({
                "person_a": a["person_id"], "given_a": a.get("given_names"),
                "birth_a": a.get("birth_year"), "eds_a": sorted(a["_eds"]),
                "person_b": b["person_id"], "given_b": b.get("given_names"),
                "birth_b": b.get("birth_year"), "eds_b": sorted(b["_eds"]),
                "surname": a.get("surname"),
                "n_shared": len(shared),
                "shared_appts": sorted(f"{ps}:{yr}" for ps, yr in shared),
                "birth_conflict": bool(a.get("birth_year") and b.get("birth_year")
                                       and abs(a["birth_year"] - b["birth_year"]) > 2),
            })
    cands.sort(key=lambda c: -c["n_shared"])
    with open(OUT, "w") as f:
        for c in cands: f.write(json.dumps(c, ensure_ascii=False) + "\n")
    sys.stderr.write(f"{len(cands)} candidate under-merge pairs -> {OUT}\n")
    bc = sum(1 for c in cands if c["birth_conflict"])
    sys.stderr.write(f"  with birth-year conflict (the class the veto blocked): {bc}\n")
    for c in cands[:25]:
        print(f"{c['surname']:14} {c['given_a']!r}/{c['given_b']!r}  shared={c['n_shared']} "
              f"b={c['birth_a']}/{c['birth_b']}{' CONFLICT' if c['birth_conflict'] else ''}  "
              f"{c['eds_a']} vs {c['eds_b']}")

if __name__ == "__main__":
    main()
