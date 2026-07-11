#!/usr/bin/env python3
"""B1: audit the within-volume bio<->roster links (IDENTITY_QA_ROADMAP).

Everything person-level rests on the ~79k within-volume links, and unlike
the class-C overlay they were never adversarially audited — the 0-FP
discipline is a design claim, not a measured rate. This scores every link
deterministically on signals BEYOND the linker's gates, then draws a
stratified sample for Nibi adjudication so the score distribution converts
into a measured precision per stratum.

Per-link features (the linker already gated surname, name compatibility and
colony agreement, so those hold by construction — except colony for some
'unique' links with unplaced bios):

  name_class    full_forename > multi_initials > partial > thin
  position_sim  at the linked bio event (linker field)
  shared_honours (linker field)
  rivals_colony  other same-surname, name-compatible records in the SAME
                 colony that edition — the link won a contest
  rivals_edition same but edition-wide (cross-colony namesake pressure)
  surname_freq   corpus-wide roster frequency (the dominant risk axis)
  bio_anchor     bio has birth year / honours / >=3 dated events

Score = transparent points; strata = strength x score tercile. Sample ~45
per stratum -> b1_audit_worklist.jsonl in the classc pair format, runnable
by nibi/qwen_classc_worker.py unchanged (career = the one-year roster
record; person = the bio).

Outputs data/volume/identity/{b1_link_scores.jsonl, b1_audit_worklist.jsonl,
B1_AUDIT.md}. Read-only over the edition dirs; applies nothing.
"""

from __future__ import annotations

import json
import random
import re
from collections import Counter, defaultdict
from pathlib import Path

from col_match.services.match import _initials, _names_compatible, _norm

ROOT = Path("data/volume")
OUT = ROOT / "identity"
SAMPLE_PER_STRATUM = 45
SEED = 20260711


def surname_key(s: str | None) -> str:
    return _norm(s.split()[-1]) if s else ""


def name_class(bio_given: str | None, rec_given: str | None) -> str:
    bt = [t for t in re.split(r"[ .]+", bio_given or "") if t]
    rt = [t for t in re.split(r"[ .]+", rec_given or "") if t]
    if bt and rt and len(bt[0]) > 1 and len(rt[0]) > 1 \
            and _norm(bt[0]) == _norm(rt[0]):
        return "full_forename"
    bi, ri = _initials(bio_given), _initials(rec_given)
    if len(bi) >= 2 and len(ri) >= 2:
        return "multi_initials"
    if len(bi) >= 2 or len(ri) >= 2:
        return "partial"
    return "thin"


_NAME_CLASS_PTS = {"full_forename": 2, "multi_initials": 1, "partial": 0,
                   "thin": -1}


def score_link(feat: dict) -> int:
    pts = 0
    sim = feat["position_sim"]
    pts += 3 if sim >= 60 else (1 if sim >= 40 else 0)
    if feat["shared_honours"]:
        pts += 3
    pts += _NAME_CLASS_PTS[feat["name_class"]]
    pts += 2 if feat["rivals_colony"] == 0 else -2 * min(feat["rivals_colony"], 2)
    if feat["rivals_edition"] == 0:
        pts += 1
    if feat["surname_freq"] <= 20:
        pts += 1
    elif feat["surname_freq"] >= 500:
        pts -= 1
    if feat["bio_anchor"]:
        pts += 1
    return pts


def bio_lines(bio: dict) -> list[str]:
    out = []
    for ev in bio["events"]:
        span = ev.get("text_span") or (
            (ev.get("position") or "?")
            + (f" [{ev['place']}]" if ev.get("place") else ""))
        y = ev.get("year_start") or "?"
        out.append(f"  {y}: {span}")
    return out[:40]


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    editions = sorted(
        int(p.name[3:]) for p in ROOT.glob("col*") if p.is_dir()
        and (p / "links.jsonl").exists())

    # pass 1: corpus-wide surname frequency over roster records
    sfreq: Counter = Counter()
    for year in editions:
        for line in open(ROOT / f"col{year}" / "records.jsonl",
                         encoding="utf-8"):
            sfreq[surname_key(json.loads(line).get("surname"))] += 1

    scores, by_stratum_pool = [], defaultdict(list)
    for year in editions:
        ed = ROOT / f"col{year}"
        bios = {b["bio_id"]: b for b in map(
            json.loads, open(ed / "bios.jsonl", encoding="utf-8"))}
        records, rec_by_key = {}, defaultdict(list)
        for line in open(ed / "records.jsonl", encoding="utf-8"):
            r = json.loads(line)
            records[r["record_id"]] = r
            rec_by_key[surname_key(r.get("surname"))].append(r)
        for line in open(ed / "links.jsonl", encoding="utf-8"):
            ln = json.loads(line)
            bio = bios.get(ln["bio_id"])
            rec = records.get(ln["record_id"])
            if bio is None or rec is None:
                continue
            key = surname_key(ln["rec_surname"])
            compat = [r for r in rec_by_key[key]
                      if r["record_id"] != ln["record_id"]
                      and _names_compatible(ln["bio_given"],
                                            r.get("given_names"))]
            feat = {
                "link_id": f"{ln['record_id']}::{ln['bio_id']}",
                "bio_id": ln["bio_id"], "record_id": ln["record_id"],
                "edition_year": ln["edition_year"],
                "strength": ln["strength"],
                "surname_match": ln["surname_match"],
                "colony": ln["colony"],
                "position_sim": ln["position_sim"],
                "shared_honours": ln["shared_honours"],
                "name_class": name_class(ln["bio_given"], ln["rec_given"]),
                "rivals_colony": sum(
                    1 for r in compat if r.get("colony") == ln["colony"]),
                "rivals_edition": len(compat),
                "surname_freq": sfreq[key],
                "bio_anchor": bool(bio.get("birth_year") or bio.get("honours")
                                   or sum(1 for e in bio["events"]
                                          if e.get("year_start")) >= 3),
            }
            feat["score"] = score_link(feat)
            scores.append(feat)

    # terciles within strength -> strata
    by_strength = defaultdict(list)
    for f in scores:
        by_strength[f["strength"]].append(f["score"])
    cuts = {}
    for st, vals in by_strength.items():
        vals = sorted(vals)
        cuts[st] = (vals[len(vals) // 3], vals[2 * len(vals) // 3])
    for f in scores:
        lo, hi = cuts[f["strength"]]
        f["risk_tier"] = ("high" if f["score"] < lo
                          else "low" if f["score"] >= hi else "mid")
        f["stratum"] = f"{f['strength']}:{f['risk_tier']}"
        by_stratum_pool[f["stratum"]].append(f)

    with open(OUT / "b1_link_scores.jsonl", "w", encoding="utf-8") as fh:
        for f in scores:
            fh.write(json.dumps(f, ensure_ascii=False) + "\n")

    # stratified sample -> classc-format pair worklist
    rng = random.Random(SEED)
    sample = []
    for st in sorted(by_stratum_pool):
        pool = by_stratum_pool[st]
        sample += rng.sample(pool, min(len(pool), SAMPLE_PER_STRATUM))
    need = {(f["edition_year"], f["bio_id"], f["record_id"], f["stratum"],
             f["link_id"]) for f in sample}
    by_year = defaultdict(list)
    for t in need:
        by_year[t[0]].append(t)
    rows = []
    for year, items in sorted(by_year.items()):
        ed = ROOT / f"col{year}"
        bios = {b["bio_id"]: b for b in map(
            json.loads, open(ed / "bios.jsonl", encoding="utf-8"))}
        records = {r["record_id"]: r for r in map(
            json.loads, open(ed / "records.jsonl", encoding="utf-8"))}
        for _, bio_id, record_id, stratum, link_id in items:
            bio, rec = bios[bio_id], records[record_id]
            line = f"  {year} | {rec.get('position') or '?'}"
            if rec.get("department"):
                line += f" | dept: {rec['department']}"
            if rec.get("salary"):
                line += f" | salary: {rec['salary']}"
            rows.append({
                "id": f"b1::{link_id}", "stratum": stratum,
                "career_id": record_id, "person_id": bio_id,
                "cand_rank": 0,
                "career": {
                    "colony": rec.get("colony"),
                    "name": f"{rec.get('surname')}, {rec.get('given_names')}",
                    "roster_years": [year],
                    "lines": [line],
                },
                "person": {
                    "name": f"{bio['surname']}, {bio.get('given_names')}",
                    "birth_year": bio.get("birth_year"),
                    "honours": [h["award"] for h in bio.get("honours", [])],
                    "editions": [year, year],
                    "lines": bio_lines(bio),
                },
            })
    rng.shuffle(rows)
    with open(OUT / "b1_audit_worklist.jsonl", "w", encoding="utf-8") as fh:
        for r in rows:
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")

    # report
    n = len(scores)
    st_counts = Counter(f["stratum"] for f in scores)
    lines = [
        "# B1 within-volume link audit",
        "",
        f"{n:,} links scored over {len(editions)} editions; sample of"
        f" {len(rows)} drawn ({SAMPLE_PER_STRATUM}/stratum, seed {SEED}).",
        "",
        "| stratum | links | sampled | median sim | rivals>0 | thin names |",
        "|---|---|---|---|---|---|",
    ]
    for st in sorted(st_counts):
        pool = by_stratum_pool[st]
        sims = sorted(p["position_sim"] for p in pool)
        riv = sum(1 for p in pool if p["rivals_colony"] > 0)
        thin = sum(1 for p in pool if p["name_class"] in ("thin", "partial"))
        lines.append(
            f"| {st} | {len(pool):,} | {min(len(pool), SAMPLE_PER_STRATUM)}"
            f" | {sims[len(sims)//2]:.0f} | {riv/len(pool):.1%}"
            f" | {thin/len(pool):.1%} |")
    lines += [
        "",
        "Adjudicate on Nibi with the classc worker unchanged:",
        "",
        "```",
        "python3 qwen_classc_worker.py --worklist b1_audit_worklist.jsonl \\",
        "    --out b1_audit_results.jsonl --url http://localhost:8000/v1",
        "```",
        "",
        "Precision per stratum = same / (same + different) over verdicts;",
        "extrapolate by stratum weight for the corpus-wide measured rate.",
    ]
    (OUT / "B1_AUDIT.md").write_text("\n".join(lines) + "\n",
                                     encoding="utf-8")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
