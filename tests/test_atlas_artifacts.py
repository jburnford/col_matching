"""Corpus-wide assertions on the rebuilt public artifacts."""
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class AtlasArtifactTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = json.loads((ROOT / 'docs/data/careers.json').read_text())
        cls.places = json.loads((ROOT / 'docs/data/places.json').read_text())
        cls.arcs = json.loads((ROOT / 'docs/data/arcs.json').read_text())

    def test_all_stints_have_coordinates_and_valid_union_dates(self):
        for pid, person in self.data['persons'].items():
            for key, start, end, role, acting in person['st']:
                self.assertIn(key, self.places, pid)
                node = self.places[key]
                if node['entity_qid'] == 'Q193619': self.assertGreaterEqual(start, 1910, pid)
                if node['entity_qid'] == 'Q1643555' and start < 1970:
                    self.assertEqual(node['capital_qid'], 'Q108223', pid)
                if node['entity_qid'] == 'Q129286' and start < 1911:
                    self.assertEqual(node['capital_qid'], 'Q1348', pid)

    def test_arcs_and_tours_reference_existing_points(self):
        for yr, a, b, pid, corpus in self.arcs:
            self.assertIn(a, self.places)
            self.assertIn(b, self.places)
            self.assertIn(pid, self.data['persons'])
        for tour in json.loads((ROOT / 'docs/data/tours.json').read_text()):
            for step in tour['steps']:
                if step.get('qid'): self.assertIn(step['qid'], self.places)

    def test_wodehouse_both_records(self):
        for pid in ('kgp_col1878-p447b3', 'kgp_iol1889_jan-c2242376'):
            st = self.data['persons'][pid]['st']
            by_year = lambda y: {self.places[s[0]]['entity_qid'] for s in st if s[1] == y}
            self.assertEqual(by_year(1851), {'Q1643555'})
            self.assertEqual(by_year(1858), {'Q717'})
            self.assertEqual(by_year(1861), {'Q370736'})

    def test_brewster_defeat_retained_without_tenure(self):
        p = self.data['persons']['kgp_col1918-p696b8']
        self.assertFalse(any(s[1] == 1912 for s in p['st']))
        self.assertTrue(any(u[0] == 1912 and 'defeat' in u[4] for u in p['un']))
        self.assertTrue(any(s[1] == 1916 for s in p['st']))


if __name__ == '__main__': unittest.main()
