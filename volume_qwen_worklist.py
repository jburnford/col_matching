#!/usr/bin/env python3
"""Build the Qwen worklist: roster-region blocks that the rules tier could not
parse (zero records) but that visibly carry personnel content — a salary
marker or repeated initials patterns. Narrative prose is excluded.

Output: data/volume/qwen_worklist.jsonl
  {"id", "year", "colony", "department", "text", "provenance"}
"""
import json, re
from pathlib import Path
from col_match.volume import roster

ROOT = Path("data/volume")
INITIALS_PAIR = re.compile(r"\b[A-Z]\.\s*[A-Z]")
MAX_CHARS = 5000

out_path = ROOT / "qwen_worklist.jsonl"
n_in = n_out = 0
with open(out_path, "w") as out:
    for d in sorted(ROOT.glob("col[0-9]*")):
        year = int(d.name[3:])
        rec_keys = {(r["provenance"]["page"], r["provenance"]["block"])
                    for r in map(json.loads, open(d / "records.jsonl"))}
        for line in open(d / "roster_blocks.jsonl"):
            b = json.loads(line)
            key = (b["provenance"]["page"], b["provenance"]["block"])
            t = b.get("text", "")
            n_in += 1
            if key in rec_keys or len(t) < 60:
                continue
            if not (roster._SALARY.search(t) or len(INITIALS_PAIR.findall(t)) >= 2):
                continue
            n_out += 1
            out.write(json.dumps({
                "id": f"col{year}-p{key[0]}b{key[1]}",
                "year": year,
                "colony": b.get("colony"),
                "department": b.get("department"),
                "text": t[:MAX_CHARS],
                "provenance": b["provenance"],
            }, ensure_ascii=False) + "\n")
print(f"scanned {n_in:,} roster blocks -> worklist {n_out:,} -> {out_path}")
