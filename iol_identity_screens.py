#!/usr/bin/env python3
"""Tier-A identity screens over the IOL canonical persons (docs/IOL_VS_COL.md §8).

Reuses the COL screen implementations (volume_identity_screens) unchanged —
the CSI/KCSI/GCSI and CIE/KCIE/GCIE ladders are already in ORDER_LADDERS —
via a light adapter from the stage-3 deduped structured corpus to the
bio_persons record shape the screens expect.

What runs here and what doesn't (see the assessment doc):
  A1  honours precedence      unchanged (dated honours only, 56% of entries)
  A2  age invariants + repair unchanged, but only the ~48% of persons with a
      birth year (the List prints (b. ...) only from c.1929)
  A2h birth-from-honour       unchanged
  A6  rare-honour duplicates  unchanged
  --  A2 birth-vote conflicts SKIPPED (no birth_year_votes in this table)
  --  A3 salary regression    DEAD (the IOL prints no per-officer salaries)

Inputs  data/iol/llm_struct_corpus.stage3.deduped.jsonl
Outputs data/iol/identity/{a1_honour_precedence,a2_age_invariants,
        a2_birth_from_honour,a6_honour_duplicates}.jsonl + SCREENS.md

Candidates feed adjudication; nothing here mutates the person table.
"""

from __future__ import annotations

import json
from collections import Counter
from pathlib import Path

from volume_identity_screens import (screen_a1, screen_a2_birth_from_honour,
                                     screen_a2_invariants, screen_a6)

ROOT = Path("data/iol")
OUT = ROOT / "identity"


def load_persons() -> list[dict]:
    persons = []
    for line in open(ROOT / "llm_struct_corpus.stage3.deduped.jsonl",
                     encoding="utf-8"):
        r = json.loads(line)
        persons.append({
            "person_id": r["person_id"],
            "surname": r.get("surname"),
            "given_names": r.get("given_names"),
            "birth_year": r.get("birth_year"),
            "honours": r.get("honours") or [],
            "events": r.get("events") or [],
            "editions": r.get("editions") or [],
            # screens report n_members for context; the IOL analogue is the
            # number of stage-3-folded structured records
            "n_members": r.get("n_stage3_merged") or 1,
            "flags": r.get("flags") or [],
        })
    return persons


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    persons = load_persons()

    a1 = screen_a1(persons)
    a2 = screen_a2_invariants(persons)
    a2h = screen_a2_birth_from_honour(persons)
    a6 = screen_a6(persons)

    for name, rows in [("a1_honour_precedence", a1),
                       ("a2_age_invariants", a2),
                       ("a2_birth_from_honour", a2h),
                       ("a6_honour_duplicates", a6)]:
        with open(OUT / f"{name}.jsonl", "w", encoding="utf-8") as f:
            for r in rows:
                f.write(json.dumps(r, ensure_ascii=False) + "\n")

    n_birth = sum(1 for p in persons if p["birth_year"])
    n_hon = sum(1 for p in persons if p["honours"])
    diag = Counter(r["diagnosis"] for r in a2)
    flags = Counter(f for r in a2 for f in r["flags"])
    a6_strong = sum(1 for r in a6 if r["editions_disjoint"]
                    and not r["birth_conflict"])
    lines = [
        "# Tier-A identity screens — India Office List person table",
        "",
        f"Over {len(persons):,} canonical persons "
        f"({n_birth:,} with birth years, {n_hon:,} with honours).",
        "",
        "## A1 honours-precedence violations (over-merge / garbled year)",
        f"- persons flagged: **{len(a1)}**",
        "",
        "## A2 age invariants",
        f"- persons flagged: **{len(a2)}** "
        f"(entry_too_young {flags.get('entry_too_young', 0)}, "
        f"entry_too_old {flags.get('entry_too_old', 0)}, "
        f"active_past_75 {flags.get('active_past_75', 0)})",
        f"- diagnosis: {dict(diag)}",
        "",
        "## A2 birth year absorbed from an honour year (parser bug)",
        f"- persons flagged: **{len(a2h)}** — null the birth year, do not"
        " digit-repair.",
        "",
        "## A6 same-honour duplicate persons (under-merge)",
        f"- candidate pairs: **{len(a6)}**; strong (edition-disjoint, no"
        f" birth conflict): **{a6_strong}**",
        "",
        "Candidate files feed the adjudication ledger; nothing applied.",
    ]
    (OUT / "SCREENS.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
