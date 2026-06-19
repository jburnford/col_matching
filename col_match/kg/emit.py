"""Assemble the biography knowledge graph into JSONL node/edge tables.

Joins the validated LLM structure (struct_valid.jsonl) with the person spine
(persons.jsonl), the place grounding cache (places_grounding.jsonl) and the
empire-KG colony resolution, and writes node/edge tables under data/kg/graph/.
Mirrors the field conventions of services/assemble.py so a later RDF/CIDOC-CRM
or Neo4j emitter is a thin add-on.

Tables (all JSONL):
  persons.jsonl        person nodes (identity + provenance)
  career_events.jsonl  edges: person -> (position, place_qid, colony_qid, span)
  honours.jsonl        person -> award (+year)
  education.jsonl      person -> education string
  status.jsonl         person -> career status (active/retired/died/...)
  places.jsonl         place nodes (grounded QID + resolved colony)
Every row carries the canonical entry's (edition, page, block, bbox) provenance.
"""

from __future__ import annotations

import json
from pathlib import Path

from ..volume import status as status_mod
from . import colony as colony_mod
from . import ground as ground_mod
from .normalize import position_norm


def _load(path: Path) -> list[dict]:
    return [json.loads(l) for l in path.open(encoding="utf-8")] if path.exists() else []


def _bios_index() -> dict[str, dict]:
    out = {}
    for f in Path("data/kg/bios").glob("*.jsonl"):
        for l in f.open(encoding="utf-8"):
            b = json.loads(l)
            out[b["bio_id"]] = b
    return out


def build_kg(out_dir: Path) -> dict:
    structs = {s["person_id"]: s for s in _load(out_dir / "struct_valid.jsonl")}
    persons = [p for p in _load(out_dir / "persons.jsonl") if p["person_id"] in structs]
    bios = _bios_index()
    gcache = ground_mod.load_cache()
    # resolve colony once per grounded place
    colony_of = {pl: colony_mod.resolve_colony(row) for pl, row in gcache.items()}

    gdir = out_dir / "graph"
    gdir.mkdir(parents=True, exist_ok=True)
    f_persons = (gdir / "persons.jsonl").open("w", encoding="utf-8")
    f_events = (gdir / "career_events.jsonl").open("w", encoding="utf-8")
    f_hon = (gdir / "honours.jsonl").open("w", encoding="utf-8")
    f_edu = (gdir / "education.jsonl").open("w", encoding="utf-8")
    f_status = (gdir / "status.jsonl").open("w", encoding="utf-8")

    stats = {"persons": 0, "events": 0, "events_grounded": 0, "events_with_colony": 0,
             "honours": 0}
    for p in persons:
        s = structs[p["person_id"]]
        prov = p.get("provenance", [])
        canon = bios.get(p["canonical_bio_id"], {})
        f_persons.write(json.dumps({
            "person_id": p["person_id"], "surname": s.get("surname") or p["surname"],
            "given_names": s.get("given_names") or p.get("given_names"),
            "birth_year": s.get("birth_year") or p.get("birth_year"),
            "education": s.get("education"),
            "editions": p.get("editions", []), "n_attestations": p.get("n_attestations"),
            "canonical_bio_id": p["canonical_bio_id"], "provenance": prov,
        }, ensure_ascii=False) + "\n")
        stats["persons"] += 1

        for i, ev in enumerate(s.get("events") or []):
            place = ev.get("place")
            g = gcache.get(place) if place else None
            col = colony_of.get(place) if place else None
            row = {
                "person_id": p["person_id"], "seq": i,
                "position": ev.get("position"),
                "position_norm": position_norm(ev.get("position")),
                "place_raw": place,
                "place_qid": (g or {}).get("qid"),
                "place_label": (g or {}).get("label"),
                "colony_qid": (col or {}).get("colony_qid"),
                "colony_label": (col or {}).get("colony_label"),
                "year_start": ev.get("year_start"), "year_end": ev.get("year_end"),
                "place_inherited": ev.get("place_inherited", False),
                "is_acting": ev.get("is_acting", False),
                "org_type": ev.get("org_type", "civil"),
                "grounded": bool((g or {}).get("qid")),
                "provenance": prov,
            }
            f_events.write(json.dumps(row, ensure_ascii=False) + "\n")
            stats["events"] += 1
            stats["events_grounded"] += bool(row["grounded"])
            stats["events_with_colony"] += bool(row["colony_qid"])

        for h in s.get("honours") or []:
            f_hon.write(json.dumps({"person_id": p["person_id"], **h}, ensure_ascii=False) + "\n")
            stats["honours"] += 1
        if s.get("education"):
            f_edu.write(json.dumps({"person_id": p["person_id"], "education": s["education"]},
                                   ensure_ascii=False) + "\n")
        st = status_mod.classify_status(canon.get("raw_text", ""), s.get("events") or [],
                                        p.get("canonical_edition", 0))
        f_status.write(json.dumps({"person_id": p["person_id"], **st}, ensure_ascii=False) + "\n")

    for fh in (f_persons, f_events, f_hon, f_edu, f_status):
        fh.close()

    # place nodes
    with (gdir / "places.jsonl").open("w", encoding="utf-8") as fh:
        for pl, row in gcache.items():
            col = colony_of.get(pl, {})
            fh.write(json.dumps({**row, "colony_qid": col.get("colony_qid"),
                                 "colony_label": col.get("colony_label")},
                                ensure_ascii=False) + "\n")
    (gdir / "kg_stats.json").write_text(json.dumps(stats, indent=2))
    return stats
