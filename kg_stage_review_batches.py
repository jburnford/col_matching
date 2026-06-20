#!/usr/bin/env python3
"""Stage the flagged-drop review queue into per-person batches for an in-session
reviewer fan-out (see docs/REVIEW_RUN.md).

Groups data/kg/review/llm_review_queue.jsonl by person (so each bio's source is
read once) and chunks into batch files of <= --per persons. Each batch line:
  {person_id, source_text, packets:[{field_path, flagged_value, reason}]}

  python3 kg_stage_review_batches.py [--per 80]
"""
from __future__ import annotations

import argparse
import json
import os
from collections import defaultdict
from pathlib import Path

OUT = Path("data/kg/review")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--per", type=int, default=80)
    args = ap.parse_args()

    by_person: dict = defaultdict(list)
    source: dict = {}
    for l in (OUT / "llm_review_queue.jsonl").open(encoding="utf-8"):
        p = json.loads(l)
        source[p["person_id"]] = p["source_text"]
        by_person[p["person_id"]].append(
            {"field_path": p["field_path"], "flagged_value": p["flagged_value"], "reason": p["reason"]})
    persons = [{"person_id": pid, "source_text": source[pid], "packets": pk}
               for pid, pk in by_person.items()]

    bdir = OUT / "batches"
    bdir.mkdir(parents=True, exist_ok=True)
    (OUT / "verdicts").mkdir(parents=True, exist_ok=True)
    for f in bdir.glob("batch_*.jsonl"):
        f.unlink()
    nb = 0
    for i in range(0, len(persons), args.per):
        nb += 1
        with (bdir / f"batch_{nb:03d}.jsonl").open("w", encoding="utf-8") as fh:
            for p in persons[i:i + args.per]:
                fh.write(json.dumps(p, ensure_ascii=False) + "\n")
    print(f"packets={sum(len(p['packets']) for p in persons)}  persons={len(persons)}  "
          f"batches={nb} (<= {args.per}/batch) -> {bdir}")


if __name__ == "__main__":
    main()
