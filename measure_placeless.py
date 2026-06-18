"""MEASURE-ONLY: why are placeless_strong bios' strong-position events not
recovered by Tier A? Bucket each placeless dated event that has a real position
by what the Tier-A record index holds at (surname, year+/-2):
  - no_record         : nothing in graph -> Tier B territory (needs synth)
  - multi_colony       : >1 colony, not resolvable by intra-bio -> ambiguous
  - multi_resolved_own : >1 colony BUT bio attests one of them placed -> Tier A
                         already resolves these; shouldn't be residual
  - single_low_pos     : single colony but position < 60 vs records
  - single_ok          : single colony, pos>=60 -> Tier A SHOULD have recovered
Restricted to UNMATCHED bios (union), and only events whose position is
'strong' (len>4), i.e. the placeless_strong signal.
"""
from __future__ import annotations

import json, os
from collections import defaultdict, Counter
from pathlib import Path

from rapidfuzz import fuzz

from col_match.config import Config
from col_match.services.compile import _pos_norm
from col_match.services.infer_colony import _build_record_index, _skey, _placed_colonies
from col_match.services.attach import _initials_compatible
from col_match.services.schema import Biography
from col_match.services import gazetteer

DD = Config.from_env().data_dir
WINDOW = 2

bios = [Biography.model_validate_json(l)
        for l in (Path(DD) / "biographies" / "biographies.jsonl").open(encoding="utf-8")]
# NOTE: do NOT apply_recovered_places — we want the raw placeless events.

out = Path(DD) / "graph_cache"
aug = out / "officials_augmented.jsonl"
src = aug if (os.environ.get("COL_USE_AUGMENTED") == "1" and aug.exists()) else out / "officials.jsonl"
officials = [json.loads(l) for l in src.open(encoding="utf-8")]
idx = _build_record_index(officials)

linked = set()
for fn in ("stint_matches.jsonl", "record_attachments.jsonl"):
    p = Path(DD) / "matches" / fn
    if p.exists():
        for l in p.open(encoding="utf-8"):
            linked.add(json.loads(l)["bio_id"])

buckets = Counter()
bios_with_norec_strong = set()
for bio in bios:
    if bio.bio_id in linked:
        continue
    sn = _skey(bio.surname)
    if not sn:
        continue
    own = _placed_colonies(bio, DD)
    for ev in bio.events:
        if ev.place or ev.year_start is None or not ev.position or len(ev.position) <= 4:
            continue
        yr = ev.year_start
        cand = [r for y in range(yr - WINDOW, yr + WINDOW + 1)
                for r in idx.get((sn, y), ())
                if _initials_compatible(bio.given_names, r["given"])]
        if not cand:
            buckets["no_record"] += 1
            bios_with_norec_strong.add(bio.bio_id)
            continue
        colonies = {r["colony_norm"] for r in cand}
        if len(colonies) != 1:
            if len(colonies & own) == 1:
                buckets["multi_resolved_own"] += 1
            else:
                buckets["multi_colony"] += 1
            continue
        pos = max(fuzz.token_set_ratio(_pos_norm(ev.position), _pos_norm(r["position"]))
                  for r in cand)
        buckets["single_low_pos" if pos < 60 else "single_ok"] += 1

print("placeless STRONG-position events on UNMATCHED bios, by Tier-A outcome:")
for k, v in buckets.most_common():
    print(f"  {k:22s} {v}")
print(f"\nunmatched bios with >=1 no_record strong placeless event: {len(bios_with_norec_strong)}")
