#!/usr/bin/env python3
"""Publish the frozen inspection cohort, applied changes and remaining questions."""
import collections, csv, json
from pathlib import Path
from historical_geography import correct_event
from atlas_geography import project
ROOT=Path(__file__).resolve().parent
AUDIT=ROOT/'research/top-500-careers-2026-10-07'
OUT=ROOT/'docs/review/top-500'

ADJUDICATION={
 1:'Japan 1865 and Brussels 1870 were not taken up. Both appointments remain as source events, with no held-office or movement assertion. Same-year order is no longer inferred.',
 2:'Early editions establish Ceylon 1877. The 1887 duplicate is corrected; inherited New Orleans and West Indies locations on the 1886 exhibition committee are withdrawn.',
 3:'Prince Albert is the Cape town. Bredasdorp replaces Brodsworth for 1874; inherited Brodsworth on later central-office jobs is withdrawn.',
 23:'The source supports the Straits Settlements commission and Mauritius mission. The initial suspicion of mixed people is not established. Conflicting years remain open.',
 25:'The source explicitly records private-secretary service with Hercules Robinson in St Kitts and Hong Kong, 1855–60. This is not evidence of a false person merge; individual arrival dates remain unresolved.',
 72:'The source says he declined re-election to the medical association, but the extracted 1867 events do not assert an unaccepted cabinet office. No appointment was removed on this flag.',
 77:'Cadet appointment corrected from 1830 to 1880. Tenom/FMS grounding withdrawn: the source describes the Penom mission.',
 85:'1849 is entry to diplomatic service, not a date for every subsequent attaché posting. Those events remain in the record with unresolved individual dates.',
 92:'The Canadian politician’s Manitoba/Winnipeg events are withdrawn from the Ceylon engineer’s career. Person-record separation remains open.',
 118:'The source combines Alfred Earle, Octavus and Septimus Burt. The composite is withdrawn from office/movement assertions pending reconstruction; no Newcastle journey is asserted.',
 123:'A checked source supports Jamaica 1931–45 and British Guiana 1946. Earlier inherited and conflicting locations still require event-by-event reconstruction.',
 151:'D.W.W.I. is an administrative abbreviation in the West Indies, not Danish West Indies. Its false location is withdrawn; other mixed entomologist/agricultural events need attribution review.',
 163:'Montserrat and St George occur in Trinidad district service, not a journey to the island of Montserrat or Grenada. Those false matches are withdrawn; emigration-agent workplace needs further review.',
 233:'1835/1837/1839 corrected to 1885/1887/1889 against the 1894 source biography.',
 324:'The fuller source places the 1927 job in Northern Province, Uganda. Ceylon is removed; the precise province coordinate remains unresolved.',
 358:'One source ends with New Hebrides, another gives the Afghan embassy. The contradictory New Hebrides attribution is withdrawn, rather than silently converted to an Afghan event.',
 374:'The 1893 viceroy appointment was not taken up. It remains visible as an unaccepted appointment and is excluded from held office and movement.',
 393:'W.I. is Western India in this political-service record. The West Indies match is corrected; the agency has no verified coordinate in this cache.',
 419:'States of W.I. means Western India here. The West Indies match is corrected; the agency remains unplotted pending a coordinate.',
 420:'The 1906 source explicitly places the collectorship in Sind. Hyderabad is corrected to the Sind city, not Hyderabad State in India.',
 449:'West Africa Settlements no longer maps to London. This Samuel Rowe is distinct from the younger R. H. Rowe; their apparent similarity was not a valid merge.',
 457:'The 1915 Kenya crown-counsel appointment was not taken up. It is excluded from office/movement assertions and retained as an appointment event.',
 463:'W.I. States Agency and States of W.I. are Western India in this source. The false West Indies journey is removed.',
 468:'A separate Newfoundland legislator’s biography is present among the attestations. Those events are withdrawn from the Natal official; person-record separation remains open.',
 499:'Alexandria is the Cape district, not Egypt. Sources disagree between 1882 and 1892; geography is corrected and the year conflict remains open.'}
QUARANTINED={12,16,30,52,57,118,160}

def main():
 OUT.mkdir(parents=True,exist_ok=True)
 ds=json.loads((AUDIT/'dossiers.json').read_text())
 notes={int(n):(tags.split(','),note) for n,tags,note in (line.split('|',2) for line in (AUDIT/'inspection-notes.txt').read_text().splitlines())}
 assert len(ds)==len(notes)==500 and set(notes)==set(range(1,501))
 arcs=json.loads((ROOT/'docs/data/arcs.json').read_text());counts=collections.Counter(a[3] for a in arcs)
 data=json.loads((ROOT/'docs/data/careers.json').read_text()); persons=data['persons']
 rules=json.loads((AUDIT/'event-corrections.json').read_text())
 entries=[];total_changed=0
 for d in ds:
  n=d['rank'];changed=[]
  for e in d['events']:
   fixed=correct_event(e);key,node=project(fixed)
   before=e.get('map'); old=(e.get('map_key'),before.get('lat') if before else None,before.get('lon') if before else None)
   new=(key,node.get('lat') if node else None,node.get('lon') if node else None)
   newrules=sorted(set(fixed.get('historical_corrections',[]))-set(e.get('historical_corrections',[])))
   if newrules or old!=new:
    changed.append({'year_before':e.get('year_start'),'year_after':fixed.get('year_start'),
      'role':e.get('position'),'raw_place':e.get('place_raw'),
      'before':before.get('label') if before else None,'after':node.get('label') if node else None,
      'rules':newrules,'reason':fixed.get('location_note') or 'Named locality retained instead of jurisdiction seat; route also requires unambiguous year order.'})
  total_changed+=len(changed)
  adjudication=ADJUDICATION.get(n,'')
  if n in QUARANTINED:adjudication='The primary-source transcription combines several people. This composite is withdrawn from mapped journeys and held-office assertions; the raw events remain visible. Individual careers still require reconstruction.'
  selected=[s for s in d['sources'] if any(s['bio_id']==r.get('source') or isinstance(r.get('source'),list) and s['bio_id'] in r['source'] for r in rules if r['rank']==n)]
  if not selected:selected=sorted(d['sources'],key=lambda s:len(s['text']),reverse=True)
  src=next((s for s in selected if len(s['text'])<6500),selected[0])
  row={k:d[k] for k in ['rank','person_id','name','moves_before','corpus']}
  row.update(moves_after=counts[d['person_id']],tags=notes[n][0],inspection_note=notes[n][1],adjudication=adjudication,
    status='Composite withdrawn; reconstruction open' if n in QUARANTINED else 'Mapping inspected; corrections applied, questions remain' if changed else 'Mapping inspected; source questions remain',
    changes=changed,source_count=len(d['sources']),source=src,
    source_scope='Geographic sequence inspected. Selected source clauses adjudicated; not every attestation or life event independently verified.')
  entries.append(row)
  if d['person_id'] in persons:
   persons[d['person_id']]['review']={'rank':n,'withdrawn':n in QUARANTINED}
 meta={'date':'2026-10-07','cohort':500,'moves_before':sum(d['moves_before'] for d in ds),
  'moves_after':sum(counts[d['person_id']] for d in ds),'event_rules':len(rules),'changed_events':total_changed,
  'composites_withdrawn':len(QUARANTINED),'sources_available':sum(len(d['sources']) for d in ds),
  'method':'Fixed pre-review ranking by distinct directed corridors in the published atlas, descending; ties alphabetical, then person ID. All 500 geographic event sequences inspected in rank order. Selected primary sources checked for suspected errors. Counts are inferred corridors, not verified physical journeys. Ambiguous multi-place years break routes; unresolved identities and unaccepted appointments cannot generate moves.',
  'limitations':'Mapping inspection is complete; source adjudication is not. Working notes are hypotheses where not explicitly adjudicated. Duplicate people, inherited locations, joint duties, event dates and institutional scope still have open questions. Automated inception dates were not accepted wholesale: for example, the Leeward QID was valid but its display label was wrong.'}
 (OUT/'review.json').write_text(json.dumps({'meta':meta,'careers':entries},ensure_ascii=False,separators=(',',':'))+'\n')
 (AUDIT/'review-summary.json').write_text(json.dumps(meta,ensure_ascii=False,indent=2)+'\n')
 with (OUT/'review.csv').open('w') as f:
  w=csv.writer(f,lineterminator='\n');w.writerow(['rank','person_id','name','corridors_before','corridors_after','status','inspection_note','adjudication'])
  for d in entries:w.writerow([d[k] for k in ['rank','person_id','name','moves_before','moves_after','status','inspection_note','adjudication']])
 (ROOT/'docs/data/careers.json').write_text(json.dumps(data,ensure_ascii=False,separators=(',',':')))
 print(json.dumps(meta,indent=2))
if __name__=='__main__':main()
