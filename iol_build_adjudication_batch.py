#!/usr/bin/env python3
"""Assemble the consolidated Nibi adjudication batch: every pending pool
rendered into qwen_classc_worker pair format (docs/IOL_NEXT_SESSION.md
item 1). One H100 job, four worker invocations (one per mode).

Pools -> worklists under data/iol/identity/adjudicate/:

  wl_dedup.jsonl   --mode ioldedup   A6 residue: same-honour duplicate
                                     pairs on the rebuilt table
                                     (under-merge candidates)
  wl_exit.jsonl    --mode iolexit    A7 events-after-death links (each a
                                     death link whose person persists) +
                                     exit-ambiguous events, one row per
                                     candidate (cand_rank recorded)
  wl_roll.jsonl    --mode iolroll    honours-roll date conflicts
                                     (iol_link_rolls.py, name-compatible
                                     rows only)
  wl_birth.jsonl   --mode iolbirth   A2 ambiguous birth repairs
                                     (2+ candidate OCR fixes)

Ids are pool-prefixed (a6:: a7:: exitamb:: roll:: a2::) so all results
can share one file safely; the `pool` field rides through the worker.
Read-only over the person table; applies nothing.
"""

from __future__ import annotations

import json
from collections import Counter
from pathlib import Path

from iol_merge_audit import rec_lines

ROOT = Path("data/iol")
IDY = ROOT / "identity"
OUT = IDY / "adjudicate"


def jload(path):
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            yield json.loads(line)


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    recs = {r["person_id"]: r for r in
            jload(ROOT / "llm_struct_corpus.stage3.deduped.jsonl")}

    def side(pid: str) -> dict:
        r = recs[pid]
        eds = r.get("editions") or []
        return {
            "name": f"{r.get('surname') or '?'}, "
                    f"{r.get('given_names') or '?'}",
            "birth_year": r.get("birth_year"),
            "honours": [f"{h.get('award')}"
                        + (f" ({h['year']})" if h.get("year") else "")
                        for h in (r.get("honours") or [])][:10],
            "editions": [min(eds), max(eds)] if eds else None,
            "lines": rec_lines(r),
        }

    n = Counter()

    # ---- wl_dedup: A6 residue (under-merge pairs) ----------------------
    with open(OUT / "wl_dedup.jsonl", "w", encoding="utf-8") as fh:
        for r in jload(IDY / "a6_honour_duplicates.jsonl"):
            a, b = r["person_a"], r["person_b"]
            fh.write(json.dumps({
                "id": f"a6::{a}::{b}", "pool": "a6",
                "person_a": a, "person_b": b,
                "a": side(a), "b": side(b),
            }, ensure_ascii=False) + "\n")
            n["a6"] += 1

    # ---- wl_exit: A7 + exit-ambiguous ----------------------------------
    # full event rows (place/establishment/day) live in the casualties
    # layer; exit files carry event_id = "<edition_tag>:<line_index>"
    ev_full = {}
    for f in sorted((ROOT / "casualties").glob("casualties_*.jsonl")):
        for i, line in enumerate(open(f, encoding="utf-8")):
            r = json.loads(line)
            ev_full[f"{r['edition_tag']}:{i}"] = r

    def exit_side(ev_id: str, fallback: dict) -> dict:
        ev = ev_full.get(ev_id, fallback)
        return {k: ev.get(k) for k in
                ("event", "name", "day", "month", "year", "place",
                 "establishment")}

    with open(OUT / "wl_exit.jsonl", "w", encoding="utf-8") as fh:
        for r in jload(IDY / "a7_events_after_death.jsonl"):
            fh.write(json.dumps({
                "id": f"a7::{r['event_id']}::{r['person_id']}",
                "pool": "a7", "event_id": r["event_id"],
                "person_id": r["person_id"],
                "exit": exit_side(r["event_id"], r),
                "person": side(r["person_id"]),
            }, ensure_ascii=False) + "\n")
            n["a7"] += 1
        for r in jload(IDY / "exit_ambiguous.jsonl"):
            for rank, c in enumerate(r["candidates"], 1):
                fh.write(json.dumps({
                    "id": f"exitamb::{r['event_id']}::{c['person_id']}",
                    "pool": "exitamb", "event_id": r["event_id"],
                    "person_id": c["person_id"], "cand_rank": rank,
                    "exit": exit_side(r["event_id"], r),
                    "person": side(c["person_id"]),
                }, ensure_ascii=False) + "\n")
                n["exitamb"] += 1

    # ---- wl_roll: honours-roll date conflicts --------------------------
    with open(OUT / "wl_roll.jsonl", "w", encoding="utf-8") as fh:
        for r in jload(IDY / "roll_conflicts.jsonl"):
            fh.write(json.dumps({
                "id": f"roll::{r['person_id']}::{r['grade']}",
                "pool": "roll", "person_id": r["person_id"],
                "roll": {k: r[k] for k in
                         ("grade", "roll_year", "roll_month", "roll_day",
                          "bio_year")} | {"name": r["roll_name"]},
                "person": side(r["person_id"]),
            }, ensure_ascii=False) + "\n")
            n["roll"] += 1

    # ---- wl_birth: A2 ambiguous repairs --------------------------------
    with open(OUT / "wl_birth.jsonl", "w", encoding="utf-8") as fh:
        for r in jload(IDY / "a2_age_invariants.jsonl"):
            cands = r.get("suggested_birth_years") or []
            if len(cands) == 1:
                continue  # unambiguous -> overlay directly, no judge
            if r["person_id"] not in recs:
                n["birth_missing_person"] += 1
                continue
            fh.write(json.dumps({
                "id": f"a2::{r['person_id']}", "pool": "a2",
                "person_id": r["person_id"],
                "person": side(r["person_id"]),
                "current_birth": r["birth_year"],
                "candidates": cands,
                "anomaly": f"entry age {r.get('entry_age')}, last-activity "
                           f"age {r.get('last_age')} "
                           f"({', '.join(r.get('flags') or [])})",
            }, ensure_ascii=False) + "\n")
            n["a2"] += 1

    total = sum(v for k, v in n.items() if not k.endswith("_person"))
    print(f"adjudication batch: {total:,} prompts -> {OUT}/")
    for k in ("a6", "a7", "exitamb", "roll", "a2"):
        print(f"  {k:8s} {n[k]:4d}")
    if n["birth_missing_person"]:
        print(f"  (skipped {n['birth_missing_person']} a2 rows whose "
              "person_id is not in the rebuilt table)")
    print("\nrun (nibi):")
    for wl, mode in (("wl_dedup", "ioldedup"), ("wl_exit", "iolexit"),
                     ("wl_roll", "iolroll"), ("wl_birth", "iolbirth")):
        print(f"  python3 qwen_classc_worker.py --mode {mode} "
              f"--worklist {wl}.jsonl --out {wl.replace('wl_', 'res_')}"
              ".jsonl")


if __name__ == "__main__":
    main()
