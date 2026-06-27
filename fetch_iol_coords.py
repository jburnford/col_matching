#!/usr/bin/env python3
"""Fetch P625 coordinates for the IOL transfer place QIDs from QLever.

Seeds from the existing CO transfer_coords cache (overlapping QIDs), then queries
QLever for the rest.  QLever is used for Wikidata coord lookups (WDQS times out on
batch VALUES queries).  Writes /tmp/iol_transfer_coords.json; prints the QIDs that
still lack coords so they can be hand-filled (historical presidencies/provinces
often have no P625)."""
import json, urllib.request, urllib.parse

QIDS = [q.strip() for q in open("/tmp/iol_transfer_qids.txt") if q.strip()]
coords = {}
# seed from the CO cache (presidencies/Burma/etc. may already be there)
try:
    coords.update(json.load(open("/tmp/transfer_coords.json")))
except FileNotFoundError:
    pass

need = [q for q in QIDS if q not in coords]
print(f"{len(QIDS)} QIDs, {len(QIDS)-len(need)} from CO cache, {len(need)} to fetch")

ENDPOINT = "https://qlever.dev/api/wikidata"
def qlever(query):
    data = urllib.parse.urlencode({"query": query}).encode()
    req = urllib.request.Request(ENDPOINT, data=data,
        headers={"Accept": "application/sparql-results+json",
                 "Content-Type": "application/x-www-form-urlencoded"})
    with urllib.request.urlopen(req, timeout=120) as r:
        return json.load(r)

# batch the VALUES query
for i in range(0, len(need), 200):
    batch = need[i:i+200]
    values = " ".join(f"wd:{q}" for q in batch)
    q = f"""
PREFIX wd: <http://www.wikidata.org/entity/>
PREFIX wdt: <http://www.wikidata.org/prop/direct/>
PREFIX geo: <http://www.opengis.net/ont/geosparql#>
SELECT ?item ?coord WHERE {{
  VALUES ?item {{ {values} }}
  ?item wdt:P625 ?coord .
}}"""
    res = qlever(q)
    for b in res["results"]["bindings"]:
        qid = b["item"]["value"].rsplit("/", 1)[-1]
        # WKT: "Point(lon lat)" (case varies); guard against multi-coord items
        if qid in coords:
            continue
        wkt = b["coord"]["value"].upper().replace("POINT(", "").replace(")", "")
        lon, lat = wkt.split()[:2]
        coords[qid] = [round(float(lat), 4), round(float(lon), 4)]

# hand-fill historical presidencies/provinces/states WDQS+QLever lack P625 for
coords.update({
    "Q15240466": [35.0, 33.0],     # Cyprus
    "Q15630982": [20.5, 84.5],     # Orissa Tributary States (Orissa region)
    "Q24905912": [12.42, 75.74],   # Coorg (Kodagu)
    "Q2629708":  [30.9, 74.6],     # Punjab Province (British India)
    "Q3243592":  [35.2, 71.88],    # Dir State (NWFP)
    "Q4412467":  [34.0, 71.5],     # North-West Frontier Province (Peshawar)
})

json.dump(coords, open("/tmp/iol_transfer_coords.json", "w"))
still = [q for q in QIDS if q not in coords]
print(f"resolved {len(QIDS)-len(still)}/{len(QIDS)}")
if still:
    labels = json.load(open("/tmp/iol_transfers.json"))["labels"]
    print("MISSING (need hand-fill):")
    for q in still:
        print(f"  {q}  {labels.get(q,'?')}")
