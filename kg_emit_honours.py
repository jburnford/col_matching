#!/usr/bin/env python3
"""Emit the HONOUR / award layer of the KG.

Reads the raw honours edge list (person -> award string + year) + the honour
grounding cache and writes TWO layers (split by kg_honour_norm.honour_class):
  data/kg/graph_stage3/honour_nodes.jsonl        state honours: orders, decorations,
  data/kg/graph_stage3/honour_edges.jsonl        medals, appointments (KC/PC...)
  data/kg/graph_stage3/qualification_nodes.jsonl academic degrees (MA/BSc/MD...) +
  data/kg/graph_stage3/qualification_edges.jsonl professional memberships (FRCS/MICE)

Per Jim 2026-06-24: degrees + learned-society memberships are NOT honours, so they
go to a separate `qualifications` layer (same grounding cache + QIDs, different
output file).

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
from kg_honour_norm import parse_honour, honour_class

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

    # two layers: "honour" (orders/decorations/medals) and "qual" (degrees+memberships)
    L = {k: {"nodes": {}, "n_people": Counter(), "seen": set(), "edges": [],
             "stat": Counter()} for k in ("honour", "qual")}
    minted = {}

    def use_node(layer, rid, label, typ, source):
        nd = L[layer]["nodes"]
        if rid not in nd:
            nd[rid] = {"id": rid, "label": label, "type": typ, "source": source}

    for e in edges_in:
        base, mods, cat = parse_honour(e.get("award"))
        edge = {"person_id": e["person_id"], "award_raw": e.get("award"),
                "year": e.get("year"), "modifiers": mods}
        if base == "_unknown":
            L["honour"]["stat"]["unknown"] += 1
            edge.update(honour_id=None, honour_label=None, source=None)
            L["honour"]["edges"].append(edge)
            continue
        layer = "qual" if honour_class(base) in ("degree", "membership") else "honour"
        lid_field = "qualification_id" if layer == "qual" else "honour_id"
        llbl_field = "qualification_label" if layer == "qual" else "honour_label"
        r = cache.get(nrm(base))
        if not r:  # internal-mint uncached honour
            r = minted.get(nrm(base))
            if not r:
                r = {"institution": base, "type": cat, "id": slug(base),
                     "label": base, "source": "internal", "match_type": "internal_mint"}
                minted[nrm(base)] = r
        use_node(layer, r["id"], r.get("label", base), r.get("type", cat), r["source"])
        edge.update({lid_field: r["id"], llbl_field: r.get("label", base), "source": r["source"]})
        L[layer]["stat"]["cached_qid" if str(r["id"]).startswith("Q") else "internal"] += 1

        key = (e["person_id"], r["id"])
        if key not in L[layer]["seen"]:
            L[layer]["n_people"][r["id"]] += 1; L[layer]["seen"].add(key)
        L[layer]["edges"].append(edge)

    out = {"honour": ("honour_nodes.jsonl", "honour_edges.jsonl"),
           "qual": ("qualification_nodes.jsonl", "qualification_edges.jsonl")}
    print(f"internal-minted this run: {len(minted)}")
    for layer, (nf, ef) in out.items():
        d = L[layer]
        for rid, node in d["nodes"].items():
            node["n_people"] = d["n_people"][rid]
        with (GD / nf).open("w") as fh:
            for n in sorted(d["nodes"].values(), key=lambda n: -n["n_people"]):
                fh.write(json.dumps(n, ensure_ascii=False) + "\n")
        with (GD / ef).open("w") as fh:
            for ed in d["edges"]:
                fh.write(json.dumps(ed, ensure_ascii=False) + "\n")
        tot = len(d["edges"])
        qid = sum(1 for n in d["nodes"].values() if str(n["id"]).startswith("Q"))
        print(f"[{layer}] nodes: {len(d['nodes']):,} (Wikidata {qid} / internal "
              f"{len(d['nodes'])-qid}); edges: {tot:,}")
        for k in ["cached_qid", "internal", "unknown"]:
            if d["stat"][k]:
                print(f"    {k:12} {d['stat'][k]:6} ({100*d['stat'][k]/tot:.0f}%)")

if __name__ == "__main__":
    main()
