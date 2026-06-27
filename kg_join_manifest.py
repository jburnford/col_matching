#!/usr/bin/env python3
"""Ground colony-level place queries from the curated empire-evolution manifest.

The colonies already have vetted, period-specific Wikidata QIDs in
empire-evolution-wpcs/data/qid_manifest.tsv (740 colonies, dates, type, modern
nation). We JOIN our grounding worklist against it instead of re-grounding
colonies via MCP — only the long tail of towns/districts needs MCP afterwards.

Matching: a worklist query matches a manifest row when their names agree after
stripping colonial-type words (colony/protectorate/of/and/…), e.g.
"Nigeria" == strip("Colony and Protectorate of Nigeria"). Candidates are filtered
to the colonial era (active 1850-1965). A single resulting QID is assigned
directly; genuinely multi-entity names (Singapore city vs Crown Colony, Canada
Dominion vs Province) are resolved by MANUAL_PICK below — period-appropriate
choices logged to manifest_picks_review.jsonl for later human review.

Writes one cache row per surface variant into data/kg/places_grounding.jsonl
(match_type "manifest" / "manifest_review"), preserving any existing non-manifest
(e.g. MCP-grounded town) rows. Unmatched queries -> places_worklist.mcp.jsonl.
"""
from __future__ import annotations

import csv
import json
import re
from collections import defaultdict
from pathlib import Path

from col_match.kg import ground as G

MANIFEST = Path("/home/jic823/empire-evolution-wpcs/data/qid_manifest.tsv")
WORKLIST = Path("data/kg/places_worklist.grounding.jsonl")
MCP_TODO = Path("data/kg/places_worklist.mcp.jsonl")
REVIEW = Path("data/kg/manifest_picks_review.jsonl")

_TYPE = re.compile(
    r"\b(colony|colonial|protectorate|crown|settlement|settlements|dominion|"
    r"territory|territories|province|of|and|the|british|presidency|state|company)\b")


def _norm(s: str) -> str:
    return re.sub(r"\s+", " ", re.sub(r"[^a-z0-9 ]", " ", (s or "").lower())).strip()


def _strip_type(s: str) -> str:
    return re.sub(r"\s+", " ", _TYPE.sub(" ", _norm(s))).strip()


# Period-appropriate picks for names that map to >1 era QID (corpus is 1867-1966).
# Keyed by lowercased query string. Reviewable in manifest_picks_review.jsonl.
MANUAL_PICK = {
    "singapore": "Q4373718",                 # Singapore Crown Colony (not modern city)
    # India: bare surface else matches "Dominion of India" Q1775277 (1947). The
    # corpus is the Raj era -> British Raj. (manifest "Indian Empire (British Raj)")
    "india": "Q129286", "british india": "Q129286",
    "dominion of india": "Q129286",
    "canada": "Q16", "dominion of canada": "Q16",
    "province of canada": "Q1121436",
    "sarawak": "Q1658411",                   # Raj of Sarawak (Brooke, 1841-1946)
    "north borneo": "Q1147441", "british north borneo": "Q1147441",
    "british north borneo company": "Q1147441",
    "aden": "Q49910", "aden colony": "Q49910",
    "aden protectorate": "Q1865132",
    "aden settlement": "Q17509767",
    "bechuanaland": "Q747314", "bechuanaland protectorate": "Q747314",
    "british bechuanaland": "Q4530733",
    "newfoundland": "Q2984260",              # Colony of Newfoundland
    "new brunswick": "Q1965", "province of new brunswick": "Q1965",
    "british columbia": "Q1973", "colony of british columbia": "Q918861",
    "columbia": "Q1973",
    "nova scotia": "Q1952", "province of nova scotia": "Q1952",
    "british new guinea": "Q2645837", "new guinea": "Q2645837",
    "territory of new guinea": "Q1443945",
}


def _era_ok(r) -> bool:
    try:
        est = int(r["established_year"])
    except Exception:
        est = 1700
    end = 2000
    m = re.match(r"(\d{4})", r.get("end_date", "") or "")
    if m:
        end = int(m.group(1))
    return est <= 1965 and end >= 1850


def main() -> None:
    rows = list(csv.DictReader(MANIFEST.open(encoding="utf-8"), delimiter="\t"))
    by_qid = {r["wikidata_id"]: r for r in rows if r["wikidata_id"]}
    idx = defaultdict(list)
    for r in rows:
        for k in (r["name"], r["canonical_name"]):
            if k:
                idx[_strip_type(k)].append(r)

    wl = [json.loads(l) for l in WORKLIST.open(encoding="utf-8") if not l.startswith("#")]

    # preserve existing non-manifest cache rows (e.g. MCP-grounded towns)
    existing = []
    if G.CACHE.exists():
        existing = [json.loads(l) for l in G.CACHE.open(encoding="utf-8")]
    keep = [r for r in existing if r.get("match_type") not in ("manifest", "manifest_review")]

    out_rows = list(keep)
    review = []
    mcp_todo = []
    n_clean = n_pick = n_mcp = 0

    def emit(wlrow, qid, rinfo, match_type):
        verdict = {
            "country_qid": (rinfo.get("modern_nation_qids", "") or "").split(";")[0] or None,
            "p131_qid": None,
            "instance_of": [rinfo.get("colony_type")] if rinfo.get("colony_type") else [],
            "has_coords": None,
        }
        label = rinfo.get("name") or rinfo.get("canonical_name")
        targets = [wlrow["query"]] if wlrow.get("context_resolved") else \
                  ([v[0] for v in wlrow.get("variants", [])] or [wlrow["query"]])
        for place in targets:
            row = G.make_row(place, qid, label, verdict, match_type)
            row["query"] = wlrow["query"]
            row["count"] = wlrow.get("count")
            out_rows.append(row)

    for w in wl:
        key = _strip_type(w["query"])
        cands = idx.get(key)
        if not cands:
            mcp_todo.append(w)
            n_mcp += 1
            continue
        pool = [r for r in cands if _era_ok(r)] or cands
        qids = sorted({r["wikidata_id"] for r in pool if r["wikidata_id"]})
        if len(qids) == 1:
            emit(w, qids[0], pool[0], "manifest")
            n_clean += 1
        else:
            pick = MANUAL_PICK.get(w["query"].lower())
            if pick and pick in by_qid:
                emit(w, pick, by_qid[pick], "manifest_review")
                n_pick += 1
                review.append({"query": w["query"], "count": w["count"],
                               "picked": pick, "picked_name": by_qid[pick]["name"],
                               "alternatives": qids})
            else:
                mcp_todo.append(w)
                n_mcp += 1

    # dedupe by place, last write wins (manifest > preserved stub)
    deduped = {r["place"]: r for r in out_rows}
    out_rows = list(deduped.values())
    with G.CACHE.open("w", encoding="utf-8") as fh:
        for r in out_rows:
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")
    with MCP_TODO.open("w", encoding="utf-8") as fh:
        fh.write(f"# {len(mcp_todo)} queries with no manifest match -> ground via MCP (place-disambig)\n")
        for w in sorted(mcp_todo, key=lambda x: -x.get("count", 0)):
            fh.write(json.dumps(w, ensure_ascii=False) + "\n")
    with REVIEW.open("w", encoding="utf-8") as fh:
        for r in sorted(review, key=lambda x: -x["count"]):
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")

    mentions = sum(w["count"] for w in wl)
    done_m = sum(w["count"] for w in wl if _strip_type(w["query"]) in idx
                 and (len({r["wikidata_id"] for r in (([r for r in idx[_strip_type(w["query"])] if _era_ok(r)]) or idx[_strip_type(w["query"])]) if r["wikidata_id"]}) == 1
                      or w["query"].lower() in MANUAL_PICK))
    print(f"manifest clean matches: {n_clean}")
    print(f"manifest manual picks:  {n_pick}  (-> {REVIEW.name})")
    print(f"-> grounded mentions:   {done_m}/{mentions} ({100*done_m/mentions:.0f}%)")
    print(f"to MCP (town tail):     {n_mcp} queries -> {MCP_TODO.name}")
    print(f"cache rows written:     {len(out_rows)} ({len(keep)} preserved non-manifest)")


if __name__ == "__main__":
    main()
