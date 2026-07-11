#!/usr/bin/env python3
"""Emit adjudication pairs for every within-volume link not yet judged.

Extends the B1 audit to the FULL corpus: all 79,748 links get an
individual same/different verdict. Links already judged by the sample
(b1::), contested (b1c::) or weak-tier (b1w::) runs are excluded; their
verdicts merge in volume_merge_b1_full.py.

Output data/volume/identity/b1_full_worklist.jsonl (prefix b1f::),
classc pair format — qwen_classc_worker.py runs it unchanged.
"""

from __future__ import annotations

import json
import random
from collections import defaultdict
from pathlib import Path

ROOT = Path("data/volume")
IDD = ROOT / "identity"
SEED = 20260711


def bio_lines(bio: dict) -> list[str]:
    out = []
    for ev in bio["events"]:
        span = ev.get("text_span") or (
            (ev.get("position") or "?")
            + (f" [{ev['place']}]" if ev.get("place") else ""))
        out.append(f"  {ev.get('year_start') or '?'}: {span}")
    return out[:40]


def main() -> None:
    judged: set[str] = set()
    for name in ("b1_audit_results.jsonl", "b1_contested_results.jsonl",
                 "b1_weak_results.jsonl"):
        for r in map(json.loads, open(IDD / name, encoding="utf-8")):
            if "error" not in r:
                judged.add(r["id"].split("::", 1)[1])

    todo = [f for f in map(json.loads,
                           open(IDD / "b1_link_scores.jsonl",
                                encoding="utf-8"))
            if f["link_id"] not in judged]
    by_year = defaultdict(list)
    for f in todo:
        by_year[f["edition_year"]].append(f)

    rows = []
    for year, items in sorted(by_year.items()):
        ed = ROOT / f"col{year}"
        bios = {b["bio_id"]: b for b in map(
            json.loads, open(ed / "bios.jsonl", encoding="utf-8"))}
        records = {r["record_id"]: r for r in map(
            json.loads, open(ed / "records.jsonl", encoding="utf-8"))}
        for f in items:
            bio, rec = bios[f["bio_id"]], records[f["record_id"]]
            line = f"  {year} | {rec.get('position') or '?'}"
            if rec.get("department"):
                line += f" | dept: {rec['department']}"
            if rec.get("salary"):
                line += f" | salary: {rec['salary']}"
            rows.append({
                "id": f"b1f::{f['link_id']}", "stratum": f["stratum"],
                "career_id": f["record_id"], "person_id": f["bio_id"],
                "cand_rank": 0,
                "career": {
                    "colony": rec.get("colony"),
                    "name": f"{rec.get('surname')}, {rec.get('given_names')}",
                    "roster_years": [year],
                    "lines": [line],
                },
                "person": {
                    "name": f"{bio['surname']}, {bio.get('given_names')}",
                    "birth_year": bio.get("birth_year"),
                    "honours": [h["award"] for h in bio.get("honours", [])],
                    "editions": [year, year],
                    "lines": bio_lines(bio),
                },
            })
    random.Random(SEED).shuffle(rows)
    with open(IDD / "b1_full_worklist.jsonl", "w", encoding="utf-8") as fh:
        for r in rows:
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")
    print(f"already judged: {len(judged):,}; remaining emitted: {len(rows):,}")


if __name__ == "__main__":
    main()
