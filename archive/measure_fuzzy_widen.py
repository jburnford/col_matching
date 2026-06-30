"""MEASURE-ONLY: what does widening _surname_block to dist<=2 for short
surnames (len 5-7) recover, and at what FP risk?

For each placed bio with NO phase-1 link, find fuzzy-surname officials that the
CURRENT block misses (len 5-7, distance exactly 2) and check whether
_align(require_strong=True) would ACCEPT them. Prints the recoverable set with
the actual surname pairs so the corroboration / FP risk is eyeballable.
"""
from __future__ import annotations

import json
import os
from collections import defaultdict
from pathlib import Path

from rapidfuzz import process
from rapidfuzz import distance

from col_match.config import Config
from col_match.services.match import (
    _align, _names_compatible, _norm, _surname_of_official, _surname_block,
)
from col_match.services.schema import Biography, StintMatch
from col_match.services.infer_colony import apply_recovered_places

cfg = Config.from_env()
DD = cfg.data_dir

bios = [Biography.model_validate_json(l)
        for l in (Path(DD) / "biographies" / "biographies.jsonl").open(encoding="utf-8")]
apply_recovered_places(bios, DD)

out = Path(DD) / "graph_cache"
aug = out / "officials_augmented.jsonl"
src = aug if (os.environ.get("COL_USE_AUGMENTED") == "1" and aug.exists()) else out / "officials.jsonl"
officials = [json.loads(l) for l in src.open(encoding="utf-8")]
print(f"officials source: {src.name}")

by_surname = defaultdict(list)
for o in officials:
    by_surname[_surname_of_official(o["name"])].append(o)
surname_keys = list(by_surname)

# phase-1 linked bios = those with a stint match or record attachment
linked = set()
sm = Path(DD) / "matches" / "stint_matches.jsonl"
if sm.exists():
    for l in sm.open(encoding="utf-8"):
        linked.add(StintMatch.model_validate_json(l).bio_id)
ra = Path(DD) / "matches" / "record_attachments.jsonl"
if ra.exists():
    for l in ra.open(encoding="utf-8"):
        linked.add(json.loads(l)["bio_id"])
print(f"phase-1 linked bios: {len(linked)}")


def widened_block(bio):
    """Officials retrieved at dist<=2 for ALL len>=5 (what the WIDENED block
    would see), minus what the CURRENT block already returns."""
    key = _norm(bio.surname)
    if key in by_surname or len(key) < 5:
        return []
    current, _ = _surname_block(bio, by_surname, surname_keys)
    cur_ids = {id(o) for o in current}
    out_ = []
    for k, _d, _i in process.extract(
        key, surname_keys, scorer=distance.Levenshtein.distance,
        score_cutoff=2, limit=8,
    ):
        for o in by_surname[k]:
            if id(o) not in cur_ids:
                out_.append(o)
    return out_


recovered = []  # (bio, official, strength)
for bio in bios:
    if bio.bio_id in linked:
        continue
    if not any(ev.year_start is not None and ev.place for ev in bio.events):
        continue
    for o in widened_block(bio):
        given_off = (o["name"].split(",", 1)[1].strip()
                     if "," in (o["name"] or "") else None)
        if not _names_compatible(bio.given_names, given_off):
            continue
        res = _align(bio, o, DD, require_strong=True)
        if res is not None:
            recovered.append((bio, o, res[1]))

# group by bio: a bio is "recovered" if >=1 passing widened candidate
by_bio = defaultdict(list)
for bio, o, s in recovered:
    by_bio[bio.bio_id].append((bio, o, s))

print(f"\nNEWLY-PASSING widened fuzzy candidates: {len(recovered)} pairs across {len(by_bio)} bios")
print("(these are dist-2 short-surname garbles the matcher can't see today)\n")
for bid, rows in sorted(by_bio.items(), key=lambda kv: -max(s for _, _, s in kv[1]))[:60]:
    bio = rows[0][0]
    bsur = bio.surname
    for _b, o, s in sorted(rows, key=lambda r: -r[2])[:1]:
        d = distance.Levenshtein.distance(_norm(bsur), _surname_of_official(o["name"]))
        print(f"  [{int(s):4d}] '{bsur}, {bio.given_names}' ~ '{o['name']}' "
              f"(d={d}, len={len(_norm(bsur))}, colony={o['colony']})")
