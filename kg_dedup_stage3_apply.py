#!/usr/bin/env python3
"""Apply the Stage-3 merge map: fold each canonical's member records into one
person with a unioned career timeline.

Bios are cumulative across editions, so the timeline = the richest member's
events as the spine, PLUS any dated appointment from other members not already
present (recovers events a later edition condensed out). Editions and folded
person_ids are preserved as provenance.

  python3 kg_dedup_stage3_apply.py [--out data/kg/llm_struct_corpus.stage3.jsonl]
"""
from __future__ import annotations
import argparse, json, re
from collections import defaultdict
from rapidfuzz import fuzz

ap = argparse.ArgumentParser()
ap.add_argument("--corpus", default="data/kg/llm_struct_corpus.reviewed.jsonl")
ap.add_argument("--map", default="data/kg/dedup_stage3_merge_map.jsonl")
ap.add_argument("--out", default="data/kg/llm_struct_corpus.stage3.jsonl")
args = ap.parse_args()

mmap = {r["person_id"]: r["canonical_person_id"]
        for r in (json.loads(l) for l in open(args.map))}

# Stage-2 bio-level provenance: structured person_id -> (editions, bio_ids).
# A structured record is one Stage-2 cluster, attested across many edition bios;
# carry that through so `editions` reflects the true span, not just Stage-3 folds.
import os
prov = {}
_provf = os.environ.get("COL_PROV", "data/kg/persons.deduped2.jsonl")
if os.path.exists(_provf):
    for l in open(_provf):
        d = json.loads(l)
        prov[d["person_id"]] = (d.get("editions") or [], d.get("attestation_bio_ids") or [])

recs = [json.loads(l) for l in open(args.corpus)]
def canon(pid): return mmap.get(pid, pid)
def edition(pid):
    m = re.search(r"(col|dol)(\d{4})", pid); return int(m.group(2)) if m else None

groups = defaultdict(list)
for r in recs:
    groups[canon(r["person_id"])].append(r)

_ROMAN = re.compile(r"\b(?=[ivxlc])(i{1,3}|iv|vi{0,3}|ix|xi{0,3})\b")
def nums(p):
    """identifying numbers in a position (197th brigade, class V) -- two posts that
    differ by these are DISTINCT appointments, never OCR variants of each other."""
    s = (p or "").lower()
    return frozenset(re.findall(r"\d+", s)) | frozenset(_ROMAN.findall(s))
def posstem(p): return re.sub(r"[^a-z]", "", (p or "").lower())[:12]
def placenorm(p): return re.sub(r"[^a-z]", "", (p or "").lower())
def ekey(e): return (posstem(e.get("position")), nums(e.get("position")),
                     e.get("year_start"), placenorm(e.get("place")))
def filled(e): return sum(1 for v in e.values() if v not in (None, "", False))

def merge_events(members):
    # spine = member with most events; then add unseen dated appointments
    spine = max(members, key=lambda r: len(r.get("events") or []))
    merged, seen = [], {}
    order = [spine] + [m for m in members if m is not spine]
    for m in order:
        for e in (m.get("events") or []):
            k = ekey(e)
            if k not in seen:
                seen[k] = len(merged); merged.append(dict(e))
            else:
                # keep the more complete version of the same appointment
                i = seen[k]
                if filled(e) > filled(merged[i]): merged[i] = dict(e)
    merged.sort(key=lambda e: (e.get("year_start") if e.get("year_start") is not None else 9999,
                               posstem(e.get("position"))))
    # collapse OCR/abbrev variants of the SAME appointment: same year_start and
    # same normalized place, with substring or high token-set overlap on position.
    # keep the longer (more descriptive) position; prefer a filled year_end.
    out = []
    for e in merged:
        ys, pl = e.get("year_start"), placenorm(e.get("place"))
        pos = (e.get("position") or "").lower().strip()
        hit = None
        if ys is not None:
            for o in out:
                if o.get("year_start") == ys and placenorm(o.get("place")) == pl:
                    op = (o.get("position") or "").lower().strip()
                    if (pos and op and nums(pos) == nums(op)
                            and (pos in op or op in pos or fuzz.token_set_ratio(pos, op) >= 85)):
                        hit = o; break
        if hit is None:
            out.append(e)
        else:
            if len(e.get("position") or "") > len(hit.get("position") or ""):
                hit["position"] = e.get("position")
            if hit.get("year_end") is None and e.get("year_end") is not None:
                hit["year_end"] = e.get("year_end")
    return out

def longest(strs):
    strs = [s for s in strs if s]
    return max(strs, key=len) if strs else None

from collections import Counter
def member_atts(m):
    """how many edition-bios attest this member (OCR-error spellings appear in fewer)."""
    _, pb = prov.get(m["person_id"], (None, None))
    return len(pb) if pb else (m.get("n_attestations") or 1)

def _given_fullness(g):
    toks = [t for t in re.split(r"[ .]+", g or "") if t]
    return (sum(1 for t in toks if len(t) >= 2), len(toks), len(g or ""))  # #full-tokens, #tokens, len

def pick_name(members):
    """Canonical display name across merged members:
    - surname = the spelling carried by the MOST attestations (an OCR slip like
      GREG/GREIG or THOMPSON/THOMSON is usually a single edition, the correct form
      recurs), tie-break to the longer spelling.
    - given_names = the FULLEST form (expand initials 'I. V. G.' -> 'Iaan Vandin
      Gordon'), tie-break by attestations then length.
    Surname and given may come from different members -- that is the best
    reconstruction of one person, not a contradiction."""
    sc = Counter()
    for m in members:
        if m.get("surname"): sc[m["surname"]] += member_atts(m)
    surname = max(sc, key=lambda s: (sc[s], len(s))) if sc else (members[0].get("surname"))
    cand = [m for m in members if m.get("given_names")]
    given = (max(cand, key=lambda m: (_given_fullness(m["given_names"]), member_atts(m)))
             ["given_names"] if cand else None)
    return surname, given

out = []
for cpid, members in groups.items():
    spine = max(members, key=lambda r: len(r.get("events") or []))
    # true provenance = union of each member's Stage-2 bio attestations
    bio_ids, eds_set = set(), set()
    for m in members:
        pe, pb = prov.get(m["person_id"], (None, None))
        if pb:
            bio_ids.update(pb); eds_set.update(pe)
        else:                                   # _s1 split: no Stage-2 cluster
            bio_ids.add(m["person_id"][4:] if m["person_id"].startswith("kgp_") else m["person_id"])
            e = edition(m["person_id"])
            if e: eds_set.add(e)
    eds = sorted(eds_set)
    honours = []
    seenh = set()
    for m in members:
        for h in (m.get("honours") or []):
            hk = json.dumps(h, sort_keys=True, ensure_ascii=False)
            if hk not in seenh: seenh.add(hk); honours.append(h)
    canon_surname, canon_given = pick_name(members)
    rec = {
        "person_id": cpid,
        "surname": canon_surname,
        "given_names": canon_given,
        "birth_year": next((m.get("birth_year") for m in members if m.get("birth_year")), None),
        "education": longest([m.get("education") for m in members]),
        "honours": honours,
        "events": merge_events(members),
        "terminal": next((m.get("terminal") for m in members if m.get("terminal")), None),
        "editions": eds,
        "n_attestations": len(bio_ids),
        "n_stage3_merged": len(members),
        "stage3_members": sorted(m["person_id"] for m in members),
        "attestations": sorted(bio_ids),
        "flags": sorted({f for m in members for f in (m.get("flags") or [])}),
    }
    out.append(rec)

out.sort(key=lambda r: (r.get("surname") or "", r.get("given_names") or ""))
with open(args.out, "w") as fh:
    for r in out: fh.write(json.dumps(r, ensure_ascii=False) + "\n")

tot_ev_in = sum(len(r.get("events") or []) for r in recs)
tot_ev_out = sum(len(r["events"]) for r in out)
multi = sum(1 for r in out if r["n_stage3_merged"] > 1)
print(f"in:  {len(recs):,} structured records, {tot_ev_in:,} events")
print(f"out: {len(out):,} persons ({multi:,} merged from >1 record), {tot_ev_out:,} events")
print(f"     events deduped by fold: {tot_ev_in - tot_ev_out:,}")
print(f"wrote -> {args.out}")
