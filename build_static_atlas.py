#!/usr/bin/env python3
"""Phase-1 build: emit the static artifacts the interactive atlas (docs/index.html)
loads on GitHub Pages.  Orchestrates the existing transfer + coord scripts, then
denormalises the two knowledge graphs into compact, browser-sized JSON.

Outputs (docs/data/):
  transfer_coords.json  {qid:[lat,lon]}                       — persisted coord cache (seed + reuse)
  arcs.json             [[yr, fromQid, toQid, pid, corpus]]   — 25k career transfers (corpus 0=CO,1=IO)
  places.json           {qid:{label,lat,lon,co_in,co_out,io_in,io_out}}
  careers.json          {positions:[...], persons:{pid:{q,c,na,st:[[colonyQid,y0,y1,posIdx,acting]]}}}
  search.json           [[pid,"SURNAME, Given",corpus,nStints]]
  meta.json             {yearRange, decadeHist:{co,io}, counts, neo4j:{queryApiUrl}, builtAt}
  tours.json            hand-authored guided tours (Willingdon bridge + overview)

The raw 119MB career-event spine never ships; only placed (colony-resolved) stints
go into careers.json.  Role labels / honours / education are deferred to the live
Neo4j deep-query tab (Phase 2).  CO corpus = 0 (steel-blue), IO corpus = 1 (gold)."""
from __future__ import annotations
import json, subprocess, collections, datetime
from pathlib import Path
from improve_place_coords import resolve_seats   # seat-of-government coords (capital P36 > centroid)

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "docs" / "data"
OUT.mkdir(parents=True, exist_ok=True)

CO = ROOT / "data" / "kg" / "graph_stage3"
IO = ROOT / "data" / "iol" / "graph_stage3"

# ---------------------------------------------------------------- transfers + coords
def run_transfers():
    print("· computing transfers (CO + IOL)…")
    subprocess.run(["python3", "compute_transfers.py"], cwd=ROOT, check=True)
    subprocess.run(["python3", "compute_transfers_iol.py"], cwd=ROOT, check=True)

# display-label fixes for upstream grounding noise where one country QID absorbed
# several colonies and a wrong sub-label won the dict. QID + (capital) seat are
# right; we just restore the QID's canonical Wikidata name. NB the over-collapse
# itself (e.g. Victoria/NSW pooled under Australia, Penang under Malaysia) is an
# upstream place-grounding bug that mislocates those careers to the country capital.
# Period-appropriate names, curated by hand: Wikidata's canonical label is often
# anachronistic for 1820-1966 (Q148 = "People's Republic of China", est. 1949) and
# P1813 short-names are ISO codes ("MYS"), so neither can be used automatically.
LABEL_FIX = {
    "Q16":  "Canada",          # had "New Brunswick" / "Upper Canada"
    "Q30":  "United States",   # had "Baker Island" / "New Hampshire Colony"
    "Q408": "Australia",       # absorbed Victoria/NSW/WA/Queensland/Tasmania/Swan River
    "Q833": "Malaya",          # absorbed Penang/Straits Settlements/Sarawak (not "Malaysia", 1963)
    "Q148": "China",           # had "Weihaiwei"; NOT "People's Republic of China" (1949)
}

def resolve_coords(all_qids, labels):
    """Seat-of-government coordinates: each place resolves to its capital (Wikidata
    P36 -> P625), falling back to centroid only where no capital exists. Persists
    transfer_coords.json + place_seats.json. (improve_place_coords.resolve_seats)"""
    coords, seats, report, fallbacks = resolve_seats(all_qids, labels)
    json.dump(coords, (OUT / "transfer_coords.json").open("w"))
    json.dump(seats, (OUT / "place_seats.json").open("w"), ensure_ascii=False)
    print(f"· coords: seat(P36)={report['seat']} curated={report['override']} "
          f"centroid={report['centroid']} no-coord={report['handfill']}")
    return coords, seats

# ---------------------------------------------------------------- arcs + places
def build_arcs_places(coords, seats, canon):
    co = json.load(open("/tmp/transfers.json"))
    io = json.load(open("/tmp/iol_transfers.json"))
    labels = {}
    labels.update(co["labels"]); labels.update(io["labels"])

    # fold to canonical person, then DEDUP repeated moves (a person re-attested
    # across editions logs the same from->to under several merged ids / near years)
    raw = []
    for corpus, data in ((0, co), (1, io)):
        for t in data["transfers"]:
            f, to = t["from"], t["to"]
            if f not in coords or to not in coords or f == to:
                continue
            raw.append([t["yr"], f, to, canon(t["pid"]), corpus])
    raw.sort(key=lambda a: a[0])                          # earliest year wins for a repeated move
    arcs, seen = [], set()
    deg = collections.defaultdict(lambda: [0, 0, 0, 0])  # [co_in, co_out, io_in, io_out]
    for a in raw:
        k = (a[3], a[1], a[2])                            # canonical pid, from, to
        if k in seen:
            continue
        seen.add(k); arcs.append(a)
        f, to, corpus = a[1], a[2], a[4]
        if corpus == 0: deg[to][0] += 1; deg[f][1] += 1
        else:           deg[to][2] += 1; deg[f][3] += 1

    places = {}
    for q in deg:
        lat, lon = coords[q]
        d = deg[q]
        places[q] = {"label": LABEL_FIX.get(q, labels.get(q, q)), "seat": seats.get(q) or "",
                     "lat": lat, "lon": lon,
                     "co_in": d[0], "co_out": d[1], "io_in": d[2], "io_out": d[3]}
    json.dump(arcs, (OUT / "arcs.json").open("w"), separators=(",", ":"))
    json.dump(places, (OUT / "places.json").open("w"), separators=(",", ":"))
    print(f"· arcs.json {len(arcs):,} arcs   places.json {len(places)} places")
    return arcs

# ---------------------------------------------------------------- careers + search
def co_events():
    """CO: career_facts already fuses role+place; use raw position for the ledger line."""
    for l in (CO / "career_facts.jsonl").open():
        d = json.loads(l)
        yield (d["person_id"], d.get("colony_qid"), d.get("year_start"),
               d.get("year_end"), d.get("position_raw"), d.get("is_acting"))

def io_events():
    """IOL: join career_events spine (place/year/position) — role label not needed for the ledger."""
    for l in (IO / "career_events.jsonl").open():
        d = json.loads(l)
        yield (d["person_id"], d.get("colony_qid"), d.get("year_start"),
               d.get("year_end"), d.get("position"), d.get("is_acting"))

def load_persons(path):
    p = {}
    for l in open(path):
        d = json.loads(l)
        p[d["person_id"]] = (d.get("surname"), d.get("given_names"), d.get("wikidata_qid"))
    return p

def build_canon():
    """Map every career-event person_id to its CANONICAL deduped person.
    Stage-3 dedup merged duplicate person nodes in persons.jsonl but career_facts
    kept the pre-merge ids (~2,983 CO orphans), which show as "?" and double-count.
    The id encodes an attestation (kgp_col1932-p858b14 -> col1932-p858b14); the
    canonical person lists that attestation, so we recover it 1:1."""
    att2canon, allpids = {}, set()
    for path in (CO / "persons.jsonl", IO / "persons.jsonl"):
        for l in open(path):
            d = json.loads(l); allpids.add(d["person_id"])
            for a in d.get("attestations") or []:
                att2canon.setdefault(a, d["person_id"])
    def canon(pid):
        if pid in allpids:
            return pid
        att = pid[4:] if pid.startswith("kgp_") else pid
        return att2canon.get(att, pid)
    return canon

def build_careers_search(canon):
    persons = load_persons(CO / "persons.jsonl"); persons.update(load_persons(IO / "persons.jsonl"))

    pos_tbl, pos_idx = [], {}
    def intern(t):
        t = (t or "").strip()
        if t not in pos_idx:
            pos_idx[t] = len(pos_tbl); pos_tbl.append(t)
        return pos_idx[t]

    # gather DEDUPED events per canonical person (a person re-attested across editions
    # produces identical events under merged ids — collapse them to a set)
    evset = collections.defaultdict(set)       # cpid -> {(y0,y1,colonyQid,posIdx,acting)}
    for corpus, gen in ((0, co_events()), (1, io_events())):
        for pid, col, y0, y1, pos, acting in gen:
            evset[canon(pid)].add((y0, (y1 or y0) if y0 else None, col, intern(pos), 1 if acting else 0))

    careers, search = {}, []
    for cpid, evs in evset.items():
        corpus = 0 if cpid.startswith("kgp_col") else 1
        sur, giv, qid = persons.get(cpid, (None, None, None))
        placed = sorted(e for e in evs if e[2] and e[0])          # has colony + start year
        st = []
        for y0, y1, col, pi, ac in placed:
            if st and st[-1][0] == col and st[-1][3] == pi:
                st[-1][2] = max(st[-1][2], y1 or y0)
            else:
                st.append([col, y0, y1 or y0, pi, ac])
        if not st:                                                # map-able officials only
            continue
        disp = f"{sur or '?'}, {giv or ''}".strip().rstrip(",")
        careers[cpid] = {"q": qid, "c": corpus, "na": len(evs), "nm": disp, "st": st}
        search.append([cpid, disp, corpus, len(st)])

    json.dump({"positions": pos_tbl, "persons": careers},
              (OUT / "careers.json").open("w"), separators=(",", ":"), ensure_ascii=False)
    json.dump(search, (OUT / "search.json").open("w"), separators=(",", ":"), ensure_ascii=False)
    print(f"· careers.json {len(careers):,} officials, {len(pos_tbl):,} interned positions   search.json {len(search):,}")

# ---------------------------------------------------------------- meta + tours
def build_meta(arcs):
    yrs = [a[0] for a in arcs]
    hist = {"co": collections.Counter(), "io": collections.Counter()}
    for yr, _, _, _, corpus in arcs:
        hist["co" if corpus == 0 else "io"][(yr // 10) * 10] += 1
    movers = {0: set(), 1: set()}
    for a in arcs:
        movers[a[4]].add(a[3])
    officials = len(movers[0]) + len(movers[1])
    roster_co = sum(1 for _ in (CO / "persons.jsonl").open())
    roster_io = sum(1 for _ in (IO / "persons.jsonl").open())
    meta = {
        "builtAt": datetime.date.today().isoformat(),
        "yearRange": [min(yrs), max(yrs)],
        "officials": officials,                                   # officials who moved (both corpora)
        "roster": {"co": roster_co, "io": roster_io, "total": roster_co + roster_io},
        "movers": {"co": len(movers[0]), "io": len(movers[1])},
        "counts": {"arcs": len(arcs),
                   "officials": officials,
                   "co": sum(1 for a in arcs if a[4] == 0),
                   "io": sum(1 for a in arcs if a[4] == 1)},
        "decadeHist": {k: dict(sorted(v.items())) for k, v in hist.items()},
        "neo4j": {"queryApiUrl": None},   # set when the Phase-2 TLS proxy is up
    }
    json.dump(meta, (OUT / "meta.json").open("w"), indent=0)
    print(f"· meta.json  years {meta['yearRange']}  CO {meta['counts']['co']:,} / IO {meta['counts']['io']:,}")

def build_tours():
    """Hand-authored (risk #5: Willingdon is 3 ungrounded person_ids, can't auto-join).
    Steps reference colony QIDs the client resolves against places.json."""
    tours = [
        {"id": "willingdon", "title": "One career, both services",
         "blurb": "Freeman Freeman-Thomas, Marquess of Willingdon, is the rare official whose "
                  "record runs through both the Colonial Office and India Office Lists — the "
                  "career that stitches the two datasets together.",
         "pids": ["kgp_iol1937-c5481176", "kgp_col1933-p1033b14"],
         "steps": [
            {"qid": "Q408",     "yr": 1895, "caption": "Freeman Freeman-Thomas — the future Lord Willingdon — begins his public life as aide-de-camp to the Governor of Victoria, in Australia."},
            {"qid": "Q891827",  "yr": 1913, "caption": "Eighteen years later he is Governor of Bombay, a presidency of the Indian Empire."},
            {"qid": "Q1772596", "yr": 1919, "caption": "He moves south to govern Madras."},
            {"qid": "Q16",      "yr": 1926, "caption": "Then he crosses the world to become Governor-General of Canada — a Colonial Office appointment."},
            {"qid": "Q129286",  "yr": 1931, "caption": "And returns to India as Viceroy. His service runs through both Lists — the single thread this atlas was built to follow."},
         ]},
        {"id": "two-services", "title": "Two services, one empire",
         "blurb": "The Colonial Office (blue) ran the dependent empire — Africa, the Caribbean, "
                  "the Pacific, Canada. The India Office (gold) ran the Raj as a world of its own. "
                  "Watch both webs build, then explore either.",
         "pids": [],
         "steps": [
            {"qid": "Q129286", "yr": 1858, "caption": "Calcutta — the hub of the Indian service."},
            {"qid": "Q16",     "yr": 1867, "caption": "Canada — a self-governing dominion within the Colonial web."},
            {"qid": "Q263",    "yr": 1910, "caption": "The Cape — where colonial careers crossed southern Africa."},
         ]},
    ]
    json.dump(tours, (OUT / "tours.json").open("w"), indent=1, ensure_ascii=False)
    print(f"· tours.json {len(tours)} tours")

# ----------------------------------------------------------------
def main():
    run_transfers()
    co = json.load(open("/tmp/transfers.json"))
    io = json.load(open("/tmp/iol_transfers.json"))
    all_qids = sorted({t["from"] for d in (co, io) for t in d["transfers"]} |
                      {t["to"] for d in (co, io) for t in d["transfers"]})
    labels = {}; labels.update(co["labels"]); labels.update(io["labels"])
    coords, seats = resolve_coords(all_qids, labels)
    canon = build_canon()
    arcs = build_arcs_places(coords, seats, canon)
    build_careers_search(canon)
    build_meta(arcs)
    build_tours()
    # cross-corpus "Two Services" bridges (reads the careers.json just written)
    import subprocess, sys
    subprocess.run([sys.executable, "build_bridges.py"], check=True)
    print("done →", OUT)

if __name__ == "__main__":
    main()
