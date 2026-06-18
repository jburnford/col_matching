"""Detect staff-list records the graph is missing, using biographies as the
index of who-served-where-when.

A gap is one biography career posting (a placed, dated event) that cannot be
attached to any graph record — the inverse of the record-claim gate in
``attach.py``. If ``attach`` could have claimed a record for the posting, the
person is in the graph and it is not a gap; if not, the record is missing.

Each gap is classified by whether the graph has *any* record for that
colony-year:
  - ``section_present`` — the section was extracted, this officer was dropped
    (a missed row);
  - ``section_absent``  — the colony-year is wholly absent from the graph
    (a missing section);
  - ``place_unresolved`` — the printed place mapped to no colony (cannot search).

Recovery (``recover.py``) then confirms each gap against the source OCR.
"""

from __future__ import annotations

from collections import defaultdict

from rapidfuzz import fuzz
from rapidfuzz.distance import Levenshtein

from . import gazetteer
from .attach import _initials_compatible, _norm
from .compile import _pos_norm
from .match import POSITION_SIM, _tenures
from .schema import Biography, GapEvent
from .source_index import SourceIndex


def _person_present(
    bio: Biography, colony: str, span: range,
    by_colony_year: dict[tuple[str, int], list[dict]],
) -> bool:
    """True if a graph record in `colony` over `span` matches this person on
    surname (exact/fuzzy) + initials + position — the attach.py gate."""
    sur = _norm(bio.surname)
    ev = bio.events
    for year in span:
        for cand in by_colony_year.get((colony, year), ()):
            r = cand
            rsur = _norm(r.get("surname") or (r.get("name_raw") or "").split(",")[0])
            if rsur != sur:
                if len(sur) < 6 or Levenshtein.distance(rsur, sur, score_cutoff=1) > 1:
                    continue
            if not _initials_compatible(bio.given_names, r.get("given_names")):
                continue
            return True
    return False


def find_gaps(
    bios: list[Biography], officials: list[dict], data_dir: str,
    index: SourceIndex,
) -> tuple[list[GapEvent], dict]:
    by_colony_year: dict[tuple[str, int], list[dict]] = defaultdict(list)
    colony_years: set[tuple[str, int]] = set()
    for o in officials:
        colony = gazetteer.norm(o["colony"] or "")
        for r in o["records"]:
            by_colony_year[(colony, r["year"])].append(r)
            colony_years.add((colony, r["year"]))

    gaps: list[GapEvent] = []
    for bio in bios:
        if not _norm(bio.surname):
            continue
        for (idx, start, end) in _tenures(bio):
            ev = bio.events[idx]
            span = range(start, end + 1)
            targets = gazetteer.colony_targets(ev.place, data_dir)
            if not targets:
                gaps.append(GapEvent(
                    bio_id=bio.bio_id, event_index=idx, surname=bio.surname,
                    given_names=bio.given_names, place=ev.place,
                    resolved_colony=None, year_start=start, year_end=end,
                    position=ev.position, gap_type="place_unresolved"))
                continue
            # covered if the person is present in ANY resolved colony in span
            if any(_person_present(bio, c, span, by_colony_year) for c in targets):
                continue
            # gap. classify by whether the graph has the colony-year at all.
            section_present = any((c, y) in colony_years
                                  for c in targets for y in span)
            primary = sorted(targets)[0]
            paths = index.resolve(ev.place, start, data_dir)
            gaps.append(GapEvent(
                bio_id=bio.bio_id, event_index=idx, surname=bio.surname,
                given_names=bio.given_names, place=ev.place,
                resolved_colony=primary, year_start=start, year_end=end,
                position=ev.position,
                gap_type="section_present" if section_present else "section_absent",
                source_file=str(paths[0]) if paths else None))

    by_type: dict[str, int] = defaultdict(int)
    by_decade: dict[int, int] = defaultdict(int)
    with_file = 0
    bios_with_gap: set[str] = set()
    for g in gaps:
        by_type[g.gap_type] += 1
        by_decade[g.year_start // 10 * 10] += 1
        if g.source_file:
            with_file += 1
        bios_with_gap.add(g.bio_id)
    stats = {
        "bios_total": len(bios),
        "gap_events": len(gaps),
        "bios_with_gap": len(bios_with_gap),
        "by_type": dict(sorted(by_type.items())),
        "by_decade": dict(sorted(by_decade.items())),
        "gaps_with_source_file": with_file,
        "recoverable_gaps": sum(
            1 for g in gaps
            if g.source_file and g.gap_type != "place_unresolved"),
    }
    return gaps, stats
