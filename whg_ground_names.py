#!/usr/bin/env python3
"""Propose Wikidata matches for name-only gazetteer places, conservatively.

For each exported name-only record (out/whg/places.jsonl), look up its
unabbreviated printed forms as exact English labels or aliases on QLever, keep
candidates with a point, and accept only when exactly one candidate place lies
within RADIUS_KM of the record's career-context colony. No string similarity,
no ranking: the colony anchors the reading (Kalgoorlie near Western Australia,
not a namesake elsewhere). Organisation and person items are refused.

Writes config/whg_name_groundings.json, which build_whg_gazetteer.py applies.
Rerun the build afterwards.

    python3 whg_ground_names.py
"""
import collections
import json
import math
from pathlib import Path
import re
import time

from build_whg_gazetteer import NON_PLACE_CLASSES, ROOT, clean_toponym, is_abbreviated, rows
from whg_fetch_wikidata import qid, sparql

RADIUS_KM = 250
OUT = ROOT / "config/whg_name_groundings.json"
CACHE = ROOT / "data/whg/name_candidates.json"


def km(a, b):
    la1, lo1, la2, lo2 = map(math.radians, (a[1], a[0], b[1], b[0]))
    h = math.sin((la2 - la1) / 2) ** 2 + math.cos(la1) * math.cos(la2) * math.sin((lo2 - lo1) / 2) ** 2
    return 6371 * 2 * math.asin(math.sqrt(h))


def literal(text):
    return '"' + text.replace("\\", "\\\\").replace('"', '\\"') + '"@en'


def candidates(labels):
    """label -> {qid: {"coords": [...], "classes": [labels]}} (cached). Label and
    alias lookups run as separate light queries; QLever rate-limits heavier ones."""
    cache = json.loads(CACHE.read_text()) if CACHE.exists() else {}
    todo = sorted(l for l in labels if l not in cache)
    for i in range(0, len(todo), 100):
        batch = todo[i:i + 100]
        found = collections.defaultdict(dict)
        v = " ".join(literal(l) for l in batch)
        for prop in ("rdfs:label", "skos:altLabel"):
            q = (f"PREFIX skos: <http://www.w3.org/2004/02/skos/core#> SELECT ?l ?q ?p WHERE {{ "
                 f"VALUES ?l {{ {v} }} ?q {prop} ?l . ?q wdt:P625 ?p }}")
            for b in sparql(q):
                m = re.match(r"point\(\s*([-\d.eE]+)\s+([-\d.eE]+)\s*\)", b["p"]["value"], re.I)
                if m:
                    found[b["l"]["value"]].setdefault(qid(b["q"]["value"]),
                                                      {"coords": [float(m[1]), float(m[2])], "classes": []})
            time.sleep(3)
        items = sorted({q for recs in found.values() for q in recs})
        classes = collections.defaultdict(set)
        for j in range(0, len(items), 200):
            iv = " ".join("wd:" + q for q in items[j:j + 200])
            for b in sparql(f'SELECT ?q ?cl WHERE {{ VALUES ?q {{ {iv} }} ?q wdt:P31 ?c . '
                            f'?c rdfs:label ?cl FILTER(LANG(?cl)="en") }}'):
                classes[qid(b["q"]["value"])].add(b["cl"]["value"])
            time.sleep(3)
        for label in batch:
            recs = found.get(label, {})
            for q, rec in recs.items():
                rec["classes"] = sorted(classes.get(q, ()))
            cache[label] = recs
        CACHE.parent.mkdir(parents=True, exist_ok=True)
        CACHE.write_text(json.dumps(cache, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8")
        print(f"  labels {min(i + 100, len(todo))}/{len(todo)}", flush=True)
    return cache


def main():
    authority = json.loads((ROOT / "data/whg/wikidata_places.json").read_text())["entities"]
    overrides = json.loads((ROOT / "config/whg_place_identities.json").read_text()).get("geometry_overrides", {})

    def point(q):
        if q in overrides:
            return [overrides[q]["lon"], overrides[q]["lat"]]
        c = authority.get(q, {}).get("coords")
        return c[0] if c else None

    records = [p for _, p in rows(ROOT / "out/whg/places.jsonl")
               if p["key"].startswith("name:") and "held_single_abbreviated_name" not in p["review_issues"]]
    forms = {}
    for p in records:
        names = {clean_toponym(n) for n in list(p["printed_toponyms"]) + [p["title"]]}
        forms[p["key"]] = sorted(n for n in names if n and not is_abbreviated(n) and "," not in n
                                 and re.search(r"[A-Za-z]{3}", n))
    cache = candidates({n for ns in forms.values() for n in ns})
    accepted, stats = {}, collections.Counter()
    for p in records:
        anchors = [point(q) for q in p.get("context_qids", []) if point(q)]
        if not anchors:
            stats["no_context_point"] += 1
            continue
        near = {}
        for name in forms[p["key"]]:
            for item, rec in cache.get(name, {}).items():
                if any(NON_PLACE_CLASSES.search(c) for c in rec["classes"]):
                    continue
                d = min(km(rec["coords"], a) for a in anchors)
                if d <= RADIUS_KM:
                    near.setdefault(item, (round(d), name, rec["classes"][:3]))
        if len(near) == 1:
            item, (d, name, classes) = next(iter(near.items()))
            accepted[p["key"]] = {"qid": item, "matched_label": name, "distance_km": d,
                                  "context_qids": p["context_qids"][:3], "classes": classes,
                                  "method": f"qlever exact label/alias, unique within {RADIUS_KM} km of career context"}
            stats["accepted"] += 1
        else:
            stats["ambiguous" if near else "no_candidate"] += 1
    OUT.write_text(json.dumps(dict(sorted(accepted.items())), ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(dict(stats), "->", OUT)


if __name__ == "__main__":
    main()
