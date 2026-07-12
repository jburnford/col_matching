#!/usr/bin/env python3
"""Extract the IOL civil lists (establishment rosters) across all annual
editions, 1896-1947 — the first tranche of the wider IOL knowledge graph
(docs/IOL_VS_COL.md §2; the office—holder grammar only).

Writes data/iol/civil/civil_<tag>.jsonl (one file per edition) and a
coverage report data/iol/civil/CIVIL_EXTRACTION.md. Pre-1896 semiannual
volumes (iacsl/il main volumes) use an untested earlier layout and are
skipped; the gradation lists, honours rolls and context lists are separate
layers.

  python3 iol_extract_civil.py [--from-year 1896]
"""

from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path

from col_match.volume import iol_civil, iol_reader

OUT = Path("data/iol/civil")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--from-year", type=int, default=1896)
    args = ap.parse_args()

    OUT.mkdir(parents=True, exist_ok=True)
    editions, _ = iol_reader.available_editions()
    editions = [e for e in editions if e.year >= args.from_year]

    # Qwen residue re-parses (accumulative overlay the build consumes;
    # data/iol/identity/adjudicate/res_civil.jsonl keyed cvl::<raw_key>).
    # A residue line's records are REPLACED by the re-parse's holders;
    # unparseable verdicts keep the rules records, flagged.
    import hashlib
    import re as _re

    def raw_key(line: str) -> str:
        norm = _re.sub(r"\s+", " ", (line or "").strip().lower())
        return hashlib.sha1(norm.encode()).hexdigest()[:16]

    overrides = {}
    res_path = Path("data/iol/identity/adjudicate/res_civil.jsonl")
    if res_path.exists():
        for line in open(res_path, encoding="utf-8"):
            r = json.loads(line)
            if r.get("id", "").startswith("cvl::") and "error" not in r:
                overrides[r["id"][5:]] = r
    ostats = Counter()

    def apply_overrides(recs):
        out = []
        done_lines = set()
        for r in recs:
            k = raw_key(r.raw_line)
            ov = overrides.get(k)
            if ov is None:
                out.append(r)
                continue
            if ov.get("unparseable") or not ov.get("holders"):
                if "llm_unparseable" not in r.flags:
                    r.flags = sorted(set(r.flags + ["llm_unparseable"]))
                ostats["kept_unparseable"] += 1
                out.append(r)
                continue
            if k in done_lines:      # line already replaced once
                ostats["records_dropped"] += 1
                continue
            done_lines.add(k)
            ostats["lines_replaced"] += 1
            for h in ov["holders"]:
                nr = json.loads(json.dumps(r.to_json()))  # deep copy dict
                nr.update({
                    "office": ov.get("office") or r.office,
                    "name": h["name"], "prefix": h.get("prefix"),
                    "honours": h.get("honours") or [],
                    "service": h.get("service"),
                    "flags": ["llm_reparse"]})
                out.append(iol_civil.CivilRecord(**nr))
                ostats["records_emitted"] += 1
        return out

    rows = []
    for ek in editions:
        recs = apply_overrides(iol_civil.extract_civil(ek))
        path = OUT / f"civil_{ek.tag}.jsonl"
        with open(path, "w", encoding="utf-8") as fh:
            for r in recs:
                fh.write(json.dumps(r.to_json(), ensure_ascii=False) + "\n")
        govs = Counter(r.government for r in recs)
        hon = sum(1 for r in recs if r.honours)
        svc = sum(1 for r in recs if r.service)
        act = sum(1 for r in recs if r.acting)
        rows.append({"edition": ek.dirpath.name, "tag": ek.tag,
                     "year": ek.year, "records": len(recs),
                     "governments": len(govs),
                     "pct_honours": round(100 * hon / len(recs), 1) if recs else 0,
                     "pct_service": round(100 * svc / len(recs), 1) if recs else 0,
                     "pct_acting": round(100 * act / len(recs), 1) if recs else 0})
        print(f"{ek.dirpath.name}: {len(recs):5d} records, "
              f"{len(govs):2d} governments")

    if overrides:
        print(f"residue re-parses applied: {dict(ostats)}")
    total = sum(r["records"] for r in rows)
    lines = [
        "# IOL civil-list extraction (office—holder rosters, 1896-1947)",
        "",
        f"{len(rows)} editions, **{total:,} records** "
        f"(col_match/volume/iol_civil.py).",
        "",
        "| edition | records | governments | honours% | service% | acting% |",
        "|---|---|---|---|---|---|",
    ]
    for r in rows:
        lines.append(f"| {r['edition']} | {r['records']:,} "
                     f"| {r['governments']} | {r['pct_honours']} "
                     f"| {r['pct_service']} | {r['pct_acting']} |")
    lines += [
        "",
        "Record schema: government / department / branch / office / name /",
        "honours / service / prefix / acting / flags (tenure dates, suffixes)",
        "/ raw_line / char_offset / page_est.",
        "",
        "Known limits: bare-province sub-groupings inside all-India service",
        "lists can inherit a stale government label; gradation and",
        "commission NAME LISTS are not parsed (separate layer); pre-1896",
        "semiannual volumes skipped.",
    ]
    (OUT / "CIVIL_EXTRACTION.md").write_text("\n".join(lines) + "\n",
                                             encoding="utf-8")
    print(f"\n{total:,} records across {len(rows)} editions -> {OUT}/")


if __name__ == "__main__":
    main()
