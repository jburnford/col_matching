#!/usr/bin/env python3
"""Verify grounded person QIDs against LIVE Wikidata (WDQS).

For every distinct QID in person_grounding.jsonl, pull fresh:
  P31 instance-of, P569 birth, owl:sameAs (redirect), P39 positions, P106 occupations.
Then flag:
  NOT_HUMAN     P31 has no Q5 (disambiguation page / list / org / deleted / redirect)
  REDIRECT      owl:sameAs present -> stale QID, should use the target
  NO_DATA       entity returns nothing (deleted / redirect / bad harvest QID)
  BIRTH_CONFLICT KG birth vs live P569 differ by >2
  NO_OFFICE     no P39 position AND no govt/military/colonial occupation (weak corroboration)
"""
import json, time, urllib.request, urllib.parse, os, sys, collections

ROOT = os.path.dirname(os.path.abspath(__file__))
KG = os.path.join(ROOT, "data/kg/graph_stage3")
GROUNDING = os.path.join(KG, "person_grounding.jsonl")
OUT = os.path.join(ROOT, "data/kg/person_qid_verification.jsonl")
ENDPOINT = "https://query.wikidata.org/sparql"
UA = "col-matching-kg/1.0 (cljim22@gmail.com)"
BATCH = 80

def sparql(q):
    data = urllib.parse.urlencode({"query": q}).encode()
    req = urllib.request.Request(ENDPOINT, data=data, headers={
        "User-Agent": UA, "Accept": "application/sparql-results+json"})
    with urllib.request.urlopen(req, timeout=90) as r:
        return json.load(r)["results"]["bindings"]

CORE_Q = """SELECT ?item ?dob ?redirect
  (GROUP_CONCAT(DISTINCT ?instQ; separator="|") AS ?insts)
  (GROUP_CONCAT(DISTINCT ?occL; separator="|") AS ?occs) WHERE {{
  VALUES ?item {{ {values} }}
  OPTIONAL {{ ?item wdt:P31 ?inst. BIND(STRAFTER(STR(?inst),"entity/") AS ?instQ) }}
  OPTIONAL {{ ?item wdt:P569 ?dob }}
  OPTIONAL {{ ?item owl:sameAs ?redirect. FILTER(STRSTARTS(STR(?redirect),"http://www.wikidata.org/entity/Q")) }}
  OPTIONAL {{ ?item wdt:P106 ?occ. ?occ rdfs:label ?occL. FILTER(LANG(?occL)="en") }}
}} GROUP BY ?item ?dob ?redirect"""

POS_Q = """SELECT ?item (GROUP_CONCAT(DISTINCT ?posL; separator="|") AS ?poss) WHERE {{
  VALUES ?item {{ {values} }}
  ?item p:P39 ?st. ?st ps:P39 ?pos. ?pos rdfs:label ?posL. FILTER(LANG(?posL)="en")
}} GROUP BY ?item"""

def year_of(v):
    if not v: return None
    neg = v.startswith("-")
    try: return (-1 if neg else 1) * int(v.lstrip("-").split("-")[0])
    except ValueError: return None

def run_batches(qids, template):
    out = {}
    for i in range(0, len(qids), BATCH):
        b = qids[i:i+BATCH]
        vals = " ".join(f"wd:{q}" for q in b)
        for attempt in range(4):
            try:
                rows = sparql(template.format(values=vals)); break
            except Exception as e:
                print(f"  retry {attempt} batch {i}: {e}", file=sys.stderr); time.sleep(5*(attempt+1))
        else:
            print(f"  FAILED batch {i}", file=sys.stderr); continue
        for r in rows:
            qid = r["item"]["value"].rsplit("/", 1)[-1]
            out[qid] = r
        print(f"  batch {i//BATCH+1}/{(len(qids)+BATCH-1)//BATCH}", file=sys.stderr)
        time.sleep(1)
    return out

OFFICE_KW = ("govern", "secretary", "administ", "commission", "minister", "officer",
             "judge", "magistrate", "colon", "diplomat", "politician", "official",
             "military", "army", "navy", "general", "colonel", "captain", "civil serv",
             "premier", "councillor", "mayor", "resident", "consul", "ambassador",
             "bishop", "clergy", "lawyer", "barrister", "police")

def main():
    rows = [json.loads(l) for l in open(GROUNDING)]
    by_qid = collections.defaultdict(list)
    for r in rows:
        by_qid[r["qid"]].append(r)
    qids = sorted(by_qid)
    print(f"verifying {len(qids)} distinct QIDs ({len(rows)} matches)")

    core = run_batches(qids, CORE_Q)
    pos = run_batches(qids, POS_Q)

    report = []
    for qid in qids:
        c = core.get(qid)
        flags = []
        insts = occs = redirect = live_birth = None
        positions = pos.get(qid, {}).get("poss", {}).get("value", "")
        if c is None:
            flags.append("NO_DATA")
        else:
            insts = c.get("insts", {}).get("value", "")
            occs = c.get("occs", {}).get("value", "")
            redirect = c.get("redirect", {}).get("value", "")
            live_birth = year_of(c.get("dob", {}).get("value"))
            if redirect:
                flags.append("REDIRECT")
            if not insts:
                flags.append("NO_DATA")
            elif "Q5" not in insts.split("|"):
                flags.append("NOT_HUMAN")
        # birth conflict vs each KG match
        kg_births = [m["kg_birth"] for m in by_qid[qid] if m.get("kg_birth")]
        if live_birth and kg_births and all(abs(b - live_birth) > 2 for b in kg_births):
            flags.append("BIRTH_CONFLICT")
        # office corroboration
        text = ((occs or "") + "|" + (positions or "")).lower()
        if not positions and not any(k in text for k in OFFICE_KW):
            flags.append("NO_OFFICE")
        report.append({
            "qid": qid, "flags": flags, "insts": insts, "occs": occs,
            "positions": positions[:300], "live_birth": live_birth,
            "redirect": (redirect or "").rsplit("/", 1)[-1] if redirect else None,
            "kg_matches": [{"pid": m["person_id"], "surname": m["kg_surname"],
                            "given": m["kg_given"], "birth": m["kg_birth"], "tier": m["tier"]}
                           for m in by_qid[qid]],
        })
    with open(OUT, "w") as fo:
        for r in report:
            fo.write(json.dumps(r) + "\n")
    fc = collections.Counter(f for r in report for f in r["flags"])
    clean = sum(1 for r in report if not r["flags"])
    print(f"\nclean QIDs: {clean}/{len(qids)}")
    print("flag counts:", dict(fc))

if __name__ == "__main__":
    main()
