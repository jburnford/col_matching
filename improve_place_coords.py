#!/usr/bin/env python3
"""Upgrade place coordinates from CENTROIDS to SEATS OF GOVERNMENT.

Officials were posted to a colony/presidency/province's capital, not its geographic
centre. For every place QID used in the atlas we resolve, in order of preference:
  1. its capital (Wikidata P36) -> that capital's coordinates (P625)   [the seat]
  2. a curated SEATS override (for historical entities WD lacks P36 for)
  3. the place's own P625                                              [centroid fallback]
  4. a curated centroid hand-fill                                      [last resort]

Writes docs/data/transfer_coords.json (qid -> [lat,lon]) and
docs/data/place_seats.json (qid -> seat label, for display). Prints a coverage
report so the centroid-fallbacks can be reviewed and promoted to SEATS."""
import json, urllib.request, urllib.parse
from pathlib import Path

OUT = Path("docs/data")
QLEVER = "https://qlever.dev/api/wikidata"

# curated administrative seats for historical entities (capital coord + label).
# Used as an override so we never fall back to a centroid for the major colonies.
SEATS = {
    "Q817165":  ([22.5726, 88.3639], "Calcutta"),       # Bengal Presidency
    "Q891827":  ([18.9667, 72.8333], "Bombay"),          # Bombay Presidency
    "Q1772596": ([13.0827, 80.2707], "Madras"),          # Madras Presidency
    "Q129286":  ([28.6139, 77.2090], "Delhi / Calcutta"),# Indian Empire (imperial capital)
    "Q2160037": ([26.8467, 80.9462], "Lucknow"),         # United Provinces
    "Q2629708": ([31.5497, 74.3436], "Lahore"),          # Punjab Province
    "Q7522091": ([24.8607, 67.0011], "Karachi"),         # Sind Province
    "Q17513379":([26.1445, 91.7362], "Shillong"),        # Assam Province
    "Q4907084": ([25.5941, 85.1376], "Patna"),           # Bihar and Orissa
    "Q4126447": ([21.1458, 79.0882], "Nagpur"),          # Central Provinces and Berar
    "Q2376315": ([16.8409, 96.1735], "Rangoon"),         # Burma
    "Q4412467": ([34.0151, 71.5249], "Peshawar"),        # North-West Frontier Province
    "Q843":     ([30.1798, 66.9750], "Quetta"),          # Baluchistan (Br. administered)
    "Q1240096": ([17.3850, 78.4867], "Hyderabad"),       # Hyderabad State
    "Q266923":  ([12.2958, 76.6394], "Mysore"),          # Kingdom of Mysore
    "Q2571484": ([34.0837, 74.7973], "Srinagar"),        # Jammu and Kashmir
    "Q205697":  ([23.0225, 72.5714], "Ahmedabad"),       # (Gujarat-area agency, if present)
    "Q17509767":([12.7794, 45.0367], "Aden"),            # Aden Province
    "Q15240466":([35.1856, 33.3823], "Nicosia"),         # Cyprus
    "Q24905912":([12.4244, 75.7382], "Madikeri"),        # Coorg
    "Q15630982":([20.4625, 85.8830], "Cuttack"),         # Orissa Tributary States
    "Q3243592": ([35.2061, 71.8765], "Dir"),             # Dir State
    "Q16":      ([45.4215, -75.6972], "Ottawa"),         # Canada
    # Caribbean / Atlantic / Pacific colonies WD lacks a coord-bearing P36 for
    "Q116282722":([10.6549, -61.5019], "Port of Spain"), # Trinidad and Tobago
    "Q130386222":([17.1211, -61.8447], "St John's"),     # Antigua Colony
    "Q3116419": ([12.0561, -61.7488], "St George's"),    # Grenada Colony
    "Q8646":    ([22.2810, 114.1583], "Victoria"),       # Hong Kong (City of Victoria)
    "Q21821453":([-4.6191, 55.4513],  "Victoria"),       # Seychelles
    "Q2566427": ([4.9589, 8.3269],    "Calabar"),        # Oil Rivers Protectorate
    "Q1937196": ([16.8409, 96.1735],  "Rangoon"),        # Lower Burma
    "Q3960459": ([27.3314, 88.6138],  "Gangtok"),        # Kingdom of Sikkim
    "Q509572":  ([26.3237, 89.4513],  "Cooch Behar"),    # Cooch Behar
    "Q4807130": ([-33.9249, 18.4241], "Cape Town"),      # Cape Colony (Dutch period)
    "Q3303188": ([30.1798, 66.9750],  "Quetta"),         # Baluchistan (alt QID)
    "Q3129772": ([54.1797, 7.8851],   "Heligoland"),     # Heligoland
    # colony entities (mostly from the 2026-06-27 reground) Wikidata lacks P36/P625 for
    "Q18348382": ([-33.8680, 151.2090], "Sydney"),       # New South Wales (colony)
    "Q28401203": ([-27.4680, 153.0280], "Brisbane"),     # Queensland (colony)
    "Q63973349": ([13.1070, -59.6130],  "Bridgetown"),   # Barbados
    "Q15240384": ([13.1570, -61.2250],  "Kingstown"),    # St Vincent
    "Q15238409": ([14.0110, -60.9870],  "Castries"),     # St Lucia
    "Q3574782":  ([-6.1650, 39.1990],   "Zanzibar"),     # Zanzibar Protectorate
    "Q21816225": ([26.2250, 50.5860],   "Manama"),       # Bahrain Protectorate
    "Q105633777":([25.2860, 51.5340],   "Doha"),         # Qatar Protectorate
    "Q1865132":  ([12.7900, 45.0200],   "Aden"),         # Aden Protectorate
    "Q6420545":  ([5.2810, 115.2410],   "Victoria, Labuan"),  # Labuan
    "Q7621163":  ([2.1960, 102.2490],   "Malacca"),      # Malacca Settlement
    "Q1973084":  ([5.0000, 102.5000],   "Unfederated Malay States"),
    "Q3593530":  ([-8.5200, 179.1980],  "Funafuti"),     # Ellice Islands
    "Q96372444": ([6.6880, -1.6240],    "Kumasi"),       # Ashanti
    "Q1806380":  ([7.8020, 6.7440],     "Lokoja"),       # Royal Niger Company
}

def qlever(query):
    data = urllib.parse.urlencode({"query": query}).encode()
    req = urllib.request.Request(QLEVER, data=data,
        headers={"Accept": "application/sparql-results+json",
                 "Content-Type": "application/x-www-form-urlencoded"})
    with urllib.request.urlopen(req, timeout=120) as r:
        return json.load(r)["results"]["bindings"]

def qid_of(uri): return uri.rsplit("/", 1)[-1]
def wkt_latlon(v):
    lon, lat = v.upper().replace("POINT(", "").replace(")", "").split()[:2]
    return [round(float(lat), 4), round(float(lon), 4)]

def capitals(qids):
    """place QID -> [capital QIDs] via P36."""
    out = {}
    for i in range(0, len(qids), 200):
        vals = " ".join(f"wd:{q}" for q in qids[i:i+200])
        rows = qlever("PREFIX wd: <http://www.wikidata.org/entity/>\n"
                      "PREFIX wdt: <http://www.wikidata.org/prop/direct/>\n"
                      f"SELECT ?p ?cap WHERE {{ VALUES ?p {{ {vals} }} ?p wdt:P36 ?cap . }}")
        for b in rows:
            out.setdefault(qid_of(b["p"]["value"]), []).append(qid_of(b["cap"]["value"]))
    return out

def coords_of(qids):
    out = {}
    for i in range(0, len(qids), 200):
        vals = " ".join(f"wd:{q}" for q in qids[i:i+200])
        rows = qlever("PREFIX wd: <http://www.wikidata.org/entity/>\n"
                      "PREFIX wdt: <http://www.wikidata.org/prop/direct/>\n"
                      f"SELECT ?i ?c WHERE {{ VALUES ?i {{ {vals} }} ?i wdt:P625 ?c . }}")
        for b in rows:
            q = qid_of(b["i"]["value"])
            if q not in out: out[q] = wkt_latlon(b["c"]["value"])
    return out

def labels_of(qids):
    out = {}
    for i in range(0, len(qids), 200):
        vals = " ".join(f"wd:{q}" for q in qids[i:i+200])
        rows = qlever("PREFIX wd: <http://www.wikidata.org/entity/>\n"
                      "PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>\n"
                      f"SELECT ?i ?l WHERE {{ VALUES ?i {{ {vals} }} ?i rdfs:label ?l . "
                      "FILTER(LANG(?l)='en') }")
        for b in rows:
            out[qid_of(b["i"]["value"])] = b["l"]["value"]
    return out

def country_labels(qids):
    """Of the given place QIDs, return {qid: canonical WD label} for those that are
    present-day sovereign countries. A colony grounded to a *country* QID means an
    over-collapse, and its colony_label is then an unreliable sub-region (China ->
    'Weihaiwei', USA -> 'Baker Island', Australia -> 'Queensland'); the country's
    own Wikidata name is the honest display label."""
    out = {}
    for i in range(0, len(qids), 200):
        vals = " ".join(f"wd:{q}" for q in qids[i:i+200])
        rows = qlever(
            "PREFIX wd: <http://www.wikidata.org/entity/>\n"
            "PREFIX wdt: <http://www.wikidata.org/prop/direct/>\n"
            "PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>\n"
            f"SELECT ?i ?l WHERE {{ VALUES ?i {{ {vals} }} "
            "?i wdt:P31 ?t . FILTER(?t IN (wd:Q3624078, wd:Q6256)) "   # sovereign state / country
            "?i rdfs:label ?l . FILTER(LANG(?l)='en') }")
        for b in rows:
            out[qid_of(b["i"]["value"])] = b["l"]["value"]
    return out

def resolve_seats(qids, labels=None):
    """qids -> ({qid:[lat,lon]} seat-preferred coords, {qid:seat label}, report, fallbacks).
    labels: optional {qid:label} for the fallback report only."""
    labels = labels or {}
    caps = capitals(qids)
    cap_qids = sorted({c for cs in caps.values() for c in cs})
    cap_coords = coords_of(cap_qids)
    cap_labels = labels_of(cap_qids)
    centroids = coords_of(qids)

    coords, seats, report, fallbacks = {}, {}, {"seat": 0, "override": 0, "centroid": 0, "handfill": 0}, []
    for q in qids:
        if q in SEATS:                                   # curated seat wins (historical gaps)
            coords[q], seats[q] = SEATS[q][0], SEATS[q][1]; report["override"] += 1; continue
        cap = next((c for c in caps.get(q, []) if c in cap_coords), None)
        if cap:
            coords[q] = cap_coords[cap]; seats[q] = cap_labels.get(cap, ""); report["seat"] += 1
        elif q in centroids:
            coords[q] = centroids[q]; report["centroid"] += 1; fallbacks.append((q, labels.get(q, q)))
        else:
            report["handfill"] += 1; fallbacks.append((q, labels.get(q, q) + " (NO COORD)"))
    return coords, seats, report, fallbacks

def main():
    places = json.load((OUT / "places.json").open())
    qids = sorted(places.keys())
    labels = {q: p["label"] for q, p in places.items()}
    print(f"resolving seats for {len(qids)} places…")
    coords, seats, report, fallbacks = resolve_seats(qids, labels)

    json.dump(coords, (OUT / "transfer_coords.json").open("w"))
    json.dump(seats, (OUT / "place_seats.json").open("w"), ensure_ascii=False)
    print(f"seats(P36)={report['seat']}  curated-seat={report['override']}  "
          f"centroid-fallback={report['centroid']}  no-coord={report['handfill']}")
    print(f"\ncentroid fallbacks ({len(fallbacks)}) — candidates to promote to SEATS, by traffic:")
    traf = {q: places[q]["co_in"]+places[q]["co_out"]+places[q]["io_in"]+places[q]["io_out"] for q, _ in fallbacks}
    for q, lab in sorted(fallbacks, key=lambda x: -traf.get(x[0], 0))[:30]:
        print(f"  {traf.get(q,0):5}  {q:12} {lab}")

if __name__ == "__main__":
    main()
