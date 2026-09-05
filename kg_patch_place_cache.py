#!/usr/bin/env python3
"""Apply data/kg/place_qid_patches.json (curated old-QID -> new-QID corrections)
to BOTH corpora's places_grounding.jsonl. Idempotent: rows already on the new
QID are untouched; a patched row records `patched_from` + the patch reason so
the correction survives cache reuse (the caches are the grounding memory the
spine emit reads — kg_join_manifest / kg_ground_mcp only touch UNGROUNDED
surfaces, so a wrong cached QID persists until rewritten here).

Run:  python3 kg_patch_place_cache.py            # then re-emit both spines
"""
import json
from pathlib import Path

PATCHES = Path("data/kg/place_qid_patches.json")
CACHES = [Path("data/kg/places_grounding.jsonl"), Path("data/iol/places_grounding.jsonl")]


def main():
    patches = {p["old"]: p for p in json.loads(PATCHES.read_text())["patches"]}
    for cache in CACHES:
        rows = [json.loads(l) for l in cache.open(encoding="utf-8")]
        n = 0
        for r in rows:
            p = patches.get(r.get("qid"))
            if not p:
                continue
            r["patched_from"] = r["qid"]
            r["qid"], r["label"] = p["new"], p["label"]
            r["match_type"] = "curated_patch"
            r["patch_reason"] = p["why"]
            r["has_coords"] = True          # every target verified on QLever to carry P625
            n += 1
        with cache.open("w", encoding="utf-8") as fh:
            for r in rows:
                fh.write(json.dumps(r, ensure_ascii=False) + "\n")
        print(f"{cache}: {n} rows patched")


if __name__ == "__main__":
    main()
