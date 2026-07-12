#!/usr/bin/env python3
"""Build the civil-list residue worklist: records whose parsed name/office
fails deterministic shape checks get their raw_line queued for a Qwen
re-parse (docs/IOL_NEXT_SESSION.md item 3; runs in the consolidated Nibi
batch via nibi/qwen_civil_parse_worker.py).

Residue classes (measured by this script; ~3.5% of 119,527 records):
  name_short / name_punct   fragment or mis-split holder names
  office_overlong / _prose  office field swallowed prose
  office_ditto / ditto_unres  multi-ditto lines the deterministic
                              resolver (iol_civil._resolve_ditto) declines

One prompt per UNIQUE raw line (cumulative editions reprint the same
line), so ~4.2k records collapse to far fewer prompts; results map back
to every record sharing the line via raw_key.

Outputs data/iol/civil/residue_records.jsonl (flagged records + raw_key)
and data/iol/identity/adjudicate/wl_civil.jsonl (the worker input).
"""

from __future__ import annotations

import hashlib
import json
import re
from collections import Counter, defaultdict
from glob import glob
from pathlib import Path

CIVIL = Path("data/iol/civil")
OUT = Path("data/iol/identity/adjudicate")

PROSE = re.compile(r"\b(is|was|are|were|which|whom|whose|has|have|had"
                   r"|shall|will|the office|vide|see page)\b", re.I)
DITTO = re.compile(r"\b(ditto|do)\b\.?", re.I)


def raw_key(line: str) -> str:
    norm = re.sub(r"\s+", " ", (line or "").strip().lower())
    return hashlib.sha1(norm.encode()).hexdigest()[:16]


def problems(r: dict) -> list[str]:
    nm, off = r.get("name") or "", r.get("office") or ""
    p = []
    if len(nm) < 4:
        p.append("name_short")
    if re.search(r"[;—]", nm):
        p.append("name_punct")
    if nm.rstrip().endswith((",", " and", " of", " the")):
        p.append("name_dangling")
    if PROSE.search(nm):
        p.append("name_prose")
    if len(off) > 90:
        p.append("office_overlong")
    if PROSE.search(off):
        p.append("office_prose")
    if DITTO.search(off):
        p.append("office_ditto")
    if "ditto_unresolved" in (r.get("flags") or []):
        p.append("ditto_unresolved")
    return p


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    flagged = []
    by_key: dict[str, dict] = {}
    key_records: Counter = Counter()
    stats = Counter()
    for f in sorted(glob(str(CIVIL / "civil_*.jsonl"))):
        for line in open(f, encoding="utf-8"):
            r = json.loads(line)
            stats["records"] += 1
            p = problems(r)
            if not p:
                continue
            k = raw_key(r.get("raw_line"))
            flagged.append({"edition_tag": r["edition_tag"],
                            "char_offset": r["char_offset"],
                            "government": r.get("government"),
                            "department": r.get("department"),
                            "office": r.get("office"),
                            "name": r.get("name"),
                            "problems": p, "raw_key": k,
                            "raw_line": r.get("raw_line")})
            key_records[k] += 1
            for x in p:
                stats[x] += 1
            if k not in by_key:
                by_key[k] = {"id": f"cvl::{k}",
                             "raw_line": r.get("raw_line"),
                             "government": r.get("government"),
                             "department": r.get("department"),
                             "problems": p}
    for k, row in by_key.items():
        row["n_records"] = key_records[k]

    with open(CIVIL / "residue_records.jsonl", "w", encoding="utf-8") as fh:
        for r in flagged:
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")
    with open(OUT / "wl_civil.jsonl", "w", encoding="utf-8") as fh:
        for row in by_key.values():
            fh.write(json.dumps(row, ensure_ascii=False) + "\n")

    print(f"{stats['records']:,} civil records; {len(flagged):,} flagged "
          f"({len(flagged) / stats['records']:.1%}) -> "
          f"{len(by_key):,} unique raw lines")
    for k in ("name_short", "name_punct", "name_dangling", "name_prose",
              "office_overlong", "office_prose", "office_ditto",
              "ditto_unresolved"):
        print(f"  {k:18s} {stats[k]:5d}")
    print(f"\n-> {CIVIL / 'residue_records.jsonl'}"
          f"\n-> {OUT / 'wl_civil.jsonl'} (qwen_civil_parse_worker.py)")


if __name__ == "__main__":
    main()
