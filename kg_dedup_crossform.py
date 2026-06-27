#!/usr/bin/env python3
"""Stage-3b CROSS-FORM person-dedup: catch same-person nodes the surname+given-name
blocking split apart (initials-vs-full like MACKAY I.V.G. / Iaan Vandin Gordon;
OCR token variants like PREVOST ...DE TEISSIER / ...DE TRISSIER).

The original `kg_dedup_stage3_candidates.py` blocks on (surname, FULL given_names),
so two records of the same person whose given-name *form* differs never land in the
same block and are never compared. This pass blocks on SURNAME ONLY and lets a
STRONG SHARED CAREER EVENT drive the merge (Jim: "two nodes with the matching
events"). The shared exact appointment (job@place@year) is what makes surname-only
blocking safe -- two distinct same-surname namesakes virtually never share a specific
appointment in the same place and year.

Operates at the CURRENT-CANONICAL level: applies the existing merge map first, then
looks for cross-canonical merges among surname-mates. Emits NEW union edges only
(pairs not already merged). MEASURE-ONLY by default; pass --emit-map to compose an
augmented merge map.

  python3 kg_dedup_crossform.py [--sample 25] [--emit-map data/kg/dedup_stage3_merge_map.crossform.jsonl]

Outputs:
  data/kg/dedup_crossform_edges.jsonl   one row per NEW merge pair + evidence
  stdout                                counts + readable sample (eyeball precision)
"""
from __future__ import annotations
import argparse, json, re
from collections import defaultdict
from rapidfuzz.distance import Levenshtein
from col_match.services.compile import _names_compatible, _canon_token

ap = argparse.ArgumentParser()
ap.add_argument("--corpus", default="data/kg/llm_struct_corpus.reviewed.jsonl")
ap.add_argument("--grounding", default="data/kg/places_grounding.jsonl")
ap.add_argument("--map", default="data/kg/dedup_stage3_merge_map.jsonl")
ap.add_argument("--out", default="data/kg/dedup_crossform_edges.jsonl")
ap.add_argument("--emit-map", default=None,
                help="if set, write existing+new merges composed into one map here")
ap.add_argument("--sample", type=int, default=25)
args = ap.parse_args()

GAP_MAX = 11      # temporal guard: max year gap between two careers to still be one person
SPAN_MAX = 55     # ... and max merged career span (matches kg-posting-dedup guard)

NK = re.compile(r"[^a-z]")
def nk(s): return NK.sub("", (s or "").lower())
_PSTEM = re.compile(r"[^a-z]")
def posstem(p): return _PSTEM.sub("", (p or "").lower())[:14]

# generic high-frequency positions -- a shared (generic, place) is NOT identifying on
# its own; only conclusive with a matching YEAR or inside a multi-posting chain.
GENERIC_POS = {
    "assistantcommi","assistantengin","executiveengin","assistantmagis","deputycommissi",
    "assistantsuper","officiating","confirmed","assistant","engineer","clerk","magistrate",
    "joinedtheservi","probationer","extraassistant","subdivisional","actingmagistr",
    "superintenden","districtsuperi","executiveengi","assistantmagi","governmentserv",
    "govtservice","militaryservic","onmilitaryser","cadet","actinggovernor",
}

# place surface -> grounded qid
gqid = {}
for l in open(args.grounding):
    r = json.loads(l)
    if r.get("qid"): gqid[r["place"]] = r["qid"]

def feats(rec):
    qids, years = set(), []
    postings_yr, postings = set(), set()
    for e in rec.get("events") or []:
        pl = e.get("place"); q = gqid.get(pl) if pl else None
        ps = posstem(e.get("position") or e.get("position_norm"))
        if q: qids.add(q)
        ys, ye = e.get("year_start"), e.get("year_end")
        for y in (ys, ye):
            if isinstance(y, int): years.append(y)
        if ps and q:
            postings.add((ps, q))
            if isinstance(ys, int): postings_yr.add((ps, q, ys))
    return qids, years, postings, postings_yr

# ---- union-find over existing merges ----
parent = {}
def find(x):
    parent.setdefault(x, x)
    while parent[x] != x:
        parent[x] = parent[parent[x]]; x = parent[x]
    return x
def union(a, b):
    ra, rb = find(a), find(b)
    if ra != rb: parent[ra] = rb
    return ra != rb

existing = [json.loads(l) for l in open(args.map)]
for r in existing:
    union(r["person_id"], r["canonical_person_id"])

# ---- read spine, aggregate per current-canonical ----
recs = [json.loads(l) for l in open(args.corpus)]
for r in recs: find(r["person_id"])      # ensure every pid is a node

# canonical -> aggregated features
agg = defaultdict(lambda: {"qids": set(), "years": [], "postings": set(),
                           "postings_yr": set(), "givens": set(), "births": set(),
                           "surname": None, "pids": []})
by_surname = defaultdict(set)             # surname_key -> {canonical}
for r in recs:
    c = find(r["person_id"])
    q, yy, p, py = feats(r)
    a = agg[c]
    a["qids"] |= q; a["years"] += yy; a["postings"] |= p; a["postings_yr"] |= py
    a["pids"].append(r["person_id"])
    g = r.get("given_names")
    if g: a["givens"].add(g)
    if r.get("birth_year"): a["births"].add(r["birth_year"])
    sk = nk(r.get("surname"))
    if sk:
        a["surname"] = sk
        by_surname[sk].add(c)

def span(a):
    return (min(a["years"]), max(a["years"])) if a["years"] else (None, None)

def gap_between(a, b):
    """year gap between the two canonicals' career spans (>0 disjoint, <=0 overlap);
    None if either lacks years."""
    sa, sb = span(a), span(b)
    if sa[0] is None or sb[0] is None: return None
    return max(sa[0], sb[0]) - min(sa[1], sb[1])

def merged_span(a, b):
    yy = a["years"] + b["years"]
    return (max(yy) - min(yy)) if yy else 0

def ocr_token_eq(x, y):
    """tokens equal after canon, OR a single-char OCR slip on a long-ish token."""
    cx, cy = _canon_token(x), _canon_token(y)
    if cx == cy: return True
    if min(len(cx), len(cy)) >= 5 and Levenshtein.distance(cx, cy) <= 1:
        return True
    return False

def name_pair_ok(ga, gb):
    """exists a compatible given-name form across the two canonicals.
    initials match full names (via _names_compatible); long full tokens may differ by
    a single OCR char (TEISSIER/TRISSIER)."""
    for a in ga:
        for b in gb:
            if _names_compatible(a, b): return True
            # OCR-tolerant token alignment (same #tokens, each token compatible)
            ta = [t for t in re.split(r"[ .]+", a) if t]
            tb = [t for t in re.split(r"[ .]+", b) if t]
            if ta and tb and len(ta) == len(tb):
                ok = True
                for x, y in zip(ta, tb):
                    if len(x) == 1 or len(y) == 1:
                        if x[0].upper() != y[0].upper(): ok = False; break
                    elif not ocr_token_eq(x, y): ok = False; break
                if ok: return True
    return False

def strong_shared_event(a, b):
    """the safety gate: a specific shared appointment that two namesakes wouldn't share."""
    sp_yr = a["postings_yr"] & b["postings_yr"]
    sp = a["postings"] & b["postings"]
    specific = {(ps, q) for (ps, q) in sp if ps not in GENERIC_POS}
    # specific exact appointment (job@place@year)
    specific_yr = {(ps, q, y) for (ps, q, y) in sp_yr if ps not in GENERIC_POS}
    if specific_yr: return ("appt_yr", sorted(f"{ps}@{q}:{y}" for ps, q, y in specific_yr))
    if len(sp) >= 2 and specific: return ("chain2", sorted(f"{ps}@{q}" for ps, q in sp))
    g = gap_between(a, b)
    if specific and (g is None or g <= 5):
        return ("specific_contig", sorted(f"{ps}@{q}" for ps, q in specific))
    # generic posting but with a shared exact YEAR is still fairly strong (e.g. asst comm 1912)
    if sp_yr and (g is None or g <= 2):
        return ("genericyr_contig", sorted(f"{ps}@{q}:{y}" for ps, q, y in sp_yr))
    return (None, [])

# ---- find cross-canonical merges within each surname block ----
new_edges = []
for sk, canons in by_surname.items():
    canons = sorted(canons)
    n = len(canons)
    if n < 2: continue
    for i in range(n):
        ai = agg[canons[i]]
        for j in range(i + 1, n):
            bj = agg[canons[j]]
            if find(canons[i]) == find(canons[j]): continue      # already merged
            if not (ai["qids"] & bj["qids"]): continue           # prefilter: must share a place
            if not name_pair_ok(ai["givens"], bj["givens"]): continue
            kind, ev = strong_shared_event(ai, bj)
            if not kind: continue
            # temporal guard
            g = gap_between(ai, bj)
            if g is not None and g > GAP_MAX: continue
            if merged_span(ai, bj) > SPAN_MAX: continue
            ba, bb = ai["births"], bj["births"]
            shared_birth = bool(ba & bb)
            # birth-year contradiction veto (distinct non-equal births = namesakes),
            # unless a shared EXACT specific appointment proves an OCR birth slip.
            birth_conflict = bool(ba and bb and not shared_birth)
            if birth_conflict and kind != "appt_yr":
                continue
            # FATHER/SON GUARD: the only signals that defeat a sequential dynasty (a
            # father and son holding the same colony office in *different* years -- e.g.
            # the two George Leakes of WA) are a shared exact appointment-YEAR or a
            # shared birth year. Career overlap (gap<0) is NOT safe: father/son careers
            # overlap too. So the no-year tiers (specific_contig/chain2) AUTO-merge ONLY
            # when a birth year confirms identity; otherwise HOLD for human review.
            auto = (kind in ("appt_yr", "genericyr_contig")
                    or (kind in ("specific_contig", "chain2") and shared_birth))
            edge = {
                "surname": sk, "kind": kind, "auto": auto,
                "a": canons[i], "b": canons[j],
                "a_given": sorted(ai["givens"]), "b_given": sorted(bj["givens"]),
                "a_births": sorted(ba), "b_births": sorted(bb),
                "a_span": span(ai), "b_span": span(bj), "gap": g,
                "evidence": ev,
            }
            new_edges.append(edge)
            if auto:
                union(canons[i], canons[j])

# ---- SECOND PASS: appointment-keyed blocking (catches SURNAME OCR variants) ----
# A surname OCR slip (GREG/GREIG, THOMPSON/THOMSON, MAC/Mc) lands the two records in
# different surname blocks, so pass 1 never compares them. Block instead on a shared
# SPECIFIC exact appointment (job@place@YEAR) -- two people virtually never share one --
# then require the surnames to be OCR-near and the given names compatible.
def surname_ocr_ok(sa, sb):
    if sa == sb: return True
    return min(len(sa), len(sb)) >= 4 and Levenshtein.distance(sa, sb) <= 1

def has_full_given(g):
    return len([t for t in re.split(r"[ .]+", g or "") if len(t) >= 2]) >= 2

def full_given_match(ga, gb):
    for a in ga:
        if not has_full_given(a): continue
        for b in gb:
            if has_full_given(b) and name_pair_ok({a}, {b}): return True
    return False

# re-aggregate per CURRENT root (so pass-1 merges are reflected)
root_agg = {}
for c, a in agg.items():
    r = find(c)
    ra = root_agg.setdefault(r, {"qids": set(), "years": [], "postings_yr": set(),
                                 "givens": set(), "births": set(), "surnames": set()})
    ra["qids"] |= a["qids"]; ra["years"] += a["years"]; ra["postings_yr"] |= a["postings_yr"]
    ra["givens"] |= a["givens"]; ra["births"] |= a["births"]
    if a["surname"]: ra["surnames"].add(a["surname"])

appt_idx = defaultdict(set)
for r, ra in root_agg.items():
    for (ps, q, y) in ra["postings_yr"]:
        if ps not in GENERIC_POS:
            appt_idx[(ps, q, y)].add(r)

seen_pairs = set()
for key, rset in appt_idx.items():
    rs = sorted(rset)
    if len(rs) < 2: continue
    for i in range(len(rs)):
        for j in range(i + 1, len(rs)):
            r1, r2 = rs[i], rs[j]
            if find(r1) == find(r2): continue
            pk = (r1, r2)
            if pk in seen_pairs: continue
            seen_pairs.add(pk)
            a1, a2 = root_agg[r1], root_agg[r2]
            # surnames must be DIFFERENT-but-OCR-near (same-surname pairs are pass 1's job)
            sn_ok = any(s1 != s2 and surname_ocr_ok(s1, s2)
                        for s1 in a1["surnames"] for s2 in a2["surnames"])
            if not sn_ok: continue
            if not name_pair_ok(a1["givens"], a2["givens"]): continue
            b1, b2 = a1["births"], a2["births"]
            if b1 and b2 and not (b1 & b2): continue          # birth conflict: never for surname class
            g = gap_between(a1, a2)
            if g is not None and g > GAP_MAX: continue
            if merged_span(a1, a2) > SPAN_MAX: continue
            shared_spec = sorted((ps, q, y) for (ps, q, y) in (a1["postings_yr"] & a2["postings_yr"])
                                 if ps not in GENERIC_POS)
            # distinct (job@place) -- a role attested across two editions (same job@place,
            # different year) is ONE appointment, not two independent coincidences.
            distinct_appts = {(ps, q) for (ps, q, y) in shared_spec}
            # STRICTER auto-gate for surname variation (surname is the primary key): need
            # >=2 DISTINCT shared appointments, OR a full (non-initials) given-name match,
            # OR a shared birth year. Otherwise -> HOLD for review.
            auto = (len(distinct_appts) >= 2 or full_given_match(a1["givens"], a2["givens"])
                    or bool(b1 & b2))
            edge = {
                "surname": "/".join(sorted(a1["surnames"] | a2["surnames"])),
                "kind": "surname_ocr", "auto": auto, "a": r1, "b": r2,
                "a_given": sorted(a1["givens"]), "b_given": sorted(a2["givens"]),
                "a_births": sorted(b1), "b_births": sorted(b2),
                "a_span": span(a1), "b_span": span(a2), "gap": g,
                "evidence": [f"{ps}@{q}:{y}" for ps, q, y in shared_spec[:4]],
            }
            new_edges.append(edge)
            if auto:
                union(r1, r2)

auto_edges = [e for e in new_edges if e["auto"]]
held_edges = [e for e in new_edges if not e["auto"]]
with open(args.out, "w") as fh:
    for e in auto_edges:
        fh.write(json.dumps(e, ensure_ascii=False) + "\n")
held_path = args.out.replace(".jsonl", "") + ".held.jsonl"
with open(held_path, "w") as fh:
    for e in held_edges:
        fh.write(json.dumps(e, ensure_ascii=False) + "\n")

# ---- report ----
from collections import Counter
kc = Counter(e["kind"] for e in auto_edges)
hc = Counter(e["kind"] for e in held_edges)
print(f"canonicals scanned: {len(agg):,} | surname blocks (>=2 canon): "
      f"{sum(1 for s in by_surname.values() if len(s)>=2):,}")
print(f"AUTO merge edges: {len(auto_edges):,}   HELD (review): {len(held_edges):,}")
for k in ("appt_yr", "genericyr_contig", "specific_contig", "chain2", "surname_ocr"):
    print(f"   {k:<18} auto={kc.get(k,0):>5}  held={hc.get(k,0):>4}")
print(f"\nAUTO sample (up to {args.sample}):")
for e in auto_edges[:args.sample]:
    print(f"  {e['surname'].upper():<14} [{e['kind']}] gap={e['gap']}")
    print(f"     A {e['a']:<24} {e['a_given']} b={e['a_births'] or '-'} {e['a_span']}")
    print(f"     B {e['b']:<24} {e['b_given']} b={e['b_births'] or '-'} {e['b_span']}")
    print(f"     ev={e['evidence'][:3]}")
print(f"\nwrote AUTO -> {args.out}   HELD -> {held_path}")

# ---- optional: compose augmented merge map ----
if args.emit_map:
    # final canonical for every pid that appears in existing map or new edges
    pids = set()
    for r in existing: pids.add(r["person_id"]); pids.add(r["canonical_person_id"])
    for e in new_edges: pids |= {e["a"], e["b"]}
    for a in agg.values():
        for p in a["pids"]: pids.add(p)
    rows = []
    for p in sorted(pids):
        c = find(p)
        if c != p:
            rows.append({"person_id": p, "canonical_person_id": c})
    with open(args.emit_map, "w") as fh:
        for r in rows:
            fh.write(json.dumps(r) + "\n")
    print(f"composed map ({len(rows):,} non-trivial mappings) -> {args.emit_map}")
