#!/usr/bin/env python3
"""Fetch birth year (P569) for harvested-candidate WD QIDs from WDQS.
Known-QID lookup (not disambiguation) -> SPARQL is reliable here."""
import json, time, urllib.request, urllib.parse, os, sys

ROOT = os.path.dirname(os.path.abspath(__file__))
QIDS = os.path.join(ROOT, "data/kg/wd_person_qids_to_fetch.txt")
OUT = os.path.join(ROOT, "data/kg/wd_person_dob.jsonl")
ENDPOINT = "https://query.wikidata.org/sparql"
UA = "col-matching-kg/1.0 (cljim22@gmail.com)"
BATCH = 250

def query(qids):
    values = " ".join(f"wd:{q}" for q in qids)
    q = f"SELECT ?item ?dob WHERE {{ VALUES ?item {{ {values} }} OPTIONAL {{ ?item wdt:P569 ?dob }} }}"
    data = urllib.parse.urlencode({"query": q}).encode()
    req = urllib.request.Request(ENDPOINT, data=data, headers={
        "User-Agent": UA, "Accept": "application/sparql-results+json"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.load(r)

def main():
    qids = [l.strip() for l in open(QIDS) if l.strip()]
    done = set()
    if os.path.exists(OUT):
        for l in open(OUT):
            done.add(json.loads(l)["qid"])
    todo = [q for q in qids if q not in done]
    print(f"{len(qids)} total, {len(done)} cached, {len(todo)} to fetch")
    fo = open(OUT, "a")
    for i in range(0, len(todo), BATCH):
        batch = todo[i:i+BATCH]
        for attempt in range(4):
            try:
                res = query(batch)
                break
            except Exception as e:
                print(f"  retry {attempt} batch {i}: {e}", file=sys.stderr)
                time.sleep(5 * (attempt + 1))
        else:
            print(f"  FAILED batch {i}", file=sys.stderr); continue
        years = {}
        for b in res["results"]["bindings"]:
            qid = b["item"]["value"].rsplit("/", 1)[-1]
            if "dob" in b:
                v = b["dob"]["value"]
                neg = v.startswith("-")
                yr = v.lstrip("-").split("-")[0]
                try: years[qid] = -int(yr) if neg else int(yr)
                except ValueError: pass
        for q in batch:
            fo.write(json.dumps({"qid": q, "year": years.get(q)}) + "\n")
        fo.flush()
        print(f"  batch {i//BATCH+1}/{(len(todo)+BATCH-1)//BATCH}: {sum(1 for q in batch if q in years)}/{len(batch)} with DOB")
        time.sleep(1)
    fo.close()

if __name__ == "__main__":
    main()
