#!/usr/bin/env python3
"""Where else did British-Africa officials serve? Regional expertise vs global
experience, and how it changes over time.

For every official with >=1 African appointment, use the FULL career (all colony
stints across the empire) to compute:
  - macro-regions of empire touched (Africa collapsed + non-African regions)
  - a career typology: single-territory / regional specialist / pan-African /
    imperial (also served outside Africa)
  - a specialization index = share of postings in the single modal macro-region
  - which non-African regions the 'imperial' careers reached (Singapore/SE Asia,
    Ceylon/South Asia, Canada/N. America, Caribbean, ...)
  - the same, split by cohort (decade of first appointment) -> temporal trend
"""
import json, statistics as st
from collections import Counter, defaultdict
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
from africa_macro_regions import region_of, AFRICA_REGIONS

careers = json.load(open("docs/data/careers.json"))["persons"]
AFR_SUB = AFRICA_REGIONS

rows = []
for pid, p in careers.items():
    stints = [s for s in p.get("st", []) if s[0]]
    macros = [region_of(s[0]) for s in stints]                    # sub-region for Africa
    afr_sub = {m for m in macros if m in AFR_SUB}
    if not afr_sub:
        continue
    nonafr = {m for m in macros if m not in AFR_SUB and m != "Other/unknown"}
    afr_terr = {s[0] for s in stints if region_of(s[0]) in AFR_SUB}
    coarse = [region_of(s[0], coarse=True) for s in stints]        # Africa + non-afr
    modal_share = Counter(coarse).most_common(1)[0][1] / len(coarse)
    first_year = min((s[1] for s in stints if s[1] is not None), default=None)
    if not nonafr:
        typ = "single-territory" if len(afr_terr) == 1 else \
              ("regional" if len(afr_sub) == 1 else "pan-African")
    else:
        typ = "imperial"
    rows.append({"pid": pid, "type": typ, "afr_regions": sorted(afr_sub),
                 "nonafr_regions": sorted(nonafr), "n_afr_terr": len(afr_terr),
                 "n_postings": len(stints), "modal_share": modal_share,
                 "first_year": first_year})

N = len(rows)
print("=" * 64)
print(f"WHERE ELSE DID BRITISH-AFRICA OFFICIALS SERVE?  (N={N:,})")
print("=" * 64)

# --- typology
typ_c = Counter(r["type"] for r in rows)
print("\nCAREER TYPOLOGY:")
for t in ("single-territory", "regional", "pan-African", "imperial"):
    print(f"  {t:16} {typ_c[t]:6,}  ({100*typ_c[t]/N:4.1f}%)")
afr_only = N - typ_c["imperial"]
print(f"  --> Africa-only: {afr_only:,} ({100*afr_only/N:.1f}%)   "
      f"served beyond Africa: {typ_c['imperial']:,} ({100*typ_c['imperial']/N:.1f}%)")

# --- regional expertise vs global experience (specialization index)
spec = [r["modal_share"] for r in rows]
print(f"\nSPECIALIZATION INDEX (share of career in modal macro-region):")
print(f"  median {st.median(spec):.2f}   mean {st.mean(spec):.2f}")
print(f"  fully specialised (100% one region): {100*sum(1 for s in spec if s==1)/N:.0f}%")
print(f"  highly mobile (<50% in any one region): {100*sum(1 for s in spec if s<0.5)/N:.0f}%")

# --- among imperial: where else?
elsewhere = Counter()
for r in rows:
    for m in r["nonafr_regions"]:
        elsewhere[m] += 1
print(f"\nAMONG THE {typ_c['imperial']:,} IMPERIAL CAREERS — other regions served"
      f" (% of all African officials):")
for m, c in elsewhere.most_common():
    print(f"  {m:14} {c:5,}  ({100*c/N:4.1f}% of all African officials)")

# --- how many African regions do the pan-African/imperial reach?
multi = Counter(len(r["afr_regions"]) for r in rows)
print("\nHOW MANY AFRICAN SUB-REGIONS PER CAREER:")
for k in sorted(multi):
    print(f"  {k} region(s): {multi[k]:6,} ({100*multi[k]/N:4.1f}%)")

# --- temporal: cohort by decade of first appointment
print("\nTEMPORAL TREND (by decade of FIRST appointment):")
print(f"  {'decade':7} {'N':>5} {'single':>7} {'region':>7} {'pan-Af':>7} {'imper':>7} {'spec':>5}")
dec_rows = defaultdict(list)
for r in rows:
    if r["first_year"]:
        dec_rows[(r["first_year"] // 10) * 10].append(r)
temporal = []
for dec in sorted(dec_rows):
    g = dec_rows[dec]
    if len(g) < 40:
        continue
    tc = Counter(r["type"] for r in g); n = len(g)
    sh = {t: tc[t] / n for t in ("single-territory", "regional", "pan-African", "imperial")}
    spec_m = st.mean(r["modal_share"] for r in g)
    temporal.append((dec, n, sh, spec_m))
    print(f"  {dec:5}s {n:5} {sh['single-territory']:6.0%} {sh['regional']:6.0%} "
          f"{sh['pan-African']:6.0%} {sh['imperial']:6.0%} {spec_m:5.2f}")

# --- figures
fig, ax = plt.subplots(figsize=(9, 5))
decs = [t[0] for t in temporal]
for typ, col in [("single-territory", "#bab0ac"), ("regional", "#4e79a7"),
                 ("pan-African", "#59a14f"), ("imperial", "#e15759")]:
    ax.plot(decs, [t[2][typ] for t in temporal], marker="o", label=typ, color=col)
ax.set_xlabel("decade of first appointment"); ax.set_ylabel("share of cohort")
ax.set_title("British-Africa career types over time"); ax.legend()
plt.tight_layout(); plt.savefig("data/africa/figs/career_types_over_time.png", dpi=140); plt.close()

fig, ax = plt.subplots(figsize=(7, 4))
top = elsewhere.most_common(8)
ax.barh([m for m, _ in top][::-1], [100*c/N for _, c in top][::-1], color="#4e79a7")
ax.set_xlabel("% of African officials who also served there")
ax.set_title("Where else British-Africa officials served")
plt.tight_layout(); plt.savefig("data/africa/figs/where_else.png", dpi=140); plt.close()

with open("data/africa/career_geography.jsonl", "w") as f:
    for r in rows:
        f.write(json.dumps(r, ensure_ascii=False) + "\n")
print("\nwrote data/africa/career_geography.jsonl + figs/{career_types_over_time,where_else}.png")
