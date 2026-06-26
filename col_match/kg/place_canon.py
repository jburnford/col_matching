"""Canonicalisation of printed colonial place abbreviations before Wikidata
grounding.

The Colonial Office Lists abbreviate territory names heavily and inconsistently
(``Nig.``, ``Ken.``, ``F.M.S.``, ``N. Rhod.``, ``H.K.``, ``S'pore``). Sent to a
vector search verbatim these short, ambiguous strings mis-ground badly. This
module maps the high-frequency printed forms to a single canonical search string
per territory so that (a) the MCP query is unambiguous and (b) the many surface
variants of one place collapse to one lookup / one QID.

Two public helpers:
- ``canonicalize(place)`` -> best MCP search string for a printed place value.
- ``is_institution(place)`` -> (flag, reason) for office/department/court values
  the structurer mislabelled as a place (they are NOT geographic; flag, never
  ground).

Conservative by design: only forms we are confident about are mapped. Genuinely
ambiguous initialisms (``S.A.`` South Africa vs South Australia, ``W.A.`` West
Africa vs Western Australia) are left untouched rather than guessed.
"""
from __future__ import annotations

import re


def canon_key(s: str) -> str:
    """Normalise a place fragment to a lookup key: lowercase, drop dots and
    apostrophes, collapse whitespace. ``F.M.S.`` -> ``fms``; ``N. Rhod.`` ->
    ``n rhod``; ``S'pore`` -> ``spore``."""
    s = s.lower().replace("'", "").replace("’", "")
    s = s.replace(".", "").replace("-", " ")
    return re.sub(r"\s+", " ", s).strip()


# Canonical territory map, keyed by canon_key(printed form) -> search string.
# Every printed variant of a territory points at the SAME canonical name so the
# grounding cache collapses them to one QID. Organised by region.
_TERRITORY = {
    # --- West Africa ---
    "nig": "Nigeria", "nigeria": "Nigeria", "fed of nig": "Nigeria",
    "n nig": "Northern Nigeria", "n nigeria": "Northern Nigeria",
    "s nig": "Southern Nigeria", "s nigeria": "Southern Nigeria",
    "so nig": "Southern Nigeria", "so nigeria": "Southern Nigeria",
    "w nig": "Western Region Nigeria", "e nig": "Eastern Region Nigeria",
    "n c protectorate now s nigeria": "Southern Nigeria",
    "gc": "Gold Coast", "g coast": "Gold Coast", "gold coast": "Gold Coast",
    "g coast colonial": "Gold Coast",
    "s leone": "Sierra Leone", "sl": "Sierra Leone", "sierra leone": "Sierra Leone",
    "gam": "Gambia", "gamb": "Gambia", "gambia": "Gambia",
    "lagos": "Lagos",
    "w africa": "British West Africa", "w indies": "West Indies",
    # --- East / Central / Southern Africa ---
    "ken": "Kenya", "kenya": "Kenya",
    "eap": "East Africa Protectorate", "e africa protectorate": "East Africa Protectorate",
    "e africa prot": "East Africa Protectorate",
    "uga": "Uganda", "uganda": "Uganda",
    "tang": "Tanganyika", "tt": "Tanganyika", "tanganyika admnstn": "Tanganyika",
    "zanz": "Zanzibar",
    "nyasa": "Nyasaland", "nyas": "Nyasaland", "nyasaland": "Nyasaland",
    "n rhod": "Northern Rhodesia", "n rhodesia": "Northern Rhodesia",
    "ne rhodesia": "Northern Rhodesia", "n e rhodesia": "Northern Rhodesia",
    "nw rhodesia": "Northern Rhodesia",
    "s rhod": "Southern Rhodesia", "s rhodesia": "Southern Rhodesia",
    "bech": "Bechuanaland", "bech protectorate": "Bechuanaland",
    "basuto": "Basutoland",
    "swaz": "Swaziland",
    "som": "Somaliland",
    "e africa": "East Africa", "ea": "East Africa",
    "gea": "German East Africa", "g e a": "German East Africa",
    "german e africa": "German East Africa",
    "bc africa": "British Central Africa", "b c africa": "British Central Africa",
    "bca protectorate": "British Central Africa",
    "br cent africa protectorate": "British Central Africa",
    "b cent africa protectorate": "British Central Africa",
    "sw africa": "South West Africa", "german sw africa": "German South West Africa",
    # --- South Africa (the provinces; the bare Union forms) ---
    "natal": "Natal", "transvaal": "Transvaal",
    "orc": "Orange River Colony", "ofs": "Orange Free State",
    "cape": "Cape Colony", "cape prov": "Cape Province",
    "union of s africa": "South Africa", "union of sa": "South Africa",
    "s africa": "South Africa",
    "c of gh": "Cape of Good Hope", "c of good hope": "Cape of Good Hope",
    "cape of good hope": "Cape of Good Hope",
    # --- Malaya / SE Asia ---
    "fms": "Federated Malay States", "f m s": "Federated Malay States",
    "ss": "Straits Settlements", "s s": "Straits Settlements",
    "s sttlmts": "Straits Settlements", "s sttlnts": "Straits Settlements",
    "s stlmts": "Straits Settlements", "s settlmts": "Straits Settlements",
    "s settlements": "Straits Settlements",
    "mal": "Malaya", "malaya": "Malaya",
    "fed of mal": "Federation of Malaya",
    "spore": "Singapore", "sing": "Singapore", "singapore": "Singapore",
    "penang": "Penang", "prov wellesley": "Province Wellesley",
    "perak": "Perak", "selangor": "Selangor", "pahang": "Pahang",
    "n sembilan": "Negeri Sembilan", "johore": "Johore", "kedah": "Kedah",
    "perlis": "Perlis", "k lumpur": "Kuala Lumpur",
    "s wak": "Sarawak", "swak": "Sarawak", "sar": "Sarawak",
    "n borneo": "North Borneo", "br n borneo": "North Borneo",
    "br north borneo": "North Borneo", "labuan": "Labuan", "brunei": "Brunei",
    "br new guinea": "British New Guinea", "br n guinea": "British New Guinea",
    "se asia": "South East Asia",
    # --- Ceylon (places stay distinct; kachcheris keep their town) ---
    "cey": "Ceylon", "ceylon": "Ceylon",
    # --- India (presidencies, provinces, agencies; India Office List) ---
    # Presidencies / major provinces of British India 1886-1947.
    "burma": "Burma", "bengal": "Bengal", "madras": "Madras",
    "bombay": "Bombay", "punjab": "Punjab",
    "e bengal": "Eastern Bengal", "e bengal and assam": "Eastern Bengal and Assam",
    "united provs": "United Provinces", "united provinces": "United Provinces",
    "u provs": "United Provinces", "up": "United Provinces",
    "united provinces of agra and oudh": "United Provinces",
    "central provs": "Central Provinces", "central provinces": "Central Provinces",
    "central provinces and berar": "Central Provinces and Berar",
    "bihar and orissa": "Bihar and Orissa", "bihar": "Bihar", "orissa": "Orissa",
    "assam": "Assam", "sind": "Sind", "sindh": "Sind", "berar": "Berar",
    "coorg": "Coorg", "baluchistan": "Baluchistan", "delhi": "Delhi",
    "ajmer": "Ajmer-Merwara", "ajmer merwara": "Ajmer-Merwara",
    "nwfp": "North-West Frontier Province", "n w f p": "North-West Frontier Province",
    "n w frontier province": "North-West Frontier Province",
    "north west frontier province": "North-West Frontier Province",
    # Agencies / residencies and the larger princely states.
    "rajputana": "Rajputana", "central india": "Central India Agency",
    "hyderabad": "Hyderabad State", "mysore": "Mysore", "baroda": "Baroda",
    "gwalior": "Gwalior", "kashmir": "Jammu and Kashmir",
    "jammu and kashmir": "Jammu and Kashmir", "travancore": "Travancore",
    "cochin": "Cochin", "indore": "Indore", "bhopal": "Bhopal State",
    "kolhapur": "Kolhapur", "kathiawar": "Kathiawar",
    # High-frequency stations whose OCR/old spelling needs steering to the QID.
    "calcutta": "Calcutta", "rangoon": "Rangoon", "karachi": "Karachi",
    "cawnpore": "Kanpur", "lahore": "Lahore", "simla": "Simla",
    # --- China coast / HK / Malaya tail ---
    "hk": "Hong Kong", "h kong": "Hong Kong", "hong kong": "Hong Kong",
    "kowloon": "Kowloon",
    "fed of mal states": "Federation of Malaya",
    # --- Mediterranean / Near East ---
    "malta": "Malta", "gozo": "Gozo", "cyp": "Cyprus", "cyprus": "Cyprus",
    "gib": "Gibraltar",
    "pal": "Palestine", "palestine": "Palestine",
    "aden": "Aden", "e aden protectorate": "Eastern Aden Protectorate",
    "w aden protectorate": "Western Aden Protectorate",
    "iraq": "Iraq", "soudan": "Sudan", "sudan": "Sudan", "egypt": "Egypt",
    # --- Caribbean / Atlantic ---
    "trin": "Trinidad", "tdad": "Trinidad", "trinidad": "Trinidad",
    "trin and tob": "Trinidad and Tobago", "tobago": "Tobago",
    "jca": "Jamaica", "jam": "Jamaica", "jamaica": "Jamaica",
    "barb": "Barbados", "barbados": "Barbados",
    "b guiana": "British Guiana", "br guiana": "British Guiana",
    "brit guiana": "British Guiana", "british guiana": "British Guiana",
    "bg": "British Guiana", "guiana": "British Guiana",
    "b hond": "British Honduras", "br hond": "British Honduras",
    "b honduras": "British Honduras", "br honduras": "British Honduras",
    "brit honduras": "British Honduras", "belize": "Belize",
    "st vincent": "Saint Vincent", "st v": "Saint Vincent",
    "st lucia": "Saint Lucia", "st l": "Saint Lucia",
    "st kitts": "Saint Kitts", "st k": "Saint Kitts", "st kitt s": "Saint Kitts",
    "st christopher": "Saint Kitts", "st kitts nevis": "Saint Kitts and Nevis",
    "st k n": "Saint Kitts and Nevis", "st kitts and nevis": "Saint Kitts and Nevis",
    "nevis": "Nevis", "gren": "Grenada", "grenada": "Grenada",
    "dom": "Dominica", "dominica": "Dominica",
    "bah": "Bahamas", "bahamas": "Bahamas", "nassau": "Nassau",
    "berm": "Bermuda", "bermuda": "Bermuda",
    "leeward is": "Leeward Islands", "leeward islds": "Leeward Islands",
    "windward is": "Windward Islands", "wind is": "Windward Islands",
    "virgin is": "Virgin Islands", "cayman is": "Cayman Islands",
    "turks is": "Turks and Caicos Islands",
    "turks and caicos is": "Turks and Caicos Islands",
    "turks and caicos islds": "Turks and Caicos Islands",
    "bwi": "British West Indies", "wi": "West Indies",
    "st helena": "Saint Helena", "st h": "Saint Helena",
    "falkland is": "Falkland Islands", "falkland islds": "Falkland Islands",
    "falk is": "Falkland Islands",
    # --- Pacific ---
    "fiji": "Fiji", "tonga": "Tonga", "samoa": "Samoa", "papua": "Papua",
    "w pacific": "Western Pacific", "w pac": "Western Pacific",
    "bsip": "British Solomon Islands Protectorate",
    "b sol is protectorate": "British Solomon Islands Protectorate",
    "br solomon is protectorate": "British Solomon Islands Protectorate",
    "b sol is": "British Solomon Islands Protectorate",
    "gilbert and ellice is": "Gilbert and Ellice Islands",
    "g and eic": "Gilbert and Ellice Islands", "g & eic": "Gilbert and Ellice Islands",
    "g & e is": "Gilbert and Ellice Islands", "gilbert and ellice islands": "Gilbert and Ellice Islands",
    "n heb": "New Hebrides", "n hebs": "New Hebrides",
    "christmas is": "Christmas Island",
    # --- Mauritius / Indian Ocean ---
    "maur": "Mauritius", "mauritius": "Mauritius",
    "sey": "Seychelles", "seychelles": "Seychelles",
    # --- Canada ---
    "can": "Canada", "canada": "Canada",
    "b columbia": "British Columbia", "br columbia": "British Columbia",
    "bc": "British Columbia",
    "n brunswick": "New Brunswick", "nb": "New Brunswick",
    "newfndld": "Newfoundland", "newfoundland": "Newfoundland",
    "pei": "Prince Edward Island", "pe is": "Prince Edward Island",
    "nwt": "Northwest Territories", "sask": "Saskatchewan", "ont": "Ontario",
    "quebec": "Quebec",
    # --- Australia / NZ ---
    "ns wales": "New South Wales", "nsw": "New South Wales",
    "new s wales": "New South Wales",
    "w australia": "Western Australia", "w aust": "Western Australia",
    "w austral": "Western Australia",
    "s australia": "South Australia", "s aust": "South Australia",
    "s austral": "South Australia", "s austr": "South Australia",
    "n territory": "Northern Territory", "n territories": "Northern Territory",
    "commonwealth of aust": "Australia", "c of aust": "Australia",
    "c of a": "Australia",
    "nz": "New Zealand", "n zealand": "New Zealand",
    # --- British Isles / Europe ---
    # --- spacing variants of forms already mapped (single-letter initials split
    #     by spaces survive canon_key, so map them explicitly) ---
    "n s wales": "New South Wales", "s w africa": "South West Africa",
    "b n borneo": "North Borneo", "n w rhodesia": "Northern Rhodesia",
    "n e rhodesia": "Northern Rhodesia", "b e africa": "British East Africa",
    "b c africa": "British Central Africa", "g c colony": "Gold Coast",
    "s a republic": "South African Republic", "griqualand w": "Griqualand West",
    # --- St Kitts-Nevis hyphenated forms ---
    "st kitts nevis": "Saint Kitts and Nevis", "st k n": "Saint Kitts and Nevis",
    # --- Malayan "Kuala" towns printed as K. ---
    "k lumpur": "Kuala Lumpur", "k kangsar": "Kuala Kangsar",
    "k selangor": "Kuala Selangor", "k pilah": "Kuala Pilah", "k lipis": "Kuala Lipis",
    "uk": "United Kingdom", "eng": "England",
    "lond": "London", "london": "London", "edin": "Edinburgh",
    "camb": "Cambridge", "n ireland": "Northern Ireland",
    "usa": "United States", "us": "United States",
}

# Some entries are full multi-word canonicals already in the source; map them to
# themselves so canonicalize() is idempotent and dedups capitalisation variants.


# --- institution / office values mislabelled as place (FLAG, do not ground) ---
# Dotted office initialisms (case-insensitive on the dotted form).
_OFFICE_ABBR = {
    "co": "Colonial Office", "fo": "Foreign Office", "wo": "War Office",
    "do": "Dominions Office", "lco": "Crown Agents / colonial office",
    "b of t": "Board of Trade", "co rown": "Colonial Office",
    "imp inst": "Imperial Institute",
    # railways & harbours / high commissions / common-services orgs / civil
    # services / research orgs — administrative bodies, not places.
    "ear & h": "East African Railways & Harbours",
    "ear and h": "East African Railways & Harbours",
    "kur & h": "Kenya-Uganda Railways & Harbours",
    "kur and h": "Kenya-Uganda Railways & Harbours",
    "tr & ps": "Tanganyika Railways & Posts",
    "eacso": "East Africa Common Services Organisation",
    "ken and eacso": "East Africa Common Services Organisation",
    "eahc": "East Africa High Commission",
    "eaafro": "East African Agriculture & Forestry Research Org.",
    "w pac hc": "Western Pacific High Commission",
    "wphc": "Western Pacific High Commission",
    "hct": "High Commission Territories",
    "mcs": "Malayan Civil Service", "mal cs": "Malayan Civil Service",
    "sarawak cs": "Sarawak Civil Service", "cey cs": "Ceylon Civil Service",
    # India Office services / departments mislabelled as a place (flag, never ground).
    "ics": "Indian Civil Service", "indian cs": "Indian Civil Service",
    "ips": "Indian Police", "ims": "Indian Medical Service",
    "ifs": "Indian Forest Service", "ise": "Indian Service of Engineers",
    "iccs": "Indian Civil Service", "ipd": "Indian Political Department",
}
# Word-level signals that a value is an institution/office, not a place.
_INSTITUTION_RE = re.compile(
    r"\b(office|dept|department|administration|admin|council|commission|"
    r"secretariat|service|civil service|court|judiciary|legislature|assembly|"
    r"treasury|exchequer|customs|posts? and tel|telegraphs?|railways?|rlwy|"
    r"police|constabulary|force|regiment|regt|battalion|corps|"
    r"university|college|school|institute|hospital|hosp)\b",
    re.I)
# But these geographic words override the institution signal (e.g. a real town
# named "... College" is rare; keep precision high by NOT exempting any here).


def canonicalize(place: str) -> str:
    """Best MCP search string for a printed place value. Splits on commas,
    canonicalises each fragment via the territory map, de-dupes, and rejoins.

    'Penang, S. Sttlmts.' -> 'Penang Straits Settlements';
    'Nig.' -> 'Nigeria'; 'the Gambia' -> 'Gambia'."""
    parts = [s.strip() for s in str(place).split(",") if s.strip()]
    out, seen = [], set()
    for part in parts:
        cleaned = re.sub(r"^(the|of)\s+", "", part, flags=re.I).strip()
        mapped = _TERRITORY.get(canon_key(cleaned), cleaned)
        k = mapped.lower()
        if k not in seen:
            seen.add(k)
            out.append(mapped)
    return " ".join(out) if out else str(place).strip()


def is_institution(place: str) -> tuple[bool, str]:
    """Is ``place`` an office/department/court mislabelled as a place? Returns
    (flag, reason). High precision: only clear institution signals."""
    p = (place or "").strip()
    if not p:
        return (False, "")
    key = canon_key(p)
    if key in _OFFICE_ABBR:
        return (True, f"office abbrev ({_OFFICE_ABBR[key]})")
    if _INSTITUTION_RE.search(p):
        return (True, "institution/office term")
    return (False, "")
