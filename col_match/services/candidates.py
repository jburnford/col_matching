"""Enumerate below-bar bio↔stint candidates with full evidence annotations.

Phase 1 (match.py / attach.py) keeps only pairs that clear a strict evidence
bar and silently discards everything else. This stage re-runs candidate
generation keeping only the HARD gates as filters — surname block, initial
compatibility, age sanity; the rules never delegated to an adjudicator — and
persists every surviving pair with each evidence dimension annotated, passed
or failed, so a dossier can show exactly what the deterministic pass saw and
why it declined.

Output population: pairs for biographies with at least one placed dated event
and NO phase-1 link (no stint match, no record attachment), plus any pair
that passed phase 1's evidence bar but was dropped by its ambiguity guard
(`phase1_dropped_ambiguous` — already-identified contests). Competitor lists
are computed over ALL placed biographies, including phase-1-linked ones, so
a dossier never hides a stronger claimant.
"""

from __future__ import annotations

import os
from collections import defaultdict

from rapidfuzz import fuzz
from rapidfuzz.distance import Levenshtein

from . import gazetteer
from .compile import _pos_norm
from .match import (
    POSITION_SIM,
    _align,
    _cooc_scan,
    _initials,
    _names_compatible,
    _norm,
    _surname_block,
    _surname_of_official,
    _tenures,
    _truncation_block,
    _truncation_index,
)
from .schema import Biography, DimensionCheck, StintCandidate


def enumerate_candidates(
    bios: list[Biography],
    officials: list[dict],
    data_dir: str,
    phase1_stint_pairs: set[tuple[str, str]],
    phase1_linked_bios: set[str],
) -> tuple[list[StintCandidate], dict]:
    """Returns (candidates, stats). `phase1_stint_pairs` = accepted
    (bio_id, official_id) from stint_matches.jsonl; `phase1_linked_bios` =
    bio_ids with any accepted stint match or record attachment."""
    by_surname: dict[str, list[dict]] = defaultdict(list)
    for o in officials:
        by_surname[_surname_of_official(o["name"])].append(o)
    surname_keys = list(by_surname)
    trunc_on = os.environ.get("COL_NO_TRUNC") != "1"
    trunc_index = _truncation_index(surname_keys) if trunc_on else {}

    bio_surname_counts: dict[str, int] = defaultdict(int)
    for b in bios:
        bio_surname_counts[_norm(b.surname)] += 1

    placed = [b for b in bios
              if any(ev.year_start is not None and ev.place for ev in b.events)]
    target_bios = {b.bio_id for b in placed if b.bio_id not in phase1_linked_bios}

    all_pairs: list[StintCandidate] = []
    for bio in placed:
        block, fuzzy = _surname_block(bio, by_surname, surname_keys)
        tried: set = set()
        for official in block:
            tried.add(official["id"])
            cand = _annotate(bio, official, fuzzy, data_dir,
                             bio_surname_counts, by_surname)
            if cand is None:
                continue
            cand.phase1_dropped_ambiguous = (
                cand.phase1_passed_bar
                and (cand.bio_id, cand.official_id) not in phase1_stint_pairs
            )
            all_pairs.append(cand)
        if trunc_on:
            # mirror match.py's truncation path so reconciliation
            # (phase1_matches_not_reproduced) stays 0
            for official in _truncation_block(_norm(bio.surname), trunc_index, by_surname):
                if official["id"] in tried:
                    continue
                tried.add(official["id"])
                cand = _annotate(bio, official, False, data_dir,
                                 bio_surname_counts, by_surname, trunc=True)
                if cand is None:
                    continue
                cand.phase1_dropped_ambiguous = (
                    cand.phase1_passed_bar
                    and (cand.bio_id, cand.official_id) not in phase1_stint_pairs
                )
                all_pairs.append(cand)

    by_stint: dict[str, set[str]] = defaultdict(set)
    for c in all_pairs:
        by_stint[c.official_id].add(c.bio_id)
    for c in all_pairs:
        c.competing_bio_ids = sorted(by_stint[c.official_id] - {c.bio_id})

    kept = [c for c in all_pairs
            if c.bio_id in target_bios or c.phase1_dropped_ambiguous]

    # reconciliation: enumeration must reproduce phase 1 exactly — every
    # accepted stint match reappears as a passed-bar pair, and the passed-bar
    # pairs NOT accepted are precisely the ambiguity-guard drops
    passed_pairs = {(c.bio_id, c.official_id)
                    for c in all_pairs if c.phase1_passed_bar}
    stats = {
        "bios_total": len(bios),
        "bios_placed": len(placed),
        "bios_unlinked_placed": len(target_bios),
        "pairs_enumerated": len(all_pairs),
        "pairs_passed_phase1_bar": len(passed_pairs),
        "pairs_dropped_ambiguous": sum(c.phase1_dropped_ambiguous for c in all_pairs),
        "phase1_matches_not_reproduced": len(phase1_stint_pairs - passed_pairs),
        "candidates_written": len(kept),
        "bios_with_candidates": len({c.bio_id for c in kept}),
        "stints_with_candidates": len({c.official_id for c in kept}),
        "single_initial_candidates": sum(c.single_initial for c in kept),
        "fuzzy_surname_candidates": sum(c.surname_gate != "exact" for c in kept),
    }
    return kept, stats


def _annotate(
    bio: Biography,
    official: dict,
    fuzzy: bool,
    data_dir: str,
    bio_surname_counts: dict[str, int],
    by_surname: dict[str, list[dict]],
    trunc: bool = False,
) -> StintCandidate | None:
    fy, ly = official["first_year"], official["last_year"]
    if fy is None or ly is None:
        return None
    # hard gates, mirroring _align: a stint can't begin before the person
    # could have served, or after they died
    if bio.birth_year and fy < bio.birth_year.value + 15:
        return None
    if bio.terminal and bio.terminal.kind == "died" and bio.terminal.year \
            and fy > bio.terminal.year:
        return None
    given_off = (official["name"].split(",", 1)[1].strip()
                 if "," in (official["name"] or "") else None)
    if not _names_compatible(bio.given_names, given_off):
        return None

    bio_sur, off_sur = _norm(bio.surname), _surname_of_official(official["name"])
    if trunc:
        gate = f"trunc:{len(off_sur) - len(bio_sur)}"
    else:
        gate = "exact" if off_sur == bio_sur else \
            f"fuzzy:{Levenshtein.distance(off_sur, bio_sur)}"

    colony = gazetteer.norm(official["colony"] or "")
    stint_positions = [r["position_raw"] for r in official["records"]
                       if r.get("position_raw")]
    stint_honours = {_norm(h) for r in official["records"]
                     for h in (r.get("honors") or [])}
    bio_honours = {_norm(h.award): h.award for h in bio.honours}
    honour_overlap = sorted(bio_honours[h] for h in stint_honours
                            if h in bio_honours)

    colony_events: list[int] = []
    overlaps: list[tuple[int, int, int]] = []
    any_printed_place = False
    best_pos, best_pos_detail = 0, ""
    for i, start, end in _tenures(bio):
        ev = bio.events[i]
        if colony not in gazetteer.colony_targets(ev.place, data_dir):
            continue
        colony_events.append(i)
        if end < fy - 1 or start > ly + 1:
            continue
        overlaps.append((i, start, end))
        if not ev.place_inherited:
            any_printed_place = True
        for pos in stint_positions:
            s = fuzz.token_set_ratio(_pos_norm(ev.position), _pos_norm(pos))
            if s > best_pos:
                best_pos = s
                best_pos_detail = f"'{ev.position}' ~ '{pos}'"

    cooc = _cooc_scan(bio, official, colony, data_dir)
    cooc_years = [y for y, _ in cooc]
    cooc_avg = sum(s for _, s in cooc) / len(cooc) if cooc else 0

    checks = [
        DimensionCheck(
            name="surname_gate", passed=True,
            detail=f"bio '{bio.surname}' vs stint '{official['name']}' ({gate})"),
        DimensionCheck(
            name="initials", passed=True,
            detail=f"bio {_initials(bio.given_names) or ['?']} ~ "
                   f"stint {_initials(given_off) or ['?']}"),
        DimensionCheck(
            name="age_gate", passed=True,
            detail=(f"stint starts {fy}, birth {bio.birth_year.value} "
                    f"(age {fy - bio.birth_year.value})" if bio.birth_year
                    else f"stint starts {fy}; no printed birth year — UNCHECKED")),
        DimensionCheck(
            name="colony", passed=bool(colony_events),
            detail=(f"{len(colony_events)} placed event(s) resolve to "
                    f"'{official['colony']}'" if colony_events
                    else f"no placed event resolves to '{official['colony']}'")),
        DimensionCheck(
            name="tenure_overlap", passed=bool(overlaps),
            detail=(f"{len(overlaps)} event tenure(s) overlap stint years "
                    f"{fy}-{ly}" if overlaps
                    else f"no colony-agreeing tenure overlaps stint years {fy}-{ly}")),
        DimensionCheck(
            name="position_sim", passed=best_pos >= POSITION_SIM,
            detail=(f"best {best_pos:.0f} vs bar {POSITION_SIM}: {best_pos_detail}"
                    if best_pos_detail
                    else "no overlapping placed event to compare")),
        DimensionCheck(
            name="honour", passed=bool(honour_overlap),
            detail=(f"shared: {', '.join(honour_overlap)}" if honour_overlap
                    else "no shared honour")),
        DimensionCheck(
            name="edition_cooccurrence", passed=len(cooc_years) >= 2,
            detail=(f"{len(cooc_years)} agreeing edition-year(s) "
                    f"{cooc_years[:6]} pos~{cooc_avg:.0f} (bar: >=2)"
                    if cooc_years else "no agreeing edition-years")),
        DimensionCheck(
            name="place_inherited", passed=any_printed_place,
            detail=("at least one supporting event names its place in print"
                    if any_printed_place else
                    ("ALL supporting events inherit their place from an "
                     "earlier clause — weak evidence" if overlaps
                     else "no supporting events"))),
    ]

    result = _align(bio, official, data_dir, require_strong=fuzzy or trunc, trunc=trunc)
    return StintCandidate(
        bio_id=bio.bio_id,
        official_id=official["id"],
        surname_gate=gate,
        single_initial=len(_initials(bio.given_names)) <= 1,
        checks=checks,
        cooc_years=cooc_years,
        best_position_score=best_pos,
        honour_overlap=honour_overlap,
        tenure_overlaps=overlaps,
        phase1_strength=result[1] if result else None,
        phase1_passed_bar=result is not None,
        same_surname_officials=len(by_surname.get(off_sur, [])),
        same_surname_bios=bio_surname_counts.get(bio_sur, 0),
    )
