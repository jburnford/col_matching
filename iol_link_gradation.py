#!/usr/bin/env python3
"""Gradation -> person linker (docs/IOL_NEXT_SESSION.md item 4, second
half). The gradation lists are seniority rosters 1861-1919: army officers
keyed by year of first commission, covenanted civil servants keyed by
covenant (entry) year. Two stages:

  1. collapse 119,429 entries into cross-edition gradation IDENTITIES on
     (list_type, surname, initials, commission/covenant year) — the year
     is printed every edition and stable for life, so an identity is the
     officer's whole seniority trace;
  2. link identities to the audited person table: name compatibility +
     the decisive corroboration that the person's bio entry year equals
     the identity's commission/covenant year (bios open with "appointed
     to the <establishment> civil service" at exactly that year), plus
     establishment<->place, appointment-stem and honours agreement.

Payoff: careers extend back to 1861 (25 years before the Record of
Services begins) and the pre-1886 casualties get an identity spine.

Outputs (data/iol/gradation/):
  gradation_identities.jsonl    one row per identity, editions span,
                                sections/appointments trace
  gradation_person_links.jsonl  accepted links (tiered like the civil
                                linker: strong/standard/weak)
  gradation_link_ambiguous.jsonl
  GRADATION_LINKS.md
"""

from __future__ import annotations

import json
import re
from collections import Counter, defaultdict
from glob import glob
from pathlib import Path

ROOT = Path("data/iol")
GRAD = ROOT / "gradation"

MIN_SCORE = 45
WEAK_SCORE = 40
GAP = 15

_STYLES = {"sir", "hon", "honble", "rev", "revd", "dr", "lord", "bart",
           "bt", "mr", "major", "col", "capt", "lieut", "lt", "gen"}


def sk(s: str | None) -> str:
    return re.sub(r"[^A-Z]", "", (s or "").upper())


def posstem(p: str | None) -> str:
    return re.sub(r"[^a-z]", "", (p or "").lower())[:10]


def given_tokens(given: str | None) -> list[str]:
    toks = [t.strip(".") for t in re.split(r"[ .]+", given or "")
            if t.strip(".")]
    return [t for t in toks
            if re.sub(r"[^a-z]", "", t.lower()) not in _STYLES]


def initials_of(tokens: list[str]) -> str:
    return "".join(t[0].upper() for t in tokens if t and t[0].isalpha())


def name_class(g_toks: list[str], given: str | None) -> str | None:
    p_toks = [t for t in re.split(r"[ .]+", given or "") if t]
    if not g_toks or not p_toks:
        return None
    gi, pi = initials_of(g_toks), initials_of(p_toks)
    gw = [t.upper() for t in g_toks if len(t) > 2]
    pw = [t.upper() for t in p_toks if len(t) > 2]
    if gw and pw and gw[0] == pw[0] and (gi == pi or pi.startswith(gi)
                                         or gi.startswith(pi)):
        return "forename"
    if gi == pi:
        return "initials_exact"
    if pi.startswith(gi) or gi.startswith(pi):
        return "initials_prefix"
    return None


def main() -> None:
    # ---- stage 1: collapse entries into identities ---------------------
    idents: dict[tuple, dict] = {}
    n_entries = 0
    for f in sorted(glob(str(GRAD / "gradation_1[89]*.jsonl"))):
        for r in map(json.loads, open(f, encoding="utf-8")):
            n_entries += 1
            lt = r.get("list_type")
            entry_year = r.get("commission_year") if lt == "army" \
                else r.get("group_year")
            toks = given_tokens(r.get("given"))
            key = (lt, sk(r.get("surname")), initials_of(toks), entry_year)
            it = idents.get(key)
            if it is None:
                it = idents[key] = {
                    "gradation_id": f"grd_{lt}_{sk(r.get('surname'))}_"
                                    f"{initials_of(toks) or 'X'}_"
                                    f"{entry_year or 0}",
                    "list_type": lt, "surname": r.get("surname"),
                    "given": r.get("given"), "entry_year": entry_year,
                    "editions": set(), "sections": set(),
                    "corps": set(), "establishments": set(),
                    "appointments": set(), "honours": set(),
                    "n_entries": 0}
            it["n_entries"] += 1
            it["editions"].add(r["edition_year"])
            if len(r.get("given") or "") > len(it["given"] or ""):
                it["given"] = r.get("given")   # keep the fullest form
            if r.get("section"):
                it["sections"].add(r["section"])
            if r.get("corps"):
                it["corps"].add(r["corps"])
            if r.get("establishment"):
                it["establishments"].add(r["establishment"])
            if r.get("appointment"):
                it["appointments"].add(r["appointment"][:80])
            for h in r.get("honours") or []:
                it["honours"].add(sk(h))

    # ---- person index --------------------------------------------------
    persons = [json.loads(l) for l in
               open(ROOT / "llm_struct_corpus.stage3.deduped.jsonl",
                    encoding="utf-8")]
    by_surname: dict[str, list[dict]] = defaultdict(list)
    for p in persons:
        eds = set(p.get("editions") or [])
        ev_years = set()
        stems = set()
        places = set()
        entry_years = set()
        for e in p.get("events") or []:
            y = e.get("year_start")
            if y:
                ev_years.add(y)
                pos = (e.get("position") or "").lower()
                if y < 1930 and ("appointed" in pos or "arrived" in pos
                                 or "entered" in pos):
                    entry_years.add(y)
            st = posstem(e.get("position"))
            if len(st) >= 4:
                stems.add(st)
            pl = sk(e.get("place"))[:12]
            if pl:
                places.add(pl)
        if ev_years:
            entry_years.add(min(ev_years))   # earliest event ~ entry
        by_surname[sk(p.get("surname"))].append({
            "person_id": p["person_id"], "given": p.get("given_names"),
            "first_ed": min(eds) if eds else None,
            "entry_years": entry_years, "stems": stems, "places": places,
            "honour_keys": {sk(h.get("award")) for h in
                            (p.get("honours") or []) if h.get("award")}})
    surname_freq = {k: len(v) for k, v in by_surname.items()}

    # ---- stage 2: link ---------------------------------------------------
    links, ambiguous = [], []
    stats = Counter()
    corro = Counter()
    for key, it in idents.items():
        stats["identities"] += 1
        g_toks = given_tokens(it["given"])
        cands = []
        for c in by_surname.get(key[1], []):
            nc = name_class(g_toks, c["given"])
            if nc is None:
                continue
            # the person's record must not START implausibly before the
            # identity: an officer commissioned in 1900 cannot be a person
            # whose career ended before that
            ey = it["entry_year"]
            score = {"forename": 40, "initials_exact": 30,
                     "initials_prefix": 15}[nc]
            freq = surname_freq[key[1]]
            score += 15 if freq <= 3 else (
                5 if freq <= 10 else (-15 if freq >= 30 else 0))
            flags = []
            if ey and any(abs(ey - py) <= 1 for py in c["entry_years"]):
                score += 30
                flags.append("entry_year")
            if it["establishments"] and any(
                    sk(est)[:12] in c["places"]
                    for est in it["establishments"]):
                score += 10
                flags.append("establishment")
            if any(posstem(a) in c["stems"]
                   for a in it["appointments"] if len(posstem(a)) >= 4):
                score += 20
                flags.append("appointment")
            if it["honours"] & c["honour_keys"]:
                score += 15
                flags.append("honours")
            cands.append({"person_id": c["person_id"],
                          "given": c["given"], "name_class": nc,
                          "score": score, "corro": flags})
        cands = [c for c in cands if c["score"] >= WEAK_SCORE]
        if not cands:
            stats["no_candidate"] += 1
            continue
        cands.sort(key=lambda c: -c["score"])
        if len(cands) > 1 and cands[0]["score"] - cands[1]["score"] < GAP:
            stats["ambiguous"] += 1
            ambiguous.append({"gradation_id": it["gradation_id"],
                              "surname": it["surname"],
                              "given": it["given"],
                              "entry_year": it["entry_year"],
                              "list_type": it["list_type"],
                              "candidates": cands[:4]})
            continue
        top = cands[0]
        if top["score"] < MIN_SCORE:
            tier = "weak"
        elif top["score"] >= 60 or len(top["corro"]) >= 2:
            tier = "strong"
        else:
            tier = "standard"
        stats["linked"] += 1
        stats[f"tier_{tier}"] += 1
        stats[f"linked_{it['list_type']}"] += 1
        for fl in top["corro"] or ["name_only"]:
            corro[fl] += 1
        links.append({"gradation_id": it["gradation_id"],
                      "list_type": it["list_type"],
                      "surname": it["surname"], "given": it["given"],
                      "entry_year": it["entry_year"],
                      "editions": [min(it["editions"]),
                                   max(it["editions"])],
                      "person_id": top["person_id"],
                      "person_given": top["given"],
                      "name_class": top["name_class"],
                      "score": top["score"], "tier": tier,
                      "corroboration": top["corro"]})

    def ident_json(it: dict) -> dict:
        out = dict(it)
        for k in ("editions", "sections", "corps", "establishments",
                  "appointments", "honours"):
            out[k] = sorted(out[k])
        return out

    with open(GRAD / "gradation_identities.jsonl", "w",
              encoding="utf-8") as fh:
        for it in idents.values():
            fh.write(json.dumps(ident_json(it), ensure_ascii=False) + "\n")
    with open(GRAD / "gradation_person_links.jsonl", "w",
              encoding="utf-8") as fh:
        for r in links:
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")
    with open(GRAD / "gradation_link_ambiguous.jsonl", "w",
              encoding="utf-8") as fh:
        for r in ambiguous:
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")

    pre86 = sum(1 for it in idents.values()
                if it["editions"] and min(it["editions"]) < 1886)
    linked_pre86 = sum(1 for r in links if r["editions"][0] < 1886)
    lines = [
        "# Gradation -> person links",
        "",
        f"{n_entries:,} gradation entries -> **{stats['identities']:,} "
        f"identities** (commission/covenant-year keyed; {pre86:,} attested "
        "before 1886, i.e. before the Record of Services exists).",
        "",
        f"Linked **{stats['linked']:,}** identities "
        f"(army {stats['linked_army']:,} / civil {stats['linked_civil']:,}; "
        f"tiers strong {stats['tier_strong']:,} / standard "
        f"{stats['tier_standard']:,} / weak {stats['tier_weak']:,}), "
        f"ambiguous {stats['ambiguous']:,}, no candidate "
        f"{stats['no_candidate']:,}.",
        f"Links whose gradation trace starts pre-1886: {linked_pre86:,} "
        "— these EXTEND known careers backwards.",
        "",
        "Corroboration (multi-count): "
        + ", ".join(f"{k} {v:,}" for k, v in corro.most_common()),
        "",
        "Scoring: name class 15-40, surname rarity ±15, entry-year "
        "agreement ±1 +30 (commission/covenant year vs bio entry "
        "events), establishment-place +10, appointment-stem +20, "
        f"honours +15; accept ≥{MIN_SCORE} (weak tier ≥{WEAK_SCORE}) "
        f"with a ≥{GAP} gap.",
        "",
        "Unlinked pre-1886 identities are the spine for linking the "
        "1861-85 casualties (iol_link_exits.py residue).",
    ]
    (GRAD / "GRADATION_LINKS.md").write_text("\n".join(lines) + "\n",
                                             encoding="utf-8")
    print("\n".join(lines))
    print("\nstats:", dict(stats))


if __name__ == "__main__":
    main()
