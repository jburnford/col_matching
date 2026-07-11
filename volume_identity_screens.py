#!/usr/bin/env python3
"""Tier-A identity screens over the unified bio-persons (IDENTITY_QA_ROADMAP A1+A2+A6).

Deterministic fingerprints for over- and under-merged persons, no GPU:

  A1  Honours-precedence violations. Within one order grades only ascend
      (C.M.G. -> K.C.M.G. -> G.C.M.G.). A person whose earliest attestation
      of a LOWER grade postdates a higher one is either two people fused or
      carries a garbled award year. The violating pair localizes the split.

  A2  Age invariants. Entry age <13 or >65, or active service past 75.
      IMPORTANT: birth years are OCR-fragile (b.1888 holding an 1853
      ensigncy), so every hit is first attacked as a digit-garble — we
      search one-digit repairs of the birth year that land entry age in the
      plausible band (15-35) — and only escalates to a dynastic/over-merge
      candidate when no repair explains the events. Same rule
      auto-adjudicates the persons already flagged `birth_year_conflict`:
      prefer the vote whose reading lands entry age in-band.

  A6  Same-rare-honour duplicates (UNDER-merge). An award x year x surname
      is a near-unique key (orders appoint once); two distinct persons with
      compatible given names claiming the same one are one person split.
      Edition-disjoint pairs are the strong candidates.

Inputs  data/volume/bio_persons/bio_persons.jsonl
Outputs data/volume/identity/{a1_honour_precedence,a2_age_invariants,
        a2_birthyear_resolutions,a6_honour_duplicates}.jsonl + SCREENS.md

Candidates feed the adjudication ledger (undermerge_decisions.jsonl format:
person_a/person_b/decision/reason); nothing here mutates the person table.
"""

from __future__ import annotations

import json
import re
from collections import Counter, defaultdict
from pathlib import Path

from col_match.services.compile import _names_compatible

ROOT = Path("data/volume")
OUT = ROOT / "identity"

# ---------------------------------------------------------------- honours --

# Grade ladders per order, junior -> senior. Dames share the knights' slot.
ORDER_LADDERS = {
    "St Michael & St George": ["CMG", "KCMG", "GCMG"],
    "Bath": ["CB", "KCB", "GCB"],
    "British Empire": ["MBE", "OBE", "CBE", "KBE", "GBE"],
    "Star of India": ["CSI", "KCSI", "GCSI"],
    "Indian Empire": ["CIE", "KCIE", "GCIE"],
    "Royal Victorian": ["MVO", "CVO", "KCVO", "GCVO"],
}
_ALIAS = {"DBE": "KBE", "DCMG": "KCMG", "DCVO": "KCVO"}

_TOKEN_ORDER: dict[str, tuple[str, int]] = {}
for _order, _ladder in ORDER_LADDERS.items():
    for _rank, _tok in enumerate(_ladder):
        _TOKEN_ORDER[_tok] = (_order, _rank)
for _a, _b in _ALIAS.items():
    _TOKEN_ORDER[_a] = _TOKEN_ORDER[_b]

# Dotted-sequence patterns ("K.C.M.G", "K C M G", "KCMG"), longest token
# first so C.M.G never fires inside K.C.M.G, nor C.B inside C.B.E.
_TOKEN_RX = [
    (tok, re.compile(
        r"(?<![A-Za-z])" + r"\.?\s*".join(tok) + r"\.?(?![A-Za-z])"))
    for tok in sorted(_TOKEN_ORDER, key=len, reverse=True)
]


def award_token(award: str | None) -> str | None:
    """Normalize a messy bio award string to a ladder token, or None."""
    if not award:
        return None
    for tok, rx in _TOKEN_RX:
        if rx.search(award):
            return _ALIAS.get(tok, tok)
    return None


def screen_a1(persons: list[dict]) -> list[dict]:
    hits = []
    for p in persons:
        # earliest attested year per (order, grade)
        first: dict[tuple[str, int], int] = {}
        for h in p["honours"]:
            tok, year = award_token(h.get("award")), h.get("year")
            if tok is None or not year:
                continue
            order, rank = _TOKEN_ORDER[tok]
            key = (order, rank)
            if key not in first or year < first[key]:
                first[key] = year
        by_order: dict[str, list[tuple[int, int]]] = defaultdict(list)
        for (order, rank), year in first.items():
            by_order[order].append((rank, year))
        violations = []
        for order, grades in by_order.items():
            grades.sort()
            for i, (rlo, ylo) in enumerate(grades):
                for rhi, yhi in grades[i + 1:]:
                    if ylo > yhi:
                        ladder = ORDER_LADDERS[order]
                        violations.append({
                            "order": order,
                            "lower": ladder[rlo], "lower_year": ylo,
                            "higher": ladder[rhi], "higher_year": yhi,
                            # 3-digit / pre-order years are OCR truncations
                            # ("KCMG 181"), not identity evidence
                            "suspect_garbled_year":
                                ylo < 1815 or yhi < 1815,
                        })
        if violations:
            hits.append({
                "person_id": p["person_id"], "surname": p["surname"],
                "given_names": p["given_names"],
                "birth_year": p["birth_year"],
                "n_members": p["n_members"], "editions": p["editions"],
                "violations": violations,
                "honours": p["honours"],
            })
    return hits


# ------------------------------------------------------------------- ages --

ENTRY_LO, ENTRY_HI = 13, 65          # invariant band (flag outside)
PLAUS_LO, PLAUS_HI = 15, 35          # plausible entry band (repair target)
MAX_ACTIVE_AGE = 75
BIRTH_LO, BIRTH_HI = 1770, 1950


def event_years(p: dict) -> list[int]:
    ys = []
    for e in p["events"]:
        for k in ("year_start", "year_end"):
            y = e.get(k)
            if y and 1750 <= y <= 1970:
                ys.append(y)
    return ys


def digit_repairs(year: int, entry_year: int, subs: int = 1) -> list[int]:
    """Substitutions of up to `subs` digits of `year` landing entry age
    in-band. Birth years are OCR-fragile; a printed 1848 can be a true
    1812 (two digits), so callers try subs=1 then subs=2."""
    s = str(year)
    cands = {s}
    for _ in range(subs):
        cands |= {c[:i] + d + c[i + 1:]
                  for c in cands for i in range(len(c)) for d in "0123456789"}
    out = set()
    for c in cands:
        cand = int(c)
        if cand != year and BIRTH_LO <= cand <= BIRTH_HI \
                and PLAUS_LO <= entry_year - cand <= PLAUS_HI:
            out.add(cand)
    return sorted(out)


def screen_a2_invariants(persons: list[dict]) -> list[dict]:
    hits = []
    for p in persons:
        by = p.get("birth_year")
        if not by:
            continue
        ys = event_years(p)
        if not ys:
            continue
        entry_age = min(ys) - by
        last_age = max(ys) - by
        flags = []
        if entry_age < ENTRY_LO:
            flags.append("entry_too_young")
        if entry_age > ENTRY_HI:
            flags.append("entry_too_old")
        if last_age > MAX_ACTIVE_AGE:
            flags.append("active_past_75")
        if not flags:
            continue
        # A repair only explains the person if the WHOLE career fits one
        # lifetime under it; otherwise the events span two lives.
        def fits(r: int) -> bool:
            return max(ys) - r <= MAX_ACTIVE_AGE
        span = max(ys) - min(ys)
        repairs = [r for r in digit_repairs(by, min(ys), subs=1) if fits(r)]
        repairs2 = [] if repairs else \
            [r for r in digit_repairs(by, min(ys), subs=2) if fits(r)]
        # entry 15-35 + last <=75 means any span <=60 career fits SOME
        # lifetime; a person no repair reaches, or whose span exceeds one
        # service life, is two people fused.
        if repairs:
            diagnosis = "birth_year_ocr"          # garbled digits, fixable
        elif span > 60 or not repairs2:
            diagnosis = "dynastic_merge_candidate"  # two lifetimes fused
        else:
            diagnosis = "birth_year_ocr_2digit"   # weaker: 2-digit repair
            repairs = repairs2
        hits.append({
            "person_id": p["person_id"], "surname": p["surname"],
            "given_names": p["given_names"], "birth_year": by,
            "entry_year": min(ys), "last_year": max(ys),
            "entry_age": entry_age, "last_age": last_age,
            "event_span": span, "n_members": p["n_members"],
            "flags": flags, "diagnosis": diagnosis,
            "suggested_birth_years": repairs,
        })
    return hits


def screen_a2_birth_from_honour(persons: list[dict]) -> list[dict]:
    """Spot-check find (2026-07-11): the bio parser sometimes absorbs an
    honour year as the birth year (HENNESSY 'b.1880' = his K.C.M.G. year;
    career from 1859). Signature: birth_year equals an honour year AND the
    career starts >5 years before it. Repair: null the birth year — do NOT
    digit-repair it."""
    out = []
    for p in persons:
        by = p.get("birth_year")
        if not by:
            continue
        if by not in {h.get("year") for h in p["honours"]}:
            continue
        ys = event_years(p)
        if ys and min(ys) < by - 5:
            out.append({
                "person_id": p["person_id"], "surname": p["surname"],
                "given_names": p["given_names"], "birth_year": by,
                "matching_honours": [h for h in p["honours"]
                                     if h.get("year") == by],
                "entry_year": min(ys),
                "action": "null_birth_year_absorbed_honour",
            })
    return out


def screen_a2_conflicts(persons: list[dict]) -> list[dict]:
    """Auto-adjudicate flagged birth-year conflicts: prefer the vote whose
    reading lands entry age in the plausible band."""
    out = []
    for p in persons:
        if "birth_year_conflict" not in p["flags"]:
            continue
        votes = {int(y): n for y, n in (p.get("birth_year_votes") or {}).items()}
        ys = event_years(p)
        entry = min(ys) if ys else None
        scored = []
        for y, n in sorted(votes.items()):
            age = entry - y if entry else None
            plaus = age is not None and PLAUS_LO <= age <= PLAUS_HI
            ok = age is not None and ENTRY_LO <= age <= ENTRY_HI
            scored.append({"year": y, "votes": n, "entry_age": age,
                           "plausible": plaus, "in_band": ok})
        plaus = [s for s in scored if s["plausible"]]
        inband = [s for s in scored if s["in_band"]]
        if len(plaus) == 1:
            resolution, pick = "unique_plausible", plaus[0]["year"]
        elif len(plaus) > 1:
            pick = max(plaus, key=lambda s: s["votes"])["year"]
            resolution = "majority_of_plausible"
        elif len(inband) >= 1:
            pick = max(inband, key=lambda s: s["votes"])["year"]
            resolution = "band_relaxed"
        else:
            pick = None
            resolution = ("no_plausible_reading_span2lives"
                          if ys and max(ys) - min(ys) > 55
                          else "no_plausible_reading")
        out.append({
            "person_id": p["person_id"], "surname": p["surname"],
            "given_names": p["given_names"],
            "current_birth_year": p.get("birth_year"),
            "entry_year": entry, "last_year": max(ys) if ys else None,
            "candidates": scored, "resolution": resolution,
            "suggested_birth_year": pick,
            "n_members": p["n_members"],
        })
    return out


# -------------------------------------------------------------- duplicates --

def _surname_key(s: str | None) -> str:
    return re.sub(r"[^A-Z]", "", (s or "").upper())


def screen_a6(persons: list[dict]) -> list[dict]:
    groups: dict[tuple[str, str, int], list[dict]] = defaultdict(list)
    for p in persons:
        seen = set()
        for h in p["honours"]:
            tok, year = award_token(h.get("award")), h.get("year")
            if tok is None or not year or (tok, year) in seen:
                continue
            seen.add((tok, year))
            groups[(_surname_key(p["surname"]), tok, year)].append(p)
    pairs = []
    for (skey, tok, year), members in groups.items():
        if not skey or len(members) < 2:
            continue
        for i, a in enumerate(members):
            for b in members[i + 1:]:
                if a["person_id"] == b["person_id"]:
                    continue
                if not _names_compatible(a["given_names"], b["given_names"]):
                    continue
                shared_ed = sorted(set(a["editions"]) & set(b["editions"]))
                ga = [t for t in re.split(r"[ .]+", a["given_names"] or "") if t]
                gb = [t for t in re.split(r"[ .]+", b["given_names"] or "") if t]
                full_names = min(len(t) for t in ga[:1] + gb[:1]) > 1 \
                    if ga and gb else False
                by_a, by_b = a.get("birth_year"), b.get("birth_year")
                pairs.append({
                    "person_a": a["person_id"], "person_b": b["person_id"],
                    "surname": a["surname"],
                    "given_a": a["given_names"], "given_b": b["given_names"],
                    "award": tok, "award_year": year,
                    "birth_a": by_a, "birth_b": by_b,
                    "birth_agree": bool(by_a and by_b and by_a == by_b),
                    "birth_conflict": bool(by_a and by_b and by_a != by_b),
                    "editions_disjoint": not shared_ed,
                    "shared_editions": shared_ed,
                    "full_given_names": full_names,
                })
    # strongest first: disjoint editions + agreeing birth years + full names
    pairs.sort(key=lambda r: (
        not r["editions_disjoint"], r["birth_conflict"],
        not r["birth_agree"], not r["full_given_names"],
        r["surname"], r["award_year"]))
    return pairs


# ------------------------------------------------------------------- main --

def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    persons = []
    for line in open(ROOT / "bio_persons" / "bio_persons.jsonl",
                     encoding="utf-8"):
        p = json.loads(line)
        if "not_a_person" in p["flags"]:
            continue
        persons.append(p)

    a1 = screen_a1(persons)
    a2 = screen_a2_invariants(persons)
    a2c = screen_a2_conflicts(persons)
    a2h = screen_a2_birth_from_honour(persons)
    a6 = screen_a6(persons)

    for name, rows in [("a1_honour_precedence", a1),
                       ("a2_age_invariants", a2),
                       ("a2_birthyear_resolutions", a2c),
                       ("a2_birth_from_honour", a2h),
                       ("a6_honour_duplicates", a6)]:
        with open(OUT / f"{name}.jsonl", "w", encoding="utf-8") as f:
            for r in rows:
                f.write(json.dumps(r, ensure_ascii=False) + "\n")

    diag = Counter(r["diagnosis"] for r in a2)
    res = Counter(r["resolution"] for r in a2c)
    flags = Counter(f for r in a2 for f in r["flags"])
    a6_strong = sum(1 for r in a6 if r["editions_disjoint"]
                    and not r["birth_conflict"])
    lines = [
        "# Tier-A identity screens",
        "",
        f"Over {len(persons):,} persons (not_a_person excluded).",
        "",
        "## A1 honours-precedence violations (over-merge / garbled year)",
        f"- persons flagged: **{len(a1)}**",
        "",
        "## A2 age invariants",
        f"- persons flagged: **{len(a2)}** "
        f"(entry_too_young {flags.get('entry_too_young', 0)}, "
        f"entry_too_old {flags.get('entry_too_old', 0)}, "
        f"active_past_75 {flags.get('active_past_75', 0)})",
        f"- diagnosis: {dict(diag)}",
        "  - `birth_year_ocr`: a one-digit repair puts entry age 15-35 AND"
        " the whole career inside one lifetime — treat as garbled digits,"
        " not identity error.",
        "  - `birth_year_ocr_2digit`: same but needs two digits — weaker,"
        " verify against the bio text before applying.",
        "  - `dynastic_merge_candidate`: events span >60 years or no"
        " repair reaches a plausible reading — likely two lifetimes fused.",
        "",
        "## A2 birth-year conflict auto-adjudication "
        f"({len(a2c)} flagged persons)",
        f"- resolutions: {dict(res)}",
        "",
        "## A2 birth year absorbed from an honour year (parser bug)",
        f"- persons flagged: **{len(a2h)}** — null the birth year, do not"
        " digit-repair.",
        "",
        "## A6 same-honour duplicate persons (under-merge)",
        f"- candidate pairs: **{len(a6)}**; strong (edition-disjoint, no"
        f" birth conflict): **{a6_strong}**",
        "",
        "Candidate files feed the adjudication ledger; nothing applied.",
    ]
    (OUT / "SCREENS.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
