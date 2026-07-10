#!/usr/bin/env python3
"""Re-key class-C adjudication verdicts after a careers rebuild.

career_ids are positional (colony|surname|k) and renumber whenever the roster
corpus changes, so verdicts from a Nibi run against an older careers build
must be joined onto the current worklist by CONTENT: a pair is the same
adjudication problem iff (person_id, colony, career name, first/last roster
year) match — the evidence the model saw.

Inputs:
  --old-worklist   the worklist the verdicts were produced against
                   (e.g. git show <sha>:data/volume/classc/classc_worklist.jsonl)
  data/volume/classc/classc_results.jsonl   verdicts keyed by OLD pair ids
  data/volume/classc/classc_worklist.jsonl  CURRENT worklist (new pair ids)

Outputs (data/volume/classc/):
  classc_results.jsonl        verdicts re-keyed to current pair ids (the
                              original file is kept at classc_results.<tag>.jsonl)
  classc_worklist_delta.jsonl current pairs with NO reusable verdict — the
                              next GPU batch (new post-war careers, mostly)

Usage: python3 volume_remap_classc_results.py --old-worklist OLD.jsonl --tag run1
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

CLASSDIR = Path("data/volume/classc")


def content_key(pair: dict) -> tuple:
    c = pair["career"]
    y = c.get("roster_years") or [0]
    return (pair["person_id"], c["colony"], c["name"].lower(), y[0], y[-1])


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--old-worklist", required=True)
    ap.add_argument("--tag", default="run1")
    args = ap.parse_args()

    old_key = {}
    for line in open(args.old_worklist, encoding="utf-8"):
        p = json.loads(line)
        old_key[p["id"]] = content_key(p)

    verdicts = {}          # content key -> verdict row
    orig_lines = []
    for line in (CLASSDIR / "classc_results.jsonl").open(encoding="utf-8"):
        orig_lines.append(line)
        r = json.loads(line)
        if "error" in r or r["id"] not in old_key:
            continue
        verdicts[old_key[r["id"]]] = r

    backup = CLASSDIR / f"classc_results.{args.tag}.jsonl"
    if not backup.exists():
        backup.write_text("".join(orig_lines), encoding="utf-8")

    reused = 0
    delta = []
    with (CLASSDIR / "classc_results.jsonl").open("w", encoding="utf-8") as fh:
        for line in (CLASSDIR / "classc_worklist.jsonl").open(encoding="utf-8"):
            p = json.loads(line)
            v = verdicts.get(content_key(p))
            if v is None:
                delta.append(p)
                continue
            reused += 1
            fh.write(json.dumps({
                "id": p["id"], "career_id": p["career_id"],
                "person_id": p["person_id"], "cand_rank": p.get("cand_rank"),
                "verdict": v["verdict"], "confidence": v.get("confidence"),
                "reason": v.get("reason"), "reused_from": args.tag,
            }, ensure_ascii=False) + "\n")
    with (CLASSDIR / "classc_worklist_delta.jsonl").open("w", encoding="utf-8") as fh:
        for p in delta:
            fh.write(json.dumps(p, ensure_ascii=False) + "\n")
    print(f"verdicts reused: {reused:,}; delta pairs needing adjudication: "
          f"{len(delta):,} -> classc_worklist_delta.jsonl")


if __name__ == "__main__":
    main()
