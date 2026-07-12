#!/usr/bin/env python3
"""Census of the IOL no-bio population — the roster-only people the
Record of Services never covered (docs/NOBIO_DEDUP_KICKOFF.md).

Builds the raw material the no-bio dedup cycle starts from:

  civil chains      unlinked civil-list records collapsed to person-
                    chains on (surname-key, initials, government),
                    split at >8-year gaps (namesake generations)
  gradation         identities (commission/covenant-year keyed) not
                    linked to any bio person
  overlap           gradation-unlinked whose (surname, initials) matches
                    a civil chain in an overlapping era

Outputs (data/iol/identity/):
  nobio_civil_chains.jsonl   one row per chain: key, years, records,
                             offices sample, governments
  nobio_census.json          the headline numbers
  NOBIO_CENSUS.md            report

Estimate caveats (state them wherever the numbers travel):
  - initials-keyed chains merge same-initial namesakes inside one
    government (undercount) and split one person across governments
    (overcount); the two roughly offset but are UNMEASURED
  - ~11k unlinked records with unusable names are excluded (floor)
  - "unlinked" means the tiered linker could not confirm a bio match,
    not that none exists — the COL-style A/B/C adjudication is the
    dedup cycle's job
"""

from __future__ import annotations

import json
import re
from collections import Counter, defaultdict
from glob import glob
from pathlib import Path

ROOT = Path("data/iol")
IDD = ROOT / "identity"
GAP_YEARS = 8


def sk(s):
    return re.sub(r"[^A-Z]", "", (s or "").upper())


def initials(g):
    return "".join(t[0].upper() for t in re.split(r"[ .]+", g or "")
                   if t and t[0].isalpha())


def main() -> None:
    linked = set()
    for l in open(ROOT / "civil/civil_person_links.jsonl",
                  encoding="utf-8"):
        r = json.loads(l)
        linked.add((r["edition_tag"], r["char_offset"], r["line_no"]))

    groups = defaultdict(list)
    stats = Counter()
    for f in sorted(glob(str(ROOT / "civil/civil_1[89]*.jsonl"))):
        for i, l in enumerate(open(f, encoding="utf-8")):
            r = json.loads(l)
            stats["records"] += 1
            if (r["edition_tag"], r["char_offset"], i) in linked:
                stats["linked"] += 1
                continue
            nm = r.get("name") or ""
            toks = [t for t in nm.split() if any(c.isalpha() for c in t)]
            if len(toks) < 2 or len(toks[-1]) < 3:
                stats["unusable_name"] += 1
                continue
            stats["unlinked_usable"] += 1
            key = (sk(toks[-1]), initials(" ".join(toks[:-1])),
                   r.get("government"))
            groups[key].append(r)

    chains = []
    for (s, ini, gov), rows in groups.items():
        rows.sort(key=lambda r: r["edition_year"])
        cur = [rows[0]]
        for r in rows[1:]:
            if r["edition_year"] - cur[-1]["edition_year"] > GAP_YEARS:
                chains.append(((s, ini, gov), cur))
                cur = []
            cur.append(r)
        chains.append(((s, ini, gov), cur))

    with open(IDD / "nobio_civil_chains.jsonl", "w",
              encoding="utf-8") as fh:
        for n, ((s, ini, gov), rows) in enumerate(chains):
            years = sorted({r["edition_year"] for r in rows})
            fh.write(json.dumps({
                "chain_id": f"nbc_{s}_{ini or 'X'}_{years[0]}_{n}",
                "surname_key": s, "initials": ini, "government": gov,
                "name": max((r.get("name") or "" for r in rows), key=len),
                "years": [years[0], years[-1]], "n_records": len(rows),
                "offices": sorted({(r.get("office") or "")[:60]
                                   for r in rows})[:6],
                "records": [[r["edition_tag"], r["char_offset"]]
                            for r in rows][:40],
            }, ensure_ascii=False) + "\n")

    gid = [json.loads(l) for l in
           open(ROOT / "gradation/gradation_identities.jsonl",
                encoding="utf-8")]
    glinked = {json.loads(l)["gradation_id"] for l in
               open(ROOT / "gradation/gradation_person_links.jsonl",
                    encoding="utf-8")}
    unl = [g for g in gid if g["gradation_id"] not in glinked]

    civkeys = defaultdict(set)
    for (s, ini, gov), rows in chains:
        civkeys[(s, ini)].update(r["edition_year"] for r in rows)
    overlap = 0
    for g in unl:
        k = (sk(g["surname"]), initials(g.get("given") or ""))
        ys = civkeys.get(k)
        if ys and g["editions"] and \
                min(g["editions"]) - 5 <= max(ys) and \
                max(g["editions"]) + 5 >= min(ys):
            overlap += 1

    census = {
        "civil_records": stats["records"],
        "civil_linked": stats["linked"],
        "civil_unusable": stats["unusable_name"],
        "civil_unlinked_usable": stats["unlinked_usable"],
        "civil_chains": len(chains),
        "gradation_identities": len(gid),
        "gradation_unlinked": len(unl),
        "gradation_unlinked_army": sum(
            1 for g in unl if g["list_type"] == "army"),
        "overlap": overlap,
        "nobio_union": len(chains) + len(unl) - overlap,
        "bio_persons": 19513,
    }
    json.dump(census, open(IDD / "nobio_census.json", "w"), indent=1)

    lines = [
        "# IOL no-bio census",
        "",
        f"{stats['records']:,} civil records: {stats['linked']:,} linked "
        f"to bio persons, {stats['unlinked_usable']:,} unlinked usable "
        f"({stats['unusable_name']:,} unusable names excluded) -> "
        f"**{len(chains):,} person-chains** "
        f"(gap-split at {GAP_YEARS} years).",
        f"Gradation: {len(unl):,} of {len(gid):,} identities unlinked "
        f"({census['gradation_unlinked_army']:,} army); {overlap:,} "
        "overlap a civil chain.",
        "",
        f"**No-bio union: {census['nobio_union']:,} individuals** beside "
        f"the {census['bio_persons']:,} bio persons — a 36% biography "
        "rate. Estimate caveats in the script docstring; the dedup cycle "
        "(COL-style A/B/C adjudication) turns this into a measured table.",
    ]
    (IDD / "NOBIO_CENSUS.md").write_text("\n".join(lines) + "\n",
                                         encoding="utf-8")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
