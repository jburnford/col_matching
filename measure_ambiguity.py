#!/usr/bin/env python3
"""Measure the ambiguity-guard over-drop lever (ADJUDICATION_GUIDE §0 lever #2).

Reproduces match.py candidate generation + _disambiguate, but INSTRUMENTS every
dropped pair: which prune rule fired (by_stint = two bios contest one stint;
by_bio_colony = one bio, overlapping same-colony stints), the competitors and
their strengths, and whether the contest looks like a genuine different-person
collision vs a recoverable case (e.g. the competing bio is a duplicate, or the
competitor's strength is much weaker / its career clearly sits elsewhere).

Goal: size how many of the ~1,265 extrapolated ambiguity_drop bios could be
safely recovered by a refined guard, BEFORE writing any code. Read-only.

Usage:  COL_USE_AUGMENTED=1 python3 measure_ambiguity.py
"""
import json
import os
from collections import Counter, defaultdict
from pathlib import Path

from col_match.services import gazetteer
from col_match.services.compile import _names_compatible
from col_match.services.infer_colony import apply_recovered_places
from col_match.services.match import (
    AMBIGUITY_MARGIN, _align, _names_compatible as _nc, _norm, _surname_block,
    _surname_of_official,
)
from col_match.services.schema import Biography

DD = Path("data/services")


def load_bios():
    bios = [Biography.model_validate_json(l)
            for l in (DD / "biographies" / "biographies.jsonl").open(encoding="utf-8")]
    apply_recovered_places(bios, str(DD))
    return bios


def load_officials():
    aug = DD / "graph_cache" / "officials_augmented.jsonl"
    p = aug if (os.environ.get("COL_USE_AUGMENTED") == "1" and aug.exists()) else DD / "graph_cache" / "officials.jsonl"
    return [json.loads(l) for l in p.open(encoding="utf-8")]


def matched_ids():
    m = set()
    for fn in ("record_attachments", "stint_matches"):
        p = DD / "matches" / f"{fn}.jsonl"
        if p.exists():
            for l in p.open(encoding="utf-8"):
                if l.strip():
                    m.add(json.loads(l)["bio_id"])
    return m


def main():
    bios = load_bios()
    officials = load_officials()
    bio_by_id = {b.bio_id: b for b in bios}
    off_by_id = {o["id"]: o for o in officials}
    matched = matched_ids()

    by_surname = defaultdict(list)
    for o in officials:
        by_surname[_surname_of_official(o["name"])].append(o)
    surname_keys = list(by_surname)

    # reproduce match_biographies candidate generation
    candidates = []  # (StintMatch, strength)
    for bio in bios:
        cands, fuzzy = _surname_block(bio, by_surname, surname_keys)
        for official in cands:
            given_off = (official["name"].split(",", 1)[1].strip()
                         if "," in (official["name"] or "") else None)
            if not _nc(bio.given_names, given_off):
                continue
            result = _align(bio, official, str(DD), require_strong=fuzzy)
            if result is not None:
                candidates.append(result)

    # group like _disambiguate
    by_stint = defaultdict(list)
    by_bio_colony = defaultdict(list)
    for m, s in candidates:
        by_stint[m.official_id].append((m, s))
        colony = m.official_id.split("___")[1] if "___" in m.official_id else ""
        by_bio_colony[(m.bio_id, colony)].append((m, s))

    dropped = {}  # id(m) -> reason record

    def colony_of(oid):
        return oid.split("___")[1] if "___" in oid else ""

    # by_stint prune (instrumented)
    for oid, group in by_stint.items():
        if len(group) < 2:
            continue
        if any(not m.fuzzy_surname for m, _ in group):
            fuzzies = [t for t in group if t[0].fuzzy_surname]
            for m, _ in fuzzies:
                dropped.setdefault(id(m), ("by_stint_fuzzy", oid, group))
            group = [t for t in group if not t[0].fuzzy_surname]
            if len(group) < 2:
                continue
        group = sorted(group, key=lambda t: t[1], reverse=True)
        best_s = group[0][1]
        if group[1][1] >= best_s - AMBIGUITY_MARGIN:
            for m, _ in group:
                dropped.setdefault(id(m), ("by_stint_alldrop", oid, group))
        else:
            for m, _ in group[1:]:
                dropped.setdefault(id(m), ("by_stint_loser", oid, group))

    # by_bio_colony prune (instrumented)
    for key, group in by_bio_colony.items():
        if len(group) < 2:
            continue
        spans = []
        for m, s in group:
            try:
                fy = int(m.official_id.rsplit("___", 1)[1])
            except ValueError:
                fy = 0
            spans.append((fy, m, s))
        spans.sort(key=lambda t: t[0])
        for (fa, ma, sa), (fb, mb, sb) in zip(spans, spans[1:]):
            if fb <= fa + 3 and abs(sa - sb) < AMBIGUITY_MARGIN:
                dropped.setdefault(id(ma), ("by_bio_colony", key, group))
                dropped.setdefault(id(mb), ("by_bio_colony", key, group))

    # Which dropped pairs belong to bios that are ENTIRELY unmatched (recovery
    # would add a brand-new matched bio)?
    kept_ids = {id(m) for m, _ in candidates if id(m) not in dropped}
    bios_with_kept = {next(m for m2, _ in candidates if id(m2) == i).bio_id
                      for i in kept_ids}

    reason_counts = Counter()
    # for each dropped pair on an unmatched bio, characterize the contest
    unmatched_drop_bios = set()
    recoverable_buckets = Counter()
    examples = defaultdict(list)

    for m, s in candidates:
        if id(m) not in dropped:
            continue
        reason, key, group = dropped[id(m)]
        reason_counts[reason] += 1
        bio = bio_by_id[m.bio_id]
        # only interesting if this bio is otherwise unmatched & has no kept cand
        if m.bio_id in matched or m.bio_id in bios_with_kept:
            continue
        unmatched_drop_bios.add(m.bio_id)

        if reason.startswith("by_stint"):
            # competitors = other bios contesting this same stint
            comp_bios = [(mm, ss) for mm, ss in group if mm.bio_id != m.bio_id]
            # are competitors likely duplicates of THIS bio (same given names)?
            dup = False
            diff_person = False
            for mm, ss in comp_bios:
                cb = bio_by_id.get(mm.bio_id)
                if cb and _names_compatible(bio.given_names, cb.given_names):
                    dup = True
                else:
                    diff_person = True
            if reason == "by_stint_alldrop":
                if dup and not diff_person:
                    recoverable_buckets["stint_competitor_is_duplicate"] += 1
                    bucket = "stint_competitor_is_duplicate"
                elif not dup and diff_person:
                    recoverable_buckets["stint_competitor_diff_person_genuine"] += 1
                    bucket = "stint_competitor_diff_person_genuine"
                else:
                    recoverable_buckets["stint_competitor_mixed"] += 1
                    bucket = "stint_competitor_mixed"
            else:
                recoverable_buckets[reason] += 1
                bucket = reason
        else:  # by_bio_colony
            # are the contesting stints the SAME official re-listed (same name)?
            names = {off_by_id[mm.official_id]["name"] for mm, _ in group
                     if mm.official_id in off_by_id}
            if len(names) == 1:
                recoverable_buckets["biocolony_same_official_name"] += 1
                bucket = "biocolony_same_official_name"
            else:
                recoverable_buckets["biocolony_diff_official_names"] += 1
                bucket = "biocolony_diff_official_names"

        if len(examples[bucket]) < 6:
            examples[bucket].append((m, s, key, group))

    print(f"total candidates (passed _align): {len(candidates)}")
    print(f"total dropped by guard: {len(dropped)}")
    print(f"\ndrop reason counts (all dropped pairs):")
    for r, n in reason_counts.most_common():
        print(f"  {n:6d}  {r}")
    print(f"\nbios that are ENTIRELY unmatched AND lost a pair to the guard: "
          f"{len(unmatched_drop_bios)}")
    print(f"(these are the recovery-upside population)")
    print(f"\nrecoverability buckets (dropped pairs on entirely-unmatched bios):")
    for b, n in recoverable_buckets.most_common():
        print(f"  {n:6d}  {b}")

    # show a few examples per bucket
    for bucket in ("stint_competitor_diff_person_genuine",
                   "stint_competitor_is_duplicate",
                   "biocolony_same_official_name",
                   "biocolony_diff_official_names",
                   "stint_competitor_mixed"):
        exs = examples.get(bucket, [])
        if not exs:
            continue
        print(f"\n=== examples: {bucket} ===")
        for m, s, key, group in exs:
            bio = bio_by_id[m.bio_id]
            off = off_by_id.get(m.official_id, {})
            print(f"  BIO {bio.surname},{bio.given_names} [{m.bio_id}] str={s}")
            print(f"    -> stint {off.get('name')} | {off.get('colony')} "
                  f"{off.get('first_year')}-{off.get('last_year')}")
            for mm, ss in group:
                if id(mm) == id(m):
                    continue
                if mm.bio_id != m.bio_id:
                    cb = bio_by_id.get(mm.bio_id)
                    print(f"    competitor BIO {cb.surname},{cb.given_names} "
                          f"[{mm.bio_id}] str={ss}")
                else:
                    co = off_by_id.get(mm.official_id, {})
                    print(f"    competitor STINT {co.get('name')} | "
                          f"{co.get('colony')} {co.get('first_year')} str={ss}")


if __name__ == "__main__":
    main()
