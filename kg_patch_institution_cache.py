#!/usr/bin/env python3
"""Institution-cache corrections from the 2026-09-03 review (C20/C23):
  CO  Royal Military College, Sandhurst  Q575618 (1947 Academy) -> Q17020147 (1802 College)
  IOL St. Xavier's High School, Bombay   Q26258687 (1957 academy) -> Q7592184
  ambiguous (Jim's rule: bare multi-referent surfaces are flagged, never merged):
      St. Ignatius College (Galway / Malta / Stamford Hill), Royal Grammar School
      (Lancaster / Newcastle / Colchester), St Andrew's College (Dublin / Grahamstown)
  Haileybury (IOL): the surface names BOTH the East India Company College
      (1806-58, Q142599) and the 1862 public school (Q5639263). Marked ambiguous;
      per-person mention overrides are written by birth year / first career year
      (attended before 1858 -> EIC College) into education_mention_overrides.jsonl.
Idempotent. Run, then `kg_ground_institutions.py emit` per corpus + kg_dedup_nodes.
"""
import json
from pathlib import Path

CO = Path("data/kg/institutions_grounding.jsonl")
IOL = Path("data/iol/institutions_grounding.jsonl")
REGROUND = {CO: {"Royal Military College, Sandhurst": ("Q17020147", "Royal Military College, Sandhurst")},
            IOL: {"St. Xavier's High School, Bombay": ("Q7592184", "St. Xavier's High School, Bombay")}}
AMBIG = {CO: {"St. Ignatius College", "Royal Grammar School", "St Andrew's College", "St. Andrew's College"},
         IOL: {"St. Ignatius College", "Haileybury", "Haileybury College"}}
EIC, PUB = ("Q142599", "East India Company College"), ("Q5639263", "Haileybury College")


def patch(cache):
    rows = [json.loads(l) for l in cache.open(encoding="utf-8")]
    n = 0
    for r in rows:
        inst = r["institution"]
        if inst in REGROUND.get(cache, {}):
            q, lbl = REGROUND[cache][inst]
            if r.get("id") != q:
                r.update(id=q, label=lbl, source="curated", match_type="review_2026-09-04"); n += 1
        elif inst in AMBIG.get(cache, set()) and r.get("source") != "ambiguous":
            r.update(id=None, source="ambiguous", match_type="review_2026-09-04"); n += 1
    with cache.open("w", encoding="utf-8") as fh:
        for r in rows:
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")
    print(f"{cache}: {n} rows changed")


def haileybury_overrides():
    """IOL per-mention split of 'Haileybury' by the attendee's era."""
    work = {w["institution"]: w for w in map(json.loads, Path("data/iol/education_worklist.jsonl").open(encoding="utf-8"))}
    pids = {p for s in ("Haileybury", "Haileybury College") for p in work.get(s, {}).get("person_ids", [])}
    surf = {p: s for s in ("Haileybury", "Haileybury College") for p in work.get(s, {}).get("person_ids", [])}
    birth, first = {}, {}
    for l in Path("data/iol/graph_stage3/persons.jsonl").open(encoding="utf-8"):
        p = json.loads(l)
        if p["person_id"] in pids:
            birth[p["person_id"]] = p.get("birth_year")
    for l in Path("data/iol/graph_stage3/career_events.jsonl").open(encoding="utf-8"):
        e = json.loads(l)
        if e["person_id"] in pids and e.get("year_start"):
            first[e["person_id"]] = min(first.get(e["person_id"], 9999), e["year_start"])
    ovp = Path("data/iol/graph_stage3/education_mention_overrides.jsonl")
    have = {(r["person_id"], r["institution"]) for r in map(json.loads, ovp.open(encoding="utf-8"))} if ovp.exists() else set()
    n = {"eic": 0, "pub": 0, "skip": 0}
    with ovp.open("a", encoding="utf-8") as fh:
        for pid in sorted(pids):
            if (pid, surf[pid]) in have:
                continue
            b, f = birth.get(pid), first.get(pid)
            if (b and b <= 1842) or (not b and f and f <= 1860):
                q, lbl, k = *EIC, "eic"
            elif (b and b >= 1848) or (not b and f and f >= 1868):
                q, lbl, k = *PUB, "pub"
            else:
                n["skip"] += 1; continue           # 1843-47 births: either; leave unlinked
            fh.write(json.dumps({"person_id": pid, "institution": surf[pid], "institution_id": q,
                                 "institution_label": lbl, "type": "school",
                                 "cue": "era: birth<=1842 or first event<=1860 -> EIC College; birth>=1848 or first event>=1868 -> 1862 school"}) + "\n")
            n[k] += 1
    print(f"Haileybury overrides: {n}")


if __name__ == "__main__":
    patch(CO); patch(IOL); haileybury_overrides()
