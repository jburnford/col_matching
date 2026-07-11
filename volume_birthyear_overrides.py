#!/usr/bin/env python3
"""Build the birth-year override ledger from the Tier-A screen outputs.

Precedence (first source claiming a person wins):

  1. a2_birth_from_honour.jsonl      birth year is an absorbed honour year
                                     -> NULL (never digit-repair these)
  2. a2_birthyear_resolutions.jsonl  vote conflicts -> the plausible
                                     reading (unique_plausible,
                                     majority_of_plausible, band_relaxed);
                                     no_plausible_reading -> NULL;
                                     span-two-lives -> SKIPPED (identity
                                     problem, not a data repair)
  3. a2_age_invariants.jsonl         OCR digit repairs — applied ONLY when
                                     exactly one candidate year survives
                                     the entry-age + lifetime constraints;
                                     ambiguous repairs stay queued

Output data/volume/bio_persons/birth_year_overrides.jsonl
       {person_id, birth_year: int|null, basis} — consumed by
       volume_bio_persons.py at build time (survives rebuilds).
"""

from __future__ import annotations

import json
from collections import Counter
from pathlib import Path

ROOT = Path("data/volume")
IDD = ROOT / "identity"
OUT = ROOT / "bio_persons/birth_year_overrides.jsonl"


def main() -> None:
    overrides: dict[str, dict] = {}
    stats = Counter()

    # ACCUMULATIVE: the screens run against the post-override table, so a
    # fresh build no longer re-derives applied fixes — losing them here
    # would revert them at the next rebuild. Existing entries are kept;
    # new adjudications only add persons not already in the ledger.
    if OUT.exists():
        for r in map(json.loads, open(OUT, encoding="utf-8")):
            overrides[r["person_id"]] = r
            stats["kept_existing"] += 1

    for r in map(json.loads, open(IDD / "a2_birth_from_honour.jsonl",
                                  encoding="utf-8")):
        # highest priority: supersedes an earlier vote/repair override
        # whose picked year turned out to be an honour year
        prev = overrides.get(r["person_id"])
        if prev and prev["basis"].startswith("honour_absorption"):
            continue
        if prev:
            stats["superseded_by_honour_null"] += 1
        overrides[r["person_id"]] = {
            "person_id": r["person_id"], "birth_year": None,
            "basis": f"honour_absorption (was {r['birth_year']})"}
        stats["null_honour_absorption"] += 1

    for r in map(json.loads, open(IDD / "a2_birthyear_resolutions.jsonl",
                                  encoding="utf-8")):
        if r["person_id"] in overrides:
            stats["skip_lower_priority"] += 1
            continue
        res = r["resolution"]
        if res == "no_plausible_reading_span2lives":
            stats["skip_span2lives"] += 1
            continue
        if r["suggested_birth_year"] is not None:
            if r["suggested_birth_year"] == r.get("current_birth_year"):
                stats["already_current"] += 1
                continue
            overrides[r["person_id"]] = {
                "person_id": r["person_id"],
                "birth_year": r["suggested_birth_year"],
                "basis": f"vote_resolution:{res}"
                         f" (was {r.get('current_birth_year')})"}
            stats[f"vote_{res}"] += 1
        else:
            overrides[r["person_id"]] = {
                "person_id": r["person_id"], "birth_year": None,
                "basis": f"vote_resolution:{res}"
                         f" (was {r.get('current_birth_year')})"}
            stats["null_no_plausible"] += 1

    for r in map(json.loads, open(IDD / "a2_age_invariants.jsonl",
                                  encoding="utf-8")):
        if r["person_id"] in overrides:
            stats["skip_lower_priority"] += 1
            continue
        if r["diagnosis"] not in ("birth_year_ocr", "birth_year_ocr_2digit"):
            continue
        cands = r["suggested_birth_years"]
        if len(cands) != 1:
            stats[f"ambiguous_{r['diagnosis']}"] += 1
            continue
        overrides[r["person_id"]] = {
            "person_id": r["person_id"], "birth_year": cands[0],
            "basis": f"{r['diagnosis']} (was {r['birth_year']})"}
        stats[f"repair_{r['diagnosis']}"] += 1

    with open(OUT, "w", encoding="utf-8") as fh:
        for pid in sorted(overrides):
            fh.write(json.dumps(overrides[pid], ensure_ascii=False) + "\n")
    print(f"{len(overrides)} overrides -> {OUT}")
    for k, v in sorted(stats.items()):
        print(f"  {k}: {v}")


if __name__ == "__main__":
    main()
