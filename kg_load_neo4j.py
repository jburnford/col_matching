#!/usr/bin/env python3
"""Load the v3 knowledge graph into a Neo4j database.

This is the Neo4j twin of ``kg_load_ladybug.py`` — same reified career-event
model, same JSONL inputs, but writing to Neo4j over the Bolt protocol instead of
into an embedded LadybugDB file.

  (:Person)-[:HAS_EVENT]->(:CareerEvent)-[:EVENT_ROLE]->(:Role)
                          (:CareerEvent)-[:EVENT_PLACE]->(:Place)
                          (:CareerEvent)-[:EVENT_COLONY]->(:Place)
  (:Person)-[:RECEIVED]->(:Honour)
  (:Person)-[:HOLDS_QUAL]->(:Qualification)
  (:Person)-[:EDUCATED_AT]->(:Institution)
  (:Person)-[:EMPLOYED_BY]->(:Organisation)

SAFETY: this targets a SEPARATE, local Neo4j by default (bolt://localhost:7687)
and is fully standalone — it does NOT import col_match.config, so it can never
inherit the production graph credentials. It only ever creates/clears nodes that
carry the ``:ICKG`` marker label (and an ``ICKG_corpus`` property), so it cannot
disturb other data living in the same database.

Connection (env vars, all optional):
  KG_NEO4J_URI       default bolt://localhost:7687
  KG_NEO4J_USER      default neo4j
  KG_NEO4J_PASSWORD  default neo4j
  KG_NEO4J_DATABASE  default neo4j

Which corpus to load is chosen, as everywhere in this repo, by COL_KG_OUT:

  COL_KG_OUT=data/kg  python3 kg_load_neo4j.py     # Colonial Office List
  COL_KG_OUT=data/iol python3 kg_load_neo4j.py     # India Office List

Pass --keep to append instead of clearing this corpus first.
"""
from __future__ import annotations
import json, os, sys
from pathlib import Path
from col_match.kg.paths import kg_out
from neo4j import GraphDatabase

GD = kg_out() / "graph_stage3"
CORPUS = "iol" if "iol" in str(kg_out()).lower() else "co"
MARKER = "ICKG"  # Imperial Careers KG — namespacing label so we never touch other data

URI = os.environ.get("KG_NEO4J_URI", "bolt://localhost:7687")
USER = os.environ.get("KG_NEO4J_USER", "neo4j")
PASSWORD = os.environ.get("KG_NEO4J_PASSWORD", "neo4j")
DATABASE = os.environ.get("KG_NEO4J_DATABASE", "neo4j")
BATCH = 5000


def L(f):
    p = GD / f
    return [json.loads(l) for l in p.open()] if p.exists() else []


def load_facts():
    """Synthesize career_facts from career_events joined with role_edges
    (on person_id+seq), exactly as kg_load_ladybug.py does."""
    if (GD / "career_facts.jsonl").exists() and not (GD / "career_events.jsonl").exists():
        return L("career_facts.jsonl")
    rng = {(r["person_id"], r.get("seq")): r for r in L("role_edges.jsonl")}
    facts = []
    for e in L("career_events.jsonl"):
        r = rng.get((e["person_id"], e.get("seq")), {})
        facts.append({
            "person_id": e["person_id"], "seq": e.get("seq"),
            "role_id": r.get("role_id"),
            "role_label": r.get("role_label") or e.get("position_norm"),
            "role_modifiers": r.get("modifiers") or [],
            "place_qid": e.get("place_qid"), "place_label": e.get("place_label"),
            "colony_qid": e.get("colony_qid"), "colony_label": e.get("colony_label"),
            "year_start": e.get("year_start"), "year_end": e.get("year_end"),
            "is_acting": e.get("is_acting"), "position_raw": e.get("position"),
            "role_source": r.get("source") or "",
        })
    return facts


def run_batched(session, query, rows):
    for i in range(0, len(rows), BATCH):
        session.run(query, rows=rows[i:i + BATCH])


def main():
    keep = "--keep" in sys.argv
    facts = load_facts()
    if not facts:
        sys.exit(f"No graph data found under {GD} — download the data bundle first "
                 f"(see README → Open data).")

    persons = L("persons.jsonl")
    places = {p["qid"]: p for p in L("places.jsonl") if p.get("qid")}
    # Places referenced by an event but absent from places.jsonl still need a node.
    for f in facts:
        for q, lk in ((f.get("place_qid"), "place_label"), (f.get("colony_qid"), "colony_label")):
            if q and q not in places:
                places[q] = {"qid": q, "label": f.get(lk) or q, "country_qid": None}

    def nodes(rows, idk="id"):
        return [r for r in rows if r.get(idk) and str(r[idk]).strip()]

    roles = nodes(L("roles.jsonl"))
    orgs = nodes(L("organisations.jsonl"))
    insts = nodes(L("institutions.jsonl"))
    hons = nodes(L("honour_nodes.jsonl"))
    quals = nodes(L("qualification_nodes.jsonl"))

    pgf = GD / "person_grounding.final.jsonl"
    if not pgf.exists():
        pgf = GD / "person_grounding.verified.jsonl"
    pground = {}
    if pgf.exists():
        for l in pgf.open():
            g = json.loads(l)
            pground[g["person_id"]] = (g["qid"], g.get("wd_name") or "", g.get("tier") or "")

    driver = GraphDatabase.driver(URI, auth=(USER, PASSWORD))
    with driver.session(database=DATABASE) as s:
        # constraints (idempotent) — composite key on (corpus,id) so CO and IOL coexist
        for lbl, key in [("Person", "person_id"), ("Place", "qid"), ("Role", "id"),
                         ("Organisation", "id"), ("Institution", "id"), ("Honour", "id"),
                         ("Qualification", "id"), ("CareerEvent", "id")]:
            s.run(f"CREATE CONSTRAINT {MARKER}_{lbl}_key IF NOT EXISTS "
                  f"FOR (n:{MARKER}_{lbl}) REQUIRE (n.ICKG_corpus, n.{key}) IS UNIQUE")

        if not keep:
            print(f"clearing existing {CORPUS!r} corpus...")
            while True:
                r = s.run(f"MATCH (n:{MARKER}) WHERE n.ICKG_corpus=$c "
                          f"WITH n LIMIT 50000 DETACH DELETE n RETURN count(n) AS n",
                          c=CORPUS).single()
                if not r or r["n"] == 0:
                    break

        c = CORPUS
        print("nodes:")
        rows = [{"person_id": p["person_id"], "surname": p.get("surname") or "",
                 "given_names": p.get("given_names") or "",
                 "birth_year": p.get("birth_year"),
                 "n_attestations": p.get("n_attestations") or 0,
                 "wikidata_qid": pground.get(p["person_id"], ("", "", ""))[0],
                 "wikidata_label": pground.get(p["person_id"], ("", "", ""))[1],
                 "wikidata_tier": pground.get(p["person_id"], ("", "", ""))[2]} for p in persons]
        run_batched(s, f"UNWIND $rows AS r MERGE (n:{MARKER}:{MARKER}_Person "
                    f"{{ICKG_corpus:'{c}', person_id:r.person_id}}) SET n += r", rows)
        print(f"  Person          {len(rows):>7,}")

        for label, data, idk, props in [
            ("Place", list(places.values()), "qid", ["label", "country_qid"]),
            ("Role", roles, "id", ["label", "category", "source"]),
            ("Organisation", orgs, "id", ["label", "type", "source"]),
            ("Institution", insts, "id", ["label", "type", "source"]),
            ("Honour", hons, "id", ["label", "type", "source"]),
            ("Qualification", quals, "id", ["label", "type", "source"]),
        ]:
            rows = [{**{idk: d[idk]}, **{k: d.get(k) for k in props}} for d in data]
            run_batched(s, f"UNWIND $rows AS r MERGE (n:{MARKER}:{MARKER}_{label} "
                        f"{{ICKG_corpus:'{c}', {idk}:r.{idk}}}) SET n += r", rows)
            print(f"  {label:14}  {len(rows):>7,}")

        def eid(f): return f"{f['person_id']}#{f['seq']}"
        rows = [{"id": eid(f), "year_start": f.get("year_start"), "year_end": f.get("year_end"),
                 "is_acting": bool(f.get("is_acting")), "position_raw": f.get("position_raw") or "",
                 "role_source": f.get("role_source") or ""} for f in facts]
        run_batched(s, f"UNWIND $rows AS r MERGE (n:{MARKER}:{MARKER}_CareerEvent "
                    f"{{ICKG_corpus:'{c}', id:r.id}}) SET n += r", rows)
        print(f"  CareerEvent     {len(rows):>7,}")

        # ---- relationships -------------------------------------------------
        print("rels:")
        role_ids = {r["id"] for r in roles}
        org_ids = {o["id"] for o in orgs}
        inst_ids = {i["id"] for i in insts}
        hon_ids = {h["id"] for h in hons}
        qual_ids = {q["id"] for q in quals}
        person_ids = {p["person_id"] for p in persons}

        def rel(name, rows, frm_lbl, frm_key, to_lbl, to_key, set_clause=""):
            q = (f"UNWIND $rows AS r "
                 f"MATCH (a:{MARKER}_{frm_lbl} {{ICKG_corpus:'{c}', {frm_key}:r.frm}}) "
                 f"MATCH (b:{MARKER}_{to_lbl} {{ICKG_corpus:'{c}', {to_key}:r.to}}) "
                 f"MERGE (a)-[e:{name}]->(b){set_clause}")
            run_batched(s, q, rows)
            print(f"  {name:14}  {len(rows):>7,}")

        rel("HAS_EVENT", [{"frm": f["person_id"], "to": eid(f)} for f in facts],
            "Person", "person_id", "CareerEvent", "id")
        rel("EVENT_ROLE", [{"frm": eid(f), "to": f["role_id"],
                            "mods": ",".join(f.get("role_modifiers") or [])}
                           for f in facts if f.get("role_id") in role_ids],
            "CareerEvent", "id", "Role", "id", " SET e.modifiers=r.mods")
        rel("EVENT_PLACE", [{"frm": eid(f), "to": f["place_qid"]}
                            for f in facts if f.get("place_qid") in places],
            "CareerEvent", "id", "Place", "qid")
        rel("EVENT_COLONY", [{"frm": eid(f), "to": f["colony_qid"]}
                             for f in facts if f.get("colony_qid") in places],
            "CareerEvent", "id", "Place", "qid")
        rel("RECEIVED", [{"frm": e["person_id"], "to": e["honour_id"], "year": e.get("year"),
                          "mods": ",".join(e.get("modifiers") or [])}
                         for e in L("honour_edges.jsonl")
                         if e["person_id"] in person_ids and e.get("honour_id") in hon_ids],
            "Person", "person_id", "Honour", "id", " SET e.year=r.year, e.modifiers=r.mods")
        rel("HOLDS_QUAL", [{"frm": e["person_id"], "to": e["qualification_id"], "year": e.get("year")}
                           for e in L("qualification_edges.jsonl")
                           if e["person_id"] in person_ids and e.get("qualification_id") in qual_ids],
            "Person", "person_id", "Qualification", "id", " SET e.year=r.year")
        rel("EDUCATED_AT", [{"frm": e["person_id"], "to": e["institution_id"],
                             "edu_type": e.get("type") or ""}
                            for e in L("education_edges.jsonl")
                            if e["person_id"] in person_ids and e.get("institution_id") in inst_ids],
            "Person", "person_id", "Institution", "id", " SET e.edu_type=r.edu_type")

        def empl_org(e): return e.get("org_id") or e.get("institution_id")
        rel("EMPLOYED_BY", [{"frm": e["person_id"], "to": empl_org(e)}
                            for e in L("employment_edges.jsonl")
                            if e["person_id"] in person_ids and empl_org(e) in org_ids],
            "Person", "person_id", "Organisation", "id")

        # ---- validation ----------------------------------------------------
        print("\nvalidation:")
        for name, q in [
            ("persons", f"MATCH (p:{MARKER}_Person {{ICKG_corpus:'{c}'}}) RETURN count(p) AS n"),
            ("career events", f"MATCH (e:{MARKER}_CareerEvent {{ICKG_corpus:'{c}'}}) RETURN count(e) AS n"),
            ("persons grounded to Wikidata",
             f"MATCH (p:{MARKER}_Person {{ICKG_corpus:'{c}'}}) WHERE p.wikidata_qid <> '' RETURN count(p) AS n"),
        ]:
            print(f"  {name:32} {s.run(q).single()['n']:,}")
    driver.close()
    print(f"\nDone. Loaded corpus {CORPUS!r} into {URI} / db {DATABASE!r} "
          f"(label namespace :{MARKER}).")


if __name__ == "__main__":
    main()
