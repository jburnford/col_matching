#!/usr/bin/env python3
"""Ground institutions (education first, employers/orgs later) to Wikidata QIDs,
minting a stable INTERNAL id where Wikidata has no entity -- so everyone sharing
an ungrounded institution (e.g. "Ceylon Police") still links to one node.

Cache: data/kg/institutions_grounding.jsonl, keyed by `institution` surface, row:
  {institution, type, id, label, instance_of, country_qid, source, match_type}
  id is a Wikidata QID (Q...) OR an internal id `colkg:<Slug>`.

Subcommands:
  pending  [--n 20] [--type school]   top-N uncached institutions, count-desc
  record   <rows.jsonl>               merge MCP/grounding rows into the cache
  internal <names.txt|->               mint colkg: internal ids for listed institutions
  internal-tail [--max-count 1]       mint internal ids for ALL remaining low-count ones
  emit                                institution nodes + education edges
  stats
"""
from __future__ import annotations
import argparse, json, os, re, sys
from pathlib import Path
from collections import defaultdict

# Paths are env-overridable so the same harness serves both the education layer
# (defaults below) and the employer/org layer (COL_WORK=org_worklist.jsonl,
# COL_CACHE=org_grounding.jsonl, COL_NODES=organisations.jsonl,
# COL_EDGES=employment_edges.jsonl).
WORK = Path(os.environ.get("COL_WORK", "data/kg/education_worklist.jsonl"))
CACHE = Path(os.environ.get("COL_CACHE", "data/kg/institutions_grounding.jsonl"))
EMIT_NODES = os.environ.get("COL_NODES", "institutions.jsonl")
EMIT_EDGES = os.environ.get("COL_EDGES", "education_edges.jsonl")

def load_work():
    return [json.loads(l) for l in WORK.open()] if WORK.exists() else []
def load_cache():
    return {r["institution"]: r for r in (json.loads(l) for l in CACHE.open())} if CACHE.exists() else {}
def write_cache(cache):
    with CACHE.open("w") as fh:
        for r in cache.values(): fh.write(json.dumps(r, ensure_ascii=False) + "\n")

def slug(name):
    s = re.sub(r"[^A-Za-z0-9]+", "_", name).strip("_")
    return "colkg:" + re.sub(r"_+", "_", s)

def cmd_pending(a):
    work = load_work(); cache = load_cache()
    pend = [w for w in work if w["institution"] not in cache and (not a.type or w["type"] == a.type)]
    pend.sort(key=lambda w: -w["count"])
    for w in pend[:a.n]:
        print(json.dumps({"institution": w["institution"], "type": w["type"],
                          "count": w["count"], "examples": w["examples"]}, ensure_ascii=False))
    print(f"# {len(pend)} pending ({sum(w['count'] for w in pend):,} mentions); showing {min(a.n,len(pend))}",
          file=sys.stderr)

def cmd_record(a):
    cache = load_cache(); n = 0
    for l in open(a.rows):
        l = l.strip()
        if not l: continue
        r = json.loads(l); cache[r["institution"]] = r; n += 1
    write_cache(cache); print(f"recorded {n}; cache now {len(cache)}")

def cmd_internal(a):
    cache = load_cache(); work = {w["institution"]: w for w in load_work()}
    src = sys.stdin if a.names == "-" else open(a.names)
    n = 0
    for line in src:
        name = line.strip()
        if not name or name in cache: continue
        cache[name] = {"institution": name, "type": work.get(name, {}).get("type", "other"),
                       "id": slug(name), "label": name, "instance_of": [],
                       "country_qid": None, "source": "internal", "match_type": "internal_mint"}
        n += 1
    write_cache(cache); print(f"minted {n} internal ids; cache now {len(cache)}")

def cmd_internal_tail(a):
    cache = load_cache(); work = load_work(); n = 0
    for w in work:
        if w["institution"] in cache or w["count"] > a.max_count: continue
        cache[w["institution"]] = {"institution": w["institution"], "type": w["type"],
            "id": slug(w["institution"]), "label": w["institution"], "instance_of": [],
            "country_qid": None, "source": "internal", "match_type": "internal_mint"}
        n += 1
    write_cache(cache); print(f"minted {n} internal ids (count<={a.max_count}); cache now {len(cache)}")

def cmd_ambiguous(a):
    # Mark a bare, multi-referent surface (e.g. "St. John's College", "King's College")
    # as ambiguous: NOT grounded and NOT internal-minted (which would false-merge distinct
    # institutions into one node). Excluded from emit; queued for a future per-mention
    # context-disambiguation pass that resolves each mention by its surrounding location cue.
    cache = load_cache(); work = {w["institution"]: w for w in load_work()}
    src = sys.stdin if a.names == "-" else open(a.names)
    n = 0
    for line in src:
        name = line.strip()
        if not name: continue
        cache[name] = {"institution": name, "type": work.get(name, {}).get("type", "other"),
                       "id": None, "label": name, "instance_of": [],
                       "country_qid": None, "source": "ambiguous",
                       "match_type": "ambiguous_multi_referent"}
        n += 1
    write_cache(cache); print(f"marked {n} ambiguous; cache now {len(cache)}")

def cmd_emit(a):
    cache = load_cache(); work = {w["institution"]: w for w in load_work()}
    out = Path(os.environ.get("COL_KG_OUT", "data/kg")) / "graph_stage3"
    # institution nodes (skip ambiguous surfaces — they are not real single nodes)
    with (out / EMIT_NODES).open("w") as fh:
        for inst, r in sorted(cache.items()):
            if r.get("source") == "ambiguous": continue
            fh.write(json.dumps({**r, "n_people": work.get(inst, {}).get("count", 0)},
                                ensure_ascii=False) + "\n")
    # edges: person -> institution (one per (person,institution) mention)
    n = 0
    with (out / EMIT_EDGES).open("w") as fh:
        for inst, w in work.items():
            r = cache.get(inst)
            if not r or r.get("source") == "ambiguous": continue
            for pid in w["person_ids"]:
                fh.write(json.dumps({"person_id": pid, "institution": inst, "institution_id": r["id"],
                                     "institution_label": r["label"], "type": r["type"]},
                                    ensure_ascii=False) + "\n")
                n += 1
    n_nodes = sum(1 for r in cache.values() if r.get("source") != "ambiguous")
    print(f"emitted {n_nodes} {EMIT_NODES} nodes, {n} {EMIT_EDGES} -> {out}/")

def cmd_stats(a):
    cache = load_cache(); work = load_work()
    tot_m = sum(w["count"] for w in work)
    cov = sum(w["count"] for w in work if w["institution"] in cache)
    wd = sum(1 for r in cache.values() if str(r["id"]).startswith("Q"))
    intn = sum(1 for r in cache.values() if str(r["id"]).startswith("colkg:"))
    amb = sum(1 for r in cache.values() if r.get("source") == "ambiguous")
    amb_m = sum(w["count"] for w in work
                if cache.get(w["institution"], {}).get("source") == "ambiguous")
    grounded_m = cov - amb_m
    print(f"institutions: {len(work):,} distinct | cached {len(cache):,} "
          f"(Wikidata {wd:,} / internal {intn:,} / ambiguous {amb:,})")
    print(f"mention coverage (grounded+internal): {grounded_m:,}/{tot_m:,} "
          f"({100*grounded_m/tot_m:.1f}%)  | ambiguous-flagged: {amb_m:,} mentions")

ap = argparse.ArgumentParser()
sub = ap.add_subparsers(dest="cmd", required=True)
p = sub.add_parser("pending"); p.add_argument("--n", type=int, default=20); p.add_argument("--type", default=""); p.set_defaults(f=cmd_pending)
p = sub.add_parser("record"); p.add_argument("rows"); p.set_defaults(f=cmd_record)
p = sub.add_parser("internal"); p.add_argument("names"); p.set_defaults(f=cmd_internal)
p = sub.add_parser("internal-tail"); p.add_argument("--max-count", type=int, default=1); p.set_defaults(f=cmd_internal_tail)
p = sub.add_parser("ambiguous"); p.add_argument("names"); p.set_defaults(f=cmd_ambiguous)
p = sub.add_parser("emit"); p.set_defaults(f=cmd_emit)
p = sub.add_parser("stats"); p.set_defaults(f=cmd_stats)
a = ap.parse_args(); a.f(a)
