#!/usr/bin/env python3
"""Build and inspect the fixed, pre-review top-500 atlas cohort."""
import collections, json, re, sys
from pathlib import Path
from build_static_atlas import build_canon
from atlas_geography import project
ROOT=Path(__file__).resolve().parent
OUT=ROOT/'research/top-500-careers-2026-10-07'

def dump(name,value): (OUT/name).write_text(json.dumps(value,ensure_ascii=False,indent=1)+'\n')
def prepare():
    if (OUT/'ranking.json').exists():
        raise SystemExit('The starting ranking is frozen; use a new dated audit directory.')
    careers=json.loads((ROOT/'docs/data/careers.json').read_text())['persons']
    places=json.loads((ROOT/'docs/data/places.json').read_text())
    arcs=json.loads((ROOT/'docs/data/arcs.json').read_text())
    counts=collections.Counter(a[3] for a in arcs)
    ranked=sorted(counts,key=lambda p:(-counts[p],careers[p]['nm'].casefold(),p))[:500]
    dossiers={pid:{'rank':i+1,'person_id':pid,'name':careers[pid]['nm'],'moves_before':counts[pid],
                    'corpus':'iol' if careers[pid]['c'] else 'kg','events':[],'sources':[]} for i,pid in enumerate(ranked)}
    canon=build_canon(); wanted=collections.defaultdict(set)
    for corpus in ('kg','iol'):
        gd=ROOT/f'data/{corpus}/graph_stage3'
        for line in (gd/'persons.jsonl').open():
            p=json.loads(line);pid=p['person_id']
            if pid in dossiers:
                dossiers[pid]['person']=p
                for att in p.get('attestations',[]):wanted[att].add(pid)
        for line in (gd/'career_events.jsonl').open():
            e=json.loads(line);pid=canon(e['person_id'])
            if pid in dossiers:
                key,node=project(e)
                dossiers[pid]['events'].append({**e,'map_key':key,'map':node})
    # CO source biographies: retain all attestations, not merely the longest one.
    for path in sorted((ROOT/'data/kg/bios').glob('*.jsonl')):
        for line in path.open():
            b=json.loads(line)
            for pid in wanted.get(b['bio_id'],[]):
                dossiers[pid]['sources'].append({'bio_id':b['bio_id'],'path':str(path.relative_to(ROOT)),
                    'year':b['edition_year'],'text':b['raw_text'],'surname':b.get('surname'),'birth_year':b.get('birth_year')})
    # IOL bios are recoverable directly from the original HTML character offsets.
    from col_match.volume.iol_reader import available_editions, load_edition
    from col_match.volume.iol_bios import _PARA,_text,_iol_headword
    byedition=collections.defaultdict(list)
    for att,pids in wanted.items():
        m=re.fullmatch(r'iol(.+)-c(\d+)',att)
        if m:byedition[m[1]].append((int(m[2]),att,pids))
    for ek in available_editions()[0]:
        if ek.tag not in byedition:continue
        html,_=load_edition(ek)
        for pos,att,pids in byedition[ek.tag]:
            parts=[]
            for pm in _PARA.finditer(html,pos,min(pos+35000,len(html))):
                text=_text(pm.group(1))
                if parts and _iol_headword(text):break
                if text:parts.append(text)
            if parts:
                src={'bio_id':att,'path':str(ek.html_path.relative_to(ROOT)),'char_offset':pos,
                     'year':ek.year,'text':' '.join(parts),'offset_exact':html[pos:pos+2]=='<p'}
                for pid in pids:dossiers[pid]['sources'].append(src)
    for d in dossiers.values():
        d['sources'].sort(key=lambda s:(s['year'],len(s['text'])),reverse=True)
        d['arcs_before']=[a for a in arcs if a[3]==d['person_id']]
    dump('dossiers.json',list(dossiers.values()))
    dump('ranking.json',[{k:d[k] for k in ('rank','person_id','name','moves_before','corpus')} for d in dossiers.values()])
    print('prepared',len(dossiers),'careers; sources',sum(len(d['sources']) for d in dossiers.values()),
          'missing',[(d['rank'],d['name']) for d in dossiers.values() if not d['sources']])

def show(lo,hi,source=False):
    ds=json.loads((OUT/'dossiers.json').read_text())
    for d in ds[lo-1:hi]:
        print(f"\n#{d['rank']} {d['name']} | {d['person_id']} | {d['moves_before']} arcs | {len(d['sources'])} sources")
        if source:
            ss=sorted(d['sources'],key=lambda s:len(s['text']),reverse=True)
            if ss:print('SOURCE',ss[0]['bio_id'],ss[0]['text'])
        for e in d['events']:
            m=e['map'];dest=(m['label']+' ['+m['entity_qid']+']') if m else 'UNPLACED'
            print(f"{e['seq']}:{e.get('year_start') or '?'}{'–'+str(e['year_end']) if e.get('year_end') else ''} {e.get('position')} | {e.get('place_raw')} => {dest}")

if __name__=='__main__':
    if sys.argv[1]=='prepare':prepare()
    else:show(int(sys.argv[1]),int(sys.argv[2]),'--source' in sys.argv)
