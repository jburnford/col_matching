#!/usr/bin/env python3
"""Propose Wikidata matches for name-only gazetteer places, conservatively.

For each exported name-only record (out/whg/places.jsonl), look up its
unabbreviated printed forms as exact English labels or aliases on QLever, keep
candidates with a point, and accept only when exactly one candidate place lies
within RADIUS_KM of the record's career-context colony. No string similarity,
no ranking: the colony anchors the reading (Kalgoorlie near Western Australia,
not a namesake elsewhere). Organisation and person items are refused.

Writes PROPOSALS to config/whg_name_groundings.json (and a TSV beside it in
data/whg/). A sampled check found roughly one in ten doubtful (anachronistic or
namesake items), so the build applies an entry only after a reviewer sets
"reviewed": true on it. Reruns keep existing review flags.

    python3 whg_ground_names.py
"""
import collections
import json
import math
from pathlib import Path
import re
import time

from build_whg_gazetteer import (CLASS_RULES, NON_PLACE_CLASSES, ROOT, _SITE, clean_toponym,
                                 is_abbreviated, rows)
from whg_fetch_wikidata import qid, sparql

RADIUS_KM = 250
# Classes a namesake often has that a printed posting place is not.
REFUSED = re.compile(r"\b(meteorite|electoral|constituency|division of the|stop|street|road|"
                     r"building|church|school|company|ship|hotel|house|station|ward|"
                     r"railway|airport|star|asteroid|crater|family name|given name|wikimedia|"
                     r"toponym|disambiguation)\b", re.I)
# A single point for a whole country (or the UK metropole, plotted at London)
# cannot anchor a 250 km test: dozens of Petersburgs, two Cheadles.
NATIONAL = re.compile(r"\b(sovereign state|country|federal|metropole)\b", re.I)
NATIONAL_QIDS = {"Q84", "Q145", "Q30", "Q16", "Q129286", "Q408", "Q148", "Q159", "Q142", "Q183", "Q38", "Q17"}
PLACE_CODES = {"P", "A", "H", "T", "L"}


def acceptable(classes, printed):
    """A settlement, polity, water, landform or region class; sites only when
    the printed name itself names a site ('Larkhill camp')."""
    if not classes or any(NON_PLACE_CLASSES.search(c) or REFUSED.search(c) for c in classes):
        return False
    codes = {next((code for code, pat in CLASS_RULES if re.search(pat, c, re.I)), None) for c in classes}
    return bool(codes & PLACE_CODES) or ("S" in codes and bool(_SITE.search(printed)))
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

    with (ROOT / "data/whg/wikidata_places.json").open(encoding="utf-8") as handle:
        class_labels = json.load(handle)["classes"]

    def classes_of(q):
        return [class_labels.get(c, {}).get("label") or "" for c in authority.get(q, {}).get("classes", [])]

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
        contexts = [q for q in p.get("context_qids", []) if q not in NATIONAL_QIDS
                    and not any(NATIONAL.search(c) for c in classes_of(q))]
        anchors = [point(q) for q in contexts if point(q)]
        if not anchors:
            stats["no_context_point"] += 1
            continue
        near = {}
        for name in forms[p["key"]]:
            for item, rec in cache.get(name, {}).items():
                if not acceptable(rec["classes"], name):
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
    previous = json.loads(OUT.read_text(encoding="utf-8")) if OUT.exists() else {}
    for key, v in accepted.items():  # keep a reviewer's decision if the proposal is unchanged
        old = previous.get(key, {})
        v["reviewed"] = bool(old.get("reviewed")) and old.get("qid") == v["qid"]
    OUT.write_text(json.dumps(dict(sorted(accepted.items())), ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    with (ROOT / "data/whg/name_grounding_proposals.tsv").open("w", encoding="utf-8") as handle:
        handle.write("place_key\tproposed_qid\tmatched_label\tdistance_km\tcontext_qids\tclasses\treviewed\n")
        for key, v in sorted(accepted.items()):
            handle.write("\t".join([key, v["qid"], v["matched_label"], str(v["distance_km"]),
                                    ";".join(v["context_qids"]), ";".join(v["classes"]),
                                    str(v["reviewed"]).lower()]) + "\n")
    print(dict(stats), "->", OUT)


if __name__ == "__main__":
    main()
