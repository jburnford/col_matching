#!/usr/bin/env python3
"""Post-emit career-event YEAR fixups — the OCR/source-copied year errors that
the spine cannot self-correct (the List copies bios forward, so a wrong year
rides across editions and majority-vote fails; the correct year is often the
minority, printed only by the earliest mentioning edition).

Surfaced by audit_career_years.py (earliest-mention-wins, zero-FP gates) and
curated in data/kg/career_year_fixups.json. Mirrors kg_apply_colony_fixups.py:
every emit recomputes years from the spine, so these corrections would silently
revert on each re-emit. reemit_dedup.sh runs this as its final step (after the
colony fixups); it is idempotent and safe to run repeatedly.

Each rule matches one event by (person_id, seq) AND a match_year_start guard: if
a re-emit shifts seq alignment or changes the spine year, the rule no-ops rather
than mis-targeting. Applied to every layer carrying an event year keyed by
person_id+seq: career_events, career_facts, employment_edges, role_edges.
"""
from __future__ import annotations
import json, collections
from pathlib import Path

ROOT = Path(__file__).resolve().parent
FIXUPS = json.loads((ROOT / "data/kg/career_year_fixups.json").read_text())["corrections"]
# key: (person_id, seq) -> (match_year_start, new_year_start)
BY_KEY = {(c["person_id"], c["seq"]): (c["match_year_start"], c["year_start"])
          for c in FIXUPS}

LAYERS = ("career_events", "career_facts", "employment_edges", "role_edges")


def fix(r):
    """Mutate one row's year_start if it matches a guarded fixup; return True if changed."""
    rule = BY_KEY.get((r.get("person_id"), r.get("seq")))
    if rule is None:
        return False
    match_ys, new_ys = rule
    if r.get("year_start") != match_ys:      # guard: only touch the known-wrong year
        return False
    if r["year_start"] == new_ys:            # already applied
        return False
    r["year_start"] = new_ys
    return True


def main():
    tot = collections.Counter()
    for corpus in ("data/kg", "data/iol"):
        for name in LAYERS:
            p = ROOT / corpus / "graph_stage3" / f"{name}.jsonl"
            if not p.exists():
                continue
            out, n = [], 0
            for line in p.open():
                r = json.loads(line)
                if fix(r):
                    n += 1
                out.append(json.dumps(r, ensure_ascii=False))
            if n:
                p.write_text("\n".join(out) + "\n")
            tot[f"{corpus}/{name}"] = n
    for k, n in tot.items():
        if n:
            print(f"  year fixups {k}: {n}")
    if not any(tot.values()):
        print("  year fixups: nothing to do (already applied, or spine already correct)")


if __name__ == "__main__":
    main()
