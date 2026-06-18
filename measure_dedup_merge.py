#!/usr/bin/env python3
"""Measure the OCR-garbled-surname DEDUP-MERGE upside.

Compile's union-find merges duplicate entry fragments, but its two-anchor rule
is conservative and OCR-garbled surnames (hagelthorn/hagetthorn/hageithorn,
mcgregor/macgregor) land in different surname blocks; thin fragments then never
merge. Each unmerged fragment is a separate (often unmatched) biography.

Sizing (read-only): for each UNMATCHED placed bio, is there ANOTHER bio that is
its confident duplicate -- surname exact or OCR-fuzzy (Levenshtein<=2, len>=6),
given names compatible with a SHARED SPELLED forename, and edition-year overlap?
Split by whether the twin is already matched:
  (A) twin MATCHED  -> merging folds the fragment into a matched person (removes
      an unmatched bio; more correct);
  (B) twin UNMATCHED -> merging pools thin events; may cross the bar together.

Usage: COL_USE_AUGMENTED=1 python3 measure_dedup_merge.py
"""
import json
from collections import defaultdict
from pathlib import Path

from rapidfuzz.distance import Levenshtein

from col_match.services.match import _norm, _initials
from col_match.services.schema import Biography

DD = Path("data/services")


def shared_spelled_forename(a, b):
    import re
    from col_match.services.compile import _token_match_ocr
    ta = [t for t in re.split(r"[ .]+", a or "") if len(t) > 1 and t[0].isalpha()]
    tb = [t for t in re.split(r"[ .]+", b or "") if len(t) > 1 and t[0].isalpha()]
    return any(_token_match_ocr(x, y) for x in ta for y in tb)


def main():
    bios = [Biography.model_validate_json(l)
            for l in (DD / "biographies" / "biographies.jsonl").open(encoding="utf-8")]
    matched = set()
    for fn in ("record_attachments", "stint_matches"):
        for l in (DD / "matches" / f"{fn}.jsonl").open(encoding="utf-8"):
            if l.strip():
                matched.add(json.loads(l)["bio_id"])

    placed = [b for b in bios if any(e.year_start and e.place for e in b.events)]
    # block by surname key; also gather keys for fuzzy neighbour search
    by_key = defaultdict(list)
    for b in bios:
        by_key[_norm(b.surname)].append(b)
    keys = list(by_key)

    def eds(b):
        s = set(b.editions or [])
        for e in b.events:
            if e.year_start:
                s.add(e.year_start)
        return s

    twin_matched = twin_unmatched = 0
    examples_m, examples_u = [], []
    for b in placed:
        if b.bio_id in matched:
            continue
        bkey = _norm(b.surname)
        # candidate twins: same key + fuzzy keys dist<=2 (len>=6)
        cand_keys = {bkey}
        if len(bkey) >= 6:
            for k in keys:
                if k != bkey and len(k) >= 6 and Levenshtein.distance(k, bkey, score_cutoff=2) <= 2:
                    cand_keys.add(k)
        be = eds(b)
        best = None
        for k in cand_keys:
            for o in by_key[k]:
                if o.bio_id == b.bio_id:
                    continue
                if not shared_spelled_forename(b.given_names, o.given_names):
                    continue
                if not (be & eds(o)):
                    continue
                best = o
                if o.bio_id in matched:
                    break
            if best and best.bio_id in matched:
                break
        if not best:
            continue
        if best.bio_id in matched:
            twin_matched += 1
            if len(examples_m) < 15:
                examples_m.append((b, best))
        else:
            twin_unmatched += 1
            if len(examples_u) < 10:
                examples_u.append((b, best))

    print(f"unmatched placed bios with a confident duplicate twin:")
    print(f"  (A) twin already MATCHED   : {twin_matched}  -> merge removes an unmatched bio")
    print(f"  (B) twin also UNMATCHED    : {twin_unmatched}  -> merge may cross bar together")
    print("\n(A) examples [unmatched bio]  <~>  [matched twin]:")
    for b, o in examples_m:
        print(f"  {b.surname},{b.given_names} [{b.bio_id}]  <~>  {o.surname},{o.given_names} [{o.bio_id}]")
    print("\n(B) examples:")
    for b, o in examples_u:
        print(f"  {b.surname},{b.given_names} [{b.bio_id}]  <~>  {o.surname},{o.given_names} [{o.bio_id}]")


if __name__ == "__main__":
    main()
