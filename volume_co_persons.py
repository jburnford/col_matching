#!/usr/bin/env python3
"""Cross-edition dedup of Colonial Office establishment staff.

The CO promotion matrices reprint every clerk's full ladder each edition
(19.5k records ~ a few hundred people), so identity is the same problem the
governor lists posed: string per-edition rows into persons on
(surname, given-compat) + shared promotion evidence, then majority-vote each
promotion date across attestations (OCR garble is outvoted).

Merge rule (union-find within a surname block): two records merge when the
given names are initials-compatible AND they share >=1 exact
(grade-stem, year) promotion — a reprinted ladder guarantees overlap for a
real person; namesakes with disjoint ladders stay apart. Records with no
promotion overlap merge only on exact given-name equality + overlapping
edition era (<=15yr gap).

Also links each CO person to the unified bio-person layer (strict name gate:
exact initials or shared spelled forename + order-compatible; unique hit).

Outputs (data/volume/context/):
  co_persons.jsonl   one row per CO official: voted ladder, editions, links
  CO_PERSONS.md      report

Usage: python3 volume_co_persons.py
"""

from __future__ import annotations

import json
import re
from collections import Counter, defaultdict
from pathlib import Path

from col_match.services.match import _initials, _names_compatible

CTX = Path("data/volume/context")
PERSONS = Path("data/volume/bio_persons/bio_persons.jsonl")

_TITLE_TOKS = {"the", "hon", "sir", "dame", "mrs", "miss", "lady", "rev",
               "dr", "col", "capt", "captain", "lieut", "major", "gen",
               "prof", "ven", "mr"}


def _detitle(g: str | None) -> str:
    return " ".join(t for t in (g or "").split()
                    if t.lower().strip(".,") not in _TITLE_TOKS)


def strict_name(g: str | None, pg: str | None) -> bool:
    g, pg = _detitle(g), _detitle(pg)
    ti, pi = _initials(g), _initials(pg)
    if ti and pi and ti == pi:
        return True
    gt = {t.lower().strip(".,") for t in g.split() if len(t) > 2}
    pt = {t.lower().strip(".,") for t in pg.split() if len(t) > 2}
    return bool(gt & pt) and _names_compatible(g, pg)


def surname_norm(s: str | None) -> str:
    return re.sub(r"[^a-z]", "", (s or "").lower())


def gradestem(g: str | None) -> str:
    return re.sub(r"[^a-z]", "", (g or "").lower())[:14]


def promo_keys(r: dict) -> set[tuple[str, int]]:
    return {(gradestem(p["grade"]), p["year"]) for p in r.get("promotions", ())
            if p.get("year")}


def main() -> None:
    recs = [json.loads(l) for l in (CTX / "co_staff.jsonl").open(encoding="utf-8")]

    # ---- union-find within surname blocks
    parent = list(range(len(recs)))

    def find(x: int) -> int:
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a: int, b: int) -> None:
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[max(ra, rb)] = min(ra, rb)

    blocks: dict[str, list[int]] = defaultdict(list)
    for i, r in enumerate(recs):
        blocks[surname_norm(r["surname"])].append(i)
    for _, idxs in blocks.items():
        keyed = [(i, promo_keys(recs[i])) for i in idxs]
        for a in range(len(keyed)):
            ia, ka = keyed[a]
            for b in range(a + 1, len(keyed)):
                ib, kb = keyed[b]
                if find(ia) == find(ib):
                    continue
                ga, gb = recs[ia].get("given_names"), recs[ib].get("given_names")
                if not _names_compatible(ga, gb):
                    continue
                if ka & kb:
                    union(ia, ib)
                elif (ga and gb and _detitle(ga).lower() == _detitle(gb).lower()
                      and abs(recs[ia]["edition"] - recs[ib]["edition"]) <= 15):
                    union(ia, ib)

    groups: dict[int, list[dict]] = defaultdict(list)
    for i, r in enumerate(recs):
        groups[find(i)].append(r)

    # ---- unified bio-persons for linking
    bio_by_sur: dict[str, list[dict]] = defaultdict(list)
    for l in PERSONS.open(encoding="utf-8"):
        p = json.loads(l)
        if "not_a_person" not in p["flags"]:
            bio_by_sur[surname_norm(p.get("surname"))].append(p)

    persons = []
    linked = 0
    for members in groups.values():
        members.sort(key=lambda r: r["edition"])
        given = max((r.get("given_names") or "" for r in members),
                    key=lambda g: (sum(1 for t in g.split() if len(t) > 2), len(g)))
        # majority-vote each grade's year across attestations
        votes: dict[str, Counter] = defaultdict(Counter)
        grade_raw: dict[str, str] = {}
        for r in members:
            for p in r.get("promotions", ()):
                if p.get("year"):
                    votes[gradestem(p["grade"])][p["year"]] += 1
                    grade_raw.setdefault(gradestem(p["grade"]), p["grade"])
        ladder = sorted(
            ({"grade": grade_raw[g], "year": c.most_common(1)[0][0],
              "n_attest": sum(c.values()),
              **({"year_minority": True} if len(c) > 1 else {})}
             for g, c in votes.items()),
            key=lambda x: x["year"])
        honours = sorted({h for r in members for h in r.get("honours", ())})
        # strict unique link to the bio-person layer
        cands = [p for p in bio_by_sur.get(surname_norm(members[0]["surname"]), ())
                 if strict_name(given, p.get("given_names"))]
        link = cands[0]["person_id"] if len({p["person_id"] for p in cands}) == 1 else None
        if link:
            linked += 1
        persons.append({
            "surname": members[0]["surname"], "given_names": given or None,
            "honours": honours, "promotions": ladder,
            "first_edition": members[0]["edition"],
            "last_edition": members[-1]["edition"],
            "n_records": len(members),
            "bio_person_id": link,
        })

    persons.sort(key=lambda p: (surname_norm(p["surname"]), p["first_edition"]))
    with (CTX / "co_persons.jsonl").open("w", encoding="utf-8") as fh:
        for p in persons:
            fh.write(json.dumps(p, ensure_ascii=False) + "\n")

    multi = sum(1 for p in persons if p["n_records"] > 1)
    minority = sum(1 for p in persons
                   for x in p["promotions"] if x.get("year_minority"))
    lines = [
        "# Colonial Office staff — cross-edition persons",
        "",
        f"- {len(recs):,} per-edition matrix rows -> {len(persons):,} persons "
        f"({multi:,} attested in >1 edition; mean "
        f"{len(recs)/max(len(persons),1):.1f} attestations)",
        f"- promotion dates majority-voted; {minority:,} grade-dates had a "
        f"dissenting OCR reading (outvoted, flagged year_minority)",
        f"- linked to a unified bio-person: {linked:,} "
        f"({100*linked/max(len(persons),1):.0f}%)",
        "",
        "## Longest ladders (sanity sample)",
        "",
    ]
    for p in sorted(persons, key=lambda p: -len(p["promotions"]))[:8]:
        steps = " -> ".join(f"{x['grade'][:28]} {x['year']}"
                            for x in p["promotions"][:6])
        lines.append(f"- **{p['surname']}, {p['given_names']}** "
                     f"({p['first_edition']}–{p['last_edition']}, "
                     f"{p['n_records']} eds): {steps}")
    (CTX / "CO_PERSONS.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines[:8]))
    print(f"-> {CTX}/co_persons.jsonl")


if __name__ == "__main__":
    main()
