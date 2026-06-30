#!/usr/bin/env python3
"""Probe: are unmatched SENIOR officials actually in Wikidata? (via QLever, fast/no-timeout)
For each unmatched person who held a governor/colonial-secretary/chief-justice role and
has a birth year, ask Wikidata for a human with that surname + exact birth year who holds
ANY P39 position. A hit = they ARE in Wikidata; Layer 1 (harvest) simply missed them."""
import ladybug, json, urllib.request, sys

QLEVER = "https://qlever.dev/api/wikidata"
PREFIX = ("PREFIX wd: <http://www.wikidata.org/entity/> "
          "PREFIX wdt: <http://www.wikidata.org/prop/direct/> "
          "PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> ")

def ask(sur, by):
    sur = sur.lower().replace('"', '')
    q = (PREFIX + f'SELECT ?item ?lab WHERE {{ ?item wdt:P31 wd:Q5 ; wdt:P569 ?dob ; '
         f'rdfs:label ?lab . FILTER(YEAR(?dob)={by}) FILTER(LANG(?lab)="en") '
         f'FILTER(CONTAINS(LCASE(?lab),"{sur}")) ?item wdt:P39 ?pos }} LIMIT 3')
    req = urllib.request.Request(QLEVER, data=q.encode(),
        headers={"Accept": "application/sparql-results+json",
                 "Content-type": "application/sparql-query"})
    try:
        r = json.load(urllib.request.urlopen(req, timeout=60))["results"]["bindings"]
    except Exception as e:
        return "ERR", str(e)[:50]
    seen = {b["item"]["value"].rsplit("/",1)[-1]: b["lab"]["value"] for b in r}
    return ("HIT" if seen else "miss"), "; ".join(f"{l} ({q})" for q,l in list(seen.items())[:2])

def main():
    db = ladybug.Database("data/kg/ladybug_db"); conn = ladybug.Connection(db)
    df = conn.execute("""MATCH (p:Person)-[:HAS_EVENT]->(:CareerEvent)-[:EVENT_ROLE]->(r:Role)
      WHERE p.wikidata_qid='' AND p.birth_year IS NOT NULL AND size(p.given_names)>4
        AND (r.label CONTAINS 'overnor' OR r.label CONTAINS 'olonial Secretary'
             OR r.label CONTAINS 'hief Justice')
      RETURN DISTINCT p.surname AS s, p.given_names AS g, p.birth_year AS b LIMIT 20""").get_as_df()
    hit = 0
    for _, row in df.iterrows():
        st, info = ask(row.s, int(row.b))
        if st == "HIT": hit += 1
        print(f"  [{st:4}] {row.s}, {row.g} (b{row.b})  {info}", flush=True)
    print(f"\nWikidata HITS among {len(df)} unmatched senior officials: {hit}/{len(df)}", flush=True)

if __name__ == "__main__":
    main()
