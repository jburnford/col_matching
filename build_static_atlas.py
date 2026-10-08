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
from atlas_geography import records, project

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
    "Q117": "Gold Coast",      # had "British Togoland"; the Gold Coast / Ghana (seat Accra)
}

def resolve_coords(all_qids, labels):
    nodes = {}
    for name in ('transfers', 'iol_transfers'):
        nodes.update(json.load(open('/tmp/' + name + '.json'))['nodes'])
    coords = {q: [v['lat'], v['lon']] for q, v in nodes.items()}
    seats = {q: v['seat'] for q, v in nodes.items()}
    json.dump(coords, (OUT / 'transfer_coords.json').open('w'))
    json.dump(seats, (OUT / 'place_seats.json').open('w'))
    return coords, seats

# ---------------------------------------------------------------- arcs + places
def build_arcs_places(coords, seats, canon):
    co = json.load(open("/tmp/transfers.json"))
    io = json.load(open("/tmp/iol_transfers.json"))
    labels = {}
    labels.update(co["labels"]); labels.update(io["labels"])

    # fold to canonical person, then DEDUP repeated moves (a person re-attested
    # across editions logs the same from->to under several merged ids / near years)
    raw, uncertain = [], []
    for corpus, data in ((0, co), (1, io)):
        for t in data["transfers"] + data.get('uncertain_transfers', []):
            f, to = t["from"], t["to"]
            if f not in coords or to not in coords or f == to:
                continue
            row = [t["yr"], f, to, canon(t["pid"]), corpus]
            if t.get('uncertain'):
                uncertain.append(row + [t['uncertain']])
            else:
                raw.append(row)
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

    # Alternative connections are published separately from ordered corridors.
    # A same-year association is undirected; never use its storage order as travel.
    uncertain_out, uncertain_seen = [], set()
    for a in sorted(uncertain, key=lambda a: (a[0], a[3], a[1], a[2])):
        k = (a[3], a[1], a[2])
        reverse = (a[3], a[2], a[1])
        same_year = a[5].startswith('same-year')
        if k in seen or (same_year and reverse in seen): continue
        uk = (a[3], *sorted(a[1:3])) if same_year else k
        if uk in uncertain_seen: continue
        uncertain_seen.add(uk); uncertain_out.append(a)
    json.dump(uncertain_out, (OUT / 'uncertain_arcs.json').open('w'), separators=(',', ':'))

    places = {}
    nodes = {**co["nodes"], **io["nodes"]}
    for q in nodes:
        lat, lon = coords[q]
        d = deg[q]
        places[q] = {**nodes[q], "label": LABEL_FIX.get(q, labels.get(q, q)), "seat": seats.get(q) or "",
                     "lat": lat, "lon": lon,
                     "co_in": d[0], "co_out": d[1], "io_in": d[2], "io_out": d[3]}
    json.dump(arcs, (OUT / "arcs.json").open("w"), separators=(",", ":"))
    json.dump(places, (OUT / "places.json").open("w"), separators=(",", ":"))
    print(f"· arcs.json {len(arcs):,} ordered corridors; {len(uncertain_out):,} uncertain connections; {len(places)} places")
    return arcs

# ---------------------------------------------------------------- careers + search
# NOTE: OCR/source career-YEAR fixes now live UPSTREAM in data/kg/career_year_fixups.json,
# applied by kg_apply_year_fixups.py as the final step of reemit_dedup.sh (mirroring the
# colony fixups). career_facts.jsonl therefore already carries the corrected years, so the
# atlas reads them straight through — no downstream override here. (The old downstream
# data/kg/career_event_corrections.json Guggisberg entry has been superseded by that fixup.)
def load_persons(path):
    p = {}
    for l in open(path):
        d = json.loads(l)
        p[d["person_id"]] = (d.get("surname"), d.get("given_names"), d.get("wikidata_qid"),
                             d.get("wikidata_label"))
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
    co_persons = load_persons(CO / "persons.jsonl")
    persons = {**co_persons, **load_persons(IO / "persons.jsonl")}

    # intern the GROUNDED role (id + canonical label), keyed by role identity so
    # every spelling of "Governor" folds to one row — that shared index is also what
    # lets the client list everyone who held a role at a colony.
    role_tbl, role_idx = [], {}
    def intern_role(rid, label, raw):
        disp = (label or raw or "in service").strip()
        key = rid or ("L:" + disp.lower())
        if key not in role_idx:
            role_idx[key] = len(role_tbl); role_tbl.append([rid, disp])
        return role_idx[key]

    # gather DEDUPED events per canonical person (a person re-attested across editions
    # produces identical events under merged ids — collapse them to a set)
    evset = collections.defaultdict(set)
    unplaced = collections.defaultdict(set)
    for corpus in ('kg', 'iol'):
        for r in records(corpus):
            pid = canon(r['person_id'])
            key, node = project(r)
            y0, y1 = r.get('year_start'), r.get('year_end')
            ri = intern_role(r.get('role_id'), r.get('role_label'), r.get('position_raw'))
            if not key:
                reason = ('electoral defeat; not an appointment' if r.get('event_kind') == 'electoral_defeat'
                          else r.get('location_note') or ('undated event' if not y0 else 'location unresolved'))
                unplaced[pid].add((y0, y1, r.get('role_label') or r.get('position_raw') or '',
                                  r.get('place_raw') or r.get('place_label') or '', reason))
            else:
                evset[pid].add((y0, y1 or y0, key, ri, 1 if r.get('is_acting') else 0, r.get('route_order', 0)))

    careers, search = {}, []
    for cpid in sorted(evset.keys() | unplaced.keys()):
        corpus = 0 if cpid in co_persons else 1
        sur, giv, qid, wlabel = persons.get(cpid, (None, None, None, None))
        evs = sorted(evset[cpid], key=lambda e: (e[0], e[5], e[2], e[3], e[1]))
        # Preserve distinct event dates: equal roles years apart do not prove
        # uninterrupted tenure (Brewster's electoral defeat exposed this too).
        st = [[q, y0, y1, ri, ac] for y0, y1, q, ri, ac, order in evs]
        un = sorted(unplaced[cpid], key=lambda e: (e[0] or 9999, e[2], e[3]))
        disp = wlabel or f"{sur or '?'}, {giv or ''}".strip().rstrip(',')
        careers[cpid] = {'q': qid, 'c': corpus, 'na': len(evs) + len(un), 'nm': disp, 'st': st, 'un': un}
        search.append([cpid, disp, corpus, len(st)])

    json.dump({"roles": role_tbl, "persons": careers},
              (OUT / "careers.json").open("w"), separators=(",", ":"), ensure_ascii=False)
    json.dump(search, (OUT / "search.json").open("w"), separators=(",", ":"), ensure_ascii=False)
    print(f"· careers.json {len(careers):,} officials, {len(role_tbl):,} grounded roles   search.json {len(search):,}")

# ---------------------------------------------------------------- meta + tours
def build_meta(arcs):
    uncertain = json.loads((OUT / 'uncertain_arcs.json').read_text())
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
        "counts": {"arcs": len(arcs), "uncertain_connections": len(uncertain),
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
        {"id": "two-services", "title": "Two services, one empire",
         "blurb": "Britain ran its empire through two civil services, each published as a thick "
                  "annual register. Meet the two Lists this atlas is built from, and watch each "
                  "web build before you explore.",
         "pids": [],
         "steps": [
            {"web": "both", "yr": 1966, "caption":
             "Britain governed its empire through two separate civil services, and each printed a "
             "fat annual book of names — who held which post, where, and when. From the 1820s to "
             "the 1960s those registers track tens of thousands of careers. This atlas plots every "
             "posting that changed hands."},
            {"web": "io", "qid": "Q129286", "yr": 1911, "zoom": 3.6, "caption":
             "The India Office List (gold) recorded the Indian Empire — the Indian Civil Service, "
             "the army, the presidencies and the princely states. It was a world of its own, run "
             "from Calcutta and Delhi."},
            {"web": "io", "qid": "Q2629708", "yr": 1911, "zoom": 4.0, "caption":
             "Its officials circulated within the subcontinent — Bengal, Bombay, Madras, the "
             "Punjab, Burma and the frontier — and rarely served anywhere else."},
            {"web": "co", "qid": "Q2046345", "yr": 1935, "zoom": 3.4, "caption":
             "The Colonial Office List (blue) recorded everyone else: the dependent empire. West "
             "Africa first — Nigeria, the Gold Coast, Sierra Leone."},
            {"web": "co", "qid": "Q116282722", "yr": 1935, "zoom": 3.4, "caption":
             "Then the Caribbean — Trinidad, Jamaica, British Guiana — the Mediterranean, and the "
             "islands of the Pacific."},
            {"web": "co", "qid": "Q16", "yr": 1910, "zoom": 3.2, "caption":
             "And the self-governing dominions, Canada among them — their own parliaments, but "
             "still names in the register."},
            {"web": "both", "yr": 1966, "caption":
             "Two services, one empire. They almost never mixed — but a handful of officials cross "
             "from one List to the other. Explore either web, or follow a single crossing career "
             "in ‘One career, both services.’"},
         ]},
        {"id": "willingdon", "title": "One career, both services",
         "blurb": "Freeman Freeman-Thomas, Marquess of Willingdon, is the rare official whose "
                  "record runs through both the Colonial Office and India Office Lists — the "
                  "career that stitches the two datasets together.",
         "pids": ["kgp_iol1931-c5407596", "kgp_col1933-p1033b14"],
         "steps": [
            {"web": "both", "yr": 1966, "caption":
             "Two annual registers recorded the people who ran the British Empire. The Colonial "
             "Office List — here in blue — named the officials of the dependent empire: "
             "Africa, the Caribbean, the Pacific, Canada. The India Office List — in gold "
             "— did the same for the Indian Empire. A few careers run through both at once. "
             "Here is one."},
            {"qid": "Q408",     "yr": 1895, "caption": "Freeman Freeman-Thomas — the future Lord Willingdon — begins his public life as aide-de-camp to the Governor of Victoria, in Australia."},
            {"qid": "Q891827",  "yr": 1913, "caption": "Eighteen years later he is Governor of Bombay, a presidency of the Indian Empire."},
            {"qid": "Q1772596", "yr": 1919, "caption": "He moves south to govern Madras."},
            {"qid": "Q16",      "yr": 1926, "caption": "Then he crosses the world to become Governor-General of Canada — a Colonial Office appointment."},
            {"qid": "Q129286",  "yr": 1931, "caption": "And returns to India as Viceroy. His service runs through both Lists — the single thread this atlas was built to follow."},
            {"web": "both", "home": True, "yr": 1966, "caption": "One thread among the officials with inferred changes of location. The whole web is yours now: search an official by name in the panel on the right, or click any circle on the map to see the careers that ran through that place. Click a busy corridor in the panel to trace who travelled it; switch between the two services — or the schools that trained them — from the buttons at lower left; and drag the year along the bottom to watch the empire fill in. Press Finish to open Willingdon's own record."},
         ]},
    ]
    places = json.load((OUT / "places.json").open())
    for tour in tours:
        for step in tour['steps']:
            q = step.get('qid')
            if q and q not in places:
                key, _ = project({'colony_qid': q, 'year_start': step.get('yr', 1931)})
                if key in places: step['qid'] = key
                else: step.pop('qid')
    json.dump(tours, (OUT / "tours.json").open("w"), indent=1, ensure_ascii=False)
    print(f"· tours.json {len(tours)} tours")

# ----------------------------------------------------------------
def main():
    subprocess.run(["python3", "kg_apply_historical_fixups.py"], cwd=ROOT, check=True)
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
    import sys
    subprocess.run([sys.executable, "build_bridges.py"], check=True)
    from build_top500_review import main as build_review
    build_review()
    print("done →", OUT)

if __name__ == "__main__":
    main()
