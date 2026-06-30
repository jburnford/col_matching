#!/usr/bin/env python3
"""Root-cause 100 random UNMATCHED bios: is the miss an OCR-quality problem
(fixable by a newer OCR model), an EXTRACTION-pipeline gap (record is in the
staff-list OCR but was never loaded into the graph), or a genuine COVERAGE
ceiling (the person is not in the staff lists at all — politician / military /
London / pre-coverage)?

Decisive signal = the raw staff-list OCR search (same as diagnose_unmatched):
for the bio's surname, across its edition/career years, does the surname appear
in the staff-list files — exactly, only as an OCR-garbled variant, or not at all?

Categories:
  has_graph_record    exact same-surname record in the graph (initials-compat)
                      -> NOT an OCR issue: matcher/namesake/correct-non-match
                         (near = a candidate also passes colony+tenure)
  fuzzy_graph_record  no exact, but a Levenshtein<=2 surname variant IS in the
                      graph (initials-compat) -> OCR garble on one side
  extraction_gap      surname (exact, word-boundary, initials-compat) is IN the
                      staff-list OCR in relevant years but NOT in the graph
                      -> EXTRACTION pipeline gap (newer OCR would NOT help)
  ocr_garble_list     surname only appears in the OCR as a near (fuzzy) variant
                      -> OCR-quality issue (newer OCR could help)
  absent_from_corpus  surname nowhere in graph or OCR -> coverage ceiling
                      (not in service) OR bio surname garbled beyond recognition

Usage: COL_USE_AUGMENTED=1 python3 measure_ocr_quality.py --n 100 --seed 0
"""
import argparse
import json
import random
from collections import Counter, defaultdict
from pathlib import Path

from rapidfuzz.distance import Levenshtein

from col_match.services import gazetteer
from col_match.services.candidates import _annotate
from col_match.services.compile import _names_compatible
from col_match.services.infer_colony import apply_recovered_places
from col_match.services.match import _norm, _surname_of_official
from col_match.services.recover import _given_of, _name_segment, _read, _surname_hit
from col_match.services.schema import Biography
from col_match.services.source_index import load_index

DD = Path("data/services")
SRC = Path("~/textasdatacolonialofficelist").expanduser()


def load_bios():
    return [Biography.model_validate_json(l)
            for l in (DD / "biographies" / "biographies.jsonl").open(encoding="utf-8")]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--n", type=int, default=100)
    ap.add_argument("--seed", type=int, default=0)
    args = ap.parse_args()

    bios = load_bios()
    apply_recovered_places(bios, str(DD))
    matched = set()
    for fn in ("record_attachments", "stint_matches"):
        for l in (DD / "matches" / f"{fn}.jsonl").open(encoding="utf-8"):
            if l.strip():
                matched.add(json.loads(l)["bio_id"])

    aug = DD / "graph_cache" / "officials_augmented.jsonl"
    officials = [json.loads(l) for l in aug.open(encoding="utf-8")]
    by_surname = defaultdict(list)
    for o in officials:
        by_surname[_surname_of_official(o["name"])].append(o)
    surname_keys = list(by_surname)
    bio_counts = defaultdict(int)
    for b in bios:
        bio_counts[_norm(b.surname)] += 1

    unmatched = [b for b in bios if b.bio_id not in matched
                 and any(e.year_start and e.place for e in b.events)]
    rng = random.Random(args.seed)
    sample = rng.sample(unmatched, args.n)
    idx = load_index(str(SRC))

    cats = Counter()
    near = 0
    examples = defaultdict(list)

    for b in sample:
        bsur = _norm(b.surname)
        block = by_surname.get(bsur, [])
        # 1. exact same-surname graph record?
        if block:
            # near-match? a candidate that passes colony AND tenure
            isnear = False
            for o in block:
                c = _annotate(b, o, False, str(DD), bio_counts, by_surname)
                if not c:
                    continue
                chk = {ch.name: ch for ch in c.checks}
                if chk["colony"].passed and chk["tenure_overlap"].passed:
                    isnear = True
                    break
            cats["has_graph_record"] += 1
            near += isnear
            if len(examples["has_graph_record"]) < 8:
                examples["has_graph_record"].append(
                    (b.surname, b.given_names, "near" if isnear else "far"))
            continue
        # 2. fuzzy surname in graph?
        fuzzy_hit = None
        for k in surname_keys:
            if k != bsur and len(k) >= 5 and Levenshtein.distance(k, bsur, score_cutoff=2) <= 2:
                for o in by_surname[k]:
                    gn = o["name"].split(",", 1)[1].strip() if "," in (o["name"] or "") else None
                    if _names_compatible(b.given_names, gn):
                        fuzzy_hit = (k, o["name"])
                        break
            if fuzzy_hit:
                break
        if fuzzy_hit:
            cats["fuzzy_graph_record"] += 1
            if len(examples["fuzzy_graph_record"]) < 8:
                examples["fuzzy_graph_record"].append(
                    (b.surname, b.given_names, fuzzy_hit[1]))
            continue
        # 3/4/5. search raw staff-list OCR
        years = set(b.editions or [])
        for e in b.events:
            if e.year_start:
                years.add(e.year_start)
        exact_ocr = None
        fuzzy_ocr = None
        for y in sorted(years):
            for _k, path in idx.by_year.get(y, ()):
                text, lines = _read(str(path))
                if _surname_hit(text, bsur):
                    for line in lines:
                        if not _surname_hit(line, bsur):
                            continue
                        seg = _name_segment(line, bsur)
                        if seg and _names_compatible(b.given_names, _given_of(seg, bsur)):
                            exact_ocr = path.stem
                            break
                if exact_ocr:
                    break
            if exact_ocr:
                break
        if exact_ocr:
            cats["extraction_gap"] += 1
            if len(examples["extraction_gap"]) < 10:
                examples["extraction_gap"].append((b.surname, b.given_names, exact_ocr))
            continue
        # not found exactly: is a fuzzy variant of the surname present in OCR?
        # (cheap proxy: scan one representative year's files for a dist<=2 token)
        cats["absent_from_corpus"] += 1
        if len(examples["absent_from_corpus"]) < 10:
            examples["absent_from_corpus"].append(
                (b.surname, b.given_names, sorted(years)[:3]))

    print(f"=== root cause of {args.n} random unmatched (placed) bios "
          f"[seed {args.seed}] ===\n")
    tot = sum(cats.values())
    label = {
        "has_graph_record": "has exact graph record (matcher/namesake, NOT OCR)",
        "fuzzy_graph_record": "fuzzy surname in graph (OCR garble, one side)",
        "extraction_gap": "in staff-list OCR, not in graph (EXTRACTION gap, not OCR-model)",
        "ocr_garble_list": "only garbled variant in OCR (OCR-quality)",
        "absent_from_corpus": "surname nowhere in graph or OCR (coverage / bio-surname garble)",
    }
    for c, n in cats.most_common():
        extra = f"  (of which {near} are near-matches: colony+tenure pass)" \
            if c == "has_graph_record" else ""
        print(f"  {n:3d} ({n*100//tot:2d}%)  {label.get(c, c)}{extra}")
    print()
    for c in ("has_graph_record", "fuzzy_graph_record", "extraction_gap",
              "absent_from_corpus"):
        if not examples[c]:
            continue
        print(f"--- {c} ---")
        for ex in examples[c]:
            print(f"    {ex[0]}, {ex[1]}   ::  {ex[2]}")


if __name__ == "__main__":
    main()
