import urllib.request, json, time, sys
QIDS=sorted(set(json.loads(l)['qid'] for l in open('data/kg/graph_stage3/person_grounding.final.jsonl')))
print("QIDs:", len(QIDS), file=sys.stderr)
HDR={'Content-Type':'application/sparql-query','Accept':'application/sparql-results+json'}
PREFIX='''PREFIX wd: <http://www.wikidata.org/entity/>
PREFIX p: <http://www.wikidata.org/prop/>
PREFIX ps: <http://www.wikidata.org/prop/statement/>
PREFIX pq: <http://www.wikidata.org/prop/qualifier/>
PREFIX wdt: <http://www.wikidata.org/prop/direct/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
'''
def chunk(l,n):
    for i in range(0,len(l),n): yield l[i:i+n]
out=open('/tmp/wd_positions.jsonl','w')
nrows=0
for ci,qs in enumerate(chunk(QIDS,150)):
    vals=' '.join('wd:'+q for q in qs)
    Q=PREFIX+'''SELECT ?person ?posLabel ?jur ?jurLabel ?posJur ?posJurLabel ?start ?end WHERE {
  VALUES ?person { %s }
  ?person p:P39 ?st .
  ?st ps:P39 ?pos .
  OPTIONAL { ?pos rdfs:label ?posLabel . FILTER(LANG(?posLabel)="en") }
  OPTIONAL { ?st pq:P1001 ?jur . OPTIONAL { ?jur rdfs:label ?jurLabel . FILTER(LANG(?jurLabel)="en") } }
  OPTIONAL { ?pos wdt:P1001 ?posJur . OPTIONAL { ?posJur rdfs:label ?posJurLabel . FILTER(LANG(?posJurLabel)="en") } }
  OPTIONAL { ?st pq:P580 ?start }
  OPTIONAL { ?st pq:P582 ?end }
}'''%vals
    for attempt in range(3):
        try:
            req=urllib.request.Request('https://qlever.dev/api/wikidata',data=Q.encode(),headers=HDR)
            r=json.load(urllib.request.urlopen(req,timeout=120))
            break
        except Exception as e:
            print("retry",ci,e,file=sys.stderr); time.sleep(3)
    else:
        print("FAILED chunk",ci,file=sys.stderr); continue
    for b in r['results']['bindings']:
        g=lambda k: b.get(k,{}).get('value','')
        rec={'qid':g('person').split('/')[-1],'pos':g('posLabel'),
             'jur':g('jur').split('/')[-1],'jurLabel':g('jurLabel'),
             'posJur':g('posJur').split('/')[-1],'posJurLabel':g('posJurLabel'),
             'start':g('start')[:4],'end':g('end')[:4]}
        out.write(json.dumps(rec)+'\n'); nrows+=1
    print("chunk",ci,"done, rows so far",nrows,file=sys.stderr); time.sleep(1)
out.close()
print("TOTAL position rows:",nrows,file=sys.stderr)
