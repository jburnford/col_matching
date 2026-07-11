#!/usr/bin/env python3
"""Apply the B1 master ledger: drop refuted within-volume links.

Reads data/volume/identity/b1_link_verdicts.jsonl (every link judged;
keep 68,343 / drop 11,248 / review 157) and rewrites each edition's
links.jsonl WITHOUT the action=="drop" links. review/keep links stay
(unlinked is the conservative direction only for drops the judge actually
refuted). First run backs up the original as links.pre_b1.jsonl; reruns
are idempotent against the backup.

Downstream rebuild after this (order matters):
  volume_bio_persons.py        (also applies pending under-merge approves)
  volume_careers.py            (bio_ids re-derived from filtered links)
  <remap classc person ids>    via bio_persons/person_id_merges.jsonl
  volume_transfers.py, volume_kg.py, volume_audit.py
  volume_identity_check.py     (remeasure, lower baselines in-file)
"""

from __future__ import annotations

import json
from collections import Counter
from pathlib import Path

ROOT = Path("data/volume")
IDD = ROOT / "identity"


def main() -> None:
    drops: dict[int, set[str]] = {}
    n_drop = 0
    for r in map(json.loads, open(IDD / "b1_link_verdicts.jsonl",
                                  encoding="utf-8")):
        if r["action"] == "drop":
            drops.setdefault(r["edition_year"], set()).add(r["link_id"])
            n_drop += 1
    print(f"ledger: {n_drop:,} drop links across {len(drops)} editions")

    total = Counter()
    for d in sorted(ROOT.glob("col*")):
        if not (d / "links.jsonl").exists():
            continue
        year = int(d.name[3:])
        src = d / "links.pre_b1.jsonl"
        if not src.exists():                      # first run: back up
            (d / "links.jsonl").rename(src)
        bad = drops.get(year, set())
        kept = dropped = 0
        with open(d / "links.jsonl", "w", encoding="utf-8") as out:
            for line in open(src, encoding="utf-8"):
                ln = json.loads(line)
                if f"{ln['record_id']}::{ln['bio_id']}" in bad:
                    dropped += 1
                    continue
                out.write(line)
                kept += 1
        total["kept"] += kept
        total["dropped"] += dropped
    print(f"links kept {total['kept']:,}, dropped {total['dropped']:,}"
          f" (originals in links.pre_b1.jsonl)")


if __name__ == "__main__":
    main()
