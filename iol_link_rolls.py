#!/usr/bin/env python3
"""Link the honours-roll layer (Star of India / Indian Empire / Crown of
India grade rolls, 81,435 entries 1875-1937) to the audited person table's
honours — the externally-grounded date source the bios lack.

Two payoffs (docs/IOL_NEXT_SESSION.md items 1-2):
  date_fill   bio honour has NO year; a unique roll appointment date on
              (grade, name) supplies one  -> overlay candidates
  conflict    bio honour year DISAGREES with the unique roll date ->
              garbled-year adjudication queue (roll dates are printed
              appointment dates; bios are LLM-parsed prose)

Roll names are given-first full names ("Arthur Henry McMahon"); bio
surnames are surname-only for Europeans but full names for most Indian
officers. So each roll entry gets TWO keys: last-token surname and the
full-name letter key; a bio person matches on either (tier recorded).
Rolls are cumulative across editions, so entries collapse to
(grade, name-key) groups first; a group is usable only when its dated
entries agree on ONE appointment year.

Outputs (data/iol/identity/):
  roll_links.jsonl      one row per matched (person, honour):
                        status agree|date_fill|conflict, roll date,
                        match_tier, claimant counts
  roll_conflicts.jsonl  the conflict subset (adjudication pool)
  ROLL_LINKS.md         rates, delta histogram
Read-only; applies nothing. Overlay apply gates on n_bio_claimants == 1.
"""

from __future__ import annotations

import json
import re
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path("data/iol")
OUT = ROOT / "identity"
ROLLS = ROOT / "honours_rolls"

GRADES = {"GCSI", "KCSI", "CSI", "GCIE", "KCIE", "CIE", "CI"}

_PREFIXES = {
    "sir", "lord", "the", "rt", "right", "hon", "honble", "hony", "rev",
    "revd", "dr", "mr", "col", "colonel", "lt", "lieut", "lieutenant",
    "maj", "major", "gen", "genl", "general", "capt", "captain", "brig",
    "brigadier", "surg", "surgn", "surgeon", "admiral", "cdr", "commander",
    "field", "marshal", "staff", "hh", "he", "hrh", "hm", "her", "his",
    "majesty", "highness", "excellency", "prince", "princess", "lady",
    "dame", "miss", "mrs", "vice", "rear", "air", "esq",
}


def lk(s: str | None) -> str:
    """Letter key: uppercase letters only."""
    return re.sub(r"[^A-Z]", "", (s or "").upper())


def award_key(a: str | None) -> str:
    return re.sub(r"[^A-Z]", "", (a or "").upper())


def roll_name_tokens(name: str) -> list[str]:
    """Given-first roll name -> name tokens (prefix ranks/styles dropped,
    territorial tail after a comma dropped)."""
    head = name.split(",", 1)[0]
    toks = [t.strip(" .") for t in re.split(r"[ ]+", head) if t.strip(" .")]
    while toks and re.sub(r"[^a-z]", "", toks[0].lower()) in _PREFIXES:
        toks = toks[1:]
    return [t for t in toks if any(c.isalpha() for c in t)]


def initials_of(tokens: list[str]) -> str:
    return "".join(t[0].upper() for t in tokens if t and t[0].isalpha())


def given_compat(roll_toks: list[str], given: str | None) -> str:
    """Compatibility of roll given names (all tokens but last) with the
    person's given_names."""
    g_toks = [t for t in re.split(r"[ .]+", given or "") if t]
    r_toks = roll_toks[:-1]
    if not r_toks or not g_toks:
        return "none"
    ri, gi = initials_of(r_toks), initials_of(g_toks)
    rw = [t.upper() for t in r_toks if len(t) > 2]
    gw = [t.upper() for t in g_toks if len(t) > 2]
    if rw and gw and rw[0] == gw[0]:
        return "forename"
    if ri and gi and (ri == gi or ri.startswith(gi) or gi.startswith(ri)):
        return "initials"
    return "mismatch"


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)

    # ---- roll side: (grade, key) -> group of entries -------------------
    groups: dict[tuple[str, str], list[dict]] = defaultdict(list)
    n_entries = 0
    for f in sorted(ROLLS.glob("rolls_*.jsonl")):
        for line in open(f, encoding="utf-8"):
            r = json.loads(line)
            if r.get("grade") not in GRADES:
                continue
            n_entries += 1
            toks = roll_name_tokens(r.get("name") or "")
            if not toks:
                continue
            entry = {"name": r["name"], "toks": toks,
                     "year": r.get("appt_year"), "month": r.get("appt_month"),
                     "day": r.get("appt_day"), "edition": r["edition_tag"]}
            keys = {(r["grade"], lk(toks[-1])), (r["grade"], lk("".join(toks)))}
            for k in keys:
                if k[1]:
                    groups[k].append(entry)

    def group_date(entries: list[dict]):
        """-> (year, month, day, n_dated, distinct_years) for a group;
        usable only when dated entries agree on one year."""
        dated = [e for e in entries if e.get("year")]
        years = sorted({e["year"] for e in dated})
        if len(years) != 1:
            return None, None, None, len(dated), years
        best = max(dated, key=lambda e: ((e.get("month") or 0),
                                         (e.get("day") or 0)))
        return years[0], best.get("month"), best.get("day"), len(dated), years

    # ---- bio side ------------------------------------------------------
    persons = [json.loads(l) for l in
               open(ROOT / "llm_struct_corpus.stage3.deduped.jsonl",
                    encoding="utf-8")]

    # claimant counts: how many canonical persons carry (grade, key)
    claimants: Counter = Counter()
    person_award_keys = []
    for p in persons:
        seen = set()
        for h in p.get("honours") or []:
            ak = award_key(h.get("award"))
            if ak not in GRADES or ak in seen:
                continue
            seen.add(ak)
            for key in {(ak, lk(p.get("surname"))),
                        (ak, lk((p.get("given_names") or "")
                                + (p.get("surname") or "")))}:
                if key[1]:
                    claimants[key] += 1
        person_award_keys.append(seen)

    links, conflicts = [], []
    stats = Counter()
    deltas = Counter()
    for p, awards in zip(persons, person_award_keys):
        sk_key = lk(p.get("surname"))
        full_key = lk((p.get("given_names") or "") + (p.get("surname") or ""))
        for h in p.get("honours") or []:
            ak = award_key(h.get("award"))
            if ak not in GRADES:
                continue
            stats["bio_indian_honours"] += 1
            if h.get("year"):
                stats["bio_dated"] += 1
            else:
                stats["bio_undated"] += 1
            # tiered match: full-name key first, then surname key
            hit, tier = None, None
            if full_key and (ak, full_key) in groups:
                hit, tier = groups[(ak, full_key)], "fullname"
            elif sk_key and (ak, sk_key) in groups:
                hit, tier = groups[(ak, sk_key)], "surname"
            if hit is None:
                stats["no_roll_match"] += 1
                continue
            ry, rm, rd, n_dated, years = group_date(hit)
            if ry is None:
                stats["roll_group_multi_year" if years else
                      "roll_group_undated"] += 1
                continue
            sample = max(hit, key=lambda e: len(e["toks"]))
            compat = given_compat(sample["toks"], p.get("given_names")) \
                if tier == "surname" else "fullname"
            n_claim = claimants[(ak, full_key if tier == "fullname"
                                 else sk_key)]
            row = {"person_id": p["person_id"],
                   "surname": p.get("surname"),
                   "given_names": p.get("given_names"),
                   "birth_year": p.get("birth_year"),
                   "award": h.get("award"), "grade": ak,
                   "bio_year": h.get("year"),
                   "roll_year": ry, "roll_month": rm, "roll_day": rd,
                   "roll_name": sample["name"],
                   "roll_dated_entries": n_dated,
                   "match_tier": tier, "given_compat": compat,
                   "n_bio_claimants": n_claim}
            # a surname-tier hit whose given names contradict the roll's
            # is a namesake, not a link — record it, apply nothing
            namesake = compat == "mismatch"
            if not h.get("year"):
                row["status"] = "fill_namesake" if namesake else "date_fill"
                stats[row["status"]] += 1
                if not namesake:
                    stats["date_fill_unique_claimant"] += (n_claim == 1)
            elif h["year"] == ry:
                row["status"] = "agree_namesake" if namesake else "agree"
                stats[row["status"]] += 1
            else:
                row["delta"] = h["year"] - ry
                row["status"] = "conflict_namesake" if namesake \
                    else "conflict"
                stats[row["status"]] += 1
                if not namesake:
                    deltas[h["year"] - ry] += 1
                    conflicts.append(row)
            links.append(row)

    with open(OUT / "roll_links.jsonl", "w", encoding="utf-8") as fh:
        for r in links:
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")
    with open(OUT / "roll_conflicts.jsonl", "w", encoding="utf-8") as fh:
        for r in conflicts:
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")

    dated_pct = stats["agree"] / max(stats["agree"] + stats["conflict"], 1)
    lines = [
        "# Honours-roll links (grade rolls -> person-table honours)",
        "",
        f"{n_entries:,} roll entries in scope -> {len(groups):,} "
        f"(grade,key) groups; {stats['bio_indian_honours']:,} bio "
        f"Indian-order honours ({stats['bio_dated']:,} dated / "
        f"{stats['bio_undated']:,} undated).",
        "",
        f"- **date_fill**: {stats['date_fill']:,} undated bio honours get "
        f"a unique roll date ({stats['date_fill_unique_claimant']:,} with "
        "a single claimant person — the safe overlay set)",
        f"- **agree**: {stats['agree']:,} dated mentions match the roll "
        f"({dated_pct:.0%} of matched dated mentions)",
        f"- **conflict**: {stats['conflict']:,} dated mentions disagree "
        "-> `roll_conflicts.jsonl` adjudication pool",
        f"- namesakes excluded by given-name contradiction: "
        f"{stats['fill_namesake']:,} fills, {stats['conflict_namesake']:,} "
        f"conflicts, {stats['agree_namesake']:,} agrees",
        f"- no roll match: {stats['no_roll_match']:,}; group undated: "
        f"{stats['roll_group_undated']:,}; group multi-year: "
        f"{stats['roll_group_multi_year']:,}",
        "",
        "## Conflict year deltas (bio - roll)",
        "",
        "| delta | n |", "|---|---|",
    ]
    for d in sorted(deltas, key=lambda x: (abs(x), x)):
        lines.append(f"| {d:+d} | {deltas[d]} |")
    lines += [
        "",
        "Roll dates are printed appointment dates (day-level from 1889);",
        "bio years are LLM-parsed prose. |delta|=1 rows may be gazette-vs-",
        "investiture drift; larger deltas are garbled years or namesakes —",
        "the adjudication prompt shows both records.",
    ]
    (OUT / "ROLL_LINKS.md").write_text("\n".join(lines) + "\n",
                                       encoding="utf-8")
    print("\n".join(lines))
    print("\nstats:", dict(stats))


if __name__ == "__main__":
    main()
