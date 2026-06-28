import json, re, collections
G='data/kg/graph_stage3/'
def base(pid): return re.sub(r'_s\d+$','',pid)
# our career tokens per person
ROLE_PREFIX=re.compile(r'^(lieutenant[- ]governor|governor[- ]general|governor|administrator|colonial secretary|chief secretary|chief justice|president|premier|prime minister|attorney[- ]general|bishop|archbishop|high commissioner|resident|commissioner|chief commissioner|member of the legislative (assembly|council)|member of the house of (commons|assembly)|member of parliament|member of the senate|senator|speaker|agent[- ]general|consul[- ]general|consul|chief native commissioner|puisne judge|judge|justice|delegate|minister|treasurer|secretary)\b',re.I)
STOP=re.compile(r'\b(of|for|in|to|the|colony|province|dominion|state|island[s]?|british|mandatory|protectorate|crown|territory|territories|settlements?|presidency|and|federation|union|new|legislative|assembly|council|supreme|court|house|commons|senate)\b',re.I)
def toks(s):
    s=re.sub(r'[^a-z\s-]',' ',s.lower()); s=STOP.sub(' ',s)
    return set(t for t in s.split() if len(t)>2)
def place_from_pos(p):
    m=ROLE_PREFIX.search(p)
    if not m: return ''
    rest=re.sub(r'^\s*(of|for|in|to)\s+','',p[m.end():],flags=re.I)
    return rest
# WD junk markers (non-geographic jurisdictions -> not "data we lack")
JUNK=re.compile(r'royal geograph|society|spy base|privy council|geological',re.I)
DIPLO=re.compile(r'High Commissioner of the United Kingdom|ambassador of the United Kingdom|ambassador of Israel|Canadian ambassador',re.I)

cf=collections.defaultdict(set)
for l in open(G+'career_facts.jsonl'):
    d=json.loads(l)
    for k in (d['person_id'], base(d['person_id'])):
        for lab in (d.get('colony_label'),d.get('place_label')):
            if lab: cf[k]|=toks(lab)
wd=collections.defaultdict(list)
for l in open('/tmp/wd_positions.jsonl'):
    d=json.loads(l); wd[d['qid']].append(d)

ground=[json.loads(l) for l in open(G+'person_grounding.final.jsonl')]  # cleaned
flags=[]
for r in ground:
    pid,qid=r['person_id'],r['qid']
    ours=cf.get(pid) or cf.get(base(pid)) or set()
    extra=[]
    seen=set()
    for w in wd.get(qid,[]):
        place=w.get('jurLabel') or w.get('posJurLabel') or place_from_pos(w['pos'])
        pt=toks(place) if place else set()
        if not pt: continue                      # no geographic place -> skip
        if JUNK.search(w['pos']): continue
        if pt & ours: continue                   # we already have this place
        key=(w['pos'],place)
        if key in seen: continue
        seen.add(key)
        kind='diplomatic' if DIPLO.search(w['pos']) else 'colonial/other'
        extra.append({'pos':w['pos'],'place':place,'start':w['start'],'end':w['end'],'kind':kind})
    if extra:
        flags.append({'person_id':pid,'qid':qid,'wd_name':r['wd_name'],'tier':r['tier'],
                      'n_extra':len(extra),'extra':extra})
json.dump(flags,open(G+'wikidata_has_more.json','w'),ensure_ascii=False,indent=1)
nd=sum(1 for f in flags if any(e['kind']=='diplomatic' for e in f['extra']))
print(f"grounded persons: {len(ground)}")
print(f"persons where WD records jurisdictions we DON'T have: {len(flags)}")
print(f"  (of these, {nd} include a UK/diplomatic post)")
print(f"wrote {G}wikidata_has_more.json")
print("\nExamples (WD has career data beyond our bios):")
for f in flags[:12]:
    ex='; '.join(f"{e['pos']}" for e in f['extra'][:2])
    print(f"  {f['wd_name']} ({f['qid']}) +{f['n_extra']}: {ex}")
