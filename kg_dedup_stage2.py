#!/usr/bin/env python3
"""Stage 2 dedup: collapse the text-chained persons (persons.deduped.jsonl, ~39k)
to ~30k by merging chains that are the SAME person but text-chaining couldn't
link — OCR surname/name variants (HAGGART/AGGART) and 1948-reformat chain breaks.

Two merge sources, union-find over the ~39k chains:
  L) the ported June LLM ledger (fingerprints -> bio -> chain)
  D) deterministic: birth +-1 + name-OCR-variant OR career match; cross-surname
     OCR (strong career match); no-birth career match.  Reuses kg_dup_audit logic
     but on the RICHEST canonical per chain (stronger signatures, 39k not 90k).

  python3 kg_dedup_stage2.py [--write data/kg/persons.deduped2.jsonl]
"""
from __future__ import annotations
import argparse, json, glob, re
from collections import defaultdict
from difflib import SequenceMatcher
from rapidfuzz import fuzz
from col_match.services.compile import _names_compatible  # calibrated 0-FP name gate

ap = argparse.ArgumentParser()
ap.add_argument("--write", default="")
ap.add_argument("--min-score", type=float, default=70.0)
args = ap.parse_args()

YEAR = re.compile(r"\b1[789]\d\d\b")
SUR = re.compile(r"[^A-Z]")
STOP = set("the of and to in a at as for on b ed sch coll univ hon sir served".split())

def edition(s):
    m = re.match(r"([a-z]+\d{4})", s); return m.group(1) if m else s.split("-")[0]
def sk(s): return SUR.sub("", (s or "").upper())
def gspell(s): return " ".join(t for t in re.findall(r"[a-z]+", (s or "").lower()) if len(t) > 1)
def gsim(a, b):
    A, B = gspell(a), gspell(b); return SequenceMatcher(None, A, B).ratio() if A and B else 0.0
def jac(a, b): return len(a & b) / len(a | b) if a and b else 0.0

# bios cache: bio_id -> raw_text, and per-edition list for ledger matching
bio_txt = {}
by_ed = defaultdict(list)
for f in glob.glob("data/kg/bios/*.jsonl"):
    for l in open(f):
        b = json.loads(l); bio_txt[b["bio_id"]] = b["raw_text"]
        b["_years"] = set(int(y) for y in YEAR.findall(b["raw_text"]))
        by_ed[edition(b["bio_id"])].append(b)

# deduped chains (the stage-1 persons)
P = [json.loads(l) for l in open("data/kg/persons.deduped.jsonl")]
bio2idx = {}
for i, p in enumerate(P):
    t = bio_txt.get(p["canonical_bio_id"], "")
    body = t.split(".", 1)[1] if "." in t else t
    p["_years"] = set(int(y) for y in YEAR.findall(t))
    p["_toks"] = set(w for w in re.findall(r"[a-z]{4,}", body.lower()) if w not in STOP)
    p["_text"] = re.sub(r"\s+", " ", body.lower())[:600]
    for bid in p["attestation_bio_ids"]:
        bio2idx[bid] = i

def career_match(a, b):
    if jac(a["_years"], b["_years"]) >= 0.6 and jac(a["_toks"], b["_toks"]) >= 0.5: return True
    if len(a["_years"] & b["_years"]) >= 3 and SequenceMatcher(None, a["_text"], b["_text"]).ratio() >= 0.55: return True
    return False

class UF:
    def __init__(s, n): s.p = list(range(n))
    def f(s, x):
        while s.p[x] != x: s.p[x] = s.p[s.p[x]]; x = s.p[x]
        return x
    def u(s, a, b): s.p[s.f(a)] = s.f(b)
uf = UF(len(P))

# ---- source L: ported LLM ledger ----
def fp_score(fpr, b):
    s = fuzz.token_set_ratio(fpr.get("surname") or "", b.get("surname") or "") * 0.35
    s += fuzz.token_set_ratio(fpr.get("given") or "", b.get("given_names") or "") * 0.25
    if fpr.get("birth") and b.get("birth_year"): s += 15 if abs(fpr["birth"] - b["birth_year"]) <= 1 else 0
    elif not fpr.get("birth") and not b.get("birth_year"): s += 5
    fy = {e[0] for e in fpr.get("events", []) if e and e[0]}
    if fy: s += 25 * (len(fy & b["_years"]) / len(fy))
    return s
def best_bio(fpr):
    ed = fpr.get("edition") or edition(fpr.get("version_id", "")); best, bs = None, -1
    for b in by_ed.get(ed, []):
        sc = fp_score(fpr, b)
        if sc > bs: best, bs = b, sc
    return (best, bs)
nL = 0
for g in (json.loads(l) for l in open("data/services/dedup/llm_merges_fingerprinted.jsonl")):
    idxs = set()
    for fpr in g["fingerprints"]:
        b, sc = best_bio(fpr)
        # guard fingerprint mismatch: the mapped bio's GIVEN name must be
        # compatible with the fingerprint's (given survives OCR better than
        # surname; rejects wrong-bio maps that scored >=min on birth/year alone)
        if (b and sc >= args.min_score and b["bio_id"] in bio2idx
                and _names_compatible(fpr.get("given"), b.get("given_names"))):
            idxs.add(bio2idx[b["bio_id"]])
    idxs = list(idxs)
    for k in range(1, len(idxs)):
        if uf.f(idxs[0]) != uf.f(idxs[k]): uf.u(idxs[0], idxs[k]); nL += 1

# ---- source D: deterministic, on the 39k chains ----
wb = [i for i, p in enumerate(P) if p.get("birth_year")]
blk = defaultdict(list)
for i in wb: blk[sk(P[i].get("surname"))].append(i)
nD = 0
for s, ids in blk.items():
    for a in range(len(ids)):
        for b in range(a + 1, len(ids)):
            x, y = P[ids[a]], P[ids[b]]
            # REQUIRE name compatibility (handles initials<->full, rejects
            # different given names) + birth + (OCR-name-variant OR career)
            if (abs(x["birth_year"] - y["birth_year"]) <= 1
                    and _names_compatible(x.get("given_names"), y.get("given_names"))
                    and (gsim(x.get("given_names"), y.get("given_names")) >= 0.82 or career_match(x, y))):
                if uf.f(ids[a]) != uf.f(ids[b]): uf.u(ids[a], ids[b]); nD += 1
# cross-surname OCR (same birth, strong career + some name sim)
bb = defaultdict(list)
for i in wb: bb[P[i]["birth_year"]].append(i)
nX = 0
for y, ids in bb.items():
    for a in range(len(ids)):
        for b in range(a + 1, len(ids)):
            x, z = P[ids[a]], P[ids[b]]
            if sk(x.get("surname")) == sk(z.get("surname")): continue
            # cross-surname OCR: surname is unreliable, so require a DISTINCTIVE
            # SPELLED given-name match (gsim>=0.8 needs real spelled tokens, which
            # blocks initials-only coincidences) PLUS name-compat + strong career.
            if (gsim(x.get("given_names"), z.get("given_names")) >= 0.80
                    and _names_compatible(x.get("given_names"), z.get("given_names"))
                    and len(x["_years"] & z["_years"]) >= 3 and career_match(x, z)):
                if uf.f(ids[a]) != uf.f(ids[b]): uf.u(ids[a], ids[b]); nX += 1

grp = defaultdict(list)
for i in range(len(P)): grp[uf.f(i)].append(i)
final = list(grp.values())
print(f"stage-1 chains {len(P):,}")
print(f"  ledger merges {nL} | det same-surname {nD} | cross-surname OCR {nX}")
print(f"-> stage-2 persons {len(final):,}  ({len(P)-len(final):,} further collapsed)")
xs = sorted((g for g in final if len(g) > 1), key=lambda g: -len(g))
print("sample stage-2 merges (chains joined):")
for g in xs[:10]:
    print("  " + " | ".join(f"{P[i].get('surname')},{P[i].get('given_names')} b.{P[i].get('birth_year')}" for i in g[:4]))

if args.write:
    def rich(p): return len(p["_years"]) * 100 + len(bio_txt.get(p["canonical_bio_id"], ""))
    with open(args.write, "w") as fh:
        for g in final:
            canon = max((P[i] for i in g), key=rich)
            bios = [bid for i in g for bid in P[i]["attestation_bio_ids"]]
            eds = sorted({e for i in g for e in P[i]["editions"]})
            fh.write(json.dumps({
                "person_id": canon["person_id"], "surname": canon.get("surname"),
                "given_names": canon.get("given_names"),
                "birth_year": next((P[i].get("birth_year") for i in g if P[i].get("birth_year")), None),
                "editions": eds, "canonical_bio_id": canon["canonical_bio_id"],
                "canonical_edition": canon["canonical_edition"],
                "n_attestations": len(bios), "attestation_bio_ids": bios,
                "merged_chains": len(g),
            }, ensure_ascii=False) + "\n")
    print(f"wrote -> {args.write}")
