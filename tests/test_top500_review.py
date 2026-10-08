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
    def test_ambiguous_year_breaks_route(self):
        nodes={q:{'entity_qid':q,'lat':i,'lon':i} for i,q in enumerate('abcd')}
        rows=[(1900,0,'a'),(1901,1,'b'),(1901,2,'c'),(1902,3,'d')]
        self.assertEqual(list(ordered_arcs('p',rows,nodes)),[])
        self.assertEqual(len(list(ordered_arcs('p',[(1900,0,'a'),(1901,1,'b'),(1901,2,'b')],nodes))),1)
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
