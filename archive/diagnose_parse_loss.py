#!/usr/bin/env python3
"""Quantify parse truncation: biographies whose RAW OCR entry contains many
career years but whose PARSED bio kept almost no events. The E. L. Brockman
case (a ~30-clause Malayan career parsed down to one 'Cadet, 1886' event)
suggests OCR-garbled dense entries are being dropped.

Method: for each biography, take its source raw entry text (via its version
lead entry ids), count distinct 4-digit years (a proxy for # career clauses),
and compare to the number of parsed events. A big gap = lost career.

Run from the repo root:  python3 diagnose_parse_loss.py
"""
import glob
import json
import re
from pathlib import Path

DD = Path("data/services")
YEAR = re.compile(r"\b(1[789]\d\d)\b")


def load_raw_entries() -> dict[str, str]:
    by_id: dict[str, str] = {}
    for p in glob.glob(str(DD / "raw_entries" / "*.jsonl")):
        with open(p, encoding="utf-8") as fh:
            for line in fh:
                d = json.loads(line)
                by_id[d["entry_id"]] = d.get("raw_text", "")
    return by_id


def load_matched_bio_ids() -> set[str]:
    matched: set[str] = set()
    for fn in ("matches/record_attachments.jsonl", "matches/stint_matches.jsonl"):
        p = DD / fn
        if p.exists():
            for line in p.open(encoding="utf-8"):
                if line.strip():
                    matched.add(json.loads(line)["bio_id"])
    return matched


def raw_text_for(bio: dict, by_id: dict[str, str]) -> str:
    """Longest source raw text among the bio's version lead entries."""
    best = ""
    for vid in bio.get("version_ids", []):
        eid = vid[:-2] if vid.endswith(".v") else vid
        txt = by_id.get(eid, "")
        if len(txt) > len(best):
            best = txt
    return best


def main() -> None:
    by_id = load_raw_entries()
    matched = load_matched_bio_ids()
    print(f"raw entries indexed: {len(by_id):,};  matched bios: {len(matched):,}\n")

    truncated = []           # (gap, raw_years, n_events, bio_id, surname, given, is_matched)
    n_total = 0
    for line in (DD / "biographies" / "biographies.jsonl").open(encoding="utf-8"):
        d = json.loads(line)
        n_total += 1
        txt = raw_text_for(d, by_id)
        raw_years = len(set(YEAR.findall(txt)))
        n_events = len(d.get("events", []))
        # truncation signal: source mentions >=5 distinct years, parse kept <=2 events
        if raw_years >= 5 and n_events <= 2:
            truncated.append((raw_years - n_events, raw_years, n_events,
                              d["bio_id"], d["surname"], d.get("given_names"),
                              d["bio_id"] in matched))

    truncated.sort(reverse=True)
    n_unmatched = sum(1 for t in truncated if not t[6])
    print(f"=== parse-truncation casualties (raw years>=5, parsed events<=2) ===")
    print(f"  {len(truncated):,} of {n_total:,} biographies "
          f"({len(truncated)*100//max(n_total,1)}%) — of which {n_unmatched:,} are UNMATCHED\n")
    print("  worst 25 (raw_years -> parsed_events):")
    for gap, ry, ne, bid, sur, giv, m in truncated[:25]:
        print(f"    {ry:2d}y -> {ne} ev  {'MATCHED ' if m else 'unmatched'}  "
              f"{sur}, {giv}  [{bid}]")

    print("\n=== Brockman detail ===")
    for line in (DD / "biographies" / "biographies.jsonl").open(encoding="utf-8"):
        d = json.loads(line)
        if d["surname"].upper().startswith("BROCKMAN"):
            txt = raw_text_for(d, by_id)
            print(f"  {d['bio_id']}  given={d.get('given_names')!r}")
            print(f"     version_ids={d.get('version_ids')}  flags={d.get('flags')}")
            print(f"     parsed events={len(d['events'])}; raw distinct years="
                  f"{len(set(YEAR.findall(txt)))}")
            print(f"     parsed events: {[ (e.get('position'), e.get('place'), e.get('year_start')) for e in d['events'] ]}")
            print(f"     raw text (first 400 chars): {txt[:400]!r}")


if __name__ == "__main__":
    main()
