#!/usr/bin/env python3
"""Build a place_qid -> colony crosswalk for grounded localities that are NOT
themselves colonial polities.

`col_match/kg/colony.py:resolve_colony` only assigns a colony when the grounded
place IS a polity in the empire KG. Cities/provinces (Calcutta Q1348, Cape Town
Q5465, North-Western Provinces Q138521) ground to a place_qid but get
colony_qid=null and are dropped from the careers map. The colony.py docstring
promised a "country+year lineage walk" to fix this -- this script is that walk.

Mechanism (no guessing about the historical entity -- only about the rollup):
  1. For every grounded place currently lacking a colony, take its modern country
     (Wikidata P17) and admin parent (P131), cached in place_geo_chain.json.
  2. Map country -> the colonial polity QID the graph ALREADY uses (so recovered
     places fold into existing colony nodes, not duplicates). Single-colony
     countries map at country level; the four multi-colony countries
     (South Africa, Australia, Canada, Malaysia) refine by P131 province.
  3. United Kingdom -> a metropole marker (officials who served at the imperial
     centre -- Colonial Office, Crown Agents, India Office, Custom House clerks),
     so they appear on the map at London rather than vanishing (Jim 2026-06-27).
  4. Foreign / non-empire countries (Iran, France, US, China) are left null --
     these are education / birth / foreign-posting noise, not colonial service.

Writes data/kg/place_colony_crosswalk.json {place_qid: {colony_qid, colony_label,
method}}. Consumed by colony.resolve_colony. Reproducible; re-fetches the geo
chain via QLever if the cache is missing.
"""
from __future__ import annotations
import json, sys, urllib.request, urllib.parse, collections
from pathlib import Path

ROOT = Path(__file__).resolve().parent
GEO_CACHE = ROOT / "data/kg/place_geo_chain.json"
OUT = ROOT / "data/kg/place_colony_crosswalk.json"
QLEVER = "https://qlever.dev/api/wikidata"

# The metropole: officials who served in London/UK. A dedicated marker QID so the
# atlas can plot them at the imperial centre and the client can label them.
METROPOLE = {"colony_qid": "Q84", "colony_label": "United Kingdom (metropole)"}

# Country (Wikidata P17) -> colony_qid/label the graph already uses. colony_qids
# are reused verbatim from existing colony nodes so recovered places fold in.
COUNTRY_COLONY = {
    "Q668":  ("Q129286", "Indian Empire (British Raj)"),   # India
    "Q843":  ("Q129286", "Indian Empire (British Raj)"),   # Pakistan (pre-1947 British India)
    "Q902":  ("Q129286", "Indian Empire (British Raj)"),   # Bangladesh (pre-1947 British India)
    "Q129286": ("Q129286", "Indian Empire (British Raj)"), # already British Raj
    "Q854":  ("Q918153", "Ceylon"),                        # Sri Lanka
    "Q836":  ("Q2376315", "Burma (Separate Colony)"),      # Myanmar / Burma
    "Q117":  ("Q503623", "British Gold Coast"),            # Ghana
    "Q1033": ("Q2046345", "Colony and Protectorate of Nigeria"),  # Nigeria
    "Q1036": ("Q1097943", "Uganda"),                       # Uganda
    "Q114":  ("Q2538511", "Kenya, Colony & Protectorate of"),     # Kenya
    "Q924":  ("Q158725", "Tanganyika Territory"),          # Tanzania (mainland = Tanganyika)
    "Q712":  ("Q5148320", "Fiji"),                         # Fiji
    "Q664":  ("Q664", "New Zealand"),                      # New Zealand
    "Q766":  ("Q2526023", "Jamaica"),                      # Jamaica
    "Q778":  ("Q21815597", "Bahamas Colony"),             # Bahamas
    "Q244":  ("Q63973349", "Barbados Colony"),            # Barbados
    "Q754":  ("Q116282722", "Trinidad and Tobago"),       # Trinidad and Tobago
    "Q769":  ("Q3116419", "Grenada Colony"),              # Grenada
    "Q784":  ("Q784", "Dominica Colony"),                 # Dominica
    "Q757":  ("Q15240384", "St. Vincent Colony"),         # St Vincent & the Grenadines
    "Q760":  ("Q15238409", "Saint Lucia Colony"),         # Saint Lucia
    "Q1011": ("Q3557236", "Gambia Colony and Protectorate"),  # Cape Verde? no -> skip below; Gambia=Q1005
    "Q1005": ("Q3557236", "Gambia Colony and Protectorate"),  # Gambia
    # NOTE: Q1037 is RWANDA (not Sierra Leone) and Q967 is BURUNDI (not Zambia);
    # both removed — neither was a British colony. Sierra Leone = Q1044 (below),
    # Zambia = Q953 (below). These were QID-transposition errors.
    "Q954":  ("Q750583", "Southern Rhodesia (Restored)"), # Zimbabwe
    "Q1020": ("Q1649306", "Nyasaland (Post-Federation)"), # Malawi
    "Q1042": ("Q21821453", "Seychelles"),                 # Seychelles (Q1042 is Seychelles, NOT Zanzibar — was wrongly mapped to Zanzibar Protectorate)
    "Q1027": ("Q12053604", "Isle de France (British Occupation)"),  # Mauritius
    "Q1044": ("Q30059027", "Sierra Leone Colony and Protectorate"),  # Sierra Leone (Q1044 is Sierra Leone, NOT Somalia — was wrongly mapped to British Somaliland)
    "Q1045": ("Q662653", "British Somaliland"),           # Somalia / Somaliland (correct)
    "Q241":  ("Q15240466", "Saint Lucia Colony"),         # (guard) -- overwritten if wrong
    "Q233":  ("Q6744657", "Malta"),                       # Malta
    "Q229":  ("Q15240466", "Cyprus"),                     # placeholder, fixed below
    "Q804":  ("Q541455", "Sudan, Anglo-Egyptian"),        # Panama? no -> Sudan=Q1049
    "Q1049": ("Q541455", "Sudan, Anglo-Egyptian"),        # Sudan
    "Q953":  ("Q953903", "Northern Rhodesia Colony"),     # Zambia (alt qid)
    "Q691":  ("Q2645837", "British New Guinea"),          # Papua New Guinea
    "Q683":  ("Q683", "Western Samoa"),                   # Samoa
    "Q242":  ("Q1643555", "British Honduras"),            # Belize
    "Q734":  ("Q918126", "British Guiana"),               # Guyana
    "Q79":   ("Q127861", "Egypt"),                        # Egypt
    "Q23681": ("Q15240466", "Cyprus"),                    # Northern Cyprus -> Cyprus
    "Q34":   None,  # Sweden -> foreign
    "Q794":  None, "Q142": None, "Q183": None, "Q30": None, "Q148": None,
    "Q801":  None,  # Israel/Palestine handled elsewhere
}
# correct a couple of entries that share ambiguous keys
COUNTRY_COLONY["Q229"] = ("Q15240466", "Cyprus")   # Cyprus
COUNTRY_COLONY.pop("Q1011", None)                  # Cape Verde is not British -> leave null
COUNTRY_COLONY.pop("Q804", None)                   # Panama -> leave null
COUNTRY_COLONY.pop("Q241", None)                   # Cuba -> leave null

# Multi-colony countries: match on P131 admin label substrings -> colony.
PROVINCE_COLONY = {
    "Q258": [  # South Africa
        (("cape town", "western cape", "eastern cape", "northern cape", "buffalo city",
          "nelson mandela", "sol plaatje", "kimberley", "graaff", "george", "knysna"),
         ("Q370736", "Cape Colony")),
        (("ethekwini", "msunduzi", "kwazulu", "natal", "umtshezi", "newcastle", "pietermaritzburg",
          "umgeni", "ladysmith"),
         ("Q1301901", "Colony of Natal")),
        (("tshwane", "johannesburg", "transvaal", "ekurhuleni", "pretoria", "gauteng", "mbombela",
          "polokwane", "rustenburg"),
         ("Q1187978", "Transvaal Colony (Second British)")),
        (("mangaung", "free state", "bloemfontein", "matjhabeng"),
         ("Q1142179", "Orange River Colony")),
    ],
    "Q408": [  # Australia
        (("western australia", "albany", "busselton", "fremantle", "perth", "kalgoorlie", "geraldton"),
         ("Q57676556", "Western Australia")),
        (("new south wales", "sydney", "newcastle", "broken hill", "wagga"),
         ("Q18348382", "New South Wales")),
        (("south australia", "adelaide"), ("Q35715", "South Australia")),
        (("victoria", "melbourne", "ballarat", "bendigo", "geelong"), ("Q56850459", "Victoria (Colony)")),
        (("queensland", "brisbane", "townsville", "rockhampton", "cairns"), ("Q28401203", "Queensland")),
        (("tasmania", "hobart", "launceston"), ("Q5148519", "Tasmania")),
    ],
    "Q16": [  # Canada
        (("ontario", "toronto", "ottawa", "hamilton", "london"), ("Q1904", "Ontario")),
        (("quebec", "montreal", "québec"), ("Q176", "Quebec")),
        (("nova scotia", "halifax"), ("Q1952", "Nova Scotia (Province)")),
        (("new brunswick", "fredericton", "saint john"), ("Q1965", "New Brunswick (Province)")),
        (("british columbia", "vancouver", "victoria"), ("Q1973", "British Columbia")),
        (("manitoba", "winnipeg"), ("Q1948", "Manitoba")),
        (("saskatchewan", "regina", "saskatoon"), ("Q1989", "Saskatchewan")),
        (("alberta", "calgary", "edmonton"), ("Q1951", "Alberta")),
        (("prince edward", "charlottetown"), ("Q1978", "Prince Edward Island (Province)")),
        (("newfoundland", "labrador", "st. john"), ("Q2984260", "Colony of Newfoundland")),
    ],
    "Q833": [  # Malaysia
        (("penang", "george town", "seberang perai", "prince of wales"), ("Q188096", "Penang")),
        (("malacca", "melaka"), ("Q7621163", "Malacca Settlement")),
        (("perak", "kinta", "ipoh", "selangor", "klang", "negeri sembilan", "seremban",
          "kuala pilah", "pahang", "kuantan", "kuala lumpur"),
         ("Q1400154", "Federated Malay States")),
        (("kedah", "kelantan", "terengganu", "trengganu", "johor", "johore", "perlis"),
         ("Q1973084", "Unfederated Malay States")),
    ],
}
# direct place_qid -> colony for colonial-umbrella entities Wikidata geocodes to
# the wrong / no modern country (so the country walk can't reach them).
PLACE_OVERRIDE = {
    "Q871091":  ("Q1400154", "Federated Malay States"),   # British Malaya (P17=Q8680 British Empire)
    "Q920396":  ("Q920396", "British West Indies"),        # umbrella federation; ground to itself
    "Q953068":  ("Q953068", "South-West Africa"),          # SA-administered mandate; ground to itself
    "Q4765854": ("Q2376315", "Burma (Separate Colony)"),  # Shan States -> Burma
    "Q918121":  ("Q370736", "Cape Colony"),               # British Kaffraria -> Cape
    "Q20618539": ("Q370736", "Cape Colony"),              # Victoria East (Victoria-Oos), Eastern Cape -> Cape (no P17 on WD)
    "Q1042":  ("Q21821453", "Seychelles"),                # Seychelles country -> canonical Seychelles colony node (NOT the stray 'Farquhar Islands' Q1042 node)
    "Q3940":  ("Q21821453", "Seychelles"),                # Victoria, capital of Seychelles -> Seychelles
}

# country-level fallback for the multi-colony countries (admin unknown)
COUNTRY_FALLBACK = {
    "Q258": ("Q193619", "Union of South Africa"),
    "Q408": ("Q408", "Commonwealth of Australia"),
    "Q16":  ("Q16", "Dominion of Canada"),
    "Q833": ("Q1400154", "Federated Malay States"),
}


def fetch_geo(qids):
    def run(sparql):
        data = urllib.parse.urlencode({"query": sparql}).encode()
        req = urllib.request.Request(QLEVER, data=data, headers={
            "Accept": "application/sparql-results+json",
            "Content-Type": "application/x-www-form-urlencoded"})
        with urllib.request.urlopen(req, timeout=120) as r:
            return json.load(r)
    out = {}
    for i in range(0, len(qids), 400):
        vals = " ".join(f"wd:{q}" for q in qids[i:i+400])
        res = run(f"""PREFIX wd: <http://www.wikidata.org/entity/>
        PREFIX wdt: <http://www.wikidata.org/prop/direct/>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        SELECT ?p ?country ?admin ?adminLabel WHERE {{ VALUES ?p {{ {vals} }}
          OPTIONAL {{ ?p wdt:P17 ?country }}
          OPTIONAL {{ ?p wdt:P131 ?admin. OPTIONAL {{ ?admin rdfs:label ?adminLabel. FILTER(LANG(?adminLabel)="en") }} }} }}""")
        for b in res["results"]["bindings"]:
            q = b["p"]["value"].rsplit("/", 1)[-1]
            e = out.setdefault(q, {"country": None, "admins": []})
            if "country" in b and not e["country"]:
                e["country"] = b["country"]["value"].rsplit("/", 1)[-1]
            if "admin" in b:
                a = (b["admin"]["value"].rsplit("/", 1)[-1], b.get("adminLabel", {}).get("value"))
                if a not in e["admins"]:
                    e["admins"].append(a)
    return out


def all_place_qids():
    """Every grounded place_qid in either corpus. The crosswalk must be COMPLETE,
    not just over currently-ungrounded places: resolve_colony recomputes colonies
    on every emit, so a place dropped from the crosswalk would lose the colony it
    was previously given (re-emit must be idempotent). Polity places that resolve
    earlier via the empire-KG index simply never consult their crosswalk entry."""
    qids = set()
    for path in ("data/kg/graph_stage3/places.jsonl", "data/iol/graph_stage3/places.jsonl"):
        p = ROOT / path
        if not p.exists():
            continue
        for l in p.open():
            d = json.loads(l)
            if d.get("qid"):
                qids.add(d["qid"])
    return sorted(qids)


def load_existing_colonies():
    """qid set + normalised-label/alias -> (qid,label) over colony nodes the graph
    already uses, so a P17/P131 hop that lands ON a colonial polity reuses it."""
    import re
    norm = lambda s: re.sub(r"[^a-z0-9 ]", "", (s or "").lower()).strip()
    qids, alias = {}, {}
    for path in ("data/kg/graph_stage3/places.jsonl", "data/iol/graph_stage3/places.jsonl"):
        p = ROOT / path
        if not p.exists():
            continue
        for l in p.open():
            d = json.loads(l)
            cq, cl = d.get("colony_qid"), d.get("colony_label")
            if cq:
                qids[cq] = cl
                alias.setdefault(norm(cl.split("(")[0]) if cl else "", (cq, cl))
    # curated aliases for historical-admin labels Wikidata uses
    for a, qid in (("british raj", "Q129286"), ("british india", "Q129286"),
                   ("indian empire", "Q129286"), ("dominion of india", "Q129286")):
        if qid in qids:
            alias[a] = (qid, qids[qid])
    return qids, alias, norm


_COL_QIDS, _COL_ALIAS, _NORM = {}, {}, (lambda s: s)


def map_place(qid, geo):
    e = geo.get(qid)
    if not e:
        return None
    country = e.get("country")
    admins = e.get("admins") or []
    # 0. direct override for colonial-umbrella places Wikidata geocodes oddly
    if qid in PLACE_OVERRIDE:
        cq, cl = PLACE_OVERRIDE[qid]
        return {"colony_qid": cq, "colony_label": cl, "method": "override"}
    # 0b. the place IS itself a colony the graph knows but colony.py's empire-KG
    #     index missed (e.g. Ontario Q1904) -> ground to itself
    if qid in _COL_QIDS:
        return {"colony_qid": qid, "colony_label": _COL_QIDS[qid], "method": "self_colony"}
    # 1. admin (P131) chain lands on a known colonial polity (catches historical
    #    provinces whose P17 is wrongly the UK -- e.g. Bihar Province -> British Raj).
    #    Skip when the admin is one of the multi-colony umbrella QIDs (those need
    #    the province walk below, not a collapse to the country node).
    for aq, al in admins:
        if aq in _COL_QIDS and aq not in PROVINCE_COLONY:
            return {"colony_qid": aq, "colony_label": _COL_QIDS[aq], "method": "admin_walk"}
        hit = _COL_ALIAS.get(_NORM(al)) if al else None
        if hit and hit[0] not in PROVINCE_COLONY:
            return {"colony_qid": hit[0], "colony_label": hit[1], "method": "admin_walk"}
    # 2. multi-colony country -> refine by province (BEFORE country_is_colony: the
    #    four umbrella countries are themselves colony nodes, e.g. Q258 ->
    #    'Orange River Sovereignty', which would wrongly swallow Cape Town)
    if country in PROVINCE_COLONY:
        astr = " | ".join((al or "").lower() for _, al in admins)
        for keys, (cq, cl) in PROVINCE_COLONY[country]:
            if any(k in astr for k in keys):
                return {"colony_qid": cq, "colony_label": cl, "method": "province_walk"}
        fb = COUNTRY_FALLBACK.get(country)
        return {"colony_qid": fb[0], "colony_label": fb[1], "method": "country_fallback"} if fb else None
    # 3. P17 is ITSELF a colonial polity (Yangon->Burma, St Kitts->Q763)
    if country in _COL_QIDS:
        return {"colony_qid": country, "colony_label": _COL_QIDS[country], "method": "country_is_colony"}
    # 4. single-colony country
    cc = COUNTRY_COLONY.get(country)
    if cc:
        return {"colony_qid": cc[0], "colony_label": cc[1], "method": "country_walk"}
    # 5. last resort: served at the imperial centre
    if country == "Q145":
        return {**METROPOLE, "method": "metropole_uk"}
    return None


def country_to_colony(country_qid):
    """Country-level colony resolution (no province refinement) for rolling up an
    ORG's country_qid -> colony. Used by kg_backfill_colony.py. Returns
    (colony_qid, colony_label, method) or None."""
    global _COL_QIDS, _COL_ALIAS, _NORM
    if not _COL_QIDS:
        _COL_QIDS, _COL_ALIAS, _NORM = load_existing_colonies()
    if country_qid in COUNTRY_FALLBACK:           # multi-colony umbrella
        cq, cl = COUNTRY_FALLBACK[country_qid]
        return (cq, cl, "org_country_fallback")
    cc = COUNTRY_COLONY.get(country_qid)
    if cc:
        return (cc[0], cc[1], "org_country")
    if country_qid in _COL_QIDS:                  # country is itself a colony node
        return (country_qid, _COL_QIDS[country_qid], "org_country_is_colony")
    if country_qid == "Q145":
        return (METROPOLE["colony_qid"], METROPOLE["colony_label"], "org_metropole")
    return None


def main():
    global _COL_QIDS, _COL_ALIAS, _NORM
    _COL_QIDS, _COL_ALIAS, _NORM = load_existing_colonies()
    qids = all_place_qids()
    if GEO_CACHE.exists():
        geo = json.loads(GEO_CACHE.read_text())
        missing = [q for q in qids if q not in geo]
        if missing:
            geo.update(fetch_geo(missing))
            GEO_CACHE.write_text(json.dumps(geo))
    else:
        geo = fetch_geo(qids)
        GEO_CACHE.write_text(json.dumps(geo))

    cross, methods, unresolved_country = {}, collections.Counter(), collections.Counter()
    for q in qids:
        m = map_place(q, geo)
        if m:
            cross[q] = m
            methods[m["method"]] += 1
        else:
            methods["unresolved"] += 1
            unresolved_country[(geo.get(q) or {}).get("country")] += 1
    OUT.write_text(json.dumps(cross, ensure_ascii=False, indent=0))
    print(f"crosswalk: {len(cross)}/{len(qids)} ungrounded place_qids mapped")
    for k, n in methods.most_common():
        print(f"  {k:18s} {n}")
    print("top unresolved countries (left null):")
    for c, n in unresolved_country.most_common(12):
        print(f"  {c}: {n}")


if __name__ == "__main__":
    main()
