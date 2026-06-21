"""Ground distinct event places to Wikidata QIDs via the Wikidata MCP.

Per the project rule, grounding uses the WikidataMCP vector search
(``mcp__wikidata__search_items``) + statement verification
(``mcp__wikidata__get_statements``) — NEVER the REST ``wbsearchentities`` API,
which matches on string similarity with no semantic context.

The MCP calls are AGENT-DRIVEN (an assistant loop, ≤5 calls/turn, cached
aggressively), exactly as the place-disambig skill works — a Python module
cannot call the MCP itself. This module therefore provides the deterministic
scaffolding around that loop:

  * ``distinct_places`` — the worklist (most-frequent first, minus what's cached);
  * ``query_for`` — a clean search query from a printed place string;
  * ``parse_statements`` — turn ``get_statements`` output into a verification
    verdict (is it geographic? country QID? coords present?);
  * cache read/append to ``data/kg/places_grounding.jsonl`` (resumable).

Places are recorded as PRINTED on the event; this module never upgrades a
locality to a colony — that is colony.py's job, against the empire-evolution KG.
"""

from __future__ import annotations

import json
import re
from collections import Counter
from pathlib import Path

from ..services import gazetteer
from . import place_canon

CACHE = Path("data/kg/places_grounding.jsonl")

# light, deterministic query cleanups (NOT colony guessing — just better search
# strings). Abbreviation expansion + variant collapse live in place_canon.


def load_cache() -> dict[str, dict]:
    if not CACHE.exists():
        return {}
    return {r["place"]: r for r in (json.loads(l) for l in CACHE.open(encoding="utf-8"))}


def append(row: dict) -> None:
    CACHE.parent.mkdir(parents=True, exist_ok=True)
    with CACHE.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(row, ensure_ascii=False) + "\n")


def distinct_places(struct_path: Path, cache: dict[str, dict] | None = None) -> list[tuple[str, int]]:
    """Distinct event places across structured bios, most frequent first,
    excluding those already in the grounding cache."""
    cache = cache if cache is not None else load_cache()
    c: Counter = Counter()
    for l in struct_path.open(encoding="utf-8"):
        for ev in json.loads(l).get("events") or []:
            p = (ev.get("place") or "").strip()
            if p:
                c[p] += 1
    return [(p, n) for p, n in c.most_common() if p not in cache]


def query_for(place: str) -> str:
    """Build a clean MCP search query from a printed place string, expanding the
    colonial territory abbreviations (``Nig.``->Nigeria, ``F.M.S.``->Federated
    Malay States) and collapsing surface variants to one canonical form.

    'Penang, S. Sttlnts.' -> 'Penang Straits Settlements';
    'the Gambia' -> 'Gambia'; 'Ixopo, Natal' -> 'Ixopo Natal'."""
    return place_canon.canonicalize(place)


# --- place-noise guard (FLAG, do not drop) --------------------------------
# Non-geographic values the structurer sometimes lands in `place` (war/campaign
# names, months, languages, conflict phrasing). They would pollute the Wikidata
# worklist. We FLAG them (with a reason) so grounding can skip/route them for
# review — nothing is removed from the worklist. A value the gazetteer recognises
# as a real place is never flagged (rescue), so abbreviations like "T.T." stay.
from .normalize import MONTH_ABBREV as _MONTHS_ABBR

_MONTH_KEYS = set(_MONTHS_ABBR) | {m.lower() for m in _MONTHS_ABBR.values()}
_WAR = re.compile(
    r"\b(war|campaign|expe?dn?|expedition|rebellion|rising|mutiny|punitive|"
    r"operations|siege|relief of|frontier force|expeditionary)\b", re.I)
_CONFLICT_PHRASE = re.compile(r"\b(against|in connection with)\b", re.I)
_LANGUAGES = {"swahili", "hausa", "arabic", "tamil", "urdu", "hindustani",
              "chinese", "persian", "yoruba", "twi", "malayalam", "telugu"}


def suspected_noise(place: str, known=None) -> tuple[bool, str]:
    """Is ``place`` likely NOT a geographic place? Returns (flag, reason).
    ``known`` is an optional callable (e.g. a gazetteer lookup) that rescues a
    value it recognises as a real place. High precision — only clear non-places
    are flagged, since a flag steers grounding to skip the value."""
    p = (place or "").strip()
    if not p:
        return (False, "")
    if known and known(p):
        return (False, "")
    inst, reason = place_canon.is_institution(p)
    if inst:
        return (True, reason)
    key = re.sub(r"[^a-z]", "", p.lower())
    if key in _MONTH_KEYS:
        return (True, "month name")
    # language only when the whole place is a single plain word (avoid abbrevs
    # like "T.W.I." collapsing to "twi")
    if re.fullmatch(r"[A-Za-z]+", p) and p.lower() in _LANGUAGES:
        return (True, "language name")
    # war/campaign — but NOT institutions like "War Office"/"War Dept."
    if _WAR.search(p) and not re.search(r"\bwar\s+(office|dept|department|memorial)\b", p, re.I):
        return (True, "war/campaign term")
    if _CONFLICT_PHRASE.search(p):
        return (True, "conflict-context phrase")
    return (False, "")


# --- verification of get_statements output --------------------------------
_P31 = re.compile(r"instance of \(P31\):\s*(.+?)\s*\(Q\d+\)")
_P17 = re.compile(r"country \(P17\):.*?\((Q\d+)\)")
_P131 = re.compile(r"located in the administrative territorial entity \(P131\):.*?\((Q\d+)\)")
_P625 = re.compile(r"coordinate location \(P625\)")
_GEO_HINT = re.compile(
    r"\b(city|town|village|settlement|colony|territory|province|district|island"
    r"|country|state|capital|municipality|protectorate|region|county|port"
    r"|administrative|human settlement|geographic)\b", re.I)


def parse_statements(text: str) -> dict:
    """Verdict from a ``get_statements`` result block: is the entity a place,
    its country QID, its admin-parent QID, whether it has coordinates."""
    p31 = _P31.findall(text)
    country = _P17.search(text)
    p131 = _P131.search(text)
    has_coords = bool(_P625.search(text))
    is_geo = has_coords or any(_GEO_HINT.search(t) for t in p31) or bool(country)
    return {
        "is_geographic": is_geo,
        "instance_of": p31,
        "country_qid": country.group(1) if country else None,
        "p131_qid": p131.group(1) if p131 else None,
        "has_coords": has_coords,
    }


def make_row(place: str, qid: str | None, label: str | None,
             verdict: dict | None, match_type: str) -> dict:
    return {
        "place": place,
        "qid": qid,
        "label": label,
        "country_qid": (verdict or {}).get("country_qid"),
        "p131_qid": (verdict or {}).get("p131_qid"),
        "instance_of": (verdict or {}).get("instance_of", []),
        "match_type": match_type,          # mcp_verified | mcp_unverified | ungrounded
    }
