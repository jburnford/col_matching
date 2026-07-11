#!/usr/bin/env python3
"""Convert the IOL merge-audit verdicts from Nibi into measured precision.

Input   data/iol/identity/merge_audit_results.jsonl
        (qwen_classc_worker.py --mode ioldedup output for the 1,800-pair
        stratified sample from iol_merge_audit.py; verdicts
        same | different | unsure, ids iolm::<person_a>::<person_b>)
Reads   data/iol/identity/merge_edge_scores.jsonl for stratum weights.

Outputs data/iol/identity/merge_measured.json + MERGE_MEASURED.md:
        precision per stratum with Wilson CIs, evidence-class rollups, and
        the stratum-weighted corpus-wide rate — the measured number the IOL
        person table has been missing. Also emits the per-edge verdict
        ledger rows for the eventual apply step
        (merge_audit_verdicts.jsonl: person_a/person_b/stratum/verdict).

Nothing is applied here.
"""

from __future__ import annotations

import json
import math
from collections import Counter, defaultdict
from pathlib import Path

IDD = Path("data/iol/identity")


def wilson(k: int, n: int, z: float = 1.96) -> tuple[float, float]:
    if n == 0:
        return (0.0, 1.0)
    p = k / n
    d = 1 + z * z / n
    c = (p + z * z / (2 * n)) / d
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
    return (max(0.0, c - h), min(1.0, c + h))


def main() -> None:
    weights = Counter(f["stratum"] for f in
                      map(json.loads, open(IDD / "merge_edge_scores.jsonl")))
    results, errors = [], 0
    for line in open(IDD / "merge_audit_results.jsonl", encoding="utf-8"):
        r = json.loads(line)
        if "error" in r:
            errors += 1
            continue
        results.append(r)

    by_stratum = defaultdict(Counter)
    ledger = []
    for r in results:
        st = r.get("stratum") or "?"
        by_stratum[st][r["verdict"]] += 1
        ledger.append({"person_a": r.get("person_a"),
                       "person_b": r.get("person_b"),
                       "stratum": st,
                       "evidence_class": r.get("evidence_class"),
                       "verdict": r["verdict"],
                       "confidence": r.get("confidence"),
                       "reason": r.get("reason")})
    with open(IDD / "merge_audit_verdicts.jsonl", "w", encoding="utf-8") as fh:
        for row in ledger:
            fh.write(json.dumps(row, ensure_ascii=False) + "\n")

    table, wnum, wden = [], 0.0, 0
    for st in sorted(by_stratum):
        c = by_stratum[st]
        same, diff, uns = c["same"], c["different"], c["unsure"]
        dec = same + diff
        prec = same / dec if dec else None
        lo, hi = wilson(same, dec)
        table.append({"stratum": st, "edges": weights.get(st, 0),
                      "judged": sum(c.values()), "same": same,
                      "different": diff, "unsure": uns,
                      "precision": prec,
                      "ci95": [round(lo, 3), round(hi, 3)]})
        if prec is not None:
            wnum += prec * weights.get(st, 0)
            wden += weights.get(st, 0)
    overall = wnum / wden if wden else None

    # evidence-class rollups (weighted across the class's strata);
    # stratum = base:A_birth:high (class base:A_birth) or roleyear (itself)
    cls_roll = []
    by_cls = defaultdict(list)
    for row in table:
        parts = row["stratum"].split(":")
        cls = ":".join(parts[:-1]) if parts[-1] in ("high", "mid", "low") \
            else row["stratum"]
        by_cls[cls].append(row)
    for cls in sorted(by_cls):
        rows = by_cls[cls]
        n = sum(r["edges"] for r in rows)
        num = sum(r["precision"] * r["edges"] for r in rows
                  if r["precision"] is not None)
        den = sum(r["edges"] for r in rows if r["precision"] is not None)
        cls_roll.append({"class": cls, "edges": n,
                         "precision": num / den if den else None})

    out = {"overall_weighted_precision": overall,
           "judged": len(results), "errors": errors,
           "strata": table, "classes": cls_roll}
    (IDD / "merge_measured.json").write_text(
        json.dumps(out, indent=1), encoding="utf-8")

    lines = [
        "# IOL merge-map measured precision (Nibi job 17504437)",
        "",
        f"Stratified sample: {len(results):,} judged edges"
        + (f" ({errors} errors)" if errors else "") + ".",
        f"Corpus-wide stratum-weighted precision: "
        f"**{overall:.1%}**" if overall is not None else "no verdicts",
        "(unsure excluded from denominators).",
        "",
        "| stratum | edges | judged | same | diff | unsure | precision | 95% CI |",
        "|---|---|---|---|---|---|---|---|",
    ]
    for r in table:
        p = f"{r['precision']:.1%}" if r["precision"] is not None else "—"
        lines.append(
            f"| {r['stratum']} | {r['edges']:,} | {r['judged']} | {r['same']} "
            f"| {r['different']} | {r['unsure']} | {p} "
            f"| {r['ci95'][0]:.1%}–{r['ci95'][1]:.1%} |")
    lines += ["", "## Evidence-class rollups", "",
              "| class | edges | weighted precision |", "|---|---|---|"]
    for r in cls_roll:
        p = f"{r['precision']:.1%}" if r["precision"] is not None else "—"
        lines.append(f"| {r['class']} | {r['edges']:,} | {p} |")
    lines += ["", "Per-edge verdicts: merge_audit_verdicts.jsonl (ledger; "
              "apply step pending).",]
    (IDD / "MERGE_MEASURED.md").write_text("\n".join(lines) + "\n",
                                           encoding="utf-8")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
