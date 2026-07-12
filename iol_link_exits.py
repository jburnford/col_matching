#!/usr/bin/env python3
"""Link the casualties exit events (deaths / retirements / resignations)
to the audited IOL person table, and run the A7 screen the corpus never
had data for: EVENTS AFTER DEATH.

A matched death is decisive both ways:
  - person's attestation stops at the death year  -> career terminus
    confirmed, death date attached (an event layer neither the bios nor
    the rolls carry);
  - person keeps appearing, or has career events, AFTER the death year
    -> the person is two people fused (or the link is a namesake) —
    the strongest over-merge fingerprint there is.

Casualty name forms (measured: 69% / 31%):
  "Wheatley, Major W. P. R., D.S.O."      surname-first, rank+honours mixed
  "Infantry Lt.Gen. T. Marrett"           given-first, corps/rank prefix

Matching: surname key + initials/forename compatibility; transparent
points (name class, surname rarity, last-attestation proximity for
deaths); links accepted only when a single candidate clears the bar.
Note: pre-1886 casualties largely predate the biographical record — the
person table is bio-derived, so match volume concentrates 1886+; the
1861-85 events await the gradation linker.

Outputs (data/iol/identity/):
  exit_links.jsonl        accepted links {event.., person_id, score,..}
  exit_ambiguous.jsonl    >1 surviving candidate (adjudication pool)
  a7_events_after_death.jsonl   over-merge candidates
  EXIT_LINKS.md           rates + the A7 table
"""

from __future__ import annotations

import json
import re
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path("data/iol")
OUT = ROOT / "identity"
CAS = ROOT / "casualties"

MIN_SCORE = 45

_RANKS = {
    "lt", "lieut", "lieutenant", "col", "colonel", "major", "maj", "capt",
    "captain", "gen", "genl", "general", "brig", "brigadier", "sir", "dr",
    "mr", "rev", "revd", "hon", "hony", "surg", "surgn", "surgeon", "asst",
    "sergt", "cadet", "ensign", "cornet", "commr", "commander", "cdr",
    "admiral", "esq", "bart", "bt", "miss", "mrs", "lady", "dame", "the",
    "staff", "field", "marshal", "deputy", "dep", "insp", "inspector",
    "pilot",
}
_LETTERS = re.compile(r"^(?:[A-Z]\.?\s*){1,6}$")
_HONOUR = re.compile(
    r"^(?:[A-Z]\.){2,6}$|^(CSI|KCSI|GCSI|CIE|KCIE|GCIE|CB|KCB|GCB|CMG|KCMG"
    r"|GCMG|OBE|CBE|MBE|KBE|DSO|MC|VC|ISO|VD|MD|MA|BA|RE|RA|RN|SC)$")


def sk(s: str | None) -> str:
    return re.sub(r"[^A-Z]", "", (s or "").upper())


def _clean_tokens(part: str) -> list[str]:
    """Drop rank words, honour letter-groups and corps junk from a name
    fragment; keep forename/initial tokens."""
    out = []
    for tok in re.split(r"[ ,]+", part):
        t = tok.strip(" .")
        if not t:
            continue
        low = re.sub(r"[^a-z]", "", t.lower())
        if low in _RANKS:
            continue
        if _HONOUR.match(re.sub(r"[^A-Z]", "", t.upper())) and len(t) <= 8 \
                and (t.isupper() or "." in tok):
            continue
        out.append(t)
    return out


def parse_casualty_name(name: str) -> tuple[str, list[str]] | None:
    """-> (surname, given/initial tokens) or None."""
    name = name.strip(" .,\"'")
    if not name or len(name) < 3:
        return None
    if "," in name:
        surname, rest = name.split(",", 1)
        surname = surname.strip()
        toks = _clean_tokens(rest)
    else:
        toks_all = _clean_tokens(name)
        if not toks_all:
            return None
        surname = toks_all[-1]
        toks = toks_all[:-1]
        # drop leading corps words that survived (capitalized non-initials
        # before the first initial, e.g. "Infantry")
        while toks and len(toks[0]) > 2 and "." not in toks[0] \
                and toks and any("." in t or len(t) <= 2 for t in toks[1:]):
            toks = toks[1:]
    if len(surname) < 3 or not surname[0].isupper() \
            or any(c.isdigit() for c in surname):
        return None
    return surname, toks


def initials_of(tokens: list[str]) -> str:
    return "".join(t[0].upper() for t in tokens if t and t[0].isalpha())


def name_class(cas_toks: list[str], given: str | None) -> str | None:
    """Compatibility class between casualty name tokens and a person's
    given_names; None = incompatible."""
    g_toks = [t for t in re.split(r"[ .]+", given or "") if t]
    if not cas_toks:
        return "surname_only"
    if not g_toks:
        return None
    ci, gi = initials_of(cas_toks), initials_of(g_toks)
    if not ci:
        return "surname_only"
    # full-word forename agreement
    cw = [t.upper() for t in cas_toks if len(t) > 2]
    gw = [t.upper() for t in g_toks if len(t) > 2]
    if cw and gw and cw[0] == gw[0] and (ci == gi or gi.startswith(ci)
                                         or ci.startswith(gi)):
        return "forename"
    if ci == gi:
        return "initials_exact"
    if gi.startswith(ci) or ci.startswith(gi):
        return "initials_prefix"
    return None


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    # adjudicated overrides (accumulative ledger; regenerating this
    # linker's outputs must NOT revert judged decisions):
    #   suppress = link judged a namesake -> never emit
    #   promote  = ambiguous candidate judged same -> accept directly
    suppress, promote = set(), {}
    ov_path = OUT / "exit_link_overrides.jsonl"
    if ov_path.exists():
        for line in open(ov_path, encoding="utf-8"):
            r = json.loads(line)
            if r["action"] == "suppress":
                suppress.add((r["event_id"], r["person_id"]))
            elif r["action"] == "promote":
                promote[r["event_id"]] = r["person_id"]
    # override rows may cite absorbed ids — resolve through the live map
    mmap = {r["person_id"]: r["canonical_person_id"] for r in
            (json.loads(l) for l in
             open(ROOT / "dedup_stage3_merge_map.audited.jsonl"))}
    suppress = {(e, mmap.get(p, p)) for e, p in suppress}
    promote = {e: mmap.get(p, p) for e, p in promote.items()}
    persons = [json.loads(l) for l in
               open(ROOT / "llm_struct_corpus.stage3.deduped.jsonl")]
    by_surname: dict[str, list[dict]] = defaultdict(list)
    for p in persons:
        eds = p.get("editions") or []
        evy = [y for e in (p.get("events") or [])
               for y in (e.get("year_start"), e.get("year_end"))
               if y and 1750 < y < 1970]
        by_surname[sk(p.get("surname"))].append({
            "person_id": p["person_id"], "given": p.get("given_names"),
            "first_ed": min(eds) if eds else None,
            "last_ed": max(eds) if eds else None,
            "ev_years": evy, "birth": p.get("birth_year")})
    surname_freq = {k: len(v) for k, v in by_surname.items()}

    events = []
    for f in sorted(CAS.glob("casualties_*.jsonl")):
        for i, line in enumerate(open(f, encoding="utf-8")):
            r = json.loads(line)
            r["event_id"] = f"{r['edition_tag']}:{i}"
            events.append(r)

    links, ambiguous, a7 = [], [], []
    stats = Counter()
    for ev in events:
        stats["events"] += 1
        if not ev.get("year"):
            stats["no_year"] += 1
            continue
        parsed = parse_casualty_name(ev["name"])
        if not parsed:
            stats["unparsed_name"] += 1
            continue
        surname, toks = parsed
        cands = []
        for c in by_surname.get(sk(surname), []):
            nc = name_class(toks, c["given"])
            if nc is None:
                continue
            # career must not START after the exit event
            if c["first_ed"] and c["first_ed"] > ev["year"] + 2:
                continue
            score = {"forename": 40, "initials_exact": 30,
                     "initials_prefix": 15, "surname_only": 0}[nc]
            freq = surname_freq[sk(surname)]
            score += 15 if freq <= 3 else (5 if freq <= 10 else
                                           (-15 if freq >= 30 else 0))
            after_eds = c["last_ed"] and c["last_ed"] > ev["year"] + 2
            after_evs = [y for y in c["ev_years"] if y > ev["year"] + 1]
            if ev["event"] == "death":
                if c["last_ed"] and abs(c["last_ed"] - ev["year"]) <= 2:
                    score += 25          # attestation stops at death
                if ev["month"] and ev["day"]:
                    score += 5           # exact dates are table-grade rows
            else:
                # retirements: person usually persists in the List; mild
                # bonus when the career reaches the retirement year
                if c["last_ed"] and c["last_ed"] >= ev["year"] - 1:
                    score += 10
            if nc == "surname_only" and freq > 1:
                continue                 # bare surname only viable if unique
            cands.append({**c, "name_class": nc, "score": score,
                          "after_eds": bool(after_eds),
                          "after_event_years": after_evs[:6]})
        # adjudicated overrides: drop judged namesakes, accept judged sames
        cands = [c for c in cands
                 if (ev["event_id"], c["person_id"]) not in suppress]
        forced = [c for c in cands
                  if promote.get(ev["event_id"]) == c["person_id"]]
        if forced:
            cands = [dict(forced[0], score=max(forced[0]["score"],
                                               MIN_SCORE))]
            stats["promoted"] += 1
        cands = [c for c in cands if c["score"] >= MIN_SCORE]
        if not cands:
            stats["no_candidate"] += 1
            continue
        cands.sort(key=lambda c: -c["score"])
        if len(cands) > 1 and cands[0]["score"] - cands[1]["score"] < 15:
            stats["ambiguous"] += 1
            ambiguous.append({"event_id": ev["event_id"],
                              "event": ev["event"], "year": ev["year"],
                              "name": ev["name"],
                              "candidates": [{k: c[k] for k in
                                              ("person_id", "given",
                                               "name_class", "score")}
                                             for c in cands[:4]]})
            continue
        top = cands[0]
        stats[f"linked_{ev['event']}"] += 1
        link = {"event_id": ev["event_id"], "event": ev["event"],
                "name": ev["name"], "person_id": top["person_id"],
                "person_given": top["given"], "name_class": top["name_class"],
                "score": top["score"], "day": ev.get("day"),
                "month": ev.get("month"), "year": ev["year"],
                "place": ev.get("place"),
                "establishment": ev.get("establishment"),
                "last_edition": top["last_ed"]}
        links.append(link)
        if ev["event"] == "death" and (top["after_eds"]
                                       or top["after_event_years"]):
            a7.append({**link,
                       "editions_after_death": top["after_eds"],
                       "event_years_after_death": top["after_event_years"]})

    with open(OUT / "exit_links.jsonl", "w", encoding="utf-8") as fh:
        for r in links:
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")
    with open(OUT / "exit_ambiguous.jsonl", "w", encoding="utf-8") as fh:
        for r in ambiguous:
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")
    with open(OUT / "a7_events_after_death.jsonl", "w",
              encoding="utf-8") as fh:
        for r in a7:
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")

    deaths_linked = stats["linked_death"]
    deaths_total = sum(1 for e in events if e["event"] == "death"
                       and e.get("year"))
    post86 = sum(1 for e in events if e["event"] == "death"
                 and (e.get("year") or 0) >= 1886)
    d86 = sum(1 for r in links if r["event"] == "death"
              and r["year"] >= 1886)
    lines = [
        "# Exit-event links (casualties -> person table)",
        "",
        f"{stats['events']:,} exit events; linked "
        f"{len(links):,} (deaths {deaths_linked:,}/{deaths_total:,}; "
        f"1886+ deaths {d86:,}/{post86:,} = {d86 / max(post86, 1):.0%}), "
        f"ambiguous {stats['ambiguous']:,}, no candidate "
        f"{stats['no_candidate']:,} (pre-1886 events largely predate the "
        "bio-derived person table).",
        "",
        f"## A7: events after death — **{len(a7)}** over-merge candidates",
        "",
        "A linked death after which the person is still attested (later",
        "editions or dated career events) = two people fused or a namesake",
        "link; each row carries the death date and the offending years.",
        "",
        "Ledgers: exit_links.jsonl (career-terminus enrichment; apply as a",
        "death_date overlay), exit_ambiguous.jsonl (adjudication pool),",
        "a7_events_after_death.jsonl (screen output).",
    ]
    (OUT / "EXIT_LINKS.md").write_text("\n".join(lines) + "\n",
                                       encoding="utf-8")
    print("\n".join(lines))
    print("\nstats:", dict(stats))


if __name__ == "__main__":
    main()
