#!/usr/bin/env python3
"""How does the SAME person's services-section entry evolve across editions?

Three hypotheses to discriminate (Jim, 2026-06-19):
  (1) cumulative/append-only -> just take the last (longest) version;
  (2) early-career detail is dropped as decades pass -> must merge editions;
  (3) the whole section condenses later -> some decade is the detail "sweet spot".

Parse-independent richness proxy = count of year tokens (1[789]\\d\\d) in the
entry text, plus raw length. Same-person key = surname_key + first given-name
initial + birth year (birth year is printed from ~1913 on, so cross-edition
tracking is reliable for the mid/late eras; early eras lack it).
"""

from __future__ import annotations

import re
import statistics
import sys
from collections import defaultdict

from col_match.config import Config
from col_match.volume import bios as bios_mod
from col_match.volume import reader

_YEAR = re.compile(r"\b1[789]\d\d\b")
_BIRTH = re.compile(r"\bb(?:orn)?\.?,?\s*(1[789]\d\d)\b", re.I)
_SURKEY = re.compile(r"[^A-Z]")

YEARS = [int(y) for y in sys.argv[1:]] or [1888, 1900, 1912, 1921, 1930, 1939, 1950, 1960]


def _surkey(text: str) -> str:
    return _SURKEY.sub("", text.split(",", 1)[0].upper())


def _person_key(b: dict) -> tuple | None:
    m = _BIRTH.search(b["raw_text"])
    if not m:
        return None
    g = (b.get("given_names") or "").strip()
    init = g[0].upper() if g[:1].isalpha() else "?"
    return (_surkey(b["raw_text"]), init, int(m.group(1)))


def main() -> None:
    cfg = Config.from_env()
    per_edition: dict[int, list[dict]] = {}
    section_stats = []
    for y in YEARS:
        blocks = reader.load_volume(y)
        bios, st = bios_mod.extract_bios(blocks, cfg.data_dir)
        rows = [b.to_json() for b in bios]
        per_edition[y] = rows
        yrs = [len(_YEAR.findall(b["raw_text"])) for b in rows]
        lens = [len(b["raw_text"]) for b in rows]
        section_stats.append((y, len(rows), st["rules_ok"] / max(1, len(rows)),
                              statistics.mean(yrs) if yrs else 0,
                              statistics.median(lens) if lens else 0))

    print("=== SECTION-LEVEL (condensation check) ===")
    print(f"{'year':6}{'bios':>7}{'rules%':>8}{'yr-tok/bio':>12}{'med.len':>9}")
    for y, n, ok, ytok, mlen in section_stats:
        print(f"{y:<6}{n:>7}{ok*100:>7.0f}%{ytok:>12.1f}{mlen:>9.0f}")

    # cross-edition person tracking
    index: dict[tuple, dict[int, dict]] = defaultdict(dict)
    for y, rows in per_edition.items():
        for b in rows:
            k = _person_key(b)
            if k:
                # keep the longest entry if a key repeats within an edition
                if y not in index[k] or len(b["raw_text"]) > len(index[k][y]["raw_text"]):
                    index[k][y] = b
    multi = {k: v for k, v in index.items() if len(v) >= 3}
    print(f"\n=== PERSON-LEVEL: {len(multi)} people tracked across >=3 editions ===")

    # mean year-tokens by edition, restricted to people present in >=3 editions
    by_year_rich = defaultdict(list)
    rising_minyear = falling = rising = flat = 0
    for k, ed in multi.items():
        ys = sorted(ed)
        for y in ys:
            by_year_rich[y].append(len(_YEAR.findall(ed[y]["raw_text"])))
        first, last = ed[ys[0]], ed[ys[-1]]
        ytok_first = len(_YEAR.findall(first["raw_text"]))
        ytok_last = len(_YEAR.findall(last["raw_text"]))
        if ytok_last > ytok_first + 1:
            rising += 1
        elif ytok_last < ytok_first - 1:
            falling += 1
        else:
            flat += 1
        # earliest career year mentioned — does it rise (early detail dropped)?
        ey_first = min((int(x) for x in _YEAR.findall(first["raw_text"])), default=0)
        ey_last = min((int(x) for x in _YEAR.findall(last["raw_text"])), default=0)
        if ey_last > ey_first + 2:
            rising_minyear += 1

    print(f"{'year':6}{'tracked':>9}{'mean yr-tok':>13}")
    for y in sorted(by_year_rich):
        v = by_year_rich[y]
        print(f"{y:<6}{len(v):>9}{statistics.mean(v):>13.1f}")
    print(f"\nfirst->last entry richness:  rising {rising}  flat {flat}  falling {falling}")
    print(f"earliest-career-year rose (early detail dropped): {rising_minyear}/{len(multi)} "
          f"({rising_minyear/len(multi)*100:.0f}%)")

    # one worked example: a person present in the most editions
    star = max(multi.items(), key=lambda kv: len(kv[1]))
    print(f"\n=== EXAMPLE: {star[0]} across {len(star[1])} editions ===")
    for y in sorted(star[1]):
        t = star[1][y]["raw_text"]
        print(f"  {y}: {len(_YEAR.findall(t))} yr-tok, {len(t)} chars | {t[:90]}")


if __name__ == "__main__":
    main()
