#!/usr/bin/env python3
"""Stage-3 person-dedup CANDIDATE generator (no merges — evidence only).

The structured corpus (llm_struct_corpus.reviewed.jsonl, 36,167 records) is one
record per Stage-2 person chain. ~4,800 same-name groups survived Stage-2's
text-chain + raw-text-career dedup because Stage-2 ran BEFORE LLM structuring and
BEFORE place grounding. Stage-3 re-examines those same-name groups with the two
NEW signals now available:
  - LLM-extracted birth_year (cleaner than raw-text birth year)
  - grounded place_qid event overlap (cleaner than raw-text token jaccard)

This script does NOT merge. It emits, per same-name group, a TIER + the evidence
so the merge precision can be eyeballed before any fold:

  A_birth   >=1 distinct birth_year and all members agree (<=1 distinct) -> high conf
  B_place   no birth_year on any member, but members share >=1 place_qid
            with contiguous/overlapping career years -> place-driven (the new lever)
  CONFLICT  >=2 distinct birth_years -> likely namesakes (or OCR birth error if
            place_qids strongly overlap) -> DO NOT auto-merge, flag
  WEAK      no birth_year, no shared place_qid -> leave separate (likely namesake)

  python3 kg_dedup_stage3_candidates.py [--sample 12]

Outputs:
  data/kg/dedup_stage3_candidates.jsonl   one row per same-name group (all tiers)
  stdout                                  counts + a stratified readable sample
"""
from __future__ import annotations
import argparse, json, re
from collections import defaultdict
from col_match.services.compile import _names_compatible  # calibrated 0-FP name gate

ap = argparse.ArgumentParser()
ap.add_argument("--corpus", default="data/kg/llm_struct_corpus.reviewed.jsonl")
ap.add_argument("--grounding", default="data/kg/places_grounding.jsonl")
ap.add_argument("--out", default="data/kg/dedup_stage3_candidates.jsonl")
ap.add_argument("--sample", type=int, default=12)
args = ap.parse_args()

NK = re.compile(r"[^a-z]")
def nk(s): return NK.sub("", (s or "").lower())
def edition(pid):
    m = re.search(r"(col|dol|iol)(\d{4})", pid or ""); return int(m.group(2)) if m else None

# place surface -> grounded qid
gqid = {}
for l in open(args.grounding):
    r = json.loads(l)
    if r.get("qid"): gqid[r["place"]] = r["qid"]

_PSTEM = re.compile(r"[^a-z]")
def posstem(p): return _PSTEM.sub("", (p or "").lower())[:14]

# Generic, high-frequency positions: a shared (generic-position, common-place) is
# NOT person-identifying on its own. Such a posting is only conclusive when it
# carries a matching YEAR (an exact appointment) or appears in a multi-posting chain.
GENERIC_POS = {
    "assistantcommi","assistantengin","executiveengin","assistantmagis","deputycommissi",
    "assistantsuper","officiating","confirmed","assistant","engineer","clerk","magistrate",
    "joinedtheservi","probationer","extraassistant","subdivisional","actingmagistr",
    "superintenden","districtsuperi","executiveengi","assistantmagi",
}

def summarize(rec):
    """Per-record dedup features: place_qids, year span, and POSTINGS.

    postings_yr  = {(posstem, place_qid, year)}  exact appointment keys (strongest)
    postings     = {(posstem, place_qid)}        job@place keys (chain signal)
    """
    qids, years = set(), []
    postings_yr, postings = set(), set()
    for e in rec.get("events") or []:
        pl = e.get("place")
        q = gqid.get(pl) if pl else None
        ps = posstem(e.get("position") or e.get("position_norm"))
        if q: qids.add(q)
        ys, ye = e.get("year_start"), e.get("year_end")
        for y in (ys, ye):
            if isinstance(y, int): years.append(y)
        if ps and q:
            postings.add((ps, q))
            if isinstance(ys, int): postings_yr.add((ps, q, ys))
    return {
        "person_id": rec.get("person_id"),
        "edition": edition(rec.get("person_id")),
        "birth_year": rec.get("birth_year"),
        "given_names": rec.get("given_names"),
        "education": (rec.get("education") or "")[:120],
        "n_events": len(rec.get("events") or []),
        "place_qids": sorted(qids),
        "postings": postings,
        "postings_yr": postings_yr,
        "year_lo": min(years) if years else None,
        "year_hi": max(years) if years else None,
    }

# group structured records by normalized (surname, given_names)
groups = defaultdict(list)
n_records = 0
for l in open(args.corpus):
    rec = json.loads(l); n_records += 1
    sk, gk = nk(rec.get("surname")), nk(rec.get("given_names"))
    if sk and gk:                       # require BOTH names present (0-FP)
        groups[(sk, gk)].append(rec)

def year_contiguous(members):
    """min gap between any two members' [lo,hi] career spans (<=2 == contiguous,
    negative == overlapping). None if any member has no years."""
    spans = [(m["year_lo"], m["year_hi"]) for m in members if m["year_lo"] is not None]
    if len(spans) < 2: return None
    best = None
    for i in range(len(spans)):
        for j in range(i + 1, len(spans)):
            a, b = spans[i], spans[j]
            gap = max(a[0], b[0]) - min(a[1], b[1])   # >0 disjoint, <=0 overlap
            best = gap if best is None else min(best, gap)
    return best

def name_ok(members):
    """all pairs pass the calibrated given-name compatibility gate."""
    gs = [m["given_names"] for m in members]
    for i in range(len(gs)):
        for j in range(i + 1, len(gs)):
            if not _names_compatible(gs[i], gs[j]): return False
    return True

cands = []
for (sk, gk), recs in groups.items():
    if len(recs) < 2: continue
    members = [summarize(r) for r in recs]
    births = sorted({m["birth_year"] for m in members if m["birth_year"]})
    shared_qids = set.intersection(*[set(m["place_qids"]) for m in members]) if all(m["place_qids"] for m in members) else set()
    # union of pairwise-shared qids (weaker: any two members share)
    any_shared = set()
    for i in range(len(members)):
        for j in range(i + 1, len(members)):
            any_shared |= set(members[i]["place_qids"]) & set(members[j]["place_qids"])
    contig = year_contiguous(members)
    names_compatible = name_ok(members)

    # --- POSTING signals (the appointment-chain lever): pairwise-shared job@place ---
    shared_post_yr, shared_post = set(), set()
    for i in range(len(members)):
        for j in range(i + 1, len(members)):
            shared_post_yr |= members[i]["postings_yr"] & members[j]["postings_yr"]
            shared_post    |= members[i]["postings"]    & members[j]["postings"]
    # a shared posting is "specific" if the position is not in the generic head
    specific_post = {(ps, q) for (ps, q) in shared_post if ps not in GENERIC_POS}
    # exact appointment (job@place@year) OR a multi-posting chain OR a specific shared post
    strong_posting = bool(shared_post_yr) or len(shared_post) >= 2 or bool(specific_post)

    if len(births) >= 2:
        # different birth years = namesakes, UNLESS a strong posting says same person
        # (then it's an OCR birth-year error) -> route to review, never auto-split silently
        tier = "CONFLICT_POSTING" if strong_posting else "CONFLICT"
    elif len(births) == 1:
        tier = "A_birth" if names_compatible else "CONFLICT"
    elif strong_posting and names_compatible and (contig is None or contig <= 5):
        tier = "C_posting"                       # NEW: appointment-chain merge, no birth needed
    elif names_compatible and len(any_shared) >= 2 and (contig is None or contig <= 2):
        tier = "B_place"                         # non-thin: >=2 shared colonies + contiguous
    elif any_shared and names_compatible and (contig is None or contig <= 2):
        tier = "B_thin"                          # 1 common colony only, no shared posting -> HOLD
    else:
        tier = "WEAK"

    for m in members:                            # make JSON-serializable; drop heavy sets
        m["n_postings"] = len(m.pop("postings"))
        m.pop("postings_yr", None)
    cands.append({
        "surname_key": sk, "given_key": gk, "tier": tier,
        "n_members": len(members),
        "births": births,
        "shared_qids_all": sorted(shared_qids),
        "shared_qids_any": sorted(any_shared),
        "shared_postings": sorted(f"{ps}@{q}" for ps, q in shared_post),
        "shared_postings_yr": sorted(f"{ps}@{q}:{y}" for ps, q, y in shared_post_yr),
        "n_specific_postings": len(specific_post),
        "strong_posting": strong_posting,
        "year_gap": contig,
        "names_compatible": names_compatible,
        "members": members,
    })

# write all candidates
with open(args.out, "w") as fh:
    for c in cands:
        fh.write(json.dumps(c, ensure_ascii=False) + "\n")

# ---- report ----
from collections import Counter
tc = Counter(c["tier"] for c in cands)
rec_in = Counter()
for c in cands: rec_in[c["tier"]] += c["n_members"]
print(f"corpus records: {n_records:,}  | same-name groups (both names present): {len(cands):,}\n")
print(f"{'tier':<18}{'groups':>8}{'records':>9}{'-> merges_to':>13}")
AUTO = ("A_birth", "C_posting", "B_place")          # auto-mergeable tiers
HOLD = ("B_thin", "CONFLICT_POSTING")               # review (over-merge risk / OCR birth)
for t in ("A_birth", "C_posting", "B_place", "B_thin", "CONFLICT_POSTING", "CONFLICT", "WEAK"):
    g = tc.get(t, 0); r = rec_in.get(t, 0)
    print(f"{t:<18}{g:>8}{r:>9}{r-g:>13}")
mergeable = sum(tc.get(t, 0) for t in AUTO)
recs_folded = sum(rec_in.get(t, 0) - tc.get(t, 0) for t in AUTO)
print(f"\nif AUTO ({'+'.join(AUTO)}) merged: {n_records:,} -> ~{n_records - recs_folded:,} persons "
      f"({recs_folded:,} records folded across {mergeable:,} groups)")
held_folded = sum(rec_in.get(t, 0) - tc.get(t, 0) for t in HOLD)
print(f"HOLD tiers ({'+'.join(HOLD)}): {sum(tc.get(t,0) for t in HOLD):,} groups / "
      f"{held_folded:,} potential merges -> review before applying")

def show(tier, k):
    rows = [c for c in cands if c["tier"] == tier]
    print(f"\n===== {tier}  ({len(rows)} groups) — sample {min(k,len(rows))} =====")
    for c in rows[:k]:
        print(f"  {c['surname_key'].upper()}, {c['given_key']}  "
              f"[{c['n_members']} recs | births={c['births'] or '-'} | "
              f"shared_qids={c['shared_qids_any'] or '-'} | year_gap={c['year_gap']}]")
        for m in c["members"]:
            print(f"      {m['person_id']:<22} b.{str(m['birth_year'] or '-'):<6} "
                  f"ed{m['edition']} {m['n_events']}ev {m['year_lo']}-{m['year_hi']} "
                  f"q={m['place_qids'][:4]} edu={m['education'][:45]!r}")

for t in ("A_birth", "B_place", "CONFLICT", "WEAK"):
    show(t, args.sample)
print(f"\nwrote -> {args.out}")
