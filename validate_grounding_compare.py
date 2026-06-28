import json, re, collections
G='data/kg/graph_stage3/'
# our side: career_facts keyed by exact id and base id
import re as _re
def base(pid): return _re.sub(r'_s\d+$','',pid)
cf=collections.defaultdict(list)
for l in open(G+'career_facts.jsonl'):
    d=json.loads(l); cf[d['person_id']].append(d); 
    b=base(d['person_id'])
    if b!=d['person_id']: cf[b].append(d)
# persons birth
pbirth={}
for l in open(G+'persons.jsonl'):
    d=json.loads(l); pbirth[d['person_id']]=d.get('birth_year')

# WD positions by qid
wd=collections.defaultdict(list)
for l in open('/tmp/wd_positions.jsonl'):
    wd[json.loads(l)['qid']].append(json.loads(l))

# place-name normalization
ROLE_PREFIX=re.compile(r'^(lieutenant[- ]governor|governor[- ]general|governor|administrator|colonial secretary|chief secretary|chief justice|president|premier|prime minister|attorney[- ]general|bishop|archbishop|high commissioner|resident|commissioner|chief commissioner|member of the legislative (assembly|council)|member of parliament|speaker|agent[- ]general|consul[- ]general|consul|chief native commissioner|puisne judge|judge|secretary)\b',re.I)
STOP=re.compile(r'\b(of|the|colony|province|dominion|state|island[s]?|british|mandatory|protectorate|crown|territory|territories|settlements?|presidency|and|federation|union|new)\b',re.I)
def norm_place(s):
    s=s.lower()
    s=re.sub(r'[^a-z\s-]',' ',s)
    s=STOP.sub(' ',s)
    return set(t for t in s.split() if len(t)>2)
def place_from_pos(poslabel):
    m=ROLE_PREFIX.search(poslabel)
    if m:
        rest=poslabel[m.end():]
        rest=re.sub(r'^\s*(of|for|in)\s+','',rest,flags=re.I)
        return rest
    return ''  # not a place-bearing position

ground=[json.loads(l) for l in open(G+'person_grounding.final.jsonl')]
results=[]
for r in ground:
    pid=r['person_id']; qid=r['qid']
    facts=cf.get(pid,[])
    our_names=set(); our_tokens=set(); our_qids=set()
    for f in facts:
        for lab in (f.get('colony_label'),f.get('place_label')):
            if lab: our_names.add(lab); our_tokens|=norm_place(lab)
        for q in (f.get('colony_qid'),f.get('place_qid')):
            if q: our_qids.add(q)
    # WD side
    wd_names=set(); wd_tokens=set(); wd_qids=set(); wd_poslabels=[]
    for w in wd.get(qid,[]):
        wd_poslabels.append(w['pos'])
        for lab in (w.get('jurLabel'),w.get('posJurLabel')):
            if lab: wd_names.add(lab); wd_tokens|=norm_place(lab)
        for q in (w.get('jur'),w.get('posJur')):
            if q: wd_qids.add(q)
        pl=place_from_pos(w['pos'])
        if pl: wd_names.add(pl); wd_tokens|=norm_place(pl)
    qid_overlap=our_qids & wd_qids
    tok_overlap=our_tokens & wd_tokens
    results.append({'pid':pid,'qid':qid,'wd_name':r['wd_name'],'tier':r['tier'],
        'n_our_facts':len(facts),'our_names':sorted(our_names),'wd_names':sorted(wd_names),
        'our_tokens':sorted(our_tokens),'wd_tokens':sorted(wd_tokens),
        'qid_overlap':sorted(qid_overlap),'tok_overlap':sorted(tok_overlap),
        'wd_has_positions':qid in wd,'wd_poslabels':wd_poslabels})

json.dump(results,open('/tmp/compare_results.json','w'))
# Summarize
n=len(results)
nposed=sum(1 for r in results if r['wd_has_positions'])
print(f"grounded persons: {n}; have WD P39 positions: {nposed}")
# among those with WD positions that bear a place (wd_tokens nonempty) AND we have facts:
cmp=[r for r in results if r['wd_tokens'] and r['our_tokens']]
print(f"comparable (both sides have place tokens): {len(cmp)}")
full=[r for r in cmp if r['tok_overlap']]
disj=[r for r in cmp if not r['tok_overlap']]
qidmatch=[r for r in cmp if r['qid_overlap']]
print(f"  name-token overlap >=1: {len(full)} ({100*len(full)/len(cmp):.1f}%)")
print(f"  DISJOINT (no shared place token): {len(disj)} ({100*len(disj)/len(cmp):.1f}%)  <-- candidate errors")
print(f"  (bonus) direct QID overlap: {len(qidmatch)}")
print("\n=== Sample DISJOINT cases (our colonies vs WD jurisdictions) ===")
for r in disj[:25]:
    print(f"  {r['qid']} {r['wd_name']} [{r['tier']}]  OUR={r['our_names']}  WD={r['wd_names']}")
