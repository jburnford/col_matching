#!/usr/bin/env python3
"""Link civil-list roster records (119,527 office—holder rows, 1861-1947)
to the audited IOL person table — the B2-style roster<->bio linker
(docs/IOL_NEXT_SESSION.md item 4; mirrors iol_link_exits.py).

A civil record is a year-stamped attestation: NAME held OFFICE under
GOVERNMENT in EDITION_YEAR. The measured baseline (docs/IOL_VS_COL.md §2)
was 54% unique surname+initials matches for 1935; this linker adds the
corroboration that lifts precision:

  timing     person's editions/events must cover the edition year
  office     civil office stem == a person event position stem at ±2 yrs
  place      government/province appears among the person's event places
             around that year
  honours    shared honour letter-groups (undated compare)

Transparent points; a link is accepted only when a single candidate
clears the bar with a >=15 gap. Pre-1886 records mostly predate the
bio-derived person table and land in `no_candidate` (gradation-linker
territory).

Outputs (data/iol/civil/):
  civil_person_links.jsonl   accepted {record.., person_id, score,..}
  civil_link_ambiguous.jsonl >1 surviving candidate (pool; adjudicate
                             only if a use-case needs the mass)
  CIVIL_LINKS.md             rates by era + corroboration mix
"""

from __future__ import annotations

import json
import re
from collections import Counter, defaultdict
from glob import glob
from pathlib import Path

ROOT = Path("data/iol")
CIVIL = ROOT / "civil"

MIN_SCORE = 45
WEAK_SCORE = 40
GAP = 15

_PARTICLES = {"de", "da", "du", "van", "von", "la", "le", "el", "al",
              "ud", "ul", "bin", "ibn"}


def sk(s: str | None) -> str:
    return re.sub(r"[^A-Z]", "", (s or "").upper())


def posstem(p: str | None) -> str:
    return re.sub(r"[^a-z]", "", (p or "").lower())[:10]


def initials_of(tokens: list[str]) -> str:
    return "".join(t[0].upper() for t in tokens if t and t[0].isalpha())


def civil_name(name: str) -> tuple[str, list[str]] | None:
    """Given-first civil name -> (surname, given tokens). Trailing
    particles fold into the surname ('Denys de Saumarez Bray' -> Bray;
    'H. St. J. B. Philby' -> Philby)."""
    toks = [t for t in re.split(r"[ ]+", name.strip()) if t]
    toks = [t for t in toks if any(c.isalpha() for c in t)]
    if len(toks) < 2:
        return None
    surname = toks[-1]
    if len(surname) < 3 or not surname[0].isupper() \
            or any(c.isdigit() for c in surname):
        return None
    return surname, toks[:-1]


def name_class(cand_toks: list[str], given: str | None) -> str | None:
    g_toks = [t for t in re.split(r"[ .]+", given or "") if t]
    c_toks = [t for t in cand_toks
              if t.lower().strip(".") not in _PARTICLES]
    if not c_toks:
        return None
    if not g_toks:
        return None
    ci, gi = initials_of(c_toks), initials_of(g_toks)
    cw = [t.upper().strip(".") for t in c_toks if len(t.strip(".")) > 2]
    gw = [t.upper() for t in g_toks if len(t) > 2]
    if cw and gw and cw[0] == gw[0] and (ci == gi or gi.startswith(ci)
                                         or ci.startswith(gi)):
        return "forename"
    if ci == gi:
        return "initials_exact"
    if gi.startswith(ci) or ci.startswith(gi):
        return "initials_prefix"
    return None


# provinces/governments -> place keys that may appear in event places
def gov_key(g: str | None) -> str:
    g = (g or "").upper()
    g = re.sub(r"\bGOVERNMENT OF\b|\(.*?\)", " ", g)
    return sk(g)[:12]


def main() -> None:
    persons = [json.loads(l) for l in
               open(ROOT / "llm_struct_corpus.stage3.deduped.jsonl",
                    encoding="utf-8")]
    by_surname: dict[str, list[dict]] = defaultdict(list)
    for p in persons:
        eds = set(p.get("editions") or [])
        stems_by_year: dict[int, set[str]] = defaultdict(set)
        places_by_year: dict[int, set[str]] = defaultdict(set)
        for e in p.get("events") or []:
            st = posstem(e.get("position"))
            pl = sk(e.get("place"))[:12]
            y0 = e.get("year_start")
            y1 = e.get("year_end") or y0
            if not y0:
                continue
            for y in range(y0, min(y1, y0 + 40) + 1):
                if len(st) >= 4:
                    stems_by_year[y].add(st)
                if pl:
                    places_by_year[y].add(pl)
        info = {
            "person_id": p["person_id"], "given": p.get("given_names"),
            "eds": eds,
            "first_ed": min(eds) if eds else None,
            "last_ed": max(eds) if eds else None,
            "stems": stems_by_year, "places": places_by_year,
            "honour_keys": {sk(h.get("award")) for h in
                            (p.get("honours") or []) if h.get("award")},
        }
        by_surname[sk(p.get("surname"))].append(info)
        full = sk((p.get("given_names") or "") + (p.get("surname") or ""))
        if full and full != sk(p.get("surname")):
            by_surname[full].append(info)
    surname_freq = {k: len(v) for k, v in by_surname.items()}

    links, ambiguous = [], []
    stats = Counter()
    corro = Counter()
    era = defaultdict(Counter)

    # edition files only — civil_person_links/civil_link_ambiguous live
    # in the same directory and must not feed back in
    for f in sorted(glob(str(CIVIL / "civil_1[89]*.jsonl"))):
        for i, line in enumerate(open(f, encoding="utf-8")):
            r = json.loads(line)
            stats["records"] += 1
            y = r["edition_year"]
            decade = f"{(y // 10) * 10}s"
            era[decade]["records"] += 1
            parsed = civil_name(r.get("name") or "")
            if not parsed:
                stats["unparsed_name"] += 1
                era[decade]["unparsed"] += 1
                continue
            surname, toks = parsed
            # try surname key, then full-name key (Indian names)
            keys = [sk(surname), sk("".join(toks) + surname)]
            seen_pids = set()
            cands = []
            for k in keys:
                for c in by_surname.get(k, []):
                    if c["person_id"] in seen_pids:
                        continue
                    seen_pids.add(c["person_id"])
                    nc = "forename" if k == keys[1] \
                        else name_class(toks, c["given"])
                    if nc is None:
                        continue
                    # attestation window: person must exist around y
                    if c["first_ed"] and c["first_ed"] > y + 2:
                        continue
                    if c["last_ed"] and c["last_ed"] < y - 3:
                        continue
                    score = {"forename": 40, "initials_exact": 30,
                             "initials_prefix": 15}[nc]
                    freq = surname_freq[k]
                    score += 15 if freq <= 3 else (
                        5 if freq <= 10 else (-15 if freq >= 30 else 0))
                    flags = []
                    if y in c["eds"]:
                        score += 10
                        flags.append("ed_year")
                    ost = posstem(r.get("office"))
                    st_near = set()
                    pl_near = set()
                    for yy in range(y - 2, y + 3):
                        st_near |= c["stems"].get(yy, set())
                        pl_near |= c["places"].get(yy, set())
                    if len(ost) >= 4 and ost in st_near:
                        score += 25
                        flags.append("office")
                    gk = gov_key(r.get("government"))
                    if gk and any(gk in pl or pl in gk
                                  for pl in pl_near if pl):
                        score += 10
                        flags.append("place")
                    hks = {sk(h) for h in (r.get("honours") or [])}
                    if hks & c["honour_keys"]:
                        score += 15
                        flags.append("honours")
                    cands.append({"person_id": c["person_id"],
                                  "given": c["given"], "name_class": nc,
                                  "score": score, "corro": flags})
            cands = [c for c in cands if c["score"] >= WEAK_SCORE]
            if not cands:
                stats["no_candidate"] += 1
                era[decade]["no_candidate"] += 1
                continue
            cands.sort(key=lambda c: -c["score"])
            if len(cands) > 1 and cands[0]["score"] - cands[1]["score"] < GAP:
                stats["ambiguous"] += 1
                era[decade]["ambiguous"] += 1
                ambiguous.append({
                    "edition_tag": r["edition_tag"],
                    "char_offset": r["char_offset"], "line_no": i,
                    "name": r["name"], "office": r.get("office"),
                    "government": r.get("government"),
                    "year": y,
                    "candidates": cands[:4]})
                continue
            top = cands[0]
            # tiers mirror the COL link discipline: 'strong' has an
            # independent corroboration or a decisive score; 'weak' is the
            # unique 40-44 name+timing band (measure before trusting)
            if top["score"] < MIN_SCORE:
                tier = "weak"
            elif top["score"] >= 60 or len(top["corro"]) >= 2:
                tier = "strong"
            else:
                tier = "standard"
            stats["linked"] += 1
            stats[f"tier_{tier}"] += 1
            era[decade]["linked"] += 1
            for fl in top["corro"] or ["name_only"]:
                corro[fl] += 1
            if not top["corro"]:
                corro["name_only"] += 1
            links.append({
                "edition_tag": r["edition_tag"], "edition_year": y,
                "char_offset": r["char_offset"], "line_no": i,
                "government": r.get("government"),
                "department": r.get("department"),
                "office": r.get("office"), "name": r["name"],
                "person_id": top["person_id"],
                "person_given": top["given"],
                "name_class": top["name_class"], "score": top["score"],
                "tier": tier, "corroboration": top["corro"]})

    with open(CIVIL / "civil_person_links.jsonl", "w",
              encoding="utf-8") as fh:
        for r in links:
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")
    with open(CIVIL / "civil_link_ambiguous.jsonl", "w",
              encoding="utf-8") as fh:
        for r in ambiguous:
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")

    linked_persons = len({r["person_id"] for r in links})
    post86 = sum(v["linked"] for k, v in era.items() if k >= "1890s") \
        + era["1880s"]["linked"]
    lines = [
        "# Civil-list -> person links (B2 roster<->bio linker)",
        "",
        f"{stats['records']:,} civil records -> **{stats['linked']:,} "
        f"linked** ({stats['linked'] / stats['records']:.0%}; "
        f"{linked_persons:,} distinct persons; tiers strong "
        f"{stats['tier_strong']:,} / standard {stats['tier_standard']:,} "
        f"/ weak {stats['tier_weak']:,}), "
        f"ambiguous {stats['ambiguous']:,}, no candidate "
        f"{stats['no_candidate']:,}, unparsed {stats['unparsed_name']:,}.",
        "",
        "Corroboration on accepted links (multi-count): "
        + ", ".join(f"{k} {v:,}" for k, v in corro.most_common()),
        "",
        "| decade | records | linked | linked% | ambiguous | no cand |",
        "|---|---|---|---|---|---|",
    ]
    for dec in sorted(era):
        e = era[dec]
        lines.append(
            f"| {dec} | {e['records']:,} | {e['linked']:,} | "
            f"{e['linked'] / max(e['records'], 1):.0%} | "
            f"{e['ambiguous']:,} | {e['no_candidate']:,} |")
    lines += [
        "",
        "Pre-1886 records predate the bio-derived person table (the",
        "gradation linker's territory). Scoring: name class 15-40,",
        "surname rarity ±15, edition-year attestation +10, office-stem",
        "agreement ±2yrs +25, government-place +10, shared honours +15;",
        f"accept ≥{MIN_SCORE} with a ≥{GAP} gap.",
    ]
    (CIVIL / "CIVIL_LINKS.md").write_text("\n".join(lines) + "\n",
                                          encoding="utf-8")
    print("\n".join(lines))
    print("\nstats:", dict(stats))


if __name__ == "__main__":
    main()
