#!/usr/bin/env python3
"""Seed the IOL grounding caches from the existing single-year 1937 KG.

The `/home/jic823/indianofficelist` project already grounded India places and
education institutions to Wikidata (human-reviewed). Rather than re-pay the MCP
cost, fold those QIDs into the col_matching grounding caches as zero-cost seeds
so the Phase-5 grounding loop skips them. Read-only on the 1937 KG; writes only
under $COL_KG_OUT (default data/kg — set COL_KG_OUT=data/iol for the IOL build).

Mapping:
  1937 Place           {name, alt_names, wikidata_qid, wikidata_label}
    -> places_grounding.jsonl  {place, qid, label, ..., match_type: seed_iol1937}
       (one row per name + each alt_name surface)
  1937 EducationInstitution {name, institution_type, wikidata_qid, wikidata_label}
    -> institutions_grounding.jsonl {institution, type, id, label, ...,
       source: seed_iol1937, match_type: mcp_verified}

Idempotent: existing cache keys are preserved (seed never overwrites a real
grounding); only new surfaces are appended.

  COL_KG_OUT=data/iol python3 kg_seed_from_iol1937.py
"""
from __future__ import annotations

import json
from pathlib import Path

from col_match.kg.paths import kg_out

KG1937 = Path("/home/jic823/indianofficelist/knowledge_graph_final.json")


def _load_nodes() -> list[dict]:
    kg = json.loads(KG1937.read_text(encoding="utf-8"))
    return kg["nodes"] if isinstance(kg, dict) else kg


def _existing_keys(path: Path, key: str) -> set[str]:
    if not path.exists():
        return set()
    out = set()
    for l in path.open(encoding="utf-8"):
        try:
            out.add(json.loads(l)[key])
        except Exception:
            pass
    return out


def seed_places(nodes: list[dict], out_dir: Path) -> int:
    path = out_dir / "places_grounding.jsonl"
    have = _existing_keys(path, "place")
    rows = []
    seen = set()
    for n in nodes:
        if n.get("label") != "Place" or not n.get("wikidata_qid"):
            continue
        qid, lab = n["wikidata_qid"], n.get("wikidata_label") or n.get("name")
        surfaces = {n.get("name")} | set(n.get("alt_names") or [])
        for s in surfaces:
            s = (s or "").strip()
            if not s or s in have or s in seen:
                continue
            seen.add(s)
            rows.append({"place": s, "qid": qid, "label": lab,
                         "country_qid": None, "p131_qid": None,
                         "instance_of": [], "has_coords": False,
                         "match_type": "seed_iol1937"})
    with path.open("a", encoding="utf-8") as fh:
        for r in rows:
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")
    return len(rows)


def seed_institutions(nodes: list[dict], out_dir: Path) -> int:
    path = out_dir / "institutions_grounding.jsonl"
    have = _existing_keys(path, "institution")
    rows = []
    seen = set()
    for n in nodes:
        if n.get("label") != "EducationInstitution" or not n.get("wikidata_qid"):
            continue
        name = (n.get("name") or "").strip()
        if not name or name in have or name in seen:
            continue
        seen.add(name)
        rows.append({"institution": name, "type": n.get("institution_type") or "",
                     "id": n["wikidata_qid"], "label": n.get("wikidata_label") or name,
                     "instance_of": [], "country_qid": None,
                     "source": "seed_iol1937", "match_type": "mcp_verified"})
    with path.open("a", encoding="utf-8") as fh:
        for r in rows:
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")
    return len(rows)


def main() -> None:
    out_dir = kg_out()
    out_dir.mkdir(parents=True, exist_ok=True)
    nodes = _load_nodes()
    np = seed_places(nodes, out_dir)
    ni = seed_institutions(nodes, out_dir)
    print(f"seeded {np} place surfaces + {ni} education institutions from the "
          f"1937 KG -> {out_dir}/ (places_grounding.jsonl, institutions_grounding.jsonl)")


if __name__ == "__main__":
    main()
