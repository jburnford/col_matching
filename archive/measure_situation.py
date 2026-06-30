"""Decompose the UNMATCHED bios: how many are duplicate fragments of an
already-matched person (dedup noise) vs genuinely unmatched, split placed/unplaced."""
from __future__ import annotations
import json, os
from collections import defaultdict
from pathlib import Path
from rapidfuzz import process, distance

from col_match.config import Config
from col_match.services.match import _norm, _shared_spelled_forename, _truncation_index
from col_match.services.schema import Biography
from col_match.services.infer_colony import apply_recovered_places

cfg = Config.from_env(); DD = cfg.data_dir
bios = [Biography.model_validate_json(l)
        for l in (Path(DD)/"biographies"/"biographies.jsonl").open(encoding="utf-8")]
apply_recovered_places(bios, DD)

matched = set()
for l in (Path(DD)/"matches"/"stint_matches.jsonl").open(): matched.add(json.loads(l)["bio_id"])
for l in (Path(DD)/"matches"/"record_attachments.jsonl").open(): matched.add(json.loads(l)["bio_id"])

byid = {b.bio_id: b for b in bios}
def placed(b): return any(ev.year_start is not None and ev.place for ev in b.events)

# index MATCHED bios by surname key
matched_by_sur = defaultdict(list)
for b in bios:
    if b.bio_id in matched:
        matched_by_sur[_norm(b.surname)].append(b)
matched_keys = list(matched_by_sur)
# truncation index over matched surnames (so an unmatched truncated headword
# finds its clean matched twin)
trunc_idx = _truncation_index(matched_keys)

def has_matched_twin(b):
    """Is there a MATCHED bio that is plausibly the SAME person? Same surname
    key (exact / dist<=2 garble / truncation) AND a shared spelled forename."""
    key = _norm(b.surname)
    cands = []
    cands += matched_by_sur.get(key, [])                       # exact
    for k in trunc_idx.get(key, ()):                           # unmatched is trunc of matched
        cands += matched_by_sur.get(k, [])
    if len(key) >= 5:                                          # dist<=2 garble
        for k, d, _ in process.extract(key, matched_keys,
                scorer=distance.Levenshtein.distance, score_cutoff=2, limit=5):
            if k != key: cands += matched_by_sur.get(k, [])
    for c in cands:
        if c.bio_id != b.bio_id and _shared_spelled_forename(b.given_names, c.given_names):
            return True
    return False

unmatched = [b for b in bios if b.bio_id not in matched]
stats = defaultdict(int)
for b in unmatched:
    p = "placed" if placed(b) else "unplaced"
    stats[(p, "total")] += 1
    if has_matched_twin(b):
        stats[(p, "dup_of_matched")] += 1

tot = len(bios)
print(f"total bios: {tot}")
print(f"matched union: {len(matched)} ({100*len(matched)/tot:.1f}%)")
print(f"unmatched: {len(unmatched)} ({100*len(unmatched)/tot:.1f}%)\n")
for p in ("placed","unplaced"):
    t = stats[(p,"total")]; d = stats[(p,"dup_of_matched")]
    print(f"  {p:8s}: {t:6d} unmatched | {d:5d} are dup-of-MATCHED-person ({100*d/t:.0f}%) | "
          f"{t-d:6d} genuinely unmatched")
dt = stats[("placed","dup_of_matched")] + stats[("unplaced","dup_of_matched")]
print(f"\nTOTAL unmatched that are duplicate fragments of an already-matched person: "
      f"{dt} ({100*dt/len(unmatched):.0f}% of unmatched, {100*dt/tot:.1f}% of all bios)")
print(f"If those were deduped, EFFECTIVE person-level coverage would be "
      f"~{100*(len(matched)+dt)/tot:.1f}% (upper bound; some twins are father/son)")
