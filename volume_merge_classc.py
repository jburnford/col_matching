#!/usr/bin/env python3
"""Merge the Qwen class-C adjudication verdicts back into the never-bio'd
classing — turns the class-C ambiguity UPPER bound into a measured rate.

Inputs:
  data/volume/classc/career_classes.jsonl   from volume_classc_worklist.py
  data/volume/classc/classc_results.jsonl   scp'd back from Nibi
                                            (nibi/qwen_classc_worker.py)

A class-C career resolves by its pairs' verdicts:
  matched      any candidate judged "same"      -> plausibly bio'd after all
  never_biod   every candidate judged "different"
  unsure       otherwise (an "unsure" verdict, or the pair errored/missing)

Outputs (data/volume/classc/):
  career_classes_measured.jsonl  career_classes rows + resolution/evidence
  classc_link_candidates.jsonl   the "same" pairs (strongest first) — these
                                 are candidate roster->bio links, REVIEW
                                 before feeding the linker (0-FP discipline)
  CLASSC_MEASURED.md             never-bio'd rates: floor (A+B alone) vs
                                 measured (+C_different), per colony x rank

Usage: python3 volume_merge_classc.py
"""

from __future__ import annotations

import json
from collections import Counter, defaultdict
from pathlib import Path

CLASSDIR = Path("data/volume/classc")
SAME_CONF = 70          # "same" below this confidence counts as unsure


def main() -> None:
    verdicts: dict[str, list[dict]] = defaultdict(list)
    n_res = n_err = 0
    for line in (CLASSDIR / "classc_results.jsonl").open(encoding="utf-8"):
        r = json.loads(line)
        n_res += 1
        if "error" in r:
            n_err += 1
            continue
        verdicts[r["career_id"]].append(r)

    expected: dict[str, int] = Counter()
    for line in (CLASSDIR / "classc_worklist.jsonl").open(encoding="utf-8"):
        expected[json.loads(line)["career_id"]] += 1

    rows = [json.loads(l)
            for l in (CLASSDIR / "career_classes.jsonl").open(encoding="utf-8")]

    link_cands: list[dict] = []
    res_count: Counter[str] = Counter()
    for row in rows:
        if row["cls"] != "C":
            row["resolution"] = None
            continue
        vs = verdicts.get(row["career_id"], [])
        same = [v for v in vs if v["verdict"] == "same"
                and (v.get("confidence") or 0) >= SAME_CONF]
        weak_same = [v for v in vs if v["verdict"] == "same"
                     and (v.get("confidence") or 0) < SAME_CONF]
        diff = [v for v in vs if v["verdict"] == "different"]
        complete = len(vs) == expected.get(row["career_id"], 0)
        if same:
            row["resolution"] = "matched"
            link_cands.extend(same)
        elif complete and len(diff) == len(vs) and vs:
            row["resolution"] = "never_biod"
        else:
            row["resolution"] = "unsure"   # unsure/weak-same/error/missing
        row["n_pairs"] = expected.get(row["career_id"], 0)
        row["n_same"] = len(same)
        row["n_weak_same"] = len(weak_same)
        row["n_different"] = len(diff)
        res_count[row["resolution"]] += 1

    with (CLASSDIR / "career_classes_measured.jsonl").open("w", encoding="utf-8") as fh:
        for row in rows:
            fh.write(json.dumps(row, ensure_ascii=False) + "\n")
    link_cands.sort(key=lambda v: -(v.get("confidence") or 0))
    with (CLASSDIR / "classc_link_candidates.jsonl").open("w", encoding="utf-8") as fh:
        for v in link_cands:
            fh.write(json.dumps(v, ensure_ascii=False) + "\n")

    # ------------------------------------------------------------- report
    def rates(rows_):
        n = len(rows_)
        c = Counter(r["cls"] for r in rows_)
        res = Counter(r.get("resolution") for r in rows_ if r["cls"] == "C")
        floor = c["A"] + c["B"]
        measured = floor + res["never_biod"]
        upper = floor + c["C"]              # every C never-bio'd
        return (f"| {n:,} | {100*floor/max(n,1):.0f}% "
                f"| {100*measured/max(n,1):.0f}% | {100*upper/max(n,1):.0f}% "
                f"| {res['matched']:,} | {res['unsure']:,} |")

    lines = [
        "# Measured never-bio'd rates (class-C adjudication merged)",
        "",
        f"- verdicts: {n_res:,} pairs ({n_err:,} errors); class-C careers "
        f"resolved: " + ", ".join(f"{k}: {v:,}" for k, v in res_count.most_common()),
        f"- link candidates (verdict=same, confidence>={SAME_CONF}): "
        f"{len(link_cands):,} -> classc_link_candidates.jsonl (review before use)",
        "",
        "floor = A+B only; measured = A+B+C-adjudicated-different; upper = A+B+C.",
        "The paper's safe claim lies between floor and measured; 'unsure' stays",
        "ambiguous by design.",
        "",
        "## By salary rank (all colonies, unlinked careers)",
        "",
        "| rank | careers | floor | measured | upper | C matched | C unsure |",
        "|---|---|---|---|---|---|---|",
    ]
    for rk in ("subordinate", "clerical", "officer", "senior", "unsalaried"):
        sub = [r for r in rows if r["rank"] == rk]
        lines.append(f"| {rk} " + rates(sub))
    lines += ["", "## Gold Coast / Kenya", "",
              "| colony · rank | careers | floor | measured | upper | C matched | C unsure |",
              "|---|---|---|---|---|---|---|"]
    for col in ("GOLD COAST", "KENYA"):
        for rk in ("subordinate", "clerical", "officer", "senior", "unsalaried"):
            sub = [r for r in rows if r["colony"] == col and r["rank"] == rk]
            if sub:
                lines.append(f"| {col.title()} · {rk} " + rates(sub))
    (CLASSDIR / "CLASSC_MEASURED.md").write_text("\n".join(lines) + "\n",
                                                 encoding="utf-8")
    print(f"merged {n_res:,} verdicts ({n_err:,} errors); resolutions:",
          dict(res_count))
    print(f"-> {CLASSDIR}/CLASSC_MEASURED.md")


if __name__ == "__main__":
    main()
