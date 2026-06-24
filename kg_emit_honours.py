#!/usr/bin/env python3
"""Emit the HONOUR / award layer of the KG.

Reads the raw honours edge list (person -> award string + year) + the honour
grounding cache and writes:
  data/kg/graph_stage3/honour_nodes.jsonl   honour-type nodes (Wikidata QID or colkg:)
  data/kg/graph_stage3/honour_edges.jsonl   person -> honour, one per award mention,
                                            carrying year + branch modifiers

Disposition per award (via kg_honour_norm.parse_honour):
  - base honour in the grounding cache  -> link to that node (QID or colkg:)
  - base honour uncached & not control  -> internal-mint colkg:<honour>
  - '_unknown' (noise: bare "medal"/"board"/clasp) -> no node; edge keeps
    honour_id=null + award_raw for review

Branch qualifiers (military / civil) ride on the EDGE, not the node, so "M.B.E."
and "M.B.E. (mil.)" share one node.  Run AFTER grounding.  Read-only on the cache
(uncached tail is re-minted deterministically every run, mirroring kg_emit_roles).
"""
from __future__ import annotations
import json, re
from pathlib import Path
from collections import Counter
from kg_honour_norm import parse_honour

GD = Path("data/kg/graph_stage3")
CACHE = Path("data/kg/honour_grounding.jsonl")
HON = GD / "honours.jsonl"

def nrm(s: str) -> str:
    return re.sub(r"\s+", " ", (s or "")).strip().rstrip(".").strip().casefold()

def slug(name: str) -> str:
    return "colkg:" + re.sub(r"_+", "_", re.sub(r"[^A-Za-z0-9]+", "_", name)).strip("_")

def load_jsonl(p):
    return [json.loads(l) for l in p.open()] if p.exists() else []

def main():
    cache = {nrm(r["institution"]): r for r in load_jsonl(CACHE)}
    edges_in = load_jsonl(HON)

    nodes, n_people, seen, edges, minted = {}, Counter(), set(), [], {}
    stat = Counter()

    def use_node(rid, label, typ, source):
        if rid not in nodes:
            nodes[rid] = {"id": rid, "label": label, "type": typ, "source": source}

    for e in edges_in:
        base, mods, cat = parse_honour(e.get("award"))
        edge = {"person_id": e["person_id"], "award_raw": e.get("award"),
                "year": e.get("year"), "modifiers": mods}
        if base == "_unknown":
            stat["unknown"] += 1
            edge.update(honour_id=None, honour_label=None, source=None)
            edges.append(edge)
            continue
        r = cache.get(nrm(base))
        if not r:  # internal-mint uncached honour
            r = minted.get(nrm(base))
            if not r:
                r = {"institution": base, "type": cat, "id": slug(base),
                     "label": base, "source": "internal", "match_type": "internal_mint"}
                minted[nrm(base)] = r
        use_node(r["id"], r.get("label", base), r.get("type", cat), r["source"])
        edge.update(honour_id=r["id"], honour_label=r.get("label", base), source=r["source"])
        stat["cached_qid" if str(r["id"]).startswith("Q") else "internal"] += 1

        key = (e["person_id"], r["id"])
        if key not in seen:
            n_people[r["id"]] += 1; seen.add(key)
        edges.append(edge)

    for rid, node in nodes.items():
        node["n_people"] = n_people[rid]
    with (GD / "honour_nodes.jsonl").open("w") as fh:
        for n in sorted(nodes.values(), key=lambda n: -n["n_people"]):
            fh.write(json.dumps(n, ensure_ascii=False) + "\n")
    with (GD / "honour_edges.jsonl").open("w") as fh:
        for ed in edges:
            fh.write(json.dumps(ed, ensure_ascii=False) + "\n")

    tot = len(edges)
    qid = sum(1 for n in nodes.values() if str(n["id"]).startswith("Q"))
    print(f"internal-minted this run: {len(minted)}")
    print(f"honour nodes: {len(nodes):,} (Wikidata {qid} / internal {len(nodes)-qid})")
    print(f"honour edges: {tot:,}")
    for k in ["cached_qid", "internal", "unknown"]:
        if stat[k]:
            print(f"  {k:12} {stat[k]:6} ({100*stat[k]/tot:.0f}%)")

if __name__ == "__main__":
    main()
