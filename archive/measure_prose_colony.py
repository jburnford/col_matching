#!/usr/bin/env python3
"""Measure §0 lever #1: prose-states-the-colony but the parser didn't attach it.

`rules_parse._parse_event_clause` resolves a place only from the LAST comma
segment of a clause (gazetteer.lookup) or that segment's prefix
(lookup_prefix). A colony stated mid-clause ("Colonial Secretary, Ceylon, and
member of Legislative Council, 1907") is missed -> the event goes place-less or
wrongly inherits the previous clause's place.

This sizes the recoverable upside, staged:
  (1) parser-gap: place-less OR inherited events whose text_span names a colony
      in a NON-last segment that the parser missed;
  (2) of those, the event's bio is currently UNMATCHED;
  (3) AND a same-(surname, recovered-colony, year+-2) staff-list record exists
      (initial-compatible) -> filling the place could actually unlock a match.

Read-only. Usage: COL_USE_AUGMENTED=1 python3 measure_prose_colony.py
"""
import json
import os
from collections import Counter, defaultdict
from pathlib import Path

from col_match.services import gazetteer
from col_match.services.compile import _names_compatible
from col_match.services.match import _initials, _norm, _surname_of_official
from col_match.services.schema import ParsedEntry, Biography

DD = Path("data/services")


def scan_clause_for_colony(text: str, last_seg_only_hit: str | None):
    """Return a colony resolvable from some comma segment of `text` OTHER than
    the parser's last-segment hit, else None. Mirrors the parser's vocabulary
    (gazetteer.lookup / lookup_prefix per segment)."""
    segs = [s.strip(" ,.") for s in text.split(",") if s.strip(" ,.")]
    if len(segs) < 2:
        return None
    # the parser already tried segs[-1]; scan the others
    for seg in segs[:-1]:
        hit = gazetteer.lookup(seg, DD.as_posix()) or gazetteer.lookup_prefix(seg, DD.as_posix())
        if hit:
            return hit
    return None


def main():
    # map version_id -> bio (for matched status + given names)
    bios = [Biography.model_validate_json(l)
            for l in (DD / "biographies" / "biographies.jsonl").open(encoding="utf-8")]
    ver2bio = {}
    for b in bios:
        for v in b.version_ids:
            ver2bio[v] = b

    matched = set()
    for fn in ("record_attachments", "stint_matches"):
        p = DD / "matches" / f"{fn}.jsonl"
        for l in p.open(encoding="utf-8"):
            if l.strip():
                matched.add(json.loads(l)["bio_id"])

    aug = DD / "graph_cache" / "officials_augmented.jsonl"
    op = aug if (os.environ.get("COL_USE_AUGMENTED") == "1" and aug.exists()) else DD / "graph_cache" / "officials.jsonl"
    officials = [json.loads(l) for l in op.open(encoding="utf-8")]
    # index officials by (surname, colony-normalized) -> list of (first,last,given)
    by_sur_col = defaultdict(list)
    for o in officials:
        sur = _surname_of_official(o["name"])
        col = gazetteer.norm(o["colony"] or "")
        given = o["name"].split(",", 1)[1].strip() if "," in (o["name"] or "") else None
        by_sur_col[(sur, col)].append((o["first_year"], o["last_year"], given))

    n_gap = 0           # parser-gap events (colony mid-clause, missed)
    n_unmatched = 0     # ... on an unmatched bio
    n_recoverable = 0   # ... AND a record exists at (surname, colony, year)
    gap_bios = set()
    unmatched_bios = set()
    recoverable_bios = set()
    examples = []

    for tier in ("rules", "llm"):
        path = DD / "parsed" / f"{tier}.jsonl"
        if not path.exists():
            continue
        for line in path.open(encoding="utf-8"):
            pe = ParsedEntry.model_validate_json(line)
            bio = ver2bio.get(pe.version_id)
            for ev in pe.events:
                # parser's own decision: place-less or inherited == place not
                # confidently printed on THIS clause
                if ev.place and not ev.place_inherited:
                    continue
                if ev.year_start is None:
                    continue
                col = scan_clause_for_colony(ev.text_span, ev.place)
                if not col:
                    continue
                cnorm = gazetteer.norm(col)
                # don't count if it's the same colony the parser already inherited
                if ev.place and gazetteer.norm(ev.place) == cnorm:
                    continue
                n_gap += 1
                if bio:
                    gap_bios.add(bio.bio_id)
                if bio and bio.bio_id in matched:
                    continue
                n_unmatched += 1
                if bio:
                    unmatched_bios.add(bio.bio_id)
                # record exists?
                sur = _norm(pe.surname)
                recs = by_sur_col.get((sur, cnorm), [])
                hit = False
                for fy, ly, given in recs:
                    if fy is None or ly is None:
                        continue
                    if ev.year_start - 2 <= ly and fy <= ev.year_start + 2 \
                            and _names_compatible(pe.given_names, given):
                        hit = True
                        break
                if hit:
                    n_recoverable += 1
                    if bio:
                        recoverable_bios.add(bio.bio_id)
                    if len(examples) < 25:
                        examples.append((pe.surname, pe.given_names, ev.year_start,
                                         col, ev.text_span[:90]))

    print(f"parser-gap events (colony mid-clause, parser missed):  {n_gap}  "
          f"({len(gap_bios)} bios)")
    print(f"  ... on a currently-UNMATCHED bio:                    {n_unmatched}  "
          f"({len(unmatched_bios)} bios)")
    print(f"  ... AND a matching staff-list record exists:         {n_recoverable}  "
          f"({len(recoverable_bios)} bios)  <-- UPSIDE CEILING")
    print("\nexamples (surname, given, year, recovered-colony, clause):")
    for s, g, y, c, t in examples:
        print(f"  {s},{g} @{y} -> [{c}]  ::  {t!r}")


if __name__ == "__main__":
    main()
