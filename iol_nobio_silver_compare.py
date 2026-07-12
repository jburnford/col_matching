#!/usr/bin/env python3
"""Score the no-bio pipeline against the hand-labeled silver standard
(nobio_silver.jsonl: 85 close-read items across the four pools,
labeled 2026-07-12; ids match the shipped worklists).

Two measurements:
  1. deterministic-tier precision — silver labels on det edges judge
     the edges the apply step will union WITHOUT any LLM review;
  2. judge agreement — when res_nobio / res_abc / res_chain are
     fetched, each verdict is scored against its silver label
     (chain pool: confirm/reject; others: same/different).
Silver 'unsure' rows are excluded from denominators.

Output: printed report + data/iol/identity/NOBIO_SILVER.md
"""

from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict
from pathlib import Path

IDD = Path("data/iol/identity")


def load_jsonl(path: Path) -> list[dict]:
    if not path.exists():
        return []
    return [json.loads(l) for l in open(path, encoding="utf-8")]


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--adjudicate-dir", default=str(IDD / "adjudicate"))
    args = ap.parse_args()
    adj = Path(args.adjudicate_dir)

    silver = load_jsonl(IDD / "nobio_silver.jsonl")
    lines = ["# Silver-standard scores", "",
             f"{len(silver)} hand-labeled items "
             f"({sum(1 for s in silver if s['silver_verdict'] == 'unsure')}"
             " unsure, excluded from denominators)", ""]

    # 1. det-tier precision (edges applied without LLM review)
    det_ids = {f"nbu::{e['a']}::{e['b']}": e for e in
               load_jsonl(IDD / "nobio_unify_edges.jsonl")}
    per_tier = defaultdict(Counter)
    for s in silver:
        if s["pool"] != "det" or s["id"] not in det_ids:
            continue
        tier = det_ids[s["id"]]["tier"]
        per_tier[tier][s["silver_verdict"]] += 1
        per_tier["all"][s["silver_verdict"]] += 1
    lines.append("## Deterministic-tier precision (silver-judged)")
    lines.append("")
    for tier in ("det_strong", "det_std", "all"):
        c = per_tier[tier]
        n = c["same"] + c["different"]
        if n:
            lines.append(f"- {tier}: {c['same']}/{n} correct "
                         f"({100 * c['same'] / n:.0f}%), "
                         f"{c['unsure']} unsure")
    lines.append("")

    # 2. judge agreement per pool
    res = {}
    for name in ("res_nobio", "res_abc", "res_chain"):
        for r in load_jsonl(adj / f"{name}.jsonl"):
            if "error" not in r:
                res[r["id"]] = r["verdict"]
    if res:
        agree = defaultdict(Counter)
        for s in silver:
            v = res.get(s["id"])
            if v is None or s["silver_verdict"] == "unsure":
                continue
            ok = (v == s["silver_verdict"] or
                  (v == "confirm" and s["silver_verdict"] == "confirm"))
            agree[s["pool"]]["agree" if ok else "disagree"] += 1
            if v == "unsure":
                agree[s["pool"]]["judge_unsure"] += 1
        lines.append("## Judge agreement vs silver")
        lines.append("")
        for pool, c in sorted(agree.items()):
            n = c["agree"] + c["disagree"]
            if n:
                lines.append(
                    f"- {pool}: {c['agree']}/{n} agree "
                    f"({100 * c['agree'] / n:.0f}%), judge-unsure "
                    f"{c['judge_unsure']}")
        # disagreements in full — each is either a judge error or a
        # silver error; adjudicate by hand
        lines.append("")
        lines.append("### Disagreements")
        for s in silver:
            v = res.get(s["id"])
            if v and s["silver_verdict"] not in ("unsure", v) \
                    and v != "unsure":
                lines.append(f"- {s['id']}: judge={v} silver="
                             f"{s['silver_verdict']} — {s['evidence']}")
    else:
        lines.append("## Judge agreement — res_* not fetched yet")

    (IDD / "NOBIO_SILVER.md").write_text("\n".join(lines) + "\n",
                                         encoding="utf-8")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
