import json
from pathlib import Path
import unittest

from historical_geography import correct_event
from atlas_geography import project

ROOT=Path(__file__).resolve().parents[1]


class PrinceAlbertTests(unittest.TestCase):
    def test_every_reviewed_event_preserves_source_and_is_idempotent(self):
        rules=json.loads((ROOT/'research/prince-albert-2026-10-08/event-corrections.json').read_text())
        for rule in rules:
            original=dict(person_id=rule['person_id'],**rule['match'])
            fixed=correct_event(original)
            self.assertEqual({k:fixed[k] for k in original},original)
            self.assertEqual(correct_event(fixed),fixed,rule['id'])
            self.assertIn(rule['id'],fixed['historical_corrections'])

    def test_explicit_cape_context_and_canadian_negative_control(self):
        for raw in ('Prince Albert, Cape Colony','Prince Albert division, Cape Colony'):
            row=dict(person_id='future-record',place_raw=raw,place_qid='Q671431',colony_qid='Q1989',year_start=1881,is_acting=True)
            fixed=correct_event(row)
            self.assertEqual(fixed['place_qid'],'Q1533623')
            self.assertTrue(fixed['is_acting'])
            self.assertLess(project(fixed)[1]['lat'],0)
        canadian=dict(person_id='canadian-official',place_raw='Prince Albert',place_qid='Q671431',place_label='Prince Albert',colony_qid='Q1989',year_start=1910)
        self.assertEqual(correct_event(canadian),canadian)
        self.assertGreater(project(canadian)[1]['lat'],50)

    def test_published_careers_have_no_saskatchewan_detours(self):
        data=json.loads((ROOT/'docs/data/careers.json').read_text())['persons']
        places=json.loads((ROOT/'docs/data/places.json').read_text())
        expected={'kgp_col1897-p478b29_s1':1870,'kgp_col1897-p481b20':1860,
                  'kgp_col1921-p816b11':1891,'kgp_col1898-p520b7':1891,
                  'kgp_col1897-p546b17':1883,'kgp_col1918-p827b6':1881}
        for pid,y in expected.items():
            st=data[pid]['st']
            self.assertFalse(any(places[s[0]]['entity_qid'] in {'Q671431','Q1989'} for s in st),pid)
            self.assertTrue(any(s[1]==y and places[s[0]]['entity_qid']=='Q1533623' for s in st),pid)
        fairbairn=data['kgp_col1921-p816b11']
        self.assertTrue(any(s[1]==1892 and places[s[0]]['entity_qid']=='Q5465' for s in fairbairn['st']))
        self.assertFalse(any(s[1]>=1892 and places[s[0]]['entity_qid']=='Q1533623' for s in fairbairn['st']))
        self.assertTrue(any(u[0]==1901 and 'honour' in u[4] for u in fairbairn['un']))
        crosby=data['kgp_col1897-p481b20']
        self.assertTrue(any(s[1]==1869 and places[s[0]]['entity_qid']=='Q951161' for s in crosby['st']))


if __name__=='__main__':unittest.main()
