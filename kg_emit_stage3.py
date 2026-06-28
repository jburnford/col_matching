#!/usr/bin/env python3
"""Emit the v1 knowledge-graph node/edge tables from the Stage-3 person spine.

Reads the deduped structured corpus (llm_struct_corpus.stage3.jsonl, 30,177
persons), joins the place grounding cache (surface-form -> QID) and empire-KG
colony resolution, and writes JSONL node/edge tables under data/kg/graph_stage3/.
A thin RDF/CIDOC-CRM or Neo4j emitter can sit on top of these.

  python3 kg_emit_stage3.py [--out data/kg/graph_stage3]
"""
from __future__ import annotations
import argparse, json, re
from pathlib import Path

from col_match.kg import ground as ground_mod
from col_match.kg import colony as colony_mod
from col_match.kg.normalize import position_norm
from col_match.kg.paths import KG_OUT
from col_match.volume import status as status_mod

ap = argparse.ArgumentParser()
ap.add_argument("--corpus", default=str(KG_OUT / "llm_struct_corpus.stage3.jsonl"))
ap.add_argument("--out", default=str(KG_OUT / "graph_stage3"))
args = ap.parse_args()

gdir = Path(args.out); gdir.mkdir(parents=True, exist_ok=True)
gcache = ground_mod.load_cache()
colony_of = {pl: colony_mod.resolve_colony(row) for pl, row in gcache.items()}

# context-resolution map (abbrev province etc. -> resolved query that was grounded)
from collections import Counter, defaultdict
_per = {}                       # (person_id, place) -> resolved_query
_glob = defaultdict(Counter)    # place -> Counter(resolved_query)
_resmap = KG_OUT / "places_resolution_map.jsonl"
for l in (_resmap.open(encoding="utf-8") if _resmap.exists() else []):
    rr = json.loads(l)
    # the map keys persons by the reviewed-corpus id ("kgp_<bio>"); the spine's
    # `attestations` are bare bio-ids — strip the prefix so per-person resolution
    # (the minority-context override, e.g. Victoria→BC) actually matches.
    pid = rr["person_id"]
    pid = pid[4:] if pid.startswith("kgp_") else pid
    _per[(pid, rr["place"])] = rr["resolved_query"]
    _glob[rr["place"]][rr["resolved_query"]] += 1
_glob1 = {p: c.most_common(1)[0][0] for p, c in _glob.items()}
_ORG = re.compile(r"\b(railway|R\. ?& ?H|posts|telegraph|tels|currency|administration|"
                  r"department|dept|regiment|battalion|C\.O\.|colonial office|customs|"
                  r"constabulary|secretariat|treasury|survey|board|commission|service|"
                  r"corps|command|brigade|K\.A\.R|R\.A\.F|R\.N)\b", re.I)

from col_match.kg.place_canon import canonicalize as _canon

def resolve_place(place, attestations):
    """Return (grounding_row, resolved_via). Direct cache hit, else the
    canonicalised surface (bridges abbreviations like 'United Provs.' to a
    seeded 'United Provinces' QID), else the per-person context map."""
    g = gcache.get(place)
    if g and g.get("qid"): return g, None
    cq = _canon(place)
    if cq != place:
        gc = gcache.get(cq)
        if gc and gc.get("qid"): return gc, cq
    rq = next((_per[(a, place)] for a in attestations if (a, place) in _per), None) or _glob1.get(place)
    if rq:
        g2 = gcache.get(rq)
        if g2 and g2.get("qid"): return g2, rq
    return None, None

# bios index for status-tail classification (by latest attestation)
bio_txt = {}
for f in (KG_OUT / "bios").glob("*.jsonl"):
    if f.name.endswith(".xref.jsonl"):
        continue
    for l in f.open(encoding="utf-8"):
        b = json.loads(l); bio_txt[b["bio_id"]] = b.get("raw_text", "")

def edition(pid):
    m = re.search(r"(col|dol|iol)(\d{4})", pid); return int(m.group(2)) if m else 0
def bioid(pid): return pid[4:] if pid.startswith("kgp_") else pid

rows = [json.loads(l) for l in open(args.corpus)]

# person -> Wikidata QID (verified, zero-FP grounding layer; produced by
# kg_ground_persons.py -> verify_person_qids.py -> apply_person_verification.py)
person_qid = {}
_pgf = gdir / "person_grounding.final.jsonl"
if not _pgf.exists():
    _pgf = gdir / "person_grounding.verified.jsonl"
if _pgf.exists():
    for l in _pgf.open(encoding="utf-8"):
        g = json.loads(l)
        person_qid[g["person_id"]] = (g["qid"], g.get("wd_name"), g.get("tier"))

# person -> Wikidata-has-more flag: grounded persons for whom Wikidata records
# jurisdictions/positions absent from our bios (research signal, NOT imported).
# Produced by /tmp/wd_has_more.py -> wikidata_has_more.json.
person_has_more = {}
_pwm = gdir / "wikidata_has_more.json"
if _pwm.exists():
    for g in json.loads(_pwm.read_text(encoding="utf-8")):
        person_has_more[g["person_id"]] = g.get("n_extra", True)

f_persons = (gdir / "persons.jsonl").open("w", encoding="utf-8")
f_events  = (gdir / "career_events.jsonl").open("w", encoding="utf-8")
f_hon     = (gdir / "honours.jsonl").open("w", encoding="utf-8")
f_edu     = (gdir / "education.jsonl").open("w", encoding="utf-8")
f_status  = (gdir / "status.jsonl").open("w", encoding="utf-8")

stats = {"persons": 0, "events": 0, "events_placed": 0, "events_grounded": 0,
         "events_resolved_via_map": 0, "events_with_colony": 0, "events_org": 0,
         "honours": 0, "education": 0, "places_used": 0}
places_used = set()

for r in rows:
    pid = r["person_id"]
    stats["persons"] += 1
    f_persons.write(json.dumps({
        "person_id": pid,
        "surname": r.get("surname"), "given_names": r.get("given_names"),
        "birth_year": r.get("birth_year"),
        "editions": r.get("editions"), "n_attestations": r.get("n_attestations"),
        "attestations": r.get("attestations"), "flags": r.get("flags", []),
        "wikidata_qid": person_qid.get(pid, (None, None, None))[0],
        "wikidata_label": person_qid.get(pid, (None, None, None))[1],
        "wikidata_tier": person_qid.get(pid, (None, None, None))[2],
        "wikidata_has_more": bool(person_has_more.get(pid)),
        "wikidata_extra_count": person_has_more.get(pid) or 0,
    }, ensure_ascii=False) + "\n")

    atts = r.get("attestations") or [pid]
    for i, ev in enumerate(r.get("events") or []):
        place = ev.get("place")
        g, via = resolve_place(place, atts) if place else (None, None)
        qid = (g or {}).get("qid")
        col = colony_of.get(via or place) if (g and qid) else None
        if qid: places_used.add(via or place)
        f_events.write(json.dumps({
            "person_id": pid, "seq": i,
            "position": ev.get("position"), "position_norm": position_norm(ev.get("position")),
            "place_raw": place, "place_resolved": via, "place_qid": qid, "place_label": (g or {}).get("label"),
            "colony_qid": (col or {}).get("colony_qid"), "colony_label": (col or {}).get("colony_label"),
            "year_start": ev.get("year_start"), "year_end": ev.get("year_end"),
            "is_acting": ev.get("is_acting", False), "org_type": ev.get("org_type", "civil"),
            "grounded": bool(qid),
        }, ensure_ascii=False) + "\n")
        stats["events"] += 1
        if place: stats["events_placed"] += 1
        stats["events_grounded"] += bool(qid)
        stats["events_resolved_via_map"] += bool(via and qid)
        stats["events_with_colony"] += bool((col or {}).get("colony_qid"))
        if place and not qid and _ORG.search(place): stats["events_org"] += 1

    for h in r.get("honours") or []:
        f_hon.write(json.dumps({"person_id": pid, **h}, ensure_ascii=False) + "\n")
        stats["honours"] += 1
    if r.get("education"):
        f_edu.write(json.dumps({"person_id": pid, "education": r["education"]}, ensure_ascii=False) + "\n")
        stats["education"] += 1

    # status from the LATEST attestation's bio tail
    latest = max(r.get("attestations") or [pid], key=edition)
    st = status_mod.classify_status(bio_txt.get(bioid(latest), ""),
                                    r.get("events") or [], edition(latest))
    f_status.write(json.dumps({"person_id": pid, **st}, ensure_ascii=False) + "\n")

for fh in (f_persons, f_events, f_hon, f_edu, f_status): fh.close()

# place nodes actually referenced by events
with (gdir / "places.jsonl").open("w", encoding="utf-8") as fh:
    for pl in sorted(places_used):
        row = gcache[pl]; col = colony_of.get(pl, {})
        fh.write(json.dumps({**row, "colony_qid": col.get("colony_qid"),
                             "colony_label": col.get("colony_label")}, ensure_ascii=False) + "\n")
stats["places_used"] = len(places_used)
(gdir / "kg_stats.json").write_text(json.dumps(stats, indent=2))

ev, evp, evg = stats["events"], stats["events_placed"], stats["events_grounded"]
print(f"persons         {stats['persons']:,}")
print(f"career_events   {ev:,}  ({evp:,} have a place string, {ev-evp:,} placeless)")
print(f"  grounded      {evg:,} = {100*evg/evp:.1f}% of placed events ({stats['events_resolved_via_map']:,} via resolution map)")
print(f"  with colony   {stats['events_with_colony']:,} ({100*stats['events_with_colony']/evp:.1f}% of placed)")
print(f"  residual org  {stats['events_org']:,} (employers, not places)")
print(f"distinct places {stats['places_used']:,}")
print(f"education rows  {stats['education']:,}   honours rows {stats['honours']:,}")
print(f"tables -> {gdir}/")
