#!/usr/bin/env python3
"""Logical-consistency checks on the Stage-3 persons -- and a false-merge detector.

A bad merge (two people folded into one) shows up as an implausibly long career,
a career spanning more than one lifetime, or events inconsistent with the birth
year. We flag:

  IMPOSSIBLE_BIRTH  career starts before birth_year, or first post at age < 15
  LONG_CAREER       career span (first->last dated event) > 55 yrs
  OLD_WORKER        last dated event at age > 85
  BAD_YEAR          a dated event outside [1750,1970]
  BIRTH_OUTLIER     birth_year outside [1780,1950]

Merged persons (n_stage3_merged>1) with these flags are the dedup's suspects and
are reported first.

  python3 kg_dedup_stage3_check.py [--show 40]
"""
from __future__ import annotations
import argparse, json

ap = argparse.ArgumentParser()
ap.add_argument("--corpus", default="data/kg/llm_struct_corpus.stage3.jsonl")
ap.add_argument("--out", default="data/kg/dedup_stage3_logic_flags.jsonl")
ap.add_argument("--show", type=int, default=40)
args = ap.parse_args()

def years(rec):
    ys = []
    for e in rec.get("events") or []:
        for y in (e.get("year_start"), e.get("year_end")):
            if isinstance(y, int) and 1500 <= y <= 2100: ys.append(y)
    return ys

rows = [json.loads(l) for l in open(args.corpus)]
flagged = []
for r in rows:
    ys = years(r)
    by = r.get("birth_year")
    flags = []
    bad_years = [y for y in ys if y < 1750 or y > 1970]
    if bad_years: flags.append(("BAD_YEAR", f"events at {sorted(set(bad_years))}"))
    if by is not None and (by < 1780 or by > 1950):
        flags.append(("BIRTH_OUTLIER", f"birth_year={by}"))
    if ys:
        lo, hi = min(ys), max(ys)
        span = hi - lo
        if span > 55: flags.append(("LONG_CAREER", f"{lo}-{hi} = {span}yr"))
        if by and 1780 <= by <= 1950:
            if lo < by: flags.append(("IMPOSSIBLE_BIRTH", f"first event {lo} < birth {by}"))
            elif lo - by < 15: flags.append(("IMPOSSIBLE_BIRTH", f"first post at age {lo-by}"))
            if hi - by > 85: flags.append(("OLD_WORKER", f"last event at age {hi-by}"))
    if flags:
        flagged.append({
            "person_id": r["person_id"],
            "name": f"{r.get('surname')}, {r.get('given_names')}",
            "birth_year": by,
            "year_lo": min(ys) if ys else None, "year_hi": max(ys) if ys else None,
            "n_merged": r.get("n_stage3_merged", 1),
            "editions": r.get("editions"),
            "attestations": r.get("attestations"),
            "flag_types": [f[0] for f in flags],
            "detail": "; ".join(f"{f[0]}:{f[1]}" for f in flags),
        })

with open(args.out, "w") as fh:
    for f in flagged: fh.write(json.dumps(f, ensure_ascii=False) + "\n")

from collections import Counter
tc = Counter(t for f in flagged for t in f["flag_types"])
merged_flagged = [f for f in flagged if f["n_merged"] > 1]
print(f"persons checked: {len(rows):,}  | flagged: {len(flagged):,} "
      f"({len(merged_flagged):,} are stage-3 MERGED -> dedup suspects)\n")
print("flag-type counts (a person can carry several):")
for t, n in tc.most_common(): print(f"  {t:<17}{n}")

# the highest-stakes: MERGED persons with an impossible/long-career flag
susp = [f for f in merged_flagged
        if {"IMPOSSIBLE_BIRTH", "LONG_CAREER"} & set(f["flag_types"])]
susp.sort(key=lambda f: (f["year_hi"] or 0) - (f["year_lo"] or 0), reverse=True)
print(f"\n=== MERGED + (LONG_CAREER|IMPOSSIBLE_BIRTH): {len(susp)} false-merge suspects "
      f"(top {min(args.show,len(susp))} by span) ===")
for f in susp[:args.show]:
    print(f"  {f['name'][:34]:<34} b.{str(f['birth_year'] or '-'):<6} "
          f"{f['year_lo']}-{f['year_hi']}  n={f['n_merged']}  [{f['detail']}]")
    print(f"        {f['attestations']}")
print(f"\nwrote -> {args.out}")
