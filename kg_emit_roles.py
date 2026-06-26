#!/usr/bin/env python3
"""Emit the ROLE / occupation layer of the KG.

Reads the career-event layer + the role grounding cache and writes:
  data/kg/graph_stage3/roles.jsonl        role nodes (Wikidata QID or colkg:)
  data/kg/graph_stage3/role_edges.jsonl   person -> role, one per career event,
                                          carrying the seniority/status modifiers

Disposition per career event (via kg_role_norm.parse_position):
  - base role in the grounding cache  -> link to that node (QID or colkg:)
  - base role uncached & not a control bucket -> internal-mint colkg:<role>
  - '_military_service' -> the single colkg:military_service node (a career state)
  - '_unknown' / '_honour' -> no node; edge keeps role_id=null + position_raw for review

Modifiers (acting/assistant/deputy/senior/junior/additional/temporary/graded) ride
on the edge, NOT the node, so "acting colonial secretary" and "colonial secretary"
share one role node.  Run AFTER grounding; then kg_dedup_nodes.py.
"""
from __future__ import annotations
import json, re
from pathlib import Path
from collections import Counter
from kg_role_norm import parse_position

from col_match.kg.paths import kg_out
GD = kg_out() / "graph_stage3"
CACHE = kg_out() / "role_grounding.jsonl"
WORK = kg_out() / "position_worklist.jsonl"
EVENTS = GD / "career_events.jsonl"

def nrm(s: str) -> str:
    return re.sub(r"\s+", " ", (s or "")).strip().rstrip(".").strip().casefold()

def slug(name: str) -> str:
    return "colkg:" + re.sub(r"_+", "_", re.sub(r"[^A-Za-z0-9]+", "_", name)).strip("_")

def load_jsonl(p):
    return [json.loads(l) for l in p.open()] if p.exists() else []

def main():
    cache = {r["institution"]: r for r in load_jsonl(CACHE)}
    work = {w["institution"]: w for w in load_jsonl(WORK)}
    events = load_jsonl(EVENTS)

    ncache = {}
    for r in cache.values():
        k = nrm(r["institution"])
        if k not in ncache or (str(r["id"]).startswith("Q") and not str(ncache[k]["id"]).startswith("Q")):
            ncache[k] = r

    role_nodes, n_people, seen, edges = {}, Counter(), set(), []
    stat = Counter()

    def use_node(rid, label, cat, source, qid_country=None):
        if rid not in role_nodes:
            role_nodes[rid] = {"id": rid, "label": label, "category": cat, "source": source}

    minted = {}
    for e in events:
        raw = e.get("position_norm") or e.get("position")
        if not raw:
            continue
        base, mods, cat = parse_position(raw)
        edge = {"person_id": e["person_id"], "seq": e.get("seq"), "position_raw": raw.strip(),
                "year_start": e.get("year_start"), "year_end": e.get("year_end"),
                "modifiers": mods, "category": cat}

        if base == "_military_service":
            use_node("colkg:military_service", "military service", "military", "internal")
            edge.update(role_id="colkg:military_service", role_label="military service", source="internal")
            stat["military_service"] += 1
        elif base in ("_unknown", "_honour"):
            edge.update(role_id=None, role_label=None, source="ungrounded")
            stat["ungrounded"] += 1
        else:
            r = cache.get(base) or ncache.get(nrm(base))
            if not r:  # internal-mint uncached role
                r = minted.get(nrm(base))
                if not r:
                    r = {"institution": base, "type": cat, "id": slug(base), "label": base,
                         "instance_of": [], "country_qid": None,
                         "source": "internal", "match_type": "internal_mint"}
                    minted[nrm(base)] = r
            use_node(r["id"], r.get("label", base), r.get("type", cat), r["source"], r.get("country_qid"))
            edge.update(role_id=r["id"], role_label=r.get("label", base), source=r["source"])
            stat["cached_qid" if str(r["id"]).startswith("Q") else "internal"] += 1

        if edge.get("role_id"):
            key = (e["person_id"], edge["role_id"])
            if key not in seen:
                n_people[edge["role_id"]] += 1; seen.add(key)
        edges.append(edge)

    # NB: emit is READ-ONLY on the cache. Auto-mints stay in-memory so the cache
    # holds only deliberate grounding decisions and `pending` keeps surfacing the
    # ungrounded head. The tail is re-minted deterministically every run.
    for rid, node in role_nodes.items():
        node["n_people"] = n_people[rid]
    with (GD / "roles.jsonl").open("w") as fh:
        for n in sorted(role_nodes.values(), key=lambda n: -n["n_people"]):
            fh.write(json.dumps(n, ensure_ascii=False) + "\n")
    with (GD / "role_edges.jsonl").open("w") as fh:
        for ed in edges:
            fh.write(json.dumps(ed, ensure_ascii=False) + "\n")

    tot = len(edges)
    qid = sum(1 for n in role_nodes.values() if str(n["id"]).startswith("Q"))
    print(f"internal-minted this run: {len(minted)}")
    print(f"role nodes: {len(role_nodes):,} (Wikidata {qid} / internal {len(role_nodes)-qid})")
    print(f"role edges: {tot:,}")
    for k in ["cached_qid", "internal", "military_service", "ungrounded"]:
        if stat[k]:
            print(f"  {k:16} {stat[k]:6} ({100*stat[k]/tot:.0f}%)")

if __name__ == "__main__":
    main()
