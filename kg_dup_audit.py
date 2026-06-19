#!/usr/bin/env python3
"""Audit data/kg/persons.jsonl for same-individual duplicates the conservative
cross-edition clustering left behind.

Signals (the clustering used only name+birth): given-name fuzzy match PLUS the
career signature from the canonical text — the multiset of years and the
content tokens (places/positions/year-ranges). Two records are the same person
when birth agrees (+-1) and EITHER the names are OCR-variants OR the careers
near-coincide. A career match also catches OCR *surname* variance that a
surname-blocked pass never compares.
"""
from __future__ import annotations
import json, re, glob
from collections import defaultdict
from difflib import SequenceMatcher

YEAR = re.compile(r"\b1[789]\d\d\b")
SUR = re.compile(r"[^A-Z]")
STOP = set("the of and to in a at as for on b ed sch coll univ b a m a hon sir".split())

def load():
    P = [json.loads(l) for l in open("data/kg/persons.jsonl")]
    bio = {}
    for f in glob.glob("data/kg/bios/*.jsonl"):
        for l in open(f):
            b = json.loads(l); bio[b["bio_id"]] = b["raw_text"]
    for p in P:
        t = bio.get(p["canonical_bio_id"], "")
        p["_years"] = set(int(y) for y in YEAR.findall(t))
        # content tokens after the headword (career places/positions), de-named
        body = t.split(".", 1)[1] if "." in t else t
        p["_toks"] = set(w for w in re.findall(r"[a-z]{4,}", body.lower()) if w not in STOP)
        p["_text"] = re.sub(r"\s+", " ", body.lower())[:600]
    return P

def sk(p): return SUR.sub("", (p.get("surname") or "").upper())
def gspell(p): return " ".join(t for t in re.findall(r"[a-z]+", (p.get("given_names") or "").lower()) if len(t) > 1)
def gsim(a, b):
    A, B = gspell(a), gspell(b)
    return SequenceMatcher(None, A, B).ratio() if A and B else 0.0
def jac(a, b):
    if not a or not b: return 0.0
    return len(a & b) / len(a | b)
def career_match(a, b):
    yj = jac(a["_years"], b["_years"]); tj = jac(a["_toks"], b["_toks"])
    if yj >= 0.6 and tj >= 0.5: return True
    if len(a["_years"] & b["_years"]) >= 3 and SequenceMatcher(None, a["_text"], b["_text"]).ratio() >= 0.55:
        return True
    return False

class UF:
    def __init__(s, n): s.p = list(range(n))
    def f(s, x):
        while s.p[x] != x: s.p[x] = s.p[s.p[x]]; x = s.p[x]
        return x
    def u(s, a, b): s.p[s.f(a)] = s.f(b)

def main():
    P = load()
    uf = UF(len(P))
    wb = [i for i, p in enumerate(P) if p.get("birth_year")]
    # ---- pass 1: same surname-key, birth +-1, name-variant OR career match
    blk = defaultdict(list)
    for i in wb: blk[sk(P[i])].append(i)
    p1 = 0
    for s, ids in blk.items():
        for a in range(len(ids)):
            for b in range(a + 1, len(ids)):
                x, y = P[ids[a]], P[ids[b]]
                if abs(x["birth_year"] - y["birth_year"]) <= 1 and (gsim(x, y) >= 0.82 or career_match(x, y)):
                    if uf.f(ids[a]) != uf.f(ids[b]): uf.u(ids[a], ids[b]); p1 += 1
    # ---- pass 2: cross-surname (OCR surname variance) — same birth, strong career match
    bbirth = defaultdict(list)
    for i in wb: bbirth[P[i]["birth_year"]].append(i)
    p2 = 0
    for y, ids in bbirth.items():
        for a in range(len(ids)):
            xa = P[ids[a]]
            for b in range(a + 1, len(ids)):
                xb = P[ids[b]]
                if sk(xa) == sk(xb): continue  # pass 1 territory
                if len(xa["_years"] & xb["_years"]) >= 3 and career_match(xa, xb) and gsim(xa, xb) >= 0.6:
                    if uf.f(ids[a]) != uf.f(ids[b]): uf.u(ids[a], ids[b]); p2 += 1
    # ---- pass 3: no-birth-year persons — career+name signature, no birth anchor.
    # Gate by surname-key + >=3 shared career years (inverted index) to bound work.
    nb = [i for i, p in enumerate(P) if not p.get("birth_year") and len(P[i]["_years"]) >= 3]
    sur_year = defaultdict(lambda: defaultdict(list))
    for i in nb:
        for y in P[i]["_years"]: sur_year[sk(P[i])][y].append(i)
    p3 = 0
    seen = set()
    for s, ymap in sur_year.items():
        cand = defaultdict(int)
        cocount = defaultdict(int)
        for y, ids in ymap.items():
            for a in range(len(ids)):
                for b in range(a + 1, len(ids)):
                    cocount[(ids[a], ids[b])] += 1
        for (i, j), c in cocount.items():
            if c >= 3 and (i, j) not in seen:
                seen.add((i, j))
                if gsim(P[i], P[j]) >= 0.80 and career_match(P[i], P[j]):
                    if uf.f(i) != uf.f(j): uf.u(i, j); p3 += 1
    print(f"pass3 no-birth merges {p3:,}")

    grp = defaultdict(list)
    for i in list(wb) + nb: grp[uf.f(i)].append(i)
    dups = [g for g in grp.values() if len(g) > 1]
    excess = sum(len(g) - 1 for g in dups)
    print(f"persons total {len(P):,} | with birth_year {len(wb):,}")
    print(f"pass1 same-surname merges {p1:,} | pass2 cross-surname(OCR) merges {p2:,}")
    print(f"DUPLICATE GROUPS {len(dups):,} covering {sum(len(g) for g in dups):,} records "
          f"-> {excess:,} excess records ({100*excess/len(P):.1f}% of corpus)")
    print("\nlargest duplicate clusters:")
    for g in sorted(dups, key=lambda g: -len(g))[:12]:
        p0 = P[g[0]]
        names = [P[i].get("given_names") for i in g]
        print(f"  {sk(p0)} b.{p0['birth_year']} x{len(g)}: {names}")
    # cross-surname examples specifically
    xs = [g for g in dups if len({sk(P[i]) for i in g}) > 1]
    print(f"\ncross-surname (OCR surname) clusters: {len(xs):,}")
    for g in xs[:8]:
        print(f"  b.{P[g[0]]['birth_year']}: " + " | ".join(f"{P[i].get('surname')},{P[i].get('given_names')}" for i in g))

if __name__ == "__main__":
    main()
