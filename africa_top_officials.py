#!/usr/bin/env python3
"""Do officials who reach the TOP move more?  (mobility -> attainment)

Top tier = ever held an apex office: governor / governor-general / lieutenant-
governor / high commissioner / officer administering the government. Detected on
the grounded role LABEL with a positive title regex and a negative guard that
strips 'secretary to the governor', military 'lieutenant', 'president of <board>',
tutors, etc.

The trap: top officials serve LONGER, and longer careers mechanically accrue
more moves. So we report BOTH raw mobility and mobility normalised by career
length, and we decompose moves BEFORE vs AFTER first reaching the top (governors
are themselves shuffled across governorships).
"""
import json, re, statistics as st
from collections import Counter
from africa_macro_regions import region_of, AFRICA_REGIONS

d = json.load(open("docs/data/careers.json"))
ROLES = d["roles"]
# apex title must be the HEAD of the role (the role IS a governorship), after an
# optional acting/administering prefix — not a relational form ('adc to governor').
APEX = re.compile(r"^(?:act(?:g|ing)?\.?\s+|officer\s+administering\s+|administering\s+)?"
                  r"(governor(?:[- ]general)?|lieut(?:enant|\.)?[- ]?governor|"
                  r"high[- ]?commissioner)(?:$|[\s,]|\s+of\s+|\s+and\s+)", re.I)
APEX2 = re.compile(r"^(?:officer\s+)?administ(?:ering|rator of) the government", re.I)
BAD = re.compile(r"\b(a\.?d\.?c|aide|de\s+c|accompan|secretary|clerk|assistant|private|pte|"
                 r"tutor|prince|royal|under|deputy|adviser|advsr|library|museum|"
                 r"printery|supervr?)\b|to\s+(the\s+)?(acting\s+)?(lieut\.?\s+)?governor|"
                 r"of\s+the\s+governor|governor\s+of\s+the\s+", re.I)
TOP_IDX = set()
for idx, (rid, lab) in enumerate(ROLES):
    if lab and (APEX.search(lab) or APEX2.search(lab)) and not BAD.search(lab):
        TOP_IDX.add(idx)
caps = sorted({ROLES[i][1] for i in TOP_IDX})
print(f"distinct apex role labels: {len(caps)}   sample:")
for c in caps[:20]: print("   ", c)
print()

AFR = AFRICA_REGIONS
def macro(qid): return region_of(qid, coarse=True)

recs = []
for pid, p in d["persons"].items():
    stints = [s for s in p.get("st", []) if s[0]]
    if not any(region_of(s[0]) in AFR for s in stints):
        continue                                            # African officials only
    yrs = [s[1] for s in stints if s[1] is not None]
    if not yrs:
        continue
    terr = [s[0] for s in stints]
    seq = [t for i, t in enumerate(terr) if i == 0 or t != terr[i-1]]   # collapse stays
    moves = len(seq) - 1
    # first year they hold a top role
    top_years = [s[1] for s in stints if len(s) >= 4 and s[3] in TOP_IDX and s[1] is not None]
    is_top = bool([s for s in stints if len(s) >= 4 and s[3] in TOP_IDX])
    span = (max(yrs) - min(yrs)) or 1
    # moves before first reaching top
    moves_pre = None
    if top_years:
        t0 = min(top_years)
        pre = [s[0] for s in sorted(stints, key=lambda s: (s[1] if s[1] is not None else 9999))
               if s[1] is not None and s[1] <= t0]
        preseq = [t for i, t in enumerate(pre) if i == 0 or t != pre[i-1]]
        moves_pre = len(preseq) - 1
    recs.append({"pid": pid, "top": is_top, "n_terr": len(set(terr)), "moves": moves,
                 "n_macro": len({macro(t) for t in terr}),
                 "n_afr_sub": len({region_of(t) for t in terr if region_of(t) in AFR}),
                 "span": span, "n_post": len(stints),
                 "moves_per_decade": moves / (span / 10),
                 "moves_pre_top": moves_pre})

top = [r for r in recs if r["top"]]
oth = [r for r in recs if not r["top"]]
def med(g, k): return st.median([r[k] for r in g])
def mean(g, k): return st.mean([r[k] for r in g])

print(f"African officials: {len(recs):,}   reached apex (governor/HC/lt-gov): "
      f"{len(top):,} ({100*len(top)/len(recs):.1f}%)")
print("\n                         TOP-tier      rest      ratio")
for k, lab in [("n_terr", "distinct territories"), ("moves", "moves (territory changes)"),
               ("n_afr_sub", "African sub-regions"), ("n_macro", "macro-regions of empire"),
               ("span", "career span (years)"), ("n_post", "postings recorded"),
               ("moves_per_decade", "moves per decade  *")]:
    a, b = med(top, k), med(oth, k)
    print(f"  {lab:26} {a:7.1f}   {b:7.1f}   {a/b if b else float('nan'):5.2f}x   (median)")
print("  * length-normalised: the key control")

# imperial reach
def imp(g): return 100*sum(1 for r in g if r["n_macro"] > 1)/len(g)
print(f"\nserved beyond Africa (>1 macro-region):  top {imp(top):.0f}%   rest {imp(oth):.0f}%")

# decomposition: pre-top mobility
pre = [r["moves_pre_top"] for r in top if r["moves_pre_top"] is not None]
print(f"\nDECOMPOSITION — among apex officials:")
print(f"  median moves BEFORE first reaching the top: {st.median(pre):.1f}")
print(f"  median moves TOTAL:                         {med(top,'moves'):.1f}")
print(f"  => roughly {100*st.median(pre)/max(med(top,'moves'),1):.0f}% of their moves precede the apex")
print(f"  non-top median moves (whole career):        {med(oth,'moves'):.1f}")

# length-matched comparison: within postings-count strata
print("\nLENGTH-MATCHED (compare within same # postings) — median moves:")
print(f"  {'#postings':10} {'top n':>6} {'top mv':>7} {'rest n':>7} {'rest mv':>8}")
for lo, hi in [(1,2),(3,4),(5,7),(8,50)]:
    ts = [r for r in top if lo <= r["n_post"] <= hi]
    os_ = [r for r in oth if lo <= r["n_post"] <= hi]
    if ts and os_:
        print(f"  {lo}-{hi:<7} {len(ts):>6} {med(ts,'moves'):>7.1f} {len(os_):>7} {med(os_,'moves'):>8.1f}")

with open("data/africa/top_officials.jsonl", "w") as f:
    for r in recs:
        f.write(json.dumps(r, ensure_ascii=False) + "\n")
print("\nwrote data/africa/top_officials.jsonl")
