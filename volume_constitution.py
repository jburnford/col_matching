#!/usr/bin/env python3
"""Constitutional-change timeline from the per-colony Constitution sections.

The constitution/government prose is boilerplate reprinted every edition
(~40% verbatim carry-over, higher in truth) — so its EDITS are the signal:
an edition where the text changes materially marks a real constitutional
event (new legislative council, elected members introduced, responsible
government, crown-colony reversion...).

Per (colony, edition): concatenate the constitution-section text; chain
consecutive editions with difflib similarity (OCR-noise tolerant); a drop
below the threshold = a revision event. Status descriptors are regexed per
version (crown colony / representative / responsible / protectorate /
mandate / elected members ...) so descriptor transitions are dated even when
wording churn hides in the similarity.

Outputs data/volume/context/{constitution_timeline.jsonl, CONSTITUTION.md}.
"""

from __future__ import annotations

import json
import re
from collections import defaultdict
from pathlib import Path

from col_match.volume import reader
from volume_careers import canon_colony

ROOT = Path("data/volume")
OUT = ROOT / "context"
SIM_REVISION = 0.5           # shingle-Jaccard below this = revision event
_SHINGLE = 8                 # words per shingle


def _shingles(norm_text: str) -> set:
    toks = norm_text.split()
    return {" ".join(toks[i:i + _SHINGLE]) for i in range(0, len(toks) - _SHINGLE)}


def _jaccard(a: set, b: set) -> float:
    if not a and not b:
        return 1.0
    return len(a & b) / max(len(a | b), 1)

_STATUS = [
    ("crown_colony", re.compile(r"crown colony", re.I)),
    ("responsible_government", re.compile(r"responsible government", re.I)),
    ("representative_government", re.compile(r"representative (?:government|institutions)", re.I)),
    ("protectorate", re.compile(r"protectorate", re.I)),
    ("mandate", re.compile(r"mandated territory|mandate of the league", re.I)),
    ("trusteeship", re.compile(r"trust territory|trusteeship", re.I)),
    ("elected_members", re.compile(r"elected (?:unofficial )?members?", re.I)),
    ("universal_suffrage", re.compile(r"universal (?:adult )?suffrage", re.I)),
    ("ministerial_system", re.compile(r"ministerial system|ministers? responsible", re.I)),
    ("internal_self_government", re.compile(r"self-government|self government", re.I)),
]

_norm = lambda t: re.sub(r"\s+", " ", re.sub(r"[^a-z0-9 ]", "", t.lower()))


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    locs = defaultdict(list)
    for line in open(ROOT / "block_index.jsonl", encoding="utf-8"):
        r = json.loads(line)
        if r["section"] == "constitution" and r["category"] == "text" and r["colony"]:
            locs[r["year"]].append(r)

    texts: dict[tuple[str, int], list[str]] = defaultdict(list)
    for year in sorted(locs):
        bmap = {(b.page, b.index): b for b in reader.load_volume(year, "col")}
        for r in sorted(locs[year], key=lambda r: (r["page"], r["block"])):
            b = bmap.get((r["page"], r["block"]))
            colony = canon_colony(r["colony"]) if r["colony"] else None
            if b is None or colony is None or len(b.text) < 60:
                continue
            texts[(colony, year)].append(b.text)

    by_colony: dict[str, list[int]] = defaultdict(list)
    for (colony, year) in texts:
        by_colony[colony].append(year)

    timeline = []
    n_revisions = 0
    for colony, years in sorted(by_colony.items()):
        years.sort()
        # raw status per edition, then SMOOTH single-edition flaps: a
        # descriptor drifting between section classes for one edition is
        # classification noise, not a constitutional reversal
        raw_status = {}
        for y in years:
            full = " ".join(texts[(colony, y)])
            raw_status[y] = {name for name, rx in _STATUS if rx.search(full)}
        smooth = {}
        for i, y in enumerate(years):
            s = set(raw_status[y])
            if 0 < i < len(years) - 1:
                before, after = raw_status[years[i - 1]], raw_status[years[i + 1]]
                s |= (before & after)          # transient loss -> restore
                s -= (s - before - after)      # transient gain -> drop
            smooth[y] = s

        prev = None
        prev_status: set[str] = set()
        for i, y in enumerate(years):
            full = " ".join(texts[(colony, y)])
            sh = _shingles(_norm(full))
            status = smooth[y]
            sim = _jaccard(prev, sh) if prev is not None else None
            revision = sim is not None and sim < SIM_REVISION
            gained = sorted(status - prev_status) if prev is not None else sorted(status)
            lost = sorted(prev_status - status) if prev is not None else []
            if revision:
                n_revisions += 1
            timeline.append({"colony": colony, "edition": y, "chars": len(full),
                             "sim_prev": round(sim, 3) if sim is not None else None,
                             "revision": revision, "status": sorted(status),
                             "gained": gained if prev is not None else [],
                             "lost": lost})
            prev, prev_status = sh, status

    with (OUT / "constitution_timeline.jsonl").open("w", encoding="utf-8") as fh:
        for t in timeline:
            fh.write(json.dumps(t, ensure_ascii=False) + "\n")

    # ------------------------------------------------------------- report
    events = [t for t in timeline if t["gained"] or t["lost"]]
    lines = ["# Constitutional-change timeline", "",
             f"- (colony, edition) constitution snapshots: {len(timeline):,} "
             f"across {len(by_colony)} colonies",
             f"- revision events (text similarity < {SIM_REVISION}): {n_revisions:,}",
             f"- status-descriptor transitions: "
             f"{sum(1 for t in events if t['sim_prev'] is not None):,}",
             "", "## Sample descriptor transitions", ""]
    shown = 0
    for t in timeline:
        if t["sim_prev"] is None or not (t["gained"] or t["lost"]) or shown >= 25:
            continue
        if t["colony"] in ("JAMAICA", "GOLD COAST", "MALTA", "CEYLON", "KENYA",
                           "NIGERIA", "BARBADOS", "CYPRUS"):
            g = "+" + ",".join(t["gained"]) if t["gained"] else ""
            l = "-" + ",".join(t["lost"]) if t["lost"] else ""
            lines.append(f"- {t['colony']} ed.{t['edition']}: {g} {l} "
                         f"(sim {t['sim_prev']})")
            shown += 1
    (OUT / "CONSTITUTION.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines[:10]))
    print(f"\nwrote {OUT}/constitution_timeline.jsonl, CONSTITUTION.md")


if __name__ == "__main__":
    main()
