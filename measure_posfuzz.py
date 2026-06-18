"""MEASURE-ONLY: anatomy of the position_fuzz class.

For placed-unmatched bios whose BEST exact-surname candidate clears colony+
tenure but sits just under the position bar 60, compare the scoring under the
current `_norm` vs `_pos_norm` (abbreviation-expanded, as attach.py already
uses). Reports:
  (a) how many near-misses cross bar 60 when scored with _pos_norm, and
  (b) the actual position-string pairs, flagging grade-list-header records
      (non-name rows like "Sixty Assistant District Officers").
"""
from __future__ import annotations

import json
import os
import re
from collections import defaultdict
from pathlib import Path

from rapidfuzz import fuzz

from col_match.config import Config
from col_match.services.compile import _pos_norm
from col_match.services.match import (
    POSITION_SIM, _names_compatible, _norm, _surname_of_official, _tenures,
)
from col_match.services.schema import Biography, StintMatch
from col_match.services.infer_colony import apply_recovered_places
from col_match.services import gazetteer

cfg = load = Config.from_env()
DD = cfg.data_dir

bios = [Biography.model_validate_json(l)
        for l in (Path(DD) / "biographies" / "biographies.jsonl").open(encoding="utf-8")]
apply_recovered_places(bios, DD)

out = Path(DD) / "graph_cache"
aug = out / "officials_augmented.jsonl"
src = aug if (os.environ.get("COL_USE_AUGMENTED") == "1" and aug.exists()) else out / "officials.jsonl"
officials = [json.loads(l) for l in src.open(encoding="utf-8")]

by_surname = defaultdict(list)
for o in officials:
    by_surname[_surname_of_official(o["name"])].append(o)

linked = set()
for fn in ("stint_matches.jsonl", "record_attachments.jsonl"):
    p = Path(DD) / "matches" / fn
    if p.exists():
        for l in p.open(encoding="utf-8"):
            linked.add(json.loads(l)["bio_id"])

# grade-list header heuristic: a record "position" that is itself a name-less
# count/grade row. Cheap signal: position contains a number-word or digit and
# generic grade nouns, OR the official "name" looks like a header.
_NUMWORD = re.compile(r"\b(one|two|three|four|five|six|seven|eight|nine|ten|"
                      r"eleven|twelve|twenty|thirty|forty|fifty|sixty|seventy|"
                      r"eighty|ninety|hundred|\d+)\b")


def looks_grade_header(name: str, positions: list[str]) -> bool:
    nm = _norm(name)
    if _NUMWORD.search(nm):
        return True
    # name with no comma (no surname,given structure) and generic
    return ("," not in (name or "")) and len(nm.split()) >= 3


cross = []          # near-miss that crosses 60 under _pos_norm
headers = []        # candidate is a grade-list header
near_miss_examples = []

for bio in bios:
    if bio.bio_id in linked:
        continue
    bsur = _norm(bio.surname)
    block = by_surname.get(bsur, [])
    if not block:
        continue
    best_norm, best_posnorm, best_pair, best_o = 0, 0, "", None
    for o in block:
        given_off = (o["name"].split(",", 1)[1].strip()
                     if "," in (o["name"] or "") else None)
        if not _names_compatible(bio.given_names, given_off):
            continue
        colony = gazetteer.norm(o["colony"] or "")
        fy, ly = o["first_year"], o["last_year"]
        if fy is None or ly is None:
            continue
        positions = [r["position_raw"] for r in o["records"] if r.get("position_raw")]
        for i, start, end in _tenures(bio):
            ev = bio.events[i]
            if colony not in gazetteer.colony_targets(ev.place, DD):
                continue
            if end < fy - 1 or start > ly + 1:
                continue
            for pos in positions:
                sn = fuzz.token_set_ratio(_norm(ev.position), _norm(pos))
                sp = fuzz.token_set_ratio(_pos_norm(ev.position), _pos_norm(pos))
                if sp > best_posnorm:
                    best_posnorm = sp
                if sn > best_norm:
                    best_norm = sn
                    best_pair = f"'{ev.position}' ~ '{pos}'"
                    best_o = o
    if best_o is None:
        continue
    # focus on the near-miss band the classifier calls position_fuzz
    if 30 <= best_norm < POSITION_SIM:
        positions = [r["position_raw"] for r in best_o["records"] if r.get("position_raw")]
        if looks_grade_header(best_o["name"], positions):
            headers.append((bio.surname, best_o["name"], best_pair))
        elif best_posnorm >= POSITION_SIM:
            cross.append((bio.surname, best_norm, best_posnorm, best_pair))
        else:
            near_miss_examples.append((bio.surname, best_norm, best_pair))

print(f"position_fuzz near-miss bios (30<=norm<60): "
      f"{len(cross)+len(headers)+len(near_miss_examples)}")
print(f"  -> CROSS bar 60 under _pos_norm (recoverable by abbrev-expand): {len(cross)}")
print(f"  -> grade-list-header candidate (phantom record): {len(headers)}")
print(f"  -> still below bar (genuine near-miss): {len(near_miss_examples)}")

print("\n--- CROSS (norm<60 but pos_norm>=60) ---")
for s, n, p, pair in cross[:30]:
    print(f"  {s}: {n}->{p}  {pair}")
print("\n--- grade-list-header candidates ---")
for s, nm, pair in headers[:25]:
    print(f"  {s} ~ '{nm}'  {pair}")
print("\n--- still-below near-misses (sample) ---")
for s, n, pair in near_miss_examples[:25]:
    print(f"  {s}: {n}  {pair}")
