"""Deterministic NORMALIZE pass — the Python half of the hybrid.

Python owns the closed-vocabulary work it is reliable at: expanding the dense
Colonial Office List abbreviations, and flagging acting / military cues. It does
NOT do structure (binding position-place-time across irregular clauses — that is
the LLM's job) and it does NOT guess colonies from place names (places are
grounded to Wikidata downstream).

Two uses:
  * ``normalize_for_llm(raw_text)`` — expand abbreviations in place so the LLM
    gets cleaner, less ambiguous input (the seam that makes its extraction more
    consistent). Structure (``;`` ``—`` clause boundaries, place strings) is
    preserved.
  * ``position_norm`` / ``is_acting`` / ``military_cue`` — token-level helpers
    for the emitted events (a normalized position string for the KG, and the
    flags Gemini's review recommended).

The abbreviation table extends ``services.compile._POS_ABBREV`` (the matcher's
table) with the high-frequency Colonial Office List vocabulary measured across
the corpus (top ~300 dotted tokens cover >90% of ~52k occurrences per edition).
"""

from __future__ import annotations

import re

from ..services.compile import _POS_ABBREV as _BASE_POS

# --- abbreviation vocabulary --------------------------------------------------
# Curated extension of the matcher's table with COL position/department/admin
# abbreviations. Keys are lowercase, dot-stripped; values are full words. Only
# unambiguous expansions are included (ambiguous ones are left to the LLM).
_POS_EXTRA = {
    # roles / ranks
    "comr": "commissioner", "comsnrs": "commissioners", "comm": "commissioner",
    "comsnr": "commissioner", "comnr": "commissioner",
    "asst": "assistant", "assist": "assistant", "asstt": "assistant",
    "dep": "deputy", "depy": "deputy", "depty": "deputy",
    "actg": "acting", "ag": "acting",
    "magte": "magistrate", "magis": "magistrate", "mag": "magistrate",
    "supt": "superintendent", "supdt": "superintendent", "superintdt": "superintendent",
    "supvr": "supervisor", "subinspr": "sub-inspector", "subinsp": "sub-inspector",
    "collr": "collector", "contrlr": "controller", "comptr": "comptroller",
    "auditr": "auditor", "audr": "auditor", "acct": "accountant",
    "acctnt": "accountant", "accntnt": "accountant", "cashr": "cashier",
    "treasr": "treasurer", "treas": "treasurer",
    "registr": "registrar", "regr": "registrar", "regstr": "registrar",
    "survr": "surveyor", "survyr": "surveyor", "surv": "surveyor",
    "engr": "engineer", "engnr": "engineer", "engineer": "engineer",
    "archt": "architect", "drftsmn": "draughtsman",
    "interp": "interpreter", "interpr": "interpreter", "transl": "translator",
    "schoolmr": "schoolmaster", "schlmr": "schoolmaster",
    "matrn": "matron", "nrse": "nurse",
    "warder": "warder", "gaoler": "gaoler",
    "harbmr": "harbourmaster", "harbr": "harbour",
    "postmr": "postmaster", "postm": "postmaster",
    # offices / departments
    "sec": "secretary", "secy": "secretary", "secty": "secretary", "secr": "secretary",
    "colsec": "colonial secretary",
    "govt": "government", "gov": "governor", "govr": "governor", "gvr": "governor",
    "admr": "administrator", "admstr": "administrator", "administr": "administrator",
    "admnstr": "administrator", "admin": "administration",
    "dept": "department", "deptl": "departmental", "dpt": "department",
    "dist": "district", "distr": "district", "div": "division",
    "prot": "protectorate", "protect": "protectorate",
    "pwd": "public works department", "pw": "public works",
    "gpo": "general post office", "po": "post office",
    "rly": "railway", "rlys": "railways", "rwy": "railway",
    "telegr": "telegraph", "telegs": "telegraphs",
    "cust": "customs", "custs": "customs",
    "educn": "education", "educ": "education", "edu": "education",
    "agric": "agriculture", "agricl": "agricultural",
    "med": "medical", "medl": "medical", "med.offr": "medical officer",
    "sanit": "sanitary", "sanity": "sanitary",
    "judl": "judicial", "jud": "judicial", "judic": "judicial",
    "legis": "legislative", "legisl": "legislative", "leg": "legislative",
    "exec": "executive", "execve": "executive",
    "coun": "council", "councl": "council",
    "comtee": "committee", "comm.tee": "committee", "cmtee": "committee",
    "comsn": "commission", "commn": "commission", "comm.n": "commission",
    "treasy": "treasury", "treasry": "treasury",
    "eccles": "ecclesiastical", "eccl": "ecclesiastical",
    "constab": "constabulary", "consty": "constabulary", "pol": "police",
    "milit": "military", "mil": "military",
    "forces": "forces", "regt": "regiment", "batt": "battalion", "bn": "battalion",
    "imm": "immigration", "immig": "immigration", "immign": "immigration",
    "lands": "lands", "forest": "forest", "forestry": "forestry",
    "mines": "mines", "mining": "mining", "minng": "mining",
    "labour": "labour", "lab": "labour",
    # qualifiers / misc
    "ch": "chief", "chf": "chief", "cf": "chief",
    "prin": "principal", "princ": "principal",
    "snr": "senior", "senr": "senior", "sen": "senior",
    "jun": "junior", "junr": "junior", "jr": "junior",
    "gen": "general", "genl": "general", "gnl": "general",
    "offr": "officer", "off": "officer", "offl": "official", "offcl": "official",
    "stip": "stipendiary", "perm": "permanent", "permt": "permanent",
    "temp": "temporary", "tempy": "temporary", "tempr": "temporary",
    "addl": "additional", "add": "additional", "extra": "extra",
    "hon": "honorary", "honble": "honourable",
    "clk": "clerk", "clks": "clerks", "cl.k": "clerk",
    "mem": "member", "membr": "member",
    "pres": "president", "vpres": "vice-president", "vicepres": "vice-president",
    "chmn": "chairman", "chrmn": "chairman", "vchmn": "vice-chairman",
    "atty": "attorney", "attygen": "attorney-general", "soln": "solicitor",
    "solr": "solicitor", "solgen": "solicitor-general",
    "just": "justice", "judg": "judge",
    "civ": "civil", "civl": "civil", "ser": "service", "serv": "service",
    "servs": "services", "examr": "examiner", "exam": "examination",
    "schl": "school", "sch": "school", "coll": "college", "univ": "university",
    "pub": "public", "publ": "public",
    "wks": "works", "wk": "works", "bd": "board",
    "ct": "court", "cts": "courts", "cls": "class",
    "min": "minister", "minl": "ministerial", "ministy": "ministry",
    "apptd": "appointed", "apptmt": "appointment", "appt": "appointment",
    "promtd": "promoted", "promd": "promoted",
    "seconded": "seconded", "transfd": "transferred", "transf": "transferred",
    "retd": "retired", "resd": "resigned", "pensd": "pensioned",
}

POS_ABBREV: dict[str, str] = {**_BASE_POS, **_POS_EXTRA}

MONTH_ABBREV = {
    "jan": "January", "feb": "February", "mar": "March", "apr": "April",
    "apl": "April", "may": "May", "jun": "June", "jul": "July", "aug": "August",
    "sep": "September", "sept": "September", "oct": "October", "nov": "November",
    "dec": "December",
}

# Cues that an event/career is MILITARY (British Army/Navy/militia/expeditions),
# which the civil establishment rosters do NOT cover (refines status/denominator
# and lets the KG tag organization type). Matched case-insensitively as tokens.
_MILITARY_CUES = re.compile(
    r"\b(regt|regiment|batt|battalion|brigade|squadron|R\.?A\.?|R\.?E\.?|R\.?N\.?"
    r"|R\.?A\.?M\.?C|R\.?G\.?A|R\.?F\.?A|W\.?A\.?F\.?F|K\.?A\.?R|hussars|fusiliers"
    r"|lancers|dragoons|rifles|yeomanry|militia|expdn|expedn|expeditionary"
    r"|campaign|despatches|men\. in desp|ensign|subaltern|brevet|A\.D\.C)\b",
    re.I,
)
_ACTING = re.compile(r"\b(ag|actg|act)\.?\b", re.I)

_TOKEN = re.compile(r"[A-Za-z][A-Za-z'&.]*")


def _expand_token(tok: str) -> str:
    """Expand one whitespace token, preserving a trailing comma/semicolon."""
    m = re.match(r"([A-Za-z][A-Za-z'&.\-]*)(.*)", tok)
    if not m:
        return tok
    word, trail = m.group(1), m.group(2)
    key = re.sub(r"[^a-z]", "", word.lower())
    exp = POS_ABBREV.get(key) or MONTH_ABBREV.get(key)
    if exp and word.endswith("."):           # only expand recognised ABBREVIATIONS (dotted)
        return exp + trail
    if exp and key in MONTH_ABBREV:
        return exp + trail
    return tok


def normalize_for_llm(raw_text: str) -> str:
    """Expand recognised dotted abbreviations in place; preserve all structure
    (clause boundaries, places, names, years). Cleaner input for the LLM."""
    return " ".join(_expand_token(t) for t in raw_text.split())


def position_norm(position: str | None) -> str:
    """Fully expanded, normalised position string for the KG (token-level
    abbreviation expansion, lowercased, hyphen/slash split)."""
    if not position:
        return ""
    spaced = re.sub(r"[-/]", " ", position)
    out = []
    for t in re.split(r"\s+", spaced):
        key = re.sub(r"[^a-z]", "", t.lower())
        out.append(POS_ABBREV.get(key, key))
    return " ".join(w for w in out if w)


def is_acting(position: str | None) -> bool:
    return bool(position) and bool(_ACTING.search(position))


def military_cue(text: str | None) -> bool:
    return bool(text) and bool(_MILITARY_CUES.search(text))
