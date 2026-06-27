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
# The CIDOC TTL is incomplete on princely-state QIDs (≈395 QID-bearing nodes) —
# the period-modelled qid_manifest.tsv carries the full set (740 polities incl.
# 433 South-Asian princely states + provinces + presidencies). The TTL takes
# precedence; the manifest fills the gaps so India places resolve.
KG_MANIFEST = Path.home() / "empire-evolution-wpcs" / "data" / "qid_manifest.tsv"
_CRM = "http://www.cidoc-crm.org/cidoc-crm/"
_SKOS_RELATED = "http://www.w3.org/2004/02/skos/core#relatedMatch"
_NORM = re.compile(r"[^a-z0-9 ]")
_QID = re.compile(r"Q\d+")


def _norm(s: str) -> str:
    return _NORM.sub("", (s or "").lower()).strip()


def _fold_manifest(manifest_path: str, qid2node: dict, label2node: dict) -> None:
    """Fill gaps from the period-modelled qid_manifest.tsv (the TTL is sparse on
    princely states). Adds a polity only when its QID/label is not already
    present from the higher-precedence TTL."""
    p = Path(manifest_path)
    if not p.exists():
        return
    import csv
    with p.open(encoding="utf-8") as fh:
        for row in csv.DictReader(fh, delimiter="\t"):
            qid = (row.get("wikidata_id") or "").strip()
            if not _QID.fullmatch(qid):
                continue
            label = (row.get("canonical_name") or row.get("name") or "").strip()
            if not label:
                continue
            node = {"qid": qid, "label": label, "source": "manifest"}
            qid2node.setdefault(qid, node)
            label2node.setdefault(_norm(label.split("(")[0]), node)


@lru_cache(maxsize=1)
def _index(ttl_path: str, manifest_path: str) -> tuple[dict, dict]:
    """Return (qid -> {qid,label}, norm_label -> {qid,label}) over empire-KG
    polities: the CIDOC TTL first, then the qid_manifest.tsv filling gaps.
    Empty if neither source is available (degrades to null)."""
    qid2node: dict[str, dict] = {}
    label2node: dict[str, dict] = {}
    p = Path(ttl_path)
    try:
        import rdflib
    except ImportError:
        rdflib = None
    if rdflib is not None and p.exists():
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
            node = {"qid": qid, "label": label, "source": "ttl"}
            if qid:
                qid2node[qid] = node
            label2node.setdefault(_norm(label.split("(")[0]), node)
    _fold_manifest(manifest_path, qid2node, label2node)
    return qid2node, label2node


# Curated modern-equivalent groundings (Jim 2026-06-27): where no clean colonial
# Wikidata entity exists, we ground to the modern equivalent because it gives the
# better/more-specific geography than rolling up to the parent colony. Such places
# are their OWN colony marker (not collapsed to the modern nation), with a note.
#   Penang: grounded to Q188096 (modern state) -> George Town; the empire KG would
#   otherwise roll it up to Q833 (Malaysia/Malaya) via skos:relatedMatch, pooling
#   1,400+ Penang careers under the national capital. The colonial referent is the
#   Penang settlement of the Straits Settlements (1826-1946).
CURATED_COLONY = {
    "Q188096": {"colony_qid": "Q188096", "colony_label": "Penang",
                "method": "curated_modern_equiv",
                "note": "modern-equivalent QID for geography; colonial Penang = a "
                        "settlement of the Straits Settlements"},
}


def resolve_colony(place_row: dict, ttl_path: str | None = None,
                   manifest_path: str | None = None) -> dict:
    """Map a grounding-cache row to a colony. Returns
    {colony_qid, colony_label, method}. method = {ttl,manifest}_{qid,label},
    curated_modern_equiv, or unresolved, recording which source matched."""
    qid = place_row.get("qid")
    if qid in CURATED_COLONY:
        return dict(CURATED_COLONY[qid])
    qid2, lab2 = _index(str(ttl_path or KG_TTL), str(manifest_path or KG_MANIFEST))
    label = place_row.get("label") or place_row.get("place") or ""
    if qid and qid in qid2:
        n = qid2[qid]
        return {"colony_qid": n["qid"], "colony_label": n["label"],
                "method": f"{n.get('source', 'ttl')}_qid"}
    n = lab2.get(_norm(label.split("(")[0]))
    if n:
        return {"colony_qid": n["qid"], "colony_label": n["label"],
                "method": f"{n.get('source', 'ttl')}_label"}
    return {"colony_qid": None, "colony_label": None, "method": "unresolved"}
