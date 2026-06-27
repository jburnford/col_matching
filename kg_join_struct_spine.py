#!/usr/bin/env python3
"""Join validated structured records with the deduped person spine.

The structuring/validate output carries the LLM career fields (events, honours,
education) keyed by person_id; the dedup spine (persons.deduped*.jsonl) carries
the cross-edition provenance (editions, attestation bio_ids, n_attestations).
``kg_emit_stage3.py`` needs both on one record. The CO List produced this via the
stage-3 dedup *apply* step; for the IOL v1 graph we skip the heavier stage-3
re-dedup (stage-1 text-chaining already collapsed 258k bios -> ~30k) and just
join, emitting the emit-input corpus ``llm_struct_corpus.stage3.jsonl``.

  COL_KG_OUT=data/iol python3 kg_join_struct_spine.py
"""
from __future__ import annotations

import json
from pathlib import Path

from col_match.kg.paths import kg_out


def main() -> None:
    out = kg_out()
    spine = {p["person_id"]: p
             for p in (json.loads(l) for l in (out / "persons.deduped.jsonl").open(encoding="utf-8"))}
    valid = out / "llm_struct_corpus.valid.jsonl"
    dest = out / "llm_struct_corpus.stage3.jsonl"

    n = miss = 0
    with dest.open("w", encoding="utf-8") as fh:
        for l in valid.open(encoding="utf-8"):
            o = json.loads(l)
            if "_error" in o:
                continue
            sp = spine.get(o["person_id"])
            if not sp:
                miss += 1
                continue
            rec = {
                "person_id": o["person_id"],
                "surname": o.get("surname") or sp.get("surname"),
                "given_names": o.get("given_names") or sp.get("given_names"),
                "birth_year": o.get("birth_year") if o.get("birth_year") is not None else sp.get("birth_year"),
                "editions": sp.get("editions", []),
                "n_attestations": sp.get("n_attestations"),
                "attestations": sp.get("attestation_bio_ids", []),
                "events": o.get("events", []),
                "honours": o.get("honours", []),
                "education": o.get("education"),
                "terminal": o.get("terminal"),
                "flags": o.get("flags", []),
            }
            fh.write(json.dumps(rec, ensure_ascii=False) + "\n")
            n += 1
    print(f"joined {n} persons -> {dest}  ({miss} structs had no spine match)")


if __name__ == "__main__":
    main()
