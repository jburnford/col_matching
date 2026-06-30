"""MEASURE-ONLY: what ELSE in the bios can safely dedup the tail that pass E
(early-events>=2 + education>=85) cannot reach (thin careers / no education)?

Calibrate candidate same-person signals against the birth-year ground truth:
same-surname + shared-spelled-forename pairs, both birth-dated.
  POSITIVE  = same birth year OR one-digit-OCR difference (same person)
  TRUE NEG  = multi-digit birth gap >=3 (genuinely different person; this set is
              still mildly contaminated by double-OCR-errors, so FP is an UPPER bound)
Tail-focused: report signals that DON'T require education or >=2 early events.
Run with COL_USE_AUGMENTED=1.
"""
from __future__ import annotations
import json, re
from collections import defaultdict
from pathlib import Path
from rapidfuzz import fuzz
from rapidfuzz.distance import Levenshtein

from col_match.config import Config
from col_match.services.match import _norm, _shared_spelled_forename
from col_match.services.schema import Biography, ParsedEntry
from col_match.services.compile import _pos_norm, _canon_token

cfg = Config.from_env(); DD = cfg.data_dir
bios = [Biography.model_validate_json(l)
        for l in (Path(DD)/"biographies"/"biographies.jsonl").open(encoding="utf-8")]
edu = {}
for name in ("llm.jsonl", "rules.jsonl"):
    p = Path(DD)/"parsed"/name
    if p.exists():
        for l in p.open(encoding="utf-8"):
            r = ParsedEntry.model_validate_json(l)
            edu[r.version_id] = r.education or ""
def bio_edu(b): return max((edu.get(v, "") for v in b.version_ids), key=len, default="")

def toks(b):
    return [_canon_token(t) for t in re.split(r"[ .]+", b.given_names or "") if len(_canon_token(t)) > 2]

# corpus forename-token frequency (how many bios carry each spelled forename)
freq = defaultdict(int)
for b in bios:
    for t in set(toks(b)): freq[t] += 1

def dated(b): return [e for e in b.events if e.year_start is not None]
def early_overlap(a, b):
    da, db = dated(a), dated(b)
    if not da or not db: return 0
    longer, other = (a, b) if len(da) >= len(db) else (b, a)
    dl = dated(longer); yrs = [e.year_start for e in dl]
    cut = min(yrs) + max(1, round((max(yrs)-min(yrs))*0.5))
    n = 0
    for ea in [e for e in dl if e.year_start <= cut]:
        for eb in dated(other):
            if abs(ea.year_start-eb.year_start) > 1: continue
            if ea.place and eb.place and _norm(ea.place) == _norm(eb.place): n += 1; break
            if ea.position and eb.position and fuzz.token_set_ratio(_pos_norm(ea.position), _pos_norm(eb.position)) >= 80: n += 1; break
    return n
def one_digit(y1, y2):
    s1, s2 = str(y1), str(y2)
    return len(s1) == len(s2) == 4 and sum(c1 != c2 for c1, c2 in zip(s1, s2)) == 1
def full_name_equal(a, b):
    ta, tb = toks(a), toks(b)
    if len(ta) < 2 or len(tb) < 2 or len(ta) != len(tb): return False
    return all(x == y or Levenshtein.distance(x, y, score_cutoff=1) <= 1 for x, y in zip(ta, tb))
def honour_year(a, b):
    ha = {(_norm(h.award), h.year) for h in a.honours if h.year}
    hb = {(_norm(h.award), h.year) for h in b.honours if h.year}
    return bool(ha & hb)
def term_year(a, b):
    return bool(a.terminal and b.terminal and a.terminal.year and b.terminal.year
                and a.terminal.year == b.terminal.year)

bysur = defaultdict(list)
for b in bios:
    if b.birth_year and _norm(b.surname): bysur[_norm(b.surname)].append(b)

pos, neg = [], []
for sur, g in bysur.items():
    if len(g) < 2: continue
    for i in range(len(g)):
        for j in range(i+1, len(g)):
            a, b = g[i], g[j]
            if not _shared_spelled_forename(a.given_names, b.given_names): continue
            shared = set(toks(a)) & set(toks(b))
            rarest = min((freq[t] for t in shared), default=10**9)
            e1, e2 = bio_edu(a), bio_edu(b)
            es = fuzz.token_set_ratio(_norm(e1), _norm(e2)) if min(len(_norm(e1)), len(_norm(e2))) >= 12 else 0
            rec = {"em": early_overlap(a, b), "edu": es, "hy": honour_year(a, b),
                   "ty": term_year(a, b), "rare": rarest, "fne": full_name_equal(a, b),
                   "pair": (a, b)}
            same = a.birth_year.value == b.birth_year.value or one_digit(a.birth_year.value, b.birth_year.value)
            (pos if same else neg).append(rec)

print(f"POSITIVE (same/one-digit birth): {len(pos)}   TRUE-NEG (multi-digit gap): {len(neg)}\n")
print("PASS E baseline (for reference):")
print(f"  em>=2 AND edu>=85                          TP={sum(1 for r in pos if r['em']>=2 and r['edu']>=85):4d}  FP={sum(1 for r in neg if r['em']>=2 and r['edu']>=85):3d}")
print("\nNEW tail signals (education-free / thin-career):")
preds = [
    ("honour_year shared (alone)",              lambda r: r["hy"]),
    ("honour_year shared AND em>=1",            lambda r: r["hy"] and r["em"] >= 1),
    ("terminal(death) year shared AND em>=1",   lambda r: r["ty"] and r["em"] >= 1),
    ("terminal year shared AND rare<=50",       lambda r: r["ty"] and r["rare"] <= 50),
    ("full_name_equal (>=2 tok, exact)",        lambda r: r["fne"]),
    ("full_name_equal AND em>=1",               lambda r: r["fne"] and r["em"] >= 1),
    ("full_name_equal AND rare<=20",            lambda r: r["fne"] and r["rare"] <= 20),
    ("rare<=10 (rarest shared forename)",       lambda r: r["rare"] <= 10),
    ("rare<=10 AND em>=1",                      lambda r: r["rare"] <= 10 and r["em"] >= 1),
    ("rare<=20 AND fne AND em>=1",              lambda r: r["rare"] <= 20 and r["fne"] and r["em"] >= 1),
    ("rare<=20 AND (em>=1 OR hy OR ty)",        lambda r: r["rare"] <= 20 and (r["em"] >= 1 or r["hy"] or r["ty"])),
]
for label, pred in preds:
    tp = sum(1 for r in pos if pred(r)); fp = sum(1 for r in neg if pred(r))
    print(f"  {label:44s} TP={tp:4d}  FP={fp:3d}")

# show what the cleanest tail combo fires on among the TRUE-NEG (inspect for genuine father/son)
combo = lambda r: r["rare"] <= 20 and r["fne"] and (r["em"] >= 1 or r["hy"] or r["ty"])
print("\nTRUE-NEG pairs the 'rare<=20 AND full_name_equal AND (em>=1/hy/ty)' combo fires on:")
for r in [x for x in neg if combo(x)][:15]:
    a, b = r["pair"]
    print(f"  '{a.surname},{a.given_names}'(b{a.birth_year.value}) vs '{b.surname},{b.given_names}'(b{b.birth_year.value})"
          f"  gap={abs(a.birth_year.value-b.birth_year.value)} em={r['em']} rare={r['rare']} edu={r['edu']:.0f}")
