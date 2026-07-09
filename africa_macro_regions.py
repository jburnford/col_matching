#!/usr/bin/env python3
"""Map any colony QID -> a macro-region of empire, for the 'regional expertise vs
global experience' analysis. African territories keep their sub-region (from the
curated manifest); everything else is boxed by coordinates with a few overrides.
Importable: region_of(qid) -> macro label; AFRICA_REGIONS set.
"""
import json

TERR = json.load(open("data/africa/africa_territories.json"))
_PLACES = json.load(open("docs/data/places.json"))
AFRICA_SUB = {q: "AF:" + TERR[q]["region"] for q in TERR}       # AF:West, AF:East, ...
AFRICA_REGIONS = set(AFRICA_SUB.values())

_OVERRIDE = {"Q84": "UK"}                                         # metropole

def region_of(qid, coarse=False):
    """coarse=True collapses all African sub-regions to 'Africa'."""
    if qid in AFRICA_SUB:
        return "Africa" if coarse else AFRICA_SUB[qid]
    if qid in _OVERRIDE:
        return _OVERRIDE[qid]
    p = _PLACES.get(qid, {})
    lat, lon = p.get("lat"), p.get("lon")
    if lat is None or lon is None:
        return "Other/unknown"
    # boxes (lon, lat)
    if lat > 24 and lon < -50:                       return "NorthAmerica"
    if 4 <= lat <= 27 and -92 <= lon <= -55:          return "Caribbean"       # W.Indies+Guiana+Honduras
    if 5 <= lat <= 37 and 60 <= lon <= 92:            return "SouthAsia"       # India, Ceylon
    if -12 <= lat <= 40 and 92 < lon <= 122:          return "SEAsia"          # Straits, Burma, HK, Borneo
    if lat < -9 and 112 <= lon <= 180:                return "Australasia"     # Australia, NZ, Pacific
    if 34 <= lat <= 40 and -7 <= lon <= 36:           return "Mediterranean"   # Malta, Gibraltar, Cyprus
    if 11 <= lat <= 40 and 34 <= lon <= 60:           return "MiddleEast"      # Aden, Palestine, Iraq, Gulf
    return "Other/unknown"

if __name__ == "__main__":
    import collections
    cnt = collections.Counter()
    lab = {}
    for corp in ("data/kg", "data/iol"):
        for l in open(corp + "/graph_stage3/career_facts.jsonl"):
            r = json.loads(l); q = r.get("colony_qid")
            if q:
                cnt[q] += 1; lab[q] = r.get("colony_label")
    byreg = collections.defaultdict(list)
    for q, n in cnt.items():
        byreg[region_of(q)].append((n, lab.get(q, q)))
    for reg in sorted(byreg, key=lambda r: -sum(n for n, _ in byreg[r])):
        tot = sum(n for n, _ in byreg[reg])
        top = ", ".join(f"{l}" for _, l in sorted(byreg[reg], reverse=True)[:8])
        print(f"{reg:16} {tot:7,}  ({len(byreg[reg])} territories)  e.g. {top}")
