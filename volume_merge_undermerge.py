#!/usr/bin/env python3
"""Merge the under-merge pair verdicts (Nibi job 17500055) into the
adjudication ledger.

Input  data/volume/identity/undermerge_results.jsonl
       (qwen_classc_worker.py --mode merge over the 384 B1-cascade pairs)
Ledger data/volume/bio_persons/undermerge_decisions.jsonl — APPEND-ONLY;
       volume_bio_persons.py union-finds decision=="approve" rows at the
       next rebuild. Pairs already in the ledger (either order) are
       skipped; verdicts map same->approve, different->reject,
       unsure->review (review rows are inert but keep the audit trail).
"""

from __future__ import annotations

import json
from collections import Counter
from pathlib import Path

ROOT = Path("data/volume")
IDD = ROOT / "identity"
LEDGER = ROOT / "bio_persons/undermerge_decisions.jsonl"
JOB = "Nibi 17500055, B1 contested-record cascade"


def main() -> None:
    existing = set()
    for r in map(json.loads, open(LEDGER, encoding="utf-8")):
        existing.add(frozenset((r["person_a"], r["person_b"])))

    worklist = {w["id"]: w for w in map(
        json.loads, open(IDD / "undermerge_worklist.jsonl",
                         encoding="utf-8"))}

    rows, stats = [], Counter()
    for r in map(json.loads, open(IDD / "undermerge_results.jsonl",
                                  encoding="utf-8")):
        if "error" in r:
            stats["error"] += 1
            continue
        _, pa, pb = r["id"].split("::")
        if frozenset((pa, pb)) in existing:
            stats["already_in_ledger"] += 1
            continue
        decision = {"same": "approve", "different": "reject"}.get(
            r["verdict"], "review")
        stats[decision] += 1
        w = worklist.get(r["id"], {})
        rows.append({
            "person_a": pa, "person_b": pb,
            "surname": (w.get("a") or {}).get("name", "").split(",")[0],
            "n_shared": len(w.get("shared_records", [])),
            "tier": "B1-cascade",
            "decision": decision,
            "confidence": r.get("confidence"),
            "reason": (r.get("reason") or "")[:250],
            "adjudicated": f"2026-07-11 qwen merge-mode ({JOB})",
        })

    with open(LEDGER, "a", encoding="utf-8") as fh:
        for r in rows:
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")
    print(f"appended {len(rows)} rows to {LEDGER}: {dict(stats)}")
    print("approves take effect at the next volume_bio_persons.py rebuild")


if __name__ == "__main__":
    main()
