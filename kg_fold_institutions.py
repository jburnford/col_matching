#!/usr/bin/env python3
"""Zero-MCP reuse-fold pass for the institution grounding loop.

Many worklist surfaces are spelling/abbreviation/case variants of an institution
ALREADY in the cache (seed or freshly-grounded) under a different surface or its
label. This finds pending worklist surfaces whose NORMALISED form matches exactly
one cached entity and emits a `reuse` batch for `kg_ground_institutions.py record`
— no MCP call. Re-run after every MCP batch to sweep up the new variants.

Env (same as kg_ground_institutions.py):
  COL_WORK   education_worklist.jsonl   COL_CACHE  institutions_grounding.jsonl

  COL_WORK=data/iol/education_worklist.jsonl COL_CACHE=data/iol/institutions_grounding.jsonl \
    python3 kg_fold_institutions.py --out data/iol/inst_folds_NNN.jsonl
  # then:
  COL_KG_OUT=data/iol python3 kg_ground_institutions.py record data/iol/inst_folds_NNN.jsonl

NOTE: institution identity keeps College/School/University (NOT stripped — they
distinguish "X College" from "X School"); only case/punctuation/abbreviation and
the joiners the/of/at/and are normalised. norm-collisions (one form -> >1 entity)
are skipped, never guessed.
"""
from __future__ import annotations
import json, os, re, sys, unicodedata
from collections import defaultdict

WORK = os.environ.get("COL_WORK", "data/kg/education_worklist.jsonl")
CACHE = os.environ.get("COL_CACHE", "data/kg/institutions_grounding.jsonl")
OUT = sys.argv[sys.argv.index("--out") + 1] if "--out" in sys.argv else "inst_folds_batch.jsonl"

def _acc(s): return "".join(c for c in unicodedata.normalize("NFKD", s) if not unicodedata.combining(c))
def norm(s):
    s = _acc((s or "").lower())
    s = re.sub(r"[._,()'’`]", " ", s)
    s = re.sub(r"\bcoll?\b", "college", s); s = re.sub(r"\bunivs?\b", "university", s)
    s = re.sub(r"\bschl?\b", "school", s);  s = re.sub(r"\binst\b", "institute", s)
    s = re.sub(r"\bacad\b", "academy", s);  s = re.sub(r"\bgr\b", "grammar", s)
    s = re.sub(r"\b(the|of|at|and)\b", " ", s)
    return re.sub(r"\s+", " ", s).strip()

cache = [json.loads(l) for l in open(CACHE)]
norm2id, id_label = defaultdict(set), {}
for r in cache:
    i = r.get("id")
    if not i:
        continue
    id_label[i] = r.get("label") or r.get("institution")
    for s in (r.get("institution"), r.get("label")):
        if s:
            norm2id[norm(s)].add(i)
cached_surf = {r["institution"] for r in cache}

work = [json.loads(l) for l in open(WORK)]
wtype = {w["institution"]: w.get("type", "other") for w in work}
folds, collisions = [], 0
for w in work:
    inst = w["institution"]
    if inst in cached_surf:
        continue
    ids = norm2id.get(norm(inst), set())
    if len(ids) == 1:
        i = next(iter(ids))
        folds.append((w["count"], inst, i))
    elif len(ids) > 1:
        collisions += 1
folds.sort(key=lambda x: -x[0])

with open(OUT, "w") as f:
    for _, inst, i in folds:
        f.write(json.dumps({"institution": inst, "type": wtype.get(inst, "other"),
                            "id": i, "label": id_label.get(i, inst), "instance_of": [],
                            "country_qid": None, "source": "reuse",
                            "match_type": "reuse_variant"}, ensure_ascii=False) + "\n")

mentions = sum(c for c, _, _ in folds)
print(f"fold candidates: {len(folds)}  ({mentions:,} mentions)  | norm-collisions skipped: {collisions}")
for c, inst, i in folds[:20]:
    print(f"  {c:5d}  {inst!r:45s} -> {i} {id_label.get(i,'')}")
print(f"\nwrote -> {OUT}\nrecord:  COL_KG_OUT=... python3 kg_ground_institutions.py record {OUT}")
