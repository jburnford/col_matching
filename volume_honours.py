#!/usr/bin/env python3
"""Extract the honours rolls (order membership lists) from the back matter.

Cumulative lists of every living member of the CO-relevant orders, printed
each edition: "Latham, K.C., Lieutenant-Commander John Greig, 1920." —
surname first, interleaved honours/rank, FULL given names, award year.
Award = order (back-matter zone header) x grade (section title):

  St Michael & St George: Grand Cross->G.C.M.G., Commanders->K.C.M.G.,
                          Companions->C.M.G.
  British Empire:         ->G.B.E./K.B.E./C.B.E./O.B.E./M.B.E. (+Dames)
  Imperial Service Order: I.S.O.        Knights Bachelors: Kt.

Value for the KG: award year + full given names for tens of thousands of
officials — a strong person-matching key against bios and roster careers.
Cross-edition merge on (award, surname, year).

Outputs data/volume/context/{honours_roll.jsonl, HONOURS.md}.
"""

from __future__ import annotations

import json
import re
from collections import Counter, defaultdict
from pathlib import Path

from rapidfuzz import distance

from col_match.services import rules_parse
from col_match.volume import reader

ROOT = Path("data/volume")
OUT = ROOT / "context"

_ORDER = [
    ("SMG", re.compile(r"ST\.? MICH", re.I)),
    ("BE", re.compile(r"BRITISH EMPIRE", re.I)),
    ("ISO", re.compile(r"IMPERIAL SERVICE ORDER", re.I)),
    ("KT", re.compile(r"KNIGHTS BACHELOR", re.I)),
]
_GRADE = [
    ("GC", re.compile(r"grand cross", re.I)),
    ("K", re.compile(r"knights? commander|dames? commander", re.I)),
    ("C", re.compile(r"companion|commanders?\b", re.I)),
    ("O", re.compile(r"officer", re.I)),
    ("M", re.compile(r"member", re.I)),
]
_AWARD = {
    ("SMG", "GC"): "G.C.M.G.", ("SMG", "K"): "K.C.M.G.", ("SMG", "C"): "C.M.G.",
    ("BE", "GC"): "G.B.E.", ("BE", "K"): "K.B.E.", ("BE", "C"): "C.B.E.",
    ("BE", "O"): "O.B.E.", ("BE", "M"): "M.B.E.",
}
_ENTRY_END = re.compile(r",\s*(1[89]\d\d)\s*[.;]")
_RANK_WORD = re.compile(
    r"^(?:The\s+)?(?:Right\s+)?(?:Hon(?:ourable)?\.?|Rev(?:erend)?\.?|Sir|Dame|"
    r"Lieut(?:enant)?[.\- ]*(?:Colonel|Commander|General)?\.?|Lt\.?[-\s]?\w*\.?|"
    r"Major[.\- ]*(?:General)?|Maj\.?[-\s]?Gen\.?|Captain|Capt\.?|Colonel|Col\.?|"
    r"General|Gen\.?|Admiral|Vice[- ]Admiral|Rear[- ]Admiral|Commander|Cdr\.?|"
    r"Commodore|Brigadier|Brig\.?|Wing[- ]Commander|Group[- ]Captain|"
    r"Air\s+\w+|Field[- ]Marshal|Surgeon\w*|Paymaster\w*|Dr\.?|Mr\.?|Professor|"
    r"Bt\.?|His\s+Highness.*|Count|Baron|Lord)$", re.I)


def parse_roll_block(text: str, award: str) -> list[dict]:
    out = []
    pos = 0
    for m in _ENTRY_END.finditer(text):
        seg = text[pos:m.start()].strip(" •*†‡.;,")
        pos = m.end()
        parts = [p.strip() for p in seg.split(",") if p.strip()]
        if not parts:
            continue
        surname = parts[0].strip(" .")
        if not re.match(r"^[A-Z][A-Za-z'’\- ]{1,35}$", surname):
            continue
        honours, given = [], None
        for p in parts[1:]:
            p2 = p.rstrip(".")
            if rules_parse._DOTTED_CAPS.match(p2) or rules_parse._known_honour(p2):
                honours.append(p2)
                continue
            toks = p.split()
            while toks and _RANK_WORD.match(toks[0].rstrip(",.")):
                toks = toks[1:]
            cand = " ".join(toks).strip(" .")
            if cand and re.match(r"^[A-Z]", cand) and given is None:
                given = cand
        out.append({"surname": surname, "given_names": given,
                    "other_honours": honours, "award": award,
                    "year": int(m.group(1))})
    return out


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    locs = defaultdict(list)
    for line in open(ROOT / "block_index.jsonl", encoding="utf-8"):
        r = json.loads(line)
        if r["section"] == "honours_roll" and r["category"] == "text" \
                and r["chars"] > 80:
            locs[r["year"]].append(r)

    raw = []
    for year in sorted(locs):
        bmap = {(b.page, b.index): b for b in reader.load_volume(year, "col")}
        for r in locs[year]:
            order = next((o for o, rx in _ORDER if rx.search(r["zone"] or "")), None)
            if order is None:
                continue
            if order == "ISO":
                award = "I.S.O."
            elif order == "KT":
                award = "Kt."
            else:
                grade = next((g for g, rx in _GRADE if rx.search(r["title"])), None)
                award = _AWARD.get((order, grade))
                if award is None:
                    continue
            b = bmap.get((r["page"], r["block"]))
            if b is None:
                continue
            for rec in parse_roll_block(b.text, award):
                if rec["year"] > year:      # award can't postdate the edition
                    continue
                rec["edition"] = year
                raw.append(rec)

    # cross-edition merge on (award, surname-fuzzy, year)
    merged: dict[tuple, dict] = {}
    for rec in sorted(raw, key=lambda r: r["edition"]):
        sur = rec["surname"].lower()
        key = (rec["award"], rec["year"], sur)
        if key not in merged:
            hit = None
            for (a, y, s), v in merged.items():
                if a == rec["award"] and y == rec["year"] \
                        and abs(len(s) - len(sur)) <= 2 \
                        and distance.Levenshtein.distance(s, sur, score_cutoff=2) <= 2:
                    hit = (a, y, s)
                    break
            key = hit or key
        if key in merged:
            v = merged[key]
            v["n_editions"] += 1
            if rec["given_names"] and (not v["given_names"] or
                                       len(rec["given_names"]) > len(v["given_names"])):
                v["given_names"] = rec["given_names"]
            v["other_honours"] = sorted(set(v["other_honours"]) |
                                        set(rec["other_honours"]))
        else:
            merged[key] = {**rec, "n_editions": 1}

    rolls = sorted(merged.values(), key=lambda r: (r["award"], r["year"], r["surname"]))
    with (OUT / "honours_roll.jsonl").open("w", encoding="utf-8") as fh:
        for r in rolls:
            r.pop("edition", None)
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")

    by_award = Counter(r["award"] for r in rolls)
    with_given = sum(1 for r in rolls if r["given_names"])
    lines = ["# Honours rolls extracted", "",
             f"- raw entries: {len(raw):,} -> {len(rolls):,} distinct awards "
             f"after cross-edition merge; {with_given:,} with full given names "
             f"({100*with_given/max(len(rolls),1):.0f}%)",
             f"- year span {min(r['year'] for r in rolls)}–"
             f"{max(r['year'] for r in rolls)}",
             "", "## By award", ""]
    lines += [f"- {a}: {n:,}" for a, n in by_award.most_common()]
    lines += ["", "## Sample (C.M.G. 1920)", ""]
    for r in [r for r in rolls if r["award"] == "C.M.G." and r["year"] == 1920][:8]:
        lines.append(f"- {r['surname']}, {r['given_names'] or '?'} "
                     f"[{', '.join(r['other_honours'][:3])}] ({r['n_editions']} eds)")
    (OUT / "HONOURS.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines[:16]))
    print(f"\nwrote {OUT}/honours_roll.jsonl, HONOURS.md")


if __name__ == "__main__":
    main()
