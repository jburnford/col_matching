#!/usr/bin/env python3
"""Load the v3 knowledge graph into an embedded LadybugDB (Kuzu-fork) Cypher database.

Graph model (reified career events so person/role/org/place are all traversable):

  (Person)-[:HAS_EVENT]->(CareerEvent)-[:EVENT_ROLE]->(Role)
                          (CareerEvent)-[:EVENT_ORG]->(Organisation)
                          (CareerEvent)-[:EVENT_PLACE]->(Place)
                          (CareerEvent)-[:EVENT_COLONY]->(Place)
  (Person)-[:RECEIVED]->(Honour)
  (Person)-[:HOLDS_QUAL]->(Qualification)
  (Person)-[:EDUCATED_AT]->(Institution)

CareerEvent carries year_start/year_end/is_acting/position_raw. Nodes carry their
grounded id (Wikidata QID or colkg:) + label. Bulk-loaded via Parquet COPY FROM.

Usage:  python3 kg_load_ladybug.py   (rebuilds data/kg/ladybug_db from scratch)
"""
from __future__ import annotations
import json, shutil, tempfile
from pathlib import Path
import pandas as pd
import ladybug

GD = Path("data/kg/graph_stage3")
DB = Path("data/kg/ladybug_db")

def L(f):
    return [json.loads(l) for l in (GD / f).open()]

def main():
    # ---- read layers -----------------------------------------------------
    persons = L("persons.jsonl")
    places  = L("places.jsonl")
    roles   = L("roles.jsonl")
    orgs    = L("organisations.jsonl")
    insts   = L("institutions.jsonl")
    hons    = L("honour_nodes.jsonl")
    quals   = L("qualification_nodes.jsonl")
    facts   = L("career_facts.jsonl")
    hon_e   = L("honour_edges.jsonl")
    qual_e  = L("qualification_edges.jsonl")
    edu_e   = L("education_edges.jsonl")

    # ---- node frames -----------------------------------------------------
    df_person = pd.DataFrame([{
        "person_id": p["person_id"],
        "surname": p.get("surname") or "",
        "given_names": p.get("given_names") or "",
        "birth_year": p.get("birth_year"),
        "n_attestations": p.get("n_attestations") or 0,
    } for p in persons]).astype({"birth_year": "Int64", "n_attestations": "Int64"})
    person_ids = set(df_person["person_id"])

    # Place = grounded places + any place/colony qid referenced by an event
    place_lbl = {p["qid"]: p.get("label") or p["qid"] for p in places if p.get("qid")}
    place_ctry = {p["qid"]: p.get("country_qid") for p in places if p.get("qid")}
    for f in facts:
        for q, lk in ((f.get("place_qid"), "place_label"), (f.get("colony_qid"), "colony_label")):
            if q and q not in place_lbl:
                place_lbl[q] = f.get(lk) or q
    df_place = pd.DataFrame([{"qid": q, "label": place_lbl[q],
                              "country_qid": place_ctry.get(q) or ""} for q in place_lbl])
    place_ids = set(df_place["qid"])

    # drop any node with a null/blank id (e.g. an 'ambiguous' role surface that
    # never became a real node) -- it would violate the PK non-null constraint.
    def ok(x): return bool(x.get("id")) and str(x["id"]).strip() != ""
    df_role = pd.DataFrame([{"id": r["id"], "label": r.get("label") or r["id"],
                             "category": r.get("category") or "", "source": r.get("source") or ""}
                            for r in roles if ok(r)])
    role_ids = set(df_role["id"])
    df_org = pd.DataFrame([{"id": o["id"], "label": o.get("label") or o["id"],
                            "type": o.get("type") or "", "source": o.get("source") or ""}
                           for o in orgs if ok(o)])
    org_ids = set(df_org["id"])
    df_inst = pd.DataFrame([{"id": i["id"], "label": i.get("label") or i["id"],
                             "type": i.get("type") or "", "source": i.get("source") or ""}
                            for i in insts if ok(i)])
    inst_ids = set(df_inst["id"])
    df_hon = pd.DataFrame([{"id": h["id"], "label": h.get("label") or h["id"],
                            "type": h.get("type") or "", "source": h.get("source") or ""}
                           for h in hons if ok(h)])
    hon_ids = set(df_hon["id"])
    df_qual = pd.DataFrame([{"id": q["id"], "label": q.get("label") or q["id"],
                             "type": q.get("type") or "", "source": q.get("source") or ""}
                            for q in quals if ok(q)])
    qual_ids = set(df_qual["id"])

    # CareerEvent node (reified) -- id = person#seq
    def eid(f): return f"{f['person_id']}#{f['seq']}"
    df_event = pd.DataFrame([{
        "id": eid(f), "year_start": f.get("year_start"), "year_end": f.get("year_end"),
        "is_acting": bool(f.get("is_acting")), "position_raw": f.get("position_raw") or "",
        "role_source": f.get("role_source") or "",
    } for f in facts]).astype({"year_start": "Int64", "year_end": "Int64"})

    # ---- rel frames (filter to existing endpoints) -----------------------
    has_event = pd.DataFrame([{"from": f["person_id"], "to": eid(f)} for f in facts])
    ev_role = pd.DataFrame([{"from": eid(f), "to": f["role_id"],
                             "modifiers": ",".join(f.get("role_modifiers") or [])}
                            for f in facts if f.get("role_id") in role_ids])
    ev_org = pd.DataFrame([{"from": eid(f), "to": f["org_id"]}
                           for f in facts if f.get("org_id") in org_ids])
    ev_place = pd.DataFrame([{"from": eid(f), "to": f["place_qid"]}
                             for f in facts if f.get("place_qid") in place_ids])
    ev_colony = pd.DataFrame([{"from": eid(f), "to": f["colony_qid"]}
                              for f in facts if f.get("colony_qid") in place_ids])
    received = pd.DataFrame([{"from": e["person_id"], "to": e["honour_id"],
                              "year": e.get("year"), "modifiers": ",".join(e.get("modifiers") or [])}
                             for e in hon_e
                             if e["person_id"] in person_ids and e.get("honour_id") in hon_ids]
                            ).astype({"year": "Int64"})
    holds_qual = pd.DataFrame([{"from": e["person_id"], "to": e["qualification_id"],
                                "year": e.get("year")}
                               for e in qual_e
                               if e["person_id"] in person_ids and e.get("qualification_id") in qual_ids]
                              ).astype({"year": "Int64"})
    educated = pd.DataFrame([{"from": e["person_id"], "to": e["institution_id"],
                              "edu_type": e.get("type") or ""}
                             for e in edu_e
                             if e["person_id"] in person_ids and e.get("institution_id") in inst_ids])

    # ---- create db -------------------------------------------------------
    # clean any prior db (single-file or directory layout) + WAL/lock siblings
    for p in [DB, Path(str(DB) + ".wal"), Path(str(DB) + ".lock"), Path(str(DB) + ".tmp")]:
        if p.is_dir():
            shutil.rmtree(p)
        elif p.exists():
            p.unlink()
    db = ladybug.Database(str(DB))
    conn = ladybug.Connection(db)

    ddl = [
        "CREATE NODE TABLE Person(person_id STRING, surname STRING, given_names STRING, birth_year INT64, n_attestations INT64, PRIMARY KEY(person_id))",
        "CREATE NODE TABLE Place(qid STRING, label STRING, country_qid STRING, PRIMARY KEY(qid))",
        "CREATE NODE TABLE Role(id STRING, label STRING, category STRING, source STRING, PRIMARY KEY(id))",
        "CREATE NODE TABLE Organisation(id STRING, label STRING, type STRING, source STRING, PRIMARY KEY(id))",
        "CREATE NODE TABLE Institution(id STRING, label STRING, type STRING, source STRING, PRIMARY KEY(id))",
        "CREATE NODE TABLE Honour(id STRING, label STRING, type STRING, source STRING, PRIMARY KEY(id))",
        "CREATE NODE TABLE Qualification(id STRING, label STRING, type STRING, source STRING, PRIMARY KEY(id))",
        "CREATE NODE TABLE CareerEvent(id STRING, year_start INT64, year_end INT64, is_acting BOOL, position_raw STRING, role_source STRING, PRIMARY KEY(id))",
        "CREATE REL TABLE HAS_EVENT(FROM Person TO CareerEvent)",
        "CREATE REL TABLE EVENT_ROLE(FROM CareerEvent TO Role, modifiers STRING)",
        "CREATE REL TABLE EVENT_ORG(FROM CareerEvent TO Organisation)",
        "CREATE REL TABLE EVENT_PLACE(FROM CareerEvent TO Place)",
        "CREATE REL TABLE EVENT_COLONY(FROM CareerEvent TO Place)",
        "CREATE REL TABLE RECEIVED(FROM Person TO Honour, year INT64, modifiers STRING)",
        "CREATE REL TABLE HOLDS_QUAL(FROM Person TO Qualification, year INT64)",
        "CREATE REL TABLE EDUCATED_AT(FROM Person TO Institution, edu_type STRING)",
    ]
    for q in ddl:
        conn.execute(q)

    # ---- bulk load via parquet COPY FROM ---------------------------------
    tmp = Path(tempfile.mkdtemp())
    def copy(table, df, pk=None):
        # node tables need a unique PK: two surfaces can share one QID, so collapse.
        if pk is not None:
            df = df.drop_duplicates(subset=[pk], keep="first")
        p = tmp / f"{table}.parquet"
        df.to_parquet(p, index=False)
        conn.execute(f"COPY {table} FROM '{p}'")
        print(f"  {table:14} {len(df):>7,}")

    print("nodes:")
    copy("Person", df_person, "person_id"); copy("Place", df_place, "qid")
    copy("Role", df_role, "id"); copy("Organisation", df_org, "id")
    copy("Institution", df_inst, "id"); copy("Honour", df_hon, "id")
    copy("Qualification", df_qual, "id"); copy("CareerEvent", df_event, "id")
    print("rels:")
    copy("HAS_EVENT", has_event); copy("EVENT_ROLE", ev_role); copy("EVENT_ORG", ev_org)
    copy("EVENT_PLACE", ev_place); copy("EVENT_COLONY", ev_colony)
    copy("RECEIVED", received); copy("HOLDS_QUAL", holds_qual); copy("EDUCATED_AT", educated)
    shutil.rmtree(tmp)

    # ---- validation -------------------------------------------------------
    print("\nvalidation:")
    checks = [
        ("persons", "MATCH (p:Person) RETURN count(p)"),
        ("career events", "MATCH (e:CareerEvent) RETURN count(e)"),
        ("event->role->place->time complete",
         "MATCH (e:CareerEvent)-[:EVENT_ROLE]->(:Role), (e)-[:EVENT_PLACE]->(:Place) WHERE e.year_start IS NOT NULL RETURN count(e)"),
        ("top role by people",
         "MATCH (:CareerEvent)-[:EVENT_ROLE]->(r:Role) RETURN r.label, count(*) AS n ORDER BY n DESC LIMIT 1"),
        ("CMG recipients",
         "MATCH (p:Person)-[:RECEIVED]->(h:Honour {id:'Q12177413'}) RETURN count(p)"),
    ]
    for name, q in checks:
        res = conn.execute(q)
        print(f"  {name:38} {res.get_as_df().to_dict('records')}")

if __name__ == "__main__":
    main()
