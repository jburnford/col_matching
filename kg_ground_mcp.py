#!/usr/bin/env python3
"""Drive Wikidata MCP grounding of the place worklist into the project cache.

The MCP lookups themselves are performed by the agent (per the place-disambig
skill: search_items -> get_statements, historical-entity + skip rules, <=5
parallel). This helper does the deterministic I/O around that loop:

  pending --n N        print the next N ungrounded canonical queries (with their
                       surface variants) for the agent to look up.
  record --results F   read the agent's results JSON and fan each grounded query
                       out to one cache row PER surface variant (so emit.py, which
                       keys data/kg/places_grounding.jsonl by `place`, resolves
                       every printed form to the same QID). Context-resolved
                       queries are written keyed by the resolved query string.

Results JSON: a list of objects
  {"query": "Nigeria", "qid": "Q1033", "label": "Nigeria",
   "country_qid": "Q145", "p131_qid": null, "instance_of": ["country"],
   "has_coords": true, "match_type": "mcp_verified"}   # or "ungrounded" (qid null)
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

from col_match.kg import ground as G

WORKLIST = Path("data/kg/places_worklist.grounding.jsonl")


def _load_worklist():
    return [json.loads(l) for l in WORKLIST.open(encoding="utf-8")
            if not l.startswith("#")]


def _grounded_queries() -> set[str]:
    """Queries already in the cache (tracked via the `query` field we write)."""
    done = set()
    if G.CACHE.exists():
        for l in G.CACHE.open(encoding="utf-8"):
            r = json.loads(l)
            if r.get("query"):
                done.add(r["query"])
    return done


def cmd_pending(args):
    done = _grounded_queries()
    rows = [r for r in _load_worklist() if r["query"] not in done]
    rows = rows[:args.n]
    for r in rows:
        variants = [v[0] for v in r.get("variants", [])] or [r["query"]]
        print(json.dumps({"query": r["query"], "count": r["count"],
                          "context_resolved": bool(r.get("context_resolved")),
                          "variants": variants}, ensure_ascii=False))


def _read_results(path: str) -> list[dict]:
    """Accept either a JSON array or JSONL (one object per line)."""
    text = Path(path).read_text(encoding="utf-8").strip()
    if text.startswith("["):
        return json.loads(text)
    return [json.loads(l) for l in text.splitlines() if l.strip()]


def cmd_record(args):
    results = _read_results(args.results)
    wl = {r["query"]: r for r in _load_worklist()}
    n_rows = n_q = 0
    for res in results:
        q = res["query"]
        wlrow = wl.get(q, {})
        verdict = {"country_qid": res.get("country_qid"),
                   "p131_qid": res.get("p131_qid"),
                   "instance_of": res.get("instance_of", []),
                   "has_coords": res.get("has_coords")}
        mt = res.get("match_type", "mcp_unverified" if res.get("qid") else "ungrounded")
        # targets to key the cache by: variants for surface queries, the resolved
        # query string for context-resolved ones (applied per-person in emit).
        if wlrow.get("context_resolved"):
            targets = [q]
        else:
            targets = [v[0] for v in wlrow.get("variants", [])] or [q]
        for place in targets:
            row = G.make_row(place, res.get("qid"), res.get("label"), verdict, mt)
            row["query"] = q
            row["count"] = wlrow.get("count")
            row["has_coords"] = res.get("has_coords")
            if wlrow.get("context_resolved"):
                row["context_resolved"] = True
            G.append(row)
            n_rows += 1
        n_q += 1
    print(f"recorded {n_q} queries -> {n_rows} cache rows in {G.CACHE}")


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("pending"); p.add_argument("--n", type=int, default=50)
    p.set_defaults(fn=cmd_pending)
    r = sub.add_parser("record"); r.add_argument("--results", required=True)
    r.set_defaults(fn=cmd_record)
    args = ap.parse_args()
    args.fn(args)


if __name__ == "__main__":
    main()
