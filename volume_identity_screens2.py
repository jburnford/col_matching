#!/usr/bin/env python3
"""Tier-A identity screens, second pass: A3+A4+A5 (IDENTITY_QA_ROADMAP).

  A3  Salary/rank regression inside strung careers. A career whose peak
      salary collapses >60% mid-stream and STAYS down is a senior+junior
      namesake pair — the son entering at the bottom as the father peaks.
      The split point is the collapse year.

  A4  Trajectory incoherence. Real careers move in geographic blocks;
      interleaved namesakes alternate (Ceylon 1900, Jamaica 1901, Ceylon
      1902). Score bio-person event sequences for A-B-A colony returns
      with short periods; >=2 independent alternations flags a fused
      person (one can be a genuine secondment).

  A5  Implausible multi-post years. Same-year multi-department listings
      are normal small-colony pluralism (Treasury + Gaol) — unless the
      departments span professionalized services that were never combined
      (Police + Education + Railways): a namesake signature.

Inputs  data/volume/careers/careers.jsonl, bio_persons/bio_persons.jsonl
Outputs data/volume/identity/{a3_salary_regression,a4_place_alternation,
        a5_multipost_incompatible}.jsonl + SCREENS2.md

Candidates only; nothing applied. Salary parsing follows the verified
list_vs_bio_v2 rules (scale chains, Rs at 15:1 flagged).
"""

from __future__ import annotations

import json
import re
from collections import Counter, defaultdict
from pathlib import Path

from col_match.config import Config
from col_match.services import gazetteer

ROOT = Path("data/volume")
OUT = ROOT / "identity"
DATA_DIR = Config.from_env().data_dir

# ----------------------------------------------------------------- salary --

_AMT = re.compile(r"([\d,]+)\s*(?:l\.|£|/)")
_RS = re.compile(r"Rs\.?\s*([\d,]+)")
RS_RATE = 15


def salary_peak(s: str | None) -> int | None:
    """Peak of a salary string; scale chains use the largest amount,
    increments (<20) dropped; Rs converts at 15:1 (as in list_vs_bio_v2)."""
    if not s:
        return None
    rs = [int(d) // RS_RATE for a in _RS.findall(s)
          if (d := a.replace(",", ""))]
    rs = [r for r in rs if r >= 20]
    if rs:
        return max(rs)
    amts = [int(d) for a in _AMT.findall(s) if (d := a.replace(",", ""))]
    # >10,000l outranks a governor — OCR garble, not pay
    amts = [a for a in amts if 20 <= a <= 10_000]
    return max(amts) if amts else None


def screen_a3(careers: list[dict]) -> list[dict]:
    hits = []
    for c in careers:
        if c.get("suspect"):
            continue
        by_year: dict[int, int] = {}
        for r in c["records"]:
            p = salary_peak(r.get("salary"))
            if p is not None:
                y = r["year"]
                by_year[y] = max(by_year.get(y, 0), p)
        years = sorted(by_year)
        if len(years) < 4:
            continue
        best = None
        for i in range(1, len(years) - 1):
            # peak must persist >=2 years — a one-year spike is OCR garble
            highs = sorted((by_year[y] for y in years[:i + 1]), reverse=True)
            if len(highs) < 2 or highs[1] < 400:
                continue
            before = highs[1]
            after = max(by_year[y] for y in years[i + 1:])
            # collapse: officer-level peak, then EVERY later year under 40%
            if after <= 0.4 * before and len(years) - i - 1 >= 2:
                drop = 1 - after / before
                if best is None or drop > best["drop"]:
                    best = {"split_after": years[i], "peak_before": before,
                            "peak_after": after, "drop": round(drop, 2)}
        if best:
            hits.append({
                "career_id": c["career_id"], "colony": c["colony"],
                "surname": c["surname"], "given_names": c["given_names"],
                "years": years, "salary_by_year": by_year,
                "bio_ids": c.get("bio_ids", []), **best,
            })
    hits.sort(key=lambda h: -h["drop"])
    return hits


# ------------------------------------------------------------ alternation --

_canon_cache: dict[str, str | None] = {}


def place_colony(place: str | None, canon: set[str]) -> str | None:
    """Resolve a bio event place to a known roster colony, or None."""
    if not place:
        return None
    if place not in _canon_cache:
        targets = gazetteer.colony_targets(place, DATA_DIR) & canon
        _canon_cache[place] = next(iter(targets)) if len(targets) == 1 \
            else None
    return _canon_cache[place]


STRUCTURAL_PAIR_MIN = 10   # pairs alternating for this many persons are
                           # administrative couples (SS/FMS, Fiji/W.Pacific)


def person_alternations(p: dict, canon: set[str]):
    seq = []
    for ev in sorted(p["events"], key=lambda e: e.get("year_start") or 9999):
        y = ev.get("year_start")
        col = place_colony(ev.get("place"), canon)
        if y and col:
            if not seq or seq[-1][1] != col:
                seq.append((y, col))
    # A-B-A returns where the away leg is short (<=4 years total)
    alts = []
    for i in range(len(seq) - 2):
        (y1, a), (y2, b), (y3, a2) = seq[i], seq[i + 1], seq[i + 2]
        if a == a2 and a != b and y3 - y1 <= 4:
            alts.append({"colony_a": a, "colony_b": b,
                         "years": [y1, y2, y3]})
    return seq, alts


def screen_a4(persons: list[dict], canon: set[str]) -> list[dict]:
    # pass 1: colony pairs that alternate for MANY distinct persons are
    # structurally coupled services, not namesake signatures — learn and
    # exclude them (the corpus's own majority vote)
    per_pair_persons = defaultdict(set)
    cache = {}
    for p in persons:
        cache[p["person_id"]] = seq_alts = person_alternations(p, canon)
        for al in seq_alts[1]:
            pair = tuple(sorted([al["colony_a"], al["colony_b"]]))
            per_pair_persons[pair].add(p["person_id"])
    structural = {pair for pair, ids in per_pair_persons.items()
                  if len(ids) >= STRUCTURAL_PAIR_MIN}

    hits = []
    for p in persons:
        seq, all_alts = cache[p["person_id"]]
        alts = [al for al in all_alts
                if tuple(sorted([al["colony_a"], al["colony_b"]]))
                not in structural]
        if len(alts) >= 2:
            hits.append({
                "person_id": p["person_id"], "surname": p["surname"],
                "given_names": p["given_names"],
                "birth_year": p.get("birth_year"),
                "n_members": p["n_members"],
                "n_alternations": len(alts), "alternations": alts,
                "colony_sequence": [[y, c] for y, c in seq],
            })
    hits.sort(key=lambda h: -h["n_alternations"])
    return hits, sorted(structural)


# -------------------------------------------------------------- multi-post --

# department families; the FAR set never shares one officer in one year
_FAMILIES = [
    ("POLICE", re.compile(r"police|constabulary|gaol|prison", re.I)),
    ("MEDICAL", re.compile(r"medical|hospital|health|lunatic|asylum|quarantine", re.I)),
    ("EDUCATION", re.compile(r"education|school|college", re.I)),
    ("TRANSPORT", re.compile(r"railway|marine|harbour|port|tramway", re.I)),
    ("JUDICIAL", re.compile(r"court|judicial|magistrate|justice|attorney|legal", re.I)),
    ("LANDS", re.compile(r"survey|lands?\b|agricult|forest|mines|geolog", re.I)),
    ("REVENUE", re.compile(r"treasur|customs|audit|revenue|post office|postal|taxes", re.I)),
    ("SECRETARIAT", re.compile(r"secretar|council|governor|administrat|civil establishment|executive|legislative", re.I)),
]
_FAR = {"POLICE", "MEDICAL", "EDUCATION", "TRANSPORT"}


def dept_family(dept: str | None, position: str | None) -> str | None:
    txt = f"{dept or ''} {position or ''}"
    for fam, rx in _FAMILIES:
        if rx.search(txt):
            return fam
    return None


def screen_a5(careers: list[dict]) -> list[dict]:
    hits = []
    for c in careers:
        if c.get("suspect") or not c.get("multi_post_years"):
            continue
        bad_years = []
        for y in c["multi_post_years"]:
            # salaried posts only — unpaid board/council seats are the
            # normal pluralism of small-colony elites
            recs = [r for r in c["records"] if r["year"] == y
                    and salary_peak(r.get("salary"))]
            fams = {f for r in recs
                    if (f := dept_family(r.get("department"),
                                         r.get("position")))}
            far = fams & _FAR
            if len(far) >= 2 or (len(far) >= 1 and len(fams) >= 3):
                bad_years.append({
                    "year": y, "families": sorted(fams),
                    "posts": [f"{r.get('department')}: {r.get('position')}"
                              for r in recs],
                })
        if bad_years:
            hits.append({
                "career_id": c["career_id"], "colony": c["colony"],
                "surname": c["surname"], "given_names": c["given_names"],
                "bio_ids": c.get("bio_ids", []),
                "bad_years": bad_years,
            })
    return hits


# ------------------------------------------------------------------- main --

def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    careers = [json.loads(l) for l in
               open(ROOT / "careers/careers.jsonl", encoding="utf-8")]
    persons = [p for p in map(json.loads,
                              open(ROOT / "bio_persons/bio_persons.jsonl",
                                   encoding="utf-8"))
               if "not_a_person" not in p["flags"]]
    canon: set[str] = set()
    for c in careers:
        canon |= gazetteer.colony_targets(c["colony"], DATA_DIR)

    a3 = screen_a3(careers)
    a4, structural = screen_a4(persons, canon)
    a5 = screen_a5(careers)

    for name, rows in [("a3_salary_regression", a3),
                       ("a4_place_alternation", a4),
                       ("a5_multipost_incompatible", a5)]:
        with open(OUT / f"{name}.jsonl", "w", encoding="utf-8") as f:
            for r in rows:
                f.write(json.dumps(r, ensure_ascii=False) + "\n")

    lines = [
        "# Tier-A identity screens, second pass",
        "",
        f"Over {len(careers):,} careers and {len(persons):,} persons.",
        "",
        "## A3 salary collapse inside a career (senior+junior namesakes)",
        f"- careers flagged: **{len(a3)}** (peak >=400l then every later"
        " year <=40% of peak, >=2 years each side)",
        "",
        "## A4 A-B-A colony alternation (fused namesakes)",
        f"- persons flagged: **{len(a4)}** (>=2 short-period returns;"
        f" {len(structural)} structurally coupled colony pairs excluded:"
        f" {', '.join('/'.join(p) for p in structural[:8])} ...)",
        "",
        "## A5 incompatible same-year multi-department posts",
        f"- careers flagged: **{len(a5)}** (>=2 professionalized services"
        " in one year, or 1 + >=3 families)",
        "",
        "Candidates only; feed the adjudication ledger.",
    ]
    (OUT / "SCREENS2.md").write_text("\n".join(lines) + "\n",
                                     encoding="utf-8")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
