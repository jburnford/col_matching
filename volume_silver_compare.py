#!/usr/bin/env python3
"""Score the COL never-bio'd pipeline against the hand-labeled silver
standard (data/volume/classc/nobio_silver.jsonl: 200 close-read items
across four pools, labeled 2026-07-12; ids join the shipped outputs).

Mirrors iol_nobio_silver_compare.py. Unlike the IOL round, the judge
verdicts already exist (classc_results.jsonl), so every agreement rate
prints NOW — no GPU dependency.

Measurements:
  1. applied-link precision — silver labels on career_person_links.jsonl
     pairs, by policy tier x corroboration class (tests the 0-FP claim
     at ~10x the original 34-pair basis);
  2. judged-negative reliability — silver labels on classc 'different'
     pairs from measured never-bio'd careers (a wrong 'different' hides
     a real link and inflates the never-bio'd count);
  3. chain coherence — is a within-volume career one person
     (confirm/reject/junk);
  4. A/B spot-checks — does a compatible bio person truly not exist
     (confirm/reject/junk).
Silver 'unsure' rows leave every denominator.

Output: printed report + data/volume/classc/NOBIO_SILVER.md +
disagreement list for hand re-adjudication.
"""

from __future__ import annotations

import json
from collections import Counter, defaultdict
from pathlib import Path

CLS = Path("data/volume/classc")


def load_jsonl(path: Path) -> list[dict]:
    if not path.exists():
        return []
    return [json.loads(l) for l in open(path, encoding="utf-8")]


def wilson(k: int, n: int, z: float = 1.96) -> tuple[float, float]:
    if not n:
        return (0.0, 1.0)
    p = k / n
    d = 1 + z * z / n
    c = p + z * z / (2 * n)
    h = z * ((p * (1 - p) + z * z / (4 * n)) / n) ** 0.5
    return ((c - h) / d, (c + h) / d)


def pct(k: int, n: int) -> str:
    if not n:
        return "—"
    lo, hi = wilson(k, n)
    return f"{k}/{n} = {100*k/n:.0f}% (CI {100*lo:.0f}–{100*hi:.0f}%)"


def main() -> None:
    silver = load_jsonl(CLS / "nobio_silver.jsonl")
    links = {r["id"]: r for r in load_jsonl(CLS / "career_person_links.jsonl")}
    results = {r["id"]: r for r in load_jsonl(CLS / "classc_results.jsonl")}

    n_unsure = sum(1 for s in silver if s["silver_verdict"] == "unsure")
    lines = ["# COL silver-standard scores", "",
             f"{len(silver)} hand-labeled items across 4 pools "
             f"({n_unsure} unsure, excluded from denominators). "
             "Labeled 2026-07-12 by close reading with full context "
             "(career records + person events; bio_persons searched by "
             "surname variant for the A/B pool).", ""]
    disagreements: list[str] = []

    # ---------------- 1. applied-link precision ---------------------------
    lines += ["## 1. Applied-link precision (career_person_links.jsonl)", ""]
    per = defaultdict(Counter)
    for s in silver:
        if s["pool"] != "applied" or s["silver_verdict"] == "unsure":
            continue
        lk = links.get(s["id"])
        if not lk:
            continue
        keys = ("all", f"policy:{lk['policy']}", f"det:{lk['det_tier']}")
        for k in keys:
            per[k][s["silver_verdict"]] += 1
        if s["silver_verdict"] != "same":
            disagreements.append(
                f"- APPLIED-LINK FP [{lk['policy']}|{lk['det_tier']}] "
                f"{s['id']}: {s['evidence']}")
    lines.append("| stratum | correct (silver=same) |")
    lines.append("|---|---|")
    for k in sorted(per, key=lambda k: (k != "all", k)):
        c = per[k]
        n = c["same"] + c["different"]
        lines.append(f"| {k} | {pct(c['same'], n)} |")
    lines.append("")

    # ---------------- 2. judged negatives ---------------------------------
    lines += ["## 2. Judged-'different' reliability (measured never-bio'd "
              "negatives)", ""]
    per = defaultdict(Counter)
    for s in silver:
        if s["pool"] != "judged_diff" or s["silver_verdict"] == "unsure":
            continue
        risk = s.get("strata", "").split("|")[0] or "?"
        for k in ("all", risk):
            per[k][s["silver_verdict"]] += 1
        if s["silver_verdict"] == "same":
            disagreements.append(
                f"- MISSED LINK [{risk}] {s['id']}: {s['evidence']}")
    lines.append("| stratum | judge 'different' correct |")
    lines.append("|---|---|")
    for k in sorted(per, key=lambda k: (k != "all", k)):
        c = per[k]
        n = c["same"] + c["different"]
        lines.append(f"| {k} | {pct(c['different'], n)} |")
    lines += ["", "A silver 'same' here is a FALSE NEGATIVE: a real link "
              "judged away, i.e. a career counted never-bio'd that has a "
              "bio person. The hirisk stratum oversamples rare surnames "
              "with era-overlapping candidates by design.", ""]

    # ---------------- 3. chain coherence ----------------------------------
    lines += ["## 3. Career-chain coherence (careers.jsonl, never-bio'd "
              "multi-record chains)", ""]
    per = defaultdict(Counter)
    for s in silver:
        if s["pool"] != "chain" or s["silver_verdict"] == "unsure":
            continue
        risk = "hirisk" if s.get("strata", "").startswith("hirisk") else "general"
        for k in ("all", risk):
            per[k][s["silver_verdict"]] += 1
        if s["silver_verdict"] in ("reject", "junk"):
            disagreements.append(
                f"- CHAIN {s['silver_verdict'].upper()} [{risk}] "
                f"{s['id']}: {s['evidence']}")
    lines.append("| stratum | confirm | reject (conflation) | junk (non-person) |")
    lines.append("|---|---|---|---|")
    for k in sorted(per, key=lambda k: (k != "all", k)):
        c = per[k]
        n = sum(c.values())
        lines.append(f"| {k} | {pct(c['confirm'], n)} | {c['reject']} "
                     f"| {c['junk']} |")
    lines.append("")

    # ---------------- 4. A/B spot-checks ----------------------------------
    lines += ["## 4. Class A/B spot-checks (career_classes_measured.jsonl)", ""]
    per = defaultdict(Counter)
    for s in silver:
        if s["pool"] != "ab_check" or s["silver_verdict"] == "unsure":
            continue
        cls = s.get("strata", "?").split("|")[0]
        for k in ("all", f"class {cls}"):
            per[k][s["silver_verdict"]] += 1
        if s["silver_verdict"] == "reject":
            disagreements.append(
                f"- FALSE A/B [{cls}] {s['id']}: {s['evidence']}")
    lines.append("| stratum | confirmed never-bio'd | reject (bio exists) "
                 "| junk (non-person) |")
    lines.append("|---|---|---|---|")
    for k in sorted(per, key=lambda k: (k != "all", k)):
        c = per[k]
        n = sum(c.values())
        lines.append(f"| {k} | {pct(c['confirm'], n)} | {c['reject']} "
                     f"| {c['junk']} |")
    lines.append("")

    # ---------------- judge agreement on every scoreable pair -------------
    lines += ["## Judge agreement (classc_results vs silver, pair pools)", ""]
    agree = Counter()
    for s in silver:
        if s["pool"] not in ("applied", "judged_diff"):
            continue
        if s["silver_verdict"] not in ("same", "different"):
            continue
        r = results.get(s["id"])
        if not r or r["verdict"] not in ("same", "different"):
            continue
        agree["n"] += 1
        if r["verdict"] == s["silver_verdict"]:
            agree["ok"] += 1
    lines += [f"- judged pairs scoreable: {agree['n']}; agreement "
              f"{pct(agree['ok'], agree['n'])}",
              "- (applied pool selects on judge 'same', negatives pool on "
              "judge 'different'; the blended rate is composition-dependent "
              "— read the per-pool sections above.)", ""]

    # ---------------- junk-name / defect classes --------------------------
    junk = [s for s in silver if s["silver_verdict"] == "junk"]
    lines += ["## Junk-name exemplars recorded as labels", ""]
    for s in junk:
        lines.append(f"- `{s['id']}`: {s['evidence']}")
    lines.append("")

    # ---------------- disagreement list -----------------------------------
    lines += ["## Disagreement / action list (hand re-adjudication queue)", ""]
    lines += disagreements or ["- none"]
    lines.append("")

    out = CLS / "NOBIO_SILVER.md"
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines))
    print(f"-> {out}")


if __name__ == "__main__":
    main()
