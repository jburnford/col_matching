#!/usr/bin/env python3
"""Generate a GROUNDED place->colony roll-up from external sources (not from
model memory), written to data/services/place_rollup.json for the gazetteer to
load. Two grounded sources:

  1. capital_audit_raw.json (col_pipeline) — each colony's capital + Wikidata
     QIDs. Gives capital-city -> colony (Pretoria -> Transvaal, Colombo ->
     Ceylon). Ambiguous capitals (same name, >1 colony) are skipped.
  2. empire-evolution-wpcs CIDOC-CRM KG — P107 group membership, giving
     federation/dominion member -> parent (Quebec -> Canada, WI islands).

Only mappings whose PARENT is an actual COL record colony are kept (so the
roll-up can only ever help a real match). Each entry records its source + QID
for provenance.

Run:  python3 build_place_rollup.py
"""
import json
from collections import defaultdict
from pathlib import Path

from col_match.services import gazetteer as g

DD = Path("data/services")
CAPITAL_AUDIT = Path("/home/jic823/col_pipeline/audits/capital_audit_raw.json")
KG_TTL = Path("/home/jic823/empire-evolution-wpcs/data/empire-evolution-crm.ttl")


def record_colonies():
    rec = set()
    for l in (DD / "graph_cache" / "officials.jsonl").open():
        rec.add(g.norm(json.loads(l).get("colony") or ""))
    rec.discard("")
    return rec


def from_capitals(rec):
    out = {}
    if not CAPITAL_AUDIT.exists():
        print(f"  (capital_audit not found at {CAPITAL_AUDIT})")
        return out
    rows = json.load(CAPITAL_AUDIT.open())
    cap2col = defaultdict(set)
    cap_qid = {}
    for r in rows:
        cn, col = g.norm(r.get("cap") or ""), g.norm(r.get("col") or "")
        if cn and col:
            cap2col[cn].add(col)
            cap_qid[cn] = r.get("cap_qid")
    for cap, cols in cap2col.items():
        cols &= rec
        if len(cols) == 1 and cap not in rec:          # unambiguous, capital != colony name
            out[cap] = {"colony": next(iter(cols)), "qid": cap_qid.get(cap),
                        "source": "capital_audit"}
    return out


def from_kg(rec):
    out = {}
    if not KG_TTL.exists():
        print(f"  (KG TTL not found at {KG_TTL})")
        return out
    try:
        import rdflib
    except ImportError:
        print("  (rdflib not installed; skipping KG)")
        return out
    G = rdflib.Graph(); G.parse(str(KG_TTL), format="turtle")
    CRM = rdflib.Namespace("http://www.cidoc-crm.org/cidoc-crm/")
    SKOS = rdflib.URIRef("http://www.w3.org/2004/02/skos/core#relatedMatch")
    def lbl(u):
        for o in G.objects(u, rdflib.RDFS.label):
            return str(o)
        return None
    def qid(u):
        for o in G.objects(u, SKOS):
            return str(o).rsplit("/", 1)[-1]
        return None
    for parent, member in G.subject_objects(CRM.P107_has_current_or_former_member):
        pl, ml = lbl(parent), lbl(member)
        if not pl or not ml:
            continue
        pn = g.norm(pl)
        mn = g.norm(ml.split("(")[0])  # strip "(Province)" etc.
        if pn in rec and mn not in rec and mn:
            out[mn] = {"colony": pn, "qid": qid(member), "source": "empire_kg"}
    return out


def main():
    rec = record_colonies()
    caps = from_capitals(rec)
    kg = from_kg(rec)
    merged = {**kg, **caps}   # capital_audit wins on conflict (more specific)
    (DD / "place_rollup.json").write_text(json.dumps(merged, indent=1, sort_keys=True))
    print(f"record colonies: {len(rec)}")
    print(f"capital_audit roll-ups: {len(caps)};  KG roll-ups: {len(kg)};  merged: {len(merged)}")
    print("wrote data/services/place_rollup.json")
    for k, v in sorted(merged.items())[:25]:
        print(f"  {k:24s} -> {v['colony']}  [{v['source']}, {v.get('qid')}]")


if __name__ == "__main__":
    main()
