#!/usr/bin/env python3
"""Verify every place QID in a grounding cache against live Wikidata (WDQS).

For each distinct QID we fetch instance-of (P31), country (P17) and whether it
carries coordinates (P625), then classify:

  OK        - has >=1 P31 whose type is (a subclass* of) a geographic root
  NONPLACE  - resolves and has P31, but NONE of its types are geographic
              (e.g. a person/family-name/genus/painting was grounded by mistake)
  STUB      - resolves but has no P31 at all (statement-less item, redirect, or
              deleted QID) -> unverifiable, treat as a FP risk
  (items are mapped back to their surface place(s) + match_type for triage)

Verification is read-only SPARQL; this is the sanctioned way to validate KNOWN
QIDs (the REST search ban is about *disambiguation*, not lookup).

Usage:
  python3 verify_place_qids.py [cache.jsonl]   # default data/kg/places_grounding.jsonl
Outputs:
  data/kg/qid_verification_report.jsonl   # one row per distinct QID
  data/kg/qid_verification_flagged.jsonl  # NONPLACE + STUB only (for review)
"""
import json, sys, time, subprocess, collections, urllib.parse

CACHE = sys.argv[1] if len(sys.argv) > 1 else "data/kg/places_grounding.jsonl"
REPORT = "data/kg/qid_verification_report.jsonl"
FLAGGED = "data/kg/qid_verification_flagged.jsonl"
WDQS = "https://query.wikidata.org/sparql"
UA = "col_matching-qid-verify/1.0 (cljim22@gmail.com)"

# geographic roots: a P31 type counts as a place if it is a subclass* of any of these
GEO_ROOTS = [
    "Q2221906",  # geographic location
    "Q56061",    # administrative territorial entity
    "Q82794",    # geographic region
    "Q6256",     # country
    "Q3624078",  # sovereign state
    "Q618123",   # geographical feature
    "Q271669",   # landform
    "Q486972",   # human settlement
    "Q15916867", # historical country? (kept; harmless if absent)
    "Q133156",   # colony
    "Q164142",   # protectorate
    "Q3024240",  # historical country
]

def sparql(query):
    out = subprocess.run(
        ["curl", "-s", "-G", WDQS,
         "--data-urlencode", "query=" + query,
         "-H", "Accept: application/sparql-results+json",
         "-H", "User-Agent: " + UA],
        capture_output=True, text=True, timeout=90).stdout
    return json.loads(out)["results"]["bindings"]

def qid(uri):
    return uri.rsplit("/", 1)[-1] if uri else None

def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i+n]

# --- load cache: qid -> [(place, match_type), ...] ---
rows = [json.loads(l) for l in open(CACHE)]
qmap = collections.defaultdict(list)
for r in rows:
    if r.get("qid"):
        qmap[r["qid"]].append((r.get("place"), r.get("match_type")))
qids = sorted(qmap)
print(f"distinct QIDs to verify: {len(qids)}", file=sys.stderr)

# --- stage 1: per-item P31 / country / coord ---
item_p31 = collections.defaultdict(set)
item_country = collections.defaultdict(set)
item_coord = collections.defaultdict(bool)
seen_rows = collections.Counter()
for ci, ch in enumerate(chunks(qids, 150)):
    vals = " ".join("wd:" + q for q in ch)
    q = (f"SELECT ?item ?p31 ?country (BOUND(?coord) AS ?hc) WHERE {{ "
         f"VALUES ?item {{ {vals} }} "
         f"OPTIONAL {{ ?item wdt:P31 ?p31 }} "
         f"OPTIONAL {{ ?item wdt:P17 ?country }} "
         f"OPTIONAL {{ ?item wdt:P625 ?coord }} }}")
    for b in sparql(q):
        it = qid(b["item"]["value"]); seen_rows[it] += 1
        if "p31" in b: item_p31[it].add(qid(b["p31"]["value"]))
        if "country" in b: item_country[it].add(qid(b["country"]["value"]))
        if b.get("hc", {}).get("value") == "true": item_coord[it] = True
    print(f"  stage1 chunk {ci+1}: cumulative items seen {len(seen_rows)}", file=sys.stderr)
    time.sleep(1)

# --- stage 2: classify the distinct P31 types as geographic or not ---
all_types = sorted({t for s in item_p31.values() for t in s})
type_geo = {}
type_label = {}
for ch in chunks(all_types, 150):
    vals = " ".join("wd:" + t for t in ch)
    roots = " ".join("wd:" + r for r in GEO_ROOTS)
    q = (f"SELECT ?type ?typeLabel (BOUND(?g) AS ?isgeo) WHERE {{ "
         f"VALUES ?type {{ {vals} }} "
         f"OPTIONAL {{ ?type wdt:P279* ?g. VALUES ?g {{ {roots} }} }} "
         f"SERVICE wikibase:label {{ bd:serviceParam wikibase:language 'en'. }} }}")
    for b in sparql(q):
        t = qid(b["type"]["value"])
        if b.get("isgeo", {}).get("value") == "true": type_geo[t] = True
        else: type_geo.setdefault(t, False)
        type_label[t] = b.get("typeLabel", {}).get("value", t)
    time.sleep(1)

# --- classify each item ---
report, flagged = [], []
status_ct = collections.Counter()
for q in qids:
    p31s = item_p31.get(q, set())
    has_coord = item_coord.get(q, False)
    if any(type_geo.get(t) for t in p31s):
        status = "OK"
    elif p31s:
        status = "NONPLACE"                   # has P31 but NONE geographic -> likely wrong entity
                                              # (coords do NOT rescue: events carry coords too)
    elif has_coord:
        status = "OK_COORDS"                  # no P31 at all but carries coordinates -> real geo point
    else:
        status = "STUB"                       # no instance-of, no coords (stub/redirect/deleted)
    status_ct[status] += 1
    places = sorted({p for p, _ in qmap[q] if p})
    mtypes = sorted({m for _, m in qmap[q] if m})
    rec = {"qid": q, "status": status,
           "instance_of": sorted(p31s),
           "instance_of_labels": [type_label.get(t, t) for t in sorted(p31s)],
           "country": sorted(item_country.get(q, set())),
           "has_coords": item_coord.get(q, False),
           "n_surfaces": len(places), "surfaces": places[:8], "match_types": mtypes}
    report.append(rec)
    if status not in ("OK", "OK_COORDS"):
        flagged.append(rec)

with open(REPORT, "w") as f:
    for r in report: f.write(json.dumps(r, ensure_ascii=False) + "\n")
with open(FLAGGED, "w") as f:
    for r in flagged: f.write(json.dumps(r, ensure_ascii=False) + "\n")

print("\n=== QID verification summary ===")
print("distinct QIDs:", len(qids), "| by status:", dict(status_ct))
# how many SURFACE rows ride on flagged QIDs (impact)
flag_qids = {r["qid"] for r in flagged}
impact = sum(1 for r in rows if r.get("qid") in flag_qids)
print(f"surface rows on flagged QIDs: {impact}")
print(f"report  -> {REPORT}")
print(f"flagged -> {FLAGGED}  ({len(flagged)} QIDs)")
# show distinct non-geo P31 types that triggered NONPLACE, for eyeballing false negatives
nonplace_types = collections.Counter()
for r in flagged:
    if r["status"] == "NONPLACE":
        for t, lab in zip(r["instance_of"], r["instance_of_labels"]):
            if not type_geo.get(t): nonplace_types[lab] += 1
if nonplace_types:
    print("non-geographic P31 types seen on NONPLACE items:", dict(nonplace_types))
