#!/usr/bin/env python3
"""Re-ground already-cached COLONY place surfaces to the foundational empire KG.

Background (KG_FIXES #1): pre-federation colonies must use the colonial-era entity
(Victoria the *colony* Q56850459), not the modern state/nation (Victoria the
*state of Australia* Q36687). The CO corpus mostly joined the empire-evolution
manifest correctly; the IOL corpus did NOT (its colonies are pre-grounded seed
rows -> modern states). `kg_join_manifest.py` only touches the worklist (still-
ungrounded surfaces); these are pre-grounded cache rows, so we rewrite the cache.

Rule (Jim, 2026-06-27): per surface, pick the PERIOD-CORRECT, PLACE-TYPED entity.
- DEFAULT: the manifest's single era-OK QID for that name (the colonial entity).
- OVERRIDE: where the manifest itself is wrong (the manifest has 117 self-flagged
  QIDs in wikidata_qid_issues.csv). Verified cases hard-coded below:
    * India / British India -> Q129286 (British Raj 1858-1947), NOT the manifest's
      Q1775277 (Dominion of India, 1947).
    * Egypt -> keep modern country Q79: the manifest's Q2474428 is "Egyptian
      history under the British" (an aspect-of-history, NOT a place; won't geocode).
    * Cape Colony -> keep Q370736 (the clean colony entity both corpora already
      share); the manifest's Q4806993 is self-flagged QID_REUSED.
    * Udaipur -> Q130642141 (princely state); the manifest's other candidate
      Q1457519 is self-flagged POSSIBLE_FILE_DUPLICATE.
- GUARD: never write a NON_PLACE target (only Q2474428 in this set).
- Multi-QID manifest names with no override -> skipped (left for review).

Env: COL_KG_OUT selects the corpus (data/kg = CO default, data/iol = IOL).
Usage:  COL_KG_OUT=data/iol python3 kg_reground_colonies.py            # preview
        COL_KG_OUT=data/iol python3 kg_reground_colonies.py --apply    # write
"""
from __future__ import annotations

import argparse
import csv
import json
import re
from collections import Counter, defaultdict
from pathlib import Path

from col_match.kg.paths import KG_OUT

MANIFEST = Path("/home/jic823/empire-evolution-wpcs/data/qid_manifest.tsv")
CACHE = KG_OUT / "places_grounding.jsonl"
EVENTS = KG_OUT / "graph_stage3" / "career_events.jsonl"

_TYPE = re.compile(
    r"\b(colony|colonial|protectorate|crown|settlement|settlements|dominion|"
    r"territory|territories|province|of|and|the|british|presidency|state|company)\b")

# Manifest is wrong / a non-place for these surfaces -> explicit period-correct pick.
# Keyed by stripped surface name.
OVERRIDE = {
    "india": "Q129286",            # British Raj, not Dominion of India Q1775277
    "british india": "Q129286",
    "egypt": "Q127861",            # Khedivate of Egypt (Cairo); manifest Q2474428 was
                                   # "Egyptian history under the British" (non-place), now patched
    "cape": "Q370736",             # clean colony entity; manifest Q4806993 self-flagged
    "cape prov": "Q370736",        # "Cape Prov." abbrev not normalised by strip_type
    "udaipur": "Q130642141",       # princely state; manifest Q1457519 = file dup
}
NON_PLACE = {"Q2474428"}           # verified non-geographic targets to never write

# Surfaces where the manifest strip-match picks the WRONG referent for THIS corpus
# (verified via Wikidata). Keep the cached QID, do not re-ground.
#  - city/district names colliding with a tiny same-named princely state
#  - states ANNEXED before the corpus era (became British districts/provinces)
#  - "South Africa" -> BSAC/Rhodesia; "New York" -> 1664 colonial province
KEEP_CACHED = {
    "south africa", "new york",
    "patna", "surat", "benares", "banda",           # British-India cities, not states
    "satara", "oudh", "jhansi", "carnatic", "jalaun",  # annexed pre-corpus (1848/1856/1854/1801/1840)
    "shahpur", "narsinghpur", "rajkot",             # district/agency-HQ-vs-tiny-state ambiguity
}


def _norm(s: str) -> str:
    return re.sub(r"\s+", " ", re.sub(r"[^a-z0-9 ]", " ", (s or "").lower())).strip()


def _strip_type(s: str) -> str:
    return re.sub(r"\s+", " ", _TYPE.sub(" ", _norm(s))).strip()


def _era_ok(r) -> bool:
    try:
        est = int(r["established_year"])
    except Exception:
        est = 1700
    end = 2000
    m = re.match(r"(\d{4})", r.get("end_date", "") or "")
    if m:
        end = int(m.group(1))
    return est <= 1965 and end >= 1850


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true")
    args = ap.parse_args()

    rows = list(csv.DictReader(MANIFEST.open(encoding="utf-8"), delimiter="\t"))
    by_qid = {r["wikidata_id"]: r for r in rows if r["wikidata_id"]}
    idx = defaultdict(list)
    for r in rows:
        for k in (r["name"], r["canonical_name"]):
            if k:
                idx[_strip_type(k)].append(r)

    cache = [json.loads(l) for l in CACHE.open(encoding="utf-8") if l.strip()]
    evc = Counter()
    if EVENTS.exists():
        for l in EVENTS.open(encoding="utf-8"):
            q = json.loads(l).get("place_qid")
            if q:
                evc[q] += 1

    changes = []
    skips = []
    for r in cache:
        surface = r.get("place", "")
        key = _strip_type(surface)
        cached_qid = r.get("qid")
        if not cached_qid:
            continue
        if key in KEEP_CACHED:
            continue
        # decide target
        if key in OVERRIDE:
            target = OVERRIDE[key]
            reason = "override"
        else:
            cands = idx.get(key)
            if not cands:
                continue
            pool = [c for c in cands if _era_ok(c)] or cands
            qids = sorted({c["wikidata_id"] for c in pool if c["wikidata_id"]})
            if len(qids) != 1:
                if cached_qid not in qids and qids:
                    skips.append((surface, cached_qid, qids, "multi-qid manifest"))
                continue
            target = qids[0]
            reason = "manifest"
        if target is None or target == cached_qid:
            continue
        if target in NON_PLACE:
            skips.append((surface, cached_qid, [target], "non-place target"))
            continue
        minfo = by_qid.get(target, {})
        label = minfo.get("name") or minfo.get("canonical_name") or r.get("label")
        changes.append({
            "row": r, "surface": surface, "old": cached_qid, "new": target,
            "label": label, "ev": evc.get(cached_qid, 0), "reason": reason,
            "country": (minfo.get("modern_nation_qids", "") or "").split(";")[0] or None,
            "ctype": minfo.get("colony_type"),
        })

    changes.sort(key=lambda c: -c["ev"])
    print(f"# corpus={KG_OUT}  cache_rows={len(cache)}  changes={len(changes)}  skips={len(skips)}")
    print(f"# {'surface':26}{'ev':>6}  {'old':>12} -> {'new':<12} {'reason':10} label")
    for c in changes:
        print(f"  {c['surface'][:26]:26}{c['ev']:6}  {c['old']:>12} -> {c['new']:<12} "
              f"{c['reason']:10} {c['label']}")
    if skips:
        print(f"\n# SKIPPED ({len(skips)}):")
        for s, cq, qs, why in skips:
            print(f"  {s[:30]:30} cached={cq} manifest={qs} ({why})")
    print(f"\n# total events repointed: {sum(c['ev'] for c in changes)}")

    if args.apply:
        for c in changes:
            r = c["row"]
            r["qid"] = c["new"]
            r["label"] = c["label"]
            r["country_qid"] = c["country"]
            r["instance_of"] = [c["ctype"]] if c["ctype"] else r.get("instance_of", [])
            r["match_type"] = "manifest_reground"
        with CACHE.open("w", encoding="utf-8") as fh:
            for r in cache:
                fh.write(json.dumps(r, ensure_ascii=False) + "\n")
        print(f"\nAPPLIED -> {CACHE}")


if __name__ == "__main__":
    main()
