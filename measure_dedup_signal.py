"""MEASURE-ONLY: (1) why duplicate-of-matched fragments fail to merge today,
and (2) the FALSE-MERGE risk envelope of an early-career identity signal,
calibrated against birth-year-contradicting pairs as ground-truth NEGATIVES.

No writes. Run with COL_USE_AUGMENTED=1.
"""
from __future__ import annotations
import json, os
from collections import defaultdict
from pathlib import Path
from rapidfuzz import fuzz, process, distance

from col_match.config import Config
from col_match.services.match import _norm, _shared_spelled_forename, _truncation_index
from col_match.services.schema import Biography, ParsedEntry
from col_match.services.compile import _pos_norm, _education_sim, _initials
from col_match.services.infer_colony import apply_recovered_places

cfg = Config.from_env(); DD = cfg.data_dir
bios = [Biography.model_validate_json(l)
        for l in (Path(DD)/"biographies"/"biographies.jsonl").open(encoding="utf-8")]
apply_recovered_places(bios, DD)

# version_id -> (education, title_rank) from ParsedEntries (richer than Biography)
edu = {}
for name in ("llm.jsonl", "rules.jsonl"):
    p = Path(DD)/"parsed"/name
    if p.exists():
        for l in p.open(encoding="utf-8"):
            r = ParsedEntry.model_validate_json(l)
            edu[r.version_id] = r.education or ""
def bio_edu(b):
    return max((edu.get(v, "") for v in b.version_ids), key=len, default="")

matched = set()
for l in (Path(DD)/"matches"/"stint_matches.jsonl").open(): matched.add(json.loads(l)["bio_id"])
for l in (Path(DD)/"matches"/"record_attachments.jsonl").open(): matched.add(json.loads(l)["bio_id"])

def dated(b): return [e for e in b.events if e.year_start is not None]
def overlap(a, b):
    n = 0
    for ea in dated(a):
        for eb in dated(b):
            if abs(ea.year_start - eb.year_start) > 1: continue
            if ea.place and eb.place and _norm(ea.place) == _norm(eb.place): n += 1; break
            if ea.position and eb.position and \
               fuzz.token_set_ratio(_pos_norm(ea.position), _pos_norm(eb.position)) >= 80: n += 1; break
    return n
def first_ini(b):
    i = _initials(b.given_names); return i[0] if i else "?"

mbysur = defaultdict(list)
for b in bios:
    if b.bio_id in matched: mbysur[_norm(b.surname)].append(b)
mkeys = list(mbysur); tidx = _truncation_index(mkeys)

def best_twin(b):
    key = _norm(b.surname); rel = {}
    for c in mbysur.get(key, []): rel[c.bio_id] = ("exact", c)
    for k in tidx.get(key, ()):
        for c in mbysur.get(k, []): rel.setdefault(c.bio_id, ("trunc", c))
    if len(key) >= 5:
        for k, d, _ in process.extract(key, mkeys, scorer=distance.Levenshtein.distance,
                                       score_cutoff=2, limit=5):
            if k != key:
                for c in mbysur.get(k, []): rel.setdefault(c.bio_id, (f"fuzzy{int(d)}", c))
    best = None
    for r, c in rel.values():
        if c.bio_id == b.bio_id: continue
        if not _shared_spelled_forename(b.given_names, c.given_names): continue
        ov = overlap(b, c)
        cand = (ov, r, c)
        if best is None or ov > best[0]: best = cand
    return best

# ---------- PART 1: why don't the duplicate-of-matched merge ----------
reasons = defaultdict(int); rel_ct = defaultdict(int); birth_ct = defaultdict(int)
ov_ct = defaultdict(int); n_dup = 0
for b in bios:
    if b.bio_id in matched: continue
    tw = best_twin(b)
    if not tw: continue
    n_dup += 1
    ov, rel, c = tw
    rel_ct[rel.split("0")[0] if rel.startswith("fuzzy") else rel] += 1
    bb, cb = b.birth_year, c.birth_year
    if bb and cb: birth_ct["both_equal" if bb.value == cb.value else "both_DIFF"] += 1
    elif bb or cb: birth_ct["one_only"] += 1
    else: birth_ct["neither"] += 1
    ov_ct[min(ov, 3)] += 1
    same_block = (_norm(b.surname) == _norm(c.surname)) and (first_ini(b) == first_ini(c))
    has_birth_both = bool(bb and cb)
    e1, e2 = bio_edu(b), bio_edu(c)
    edu_ok = (min(len(_norm(e1)), len(_norm(e2))) >= 12
              and fuzz.token_set_ratio(_norm(e1), _norm(e2)) >= 85)
    # why didn't a pass merge it? (passes A/B/C need birth year for B/C; A needs same block + 2 anchors)
    if not same_block and not has_birth_both:
        reasons["diff_block_AND_no_shared_birth (no pass reaches)"] += 1
    elif same_block and ov < 2 and not has_birth_both:
        reasons["same_block_but_thin (<2 anchors, no birth)"] += 1
    elif has_birth_both and bb.value != cb.value:
        reasons["birth_years_CONTRADICT (correctly blocked / maybe not twin)"] += 1
    elif has_birth_both and ov < 1 and not edu_ok:
        reasons["shared_birth_but_no_2nd_anchor"] += 1
    else:
        reasons["other (should have merged? inspect)"] += 1

print(f"=== PART 1: {n_dup} unmatched bios are same-person twins of a MATCHED bio ===")
print("surname relation to twin:", dict(rel_ct))
print("birth-year status:       ", dict(birth_ct))
print("event-overlap w/ twin:   ", {f">={k}" if k==3 else k: v for k, v in sorted(ov_ct.items())})
print("BLOCKING MECHANISM:")
for r, n in sorted(reasons.items(), key=lambda kv: -kv[1]):
    print(f"  {n:5d}  {r}")

# ---------- PART 2: FP calibration of an early-career signal ----------
# blocks: same surname_norm + shared spelled forename, BOTH have birth year.
# positives = same birth year; NEGATIVES = different birth year (guaranteed diff person).
def early_window_overlap(a, b, frac=0.5):
    """events of the LONGER bio within its first `frac` of career span; count
    matches against the other bio (year +/-1, same place or position>=80)."""
    da, db = dated(a), dated(b)
    if not da or not db: return 0, 0.0
    longer = a if len(da) >= len(db) else b
    dl = dated(longer)
    yrs = [e.year_start for e in dl]
    lo, hi = min(yrs), max(yrs)
    cut = lo + max(1, round((hi - lo) * frac))
    early = [e for e in dl if e.year_start <= cut]
    other = b if longer is a else a
    matches = 0
    for ea in early:
        for eb in dated(other):
            if abs(ea.year_start - eb.year_start) > 1: continue
            if ea.place and eb.place and _norm(ea.place) == _norm(eb.place): matches += 1; break
            if ea.position and eb.position and \
               fuzz.token_set_ratio(_pos_norm(ea.position), _pos_norm(eb.position)) >= 80: matches += 1; break
    return matches, matches / max(len(early), 1)

bybirthsur = defaultdict(list)
for b in bios:
    if b.birth_year: bybirthsur[_norm(b.surname)].append(b)

def tight_name(a, b):
    """initials EQUAL after position, OR >=2 shared spelled forenames."""
    ia = [t[0].upper() for t in (a.given_names or "").replace(".", " ").split() if t]
    ib = [t[0].upper() for t in (b.given_names or "").replace(".", " ").split() if t]
    if ia and ib and ia == ib: return True
    ta = {w.lower() for w in (a.given_names or "").replace(".", " ").split() if len(w) > 2}
    tb = {w.lower() for w in (b.given_names or "").replace(".", " ").split() if len(w) > 2}
    return len(ta & tb) >= 2

pos = []; neg = []  # dict of signals
for sur, group in bybirthsur.items():
    if len(group) < 2 or not sur: continue
    for i in range(len(group)):
        for j in range(i+1, len(group)):
            a, b = group[i], group[j]
            if not _shared_spelled_forename(a.given_names, b.given_names): continue
            em, ef = early_window_overlap(a, b)
            e1, e2 = bio_edu(a), bio_edu(b)
            el = min(len(_norm(e1)), len(_norm(e2)))
            es = fuzz.token_set_ratio(_norm(e1), _norm(e2)) if el >= 12 else 0
            ha = {(_norm(h.award), h.year) for h in a.honours if h.year}
            hb = {(_norm(h.award), h.year) for h in b.honours if h.year}
            rec = {"em": em, "ef": round(ef, 2), "es": es, "elong": el >= 20,
                   "hon": bool(ha & hb), "tight": tight_name(a, b), "pair": (a, b)}
            (pos if a.birth_year.value == b.birth_year.value else neg).append(rec)

print(f"\n=== PART 2: early-career signal calibration (same surname + shared spelled forename, both birth-dated) ===")
print(f"POSITIVE pairs (same birth year, ~same person): {len(pos)}")
print(f"NEGATIVE pairs (diff birth year, DIFFERENT person): {len(neg)}")
def rate(rows, pred): return sum(1 for r in rows if pred(r))
preds = [
    ("em>=2", lambda r: r["em"] >= 2),
    ("em>=2 AND edu>=85", lambda r: r["em"] >= 2 and r["es"] >= 85),
    ("em>=2 AND edu_long edu>=88", lambda r: r["em"] >= 2 and r["elong"] and r["es"] >= 88),
    ("em>=3 AND edu>=80", lambda r: r["em"] >= 3 and r["es"] >= 80),
    ("em>=2 AND honour_shared", lambda r: r["em"] >= 2 and r["hon"]),
    ("em>=2 AND tight_name", lambda r: r["em"] >= 2 and r["tight"]),
    ("em>=2 AND tight AND (edu>=85 OR hon)", lambda r: r["em"] >= 2 and r["tight"] and (r["es"] >= 85 or r["hon"])),
    ("edu_long edu>=90 (alone)", lambda r: r["elong"] and r["es"] >= 90),
    ("em>=2 AND (edu>=85 OR hon) AND tight", lambda r: r["em"] >= 2 and r["tight"] and (r["es"] >= 85 or r["hon"])),
    ("em>=3 AND tight AND edu>=85", lambda r: r["em"] >= 3 and r["tight"] and r["es"] >= 85),
]
def one_digit(y1, y2):
    s1, s2 = str(y1), str(y2)
    return len(s1) == len(s2) == 4 and sum(c1 != c2 for c1, c2 in zip(s1, s2)) == 1

# re-segment negatives by birth-year gap: small/one-digit = SAME person (OCR/print
# noise); large gap = genuinely DIFFERENT person (father/son namesake).
for r in neg:
    a, b = r["pair"]; r["bdiff"] = abs(a.birth_year.value - b.birth_year.value)
    r["onedig"] = one_digit(a.birth_year.value, b.birth_year.value)
noise_neg = [r for r in neg if r["bdiff"] <= 2 or (r["onedig"] and r["bdiff"] <= 20)]
true_neg = [r for r in neg if r not in noise_neg]
print(f"\n  of {len(neg)} 'diff birth' pairs: {len(noise_neg)} are birth-NOISE (same person, gap<=2 or"
      f" one-digit OCR), {len(true_neg)} are TRUE different-person (larger gap)")
print(f"  -> recomputing FP against the {len(true_neg)} TRUE negatives only:")
for label, pred in preds:
    tp = rate(pos, pred) + rate(noise_neg, pred)   # noise_neg firing = CORRECT merges
    fp = rate(true_neg, pred)
    print(f"  {label:38s} merges {tp:5d} same-person  |  FALSE-merges {fp:3d}/{len(true_neg)} true-diff")

print("\n  TRUE-different-person pairs (gap>2, not one-digit) the best combo fires on:")
combo = lambda r: r["em"] >= 2 and r["es"] >= 85
for r in [x for x in true_neg if combo(x)][:12]:
    a, b = r["pair"]
    print(f"    '{a.surname},{a.given_names}'(b{a.birth_year.value}) vs "
          f"'{b.surname},{b.given_names}'(b{b.birth_year.value})  gap={r['bdiff']} em={r['em']} edu={r['es']:.0f}")
