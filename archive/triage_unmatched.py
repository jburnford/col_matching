#!/usr/bin/env python3
"""Bucket every UNMATCHED biography by *why* it didn't match — the quantified
answer to "we pull bios and staff lists from the same documents, so why isn't
match rate ~100%?". Each unmatched bio falls into exactly one bucket:

  parse_truncation        raw entry has >=5 years but parse kept <=2 events
                          (career lost in parsing)            [Brockman]
  no_placed_colonial      no dated event resolves to any colony (military /
                          London / education / pre-coverage — not in the
                          colonial staff lists by construction)
  no_surname_record       no official with this surname in the graph at all
  surname_diff_person     surname present but no initial-compatible official
                          (only other people of that surname were extracted —
                          this person's rows were never captured)  [Brooke]
  colony_mismatch         an initial-compatible same-surname official exists but
                          its colony matches none of the bio's event colonies —
                          usually granular places that don't roll up [Broadrick]
  matcher_rejected        record + colony agree, yet no link — position fuzz /
                          ambiguity guard / tenure (the conservative matcher)

Run from the repo root:  python3 triage_unmatched.py
"""
import glob
import json
import re
from collections import Counter, defaultdict
from pathlib import Path

from col_match.services import gazetteer as g

DD = Path("data/services")
YEAR = re.compile(r"\b(1[789]\d\d)\b")
SKEY = re.compile(r"[^a-z0-9]")


def skey(s):
    return SKEY.sub("", (s or "").lower())


def initials(given):
    return [t[0].upper() for t in re.split(r"[ .]+", given or "") if t and t[0].isalpha()]


def initials_compatible(a, b):
    ia, ib = initials(a), initials(b)
    if not ia or not ib:
        return True
    short, long_ = (ia, ib) if len(ia) <= len(ib) else (ib, ia)
    i = 0
    for x in long_:
        if i < len(short) and short[i] == x:
            i += 1
    return i == len(short)


def main():
    # matched bios
    matched = set()
    for fn in ("matches/record_attachments.jsonl", "matches/stint_matches.jsonl"):
        p = DD / fn
        if p.exists():
            for line in p.open(encoding="utf-8"):
                if line.strip():
                    matched.add(json.loads(line)["bio_id"])

    # official index by surname
    off_by_sur = defaultdict(list)
    for line in (DD / "graph_cache" / "officials.jsonl").open(encoding="utf-8"):
        o = json.loads(line)
        name = o.get("name") or ""
        sur = skey(name.split(",")[0])
        given = name.split(",", 1)[1] if "," in name else ""
        off_by_sur[sur].append({"colony": g.norm(o.get("colony") or ""), "given": given})

    # raw entry text
    raw = {}
    for p in glob.glob(str(DD / "raw_entries" / "*.jsonl")):
        for line in open(p, encoding="utf-8"):
            d = json.loads(line)
            raw[d["entry_id"]] = d.get("raw_text", "")

    def raw_text(bio):
        best = ""
        for vid in bio.get("version_ids", []):
            eid = vid[:-2] if vid.endswith(".v") else vid
            t = raw.get(eid, "")
            if len(t) > len(best):
                best = t
        return best

    buckets = Counter()
    examples = defaultdict(list)
    n_total = n_unmatched = 0
    for line in (DD / "biographies" / "biographies.jsonl").open(encoding="utf-8"):
        d = json.loads(line)
        n_total += 1
        if d["bio_id"] in matched:
            continue
        n_unmatched += 1
        sur = skey(d["surname"])
        events = d.get("events", [])
        ry = len(set(YEAR.findall(raw_text(d))))
        # colonies the bio's placed+dated events resolve to
        ev_colonies = set()
        for e in events:
            if e.get("place") and e.get("year_start") is not None:
                ev_colonies |= g.colony_targets(e["place"], str(DD))
        same = off_by_sur.get(sur, [])
        compat = [o for o in same if initials_compatible(d.get("given_names"), o["given"])]
        compat_colonies = {o["colony"] for o in compat}

        if ry >= 5 and len(events) <= 2:
            b = "parse_truncation"
        elif not ev_colonies:
            b = "no_placed_colonial"
        elif not same:
            b = "no_surname_record"
        elif not compat:
            b = "surname_diff_person"
        elif not (ev_colonies & compat_colonies):
            b = "colony_mismatch"
        else:
            b = "matcher_rejected"
        buckets[b] += 1
        if len(examples[b]) < 6:
            examples[b].append(f"{d['surname']}, {d.get('given_names')} "
                               f"(events={len(events)}, raw_years={ry})")

    print(f"biographies: {n_total:,};  unmatched: {n_unmatched:,} "
          f"({n_unmatched*100//n_total}%)\n")
    print("=== why unmatched biographies don't match ===")
    order = ["no_surname_record", "surname_diff_person", "no_placed_colonial",
             "colony_mismatch", "parse_truncation", "matcher_rejected"]
    for b in order:
        n = buckets.get(b, 0)
        print(f"  {b:22s} {n:6,}  ({n*100//max(n_unmatched,1)}%)")
        for ex in examples.get(b, []):
            print(f"        e.g. {ex}")
    print("\nNote: buckets are heuristic (coarse colony/initial checks, no tenure). "
          "no_surname_record + surname_diff_person ~= 'this person's rows are not in "
          "the graph' (extraction gap or genuinely not in colonial service).")


if __name__ == "__main__":
    main()
