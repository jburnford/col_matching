"""Resolve a grounded place to its historical COLONY, against the existing
empire-evolution-wpcs knowledge graph — never by guessing.

The empire KG (``~/empire-evolution-wpcs``) holds 314 colonial polities (plus
princely states) as CIDOC-CRM entities with Wikidata QIDs and rdfs labels. A
grounded place resolves to a colony when:

  * its grounded Wikidata QID IS a polity in the empire KG (the place is itself
    a colonial polity — Nyasaland, British Hong Kong); or
  * its grounded Wikidata LABEL matches a polity label (handles QID mismatches,
    e.g. we grounded Cape Colony to Q370736 while the KG carries a different
    Cape QID).

Sub-localities (e.g. Ixopo, Penang) whose grounded entity is NOT itself a
polity are left ``colony=null`` here (flagged), to be resolved by a later
country+year lineage walk — we do NOT guess a parent colony from the locality.
Reuses the rdflib TTL-parse pattern from build_place_rollup.py.
"""

from __future__ import annotations

import re
from functools import lru_cache
from pathlib import Path

KG_TTL = Path.home() / "empire-evolution-wpcs" / "data" / "empire-evolution-crm.ttl"
_CRM = "http://www.cidoc-crm.org/cidoc-crm/"
_SKOS_RELATED = "http://www.w3.org/2004/02/skos/core#relatedMatch"
_NORM = re.compile(r"[^a-z0-9 ]")


def _norm(s: str) -> str:
    return _NORM.sub("", (s or "").lower()).strip()


@lru_cache(maxsize=1)
def _index(ttl_path: str) -> tuple[dict, dict]:
    """Return (qid -> {qid,label}, norm_label -> {qid,label}) over empire-KG
    polities. Empty if rdflib or the TTL is unavailable (degrades to null)."""
    qid2node: dict[str, dict] = {}
    label2node: dict[str, dict] = {}
    p = Path(ttl_path)
    if not p.exists():
        return qid2node, label2node
    try:
        import rdflib
    except ImportError:
        return qid2node, label2node
    g = rdflib.Graph()
    g.parse(str(p), format="turtle")
    related = rdflib.URIRef(_SKOS_RELATED)
    for subj in set(g.subjects()):
        label = next((str(o) for o in g.objects(subj, rdflib.RDFS.label)), None)
        if not label:
            continue
        qid = None
        for o in g.objects(subj, related):
            tail = str(o).rsplit("/", 1)[-1]
            if re.fullmatch(r"Q\d+", tail):
                qid = tail
                break
        node = {"qid": qid, "label": label}
        if qid:
            qid2node[qid] = node
        label2node.setdefault(_norm(label.split("(")[0]), node)
    return qid2node, label2node


def resolve_colony(place_row: dict, ttl_path: str | None = None) -> dict:
    """Map a grounding-cache row to a colony. Returns
    {colony_qid, colony_label, method} (method: empire_kg_qid | empire_kg_label
    | unresolved)."""
    qid2, lab2 = _index(str(ttl_path or KG_TTL))
    qid = place_row.get("qid")
    label = place_row.get("label") or place_row.get("place") or ""
    if qid and qid in qid2:
        n = qid2[qid]
        return {"colony_qid": n["qid"], "colony_label": n["label"], "method": "empire_kg_qid"}
    n = lab2.get(_norm(label.split("(")[0]))
    if n:
        return {"colony_qid": n["qid"], "colony_label": n["label"], "method": "empire_kg_label"}
    return {"colony_qid": None, "colony_label": None, "method": "unresolved"}
