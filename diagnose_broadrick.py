#!/usr/bin/env python3
"""Diagnose why E. G. Broadrick's biographies don't match his Straits
Settlements records. Tests two hypotheses:
  1. granular place names (Penang, Singapore, Province Wellesley, Malacca,
     Dindings) don't roll up to 'Straits Settlements' in the gazetteer, so the
     matcher sees colony disagreement on every clause;
  2. the person is split into two biographies (EDW. GEO. / EDWD. GEO.).

Run from the repo root:  python3 diagnose_broadrick.py
"""
import json
from pathlib import Path

from col_match.services import gazetteer as g

DD = "data/services"


def main() -> None:
    print("=== H1: gazetteer.colony_targets for Straits/Malaya places ===")
    print("    (a match needs the bio place to resolve to the record colony "
          "'straitssettlements')")
    for p in ["Straits Settlements", "Penang", "Province Wellesley", "Malacca",
              "Singapore", "Dindings", "Prince of Wales Island", "Selangor",
              "Federated Malay States"]:
        tgt = sorted(g.colony_targets(p, DD))
        flag = "  <-- does NOT roll up to Straits Settlements" if (
            "straitssettlements" not in tgt and p != "Straits Settlements"
            and p not in ("Selangor", "Federated Malay States")) else ""
        print(f"  {p:28s} -> {tgt}{flag}")

    print("\n=== H2: Broadrick biographies (are there two for one man?) ===")
    for line in Path(f"{DD}/biographies/biographies.jsonl").open(encoding="utf-8"):
        d = json.loads(line)
        if d["surname"].upper().startswith("BROADRICK"):
            places = sorted({e.get("place") for e in d["events"] if e.get("place")})
            print(f"  bio_id={d['bio_id']}")
            print(f"     given={d.get('given_names')!r}  editions={d.get('editions')}")
            print(f"     placed-event places: {places}")

    print("\n=== Broadrick officials / records in the graph ===")
    for line in Path(f"{DD}/graph_cache/officials.jsonl").open(encoding="utf-8"):
        o = json.loads(line)
        if o["name"].upper().startswith("BROADRICK"):
            yrs = sorted({r["year"] for r in o["records"]})
            pos = sorted({r.get("position_raw") for r in o["records"] if r.get("position_raw")})
            print(f"  id={o['id']}")
            print(f"     colony={o['colony']}  years={yrs}")
            print(f"     positions: {pos[:8]}")


if __name__ == "__main__":
    main()
