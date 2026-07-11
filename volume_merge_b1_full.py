#!/usr/bin/env python3
"""Unify ALL B1 adjudication runs into one per-link verdict table.

Sources (data/volume/identity/): b1_audit_results (sample, b1::),
b1_contested_results (b1c::), b1_weak_results (b1w::), b1_full_results
(b1f::, Nibi 17496020). After the full run every one of the 79,748
within-volume links carries an individual verdict.

Links judged by more than one run: agreeing verdicts collapse; a
disagreement demotes the link to 'review' (measured cross-run agreement
was 98.6%).

Outputs:
  b1_link_verdicts.jsonl   one row per link: features + verdict +
                           confidence + source runs (the master ledger —
                           keep = verdict 'same', drop = 'different',
                           review = 'unsure'/conflict/unjudged)
  B1_VERDICTS.md           corpus totals, per-strength and per-stratum
                           keep rates, verdict-vs-sample consistency
"""

from __future__ import annotations

import json
from collections import Counter, defaultdict
from pathlib import Path

IDD = Path("data/volume/identity")

RUNS = [("sample", "b1_audit_results.jsonl"),
        ("contested", "b1_contested_results.jsonl"),
        ("weak", "b1_weak_results.jsonl"),
        ("full", "b1_full_results.jsonl")]


def main() -> None:
    votes: dict[str, list] = defaultdict(list)
    for run, name in RUNS:
        path = IDD / name
        if not path.exists():
            print(f"note: {name} missing, skipped")
            continue
        for r in map(json.loads, open(path, encoding="utf-8")):
            if "error" in r:
                continue
            votes[r["id"].split("::", 1)[1]].append(
                (run, r["verdict"], r.get("confidence"),
                 (r.get("reason") or "")[:200]))

    out, action_n = [], Counter()
    by_strength = defaultdict(Counter)
    by_stratum = defaultdict(Counter)
    conflicts = 0
    for f in map(json.loads, open(IDD / "b1_link_scores.jsonl",
                                  encoding="utf-8")):
        vs = votes.get(f["link_id"], [])
        verdicts = {v for _, v, _, _ in vs if v in ("same", "different")}
        if not vs:
            verdict, action = None, "review"
        elif len(verdicts) == 2:
            verdict, action = "conflict", "review"
            conflicts += 1
        elif verdicts == {"same"}:
            verdict, action = "same", "keep"
        elif verdicts == {"different"}:
            verdict, action = "different", "drop"
        else:
            verdict, action = "unsure", "review"
        confs = [c for _, v, c, _ in vs
                 if isinstance(c, (int, float)) and v == verdict]
        rec_id, bio_id = f["link_id"].split("::")
        out.append({
            "link_id": f["link_id"], "record_id": rec_id, "bio_id": bio_id,
            "edition_year": f["edition_year"], "strength": f["strength"],
            "stratum": f["stratum"], "score": f["score"],
            "verdict": verdict, "action": action,
            "confidence": max(confs) if confs else None,
            "runs": [r for r, _, _, _ in vs],
            "reason": next((rs for _, v, _, rs in vs if v == verdict and rs),
                           ""),
        })
        action_n[action] += 1
        by_strength[f["strength"]][action] += 1
        by_stratum[f["stratum"]][action] += 1

    with open(IDD / "b1_link_verdicts.jsonl", "w", encoding="utf-8") as fh:
        for r in out:
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")

    n = len(out)
    judged = n - sum(1 for r in out if r["verdict"] is None)
    lines = [
        "# B1 unified link verdicts",
        "",
        f"{n:,} links; {judged:,} judged ({judged / n:.1%});"
        f" {conflicts} cross-run conflicts (demoted to review).",
        "",
        f"Actions: keep {action_n['keep']:,}"
        f" ({action_n['keep'] / n:.1%}), drop {action_n['drop']:,}"
        f" ({action_n['drop'] / n:.1%}), review {action_n['review']:,}.",
        "",
        "| strength | links | keep | drop | review | keep rate |",
        "|---|---|---|---|---|---|",
    ]
    for st in sorted(by_strength):
        v = by_strength[st]
        tot = sum(v.values())
        dec = v["keep"] + v["drop"]
        rate = f"{v['keep'] / dec:.1%}" if dec else "-"
        lines.append(f"| {st} | {tot:,} | {v['keep']:,} | {v['drop']:,} |"
                     f" {v['review']:,} | {rate} |")
    lines += [
        "",
        "| stratum | links | keep rate | sample precision |",
        "|---|---|---|---|",
    ]
    measured = {}
    mfile = IDD / "b1_measured.json"
    if mfile.exists():
        for t in json.loads(mfile.read_text()).get("strata", []):
            measured[t["stratum"]] = t.get("precision")
    for st in sorted(by_stratum):
        v = by_stratum[st]
        dec = v["keep"] + v["drop"]
        rate = f"{v['keep'] / dec:.1%}" if dec else "-"
        mp = measured.get(st)
        lines.append(f"| {st} | {sum(v.values()):,} | {rate} |"
                     f" {mp:.1%} |" if mp is not None else
                     f"| {st} | {sum(v.values()):,} | {rate} | - |")
    lines += [
        "",
        "Master ledger: b1_link_verdicts.jsonl — apply keep/drop in the"
        " next volume_relink cycle; supersedes the partial weak/contested"
        " ledgers.",
    ]
    (IDD / "B1_VERDICTS.md").write_text("\n".join(lines) + "\n",
                                        encoding="utf-8")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
