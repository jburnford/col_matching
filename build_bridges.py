#!/usr/bin/env python3
"""Cross-corpus BRIDGE matcher: officials who served in BOTH the Colonial Office
List (CO) and the India Office List (IOL) -- the "two services, one empire" careers
(e.g. Evelyn Baring, Bernard Bourdillon, E. D. W. Greig).

Unlike the within-corpus dedup, the two careers DON'T share places (CO = colonies,
IOL = India), so the join leans on name + a corroborating signal:
  - shared dated honour (near-unique: a specific decoration in a specific year)
  - same birth year + a distinctive / full given name
  - exact full given-name match

Emits docs/data/bridges.json for the atlas "Two Services" view. This is a DISCOVERY
layer (confidence-tiered candidates for exploration), NOT a 0-FP KG merge -- common
name + birth-only matches are flagged 'C'.

  python3 build_bridges.py
"""
from __future__ import annotations
import json, re
from collections import defaultdict
from rapidfuzz.distance import Levenshtein

CO = "data/kg/graph_stage3"
IO = "data/iol/graph_stage3"
OUT = "docs/data/bridges.json"

NK = re.compile(r"[^a-z]")
def nk(s): return NK.sub("", (s or "").lower())
def load(p): return [json.loads(l) for l in open(p)]
def gtoks(g): return [t for t in re.split(r"[ .]+", g or "") if t]
def full_tokens(g): return [t for t in gtoks(g) if len(t) >= 2]

def gcompat(a, b):
    ta, tb = gtoks(a), gtoks(b)
    if not ta or not tb: return False
    for x, y in zip(ta, tb):
        if len(x) == 1 or len(y) == 1:
            if x[0].upper() != y[0].upper(): return False
        elif x.lower() != y.lower():
            if not (min(len(x), len(y)) >= 5 and Levenshtein.distance(x.lower(), y.lower()) <= 1):
                return False
    return True

def sn_ok(a, b): return a == b or (min(len(a), len(b)) >= 4 and Levenshtein.distance(a, b) <= 1)

def fullest(a, b):
    """the more informative given-name form (more full tokens, then longer)."""
    ka = (len(full_tokens(a)), len(a or "")); kb = (len(full_tokens(b)), len(b or ""))
    return a if ka >= kb else b

# common surnames where a birth-year-only match is weak (namesake risk)
COMMON_SN = {"smith","brown","jones","williams","taylor","anderson","wilson","thomson",
             "thompson","walker","white","hall","clark","clarke","wright","robinson",
             "scott","young","king","baker","martin","james","moore","campbell","stewart",
             "morris","cooper","murray","mitchell","ross","gray","grey","watson","davies"}

def honset(dirn):
    h = defaultdict(set)
    try:
        for l in open(f"{dirn}/honour_edges.jsonl"):
            r = json.loads(l)
            if r.get("year") and r.get("honour_id"):
                h[r["person_id"]].add((r["honour_id"], r["year"]))
    except FileNotFoundError:
        pass
    return h

co = [r for r in load(f"{CO}/persons.jsonl") if r.get("surname") and r.get("given_names")]
io = [r for r in load(f"{IO}/persons.jsonl") if r.get("surname") and r.get("given_names")]
coh, ioh = honset(CO), honset(IO)
# careers.json tells us who actually has mapped stints (worth showing on the map)
careers = json.load(open(OUT.replace("bridges", "careers")))["persons"]

io_by_p3 = defaultdict(list)
for r in io:
    s = nk(r["surname"])
    if s: io_by_p3[s[:3]].append(r)

def tier(c, o):
    cb, ob = c.get("birth_year"), o.get("birth_year")
    same_birth = bool(cb and ob and cb == ob)
    birth_conflict = bool(cb and ob and cb != ob)
    shared_h = coh.get(c["person_id"], set()) & ioh.get(o["person_id"], set())
    cft, oft = full_tokens(c["given_names"]), full_tokens(o["given_names"])
    exact_full = (len(cft) >= 2 and len(oft) >= 2
                  and nk(c["given_names"]) == nk(o["given_names"]))
    distinctive = max(len(cft), len(oft)) >= 3        # 3+ full given names = rare
    common = nk(c["surname"]) in COMMON_SN
    if shared_h: return "A", f"shared honour {sorted(shared_h)[0]}"
    if same_birth and (distinctive or exact_full) and not common:
        return "A", f"b.{cb} + full name"
    if same_birth and not common: return "B", f"b.{cb}"
    if exact_full and not birth_conflict and not common: return "B", "exact full name"
    if same_birth and common: return "C", f"b.{cb} (common surname)"
    if exact_full and not birth_conflict: return "C", "exact full name (common)"
    return None, None

bridges, seen = [], set()
for c in co:
    sc = nk(c["surname"])
    for o in io_by_p3.get(sc[:3], []):
        if not sn_ok(sc, nk(o["surname"])): continue
        if not gcompat(c["given_names"], o["given_names"]): continue
        key = (c["person_id"], o["person_id"])
        if key in seen: continue
        t, ev = tier(c, o)
        if not t: continue
        seen.add(key)
        cc, oc = careers.get(c["person_id"]), careers.get(o["person_id"])
        bridges.append({
            "co": c["person_id"], "io": o["person_id"],
            "name": fullest(c["given_names"], o["given_names"]),
            "surname": c["surname"] if len(c["surname"]) >= len(o["surname"]) else o["surname"],
            "birth": c.get("birth_year") or o.get("birth_year"),
            "conf": t, "ev": ev,
            "co_stints": len(cc["st"]) if cc else 0,
            "io_stints": len(oc["st"]) if oc else 0,
            "co_qid": c.get("wikidata_qid"),
        })

# flag ambiguous: a CO (or IOL) person matched to >1 of the other corpus
from collections import Counter
co_ct, io_ct = Counter(b["co"] for b in bridges), Counter(b["io"] for b in bridges)
for b in bridges:
    b["ambiguous"] = co_ct[b["co"]] > 1 or io_ct[b["io"]] > 1

# rank: confidence, then mapped (both have stints), then total career richness
rank = {"A": 0, "B": 1, "C": 2}
bridges.sort(key=lambda b: (rank[b["conf"]], -(b["co_stints"] + b["io_stints"]),
                            b["surname"], b["name"]))

from collections import Counter as C2
tc = C2(b["conf"] for b in bridges)
mapped = sum(1 for b in bridges if b["co_stints"] and b["io_stints"])
amb = sum(1 for b in bridges if b["ambiguous"])
json.dump({"bridges": bridges, "counts": {**tc, "total": len(bridges),
           "mapped_both": mapped, "ambiguous": amb}},
          open(OUT, "w"), ensure_ascii=False)
print(f"bridges: {len(bridges)}  (A={tc.get('A',0)} B={tc.get('B',0)} C={tc.get('C',0)})"
      f"  mapped-both={mapped}  ambiguous={amb}")
print(f"wrote -> {OUT}")
print("\ntop 20 (A/B, mapped both services):")
for b in [x for x in bridges if x["co_stints"] and x["io_stints"]][:20]:
    print(f"  [{b['conf']}] {b['surname']}, {b['name']:<28} b.{b['birth'] or '-'}  "
          f"CO {b['co_stints']}st / IO {b['io_stints']}st  ({b['ev']})")
