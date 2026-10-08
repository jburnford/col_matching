"""Regressions exposed by manually inspecting the frozen top-500 cohort."""
import json
from pathlib import Path
import unittest
from historical_geography import correct_event
from atlas_geography import project, ordered_arcs
from reviewed_careers import NON_HELD
ROOT=Path(__file__).resolve().parents[1]
AUDIT=ROOT/'research/top-500-careers-2026-10-07'

class Top500Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.ds=json.loads((AUDIT/'dossiers.json').read_text())
    def events(self,n):return self.ds[n-1]['events']
    def test_cohort_and_inspection_complete(self):
        self.assertEqual(len(self.ds),500)
        self.assertEqual(sum(d['moves_before'] for d in self.ds),4251)
        self.assertEqual([d['rank'] for d in self.ds],list(range(1,501)))
        notes=(AUDIT/'inspection-notes.txt').read_text().splitlines()
        self.assertEqual([int(n.split('|',1)[0]) for n in notes],list(range(1,501)))
        self.assertTrue(all(d['sources'] for d in self.ds))
    def test_all_manifest_fixes_match_and_are_idempotent(self):
        es=[e for d in self.ds for e in d['events']]
        for rule in json.loads((AUDIT/'event-corrections.json').read_text()):
            matches=[e for e in es if e['person_id']==rule['person_id'] and all(e.get(k)==v for k,v in rule['match'].items())]
            self.assertTrue(matches,rule['id'])
            for e in matches:
                fixed=correct_event(e)
                self.assertIn(rule['id'],fixed['historical_corrections'])
                self.assertEqual(correct_event(fixed),fixed,rule['id'])
    def test_appointments_not_taken_up(self):
        for n,y,raw in [(1,1865,'Japan'),(1,1870,'Brussels'),(13,1886,'Natal'),(374,1893,'India'),(457,1915,'Ken.')]:
            e=next(e for e in self.events(n) if e['year_start']==y and e['place_raw']==raw)
            fixed=correct_event(e)
            self.assertEqual(fixed['event_kind'],'appointment_not_taken_up')
            self.assertIsNone(fixed['role_id'])
            self.assertEqual(project(fixed),(None,None))
    def test_homonyms_stay_on_correct_continent(self):
        for n,raw,south in [(3,'Prince Albert',True),(295,'Prince Albert',True),(205,'Belfast',True),
                            (400,'Aberdeen',True),(499,'Alexandria',True),(127,'Rewa',True),(134,'Rewa',True),
                            (328,"St. John's",False)]:
            e=next(e for e in self.events(n) if e['place_raw']==raw)
            _,p=project(e);self.assertIsNotNone(p)
            self.assertEqual(p['lat']<0,south,(n,p))
        for n in [393,419,463]:
            e=next(e for e in self.events(n) if e['place_raw']=='W.I.')
            self.assertNotEqual(correct_event(e)['place_qid'],'Q920396')
    def test_named_city_not_colony_capital(self):
        _,p=project({'year_start':1925,'place_qid':'Q1348','place_label':'Calcutta','colony_qid':'Q129286'})
        self.assertEqual(p['entity_qid'],'Q1348');self.assertIsNone(p['capital_qid'])
        _,p=project({'year_start':1912,'place_qid':'Q1930','place_label':'Ottawa','colony_qid':'Q1904'})
        self.assertEqual(p['entity_qid'],'Q1930')
    def test_ambiguous_year_preserves_explicit_alternatives(self):
        nodes={q:{'entity_qid':q,'lat':i,'lon':i} for i,q in enumerate('abcd')}
        rows=[(1900,0,'a'),(1901,1,'b'),(1901,2,'c'),(1902,3,'d')]
        arcs=list(ordered_arcs('p',rows,nodes))
        self.assertEqual({(a['from'],a['to']) for a in arcs},{('a','b'),('a','c'),('b','c'),('b','d'),('c','d')})
        self.assertTrue(all(a.get('uncertain') for a in arcs))
        self.assertEqual(len(list(ordered_arcs('p',[(1900,0,'a'),(1901,1,'b'),(1901,2,'b')],nodes))),1)
    def test_reviewed_order_restores_same_year_routes(self):
        nodes={q:{'entity_qid':q,'lat':i,'lon':i} for i,q in enumerate('abcd')}
        rows=[(1900,0,'a',None),(1901,1,'c',20),(1901,2,'b',10),(1902,3,'d',None)]
        self.assertEqual([(a['from'],a['to']) for a in ordered_arcs('p',rows,nodes)], [('a','b'),('b','c'),('c','d')])
        # A tie or missing order must never manufacture a solid ordered route.
        for last in [10,None]:
            rows=[(1900,0,'a',None),(1901,1,'b',10),(1901,2,'c',last),(1902,3,'d',None)]
            arcs=list(ordered_arcs('p',rows,nodes))
            self.assertTrue(arcs)
            self.assertTrue(all(a.get('uncertain') for a in arcs))
    def test_unlocated_events_preserve_endpoints_without_assigning_a_place(self):
        nodes={q:{'entity_qid':q,'lat':i,'lon':i} for i,q in enumerate('abc')}
        rows=[(1900,0,'a'),(1901,1,None),(1902,2,'b'),(1903,3,'c')]
        arcs=list(ordered_arcs('p',rows,nodes))
        self.assertEqual([(a['from'],a['to']) for a in arcs],[('a','b'),('b','c')])
        self.assertIn('unlocated',arcs[0]['uncertain'])
        self.assertNotIn('uncertain',arcs[1])
    def test_cameron_conference_does_not_interrupt_temporary_appointments(self):
        rows=[];nodes={}
        for e in self.events(20):
            r=correct_event(e);key,node=project(r)
            if node:nodes[key]=node
            if r.get('event_kind') in NON_HELD or r.get('route_neutral') or r.get('appointment_map_excluded'):continue
            rows.append((r['year_start'],r['seq'],key,r.get('route_order')))
        arcs=list(ordered_arcs('cameron',rows,nodes))
        incoming=[a for a in arcs if a['to']=='Q3557236']
        self.assertEqual({a['from'] for a in incoming},{'Q2660774@Q41547'})
        self.assertTrue(all(a['yr']==1914 and not a.get('uncertain') for a in incoming))
    def test_ford_complete_reviewed_sequence(self):
        rows=[];nodes={}
        for e in self.events(1):
            r=correct_event(e);key,node=project(r)
            if node:nodes[key]=node
            if r.get('event_kind') in NON_HELD or r.get('route_neutral'):continue
            rows.append((r['year_start'],r['seq'],key,r.get('route_order')))
        arcs=list(ordered_arcs('ford',rows,nodes))
        self.assertEqual(len(arcs),22)
        pairs={(nodes[a['from']]['entity_qid'],nodes[a['to']]['entity_qid']) for a in arcs}
        for pair in [('Q1726','Q90'),('Q1022','Q1040'),('Q90','Q2984260'),('Q2984260','Q29'),('Q2807','Q16869')]:
            self.assertIn(pair,pairs)
        self.assertFalse(any('Q17' in pair for pair in pairs))
    def test_composites_cannot_make_routes_or_held_offices(self):
        for n in [12,16,30,52,57,118,160]:
            for e in self.events(n):
                f=correct_event(e)
                self.assertEqual(f['event_kind'],'attribution_unresolved')
                self.assertIsNone(f['role_id']);self.assertEqual(project(f),(None,None))
    def test_source_year_fixes(self):
        for e in self.events(233):
            if e['year_start'] in [1835,1837,1839]:self.assertEqual(correct_event(e)['year_start'],e['year_start']+50)
        for e in self.events(85):
            if e['year_start']==1849:self.assertEqual(project(e),(None,None))
    def test_singapore_and_malayan_jurisdictions(self):
        f=correct_event({'year_start':1900,'place_qid':'Q4373718','colony_qid':'Q4373718'})
        self.assertEqual(f['place_qid'],'Q1054746');self.assertEqual(f['colony_qid'],'Q376178')
        for q in ['Q183032','Q185944','Q188947','Q189701']:
            self.assertIsNone(correct_event({'year_start':1920,'place_qid':q,'colony_qid':'Q1400154'})['colony_qid'])

if __name__=='__main__':unittest.main()
