#!/usr/bin/env python3
"""Merge the weak-tier full adjudication (Nibi job 17493382).

Every weak-strength within-volume link (11,862; measured 47.5% precise in
the B1 sample) was judged individually. This folds the verdicts into a
per-link ledger so the tier is filtered link-by-link:

  same       -> keep   (with confidence)
  different  -> drop
  unsure/err -> review

Links also judged in the contested-record run (b1c:: ids) form a repeat
sample: agreement between the two independent verdicts is reported as a
judge-consistency check.

Outputs data/volume/identity/b1_weak_decisions.jsonl and appends a
weak-tier section to B1_MEASURED.md.
"""

from __future__ import annotations

import json
from collections import Counter, defaultdict
from pathlib import Path

IDD = Path("data/volume/identity")


def main() -> None:
    scores = {f["link_id"]: f for f in map(
        json.loads, open(IDD / "b1_link_scores.jsonl", encoding="utf-8"))}

    weak_v: dict[str, dict] = {}
    errs = 0
    for r in map(json.loads, open(IDD / "b1_weak_results.jsonl",
                                  encoding="utf-8")):
        if "error" in r:
            errs += 1
            continue
        weak_v[r["id"].split("::", 1)[1]] = r

    # contested-run verdicts for the same links (independent repeat)
    contested_v: dict[str, str] = {}
    for r in map(json.loads, open(IDD / "b1_contested_results.jsonl",
                                  encoding="utf-8")):
        if "error" not in r:
            contested_v[r["id"].split("::", 1)[1]] = r["verdict"]

    decisions, by_verdict = [], Counter()
    by_stratum = defaultdict(Counter)
    for link_id, r in sorted(weak_v.items()):
        rec_id, bio_id = link_id.split("::")
        v = r["verdict"]
        by_verdict[v] += 1
        st = scores.get(link_id, {}).get("stratum", "?")
        by_stratum[st][v] += 1
        action = {"same": "keep", "different": "drop"}.get(v, "review")
        decisions.append({
            "record_id": rec_id, "bio_id": bio_id, "action": action,
            "basis": f"weak_tier verdict={v} conf={r.get('confidence')}",
            "reason": (r.get("reason") or "")[:200]})
    with open(IDD / "b1_weak_decisions.jsonl", "w", encoding="utf-8") as fh:
        for d in decisions:
            fh.write(json.dumps(d, ensure_ascii=False) + "\n")

    both = {k: (r["verdict"], contested_v[k])
            for k, r in weak_v.items() if k in contested_v}
    agree = sum(1 for a, b in both.values() if a == b)

    n = len(weak_v)
    keep = by_verdict["same"]
    lines = [
        "",
        "## Weak-tier full adjudication (Nibi job 17493382)",
        "",
        f"{n:,} weak links judged ({errs} errors):"
        f" keep {keep:,} ({keep / n:.1%}), drop {by_verdict['different']:,},"
        f" review {by_verdict['unsure']:,}.",
        "",
        "| stratum | judged | keep | drop | unsure |",
        "|---|---|---|---|---|",
    ]
    for st in sorted(by_stratum):
        v = by_stratum[st]
        lines.append(f"| {st} | {sum(v.values()):,} | {v['same']:,} |"
                     f" {v['different']:,} | {v['unsure']:,} |")
    lines += [
        "",
        f"Judge consistency: {len(both):,} links independently judged in"
        f" the contested run too; verdicts agree on {agree:,}"
        f" ({agree / len(both):.1%})." if both else
        "No overlap with the contested run.",
        "",
        "Per-link ledger: b1_weak_decisions.jsonl (keep/drop/review).",
    ]
    with open(IDD / "B1_MEASURED.md", "a", encoding="utf-8") as fh:
        fh.write("\n".join(lines) + "\n")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
