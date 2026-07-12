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


# Office/section labels that leak into the name field. A name whose
# SURNAME SLOT is one of these is not a person ("Military Secretary",
# "Deputy Director Revenue Settlement"); leading ones are titles to
# strip before keying ("Assistant John R. Aitchison" -> initials JR,
# not AJR). ENGINEER/CONTRACTOR/MERCHANT/DOCTOR/JUDGE are real (Parsi)
# surnames — deliberately NOT listed.
_OFFICE_WORDS = {
    "DEPARTMENT", "OFFICE", "OFFICES", "ESTABLISHMENT", "VACANT",
    "SECRETARIAT", "BRANCH", "DIVISION", "SERVICE", "GOVERNMENT",
    "COMMITTEE", "COUNCIL", "BOARD", "SECRETARY", "OFFICER",
    "SUPERINTENDENT", "INSPECTOR", "COMMISSIONER", "REGISTRAR",
    "DIRECTOR", "COLLEGE", "SURVEY", "RAILWAY", "RAILWAYS", "POLICE",
    "CIRCLE", "PROVINCE", "PRESIDENCY", "MEMBER", "CLERK", "CLERKS",
    "GAZETTED", "ASSISTANT", "DEPUTY", "SETTLEMENT", "COMM", "TAX",
    "DITTO", "SCHOOL", "SCHOOLS", "HOSPITAL", "COURT", "SECTION",
    "GENERAL", "AGENT", "ACCOUNTANT", "AUDITOR", "EXAMINER",
    "TRANSLATOR", "UNDER",
    # department names OCR leaves in the name slot ("Stationery and
    # Stamps"). SALT/FOREST/PRESS are real surnames — not listed.
    "STAMPS", "STATIONERY", "PRINTING", "TELEGRAPH", "TELEGRAPHS",
    "CUSTOMS", "EXCISE", "ACCOUNTS", "AUDIT", "RECORDS", "ARCHIVES",
    "FORESTS", "JAILS", "STORES", "PENSIONS", "LIBRARY", "MUSEUM",
    "GAZETTE", "MINT", "OPIUM", "INDUSTRIES", "COMMERCE",
    "AGRICULTURE", "EDUCATION", "REVENUE", "FINANCE", "JUSTICE",
    "MARINE", "IRRIGATION", "SANITARY", "DEPARTMENTS", "ENGINEERING",
    "EST", "BUREAU",
    # plural office nouns + commissariat family (silver-standard audit
    # found "Deputy Assistant Commissaries" chains); singular ENGINEER/
    # SURGEON/JUDGE stay out — they are real surnames
    "COMMISSARY", "COMMISSARIES", "COMMISSARIAT", "ENGINEERS",
    "SUPERINTENDENTS", "EXAMINERS", "JUDGES", "SECRETARIES",
    "ASSISTANTS", "SURGEONS", "OFFICERS", "COLLECTORS", "MAGISTRATES",
    "SETTLEMENTS", "INSPECTORS", "AUDITORS", "TRANSLATORS", "WRITERS",
    "APPRENTICES", "PROFESSORS", "INSTRUCTORS", "CONSERVATORS",
    "CHAPLAINS", "MEMBERS",
}
_TITLE_WORDS = _OFFICE_WORDS | {
    "MR", "ESQ", "ESQR", "SIR", "HON", "HONBLE", "REV", "REVD", "DR",
    "LORD", "MAJOR", "COL", "CAPT", "CAPTAIN", "LIEUT", "LT", "GEN",
    "COLONEL", "SURG", "SURGEON", "BRIG", "RAI", "RAO", "KHAN",
    "BAHADUR", "SAHIB", "THE", "CHIEF", "ENGINEER",
}

# Real names never contain standalone lowercase function words;
# office phrases do ("Master and Registrar in Equity", "In the Civil
# Leave Code") and they dodge any word list.
_FUNCTION_WORDS = {"and", "of", "in", "the", "for", "to", "on", "with"}


def norm_gov(gov):
    """Fold government-string surface variants so one career keys to
    one chain: 'GOVERNMENT OF (THE) X' -> X, running-header/OCR
    suffixes stripped, plus the two whole-unit renames (NWP&O -> UP
    1902, CP&Berar -> CP 1936). True splits (Bihar/Orissa, Sind,
    Eastern Bengal) stay distinct — cross-government edges are the
    unifier's job, not the census key's."""
    g = (gov or "").strip()
    g = re.sub(r"—continued$", "", g)
    g = re.sub(r"[.,]\s*(November|STORE DEPARTMENT).*$", "", g)
    if g != "GOVERNMENT OF INDIA":      # proper name, not a variant
        g = re.sub(r"^GOVERNMENT OF (THE )?", "", g).strip(" .,—-")
    if g == "UNITED PROVINCES":
        g = "UNITED PROVINCES OF AGRA AND OUDH"
    if g == "NORTH-WESTERN PROVINCES AND OUDH":
        g = "UNITED PROVINCES OF AGRA AND OUDH"
    if g == "CENTRAL PROVINCES AND BERAR":
        g = "CENTRAL PROVINCES"
    return g or None


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
            r["_line_no"] = i           # char_offset is shared by
                                        # coholders on one line
            nm = r.get("name") or ""
            nm = re.sub(r"\(.*$", "", nm)   # trailing "(S. Waziristan"
            # supp lists print SURNAME-first ("COATES, JOHN MARTIN",
            # "ALI AUSAT, MUHAMMAD") — reorder before keying
            m = re.match(r"^([A-Z][A-Z'`.\- ]{2,}),\s*(.+)$", nm)
            if m:
                nm = f"{m.group(2)} {m.group(1)}"
            toks = [t for t in nm.split() if any(c.isalpha() for c in t)]
            if len(toks) < 2 or len(toks[-1]) < 3 \
                    or sk(toks[-1]) in _OFFICE_WORDS \
                    or any(t in _FUNCTION_WORDS for t in toks):
                stats["unusable_name"] += 1
                continue
            given = toks[:-1]
            while given and sk(given[0]) in _TITLE_WORDS:
                given = given[1:]
            stats["unlinked_usable"] += 1
            key = (sk(toks[-1]), initials(" ".join(given)),
                   norm_gov(r.get("government")))
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
        for (s, ini, gov), rows in chains:
            years = sorted({r["edition_year"] for r in rows})
            # id from the first record's provenance, NOT enumeration —
            # stable across rebuilds so ledgers/silver labels keep
            fh.write(json.dumps({
                "chain_id": f"nbc_{s}_{ini or 'X'}_"
                            f"{rows[0]['edition_tag']}_"
                            f"{rows[0]['_line_no']}",
                "surname_key": s, "initials": ini, "government": gov,
                "name": max((r.get("name") or "" for r in rows), key=len),
                "years": [years[0], years[-1]], "n_records": len(rows),
                "offices": sorted({(r.get("office") or "")[:60]
                                   for r in rows})[:6],
                "records": [[r["edition_tag"], r["char_offset"],
                             r["_line_no"]] for r in rows][:40],
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
