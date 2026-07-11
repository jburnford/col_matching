#!/usr/bin/env python3
"""Merge the B1 link-audit verdicts from Nibi (job 17492845).

Two result files (qwen_classc_worker.py output; verdicts same | different |
unsure, ids prefixed b1:: / b1c:: + record_id::bio_id):

  b1_audit_results.jsonl      1,650-pair stratified sample ->
                              MEASURED precision per stratum, Wilson CIs,
                              and the stratum-weighted corpus-wide rate —
                              the number the methods section needs.
  b1_contested_results.jsonl  all links on roster records claimed by >1
                              bio -> per-record resolution:
                                one 'same'   keep it, drop the rivals
                                >1  'same'   duplicate-bio suspect -> review
                                zero 'same'  no winner -> review (drop all
                                             'different', keep 'unsure')

Outputs (data/volume/identity/):
  b1_measured.json / B1_MEASURED.md    precision tables
  b1_contested_decisions.jsonl         per-LINK ledger rows
                                       {record_id, bio_id, action:
                                        keep|drop|review, basis}
Nothing is applied here; volume_relink or a dedicated apply step consumes
the decisions ledger.
"""

from __future__ import annotations

import json
import math
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path("data/volume")
IDD = ROOT / "identity"


def wilson(k: int, n: int, z: float = 1.96) -> tuple[float, float]:
    if n == 0:
        return (0.0, 1.0)
    p = k / n
    d = 1 + z * z / n
    c = (p + z * z / (2 * n)) / d
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
    return (max(0.0, c - h), min(1.0, c + h))


def load(path: Path) -> list[dict]:
    rows = []
    for line in open(path, encoding="utf-8"):
        r = json.loads(line)
        if "error" not in r:
            rows.append(r)
    return rows


def link_key(rid: str) -> str:
    return rid.split("::", 1)[1]  # strip b1:: / b1c:: prefix


def main() -> None:
    scores = {f["link_id"]: f
              for f in map(json.loads, open(IDD / "b1_link_scores.jsonl",
                                            encoding="utf-8"))}

    # ---- stratified sample -> measured precision ------------------------
    sample = load(IDD / "b1_audit_results.jsonl")
    by_stratum = defaultdict(list)
    for r in sample:
        f = scores.get(link_key(r["id"]))
        if f:
            by_stratum[f["stratum"]].append(r["verdict"])

    strata_n = Counter(f["stratum"] for f in scores.values())
    table, weighted_num, weighted_den = [], 0.0, 0
    for st in sorted(strata_n):
        vs = Counter(by_stratum.get(st, []))
        same, diff, uns = vs["same"], vs["different"], vs["unsure"]
        n_dec = same + diff
        prec = same / n_dec if n_dec else None
        lo, hi = wilson(same, n_dec) if n_dec else (0.0, 1.0)
        table.append({
            "stratum": st, "links": strata_n[st], "judged": len(
                by_stratum.get(st, [])),
            "same": same, "different": diff, "unsure": uns,
            "precision": prec, "ci95": [round(lo, 3), round(hi, 3)],
        })
        if prec is not None:
            weighted_num += strata_n[st] * prec
            weighted_den += strata_n[st]
    corpus_precision = weighted_num / weighted_den if weighted_den else None
    # split the headline by weak vs non-weak (the tiers behave differently)
    parts = {}
    for grp, pred in [("weak", lambda s: s.startswith("weak")),
                      ("nonweak", lambda s: not s.startswith("weak"))]:
        gn = gp = 0
        for t in table:
            if pred(t["stratum"]) and t["precision"] is not None:
                gn += t["links"]
                gp += t["links"] * t["precision"]
        parts[grp] = {"links": gn, "precision": gp / gn if gn else None}

    # ---- contested records -> decisions --------------------------------
    contested = load(IDD / "b1_contested_results.jsonl")
    by_record = defaultdict(list)
    for r in contested:
        key = link_key(r["id"])
        rec_id, bio_id = key.split("::")
        by_record[rec_id].append((bio_id, r["verdict"],
                                  r.get("confidence"), r.get("reason", "")))
    decisions, outcome = [], Counter()
    for rec_id, votes in sorted(by_record.items()):
        sames = [v for v in votes if v[1] == "same"]
        if len(sames) == 1:
            outcome["resolved_one_winner"] += 1
            for bio_id, verdict, conf, reason in votes:
                act = "keep" if verdict == "same" else (
                    "drop" if verdict == "different" else "review")
                decisions.append({
                    "record_id": rec_id, "bio_id": bio_id, "action": act,
                    "basis": f"contested:one_winner verdict={verdict}"
                             f" conf={conf}", "reason": reason[:200]})
        elif len(sames) > 1:
            outcome["duplicate_bio_suspect"] += 1
            for bio_id, verdict, conf, reason in votes:
                decisions.append({
                    "record_id": rec_id, "bio_id": bio_id,
                    "action": "review",
                    "basis": f"contested:multi_same verdict={verdict}"
                             f" conf={conf}", "reason": reason[:200]})
        else:
            outcome["no_winner"] += 1
            for bio_id, verdict, conf, reason in votes:
                act = "drop" if verdict == "different" else "review"
                decisions.append({
                    "record_id": rec_id, "bio_id": bio_id, "action": act,
                    "basis": f"contested:no_winner verdict={verdict}"
                             f" conf={conf}", "reason": reason[:200]})
    acts = Counter(d["action"] for d in decisions)

    # cascade: two bios BOTH judged 'same' against one roster record are
    # very likely one person — those in different bio-persons are
    # under-merge candidates (feeds the same ledger as screen A6)
    bio2p = {r["bio_id"]: r["person_id"] for r in map(
        json.loads, open(ROOT / "bio_persons/bio_person_map.jsonl",
                         encoding="utf-8"))}
    multisame, seen_pairs = [], set()
    for rec_id, votes in by_record.items():
        sames = [v for v in votes if v[1] == "same"]
        for i in range(len(sames)):
            for j in range(i + 1, len(sames)):
                a, b = sorted([sames[i][0], sames[j][0]])
                if (a, b) in seen_pairs:
                    continue
                seen_pairs.add((a, b))
                pa, pb = bio2p.get(a), bio2p.get(b)
                if pa and pb and pa != pb:
                    multisame.append({
                        "person_a": pa, "person_b": pb,
                        "bio_a": a, "bio_b": b, "record_id": rec_id,
                        "basis": "contested_record_both_same",
                    })
    with open(IDD / "b1_multisame_person_candidates.jsonl", "w",
              encoding="utf-8") as fh:
        for d in multisame:
            fh.write(json.dumps(d, ensure_ascii=False) + "\n")

    with open(IDD / "b1_contested_decisions.jsonl", "w",
              encoding="utf-8") as fh:
        for d in decisions:
            fh.write(json.dumps(d, ensure_ascii=False) + "\n")
    (IDD / "b1_measured.json").write_text(json.dumps({
        "corpus_precision_weighted": corpus_precision,
        "by_group": parts,
        "strata": table, "contested_outcomes": dict(outcome),
        "contested_actions": dict(acts),
        "n_multisame_person_candidates": len(multisame),
        "n_sample_judged": len(sample), "n_contested_judged": len(contested),
    }, indent=2), encoding="utf-8")

    lines = [
        "# B1 measured link precision (Nibi job 17492845)",
        "",
        f"Stratified sample: {len(sample):,} judged pairs. Corpus-wide"
        f" stratum-weighted precision: **{corpus_precision:.1%}**"
        if corpus_precision is not None else "no sample results",
        "(unsure verdicts excluded from the denominator).",
        "",
        f"- non-weak links ({parts['nonweak']['links']:,}):"
        f" **{parts['nonweak']['precision']:.1%}**",
        f"- weak links ({parts['weak']['links']:,}):"
        f" **{parts['weak']['precision']:.1%}** — est."
        f" {parts['weak']['links'] * (1 - parts['weak']['precision']):,.0f}"
        " bad links; treat the tier as untrusted (filter from analyses,"
        " re-adjudicate in bulk)."
        if parts.get("weak", {}).get("precision") is not None else "",
        "",
        "| stratum | links | judged | same | diff | unsure | precision"
        " | 95% CI |",
        "|---|---|---|---|---|---|---|---|",
    ]
    for t in table:
        p = f"{t['precision']:.1%}" if t["precision"] is not None else "-"
        lines.append(
            f"| {t['stratum']} | {t['links']:,} | {t['judged']} |"
            f" {t['same']} | {t['different']} | {t['unsure']} | {p} |"
            f" {t['ci95'][0]:.1%}-{t['ci95'][1]:.1%} |")
    lines += [
        "",
        "## Contested records (roster row claimed by >1 bio)",
        "",
        f"{len(by_record):,} records judged: {dict(outcome)}",
        f"Per-link actions: {dict(acts)}",
        "",
        f"Cascade: **{len(multisame):,}** cross-person bio pairs where both"
        " bios were judged 'same' for one record — under-merge candidates"
        " (b1_multisame_person_candidates.jsonl).",
        "",
        "Decisions in b1_contested_decisions.jsonl (keep/drop/review);",
        "apply drops in the next volume_relink cycle.",
    ]
    (IDD / "B1_MEASURED.md").write_text("\n".join(lines) + "\n",
                                        encoding="utf-8")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
