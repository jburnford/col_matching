#!/usr/bin/env python3
"""Ground the honour grades both corpora were internal-minting or folding to
the parent order (review C21): per-grade Wikidata items for the Royal
Victorian Order / Star of India / Indian Empire, the Volunteer Officers'
Decoration, the French and Belgian Croix de Guerre variants and the
Kaisar-i-Hind Medal classes. Rows are keyed by the honour BASE as
kg_honour_norm.parse_honour produces it (kg_emit_honours nrm()); every QID
was verified on QLever (P31 grade-of-an-order / award). Idempotent.
Run:  python3 kg_patch_honour_cache.py   then kg_emit_honours.py + kg_dedup_nodes.py per corpus
"""
import json
from pathlib import Path

ROWS = {
    "mvo":  ("Q12193926", "Member of the Royal Victorian Order"),
    "kcvo": ("Q12192712", "Knight Commander of the Royal Victorian Order"),
    "cie":  ("Q16008317", "Companion of the Order of the Indian Empire"),
    "kcie": ("Q16008267", "Knight Commander of the Order of the Indian Empire"),
    "gcie": ("Q16006972", "Knight Grand Commander of the Order of the Indian Empire"),
    "csi":  ("Q14947476", "Companion of the Order of the Star of India"),
    "kcsi": ("Q14947473", "Knight Commander of the Order of the Star of India"),
    "gcsi": ("Q14947472", "Knight Grand Commander of the Order of the Star of India"),
    "vd":   ("Q20982076", "Volunteer Officers' Decoration"),
    "croix de guerre": ("Q869896", "Croix de Guerre (France)"),
    "croix-de-guerre": ("Q869896", "Croix de Guerre (France)"),
    "french croix de guerre": ("Q869896", "Croix de Guerre (France)"),
    "croix de guerre avec palme": ("Q869896", "Croix de Guerre (France)"),
    "croix de guerre with palm": ("Q869896", "Croix de Guerre (France)"),
    "croix de guerre with palm leaves": ("Q869896", "Croix de Guerre (France)"),
    "croix de guerre with palms": ("Q869896", "Croix de Guerre (France)"),
    "croix de guerre, 1940, avec palme": ("Q869896", "Croix de Guerre (France)"),
    "belgian croix de guerre": ("Q48915", "Croix de Guerre (Belgium)"),
    "croix de guerre (belgium)": ("Q48915", "Croix de Guerre (Belgium)"),
    "kaisar-i-hind": ("Q2423226", "Kaisar-i-Hind Medal"),
    "kaisar-i-hind medal": ("Q2423226", "Kaisar-i-Hind Medal"),
    "kaisar-i-hind medal, 1st class": ("Q2423226", "Kaisar-i-Hind Medal"),
    "kaisar-i-hind medal, 2nd class": ("Q2423226", "Kaisar-i-Hind Medal"),
    "kaisar-i-hind medal, 3rd class": ("Q2423226", "Kaisar-i-Hind Medal"),
    "kaisar-i-hind gold medal": ("Q2423226", "Kaisar-i-Hind Medal"),
    "kaisar-i-hind silver medal": ("Q2423226", "Kaisar-i-Hind Medal"),
    "kaisar i hind": ("Q2423226", "Kaisar-i-Hind Medal"),
    "kaisar i hind medal": ("Q2423226", "Kaisar-i-Hind Medal"),
}
TYPE = {"croix": "decoration", "kaisar": "medal", "vd": "decoration"}


def main():
    for cache in (Path("data/kg/honour_grounding.jsonl"), Path("data/iol/honour_grounding.jsonl")):
        rows = [json.loads(l) for l in cache.open(encoding="utf-8")]
        by = {r["institution"].casefold(): r for r in rows}
        n_new = n_upd = 0
        for key, (qid, label) in ROWS.items():
            typ = next((t for k, t in TYPE.items() if key.startswith(k)), "order")
            r = by.get(key)
            if r is None:
                rows.append({"institution": key, "type": typ, "id": qid, "label": label, "instance_of": [],
                             "country_qid": "Q145", "source": "curated", "match_type": "qlever_verified_2026-09-04"})
                n_new += 1
            elif r["id"] != qid:
                r.update(id=qid, label=label, source="curated", match_type="qlever_verified_2026-09-04"); n_upd += 1
        with cache.open("w", encoding="utf-8") as fh:
            for r in rows:
                fh.write(json.dumps(r, ensure_ascii=False) + "\n")
        print(f"{cache}: +{n_new} new, {n_upd} regrounded")


if __name__ == "__main__":
    main()
