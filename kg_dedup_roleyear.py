#!/usr/bin/env python3
"""Role+year+name person dedup (peerage / OCR / compound-surname variants).

Surfaced by the atlas "who held this role" panel (Jim): the same person appears
under a peerage title vs family name (RIPON/ROBINSON), a rank-polluted given name
(NICHOLSON Baron/Lord), an OCR'd surname, or a compound-surname rearrangement
(GRANT-BROWN/BROWN). The (surname, given) blocking of the main dedup splits these.

Method (Jim's spec): block on SAME role + SAME colony + SAME year_start; merge when
the names "mostly match" after stripping ranks/honorifics (OCR-tolerant token
subset, >=2 shared tokens incl. >=1 distinctive). Birth-year conflict (>2) vetoes.
Every candidate cluster was hand-reviewed; EXCLUDE holds the few adjudicated as
distinct people. Composes onto the existing merge map; apply with
kg_dedup_stage3_apply.py.  Env: COL_KG_OUT selects the corpus.
"""
import json, re, sys
from collections import defaultdict
from rapidfuzz.distance import Levenshtein
from col_match.kg.paths import KG_OUT
lev = Levenshtein.distance

RANK={"earl","marquess","marquis","viscount","viscountess","baron","baroness","baronet",
 "bart","lord","lady","duke","duchess","count","countess","of","the","sir","dame","rt",
 "right","hon","honorary","honourable","formerly","first","second","third",
 "rai","bahadur","sahib","sahibzada","nawabzada","kunwar","pandit","babu","mirza",
 "maulvi","munshi","khan","nawab","begum","diwan","dewan","qanungo","kanungo","raja",
 "rajah","sri","srijat","brod","mst","mr","mrs","miss","esq","kt","cie","csi","maung"}
# clusters hand-reviewed and rejected as DISTINCT people (not merges)
EXCLUDE={
 # CO
 "kgp_col1906-p665b9","kgp_col1879-p397b20",        # ELLIOTT John (BG vs Burma military)
 "kgp_col1883-p366b3","kgp_col1867-p216b8",         # CALDWELL Wm James vs James
 "kgp_col1886-p422b7","kgp_col1905-p626b17",        # CLARKE Marshall James vs James
 "kgp_col1910-p772b23","kgp_col1908-p711b8",        # STUART/PITTS (Newfoundland vs SA)
 "kgp_col1957-p285b17","kgp_col1964-p220b6",        # AMOROSO-CENTENO A.E.B. vs M.
 # IOL
 "kgp_iol1945-c1691715","kgp_iol1931-c4478773","kgp_iol1937-c4498420","kgp_iol1927-c4087788", # Muhammad Fakhar/Ibrahim/Mian
 "kgp_iol1947-c1879726","kgp_iol1938-c2238012","kgp_iol1931-c4115577","kgp_iol1947-c1492440", # PYU/KYIN Maung
 "kgp_iol1898-c2531693","kgp_iol1908-c3240153","kgp_iol1894_supp-c2557200",                    # MELHUISH/WILLIAMS
 "kgp_iol1908-c3017979","kgp_iol1947-c1408121",                                                # JOHNSON/JOHNSTON
 "kgp_iol1947-c2129463","kgp_iol1947-c1770988",                                                # Burmese SOE/NYUN
}
def toks(p):
    s=((p.get("surname") or "")+" "+(p.get("given_names") or "")).lower()
    return [t for t in re.split(r"[^a-z0-9]+",s) if t and t not in RANK and len(t)>1]
def tin(t,S): return any(t==u or (len(t)>=4 and len(u)>=4 and lev(t,u)<=1) for u in S)
def match(A,B):
    TA,TB=set(toks(A)),set(toks(B))
    if len(TA)<2 or len(TB)<2: return False
    small,big=(TA,TB) if len(TA)<=len(TB) else (TB,TA)
    shared=[t for t in small if tin(t,big)]
    return len(shared)>=2 and len(shared)/len(small)>=0.75 and any(len(t)>=4 for t in shared)
def bconf(A,B):
    a,b=A.get("birth_year"),B.get("birth_year"); return a and b and abs(a-b)>2

persons={p["person_id"]:p for p in (json.loads(l) for l in open(KG_OUT/"graph_stage3/persons.jsonl"))}
nattest={pid:(p.get("n_attestations") or 0) for pid,p in persons.items()}
blocks=defaultdict(set)
for l in open(KG_OUT/"graph_stage3/career_facts.jsonl"):
    d=json.loads(l); rl=d.get("role_label"); col=d.get("colony_qid"); ys=d.get("year_start")
    if rl and col and ys: blocks[(rl,col,ys)].add(d["person_id"])

parent={}
def find(x):
    parent.setdefault(x,x)
    while parent[x]!=x: parent[x]=parent[parent[x]]; x=parent[x]
    return x
new_pairs=0
for key,pids in blocks.items():
    pl=[p for p in pids if p in persons]
    if len(pl)<2: continue
    for i in range(len(pl)):
        for j in range(i+1,len(pl)):
            a,b=pl[i],pl[j]
            if find(a)==find(b): continue
            A,B=persons[a],persons[b]
            if bconf(A,B) or not match(A,B): continue
            parent[find(a)]=find(b); new_pairs+=1
clusters=defaultdict(list)
for p in list(parent): clusters[find(p)].append(p)
clusters={r:m for r,m in clusters.items() if len(m)>1}
# drop hand-rejected clusters (any member in EXCLUDE)
kept=[m for m in clusters.values() if not any(x in EXCLUDE for x in m)]
dropped=len(clusters)-len(kept)

# compose onto existing crossform map
mapf=KG_OUT/"dedup_stage3_merge_map.crossform.jsonl"
uf={}
def f2(x):
    uf.setdefault(x,x)
    while uf[x]!=x: uf[x]=uf[uf[x]]; x=uf[x]
    return x
def union(a,b):
    ra,rb=f2(a),f2(b)
    if ra!=rb: uf[ra]=rb
existing=[json.loads(l) for l in open(mapf)]
for r in existing: union(r["person_id"], r["canonical_person_id"])
for m in kept:
    canon=max(m, key=lambda p:nattest.get(p,0))   # most-attested = canonical
    for p in m:
        if p!=canon: union(p,canon)
# emit full map: every pid that appears anywhere -> its root
allpids=set()
for r in existing: allpids.add(r["person_id"]); allpids.add(r["canonical_person_id"])
for m in kept: allpids.update(m)
out=KG_OUT/"dedup_stage3_merge_map.roleyear.jsonl"
rows=[]
for p in sorted(allpids):
    c=f2(p)
    if c!=p: rows.append({"person_id":p,"canonical_person_id":c})
with open(out,"w") as fh:
    for r in rows: fh.write(json.dumps(r)+"\n")
print(f"{KG_OUT}: new_pairs={new_pairs} clusters={len(clusters)} kept={len(kept)} dropped(excluded)={dropped}")
print(f"  records merged by this pass: {sum(len(m) for m in kept)} | composed map rows: {len(rows)} -> {out.name}")
