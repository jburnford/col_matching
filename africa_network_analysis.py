#!/usr/bin/env python3
"""First-round Woldense-style mobility network analysis for British Africa.

Pipeline:
  1. clean person set  -> data/africa/africa_persons.jsonl  (>=1 African appointment)
  2. territory-level directed weighted transfer network (canonical territories):
     an edge A->B for each pair of a person's temporally-consecutive African
     appointments in DIFFERENT territories (non-African interludes collapsed;
     self-stays excluded, as in Woldense).
  3. structure vs a fixed-degree configuration-model null (clustering, reciprocity)
  4. communities (Louvain) vs the geographic region partition  -> is circulation
     regionally bounded? (region-partition modularity is the headline number)
  5. tenure-spell distribution; pre-1930 vs 1930+ split (the unification test)
Outputs: data/africa/{africa_persons.jsonl, africa_edges.csv, report.txt, figs/*}
"""
import json, os, csv, statistics as st
from collections import defaultdict, Counter
import networkx as nx
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

os.makedirs("data/africa/figs", exist_ok=True)
TERR = json.load(open("data/africa/africa_territories.json"))
CANON = {q: TERR[q]["canonical"] for q in TERR}
CLABEL = {TERR[q]["canonical"]: TERR[q]["canonical_label"] for q in TERR}
CREGION = {TERR[q]["canonical"]: TERR[q]["region"] for q in TERR}
AFR = set(TERR)
REPORT = []
def say(*a):
    line = " ".join(str(x) for x in a); print(line); REPORT.append(line)

# ---------------------------------------------------------------- 1. person set
careers = json.load(open("docs/data/careers.json"))["persons"]
persons = []
for pid, p in careers.items():
    afr = [(CANON[s[0]], s[1], s[2]) for s in p.get("st", []) if s[0] in AFR]
    if not afr:
        continue
    persons.append({"person_id": pid, "name": p.get("nm"), "wikidata": p.get("q"),
                    "n_africa_stints": len(afr),
                    "africa_regions": sorted({CREGION[c] for c, _, _ in afr}),
                    "africa_career": [{"territory": c, "label": CLABEL[c],
                                       "region": CREGION[c], "y0": y0, "y1": y1}
                                      for c, y0, y1 in afr]})
with open("data/africa/africa_persons.jsonl", "w") as f:
    for r in persons:
        f.write(json.dumps(r, ensure_ascii=False) + "\n")

say("=" * 64)
say("BRITISH AFRICA — first-round mobility network")
say("=" * 64)
say(f"territories (canonical): {len(set(CANON.values()))}   regions: {sorted(set(CREGION.values()))}")
say(f"officials with >=1 African appointment: {len(persons):,}")
say(f"  with >=2 different African territories (mobile-in-Africa): "
    f"{sum(1 for p in persons if len({s['territory'] for s in p['africa_career']})>=2):,}")

# ---------------------------------------------------------------- 2. network
def build_edges(pmin=None, pmax=None):
    """directed weighted edges from consecutive African appointments in a year window."""
    E = Counter()
    for p in persons:
        stints = sorted([s for s in p["africa_career"] if s["y0"] is not None],
                        key=lambda s: s["y0"])
        if pmin is not None:
            stints = [s for s in stints if pmin <= s["y0"] <= pmax]
        # collapse consecutive same-territory runs, then edge on change
        seq = [s["territory"] for s in stints]
        seq = [t for i, t in enumerate(seq) if i == 0 or t != seq[i-1]]
        for a, b in zip(seq, seq[1:]):
            E[(a, b)] += 1
    return E

E = build_edges()
G = nx.DiGraph()
for (a, b), w in E.items():
    G.add_edge(a, b, weight=w)
for c in set(CANON.values()):
    if c in [x for e in E for x in e]:
        G.nodes[c]["region"] = CREGION[c]
say(f"\nNETWORK: nodes {G.number_of_nodes()}  directed edges {G.number_of_edges()}  "
    f"transfers (total weight) {sum(E.values()):,}")
say(f"density {nx.density(G):.3f}   reciprocity {nx.reciprocity(G):.3f}")
Gu = G.to_undirected()
for u, v, dd in Gu.edges(data=True):   # symmetrise weights
    dd["weight"] = G.get_edge_data(u, v, {}).get("weight", 0) + G.get_edge_data(v, u, {}).get("weight", 0)
say(f"avg clustering (unweighted) {nx.average_clustering(Gu):.3f}   transitivity {nx.transitivity(Gu):.3f}")

# edgelist export for Gephi / Josef
with open("data/africa/africa_edges.csv", "w", newline="") as f:
    w = csv.writer(f); w.writerow(["source", "target", "weight", "source_label", "target_label",
                                   "source_region", "target_region"])
    for (a, b), wt in sorted(E.items(), key=lambda kv: -kv[1]):
        w.writerow([a, b, wt, CLABEL[a], CLABEL[b], CREGION[a], CREGION[b]])

say("\ntop 12 corridors (directed):")
for (a, b), wt in sorted(E.items(), key=lambda kv: -kv[1])[:12]:
    say(f"  {wt:4}  {CLABEL[a][:26]:26} -> {CLABEL[b]}")

# ---------------------------------------------------------------- 3. config null
def clus_recip(g):
    return nx.transitivity(g.to_undirected()), nx.reciprocity(g)
obs_t, obs_r = clus_recip(G)
din = [d for _, d in G.in_degree()]; dout = [d for _, d in G.out_degree()]
rng = np.random.default_rng(42)
null_t, null_r = [], []
for _ in range(500):
    try:
        rg = nx.directed_configuration_model(din, dout, seed=int(rng.integers(1e9)))
        rg = nx.DiGraph(rg); rg.remove_edges_from(nx.selfloop_edges(rg))
        t, r = clus_recip(rg); null_t.append(t); null_r.append(r)
    except Exception:
        pass
def z(obs, null):
    m, s = np.mean(null), np.std(null) or 1e-9
    return (obs - m) / s, m
zt, mt = z(obs_t, null_t); zr, mr = z(obs_r, null_r)
say(f"\nvs 500 fixed-degree config-model nulls:")
say(f"  transitivity  obs {obs_t:.3f}  null {mt:.3f}  z={zt:+.1f}")
say(f"  reciprocity   obs {obs_r:.3f}  null {mr:.3f}  z={zr:+.1f}")

# ---------------------------------------------------------------- 4. communities vs geography
region_groups = defaultdict(set)
for n in G.nodes():
    region_groups[CREGION[n]].add(n)
region_part = list(region_groups.values())
Q_region = nx.community.modularity(Gu, region_part, weight="weight")
louv = nx.community.louvain_communities(Gu, weight="weight", seed=1)
Q_louv = nx.community.modularity(Gu, louv, weight="weight")
say(f"\nCOMMUNITY STRUCTURE (weighted, undirected projection):")
say(f"  region partition ({len(region_part)} regions): modularity Q = {Q_region:.3f}")
say(f"  Louvain data-driven ({len(louv)} communities): modularity Q = {Q_louv:.3f}")
say(f"  -> geography captures {100*Q_region/Q_louv:.0f}% of the data-driven modularity"
    if Q_louv else "")
say("  Louvain communities (dominant region shown):")
for i, com in enumerate(sorted(louv, key=len, reverse=True)):
    reg = Counter(CREGION[n] for n in com).most_common(1)[0][0]
    names = ", ".join(sorted(CLABEL[n] for n in com)[:6])
    say(f"    C{i} [{reg}] n={len(com)}: {names}{' …' if len(com)>6 else ''}")

# ---------------------------------------------------------------- 5. tenure + temporal
# tenure in a territory = time until the next move to a DIFFERENT territory
# (Woldense's appointment-to-appointment spell), collapsing same-territory runs.
spells = []
for p in persons:
    stints = sorted([s for s in p["africa_career"] if s["y0"] is not None], key=lambda s: s["y0"])
    runs = []                                  # (territory, first_y0) collapsing repeats
    for s in stints:
        if not runs or runs[-1][0] != s["territory"]:
            runs.append((s["territory"], s["y0"]))
    for (t, y0), (t2, y1) in zip(runs, runs[1:]):
        if 0 <= y1 - y0 <= 40:
            spells.append(y1 - y0)             # moved on after this many years
say(f"\nTENURE spells (years in a territory before moving on, n={len(spells):,}): "
    f"median {st.median(spells):.1f}y  mean {st.mean(spells):.1f}y   "
    f"(Woldense's Selassie median ~3.2y)")

say(f"\nTEMPORAL split (the 1930 unification test):")
for lo, hi, tag in [(1800, 1929, "pre-1930"), (1930, 2000, "1930+")]:
    Ei = build_edges(lo, hi)
    Gi = nx.DiGraph()
    for (a, b), w in Ei.items(): Gi.add_edge(a, b, weight=w)
    if Gi.number_of_nodes() < 2:
        continue
    Gui = Gi.to_undirected()
    rp = [g & set(Gi.nodes()) for g in region_part]; rp = [g for g in rp if g]
    Qr = nx.community.modularity(Gui, rp, weight="weight") if Gi.number_of_edges() else float("nan")
    say(f"  {tag}: nodes {Gi.number_of_nodes()}  edges {Gi.number_of_edges()}  "
        f"transfers {sum(Ei.values()):,}  density {nx.density(Gi):.3f}  "
        f"recip {nx.reciprocity(Gi):.3f}  Q_region {Qr:.3f}")

# ---------------------------------------------------------------- figures
REGION_COLORS = {"West": "#e15759", "East": "#4e79a7", "Central": "#59a14f",
                 "Southern": "#f28e2b", "NE_condominium": "#b07aa1", "Horn": "#9c755f",
                 "IndianOcean": "#76b7b2", "SAtlantic": "#bab0ac"}
pos = nx.spring_layout(G, weight="weight", seed=7, k=0.6)
plt.figure(figsize=(13, 10))
ews = [G[u][v]["weight"] for u, v in G.edges()]
nx.draw_networkx_edges(G, pos, alpha=0.25, width=[0.3 + 2.5*w/max(ews) for w in ews],
                       edge_color="#888", arrowsize=6, connectionstyle="arc3,rad=0.08")
sizes = [60 + 12*(G.in_degree(n, weight="weight") + G.out_degree(n, weight="weight")) for n in G.nodes()]
nx.draw_networkx_nodes(G, pos, node_size=sizes,
                       node_color=[REGION_COLORS[CREGION[n]] for n in G.nodes()])
nx.draw_networkx_labels(G, pos, {n: CLABEL[n][:18] for n in G.nodes()}, font_size=6)
plt.title("British Africa — official mobility network (node=territory, colour=region)")
plt.axis("off"); plt.tight_layout(); plt.savefig("data/africa/figs/network.png", dpi=140); plt.close()

if spells:
    plt.figure(figsize=(7, 4))
    plt.hist([min(s, 20) for s in spells], bins=range(0, 22), color="#4e79a7", edgecolor="white")
    plt.xlabel("tenure spell (years)"); plt.ylabel("appointments")
    plt.title(f"Tenure in an African territory (median {st.median(spells):.1f}y)")
    plt.tight_layout(); plt.savefig("data/africa/figs/tenure.png", dpi=140); plt.close()

with open("data/africa/report.txt", "w") as f:
    f.write("\n".join(REPORT) + "\n")
say(f"\nwrote data/africa/africa_persons.jsonl ({len(persons):,}), africa_edges.csv, report.txt, figs/")

if __name__ == "__main__":
    pass
