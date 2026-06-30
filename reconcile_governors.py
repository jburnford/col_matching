#!/usr/bin/env python3
"""reconcile_governors.py — pass 2: flag bio governorship YEARS that disagree
with the governors-table appointment year for the same (colony, surname).

The governors table is structured, independent of the free-text bio, and
repeated across editions, so where they conflict the table is authoritative.
Output: data/kg/governor_year_flags.jsonl — candidates for the corrections
overlay, each with the person, colony, the bad bio year and the table year.
"""
import json, re, collections
from pathlib import Path
import build_static_atlas as B   # reuse build_canon + paths

ROOT = Path(__file__).resolve().parent
PL = json.load(open(ROOT / "docs" / "data" / "places.json"))

HONORIFIC = re.compile(r"^(sir|hon|the|rt|right|lord|lady|major|maj|capt|captain|col|colonel|lt|lieut|"
                       r"general|gen|brig|brigadier|admiral|adm|dr|rev|hon'ble|honble|viscount|earl|baron|"
                       r"marquess|marquis|duke|count|mr|sir\.?)\.?$", re.I)

def name_parts(raw):
    """From 'Brig.-Gen. Sir F. Gordon Guggisberg, K.C.M.G.' return
    (surname='GUGGISBERG', given_initials={'F','G'})."""
    s = re.sub(r"\(.*?\)", "", raw)              # drop (Acting Governor) etc.
    s = s.split(",")[0]                          # name is before the post-nominals
    s = re.sub(r"[^A-Za-z'\-. ]", " ", s)
    toks = [t for t in re.split(r"\s+", s) if t]
    toks = [t for t in toks if not HONORIFIC.match(t.strip("."))]
    sur = ""
    for t in reversed(toks):
        if len(t.strip(".")) <= 1: continue
        sur = t.upper().replace("'", ""); break
    if not sur and toks: sur = toks[-1].upper()
    inits = {t.strip(".")[0].upper() for t in toks if t.strip(".") and t.upper() != sur}
    return sur, inits

def surname_key(raw):
    return name_parts(raw)[0]

# match the GROUNDED role being a substantive governorship — anchored, and never
# a "(private) secretary/aide/clerk TO the governor", which merely names one.
GOV_ROLE = re.compile(r"^(governor(-?\s?general)?|lieutenant[- ]?governor|administrator|high commissioner)\b", re.I)
NOT_GOV = re.compile(r"secretary|aide|clerk|\bto\b|assistant|deputy|officer", re.I)

ACTING = re.compile(r"acting|administrator|lieut|lt\.?-?gov|officer admin|deputy", re.I)

def load_table_years():
    """ (colony_qid, surname) -> list of (year, given_initials) for SUBSTANTIVE
    governor rows (acting/administrator/lieut-gov rows excluded — the bio role we
    check is the substantive governorship, and acting stints add spurious years).
    """
    idx = collections.defaultdict(list)
    for l in open(ROOT / "data" / "kg" / "governors_table_rows.jsonl"):
        r = json.loads(l)
        if ACTING.search(r["name"]):
            continue
        sur, inits = name_parts(r["name"])
        if sur:
            idx[(r["colony_qid"], sur)].append((r["year"], inits))
    return idx

def main():
    tbl = load_table_years()
    canon = B.build_canon()
    persons = B.load_persons(B.CO / "persons.jsonl"); persons.update(B.load_persons(B.IO / "persons.jsonl"))

    flags = []
    seen = set()
    for path in (B.CO / "career_facts.jsonl", B.IO / "career_facts.jsonl"):
        for line in open(path):
            d = json.loads(line)
            if not d.get("colony_qid") or not d.get("year_start"):
                continue
            label = d.get("role_label") or ""             # the GROUNDED role only
            if not GOV_ROLE.match(label) or NOT_GOV.search(label):
                continue
            cp = canon(d["person_id"])
            sur, giv, qid, wlab = persons.get(cp, (None, None, None, None))
            if not sur:
                continue
            sk = re.sub(r"[^A-Z]", "", sur.upper())
            rows = tbl.get((d["colony_qid"], sk))
            if not rows:
                continue
            bio_init = {x[0].upper() for x in re.split(r"[^A-Za-z]", giv or "") if x}
            # keep only table rows whose given initials are consistent with the bio
            # person's (intersection non-empty), to defeat same-surname collisions
            matched = [r for r in rows if not bio_init or not r[1] or (bio_init & r[1])]
            use = matched if matched else []
            if not use:
                continue
            cnt = collections.Counter(y for y, _ in use)
            bio_y = d["year_start"]
            if bio_y in cnt:
                continue                                   # agrees with some edition
            best, support = cnt.most_common(1)[0]
            # need a real consensus year (clear plurality, ≥2 editions) and a gap
            # bigger than the appointed-vs-assumed-office ±1 boundary noise
            if support < 2 or support < 0.6 * sum(cnt.values()):
                continue
            if abs(best - bio_y) < 2:
                continue
            dedup = (cp, d["colony_qid"], bio_y)
            if dedup in seen:
                continue
            seen.add(dedup)
            initials_ok = bool(bio_init) and any(bio_init & r[1] for r in use if r[1])
            # confidence: table consensus strength + given-name agreement
            conf = ("high" if support >= 2 and initials_ok else
                    "medium" if support >= 2 or initials_ok else "low")
            flags.append({
                "person_id": cp,
                "name": (wlab or f"{sur}, {giv or ''}".strip().rstrip(",")),
                "colony_qid": d["colony_qid"],
                "colony": PL.get(d["colony_qid"], {}).get("label", d["colony_qid"]),
                "role_label": d.get("role_label"),
                "bio_year": bio_y,
                "table_year": best,
                "table_year_support": dict(cnt),
                "delta": best - bio_y,
                "confidence": conf,
            })

    order = {"high": 0, "medium": 1, "low": 2}
    flags.sort(key=lambda f: (order[f["confidence"]], -abs(f["delta"]), f["colony"]))
    out = ROOT / "data" / "kg" / "governor_year_flags.jsonl"
    with out.open("w") as f:
        for x in flags: f.write(json.dumps(x, ensure_ascii=False) + "\n")
    byc = collections.Counter(f["confidence"] for f in flags)
    print(f"{len(flags)} bio/table year conflicts across {len({f['colony_qid'] for f in flags})} colonies "
          f"— {byc['high']} high / {byc['medium']} medium / {byc['low']} low confidence")
    print(f"wrote {out}\n")
    print("Conflicts (confidence, then |delta|):")
    for x in flags:
        print(f"  [{x['confidence']:<6}] {x['name'][:32]:<32} {x['colony'][:20]:<20} "
              f"bio {x['bio_year']} -> table {x['table_year']:<5} (Δ{x['delta']:+d})  support {x['table_year_support']}")

if __name__ == "__main__":
    main()
