#!/usr/bin/env python3
"""Build the data layer for the Education Atlas — "Schools of Empire".

Answers: which institutions trained which KIND of official (role-category), and
how did that change over the DECADES — plus surfaces the long tail of ungrounded
local schools a map can't show.

Inputs (both corpora; person_ids are corpus-prefixed kgp_col* / kgp_iol*):
  {CO,IO}/role_edges.jsonl       person -> (category, year_start)  [kind + decade]
  {CO,IO}/education_edges.jsonl  person -> institution (QID|colkg) + label + type
  {CO,IO}/persons.jsonl          names + wikidata_qid for panels

Outputs -> docs/data_edu/:
  institutions.json  grounded (mappable): {qid:{label,type,lat,lon,co,io,total,
                       cats:{cat:n}, by_decade:{dec:n}, dominant}}
  local.json         ungrounded tail: [{id,label,type,co,io,total,cats}]
  stream.json        {decades, categories, series:{cat:[per-decade]},
                       coverage:{dec:{grounded,local}}}  (deduped per person)
  alumni.json        {inst_id:[{id,name,corpus,qid,top_cat}]}  (capped)
  meta.json          totals, top feeders, palettes, decade range
  inst_coords.json   persisted P625 coord cache (seed + reuse)
"""
import json
from collections import Counter, defaultdict
from pathlib import Path

from improve_place_coords import resolve_inst_coords  # P625, else city/admin centroid

CO = Path("data/kg/graph_stage3")
IO = Path("data/iol/graph_stage3")
OUT = Path("docs/data_edu")
OUT.mkdir(parents=True, exist_ok=True)

ALUMNI_CAP = 60
MIN_MAP = 3   # map markers: prune <3-alumni grounded institutions (clutter)
              # the ungrounded LOCAL tail keeps ALL (>=1) — it IS the point.

# category order (by overall frequency) + a distinct categorical palette
CAT_ORDER = ["administrative", "judicial", "technical", "military", "police",
             "financial", "clerical", "medical", "education", "religious",
             "other", "unknown"]
CAT_COLOR = {"administrative": "#4E79A7", "judicial": "#59A14F",
             "technical": "#F28E2B", "military": "#E15759", "police": "#76B7B2",
             "financial": "#EDC948", "clerical": "#9C755F", "medical": "#B07AA1",
             "education": "#FF9DA7", "religious": "#86BCB6",
             "other": "#A99F8E", "unknown": "#7A736B"}   # muted: catch-all roles
VAGUE = {"other", "unknown"}   # excluded from "dominant kind of official"
TYPE_COLOR = {"school": "#4E79A7", "university": "#59A14F",
              "university_college": "#8CD17D", "military_academy": "#E15759",
              "professional": "#F28E2B", "inn_of_court": "#B07AA1",
              "other": "#79706E"}


def rows(p):
    if p.exists():
        for l in p.open(encoding="utf-8"):
            if l.strip():
                yield json.loads(l)


def load_resolver(root):
    """Transitive person_id -> canonical map from the stage3 dedup merge maps.
    The grounding-overlay edge files (education_edges, …) were emitted before the
    2026-06-27 role+year dedup re-keyed persons, so their person_ids must be
    chased to canonical or they orphan (no name, no roles, unlinkable)."""
    m = {}
    for f in root.glob("dedup_stage3_merge_map*.jsonl"):
        if "bak" in f.name or "_v2" in f.name:
            continue
        for d in rows(f):
            old, new = d["person_id"], d["canonical_person_id"]
            if old != new:
                m[old] = new

    def resolve(pid):
        seen = set()
        while pid in m and pid not in seen:
            seen.add(pid)
            pid = m[pid]
        return pid
    return resolve


def corpus_of(pid):
    return "io" if pid.startswith("kgp_iol") else "co"


def load_names():
    names, qids = {}, {}
    for path in (CO / "persons.jsonl", IO / "persons.jsonl"):
        for d in rows(path):
            nm = " ".join(x for x in [(d.get("given_names") or "").strip(),
                                      (d.get("surname") or "").strip()] if x)
            names[d["person_id"]] = nm or d["person_id"]
            if d.get("wikidata_qid"):
                qids[d["person_id"]] = d["wikidata_qid"]
    return names, qids


def person_appointments():
    """person_id -> list[(category, decade)] from dated role edges (both corpora)."""
    appt = defaultdict(list)
    for path in (CO / "role_edges.jsonl", IO / "role_edges.jsonl"):
        for d in rows(path):
            y = d.get("year_start")
            if not y:
                continue
            cat = d.get("category") or "unknown"
            appt[d["person_id"]].append((cat, (y // 10) * 10))
    return appt


def main():
    names, pqids = load_names()
    appt = person_appointments()

    # ---- aggregate per institution -------------------------------------
    inst = {}                          # inst_id -> meta
    inst_cats = defaultdict(Counter)   # inst_id -> Counter(category)         [appt]
    inst_dec = defaultdict(Counter)    # inst_id -> Counter(decade)          [appt]
    inst_alumni = defaultdict(list)    # inst_id -> [(pid, corpus)]
    pgs = defaultdict(set)             # person -> set(grounded school qid) [feeder arcs]
    edges_total = edges_seen = 0
    seen = set()                       # (pid, inst_id) dedup of alumni

    resolve = {"co": load_resolver(CO.parent), "io": load_resolver(IO.parent)}
    for corp, path in (("co", CO / "education_edges.jsonl"), ("io", IO / "education_edges.jsonl")):
        for d in rows(path):
            edges_total += 1
            iid = d.get("institution_id") or ""
            if not (iid.startswith("Q") or iid.startswith("colkg:")):
                continue
            pid = resolve[corp](d["person_id"])   # -> canonical (links + names)
            rec = inst.setdefault(iid, {"label": d.get("institution_label") or iid,
                                        "type": d.get("type") or "other",
                                        "grounded": iid.startswith("Q"),
                                        "co": set(), "io": set()})
            rec[corpus_of(pid)].add(pid)
            if iid.startswith("Q"):
                pgs[pid].add(iid)               # grounded schools, for feeder arcs
            if (pid, iid) in seen:
                continue
            seen.add((pid, iid))
            edges_seen += 1
            inst_alumni[iid].append((pid, corpus_of(pid)))
            for cat, dec in appt.get(pid, ()):
                inst_cats[iid][cat] += 1
                inst_dec[iid][dec] += 1

    # ---- coordinates for grounded institutions (cached) ----------------
    grounded_ids = [i for i, r in inst.items() if r["grounded"]
                    and len(r["co"]) + len(r["io"]) >= MIN_MAP]
    cache_p = OUT / "inst_coords.json"
    coords = json.load(open(cache_p)) if cache_p.exists() else {}
    coords = {q: (c if len(c) == 3 else [c[0], c[1], False])  # normalise to [lat,lon,approx]
              for q, c in coords.items()}
    missing = [q for q in grounded_ids if q not in coords]
    if missing:
        print(f"· resolving coords for {len(missing)} institutions (P625, else city centroid)…")
        coords.update(resolve_inst_coords(missing))
        json.dump(coords, cache_p.open("w"))
    n_approx = sum(1 for q in grounded_ids if q in coords and coords[q][2])

    # ---- emit institutions (map) + local (tail) ------------------------
    # map  = grounded, has P625, >= MIN_MAP alumni (clutter control)
    # local = ALL ungrounded (>=1) + grounded-without-coords (the long tail)
    institutions, local, alumni = {}, [], {}
    no_coord = 0
    tail_hist = Counter()          # alumni-count -> #local institutions
    tail_by_type = Counter()       # institution type -> #local institutions
    for iid, rec in inst.items():
        co_n, io_n = len(rec["co"]), len(rec["io"])
        total = co_n + io_n
        if total < 1:
            continue
        cats = dict(inst_cats[iid].most_common())
        dominant = next((c for c, _ in inst_cats[iid].most_common() if c not in VAGUE),
                        "other")
        on_map = rec["grounded"] and iid in coords and total >= MIN_MAP

        # capped alumni list for the panel (richest careers first)
        lst, seen_p = [], set()
        for pid, corpus in inst_alumni[iid]:
            if pid in seen_p:
                continue
            seen_p.add(pid)
            tc = Counter(c for c, _ in appt.get(pid, ()) if c not in VAGUE).most_common(1)
            lst.append({"id": pid, "name": names.get(pid, pid), "corpus": corpus,
                        "qid": pqids.get(pid), "top_cat": tc[0][0] if tc else None,
                        "n": len(appt.get(pid, ()))})
        lst.sort(key=lambda a: (-a["n"], a["name"]))
        alumni[iid] = lst[:ALUMNI_CAP]

        if on_map:
            lat, lon, approx = coords[iid]
            institutions[iid] = {"label": rec["label"], "type": rec["type"],
                                 "co": co_n, "io": io_n, "total": total,
                                 "cats": cats, "dominant": dominant,
                                 "by_decade": {str(k): v for k, v in
                                               sorted(inst_dec[iid].items())},
                                 "lat": lat, "lon": lon, "approx": approx}
        elif rec["grounded"] and total >= MIN_MAP:
            no_coord += 1          # grounded but WD lacks P625 -> tail
        if not on_map:
            local.append({"id": iid, "label": rec["label"], "type": rec["type"],
                          "co": co_n, "io": io_n, "total": total,
                          "cats": cats, "dominant": dominant,
                          "grounded": rec["grounded"]})
            tail_hist[min(total, 10)] += 1
            tail_by_type[rec["type"]] += 1
    local.sort(key=lambda r: -r["total"])

    # ---- streamgraph: appointments of educated persons, deduped per person
    educated = {pid for ids in inst_alumni.values() for pid, _ in ids}
    decades = sorted({dec for pid in educated for _, dec in appt.get(pid, ())})
    series = {c: [0] * len(decades) for c in CAT_ORDER}
    dpos = {d: i for i, d in enumerate(decades)}
    # coverage: head-count of alumni active per decade, grounded vs local school
    grounded_alumni = {pid for iid in institutions for pid, _ in inst_alumni[iid]}
    coverage = {str(d): {"grounded": 0, "local": 0} for d in decades}
    for pid in educated:
        decs = set()
        for cat, dec in appt.get(pid, ()):
            series.setdefault(cat, [0] * len(decades))[dpos[dec]] += 1
            decs.add(dec)
        bucket = "grounded" if pid in grounded_alumni else "local"
        for dec in decs:
            coverage[str(dec)][bucket] += 1
    stream = {"decades": decades, "categories": CAT_ORDER,
              "series": series, "coverage": coverage}

    # ---- feeder-school arcs: school<->school co-attendance --------------
    # a person who attended two GROUNDED+mapped schools links them (the
    # prep-school -> university pipeline). weight = shared alumni.
    pair = Counter()
    for schools in pgs.values():
        ms = sorted(s for s in schools if s in institutions)   # both endpoints mappable
        for i in range(len(ms)):
            for j in range(i + 1, len(ms)):
                pair[(ms[i], ms[j])] += 1
    school_arcs = [[a, b, w] for (a, b), w in pair.most_common() if w >= 2]
    json.dump(school_arcs, (OUT / "school_arcs.json").open("w"), separators=(",", ":"))

    # ---- meta ----------------------------------------------------------
    ranked = sorted(
        [{"id": i, "label": r["label"], "type": r["type"], "grounded": r["grounded"],
          "co": len(r["co"]), "io": len(r["io"]), "total": len(r["co"]) + len(r["io"])}
         for i, r in inst.items() if len(r["co"]) + len(r["io"]) >= MIN_MAP],
        key=lambda r: -r["total"])
    meta = {
        "builtAt": "2026-06-27",
        "mapped": len(institutions), "local": len(local),
        "edges_total": edges_total, "edges_attributed": edges_seen,
        "grounded_no_coord": no_coord,
        "decades": decades,
        "cat_color": CAT_COLOR, "cat_order": CAT_ORDER, "type_color": TYPE_COLOR,
        "top": ranked[:40],
        "tail": {
            "singletons": tail_hist.get(1, 0),
            "hist": {str(k): tail_hist[k] for k in sorted(tail_hist)},
            "by_type": dict(tail_by_type.most_common()),
        },
        "feeder_arcs": len(school_arcs),
    }

    json.dump(institutions, (OUT / "institutions.json").open("w"),
              ensure_ascii=False, separators=(",", ":"))
    json.dump(local, (OUT / "local.json").open("w"),
              ensure_ascii=False, separators=(",", ":"))
    json.dump(stream, (OUT / "stream.json").open("w"), separators=(",", ":"))
    json.dump(alumni, (OUT / "alumni.json").open("w"),
              ensure_ascii=False, separators=(",", ":"))
    json.dump(meta, (OUT / "meta.json").open("w"), ensure_ascii=False, indent=1)

    print(f"· mapped institutions: {len(institutions)} ({sum(1 for v in institutions.values() if v.get('approx'))} approx city-centroid)   "
          f"local tail: {len(local)} (singletons {tail_hist.get(1,0)})")
    print(f"· grounded-but-no-P625 sent to tail: {no_coord}")
    print(f"· education edges: {edges_seen:,} attributed / {edges_total:,} total")
    print(f"· tail by alumni-count: {dict(sorted(tail_hist.items()))}")
    print(f"· feeder-school arcs (w>=2, both mapped): {len(school_arcs)}")
    print(f"· decades: {decades[0]}–{decades[-1]}")
    print("· top 12 feeders:")
    for r in ranked[:12]:
        g = "MAP" if r["grounded"] else "local"
        print(f"    {r['total']:5}  {r['label'][:42]:42}  CO {r['co']:4} / IO {r['io']:4}  [{r['type']}/{g}]")


if __name__ == "__main__":
    main()
