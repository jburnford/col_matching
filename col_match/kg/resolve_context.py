"""Per-person context resolution of ambiguous place abbreviations.

Some printed place forms are ambiguous in isolation but resolvable from the rest
of a person's career:

- directional provinces/regions (``W. Prov.``, ``N. Prov.``, ``S. Provs.``,
  ``E. region``) name a sub-unit of whatever colony the person served in -> we
  attach the parent country from their sibling postings, giving a precise
  ``Western Province, Ceylon`` / ``Northern Provinces, Nigeria``.
- ``S.A.`` (South Africa vs South Australia) and ``W.A.`` (West Africa vs Western
  Australia) resolve from the region cluster of the sibling postings.

Resolution is GATED: a value is resolved only when the evidence points to a
single country/region. Ambiguous-with-conflict or no-evidence cases return None
(the caller keeps them flagged), so the 0-FP discipline is preserved — context
proposes, but only an unambiguous signal resolves.
"""
from __future__ import annotations

import re
from collections import Counter

from .place_canon import canonicalize, canon_key

# --- region evidence clusters (canonical names from place_canon) ----------
_S_AFRICA = {
    "South Africa", "Cape Colony", "Cape Province", "Cape of Good Hope", "Natal",
    "Transvaal", "Orange River Colony", "Orange Free State", "Basutoland",
    "Bechuanaland", "Swaziland", "Southern Rhodesia", "Northern Rhodesia",
}
_AUSTRALIA = {
    "South Australia", "Western Australia", "New South Wales", "Victoria",
    "Queensland", "Tasmania", "Australia", "Northern Territory",
}
_W_AFRICA = {
    "Nigeria", "Northern Nigeria", "Southern Nigeria", "Western Region Nigeria",
    "Eastern Region Nigeria", "Gold Coast", "Sierra Leone", "Gambia", "Lagos",
    "British West Africa",
}
# India Office List: presidencies/provinces/agencies. Used to disambiguate
# India-vs-Africa initialisms (C.P. = Central Provinces vs Cape Province) and as
# parent-colony candidates for directional sub-units.
_INDIA = {
    "Bengal", "Bombay", "Madras", "Punjab", "United Provinces",
    "Central Provinces", "Central Provinces and Berar", "Bihar and Orissa",
    "Bihar", "Orissa", "Assam", "Burma", "Sind", "Berar", "Coorg",
    "Ajmer-Merwara", "Baluchistan", "Delhi", "North-West Frontier Province",
    "Rajputana", "Central India Agency", "Hyderabad State", "Mysore", "Baroda",
    "Gwalior", "Jammu and Kashmir", "Travancore", "Cochin", "Eastern Bengal",
}

# --- directional province/region parsing ----------------------------------
_DIR = re.compile(
    r"^(n|s|e|w|cent|central|nw|ne|sw|se|nc)\.?\s*\.?\s*"
    r"(prov|provs|province|provinces|regn|region|district)\.?$", re.I)
_DIRNAME = {
    "n": "Northern", "s": "Southern", "e": "Eastern", "w": "Western",
    "cent": "Central", "central": "Central", "nw": "North-Western",
    "ne": "North-Eastern", "sw": "South-Western", "se": "South-Eastern",
    "nc": "North-Central",
}
# Colonies that have named provinces/regions/districts (the parent set). Regional
# Nigerias collapse to Nigeria so a directional province attaches to the country.
_COUNTRY_COLLAPSE = {
    "Northern Nigeria": "Nigeria", "Southern Nigeria": "Nigeria",
    "Western Region Nigeria": "Nigeria", "Eastern Region Nigeria": "Nigeria",
}
_PROV_COUNTRIES = {
    "Ceylon", "Kenya", "Nigeria", "Uganda", "Tanganyika", "Gold Coast",
    "Sierra Leone", "Nyasaland", "Northern Rhodesia", "Southern Rhodesia",
    "Natal", "Cape Colony", "Fiji", "Zanzibar", "British Guiana",
    "Federated Malay States", "Sudan", "Palestine",
    # India Office List presidencies/provinces (parents of directional districts)
    "Bengal", "Bombay", "Madras", "Punjab", "United Provinces",
    "Central Provinces", "Bihar and Orissa", "Assam", "Burma", "Sind",
    "North-West Frontier Province", "Rajputana",
}


def _frags(place: str):
    return [f.strip() for f in re.split(r",| and | & ", place) if f.strip()]


def is_ambiguous(place: str) -> bool:
    """Does this surface form need per-person context to ground?"""
    p = (place or "").strip()
    return bool(_DIR.match(p)) or canon_key(p) in ("sa", "wa", "cp")


def _region_hit(siblings):
    qs = {canonicalize(f) for p in siblings for f in _frags(p)}
    return qs & _S_AFRICA, qs & _AUSTRALIA, qs & _W_AFRICA, qs & _INDIA


def _parent_country(siblings):
    c: Counter = Counter()
    for p in siblings:
        for f in _frags(p):
            q = canonicalize(f)
            q = _COUNTRY_COLLAPSE.get(q, q)
            if q in _PROV_COUNTRIES:
                c[q] += 1
    return c


def _dir_label(place: str):
    m = _DIR.match(place.strip())
    if not m:
        return None
    d = m.group(1).lower().replace(".", "")
    word = m.group(2).lower()
    if word.startswith("prov"):
        base = "Provinces" if word.endswith("s") and word != "province" else "Province"
    elif word.startswith("reg"):
        base = "Region"
    else:
        base = "District"
    return f"{_DIRNAME.get(d, d.title())} {base}"


def resolve(place: str, siblings: list[str]) -> tuple[str | None, str]:
    """Resolve an ambiguous place from a person's other postings.
    Returns (resolved_query | None, evidence). None => keep flagged."""
    p = (place or "").strip()
    sa, au, wafr, india = _region_hit(siblings)

    if canon_key(p) == "cp":
        # Central Provinces (India) vs Cape Province (South Africa)
        if india and not sa:
            return "Central Provinces", f"india postings: {sorted(india)[:3]}"
        if sa and not india:
            return "Cape Province", f"southern-africa postings: {sorted(sa)[:3]}"
        return None, "no single-region signal"

    if canon_key(p) == "sa":
        if sa and not au:
            return "South Africa", f"southern-africa postings: {sorted(sa)[:3]}"
        if au and not sa:
            return "South Australia", f"australia postings: {sorted(au)[:3]}"
        return None, "no single-region signal"

    if canon_key(p) == "wa":
        if wafr and not au:
            return "British West Africa", f"west-africa postings: {sorted(wafr)[:3]}"
        if au and not wafr:
            return "Western Australia", f"australia postings: {sorted(au)[:3]}"
        return None, "no single-region signal"

    if _DIR.match(p):
        label = _dir_label(p)
        countries = _parent_country(siblings)
        if not countries:
            return None, "no parent-colony sibling"
        country, _ = countries.most_common(1)[0]
        # require the top country to dominate (>= half of colony mentions)
        if countries.most_common(1)[0][1] < sum(countries.values()) / 2 + 1e-9 and len(countries) > 1:
            # tie between colonies -> keep flagged
            top = countries.most_common(2)
            if len(top) > 1 and top[0][1] == top[1][1]:
                return None, f"ambiguous parent colony: {dict(countries)}"
        return f"{label}, {country}", f"parent colony: {country} ({dict(countries)})"

    return None, "not an ambiguous form"
