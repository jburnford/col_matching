import unittest
import contextlib
import io
import json
from pathlib import Path
import tempfile
from unittest.mock import patch

from appointment_scope import classify_for_appointment_map
from historical_geography import correct_event, location
from atlas_geography import project


class AppointmentScopeTests(unittest.TestCase):
    def test_attendance_and_travel_are_written_events(self):
        for title in (
            'representative of St. Lucia and chairman of West Indian delegates at reciprocity conference',
            'delegate to Imperial Conference',
            'attended conf. at Ottawa',
            'acted as vice-president of the London South African conference',
            'visited Canada',
            'official tour of the West Indies',
            'accompanied the governor on a visit to Canada',
        ):
            with self.subTest(title=title):
                original = dict(position=title, year_start=1912, place_raw='Ottawa',
                                place_qid='Q1930', place_label='Ottawa', role_id='recorded-role')
                fixed = correct_event(original)
                self.assertTrue(fixed['appointment_map_excluded'])
                self.assertEqual({k: fixed[k] for k in original}, original)
                self.assertEqual(location(fixed), ('Q1930', 'Ottawa'))
                self.assertEqual(project(fixed), (None, None))
                self.assertEqual(correct_event(fixed), fixed)

    def test_temporary_offices_and_special_duties_remain(self):
        for title in (
            'acting governor', 'temporary colonial secretary',
            'visiting justice, Freetown Gaol', 'visiting surgeon',
            'seconded to conference staff', 'attached to the conference delegation',
            'on special duty with the delegation to the conference',
            'secretary to the conference', 'member of conference secretariat',
            'technical adviser to delegates at the conference',
            'appointed as assistant secretary to the conference',
            'loans commissioner, representative at conference',
            'employed on a special mission', 'member of a commission of inquiry',
            'confirmed as commissioner', 'commander, HMS Tourmaline',
            'visited China on a special mission',
            'visited Nigeria at request of C.O. to rept. on stock problems',
            'visited S. Nigeria on special service',
            'visited and reported on Cyprus government railway',
            'tour of inspection principal English prisons',
            'attd. Br. del., university postal union congress',
            'representative of government of Canada to confer with H.M. government',
        ):
            with self.subTest(title=title):
                fixed = correct_event(dict(position=title, year_start=1912,
                                           colony_qid='Q41547', is_acting=True))
                self.assertFalse(fixed.get('appointment_map_excluded'))
                self.assertTrue(fixed['is_acting'])
                self.assertIsNotNone(project(fixed)[0])

    def test_changed_classification_clears_stale_flags(self):
        row = dict(position='acting governor', appointment_map_excluded=True,
                   appointment_map_note='previous classification')
        classify_for_appointment_map(row)
        self.assertNotIn('appointment_map_excluded', row)
        self.assertNotIn('appointment_map_note', row)

    def test_graph_fixup_only_changes_map_scope_and_is_reversible(self):
        import kg_apply_historical_fixups as fixups
        with tempfile.TemporaryDirectory() as directory:
            root=Path(directory)
            for corpus in ('kg','iol'):
                folder=root/f'data/{corpus}/graph_stage3'
                folder.mkdir(parents=True)
                event=dict(person_id='example',seq=1,position='delegate to conference',grounded=True)
                fact=dict(person_id='example',seq=1,position_raw='delegate to conference')
                for name,row in [('career_events',event),('career_facts',fact),('role_edges',fact)]:
                    (folder/f'{name}.jsonl').write_text(json.dumps(row)+'\n')
            with patch.object(fixups,'ROOT',root),contextlib.redirect_stdout(io.StringIO()):
                fixups.main()
                snapshot={p:p.read_text() for p in root.rglob('*.jsonl')}
                fixups.main()
                self.assertEqual(snapshot,{p:p.read_text() for p in snapshot})
                for corpus in ('kg','iol'):
                    folder=root/f'data/{corpus}/graph_stage3'
                    fixed=json.loads((folder/'career_facts.jsonl').read_text())
                    self.assertTrue(fixed.pop('appointment_map_excluded'))
                    fixed.pop('appointment_map_note')
                    self.assertEqual(fixed,fact)
                    self.assertEqual(json.loads((folder/'role_edges.jsonl').read_text()),fact)
                    path=folder/'career_events.jsonl'
                    changed=json.loads(path.read_text())
                    changed['position']='acting governor'
                    path.write_text(json.dumps(changed)+'\n')
                fixups.main()
                for p in root.rglob('*.jsonl'):
                    self.assertNotIn('appointment_map_excluded',json.loads(p.read_text()))


if __name__ == '__main__':
    unittest.main()
