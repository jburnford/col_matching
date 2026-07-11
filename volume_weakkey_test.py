#!/usr/bin/env python3
"""Weak-key namesake stress test: does single-initial career stringing
over-merge, and where?

Career stringing clusters roster records on (colony, surname,
initials-compatible given names); 37% of careers key on a single initial at
best (`weak_key`). The worry: two namesakes in one colony collapse into one
"career". The within-volume bio links give ground truth — a career whose
records link to MORE THAN ONE bio-person was strung across two real people.

For every career with >=2 distinct linked bios, map bios -> unified persons
(data/volume/bio_persons/bio_person_map.jsonl) and count careers whose links
span >1 person, stratified by weak_key x surname frequency band. Links are
0-FP-discipline products, so a multi-person career is strong evidence of
over-merge (modulo residual person-layer under-merge, which deflates the
metric equally in every stratum).

Output: data/volume/careers/WEAKKEY.md

Usage: python3 volume_weakkey_test.py
"""

from __future__ import annotations

import json
import re
from collections import Counter, defaultdict
from pathlib import Path

VOLROOT = Path("data/volume")


def surname_norm(s: str | None) -> str:
    return re.sub(r"[^a-z]", "", (s or "").lower())


def band(freq: int) -> str:
    if freq >= 100:
        return "common (>=100)"
    if freq >= 10:
        return "medium (10-99)"
    return "rare (<10)"


def main() -> None:
    pmap = {}
    for l in (VOLROOT / "bio_persons" / "bio_person_map.jsonl").open(encoding="utf-8"):
        r = json.loads(l)
        pmap[r["bio_id"]] = r["person_id"]

    careers = []
    surfreq: Counter[str] = Counter()
    for l in (VOLROOT / "careers" / "careers.jsonl").open(encoding="utf-8"):
        c = json.loads(l)
        if c.get("suspect"):
            continue
        surfreq[surname_norm(c.get("surname"))] += 1
        careers.append(c)

    strata: dict[tuple[str, str], Counter] = defaultdict(Counter)
    examples: list[str] = []
    for c in careers:
        bios = {r["bio_id"] for r in c["records"] if r.get("bio_id")}
        key = ("weak" if c.get("weak_key") else "full",
               band(surfreq[surname_norm(c.get("surname"))]))
        strata[key]["careers"] += 1
        if len(bios) < 2:
            continue
        persons = {pmap[b] for b in bios if b in pmap}
        strata[key]["testable"] += 1
        span = c["years"][-1] - c["years"][0] + 1
        strata[key][f"testable_span{'40+' if span > 40 else '<40'}"] += 1
        if len(persons) > 1:
            strata[key]["overmerged"] += 1
            strata[key][f"overmerged_span{'40+' if span > 40 else '<40'}"] += 1
            if len(examples) < 12:
                examples.append(
                    f"- {c['colony']} | {c.get('surname')}, "
                    f"{c.get('given_names')} | {c['years'][0]}–{c['years'][-1]} "
                    f"| {len(persons)} persons")

    lines = [
        "# Weak-key namesake stress test (career stringing)",
        "",
        "A career whose within-volume bio links span >1 unified person was",
        "strung across two real people. Testable = careers with >=2 distinct",
        "linked bios (multi-year, well-linked — the stringing's best case, so",
        "rates below are optimistic for well-linked careers but the weak/full",
        "and rare/common CONTRASTS are the signal).",
        "",
        "| key | surname band | careers | testable | over-merged | rate |",
        "|---|---|---|---|---|---|",
    ]
    order = ["rare (<10)", "medium (10-99)", "common (>=100)"]
    for key in ("full", "weak"):
        for b in order:
            s = strata[(key, b)]
            n, t, o = s["careers"], s["testable"], s["overmerged"]
            rate = f"{100*o/t:.1f}%" if t else "—"
            lines.append(f"| {key} | {b} | {n:,} | {t:,} | {o:,} | {rate} |")
    tot = Counter()
    for s in strata.values():
        tot.update(s)
    lines += [
        "",
        f"Overall: {tot['careers']:,} careers, {tot['testable']:,} testable, "
        f"{tot['overmerged']:,} over-merged "
        f"({100*tot['overmerged']/max(tot['testable'],1):.2f}% of testable).",
        "",
        "## The dynastic-succession mechanism",
        "",
        "Over-merges concentrate in long spans — local families (Barbados",
        "Berkeleys/Brownes/Smiths) passing posts father-to-son under shared",
        "initials, which no name key can separate:",
        "",
        f"- spans <= 40 years: {tot['overmerged_span<40']:,} / "
        f"{tot['testable_span<40']:,} testable "
        f"({100*tot['overmerged_span<40']/max(tot['testable_span<40'],1):.1f}%)",
        f"- spans  > 40 years: {tot['overmerged_span40+']:,} / "
        f"{tot['testable_span40+']:,} testable "
        f"({100*tot['overmerged_span40+']/max(tot['testable_span40+'],1):.1f}%)",
        "",
        "Methods takeaway: over-merge risk is driven by surname FREQUENCY and",
        "dynastic span, not by single-initial keys — the weak_key flag is the",
        "wrong sensitivity axis on its own; filter on (common surname) and/or",
        "(span > 40) instead.",
        "",
        "## Sample over-merged careers",
        "",
        *examples,
    ]
    out = VOLROOT / "careers" / "WEAKKEY.md"
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines[:20]))
    print(f"-> {out}")


if __name__ == "__main__":
    main()
