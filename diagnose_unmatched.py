#!/usr/bin/env python3
"""One iteration of the unmatched-bio debugging loop.

Pick an unmatched biography (random, stratified by edition decade, or a named
--bio), then surface everything needed to find the root cause of the miss:

  1. identity + career events (places/years/inherited/recovered)
  2. obvious-duplicate check (same/fuzzy surname + forename-compatible + overlap)
  3. match-gate replay: for every same-surname official, the per-dimension
     checks (colony / tenure / position_sim / honour / cooccurrence / place) —
     i.e. WHICH gate declined it (reuses candidates._annotate, the real logic)
  4. raw-OCR search: across the bio's edition/career years, which (colony, year)
     staff-list cells actually contain the surname (whole-word), with the line,
     initials-compatibility, and position — revealing extraction gaps, the true
     colony, OCR garble, etc.
  5. a heuristic verdict

Reads the CURRENT match target: officials_augmented.jsonl if present, else the
base. Run after each fix to watch the unmatched pile fall.

Usage:
  python3 diagnose_unmatched.py                 # random (seeded by --seed)
  python3 diagnose_unmatched.py --seed 7
  python3 diagnose_unmatched.py --decade 1900   # restrict to a decade
  python3 diagnose_unmatched.py --bio brooke_gilbert-e_e1894
"""
import argparse
import json
import random
import re
from collections import defaultdict
from pathlib import Path

from col_match.services import gazetteer
from col_match.services.candidates import _annotate
from col_match.services.compile import _initials as _c_initials
from col_match.services.compile import _names_compatible
from col_match.services.match import _norm, _surname_of_official
from col_match.services.recover import (_given_of, _name_segment,
                                        _position_context, _read, _surname_hit)
from col_match.services.schema import Biography
from col_match.services.source_index import load_index
from rapidfuzz.distance import Levenshtein

DD = Path("data/services")
SRC_OCR = Path("~/textasdatacolonialofficelist").expanduser()


def load_bios():
    return [Biography.model_validate_json(l)
            for l in (DD / "biographies" / "biographies.jsonl").open(encoding="utf-8")]


def load_officials():
    aug = DD / "graph_cache" / "officials_augmented.jsonl"
    p = aug if aug.exists() else DD / "graph_cache" / "officials.jsonl"
    return [json.loads(l) for l in p.open(encoding="utf-8")], p.name


def matched_bio_ids():
    m = set()
    for fn in ("record_attachments", "stint_matches"):
        p = DD / "matches" / f"{fn}.jsonl"
        if p.exists():
            for l in p.open(encoding="utf-8"):
                if l.strip():
                    m.add(json.loads(l)["bio_id"])
    return m


def career_years(bio):
    ys = set(bio.editions or [])
    for e in bio.events:
        if e.year_start:
            ys.add(e.year_start)
        if e.year_end:
            ys.add(e.year_end)
    return ys


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--bio")
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("--decade", type=int)
    ap.add_argument("--ocr-window", type=int, default=2)
    args = ap.parse_args()

    bios = load_bios()
    # apply the same recovered-place overlay attach/match use, so the gate
    # replay reflects what the matcher actually sees
    from col_match.services.infer_colony import apply_recovered_places
    n_overlay = apply_recovered_places(bios, str(DD))
    officials, src = load_officials()
    matched = matched_bio_ids()
    by_id = {b.bio_id: b for b in bios}

    if args.bio:
        bio = by_id.get(args.bio)
        if bio is None:
            print(f"no such bio {args.bio}"); return
    else:
        unmatched = [b for b in bios if b.bio_id not in matched
                     and any(e.year_start and e.place for e in b.events)]
        if args.decade:
            unmatched = [b for b in unmatched
                         if b.editions and (min(b.editions) // 10) * 10 == args.decade]
        rng = random.Random(args.seed)
        bio = rng.choice(unmatched)

    print(f"# match target: {src}   (bio matched={bio.bio_id in matched})")
    print(f"\n## {bio.surname}, {bio.given_names}   [{bio.bio_id}]")
    print(f"editions: {bio.editions}")
    if bio.birth_year:
        print(f"birth: {bio.birth_year.value}")
    if bio.terminal:
        print(f"terminal: {bio.terminal.kind} {bio.terminal.year}")
    print("events:")
    for i, e in enumerate(bio.events):
        tag = ("[inherited]" if e.place_inherited else
               "[recovered]" if getattr(e, "place_recovered", False) else "")
        print(f"  {i:2d}. {e.year_start}-{e.year_end or ''}  "
              f"place={e.place!r} {tag}  pos={e.position!r}")

    # 2. duplicate check
    bsur = _norm(bio.surname)
    print("\n## possible duplicate biographies (same/fuzzy surname, name-compatible)")
    dups = []
    for b in bios:
        if b.bio_id == bio.bio_id:
            continue
        s = _norm(b.surname)
        if s != bsur and (min(len(s), len(bsur)) < 6
                          or Levenshtein.distance(s, bsur, score_cutoff=1) > 1):
            continue
        if not _names_compatible(bio.given_names, b.given_names):
            continue
        overlap = career_years(bio) & career_years(b)
        dups.append((b, len(overlap)))
    for b, ov in sorted(dups, key=lambda t: -t[1])[:8]:
        print(f"  {b.bio_id}  given={b.given_names!r} ed={b.editions} "
              f"yr-overlap={ov}  matched={b.bio_id in matched}")
    if not dups:
        print("  (none)")

    # 3. match-gate replay over same-surname officials
    by_surname = defaultdict(list)
    for o in officials:
        by_surname[_surname_of_official(o["name"])].append(o)
    bio_surname_counts = defaultdict(int)
    for b in bios:
        bio_surname_counts[_norm(b.surname)] += 1
    block = list(by_surname.get(bsur, []))
    for k in by_surname:
        if k != bsur and len(k) >= 5 and Levenshtein.distance(k, bsur, score_cutoff=2) <= 2:
            block.extend(by_surname[k])
    cands, hardrej = [], 0
    for o in block:
        cand = _annotate(bio, o, _surname_of_official(o["name"]) != bsur, str(DD),
                         bio_surname_counts, by_surname)
        if cand is None:
            hardrej += 1
        else:
            cands.append((o, cand))
    print(f"\n## same-surname officials: {len(block)} "
          f"({len(cands)} pass hard gate (age/initials/year), {hardrej} rejected there)")
    # show initials-compatible candidates, strongest first
    cands.sort(key=lambda t: -(t[1].phase1_strength or 0))
    for o, cand in cands[:15]:
        passbar = "PASS-BAR" if cand.phase1_passed_bar else "below-bar"
        print(f"  - {o['id']}  [{passbar}, strength={cand.phase1_strength}]")
        for c in cand.checks:
            if c.name in ("colony", "tenure_overlap", "position_sim", "honour",
                          "edition_cooccurrence"):
                mark = "ok  " if c.passed else "FAIL"
                print(f"        {mark} {c.name}: {c.detail}")
    if not cands:
        print("  (no initials-compatible same-surname official — likely no record in graph for this person)")

    # 4. raw-OCR search across edition/career years
    print(f"\n## raw-OCR search (surname '{bio.surname}' in staff lists, "
          f"edition/career years +/-{args.ocr_window})")
    idx = load_index(str(SRC_OCR))
    years = sorted(career_years(bio))
    yset = set()
    for y in years:
        for d in range(-args.ocr_window, args.ocr_window + 1):
            yset.add(y + d)
    hits = []
    for y in sorted(yset):
        for terr_key, path in idx.by_year.get(y, ()):
            text, lines = _read(str(path))
            if not _surname_hit(text, bsur):
                continue
            for line in lines:
                if not _surname_hit(line, bsur):
                    continue
                seg = _name_segment(line, bsur)
                if not seg:
                    continue
                given = _given_of(seg, bsur)
                ini_ok = _names_compatible(bio.given_names, given)
                hits.append((y, path.stem, given, ini_ok,
                             _position_context(line, seg).strip()[:55], line.strip()[:90]))
    # show initials-compatible hits first, dedup by (colony,position)
    hits.sort(key=lambda h: (not h[3], h[0]))
    seen = set()
    shown = 0
    for y, terr, given, ini_ok, pos, line in hits:
        key = (terr, pos)
        if key in seen:
            continue
        seen.add(key)
        mark = "MATCH-INI" if ini_ok else "diff-ini "
        print(f"  {y} {terr:26s} {mark} given={given!r:18s} pos={pos!r}")
        shown += 1
        if shown >= 25:
            print("  ... (truncated)")
            break
    if not hits:
        print("  (surname not found in any staff-list file in these years — "
              "OCR garble, coverage gap, or genuinely not in colonial service)")

    # 5. verdict hint
    ini_hits = {(h[1]) for h in hits if h[3]}
    print("\n## verdict hint")
    if not block and not ini_hits:
        print("  NO-RECORD: surname absent from graph AND raw OCR -> not in service / OCR garble / coverage gap")
    elif not block and ini_hits:
        print(f"  EXTRACTION-GAP: surname in raw OCR ({sorted(ini_hits)}) but no graph official -> backfill/recover should add it")
    elif block:
        print("  RECORD-EXISTS: see which gate FAILs above (colony roll-up? position fuzz? ambiguity?) — likely the fix class")


if __name__ == "__main__":
    main()
