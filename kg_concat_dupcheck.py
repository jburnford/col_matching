#!/usr/bin/env python3
"""Flag recovered concatenated persons that may DUPLICATE an existing person.

A recovered person (person_id ending `_s<k>`) split out of a concatenated entry
might already exist elsewhere in the corpus under its own clean entry. This
flags probable duplicates for review — it does NOT auto-merge (0-FP discipline:
merge decisions stay reviewable). Reuses the calibrated name gate from the
stage-2 dedup (`col_match.services.compile._names_compatible`).

  python3 kg_concat_dupcheck.py
  -> data/kg/review/concat_recovered_dupcheck.jsonl
"""
from __future__ import annotations

import json
import re
from collections import defaultdict
from pathlib import Path

from col_match.services.compile import _names_compatible

OUT = Path("data/kg")
_REC = re.compile(r"_s\d+$")


def _skey(surname: str | None) -> str:
    return re.sub(r"[^A-Z]", "", (surname or "").upper())


def _years(struct: dict) -> set[int]:
    return {e["year_start"] for e in (struct.get("events") or []) if e.get("year_start")}


def main() -> None:
    structs = {}
    for l in (OUT / "llm_struct_corpus.jsonl").open(encoding="utf-8"):
        o = json.loads(l)
        if "_error" not in o:
            structs[o["person_id"]] = o

    recovered = {p: s for p, s in structs.items() if _REC.search(p)}
    existing = {p: s for p, s in structs.items() if not _REC.search(p)}
    blocks = defaultdict(list)
    for p, s in existing.items():
        blocks[_skey(s.get("surname"))].append(p)

    flags = []
    for rp, rs in recovered.items():
        ry = _years(rs)
        for ep in blocks.get(_skey(rs.get("surname")), []):
            es = existing[ep]
            if not _names_compatible(rs.get("given_names"), es.get("given_names")):
                continue
            birth_ok = (rs.get("birth_year") and es.get("birth_year")
                        and abs(rs["birth_year"] - es["birth_year"]) <= 1)
            overlap = len(ry & _years(es))
            if birth_ok or overlap >= 2:
                flags.append({
                    "recovered_id": rp, "existing_id": ep,
                    "surname": rs.get("surname"),
                    "recovered_given": rs.get("given_names"), "existing_given": es.get("given_names"),
                    "recovered_birth": rs.get("birth_year"), "existing_birth": es.get("birth_year"),
                    "year_overlap": overlap,
                    "signal": "birth±1" if birth_ok else f"career-overlap×{overlap}",
                })

    out = OUT / "review" / "concat_recovered_dupcheck.jsonl"
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w", encoding="utf-8") as fh:
        for f in flags:
            fh.write(json.dumps(f, ensure_ascii=False) + "\n")
    print(f"recovered={len(recovered)}  probable-duplicate flags={len(flags)} "
          f"(on {len({f['recovered_id'] for f in flags})} recovered persons) -> {out}")


if __name__ == "__main__":
    main()
