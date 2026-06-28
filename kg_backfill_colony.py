#!/usr/bin/env python3
"""Backfill colony_qid for officials still placeless after the place->colony
crosswalk (Fix A), so they stop being dropped from the careers map.

Runs PER CORPUS (COL_KG_OUT switches data/kg <-> data/iol). Targets ONLY persons
with NO colony on ANY career event -- the atlas already carries colony-less events
of partially-placed people to their nearest known colony, so the only dropped
officials are the truly zero-colony ones. For each:

  B. org->colony rollup -- the person's grounded EMPLOYER carries a country_qid
     (organisations.jsonl: 'Survey of India'->Q668, 'Uganda railway'->Uganda).
     Roll that country up to a colony (country level, no province). When a person
     has several employer-countries, the most frequent wins.
  C. IOL corpus default -- a still-placeless India Office List official served the
     Indian Empire by definition -> British Raj (Q129286).

Rewrites career_events.jsonl in place (backfilled events get
colony_method=org_rollup|iol_default and grounded_colony_backfill=true), then the
caller re-runs kg_emit_career_facts.py to propagate to career_facts.jsonl.
"""
from __future__ import annotations
import json, collections
from pathlib import Path
from col_match.kg.paths import kg_out
from kg_build_place_colony_crosswalk import country_to_colony

GD = kg_out() / "graph_stage3"
IS_IOL = "iol" in str(kg_out()).lower()
BRITISH_RAJ = ("Q129286", "Indian Empire (British Raj)")


def load(p):
    return [json.loads(l) for l in (GD / p).open()]


def main():
    events = load("career_events.jsonl")
    orgs = {o["id"]: o for o in load("organisations.jsonl")}
    emp = load("employment_edges.jsonl")

    # person -> Counter(country_qid) from grounded employers
    person_ctry = collections.defaultdict(collections.Counter)
    for e in emp:
        cc = orgs.get(e.get("org_id"), {}).get("country_qid")
        if cc:
            person_ctry[e["person_id"]][cc] += 1

    # persons with zero colony on any event
    has_colony = set()
    by_person = collections.defaultdict(list)
    for ev in events:
        by_person[ev["person_id"]].append(ev)
        if ev.get("colony_qid"):
            has_colony.add(ev["person_id"])
    placeless = [p for p in by_person if p not in has_colony]

    stat = collections.Counter()
    method_breakdown = collections.Counter()
    for pid in placeless:
        col = None
        # B. org->colony (most frequent employer country)
        if person_ctry.get(pid):
            for cq, _ in person_ctry[pid].most_common():
                r = country_to_colony(cq)
                if r:
                    col = (r[0], r[1], r[2]); break
        # C. IOL default
        if not col and IS_IOL:
            col = (BRITISH_RAJ[0], BRITISH_RAJ[1], "iol_default")
        if not col:
            stat["still_placeless"] += 1
            continue
        cq, cl, method = col
        for ev in by_person[pid]:
            ev["colony_qid"] = cq
            ev["colony_label"] = cl
            ev["colony_method"] = method
            ev["colony_backfill"] = True
        stat["recovered_persons"] += 1
        method_breakdown[method] += 1

    with (GD / "career_events.jsonl").open("w", encoding="utf-8") as fh:
        for ev in events:
            fh.write(json.dumps(ev, ensure_ascii=False) + "\n")

    corpus = "IOL" if IS_IOL else "CO"
    print(f"[{corpus}] placeless persons targeted: {len(placeless):,}")
    print(f"  recovered: {stat['recovered_persons']:,}   still placeless: {stat['still_placeless']:,}")
    for m, n in method_breakdown.most_common():
        print(f"    {m:22s} {n:,}")


if __name__ == "__main__":
    main()
