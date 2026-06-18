"""Assemble the unified person-career knowledge graph.

Joins every grounding the project produced into one queryable artifact:
  - biography Persons (the cross-colony spine) with their dated career
    observations, sourced from the staff-list records of the stints they were
    matched to, plus confirmed recovered records (flagged as proposals);
  - record-only provisional Persons — one per ungrounded COL_Official stint
    (the upstream already groups a name's consecutive years within one colony;
    we do NOT stitch across colonies);
  - duplicate biographies linked (never merged) via same_person_group_id;
  - colony-year / institution rollups for institutional and temporal analysis.

Outputs JSONL node/edge tables under data/services/graph/. Read-only;
recovered rows are proposals, tagged source="recovered", never silently mixed
with graph facts. Quarantine filters from the data contract are applied.
"""

from __future__ import annotations

import json
from collections import defaultdict
from pathlib import Path

from ..graph import _keep_record
from . import gazetteer
from .compile import _pos_norm
from .match import _norm, _tenures
from .schema import Biography


def _union_find(pairs: list[tuple[str, str]]) -> dict[str, str]:
    parent: dict[str, str] = {}

    def find(x: str) -> str:
        parent.setdefault(x, x)
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for a, b in pairs:
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[ra] = rb
    return {x: find(x) for x in parent}


def _obs_from_record(person_id: str, r: dict, stint_id: str,
                     score: float | None) -> dict:
    return {
        "person_id": person_id, "year": r["year"], "colony": r.get("colony"),
        "department": r.get("department_raw"),
        "position_raw": r.get("position_raw"),
        "position_norm": _pos_norm(r.get("position_raw")) or None,
        "salary_min": r.get("salary_min"), "salary_max": r.get("salary_max"),
        "military_rank": r.get("military_rank"), "honors": r.get("honors") or [],
        "source": "graph", "provenance": stint_id, "grounding_score": score,
    }


def assemble_graph(
    bios: list[Biography], officials: list[dict],
    stint_matches: list[dict], attachments: list[dict],
    recovered: list[dict], merge_groups: list[dict],
    coclaim_pairs: list[dict], candidate_bio_ids: set[str],
    gap_index: dict[tuple[str, int], dict], data_dir: str, out_dir: Path,
) -> dict:
    officials_by_id = {o["id"]: o for o in officials}
    # defensive quarantine filter (cache is already filtered)
    for o in officials:
        o["records"] = [r for r in o["records"] if _keep_record(r)]

    # --- grounding: assign each grounded stint to exactly one owner bio ------
    stint_claims: dict[str, list[str]] = defaultdict(list)
    for m in stint_matches:
        stint_claims[m["official_id"]].append(m["bio_id"])
    stint_owner: dict[str, str] = {
        sid: min(bids) for sid, bids in stint_claims.items()}
    bio_stints: dict[str, list[str]] = defaultdict(list)
    for sid, owner in stint_owner.items():
        bio_stints[owner].append(sid)

    # dated attachment scores: (bio_id, stint_id, year) -> score
    att_score: dict[tuple[str, str, int], float] = {}
    bio_att_years: dict[str, set[int]] = defaultdict(set)
    for a in attachments:
        att_score[(a["bio_id"], a["stint_id"], a["year"])] = a.get("score")
        bio_att_years[a["bio_id"]].add(a["year"])

    grounded_bios = set(bio_stints) | set(bio_att_years)

    persons: list[dict] = []
    observations: list[dict] = []
    bio_event_rows: list[dict] = []
    honour_rows: list[dict] = []
    grounding_rows: list[dict] = []

    # --- biography persons ---------------------------------------------------
    for bio in bios:
        pid = bio.bio_id
        obs: list[dict] = []
        for sid in bio_stints.get(pid, []):
            o = officials_by_id.get(sid)
            if not o:
                continue
            grounding_rows.append({"bio_id": pid, "stint_id": sid,
                                   "kind": "stint_match"})
            for r in o["records"]:
                score = att_score.get((pid, sid, r["year"]))
                obs.append(_obs_from_record(pid, r, sid, score))
        observations.extend(obs)

        colonies = sorted({ob["colony"] for ob in obs if ob["colony"]})
        years = [ob["year"] for ob in obs if ob["year"]]
        persons.append({
            "person_id": pid, "kind": "biography",
            "surname": bio.surname, "given_names": bio.given_names,
            "birth_year": bio.birth_year.value if bio.birth_year else None,
            "first_year": min(years) if years else None,
            "last_year": max(years) if years else None,
            "colonies": colonies, "n_observations": len(obs),
            "honours": [h.award for h in bio.honours],
            "terminal_kind": bio.terminal.kind if bio.terminal else None,
            "terminal_year": bio.terminal.year if bio.terminal else None,
            "editions": bio.editions, "grounded": pid in grounded_bios,
            "same_person_group_id": None, "source": "biography",
        })
        for h in bio.honours:
            honour_rows.append({"person_id": pid, "award": h.award,
                                "year": h.year})

        # bio events with grounding flag (agreement index OR attachment year)
        grounded_idx = {a.get("bio_event_index") for m in stint_matches
                        if m["bio_id"] == pid for a in m.get("agreements", [])}
        tenures = {idx: (s, e) for idx, s, e in _tenures(bio)}
        for i, ev in enumerate(bio.events):
            g = i in grounded_idx
            if not g and i in tenures:
                s, e = tenures[i]
                g = any(s <= y <= e for y in bio_att_years.get(pid, ()))
            bio_event_rows.append({
                "person_id": pid, "event_index": i, "position": ev.position,
                "place": ev.place, "year_start": ev.year_start,
                "year_end": ev.year_end, "place_inherited": ev.place_inherited,
                "grounded": g})

    # --- confirmed recovered records as observations (proposals) -------------
    for rec in recovered:
        if rec.get("confidence") != "confirmed_in_ocr":
            continue
        pid = rec["predicted_by_bio_id"]
        observations.append({
            "person_id": pid, "year": rec["year"], "colony": rec.get("colony"),
            "department": rec.get("department_raw"),
            "position_raw": rec.get("position_raw"),
            "position_norm": _pos_norm(rec.get("position_raw")) or None,
            "salary_min": None, "salary_max": None, "military_rank": None,
            "honors": rec.get("honors") or [], "source": "recovered",
            "provenance": f"{rec['source_file']}:{rec['source_line']}",
            "grounding_score": None})
        grounding_rows.append({"bio_id": pid, "stint_id": None,
                               "kind": "recovered"})

    # --- record-only provisional persons -------------------------------------
    for o in officials:
        if o["id"] in stint_owner or not o["records"]:
            continue
        pid = o["id"]
        for r in o["records"]:
            observations.append(_obs_from_record(pid, r, pid, None))
        years = [r["year"] for r in o["records"]]
        rec0 = o["records"][0]
        persons.append({
            "person_id": pid, "kind": "record_only",
            "surname": rec0.get("surname"), "given_names": rec0.get("given_names"),
            "birth_year": None, "first_year": min(years), "last_year": max(years),
            "colonies": [o["colony"]], "n_observations": len(o["records"]),
            "honours": sorted({h for r in o["records"] for h in (r.get("honors") or [])}),
            "terminal_kind": None, "terminal_year": None, "editions": o.get("editions", []),
            "grounded": False, "same_person_group_id": None, "source": "record_only"})

    # --- duplicate links (link, never merge) ---------------------------------
    pairs: list[tuple[str, str]] = []
    conf: dict[frozenset, str] = {}
    for g in merge_groups:
        ids = g.get("bio_ids", [])
        for j in range(1, len(ids)):
            pairs.append((ids[0], ids[j]))
    for p in coclaim_pairs:
        pairs.append((p["bio_a"], p["bio_b"]))
    confirmed_pairs = {frozenset((g["bio_ids"][0], b))
                       for g in merge_groups for b in g["bio_ids"][1:]}
    roots = _union_find(pairs)
    groups: dict[str, list[str]] = defaultdict(list)
    for node, root in roots.items():
        groups[root].append(node)
    same_person_rows: list[dict] = []
    bio_group: dict[str, str] = {}
    for gi, (root, members) in enumerate(sorted(groups.items())):
        gid = f"spg_{gi:04d}"
        has_confirmed = any(frozenset((a, b)) in confirmed_pairs
                            for a in members for b in members if a != b)
        for m in members:
            bio_group[m] = gid
        same_person_rows.append({
            "group_id": gid, "members": sorted(members),
            "confidence": "confirmed" if has_confirmed else "coclaim"})
    for p in persons:
        if p["person_id"] in bio_group:
            p["same_person_group_id"] = bio_group[p["person_id"]]

    # --- rollups -------------------------------------------------------------
    cy: dict[tuple, dict] = {}
    inst: dict[tuple, set] = defaultdict(set)
    for ob in observations:
        if ob["colony"] is None or ob["year"] is None:
            continue
        k = (ob["colony"], ob["year"])
        c = cy.setdefault(k, {"colony": ob["colony"], "year": ob["year"],
                              "persons": set(), "n_observations": 0})
        c["persons"].add(ob["person_id"])
        c["n_observations"] += 1
        if ob["department"]:
            inst[(ob["colony"], ob["year"], ob["department"])].add(ob["person_id"])
    colony_year_rows = [{"colony": v["colony"], "year": v["year"],
                         "n_persons": len(v["persons"]),
                         "n_observations": v["n_observations"]}
                        for v in cy.values()]
    institution_rows = [{"colony": c, "year": y, "department": d,
                         "n_persons": len(ps)}
                        for (c, y, d), ps in inst.items()]

    # --- completeness ledger over placed+dated biography events --------------
    ledger = {"grounded": 0, "scale_adjudication_addressable": 0,
              "extraction_addressable": 0, "ceiling": 0}
    for row in bio_event_rows:
        if row["year_start"] is None or not row["place"]:
            continue  # only placed+dated events are groundable
        if row["grounded"]:
            ledger["grounded"] += 1
            continue
        gap = gap_index.get((row["person_id"], row["event_index"]))
        if gap is None:
            # not grounded, not a gap -> person present in graph under
            # surname+initials: a candidate the scale adjudication would rule on
            ledger["scale_adjudication_addressable"] += 1
        elif gap.get("source_file"):
            ledger["extraction_addressable"] += 1
        else:
            ledger["ceiling"] += 1

    # --- write ---------------------------------------------------------------
    out_dir.mkdir(parents=True, exist_ok=True)
    files = {
        "persons.jsonl": persons, "observations.jsonl": observations,
        "bio_events.jsonl": bio_event_rows, "honours.jsonl": honour_rows,
        "same_person_groups.jsonl": same_person_rows,
        "grounding.jsonl": grounding_rows, "colony_year.jsonl": colony_year_rows,
        "institution.jsonl": institution_rows,
    }
    for name, rows in files.items():
        with (out_dir / name).open("w", encoding="utf-8") as fh:
            for r in rows:
                fh.write(json.dumps(r, ensure_ascii=False) + "\n")

    bio_persons = [p for p in persons if p["kind"] == "biography"]
    stats = {
        "persons_total": len(persons),
        "biography_persons": len(bio_persons),
        "biography_persons_grounded": sum(1 for p in bio_persons if p["grounded"]),
        "record_only_persons": sum(1 for p in persons if p["kind"] == "record_only"),
        "observations_total": len(observations),
        "observations_graph": sum(1 for o in observations if o["source"] == "graph"),
        "observations_recovered": sum(1 for o in observations if o["source"] == "recovered"),
        "colony_year_cells": len(colony_year_rows),
        "same_person_groups": len(same_person_rows),
        "same_person_confirmed": sum(1 for g in same_person_rows if g["confidence"] == "confirmed"),
        "completeness_ledger": ledger,
    }
    (out_dir / "graph_stats.json").write_text(json.dumps(stats, indent=1))
    return stats


def load_duckdb(out_dir: Path) -> str:
    """Load career_graph.duckdb from the JSONL tables. JSONL is canonical; if
    duckdb is unavailable this is skipped."""
    try:
        import duckdb
    except ImportError:
        return "duckdb not installed; JSONL is canonical (pip install duckdb to enable)"
    tmp = out_dir / "career_graph.duckdb.tmp"
    if tmp.exists():
        tmp.unlink()
    con = duckdb.connect(str(tmp))
    for f in sorted(out_dir.glob("*.jsonl")):
        table = f.stem
        con.execute(
            f"CREATE TABLE {table} AS SELECT * FROM read_json_auto('{f}', "
            f"format='newline_delimited', union_by_name=true)")
    con.close()
    final = out_dir / "career_graph.duckdb"
    tmp.replace(final)
    return f"wrote {final}"


def write_report(stats: dict, out_dir: Path) -> None:
    L = stats["completeness_ledger"]
    tot = sum(L.values()) or 1
    lines = [
        "# Unified person-career graph", "",
        f"- Persons: **{stats['persons_total']:,}** "
        f"({stats['biography_persons']:,} biography, "
        f"{stats['record_only_persons']:,} record-only provisional)",
        f"- Biography persons grounded to >=1 staff-list record: "
        f"**{stats['biography_persons_grounded']:,}** / {stats['biography_persons']:,}",
        f"- Career observations: **{stats['observations_total']:,}** "
        f"({stats['observations_graph']:,} graph, "
        f"{stats['observations_recovered']:,} recovered-proposal)",
        f"- Colony-year cells: {stats['colony_year_cells']:,}",
        f"- Same-person groups (linked, not merged): {stats['same_person_groups']} "
        f"({stats['same_person_confirmed']} adjudicator-confirmed)",
        "", "## Completeness ledger (placed+dated biography career clauses)", "",
        "Where the ungrounded career clauses sit, and which lever would ground "
        "them — the basis for the two go/no-go decisions:", "",
        "| bucket | clauses | share |", "|---|---|---|",
    ]
    label = {"grounded": "already grounded",
             "scale_adjudication_addressable": "→ scale adjudication (candidate exists in graph)",
             "extraction_addressable": "→ extraction backfill (record recoverable from OCR)",
             "ceiling": "ceiling (no candidate, no source)"}
    for k in ("grounded", "scale_adjudication_addressable",
              "extraction_addressable", "ceiling"):
        lines.append(f"| {label[k]} | {L[k]:,} | {L[k]/tot*100:.0f}% |")
    (out_dir / "reports").mkdir(parents=True, exist_ok=True)
    (out_dir / "reports" / "graph_report.md").write_text("\n".join(lines) + "\n")
