"""MEASURE-ONLY: size the prefix-truncation-tolerant surname lever.

OCR root-cause analysis (memory `unmatched-ocr-root-cause.md`) found ~17% of
unmatched placed bios are blocked by leading-character truncation of the bold
services-section entry-header surname (Griffiths->FFITHS, Camacho->MACHO): the
clean record surname already exists, only the bio headword lost its first 1-3
chars.

For each placed bio with NO phase-1 link, find officials whose surname is the
bio surname with a 1..MAX_DROP-char prefix dropped (a clean suffix relationship,
len>=MIN_TRUNC_LEN) and check whether `_align(require_strong=True, trunc=True)`
ACCEPTS them under the truncation guards (shared spelled forename + printed
position >= TRUNC_POS / honour / cooc). Prints the recoverable set with the
actual surname pairs so the Griffiths->FFITHS class can be eyeballed against
short-suffix namesake pollution.
"""
from __future__ import annotations

import json
import os
from collections import defaultdict
from pathlib import Path

from col_match.config import Config
from col_match.services.match import (
    _align, _names_compatible, _norm, _surname_of_official,
    _truncation_block, _truncation_index,
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
trunc_index = _truncation_index(surname_keys)
print(f"truncation suffixes indexed: {len(trunc_index)}")

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

# how many unmatched placed bios even HAVE a truncation candidate (retrieval ceiling)
retrieval_bios = 0
recovered = []  # (bio, official, strength)
for bio in bios:
    if bio.bio_id in linked:
        continue
    if not any(ev.year_start is not None and ev.place for ev in bio.events):
        continue
    block = _truncation_block(_norm(bio.surname), trunc_index, by_surname)
    if not block:
        continue
    retrieval_bios += 1
    for o in block:
        given_off = (o["name"].split(",", 1)[1].strip()
                     if "," in (o["name"] or "") else None)
        if not _names_compatible(bio.given_names, given_off):
            continue
        res = _align(bio, o, DD, require_strong=True, trunc=True)
        if res is not None:
            recovered.append((bio, o, res[1]))

by_bio = defaultdict(list)
for bio, o, s in recovered:
    by_bio[bio.bio_id].append((bio, o, s))

print(f"\nunmatched placed bios WITH a truncation candidate (retrieval): {retrieval_bios}")
print(f"ACCEPTED truncation pairs: {len(recovered)} across {len(by_bio)} bios (the realistic ceiling)\n")
print("(bio surname is a clean suffix of the official surname; dropped 1-3 leading chars)\n")
for bid, rows in sorted(by_bio.items(), key=lambda kv: -max(s for _, _, s in kv[1]))[:80]:
    bio = rows[0][0]
    bsur = _norm(bio.surname)
    for _b, o, s in sorted(rows, key=lambda r: -r[2])[:1]:
        osur = _surname_of_official(o["name"])
        drop = len(osur) - len(bsur)
        print(f"  [{int(s):4d}] '{bio.surname}, {bio.given_names}' ~ '{o['name']}' "
              f"(drop={drop}, suffix_len={len(bsur)}, colony={o['colony']})")
