#!/usr/bin/env python3
"""Fold hand adjudications into the class-C hand-verdict LEDGER
(data/volume/classc/classc_hand_verdicts.jsonl, append-only, accumulative)
that volume_apply_classc_links.py consumes ahead of the machine policy.

Sources folded (idempotent — a pair id is written once):
  nobio_silver.jsonl  pool=applied     silver 'different' -> verdict different
                                       (an applied link the close read refuted)
                      pool=judged_diff silver 'same'      -> verdict same
                                       (a judge 'different' the close read
                                       overturned = a missed link)
Rows: {id, career_id, person_id, verdict, source, confidence, evidence}.
Usage: python3 volume_silver_to_ledger.py
"""
import json
from pathlib import Path

CD = Path("data/volume/classc")
LEDGER = CD / "classc_hand_verdicts.jsonl"


def main():
    have = set()
    if LEDGER.exists():
        have = {json.loads(l)["id"] for l in LEDGER.open(encoding="utf-8")}
    added = 0
    with LEDGER.open("a", encoding="utf-8") as fh:
        for l in (CD / "nobio_silver.jsonl").open(encoding="utf-8"):
            r = json.loads(l)
            if r["id"] in have or "::" not in r["id"]:
                continue
            if r["pool"] == "applied" and r["silver_verdict"] == "different":
                v = "different"
            elif r["pool"] == "judged_diff" and r["silver_verdict"] == "same":
                v = "same"
            else:
                continue
            car, per = r["id"].split("::", 1)
            fh.write(json.dumps({"id": r["id"], "career_id": car, "person_id": per,
                                 "verdict": v, "source": "nobio_silver_2026-07-12",
                                 "confidence": r.get("confidence"),
                                 "evidence": r.get("evidence")}, ensure_ascii=False) + "\n")
            have.add(r["id"]); added += 1
    print(f"ledger {LEDGER}: +{added} rows, {len(have)} total")


if __name__ == "__main__":
    main()
