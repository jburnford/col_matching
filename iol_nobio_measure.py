#!/usr/bin/env python3
"""Turn the no-bio judged results into measured numbers
(NOBIO_DEDUP_KICKOFF steps 2+3 measurement; iol_merge_measure.py
pattern).

res_abc.jsonl    class-C identity-vs-bio verdicts -> each C identity
                 resolves matched / never_biod / unsure; the census
                 "no-bio" estimate becomes a measured number with a
                 precision statement (A/B are never-bio'd by
                 construction; U reported separately).
res_chain.jsonl  chain-coherence sample -> per-stratum conflation
                 rates with Wilson CIs, frame-weighted via
                 nobio_chain_frame.json (singleton chains cannot
                 conflate and dilute the census-level rate).

Outputs (data/iol/identity/):
  nobio_measured.json
  NOBIO_MEASURED.md
"""

from __future__ import annotations

import argparse
import json
import math
from collections import Counter, defaultdict
from pathlib import Path

IDD = Path("data/iol/identity")
SAME_CONF = 70


def wilson(k: int, n: int, z: float = 1.96) -> tuple[float, float]:
    if n == 0:
        return (0.0, 1.0)
    p = k / n
    d = 1 + z * z / n
    c = (p + z * z / (2 * n)) / d
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
    return (max(0.0, c - h), min(1.0, c + h))


def load_jsonl(path: Path) -> list[dict]:
    if not path.exists():
        return []
    return [json.loads(l) for l in open(path, encoding="utf-8")]


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--adjudicate-dir", default=str(IDD / "adjudicate"))
    args = ap.parse_args()
    adj = Path(args.adjudicate_dir)

    classes = load_jsonl(IDD / "nobio_classes.jsonl")
    out: dict = {}
    lines = ["# No-bio measured numbers", ""]

    # ---------------- A/B/C measurement ---------------------------
    res_abc = [r for r in load_jsonl(adj / "res_abc.jsonl")
               if "error" not in r]
    if res_abc:
        by_ident = defaultdict(list)
        for r in res_abc:
            by_ident[r["career_id"]].append(r)
        res = {}
        for ident, rs in by_ident.items():
            if any(r.get("verdict") == "same"
                   and (r.get("confidence") or 0) >= SAME_CONF
                   for r in rs):
                res[ident] = "matched"
            elif all(r.get("verdict") == "different" for r in rs):
                res[ident] = "never_biod"
            else:
                res[ident] = "unsure"

        tot = Counter()
        by_pop = defaultdict(Counter)
        for c in classes:
            cls = c["cls"]
            key = (cls if cls != "C"
                   else "C_" + res.get(c["id"], "unjudged"))
            tot[key] += 1
            by_pop[c["population"]][key] += 1

        n_c = sum(v for k, v in tot.items() if k.startswith("C_"))
        judged = n_c - tot["C_unjudged"]
        floor = tot["A"] + tot["B"]
        measured = floor + tot["C_never_biod"]
        upper = measured + tot["C_unsure"] + tot["C_unjudged"]
        out["abc"] = {
            "counts": dict(tot), "by_population":
            {p: dict(c) for p, c in by_pop.items()},
            "class_c_judged": judged,
            "never_biod_floor_AB": floor,
            "never_biod_measured": measured,
            "never_biod_upper": upper,
            "matched_missed_links": tot["C_matched"],
        }
        lines += [
            "## A/B/C against the bio table (judged)", "",
            f"- class C resolved: matched {tot['C_matched']:,} "
            f"(missed links), never-bio'd {tot['C_never_biod']:,}, "
            f"unsure {tot['C_unsure']:,}, unjudged "
            f"{tot['C_unjudged']:,} (of {n_c:,})",
            f"- **measured never-bio'd: {measured:,}** "
            f"(floor A+B {floor:,}; upper bound with unsure "
            f"{upper:,}; U {tot['U']:,} reported separately)",
            "",
            "| population | A | B | C matched | C never | C unsure | U |",
            "|---|---|---|---|---|---|---|",
        ]
        for p, c in sorted(by_pop.items()):
            lines.append(
                f"| {p} | {c['A']:,} | {c['B']:,} | "
                f"{c['C_matched']:,} | {c['C_never_biod']:,} | "
                f"{c['C_unsure'] + c['C_unjudged']:,} | {c['U']:,} |")
        lines.append("")
    else:
        lines += ["## A/B/C — res_abc.jsonl not fetched yet", ""]

    # ---------------- chain-coherence measurement -----------------
    res_chain = [r for r in load_jsonl(adj / "res_chain.jsonl")
                 if "error" not in r]
    if res_chain:
        frame = json.load(open(IDD / "nobio_chain_frame.json"))
        by_stratum = defaultdict(Counter)
        for r in res_chain:
            by_stratum[r.get("stratum") or "?"][r["verdict"]] += 1

        weights = frame["weights"]
        w_total = sum(weights.values())
        w_rate = w_lo = w_hi = 0.0
        rows = []
        for st in sorted(by_stratum):
            c = by_stratum[st]
            n = c["confirm"] + c["reject"]     # unsure excluded
            k = c["reject"]
            lo, hi = wilson(k, n)
            rate = k / n if n else 0.0
            w = weights.get(st, 0) / w_total
            w_rate += w * rate
            w_lo += w * lo
            w_hi += w * hi
            rows.append((st, c, n, k, rate, lo, hi))
        # census-level: singletons cannot conflate
        f_n, s_n = frame["frame"], frame["singletons"]
        dilute = f_n / (f_n + s_n)
        out["chain"] = {
            "strata": {st: {"confirm": c["confirm"],
                            "reject": c["reject"],
                            "unsure": c["unsure"],
                            "reject_rate": round(rate, 4),
                            "wilson": [round(lo, 4), round(hi, 4)]}
                       for st, c, n, k, rate, lo, hi in rows},
            "frame_weighted_conflation": round(w_rate, 4),
            "frame_weighted_wilson": [round(w_lo, 4), round(w_hi, 4)],
            "census_level_conflation": round(w_rate * dilute, 4),
            "census_level_wilson": [round(w_lo * dilute, 4),
                                    round(w_hi * dilute, 4)],
            "frame": f_n, "singletons": s_n,
        }
        lines += [
            "## Chain coherence (are the chains one person each?)", "",
            f"- frame-weighted conflation rate "
            f"**{100 * w_rate:.1f}%** "
            f"(Wilson {100 * w_lo:.1f}-{100 * w_hi:.1f}%) over "
            f"{f_n:,} multi-record chains",
            f"- census-level (with {s_n:,} singletons that cannot "
            f"conflate): **{100 * w_rate * dilute:.1f}%** "
            f"({100 * w_lo * dilute:.1f}-{100 * w_hi * dilute:.1f}%)",
            "- (weighted intervals are weight-averaged stratum "
            "Wilsons — a conservative rollup, not an exact CI)",
            "",
            "| stratum | confirm | reject | unsure | reject% | Wilson |",
            "|---|---|---|---|---|---|",
        ]
        for st, c, n, k, rate, lo, hi in rows:
            lines.append(
                f"| {st} | {c['confirm']} | {c['reject']} | "
                f"{c['unsure']} | {100 * rate:.0f}% | "
                f"{100 * lo:.0f}-{100 * hi:.0f}% |")
        lines.append("")
    else:
        lines += ["## Chain coherence — res_chain.jsonl not fetched "
                  "yet", ""]

    json.dump(out, open(IDD / "nobio_measured.json", "w"), indent=1)
    (IDD / "NOBIO_MEASURED.md").write_text("\n".join(lines) + "\n",
                                           encoding="utf-8")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
