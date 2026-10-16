#!/usr/bin/env python3
"""Cache Wikidata facts the WHG export needs for every candidate place QID.

Property lookups only (label, P31 classes, P625 point, P571/P576 dates, P17,
AAT IDs of the classes). Identity is never decided here: the QIDs come from the
reviewed graph and config/whg_place_identities.json. Uses QLever (WDQS times out
on large VALUES blocks). Output: data/whg/wikidata_places.json.

    python3 whg_fetch_wikidata.py            # fetch only QIDs missing from cache
    python3 whg_fetch_wikidata.py --refresh  # refetch everything
"""
import argparse
import json
from pathlib import Path
import re
import time
import urllib.parse
import urllib.request

ROOT = Path(__file__).resolve().parent
CACHE = ROOT / "data/whg/wikidata_places.json"
QLEVER = "https://qlever.dev/api/wikidata"
PREFIX = """PREFIX wd: <http://www.wikidata.org/entity/>
PREFIX wdt: <http://www.wikidata.org/prop/direct/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
"""


def sparql(query):
    data = urllib.parse.urlencode({"query": PREFIX + query}).encode()
    req = urllib.request.Request(QLEVER, data=data, headers={
        "Accept": "application/sparql-results+json",
        "User-Agent": "col_matching-whg/1.0 (jic823@usask.ca)"})
    for attempt in range(4):
        try:
            with urllib.request.urlopen(req, timeout=300) as resp:
                return json.load(resp)["results"]["bindings"]
        except Exception:
            if attempt == 3:
                raise
            time.sleep(5 * (attempt + 1))


def qid(uri):
    return uri.rsplit("/", 1)[-1]


def values(qids):
    return " ".join("wd:" + q for q in qids)


def candidate_qids(root):
    found = set()
    for corpus in ("kg", "iol"):
        graph = root / f"data/{corpus}/graph_stage3"
        for name, fields in (("places.jsonl", ("qid",)), ("career_events.jsonl", ("place_qid", "colony_qid"))):
            with (graph / name).open(encoding="utf-8") as handle:
                for line in handle:
                    if line.strip():
                        row = json.loads(line)
                        found.update(row[f] for f in fields if row.get(f))
        for name in ("places_grounding.jsonl",):
            path = root / f"data/{corpus}/{name}"
            if path.exists():
                for line in path.open(encoding="utf-8"):
                    if line.strip() and json.loads(line).get("qid"):
                        found.add(json.loads(line)["qid"])
    identities = root / "config/whg_place_identities.json"
    if identities.exists():
        config = json.loads(identities.read_text(encoding="utf-8"))
        for rule in config.get("period_identities", []):
            found.update(p["qid"] for p in rule["periods"] if p.get("qid"))
        found.update(r["qid"] for r in config.get("surface_identities", {}).values() if r.get("qid"))
    return sorted(q for q in found if re.fullmatch(r"Q\d+", q))


def year(literal):
    m = re.match(r"(-?\d+)-", literal or "")
    return int(m[1]) if m else None


def fetch_points(qids):
    """(qid, [lon, lat]) for each P625 value. QLever returns 'POINT(lon lat)'."""
    for b in sparql(f"SELECT ?q ?p WHERE {{ VALUES ?q {{ {values(qids)} }} ?q wdt:P625 ?p }}"):
        m = re.match(r"point\(\s*([-\d.eE]+)\s+([-\d.eE]+)\s*\)", b["p"]["value"], re.I)
        if m:
            yield qid(b["q"]["value"]), [float(m[1]), float(m[2])]


def fetch(qids):
    out = {q: {"label": None, "classes": [], "coords": [], "inception": [], "dissolved": [],
               "countries": []} for q in qids}
    for i in range(0, len(qids), 400):
        batch = qids[i:i + 400]
        v = values(batch)
        for b in sparql(f'SELECT ?q ?l WHERE {{ VALUES ?q {{ {v} }} ?q rdfs:label ?l FILTER(LANG(?l)="en") }}'):
            out[qid(b["q"]["value"])]["label"] = b["l"]["value"]
        for b in sparql(f"SELECT ?q ?c WHERE {{ VALUES ?q {{ {v} }} ?q wdt:P31 ?c }}"):
            out[qid(b["q"]["value"])]["classes"].append(qid(b["c"]["value"]))
        for q, point in fetch_points(batch):
            out[q]["coords"].append(point)
        for prop, key in (("P571", "inception"), ("P576", "dissolved")):
            for b in sparql(f"SELECT ?q ?t WHERE {{ VALUES ?q {{ {v} }} ?q wdt:{prop} ?t }}"):
                y = year(b["t"]["value"])
                if y is not None:
                    out[qid(b["q"]["value"])][key].append(y)
        for b in sparql(f"SELECT ?q ?c WHERE {{ VALUES ?q {{ {v} }} ?q wdt:P17 ?c }}"):
            out[qid(b["q"]["value"])]["countries"].append(qid(b["c"]["value"]))
        print(f"  entities {min(i + 400, len(qids))}/{len(qids)}", flush=True)
    for rec in out.values():
        for key in ("classes", "coords", "inception", "dissolved", "countries"):
            rec[key] = sorted({json.dumps(x) for x in rec[key]}) if key == "coords" else sorted(set(rec[key]))
        rec["coords"] = [json.loads(x) for x in rec["coords"]]
    return out


def fetch_classes(class_qids, known):
    """Label, AAT ID and up to three superclass hops for each P31 class."""
    todo, classes = list(class_qids), {}
    for depth in range(3):
        todo = sorted(c for c in set(todo) if c not in classes and c not in known)
        if not todo:
            break
        for i in range(0, len(todo), 400):
            v = values(todo[i:i + 400])
            for c in todo[i:i + 400]:
                classes[c] = {"label": None, "aat": [], "parents": []}
            for b in sparql(f'SELECT ?c ?l WHERE {{ VALUES ?c {{ {v} }} ?c rdfs:label ?l FILTER(LANG(?l)="en") }}'):
                classes[qid(b["c"]["value"])]["label"] = b["l"]["value"]
            for b in sparql(f"SELECT ?c ?a WHERE {{ VALUES ?c {{ {v} }} ?c wdt:P1014 ?a }}"):
                classes[qid(b["c"]["value"])]["aat"].append(b["a"]["value"])
            for b in sparql(f"SELECT ?c ?p WHERE {{ VALUES ?c {{ {v} }} ?c wdt:P279 ?p }}"):
                classes[qid(b["c"]["value"])]["parents"].append(qid(b["p"]["value"]))
        todo = [p for c in todo for p in classes[c]["parents"]]
        print(f"  class depth {depth}: {len(classes)} classes", flush=True)
    for rec in classes.values():
        rec["aat"], rec["parents"] = sorted(set(rec["aat"])), sorted(set(rec["parents"]))
    return classes


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--refresh", action="store_true")
    parser.add_argument("--refetch-coords", action="store_true",
                        help="refetch P625 points for every cached entity")
    args = parser.parse_args()
    cache = {"entities": {}, "classes": {}}
    if CACHE.exists() and not args.refresh:
        cache = json.loads(CACHE.read_text(encoding="utf-8"))
    qids = candidate_qids(ROOT)
    missing = [q for q in qids if q not in cache["entities"]]
    print(f"{len(qids)} candidate QIDs, {len(missing)} to fetch")
    CACHE.parent.mkdir(parents=True, exist_ok=True)
    if args.refetch_coords:
        cached = sorted(cache["entities"])
        for e in cache["entities"].values():
            e["coords"] = []
        for i in range(0, len(cached), 200):
            for q, point in fetch_points(cached[i:i + 200]):
                if point not in cache["entities"][q]["coords"]:
                    cache["entities"][q]["coords"].append(point)
            print(f"  coords {min(i + 200, len(cached))}/{len(cached)}", flush=True)
    if missing:
        cache["entities"].update(fetch(missing))
        CACHE.write_text(json.dumps(cache, ensure_ascii=False, indent=1, sort_keys=True) + "\n", encoding="utf-8")
    wanted = {c for e in cache["entities"].values() for c in e["classes"]}
    new = fetch_classes(wanted, cache["classes"])
    cache["classes"].update(new)
    CACHE.write_text(json.dumps(cache, ensure_ascii=False, indent=1, sort_keys=True) + "\n", encoding="utf-8")
    cache["classes"].update(new)
    # Superclasses of newly reached classes may still be missing; one more pass.
    cache["classes"].update(fetch_classes({p for c in new.values() for p in c["parents"]}, cache["classes"]))
    cache["source"] = {"endpoint": QLEVER, "fetched": time.strftime("%Y-%m-%d")}
    CACHE.parent.mkdir(parents=True, exist_ok=True)
    CACHE.write_text(json.dumps(cache, ensure_ascii=False, indent=1, sort_keys=True) + "\n", encoding="utf-8")
    print(f"wrote {CACHE}: {len(cache['entities'])} entities, {len(cache['classes'])} classes")


if __name__ == "__main__":
    main()
