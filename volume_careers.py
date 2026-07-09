#!/usr/bin/env python3
"""Career-stringing of volume roster records across edition-years.

Strings the 737k per-edition roster records (rules + qwen) into multi-year
"roster careers" on (colony, surname, initials-compatible given names) —
the person-level panel behind the 'imperial careering including the people
who never careered' analysis. Department/position/salary ride along per year
(department wording drifts between editions, so it is recorded, not keyed;
the report shows both career- and department-segment counts).

Steps:
  1. Canonicalize the 217 raw running-header colony strings (OCR garble folds,
     sequential-rename folds, federation sub-chapters folded UP, non-colony
     sections -> None). DESIGN CALLS flagged inline for Jim — edit + re-run.
  2. Group records by (colony_canon, surname_norm); cluster by given-name
     initials compatibility (ordered-subsequence, as in the bio matcher).
     Records with NO given names only join when the group has a single
     unambiguous cluster; otherwise they stay unstrung singletons.
  3. Split a cluster's years into tenure segments when >2 consecutive
     editions are skipped (editions are irregular: 1901-04, 1941-45 gaps).
  4. Propagate bio identity: any record in the career carrying a bio link
     (links.jsonl) tags the whole career with that bio_id.

Outputs (data/volume/careers/):
  careers.jsonl        one line per career segment
  colony_canon.json    raw header -> canonical colony (None = not a colony)
  CAREERS.md           summary report

Usage: python3 volume_careers.py
"""

from __future__ import annotations

import json
import re
from collections import Counter, defaultdict
from pathlib import Path

from col_match.services.match import _initials, _names_compatible, _norm

ROOT = Path("data/volume")
OUT = ROOT / "careers"

# ---------------------------------------------------------------------------
# 1. Colony-header canonicalization
# ---------------------------------------------------------------------------
# Explicit folds. Value None = not a colony personnel chapter (honours rolls,
# front/back matter, library stamps on the scans, page-spread index headers
# that join two different colonies, letter-soup OCR garble).
_FOLD: dict[str, str | None] = {
    # --- OCR garble -> real colony
    "BRITISH GULANA": "BRITISH GUIANA", "BRITISH GUYANA": "BRITISH GUIANA",
    "FIJL": "FIJI", "FLJI": "FIJI",
    "FAIKLAND ISLANDS": "FALKLAND ISLANDS", "FALKLAND ISLAND": "FALKLAND ISLANDS",
    "THE GAMBLA": "GAMBIA", "NATAI": "NATAL", "NATAL.": "NATAL",
    "TANGANIKA TERRITORY": "TANGANYIKA", "BERMUDAS": "BERMUDA",
    "G. LUCIA": "ST. LUCIA", "NICA": "DOMINICA", "OF HONG I": "HONG KONG",
    "LEEWARD I": "LEEWARD ISLANDS", "WIND": "WINDWARD ISLANDS",
    "STR": "STRAITS SETTLEMENTS", "CAPE OF GOOD HOPE'": "CAPE OF GOOD HOPE",
    "HONDURAS": "BRITISH HONDURAS",
    # DESIGN CALL: truncated running header, almost certainly "…MALAY STATES"
    "AY STATES": "FEDERATED MALAY STATES",
    # --- sequential renames folded (a rename is not a career move)
    # DESIGN CALL: East Africa Protectorate -> Kenya (1920 rename)
    "EAST AFRICA PROTECTORATE": "KENYA",
    # DESIGN CALL: British Central Africa -> Nyasaland (1907 rename)
    "BRITISH CENTRAL AFRICA": "NYASALAND PROTECTORATE",
    "BRITISH CENTRAL AFRICA PROTECTORATE": "NYASALAND PROTECTORATE",
    "SOMALILAND": "SOMALILAND PROTECTORATE",
    "BRITISH SOMALILAND PROTECTORATE": "SOMALILAND PROTECTORATE",
    "TANGANYIKA TERRITORY": "TANGANYIKA",
    "THE GOLD COAST COLONY": "GOLD COAST",
    "TRINIDAD": "TRINIDAD AND TOBAGO",          # renamed 1889; TOBAGO stays
    "FEDERATION OF NIGERIA": "NIGERIA",          # 1954 constitutional rename
    "NIGER PROTECTORATE": "NIGER COAST PROTECTORATE",
    "BRITISH NORTH BORNEO": "NORTH BORNEO",
    "BRITISH NEW GUINEA": "PAPUA",               # renamed 1906
    "MALAYA. FEDERATED MALAY STATES": "FEDERATED MALAY STATES",
    "THE UNFEDERATED MALAY STATES": "UNFEDERATED MALAY STATES",
    "PROTECTORATE OF SOUTH ARABIA": "FEDERATION OF SOUTH ARABIA",
    "MINOR POSSESSIONS": "MISCELLANEOUS POSSESSIONS",
    "WEST AFRICA. SETTLEMENTS": "WEST AFRICA SETTLEMENTS",
    "WEST AFRICAN SETTLEMENTS": "WEST AFRICA SETTLEMENTS",
    "THE TRANSVAAL STATE": "TRANSVAAL",
    "NATAL PENSION ACT": "NATAL",                # pension roll inside Natal ch.
    # London institutions
    "COLONIAL AUDIT DEPARTMENT": "OVERSEA AUDIT DEPARTMENT",   # renamed 1910
    "GOVERNMENT AGENCIES IN LONDON": "COLONIAL GOVERNMENT AGENCIES IN LONDON",
    "REGIONAL ORGANIZATIONS": "REGIONAL ORGANISATIONS",
    # DESIGN CALL: the CO's own "Distribution of Business" org pages = London
    # Colonial Office staff
    "DISTRIBUTION OF BUSINESS": "COLONIAL OFFICE (LONDON)",
    "COLONIAL OFFICE": "COLONIAL OFFICE (LONDON)",
    # headers surfaced by the em-dash/back-matter header fix
    "NYASALAND": "NYASALAND PROTECTORATE",
    "WESTERN PACIFIC HIGH COMMISSION": "WESTERN PACIFIC",
    # DESIGN CALL: bare "HIGH COMMISSION" header is WPHC-vs-SA-ambiguous
    "HIGH COMMISSION": None,
    # DESIGN CALL: Orange Free State appears as the ORC chapter's alt header
    "ORANGE FREE STATE": "ORANGE RIVER COLONY",
    # --- federation sub-chapters folded UP (continuity beats granularity;
    # DESIGN CALL — the sub-unit is preserved in `department`/`position`)
    "AUSTRALIA - QUEENSLAND": "AUSTRALIA", "AUSTRALIA SOUTH AUSTRALIA": "AUSTRALIA",
    "AUSTRALIA--TASMANIA": "AUSTRALIA", "AUSTRALIA--VICTORIA": "AUSTRALIA",
    "AUSTRALIA PAPUA": "PAPUA", "AUSTRALIA--PAPUA": "PAPUA",
    "LEEWARD ISLANDS - ANTIGUA": "LEEWARD ISLANDS",
    "LEEWARD ISLANDS- ST. CHRISTOPHER": "LEEWARD ISLANDS",
    "LEEWARD ISLANDS--ANTIGUA--MONTSERRAT": "LEEWARD ISLANDS",
    "WINDWARD ISLANDS - GRENADA": "WINDWARD ISLANDS",
    "WINDWARD ISLANDS - ST. LUCIA": "WINDWARD ISLANDS",
    "WINDWARD ISLANDS - TOBAGO": "WINDWARD ISLANDS",
    "WINDWARD ISLANDS -ST. LUCIA": "WINDWARD ISLANDS",
    "WINDWARD ISLANDS GRENADA": "WINDWARD ISLANDS",
    "WINDWARD ISLANDS ST. LUCIA": "WINDWARD ISLANDS",
    "WINDWARD ISLANDS--GRENADA": "WINDWARD ISLANDS",
    "WINDWARD ISLANDS--ST. VINCENT": "WINDWARD ISLANDS",
    "WINDWARD ISLANDS. GRENADA": "WINDWARD ISLANDS",
    # --- page-spread headers joining two colonies: side unknown -> None
    "BARBADOS--BERMUDA": None, "BRITISH NEW GUINEA- CANADA": None,
    "CANADA -- CAPE OF GOOD HOPE": None, "CANADA--CAPE OF GOOD HOPE": None,
    "CAPE OF GOOD HOPE- CEYLON": None, "CYPRUS--NIGER TERRITORIES": None,
    "HONG KONG - JAMAICA": None, "JAMAICA - LABUAN": None,
    "LAGOS LEEWARD ISLANDS": None, "NATAL -- NEWFOUNDLAND": None,
    "NATAL- NEWFOUNDLAND": None, "NATAL--NEWFOUNDLAND": None,
    "NATAL-NEWFOUNDLAND": None, "SEYCHELLES--SIERRA LEONE": None,
    "VICTORIA-- WEST AFRICA SETTLEMENTS": None,
    # DESIGN CALL: bare "RHODESIA" (38 recs) is Northern/Southern-ambiguous
    "RHODESIA": None,
    # --- honours rolls (person mentions, not postings)
    "IMPERIAL SERVICE ORDER": None, "KNIGHTS BACHELORS": None,
    "ORDER OF ST. MICHAEL AND ST GEORGE": None,
    # --- running volume title caught as colony header: chapter unknown
    "DOMINIONS OFFICE AND COLONIAL OFFICE LIST": None,
    "DOMINIONS OFFICE AND COLONIAL OFFICE LIS": None,
    "THE COLO NIAL OFFICE LIST": None, "THE COLONIAL-OFFICE LIST": None,
    # --- front/back matter, ads, library stamps, letter-soup garble
    "BERKELEY LIBRARY UNIVERSITY OF CALIFORNIA": None,
    "NATIONAL LIBRARY OF MEDICINE": None, "UNIVERSITY OF IOWA": None,
    "TITLE WITHDRAWN": None, "XXV": None, "XXXV": None, "THE": None,
    "LIST OF": None, "FOR'S": None, "F. O": None, "PERS": None,
    "MAKER TO THE QUEEN": None, "INTRODUCTION": None, "P R E F A C E": None,
    "EMIGRATION": None, "DOCUMENTS DEPARTMENT": None,
    "RULES AND REGULATIONS": None, "PARLIAMENTARY ETC. PAPERS": None,
    "REVENUE AND EXPENDITURE": None, "IMPERIAL CONFERENCE": None,
    "IMPERIAL PENSION MINUTES": None, "INTERNATIONAL CO-OPERATION": None,
    "MAP SUPPLIED BY THE NATAL GOVERNMENT": None,
    "D F N N": None, "F A E E G F T": None, "H H H H H H H H H H": None,
    "I B C F F G G G H M M N": None, "I K I": None, "K. H. F": None,
    "L M": None, "M A M D O": None, "T P": None,
}


# Federations/unions whose sub-chapter compounds ("LEEWARD ISLANDS--ANTIGUA",
# "SOUTH AFRICA--NATAL") fold UP to the federation. A compound whose FIRST
# segment is not one of these joins unrelated colonies — a page-spread index
# header — and maps to None. DESIGN CALLS flagged.
_FEDERATIONS = {"AUSTRALIA", "CANADA", "LEEWARD ISLANDS", "WINDWARD ISLANDS",
                "SOUTH AFRICA", "WEST AFRICA SETTLEMENTS"}
_COMPOUND_OVERRIDE = {
    # DESIGN CALL: pre-1885 Barbados sat inside the Windwards chapter but is
    # the dominant continuous identity — fold to BARBADOS, not the federation
    "WINDWARD ISLANDS--BARBADOS": "BARBADOS",
}


def canon_colony(raw: str) -> str | None:
    c = re.sub(r"\s+", " ", raw.strip().strip(".")).upper()
    c = re.sub(r"^THE\s+(?=(GOLD|GAMBIA|GAMBLA|TRANSVAAL|LEEWARD|WINDWARD))", "", c)
    if c in _FOLD:
        return _FOLD[c]
    # letter-soup OCR garble ("S S S W E T N S L V")
    toks = c.replace("--", " ").split()
    if toks and all(len(t) <= 2 for t in toks):
        return None
    if "--" in c:
        if c in _COMPOUND_OVERRIDE:
            return _COMPOUND_OVERRIDE[c]
        parts = [re.sub(r"^THE\s+", "", p.strip(" .")) for p in c.split("--")
                 if p.strip(" .")]
        if len(parts) == 1:
            return canon_colony(parts[0])
        # DESIGN CALL: 1930s "MALAYA: <unit>" hierarchy headers fold DOWN to
        # the unit (Straits Settlements, F.M.S., State of Johore) so the
        # series stays continuous with the pre-1930 chapter identities
        if parts[0] == "MALAYA":
            return canon_colony("--".join(parts[1:]))
        if parts[0] in _FEDERATIONS:
            return canon_colony(parts[0])
        return None                       # page-spread header: side unknown
    return c


# ---------------------------------------------------------------------------
# 2-4. Load, cluster, segment
# ---------------------------------------------------------------------------

def load_all() -> tuple[list[dict], dict[str, str]]:
    records, rec2bio = [], {}
    for d in sorted(ROOT.glob("col*")):
        if not d.is_dir():
            continue
        for line in open(d / "records.jsonl", encoding="utf-8"):
            records.append(json.loads(line))
        lp = d / "links.jsonl"
        if lp.exists():
            for line in open(lp, encoding="utf-8"):
                ln = json.loads(line)
                rec2bio[ln["record_id"]] = ln["bio_id"]
    return records, rec2bio


def cluster_group(recs: list[dict]) -> list[list[dict]]:
    """Cluster same-(colony,surname) records by initials compatibility."""
    with_given = [r for r in recs if _initials(r.get("given_names"))]
    without = [r for r in recs if not _initials(r.get("given_names"))]
    clusters: list[tuple[set[tuple], list[dict]]] = []  # (initials variants, recs)
    for r in sorted(with_given, key=lambda r: (-len(_initials(r["given_names"])),
                                               r["edition_year"])):
        ini = tuple(_initials(r["given_names"]))
        homes = [c for c in clusters
                 if all(_names_compatible(" ".join(ini), " ".join(v))
                        for v in c[0])]
        if len(homes) == 1:
            homes[0][0].add(ini)
            homes[0][1].append(r)
        else:  # 0 = new person; >1 = ambiguous ("J." fits two people) -> own
            clusters.append(({ini}, [r]))
    out = [c[1] for c in clusters]
    # no-given records: only safe when there is a single candidate cluster
    if without:
        if len(out) == 1:
            out[0].extend(without)
        else:
            out.extend([[r] for r in without])
    return out


def segment_years(years: list[int], eds: list[int]) -> list[list[int]]:
    """Split a sorted year list where >2 consecutive editions were skipped."""
    slot = {y: i for i, y in enumerate(eds)}
    segs, cur = [], [years[0]]
    for a, b in zip(years, years[1:]):
        if slot[b] - slot[a] > 3:
            segs.append(cur)
            cur = [b]
        else:
            cur.append(b)
    segs.append(cur)
    return segs


_ALPHA = re.compile(r"[a-z]+")


def _bigrams(text: str | None) -> set[tuple[str, str]]:
    # single-letter tokens are initials ("J. E. Smith") — they'd match OCR
    # letter-noise in position strings, so only full words count
    toks = [t for t in _ALPHA.findall((text or "").lower()) if len(t) >= 3]
    return set(zip(toks, toks[1:]))


def build_posbigrams(records: list[dict]) -> Counter:
    """Token bigrams seen inside position/department strings. A 'person' whose
    name reads as one of these ('Nuwara Eliya', 'Government Printer', 'Orange
    Walk') is a station/institution row misparsed as a name."""
    c: Counter = Counter()
    for r in records:
        for bg in _bigrams(r.get("position")) | _bigrams(r.get("department")):
            c[bg] += 1
    return c


def suspect_flag(career: dict, posbg: Counter) -> str | None:
    """'garble' = surname is OCR junk; 'nonperson' = the full name reads as a
    place/institution phrase seen >=3 times in position/department text and
    nothing corroborates personhood (no bio link, no honours)."""
    s = career["surname"]
    if len(s) < 3 or not s.isalpha():
        return "garble"
    if career["bio_ids"] or any(r["honours"] for r in career["records"]):
        return None
    name = f"{career['given_names'] or ''} {career['surname']}"
    if any(posbg.get(bg, 0) >= 2 for bg in _bigrams(name)):
        return "nonperson"
    return None


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    records, rec2bio = load_all()
    eds = sorted({r["edition_year"] for r in records})
    posbg = build_posbigrams(records)

    raw_headers = Counter(r["colony"] for r in records)
    canon_map = {raw: canon_colony(raw) for raw in raw_headers}
    (OUT / "colony_canon.json").write_text(
        json.dumps(canon_map, indent=1, sort_keys=True))

    groups: dict[tuple[str, str], list[dict]] = defaultdict(list)
    dropped = 0
    for r in records:
        colony = canon_map[r["colony"]]
        surname = _norm((r.get("surname") or "").split()[-1]) if r.get("surname") else ""
        if colony is None or not surname:
            dropped += 1
            continue
        r["_colony"] = colony
        groups[(colony, surname)].append(r)

    careers: list[dict] = []
    for (colony, surname), recs in groups.items():
        for cl in cluster_group(recs):
            by_year = defaultdict(list)
            for r in cl:
                by_year[r["edition_year"]].append(r)
            for seg_years in segment_years(sorted(by_year), eds):
                seg_recs = [r for y in seg_years for r in by_year[y]]
                givens = Counter(r.get("given_names") for r in seg_recs
                                 if r.get("given_names"))
                bio_ids = sorted({rec2bio[r["record_id"]] for r in seg_recs
                                  if r["record_id"] in rec2bio})
                multi_post = sorted(y for y in seg_years if len(by_year[y]) > 1)
                career = {
                    "career_id": f"{colony}|{surname}|{len(careers)}",
                    "colony": colony, "surname": surname,
                    "given_names": givens.most_common(1)[0][0] if givens else None,
                    "years": seg_years, "n_editions": len(seg_years),
                    "span": seg_years[-1] - seg_years[0] + 1,
                    "weak_key": max((len(_initials(g)) for g in givens), default=0) <= 1,
                    "multi_post_years": multi_post,
                    "bio_ids": bio_ids,
                    "records": [{
                        "year": r["edition_year"], "record_id": r["record_id"],
                        "department": r.get("department"),
                        "position": r.get("position"), "salary": r.get("salary"),
                        "honours": r.get("honours") or [],
                        "source": r.get("source", "rules"),
                        "bio_id": rec2bio.get(r["record_id"]),
                    } for r in sorted(seg_recs, key=lambda r: r["edition_year"])],
                }
                career["suspect"] = suspect_flag(career, posbg)
                careers.append(career)

    with (OUT / "careers.jsonl").open("w", encoding="utf-8") as fh:
        for c in careers:
            fh.write(json.dumps(c, ensure_ascii=False) + "\n")

    # ------------------------------------------------------------------ report
    n_rec_used = sum(len(c["records"]) for c in careers)
    multi = [c for c in careers if c["n_editions"] >= 2]
    strung = sum(len(c["records"]) for c in multi)
    linked = [c for c in careers if c["bio_ids"]]
    linked_recs = sum(len(c["records"]) for c in linked)
    direct_links = sum(1 for c in careers for r in c["records"] if r["bio_id"])
    lengths = Counter(min(c["n_editions"], 10) for c in careers)
    dept_segments = sum(
        1 + sum(1 for a, b in zip(c["records"], c["records"][1:])
                if (a["department"] or "") != (b["department"] or ""))
        for c in multi)

    n_suspect = Counter(c["suspect"] for c in careers if c["suspect"])
    suspect_recs = sum(len(c["records"]) for c in careers if c["suspect"])
    top = sorted((c for c in multi if not c["suspect"]),
                 key=lambda c: -c["n_editions"])[:15]
    lines = [
        "# Roster career-stringing", "",
        f"- input records: {len(records):,} across {len(eds)} editions "
        f"({eds[0]}–{eds[-1]}); {dropped:,} dropped (non-colony header or no surname)",
        f"- suspect careers: {dict(n_suspect)} covering {suspect_recs:,} records "
        f"(name reads as place/institution phrase, or garble surname) — "
        f"flagged, kept in careers.jsonl, excluded from the sample below",
        f"- **careers (person×colony segments): {len(careers):,}**, of which "
        f"{len(multi):,} span >=2 editions ({strung:,} records = "
        f"{strung/n_rec_used:.0%} of usable records strung into multi-year careers)",
        f"- weak keys (single initial at best): {sum(c['weak_key'] for c in careers):,}",
        f"- department segments inside multi-year careers: {dept_segments:,} "
        f"(department wording drifts; recorded per-year, not keyed)",
        f"- **bio augmentation**: {len(linked):,} careers carry >=1 bio link -> "
        f"{linked_recs:,} roster person-years now attached to a biography "
        f"({direct_links:,} directly linked, {linked_recs-direct_links:,} inherited "
        f"via the career string)",
        "", "## Career length (editions appeared, 10 = 10+)", "",
        "| editions | careers |", "|---|---|",
    ]
    lines += [f"| {k} | {lengths[k]:,} |" for k in sorted(lengths)]
    lines += ["", "## Longest careers (sanity sample)", ""]
    for c in top:
        pos = next((r["position"] for r in reversed(c["records"]) if r["position"]), "?")
        lines.append(f"- **{c['surname'].title()}, {c['given_names'] or '?'}** — "
                     f"{c['colony']} {c['years'][0]}–{c['years'][-1]} "
                     f"({c['n_editions']} eds; last: {pos[:60]}"
                     f"{'; bio-linked' if c['bio_ids'] else ''})")
    (OUT / "CAREERS.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines[:12]))
    print(f"\nwrote {OUT}/careers.jsonl, colony_canon.json, CAREERS.md")


if __name__ == "__main__":
    main()
