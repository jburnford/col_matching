#!/usr/bin/env python3
"""Class the unlinked roster careers (never-bio'd protocol) and emit the
class-C pairwise adjudication worklist for the Qwen tier on Nibi.

Protocol (methods decision, July 2026): an unlinked career (no within-volume
bio link anywhere along it) is
  A  no name-compatible bio person exists anywhere in the corpus — safely
     never-bio'd;
  B  namesake persons exist but every one is colony- AND/OR time-incompatible
     — safely never-bio'd;
  C  at least one compatible namesake — ambiguity UPPER bound. This script
     emits (career, candidate person) pairs so the LLM tier can turn the
     upper bound into a measured rate (judging timing/rank/place fit);
  U  career has no given names at all — too weak to key, reported separately.

Candidates are the UNIFIED bio persons (data/volume/bio_persons/), not
per-edition bios — one pair judges a career against a person's whole merged
record. Colony gating reuses the volume linker's gazetteer + city→colony
aliases; unresolvable-place persons stay compatible (they cannot be ruled
out, and the bound must stay an upper bound).

Outputs (data/volume/classc/):
  career_classes.jsonl   one line per unlinked career: class + evidence counts
  classc_worklist.jsonl  (career × candidate person) pairs for the GPU worker
  CLASSC.md              per-colony / per-salary-rank A/B/C/U table

Usage: python3 volume_classc_worklist.py
"""

from __future__ import annotations

import json
import re
from collections import Counter, defaultdict
from pathlib import Path

from col_match.config import Config
from col_match.services.match import _names_compatible
from col_match.volume.match import _colony_target_set

VOLROOT = Path("data/volume")
OUTDIR = VOLROOT / "classc"
MAX_CANDIDATES = 4
MAX_PERSON_EVENTS = 30

# salary parsing + rank thresholds as in the GC/Kenya v2 analysis
# (african-colonial-mobility/list_vs_bio_v2.py) so rates line up
_AMT = re.compile(r"([\d,]+)\s*(?:l\.|£|/)")


def salary_peak(s: str | None) -> int | None:
    if not s:
        return None
    amts = [int(d) for a in _AMT.findall(s) if (d := a.replace(",", ""))]
    amts = [a for a in amts if a >= 20]
    return max(amts) if amts else None


def rank_class(peak: int | None) -> str:
    if peak is None:
        return "unsalaried"
    if peak < 100:
        return "subordinate"
    if peak < 400:
        return "clerical"
    if peak < 1000:
        return "officer"
    return "senior"


def surname_norm(s: str | None) -> str:
    return re.sub(r"[^a-z]", "", (s or "").lower())


def main() -> None:
    OUTDIR.mkdir(parents=True, exist_ok=True)
    data_dir = Config.from_env().data_dir

    _tcache: dict[str, frozenset[str]] = {}

    def targets(raw: str | None) -> frozenset[str]:
        key = (raw or "").strip()
        if key not in _tcache:
            _tcache[key] = frozenset(_colony_target_set(key, data_dir))
        return _tcache[key]

    # ---------------- unified bio persons
    by_sur: dict[str, list[dict]] = defaultdict(list)
    n_persons = 0
    for line in (VOLROOT / "bio_persons" / "bio_persons.jsonl").open(encoding="utf-8"):
        p = json.loads(line)
        if "not_a_person" in p["flags"]:
            continue
        k = surname_norm(p.get("surname"))
        if not k:
            continue
        n_persons += 1
        cols: set[str] = set()
        for ev in p["events"]:
            if ev.get("place"):
                cols |= targets(ev["place"])
        eds = p["editions"] or []
        years = [y for y in (p.get("career_start"), p.get("career_end")) if y]
        lo = min(years + eds) if (years or eds) else None
        hi = max(years + eds) if (years or eds) else None
        by_sur[k].append({
            "person_id": p["person_id"],
            "given": p.get("given_names"),
            "birth_year": p.get("birth_year"),
            "colonies": cols,          # empty = unresolvable -> can't rule out
            "lo": lo, "hi": hi,
            "p": p,
        })

    # ---------------- unlinked careers
    classes: list[dict] = []
    pairs: list[dict] = []
    n_linked = 0
    for line in (VOLROOT / "careers" / "careers.jsonl").open(encoding="utf-8"):
        c = json.loads(line)
        if c.get("suspect"):
            continue
        if c.get("bio_ids"):
            n_linked += 1
            continue
        sur = surname_norm(c.get("surname"))
        given = c.get("given_names")
        years = c.get("years") or []
        peak = max((salary_peak(r.get("salary")) or 0 for r in c["records"]),
                   default=0) or None
        rank = rank_class(peak)
        row = {"career_id": c["career_id"], "colony": c["colony"],
               "surname": c.get("surname"), "given_names": given,
               "years": [years[0], years[-1]] if years else None,
               "rank": rank, "peak_salary": peak,
               "weak_key": c.get("weak_key", False)}

        if not given or not sur:
            row.update({"cls": "U", "n_namesakes": None, "n_compatible": None})
            classes.append(row)
            continue

        namesakes = [q for q in by_sur.get(sur, ())
                     if _names_compatible(given, q["given"])]
        if not namesakes:
            row.update({"cls": "A", "n_namesakes": 0, "n_compatible": 0})
            classes.append(row)
            continue

        ctargets = targets(c["colony"])
        cand = []
        for q in namesakes:
            colony_ok = (not q["colonies"]) or bool(q["colonies"] & ctargets)
            colony_known = bool(q["colonies"] & ctargets)
            if not colony_ok:
                continue
            if q["lo"] is not None and years:
                if years[-1] < q["lo"] - 2 or years[0] > q["hi"] + 3:
                    continue
                overlap = (min(years[-1], q["hi"]) - max(years[0], q["lo"]))
            else:
                overlap = 0
            cand.append((2 * colony_known + (overlap >= 0), overlap, q))
        if not cand:
            row.update({"cls": "B", "n_namesakes": len(namesakes),
                        "n_compatible": 0})
            classes.append(row)
            continue

        cand.sort(key=lambda t: (-t[0], -t[1]))
        row.update({"cls": "C", "n_namesakes": len(namesakes),
                    "n_compatible": len(cand)})
        classes.append(row)

        # ------------ worklist pairs: compact printed evidence, no invention
        career_lines = []
        for r in sorted(c["records"], key=lambda r: r["year"]):
            bits = [str(r["year"])]
            if r.get("position"):
                bits.append(r["position"][:90])
            if r.get("department"):
                bits.append(f"dept: {r['department'][:60]}")
            if r.get("salary"):
                bits.append(f"salary: {r['salary'][:40]}")
            career_lines.append("  " + " | ".join(bits))
        for rank_i, (_, _, q) in enumerate(cand[:MAX_CANDIDATES]):
            p = q["p"]
            ev_lines = []
            for ev in p["events"][:MAX_PERSON_EVENTS]:
                yr = ev.get("year_start")
                ev_lines.append(
                    f"  {yr if yr else '????'}: {ev.get('position') or '?'}"
                    + (f" [{ev['place']}]" if ev.get("place") else ""))
            pairs.append({
                "id": f"{c['career_id']}::{p['person_id']}",
                "career_id": c["career_id"],
                "person_id": p["person_id"],
                "cand_rank": rank_i,
                "career": {
                    "colony": c["colony"],
                    "name": f"{c.get('surname')}, {given}",
                    "roster_years": years,
                    "lines": career_lines[:40],
                },
                "person": {
                    "name": f"{p.get('surname')}, {p.get('given_names') or ''}".strip(", "),
                    "birth_year": p.get("birth_year"),
                    "honours": [h.get("award") for h in p.get("honours") or []][:8],
                    "editions": [p["editions"][0], p["editions"][-1]] if p["editions"] else None,
                    "lines": ev_lines,
                },
            })

    # ------------------------------------------------------------- outputs
    with (OUTDIR / "career_classes.jsonl").open("w", encoding="utf-8") as fh:
        for r in classes:
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")
    with (OUTDIR / "classc_worklist.jsonl").open("w", encoding="utf-8") as fh:
        for r in pairs:
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")

    # ------------------------------------------------------------- report
    tot = Counter(r["cls"] for r in classes)
    lines = [
        "# Never-bio'd classing of unlinked roster careers",
        "",
        f"- linked careers (excluded here): {n_linked:,}",
        f"- unlinked careers classed: {len(classes):,} — "
        + ", ".join(f"{k}: {tot[k]:,}" for k in "ABCU"),
        f"- bio persons indexed: {n_persons:,}",
        f"- class-C adjudication pairs (cap {MAX_CANDIDATES}/career): {len(pairs):,}",
        "",
        "Class C is the ambiguity UPPER bound; the Qwen pairwise pass turns it",
        "into a measured rate. Classes A/B are safely never-bio'd.",
        "",
        "## Class shares by salary rank (all colonies)",
        "",
        "| rank | careers | A | B | C | U | C% |",
        "|---|---|---|---|---|---|---|",
    ]
    def _cshare(rows):
        n = len(rows)
        cc = Counter(r["cls"] for r in rows)
        return (f"| {n:,} | {cc['A']:,} | {cc['B']:,} | {cc['C']:,} "
                f"| {cc['U']:,} | {100*cc['C']/max(n,1):.0f}% |")
    for rk in ("subordinate", "clerical", "officer", "senior", "unsalaried"):
        rows = [r for r in classes if r["rank"] == rk]
        lines.append(f"| {rk} " + _cshare(rows))
    lines += ["", "## Gold Coast / Kenya (paper colonies)", "",
              "| colony · rank | careers | A | B | C | U | C% |", "|---|---|---|---|---|---|---|"]
    for col in ("GOLD COAST", "KENYA"):
        for rk in ("subordinate", "clerical", "officer", "senior", "unsalaried"):
            rows = [r for r in classes if r["colony"] == col and r["rank"] == rk]
            if rows:
                lines.append(f"| {col.title()} · {rk} " + _cshare(rows))
    top = Counter(r["colony"] for r in classes if r["cls"] == "C").most_common(15)
    lines += ["", "## Largest class-C colonies", ""]
    for col, n in top:
        lines.append(f"- {col}: {n:,}")
    (OUTDIR / "CLASSC.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"classed {len(classes):,} unlinked careers: "
          + ", ".join(f"{k}={tot[k]:,}" for k in "ABCU"))
    print(f"worklist pairs: {len(pairs):,} -> {OUTDIR}/")


if __name__ == "__main__":
    main()
