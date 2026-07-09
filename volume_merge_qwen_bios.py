#!/usr/bin/env python3
"""Merge Qwen bio-parsing results into the per-edition bios.jsonl files.

Reads data/volume/qwen_bio_results.jsonl (pulled back from Nibi) and rewrites
each edition's bios.jsonl in place:
  - parsed entries: events/honours/birth_year filled, parser="qwen";
    the rules headword surname/given are KEPT unless they fail a sanity check
    (the headword tier is more reliable than the LLM on names).
  - not_a_bio verdicts: parser="not_a_bio" (excluded from linking naturally —
    they have no events; the tag records the verdict).
Idempotent: derived purely from (current bios.jsonl, results file).

Also writes data/volume/qwen_bio_merge_report.txt.
"""
import json
import re
from collections import Counter
from pathlib import Path

ROOT = Path("data/volume")
RESULTS = ROOT / "qwen_bio_results.jsonl"

SANE_SURNAME = re.compile(r"^[A-Za-z][A-Za-z'’.\- ]{1,39}$")


def main():
    by_id = {}
    for line in open(RESULTS, encoding="utf-8"):
        res = json.loads(line)
        if "error" not in res:
            by_id[res["id"]] = res

    stats = Counter()
    per_year = Counter()
    for d in sorted(ROOT.glob("col[0-9]*")):
        p = d / "bios.jsonl"
        if not p.exists():
            continue
        rows = [json.loads(l) for l in open(p, encoding="utf-8")]
        changed = False
        for b in rows:
            res = by_id.get(b["bio_id"])
            if res is None:
                continue
            if res.get("not_a_bio"):
                if b["parser"] != "not_a_bio":
                    b["parser"] = "not_a_bio"
                    changed = True
                    stats["not_a_bio"] += 1
                continue
            q = res["bio"]
            b["events"] = q["events"]
            b["honours"] = q["honours"]
            if q.get("birth_year") and not b.get("birth_year"):
                b["birth_year"] = q["birth_year"]
            if not SANE_SURNAME.match(b.get("surname") or ""):
                b["surname"] = q["surname"]
                b["given_names"] = q.get("given_names")
                stats["surname_replaced"] += 1
            b["parser"] = "qwen"
            changed = True
            stats["bios_updated"] += 1
            stats["events_added"] += len(q["events"])
            per_year[int(d.name[3:])] += 1
        if changed:
            with p.open("w", encoding="utf-8") as fh:
                for b in rows:
                    fh.write(json.dumps(b, ensure_ascii=False) + "\n")

    lines = ["Qwen bio merge report", "=" * 40]
    lines += [f"{k:20} {v:,}" for k, v in sorted(stats.items())]
    lines.append("\ntop 10 years:")
    lines += [f"  {y}: {v:,}" for y, v in per_year.most_common(10)]
    report = "\n".join(lines)
    (ROOT / "qwen_bio_merge_report.txt").write_text(report + "\n")
    print(report)


if __name__ == "__main__":
    main()
