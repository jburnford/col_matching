#!/usr/bin/env python3
"""Measure the BRACKETING place-interpolation lever.

A place-less dated bio event that falls chronologically BETWEEN two placed
events resolving to the SAME colony almost certainly belongs to that colony
(a continuous career listing). The parser/inheritance loses this because the
compiled bio concatenates events from several editions, so within-entry place
inheritance doesn't span the gaps. Attaching the bracketing colony lets the
intervening tenure overlap a stint it currently misses (RUSHTON: WA 1896 +
WA 1919 bracket place-less 1901 railway-secretary clauses -> overlaps the
WA 1905-1917 stint that the raw OCR confirms is him).

Sizing, staged (read-only):
  (1) bracketed place-less events (same colony both sides) on any bio;
  (2) on a currently-UNMATCHED bio;
  (3) AND a same-(surname, bracket-colony, event-year+-2) initial-compatible
      record exists -> attaching the colony could unlock a match.

Usage: COL_USE_AUGMENTED=1 python3 measure_bracket.py
"""
import json
import os
from collections import defaultdict
from pathlib import Path

from col_match.services import gazetteer
from col_match.services.compile import _names_compatible
from col_match.services.match import _norm, _surname_of_official
from col_match.services.infer_colony import apply_recovered_places
from col_match.services.schema import Biography

DD = Path("data/services")


def bracket_colony(events, i, data_dir):
    """If place-less event i is bracketed (by year) by a prior and a later
    placed event whose colonies share a target, return that shared colony
    (normalized), else None."""
    ev = events[i]
    if ev.place or ev.year_start is None:
        return None
    prior = [e for e in events
             if e.place and e.year_start is not None and e.year_start <= ev.year_start]
    later = [e for e in events
             if e.place and e.year_start is not None and e.year_start >= ev.year_start]
    if not prior or not later:
        return None
    for a in prior:
        ta = gazetteer.colony_targets(a.place, data_dir)
        for b in later:
            tb = gazetteer.colony_targets(b.place, data_dir)
            shared = ta & tb
            if shared:
                return sorted(shared)[0]
    return None


def main():
    bios = [Biography.model_validate_json(l)
            for l in (DD / "biographies" / "biographies.jsonl").open(encoding="utf-8")]
    apply_recovered_places(bios, str(DD))
    matched = set()
    for fn in ("record_attachments", "stint_matches"):
        for l in (DD / "matches" / f"{fn}.jsonl").open(encoding="utf-8"):
            if l.strip():
                matched.add(json.loads(l)["bio_id"])

    aug = DD / "graph_cache" / "officials_augmented.jsonl"
    op = aug if (os.environ.get("COL_USE_AUGMENTED") == "1" and aug.exists()) else DD / "graph_cache" / "officials.jsonl"
    officials = [json.loads(l) for l in op.open(encoding="utf-8")]
    by_sur_col = defaultdict(list)
    for o in officials:
        sur = _surname_of_official(o["name"])
        col = gazetteer.norm(o["colony"] or "")
        given = o["name"].split(",", 1)[1].strip() if "," in (o["name"] or "") else None
        by_sur_col[(sur, col)].append((o["first_year"], o["last_year"], given))

    n_brk = n_unm = n_rec = 0
    brk_bios, unm_bios, rec_bios = set(), set(), set()
    examples = []

    for b in bios:
        sur = _norm(b.surname)
        for i, ev in enumerate(b.events):
            col = bracket_colony(b.events, i, str(DD))
            if not col:
                continue
            n_brk += 1
            brk_bios.add(b.bio_id)
            if b.bio_id in matched:
                continue
            n_unm += 1
            unm_bios.add(b.bio_id)
            # does a record exist at (surname, col, year+-2) that the new tenure
            # would overlap?
            hit = False
            for cand_col in (col,):
                for fy, ly, given in by_sur_col.get((sur, gazetteer.norm(cand_col)), []):
                    if fy is None or ly is None:
                        continue
                    if ev.year_start - 2 <= ly and fy <= ev.year_start + 2 \
                            and _names_compatible(b.given_names, given):
                        hit = True
                        break
                if hit:
                    break
            if hit:
                n_rec += 1
                rec_bios.add(b.bio_id)
                if len(examples) < 25:
                    examples.append((b.surname, b.given_names, ev.year_start,
                                     ev.position, col))

    print(f"bracketed place-less events (same colony both sides): {n_brk}  ({len(brk_bios)} bios)")
    print(f"  ... on a currently-UNMATCHED bio:                   {n_unm}  ({len(unm_bios)} bios)")
    print(f"  ... AND a matching record exists:                   {n_rec}  ({len(rec_bios)} bios)  <-- UPSIDE")
    print("\nexamples (surname, given, year, position, bracket-colony):")
    for s, g, y, p, c in examples:
        print(f"  {s},{g} @{y} [{c}]  pos={p!r}")


if __name__ == "__main__":
    main()
