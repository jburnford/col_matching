#!/usr/bin/env python3
"""Audit the IOL stage-3 dedup merge map: score every merge edge, draw a
stratified sample for Nibi adjudication (docs/IOL_VS_COL.md §4; the
volume_link_audit.py pattern one layer up).

The shipped person table folds 30,446 LLM-structured records into 17,922
canonical persons through 12,540 union edges whose precision was never
measured — the COL B1 story again. Each edge (X -> C) is a claim that two
cross-edition bio chains are the same person. This scores every edge on
signals INDEPENDENT of the pass that created it, then samples per stratum
so Nibi verdicts convert into measured precision per stratum.

Strata = evidence_class x risk tercile (terciled only where the class has
>= 900 edges):

  evidence_class      which pass created the edge, base edges split by the
                      candidates-file tier:
                        base:A_birth      birth-year-anchored merges
                        base:C_posting    shared-posting merges
                        base:B_other      B_thin/B_place/CONFLICT_* + LLM/hand
                        crossform         surname-only block, shared event
                        roleyear          role+colony+year, rank-stripped name
                        school            school-blocked, confident/likely
  risk tercile        transparent points: birth agreement, shared dated
                      honours, shared postings, name completeness, surname
                      frequency, edition overlap (two chains of one person
                      should not both print in the same edition)

Outputs data/iol/identity/{merge_edge_scores.jsonl, merge_audit_worklist.jsonl,
MERGE_AUDIT.md}. The worklist is qwen_classc_worker.py --mode ioldedup pair
format. Read-only; applies nothing.
"""

from __future__ import annotations

import json
import random
import re
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path("data/iol")
OUT = ROOT / "identity"
SAMPLE_PER_STRATUM = 150
TERCILE_MIN_POOL = 900
SEED = 20260711

MAPS = [("base", "dedup_stage3_merge_map.jsonl"),
        ("crossform", "dedup_stage3_merge_map.crossform.jsonl"),
        ("roleyear", "dedup_stage3_merge_map.roleyear.jsonl"),
        ("school", "dedup_stage3_merge_map.school.jsonl")]


def jload(path: Path):
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            yield json.loads(line)


def surname_key(s: str | None) -> str:
    return re.sub(r"[^A-Z]", "", (s or "").upper())


def award_key(a: str | None) -> str:
    return re.sub(r"[^A-Z]", "", (a or "").upper())


def posstem(p: str | None) -> str:
    return re.sub(r"[^a-z]", "", (p or "").lower())[:10]


def name_class(given: str | None) -> str:
    toks = [t for t in re.split(r"[ .,]+", given or "") if t]
    if not toks:
        return "none"
    return "full" if any(len(t) > 1 for t in toks) else "initials"


def postings(rec: dict) -> set[tuple[str, int]]:
    out = set()
    for e in rec.get("events") or []:
        y = e.get("year_start")
        st = posstem(e.get("position"))
        if y and len(st) >= 4:
            out.add((st, y))
    return out


def honour_set(rec: dict) -> set[tuple[str, int]]:
    return {(award_key(h.get("award")), h["year"])
            for h in (rec.get("honours") or [])
            if h.get("year") and award_key(h.get("award"))}


def rec_lines(rec: dict, cap: int = 16) -> list[str]:
    lines = []
    if rec.get("education"):
        lines.append(f"  educ: {rec['education'][:160]}")
    evs = rec.get("events") or []
    for e in evs[:cap]:
        y0, y1 = e.get("year_start"), e.get("year_end")
        yr = f"{y0}" + (f"-{y1}" if y1 and y1 != y0 else "") if y0 else "n.d."
        pl = f" — {e['place']}" if e.get("place") else ""
        act = " (actg.)" if e.get("is_acting") else ""
        lines.append(f"  {yr}: {e.get('position') or '?'}{pl}{act}")
    if len(evs) > cap:
        lines.append(f"  ... +{len(evs) - cap} more events")
    return lines


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    recs = {r["person_id"]: r for r in
            jload(ROOT / "llm_struct_corpus.valid.jsonl")}
    editions = {r["person_id"]: r.get("editions") or []
                for r in jload(ROOT / "persons.deduped.jsonl")}
    pid_tier = {}
    for g in jload(ROOT / "dedup_stage3_candidates.jsonl"):
        for m in g["members"]:
            pid_tier[m["person_id"]] = g["tier"]

    maps = {name: {r["person_id"]: r["canonical_person_id"]
                   for r in jload(ROOT / fn)} for name, fn in MAPS}
    school = maps["school"]

    surname_freq = Counter(surname_key(r.get("surname"))
                           for r in recs.values())

    def edge_class(x: str) -> str:
        for name, _ in MAPS:
            if x in maps[name]:
                if name != "base":
                    return name
                tier = pid_tier.get(x)
                if tier == "A_birth":
                    return "base:A_birth"
                if tier == "C_posting":
                    return "base:C_posting"
                return "base:B_other"
        raise AssertionError(x)

    canon_keys = set(school.values()) & set(school)  # 16 unflattened (known)

    scored = []
    for x, c in school.items():
        a, b = recs[x], recs[c]
        f = {"person_a": x, "person_b": c,
             "evidence_class": edge_class(x),
             "surname": a.get("surname"),
             "given_a": a.get("given_names"), "given_b": b.get("given_names"),
             "unflattened_canonical": c in canon_keys}
        pts = 0
        ba, bb = a.get("birth_year"), b.get("birth_year")
        if ba and bb:
            d = abs(ba - bb)
            f["birth"] = "agree" if d == 0 else ("near" if d <= 1 else "conflict")
            pts += {"agree": 30, "near": 20, "conflict": -30}[f["birth"]]
        else:
            f["birth"] = "missing"
        sh = honour_set(a) & honour_set(b)
        f["shared_honours"] = len(sh)
        if sh:
            pts += 25
        pa, pb = postings(a), postings(b)
        shared_post = pa & pb
        f["shared_postings"] = len(shared_post)
        if shared_post:
            pts += 25
        elif {y for _, y in pa} & {y for _, y in pb}:
            pts += 5  # same active years at least
        nca, ncb = name_class(a.get("given_names")), name_class(b.get("given_names"))
        f["name_class"] = f"{nca}:{ncb}"
        if nca == ncb == "full":
            pts += 15
        elif "full" not in (nca, ncb):
            pts -= 10
        freq = surname_freq[surname_key(a.get("surname"))]
        f["surname_freq"] = freq
        pts += 15 if freq <= 3 else (5 if freq <= 10 else (-10 if freq >= 30 else 0))
        ov = len(set(editions.get(x, [])) & set(editions.get(c, [])))
        f["edition_overlap"] = ov
        if ov:
            pts -= 15
        f["score"] = pts
        scored.append(f)

    # terciles within class (big classes only)
    by_class = defaultdict(list)
    for f in scored:
        by_class[f["evidence_class"]].append(f)
    pools = defaultdict(list)
    for cls, fs in by_class.items():
        if len(fs) >= TERCILE_MIN_POOL:
            ss = sorted(x["score"] for x in fs)
            lo, hi = ss[len(ss) // 3], ss[2 * len(ss) // 3]
            for f in fs:
                f["risk_tier"] = ("high" if f["score"] < lo
                                  else "low" if f["score"] >= hi else "mid")
                f["stratum"] = f"{cls}:{f['risk_tier']}"
                pools[f["stratum"]].append(f)
        else:
            for f in fs:
                f["risk_tier"] = None
                f["stratum"] = cls
                pools[cls].append(f)

    with open(OUT / "merge_edge_scores.jsonl", "w", encoding="utf-8") as fh:
        for f in scored:
            fh.write(json.dumps(f, ensure_ascii=False) + "\n")

    # stratified sample -> worker pair worklist (--mode ioldedup)
    rng = random.Random(SEED)
    rows = []
    for st in sorted(pools):
        pool = pools[st]
        take = pool if len(pool) <= SAMPLE_PER_STRATUM \
            else rng.sample(pool, SAMPLE_PER_STRATUM)
        for f in take:
            def side(pid: str) -> dict:
                r = recs[pid]
                eds = editions.get(pid) or []
                return {
                    "name": f"{r.get('surname') or '?'}, "
                            f"{r.get('given_names') or '?'}",
                    "birth_year": r.get("birth_year"),
                    "honours": [f"{h.get('award')}"
                                + (f" ({h['year']})" if h.get("year") else "")
                                for h in (r.get("honours") or [])][:10],
                    "editions": [min(eds), max(eds)] if eds else None,
                    "lines": rec_lines(r),
                }
            rows.append({
                "id": f"iolm::{f['person_a']}::{f['person_b']}",
                "stratum": st,
                "evidence_class": f["evidence_class"],
                "person_a": f["person_a"], "person_b": f["person_b"],
                "a": side(f["person_a"]), "b": side(f["person_b"]),
            })
    with open(OUT / "merge_audit_worklist.jsonl", "w", encoding="utf-8") as fh:
        for r in rows:
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")

    # report
    lines = [
        "# IOL merge-map audit — stratified sample for Nibi adjudication",
        "",
        f"{len(scored):,} merge edges scored; {len(rows):,} drawn "
        f"({SAMPLE_PER_STRATUM}/stratum, seed {SEED}).",
        "",
        "| stratum | edges | sampled | median score | birth agree | "
        "shared posting | edition overlap |",
        "|---|---|---|---|---|---|---|",
    ]
    st_sampled = Counter(r["stratum"] for r in rows)
    for st in sorted(pools):
        pool = pools[st]
        ss = sorted(f["score"] for f in pool)
        med = ss[len(ss) // 2]
        agree = sum(1 for f in pool if f["birth"] in ("agree", "near"))
        post = sum(1 for f in pool if f["shared_postings"])
        ov = sum(1 for f in pool if f["edition_overlap"])
        lines.append(f"| {st} | {len(pool):,} | {st_sampled[st]} | {med} | "
                     f"{agree/len(pool):.0%} | {post/len(pool):.0%} | "
                     f"{ov/len(pool):.0%} |")
    lines += [
        "",
        "Run on nibi: `qwen_classc_worker.py --mode ioldedup` "
        "(slurm: `nibi/qwen_iol_merge.slurm`).",
        "Precision per stratum = same / (same + different); extrapolate by",
        "stratum weight for the corpus-wide measured rate.",
    ]
    (OUT / "MERGE_AUDIT.md").write_text("\n".join(lines) + "\n",
                                        encoding="utf-8")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
