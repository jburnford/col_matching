#!/usr/bin/env python3
"""Regenerate v3_manifest.json — the consolidated KG-stats document.

Nothing else writes this file, so it drifts whenever the graph is re-emitted
(dedup, re-grounding). Run it after kg_emit_stage3.py to keep the manifest in
sync with the live emit. Rooted on COL_KG_OUT like the other KG scripts:

    python3 kg_manifest.py                 # CO  (data/kg)
    COL_KG_OUT=data/iol python3 kg_manifest.py   # IOL

Reads graph_stage3/*.jsonl + kg_stats.json; writes graph_stage3/v3_manifest.json.
"""
import json
import os
from pathlib import Path

ROOT = Path(os.environ.get("COL_KG_OUT", "data/kg"))
G = ROOT / "graph_stage3"


def rows(name):
    p = G / f"{name}.jsonl"
    if not p.exists():
        return []
    return [json.loads(l) for l in p.open() if l.strip()]


def bucket(edges, key):
    """Split edge ids into Wikidata-QID / internal-colkg / unlinked counts."""
    qid = internal = unlinked = 0
    for e in edges:
        v = e.get(key)
        if not v:
            unlinked += 1
        elif str(v).startswith("Q"):
            qid += 1
        else:
            internal += 1
    return qid, internal, unlinked


def node_qids(nodes):
    return sum(1 for n in nodes if str(n.get("id", "")).startswith("Q"))


def main():
    # top-level emit stats are already computed by kg_emit_stage3.py
    stats = json.loads((G / "kg_stats.json").read_text())

    roles, role_edges = rows("roles"), rows("role_edges")
    r_q, r_i, r_u = bucket(role_edges, "role_id")

    orgs, emp_edges = rows("organisations"), rows("employment_edges")
    insts, edu_edges = rows("institutions"), rows("education_edges")

    h_nodes, h_edges = rows("honour_nodes"), rows("honour_edges")
    h_q, h_i, h_u = bucket(h_edges, "honour_id")

    q_nodes, q_edges = rows("qualification_nodes"), rows("qualification_edges")
    q_q, q_i, q_u = bucket(q_edges, "qualification_id")

    pg = rows("person_grounding.final")
    tiers = {}
    for r in pg:
        tiers[r.get("tier", "?")] = tiers.get(r.get("tier", "?"), 0) + 1

    cf = rows("career_facts")
    cf_role_qid = sum(1 for r in cf if str(r.get("role_id") or "").startswith("Q"))
    cf_role_any = sum(1 for r in cf if r.get("role_id"))
    cf_org = sum(1 for r in cf if r.get("org_id"))
    cf_place = sum(1 for r in cf if r.get("place_qid"))
    cf_dated = sum(1 for r in cf if r.get("year_start"))
    cf_rpt = sum(1 for r in cf if r.get("role_id") and r.get("place_qid") and r.get("year_start"))

    manifest = dict(stats)
    manifest["version"] = "v3"
    manifest["layers"] = {
        "roles": {
            "nodes": len(roles),
            "nodes_qid": node_qids(roles),
            "edges": len(role_edges),
            "edges_qid": r_q,
            "edges_internal": r_i,
            "edges_unlinked": r_u,
        },
        "organisations": {
            "nodes": len(orgs),
            "nodes_qid": node_qids(orgs),
            "employment_edges": len(emp_edges),
        },
        "education_institutions": {
            "nodes": len(insts),
            "nodes_qid": node_qids(insts),
            "education_edges": len(edu_edges),
        },
        "honours": {
            "nodes": len(h_nodes),
            "nodes_qid": node_qids(h_nodes),
            "edges": len(h_edges),
            "edges_qid": h_q,
            "edges_internal": h_i,
            "edges_unlinked": h_u,
        },
        "qualifications": {
            "nodes": len(q_nodes),
            "nodes_qid": node_qids(q_nodes),
            "edges": len(q_edges),
            "edges_qid": q_q,
            "edges_internal": q_i,
            "edges_unlinked": q_u,
        },
        "person_wikidata": {
            "method": "Layer1 harvest-match + WDQS verify; Layer2 colony+position via QLever",
            "persons_grounded": len(pg),
            "distinct_qids": len({r.get("qid") for r in pg if r.get("qid")}),
            "tiers": tiers,
            "layer2_senior_officials": tiers.get("L2", 0),
        },
    }
    manifest["career_facts"] = {
        "count": len(cf),
        "role_qid": cf_role_qid,
        "role_any": cf_role_any,
        "org": cf_org,
        "place": cf_place,
        "dated": cf_dated,
        "role_place_time": cf_rpt,
    }

    out = G / "v3_manifest.json"
    out.write_text(json.dumps(manifest, indent=2))
    print(f"wrote {out}")
    print(f"  persons={manifest['persons']} events={manifest['events']} "
          f"career_facts={len(cf)} persons_grounded={len(pg)}")


if __name__ == "__main__":
    main()
