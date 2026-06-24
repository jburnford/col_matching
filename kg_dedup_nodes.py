#!/usr/bin/env python3
"""Node-dedup cycle for the v2 institution + v2.1 organisation layers.

Post-processes the emitted graph files in place, merging duplicate nodes and
remapping the edges that point at them. Two duplicate classes are folded:

  1. CASE / SPACING variants -- event strings that missed the (case-sensitive)
     grounding cache and got their own colkg: node even though a QID (or another
     colkg:) node for the same name exists. Grouped by normalised label; the
     Wikidata QID always wins as canonical.
  2. COLONY-DEPARTMENT word-order variants (org layer only) -- "Natal treasury"
     (internal) vs "Natal Treasury" (resolved), "audit department, Kenya" vs
     "Kenya Audit Department". Grouped by a colony+dept-type TOKEN SET (order- and
     boilerplate-insensitive) so the two id schemes collapse to one node.

n_people is re-summed across merged nodes; a `merged_from` list records the
absorbed ids. Re-run safe. Run AFTER kg_emit_org.py / `... emit`.
"""
from __future__ import annotations
import json, re
from pathlib import Path
from collections import defaultdict

GD = Path("data/kg/graph_stage3")

DEPTKW = re.compile(r"treasury|secretariat|customs|public works|\baudit\b|education depart|"
                    r"medical depart|judicial|survey depart|\bfinance\b|\bstores\b|\bmines\b|"
                    r"immigration|native affairs|district administration|forest depart", re.I)
STOP = {"department", "dept", "of", "and", "the", "a", "colony", "protectorate", "crown",
        "service", "services", "office", "bureau", "administration", "admin", "govt",
        "government", "s", "'s", "amp"}

def norm(s: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", (s or "").lower()).strip()

def group_key(node):
    """Canonical grouping key. Dept-like non-QID nodes use an order-insensitive
    colony+type token set; everything else uses the normalised label (so a colkg
    case-variant lands in the same group as its QID twin)."""
    lbl = node["label"]
    if not str(node["id"]).startswith("Q") and DEPTKW.search(lbl) and node.get("type") != "railway":
        toks = frozenset(t for t in norm(lbl).split() if t not in STOP)
        if toks:
            return ("dept", toks)
    return ("lbl", norm(lbl))

def canonicalize(nodes_file, edges_file, id_field, label_field, dept_aware):
    nodes = [json.loads(l) for l in (GD / nodes_file).open()]
    edges = [json.loads(l) for l in (GD / edges_file).open()]

    groups = defaultdict(list)
    for n in nodes:
        key = group_key(n) if dept_aware else ("lbl", norm(n["label"]))
        groups[key].append(n)

    idmap = {}            # old id -> (canonical id, canonical label)
    out_nodes = []
    merged = 0
    for key, grp in groups.items():
        qs = [n for n in grp if str(n["id"]).startswith("Q")]
        rc = [n for n in grp if n.get("source") == "resolved_colony"]
        if qs:
            canon = min(qs, key=lambda n: int(str(n["id"])[1:]))
        elif rc:
            # prefer the clean "<Colony> <Dept>" resolved label over a messy
            # internal surface like "audit department, Kenya"
            canon = max(rc, key=lambda n: n.get("n_people", 0))
        else:
            canon = max(grp, key=lambda n: n.get("n_people", 0))
        total = sum(n.get("n_people", 0) for n in grp)
        for n in grp:
            idmap[n["id"]] = (canon["id"], canon["label"])
        node = dict(canon)
        node["n_people"] = total
        if len(grp) > 1:
            node["merged_from"] = sorted({str(n["id"]) for n in grp if n["id"] != canon["id"]})
            merged += len(grp) - 1
        out_nodes.append(node)

    for e in edges:
        i = e.get(id_field)
        if i in idmap:
            cid, clabel = idmap[i]
            e[id_field], e[label_field] = cid, clabel

    out_nodes.sort(key=lambda n: -n.get("n_people", 0))
    with (GD / nodes_file).open("w") as fh:
        for n in out_nodes:
            fh.write(json.dumps(n, ensure_ascii=False) + "\n")
    with (GD / edges_file).open("w") as fh:
        for e in edges:
            fh.write(json.dumps(e, ensure_ascii=False) + "\n")
    print(f"{nodes_file}: {len(nodes)} -> {len(out_nodes)} nodes ({merged} merged); "
          f"{len(edges)} edges remapped")

if __name__ == "__main__":
    canonicalize("organisations.jsonl", "employment_edges.jsonl",
                 "org_id", "org_label", dept_aware=True)
    canonicalize("institutions.jsonl", "education_edges.jsonl",
                 "institution_id", "institution_label", dept_aware=False)
    if (GD / "roles.jsonl").exists():
        canonicalize("roles.jsonl", "role_edges.jsonl",
                     "role_id", "role_label", dept_aware=False)
