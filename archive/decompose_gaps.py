#!/usr/bin/env python3
"""Two questions:
 (1) Is 'no_placed_colonial' really a structural ceiling, or addressable?
     Decompose it into sub-reasons.
 (2) Which printed places in biographies resolve to a colony that has NO
     records (orphan places)? Those are the gazetteer roll-up gaps to fix
     (e.g. Singapore/Penang/Malacca -> Straits Settlements).

Run from the repo root:  python3 decompose_gaps.py
"""
import json
import re
from collections import Counter
from pathlib import Path

from col_match.services import gazetteer as g

DD = Path("data/services")
YEAR = re.compile(r"\b(1[789]\d\d)\b")

COLONIAL = re.compile(
    r"magistrate|secretary|\boffr\b|officer|auditor|registrar|collector|collr|"
    r"commissioner|comm\b|governor|\bjudge\b|treasurer|clerk|inspector|"
    r"superintendent|supt|resident|police|customs|cadet|district|\bdist\b|"
    r"protector|surveyor|postmaster|chief|director|warden|attorney|advocate|"
    r"medical|health|land rev|public works|p\.w\.|colonial", re.I)
MILITARY = re.compile(r"\bR\.[AEN]\.|lieut|capt|colonel|\bcol\.|major|brevet|"
                      r"regiment|brigade|artillery|infantry|cavalry|\bgen\.", re.I)
EDU = re.compile(r"\bB\.A\b|\bM\.A\b|\bed\.|college|school|called to the bar|"
                 r"inns? of court|matric|scholar|exhibition|passed", re.I)


def main():
    # record colonies present in the graph
    rec_colonies = set()
    for line in (DD / "graph_cache" / "officials.jsonl").open(encoding="utf-8"):
        rec_colonies.add(g.norm(json.loads(line).get("colony") or ""))
    rec_colonies.discard("")

    matched = set()
    for fn in ("matches/record_attachments.jsonl", "matches/stint_matches.jsonl"):
        p = DD / fn
        if p.exists():
            for line in p.open(encoding="utf-8"):
                if line.strip():
                    matched.add(json.loads(line)["bio_id"])

    raw = {}
    import glob
    for p in glob.glob(str(DD / "raw_entries" / "*.jsonl")):
        for line in open(p, encoding="utf-8"):
            d = json.loads(line)
            raw[d["entry_id"]] = d.get("raw_text", "")

    def raw_years(bio):
        best = ""
        for vid in bio.get("version_ids", []):
            eid = vid[:-2] if vid.endswith(".v") else vid
            t = raw.get(eid, "")
            if len(t) > len(best):
                best = t
        return len(set(YEAR.findall(best)))

    sub = Counter()
    orphan_places = Counter()       # place -> count (resolves to a colony with no records)
    orphan_place_bios = Counter()
    sub_examples = {}

    n_bucket = 0
    for line in (DD / "biographies" / "biographies.jsonl").open(encoding="utf-8"):
        d = json.loads(line)
        if d["bio_id"] in matched:
            continue
        events = d.get("events", [])
        # ev_colonies exactly as triage computed
        ev_colonies = set()
        for e in events:
            if e.get("place") and e.get("year_start") is not None:
                ev_colonies |= g.colony_targets(e["place"], str(DD))
        ry = raw_years(d)
        if ry >= 5 and len(events) <= 2:
            continue  # parse_truncation
        if ev_colonies:
            # not in the no_placed bucket — but still useful for orphan-place scan
            for e in events:
                pl = e.get("place")
                if pl:
                    tgt = g.colony_targets(pl, str(DD))
                    if tgt and not (tgt & rec_colonies):
                        orphan_places[pl] += 1
            continue

        # --- inside no_placed_colonial bucket ---
        n_bucket += 1
        positions = " | ".join((e.get("position") or "") for e in events)
        placed_any = [e for e in events if e.get("place")]
        placed_dated = [e for e in events if e.get("place") and e.get("year_start") is not None]
        # places present but unresolved by gazetteer
        garbled = [e for e in placed_any if not g.colony_targets(e["place"], str(DD))]
        placeless_colonial = [e for e in events
                              if not e.get("place") and e.get("year_start") is not None
                              and COLONIAL.search(e.get("position") or "")]

        if placed_dated:
            reason = "has_resolved_place_but_undated_or_other"  # shouldn't happen
        elif garbled:
            reason = "place_present_unresolved_by_gazetteer"
            for e in garbled:
                orphan_places[e["place"]] += 1
        elif placeless_colonial:
            reason = "placeless_colonial_clause (TierA/B / colony-dropped)"
        elif placed_any:
            reason = "placed_but_undated"
        elif COLONIAL.search(positions) and not MILITARY.search(positions):
            reason = "colonial_role_no_place_anywhere"
        elif MILITARY.search(positions) or EDU.search(positions):
            reason = "military/education only (structural)"
        else:
            reason = "sparse/other"
        sub[reason] += 1
        if reason not in sub_examples:
            sub_examples[reason] = []
        if len(sub_examples[reason]) < 5:
            sub_examples[reason].append(
                f"{d['surname']}, {d.get('given_names')} (events={len(events)}, "
                f"raw_years={ry}) pos=[{positions[:90]}]")

    print(f"=== (1) decompose no_placed_colonial ({n_bucket:,} bios) ===")
    for r, n in sub.most_common():
        print(f"  {n:6,}  {r}")
        for ex in sub_examples.get(r, [])[:3]:
            print(f"          {ex}")

    print(f"\n=== (2) orphan places: appear in bios, resolve to a colony with NO records ===")
    print("    (these are the gazetteer roll-up gaps — map each to its parent colony)")
    for pl, n in orphan_places.most_common(30):
        tgt = sorted(g.colony_targets(pl, str(DD)))
        print(f"  {n:5,}  {pl!r:34s} -> {tgt}")


if __name__ == "__main__":
    main()
