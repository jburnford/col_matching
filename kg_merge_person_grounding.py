#!/usr/bin/env python3
"""Merge Layer-1 (harvest) + Layer-2 (colony+position) person groundings into one
final, zero-FP table -- resolving any cross-layer QID collisions.

Per QID, cluster all claimants by OCR/abbrev-tolerant name identity. If they form one
cluster they are the same person (dup fragments) -> keep all. If they split into
conflicting clusters, the POSITION-anchored Layer-2 match is authoritative (it is tied
to the actual office the Wikidata person held), so keep that cluster and drop the rest;
if the conflict has no L2 anchor to break it, drop all (ambiguous).
"""
import json, os, collections
from apply_person_verification import tokens_same_person
from kg_ground_persons import given_tokens

ROOT = os.path.dirname(os.path.abspath(__file__))
GD = os.path.join(ROOT, "data/kg/graph_stage3")

def cluster(members):
    n = len(members); parent = list(range(n))
    def find(x):
        while parent[x] != x: parent[x] = parent[parent[x]]; x = parent[x]
        return x
    toks = [given_tokens(m.get("kg_given")) for m in members]
    for i in range(n):
        for j in range(i+1, n):
            if tokens_same_person(toks[i], toks[j]): parent[find(i)] = find(j)
    g = collections.defaultdict(list)
    for i in range(n): g[find(i)].append(members[i])
    return list(g.values())

def main():
    l1 = [{**json.loads(l), "source": "L1"} for l in open(os.path.join(GD, "person_grounding.verified.jsonl"))]
    l2 = [{**json.loads(l), "source": "L2", "tier": "L2"} for l in open(os.path.join(GD, "person_grounding_l2.jsonl"))]
    # normalise field name (L2 uses wd_name already)
    rows = l1 + l2
    byq = collections.defaultdict(list)
    for r in rows: byq[r["qid"]].append(r)

    final, dropped = [], []
    for qid, members in byq.items():
        clusters = cluster(members)
        if len(clusters) == 1:
            final.extend(members); continue
        # conflict: prefer the cluster(s) containing an L2 (position-anchored) match
        l2_clusters = [c for c in clusters if any(m["source"] == "L2" for m in c)]
        if len(l2_clusters) == 1:
            for c in clusters:
                if c is l2_clusters[0]: final.extend(c)
                else: dropped.extend({**m, "drop": "lost_to_L2_position_anchor"} for m in c)
        else:
            dropped.extend({**m, "drop": "crosslayer_ambiguous"} for m in members)

    # dedup exact (person_id,qid) keeping L2 over L1 if both
    seen = {}
    for r in final:
        k = (r["person_id"], r["qid"])
        if k not in seen or r["source"] == "L2":
            seen[k] = r
    final = list(seen.values())

    with open(os.path.join(GD, "person_grounding.final.jsonl"), "w") as f:
        for r in final:
            f.write(json.dumps(r) + "\n")
    with open(os.path.join(ROOT, "data/kg/person_grounding_merge_dropped.jsonl"), "w") as f:
        for r in dropped:
            f.write(json.dumps(r) + "\n")

    src = collections.Counter(r["source"] for r in final)
    print(f"merged final groundings: {len(final)}  (L1={src['L1']} L2={src['L2']})")
    print(f"distinct persons: {len({r['person_id'] for r in final})}  distinct QIDs: {len({r['qid'] for r in final})}")
    print(f"dropped in merge: {len(dropped)}")
    for d in dropped:
        print(f"  DROP[{d['drop']}] {d['source']} {d['kg_surname']},{d.get('kg_given')} -> {d['wd_name']} {d['qid']}")

if __name__ == "__main__":
    main()
