import unittest
from historical_geography import correct_event, location
from atlas_geography import project


class HistoricalGeographyTests(unittest.TestCase):
    def test_union_boundary_and_idempotence(self):
        for y in (1828, 1861, 1909):
            row = {'year_start': y, 'place_raw': 'South Africa', 'place_qid': 'Q193619', 'colony_qid': 'Q193619'}
            fixed = correct_event(row)
            self.assertEqual(location(fixed), (None, None))
            self.assertEqual(fixed['place_raw'], 'South Africa')
            self.assertEqual(correct_event(fixed), fixed)
        for y in (1910, 1961):
            self.assertEqual(correct_event({'year_start': y, 'colony_qid': 'Q193619'})['colony_qid'], 'Q193619')

    def test_town_survives_invalid_jurisdiction(self):
        row = correct_event({'year_start': 1860, 'colony_qid': 'Q193619', 'place_qid': 'Q5465', 'place_label': 'Cape Town'})
        self.assertEqual(location(row), ('Q5465', 'Cape Town'))

    def test_no_nearest_place(self):
        self.assertEqual(location({'year_start': 1858, 'place_qid': 'Q717', 'place_label': 'Venezuela'}), ('Q717', 'Venezuela'))
        self.assertEqual(location({'year_start': 1858, 'place_raw': 'somewhere'}), (None, None))

    def test_person_guard(self):
        row = {'person_id': 'other', 'year_start': 1851, 'position': 'superintendent of Honduras'}
        self.assertEqual(correct_event(row), row)

    def test_wodehouse_both_lists(self):
        for pid in ('kgp_col1878-p447b3', 'kgp_iol1889_jan-c2242376'):
            mission = correct_event({'person_id': pid, 'year_start': 1858, 'position': 'employed on a special mission'})
            self.assertEqual(location(mission), ('Q717', 'Venezuela'))
            cape = correct_event({'person_id': pid, 'year_start': 1861, 'position': 'high commissioner', 'colony_qid': 'Q193619'})
            self.assertEqual(location(cape), ('Q370736', 'Cape Colony'))

    def test_defeat_is_not_tenure(self):
        row = correct_event({'person_id': 'kgp_col1918-p696b8', 'year_start': 1912, 'year_end': 1916,
                             'position': 'legislative ass. for Victoria', 'colony_qid': 'Q1973'})
        self.assertIsNone(row['year_end'])
        self.assertIsNone(row['role_id'])
        self.assertEqual(location(row), (None, None))

    def test_seat_dates(self):
        def p(q, y): return project({'colony_qid': q, 'year_start': y})[1]
        self.assertEqual(p('Q1643555', 1851)['capital_qid'], 'Q108223')
        self.assertEqual(p('Q1643555', 1971)['capital_qid'], 'Q3043')
        self.assertEqual(p('Q129286', 1900)['capital_qid'], 'Q1348')
        self.assertEqual(p('Q129286', 1920)['capital_qid'], 'Q987')
        self.assertIsNone(p('Q129286', 1911)['capital_qid'])
        self.assertIsNone(p('Q193619', 1920)['capital_qid'])

    def test_province_of_canada_seats_and_transition_years(self):
        for y,q in ((1841,'Q202973'),(1845,'Q340'),(1850,'Q172'),
                    (1852,'Q2145'),(1856,'Q172'),(1862,'Q2145'),(1866,'Q1930')):
            node=project({'colony_qid':'Q1121436','year_start':y})[1]
            self.assertEqual(node['capital_qid'],q)
        for y in (1844,1849,1851,1855,1859,1865):
            node=project({'colony_qid':'Q1121436','year_start':y})[1]
            self.assertIsNone(node['capital_qid'])
            self.assertTrue(43 < node['lat'] < 48 and -80 < node['lon'] < -70)
            self.assertIn('schematic',node['coordinate_kind'])
        for y in (1840,1868,1871):
            self.assertEqual(project({'colony_qid':'Q1121436','year_start':y}),(None,None))

    def test_reviewed_federal_offices_keep_source_and_use_canada(self):
        for pid,y,title in (('kgp_col1879-p423b19',1871,'clerk of the senate'),
                            ('kgp_col1879-p423b19',1872,'clerk of the parliaments'),
                            ('kgp_col1905-p661b19',1867,'minister of inland rev.')):
            row=correct_event(dict(person_id=pid,year_start=y,position=title,
                                   place_raw='province of Canada',place_qid='Q1121436',colony_qid='Q1121436'))
            self.assertEqual(location(row),('Q16','Canada'))
            self.assertEqual(row['place_raw'],'province of Canada')
            self.assertEqual(project(row)[1]['capital_qid'],'Q1930')
            self.assertEqual(correct_event(row),row)

    def test_canada_before_confederation(self):
        base=dict(person_id='kgp_x',position='clerk',place_raw='Canada',place_qid='Q16',colony_qid='Q16')
        for y,q in ((1831,'Q7721124'),(1840,'Q7721124'),(1841,'Q1121436'),(1866,'Q1121436'),(1867,'Q16')):
            row=correct_event({**base,'year_start':y})
            self.assertEqual((row['place_qid'],row['colony_qid']),(q,q))
            self.assertEqual(row['place_raw'],'Canada')
            self.assertEqual(correct_event(row),row)
        node=project({**base,'year_start':1831})[1]
        self.assertEqual(node['capital_qid'],'Q2145')
        self.assertEqual(project({'colony_qid':'Q7721124','year_start':1845}),(None,None))

    def test_named_places_get_pre_confederation_colonies(self):
        def colony(q,y): return correct_event(dict(person_id='kgp_x',year_start=y,place_qid=q,colony_qid='Q16'))['colony_qid']
        self.assertEqual(colony('Q202973',1838),'Q7721124')
        self.assertEqual(colony('Q202973',1851),'Q1121436')
        self.assertEqual(colony('Q2127',1864),'Q1978')
        self.assertEqual(colony('Q2957125',1859),'Q918861')
        self.assertIsNone(colony('Q3411',1865))
        self.assertEqual(colony('Q202973',1885),'Q16')

    def test_walcott_commissions_were_in_london(self):
        row=correct_event(dict(person_id='kgp_col1879-p464b17',year_start=1840,place_raw='Canada',
                               position='secretary to H.M. colonial land and emigration commission',
                               place_qid='Q16',colony_qid='Q16'))
        self.assertEqual(location(row),('Q84','London'))

    def test_new_york_city_and_development_welfare(self):
        row=correct_event(dict(person_id='kgp_x',year_start=1862,place_raw='New York',
                               place_qid='Q769668',colony_qid='Q769668'))
        self.assertEqual((row['place_qid'],row['colony_qid']),('Q60','Q30'))
        row=correct_event(dict(person_id='kgp_x',year_start=1943,place_raw='D.W.W.I.',
                               place_qid='Q829655',colony_qid=None))
        self.assertEqual((row['place_qid'],row['colony_qid']),(None,'Q63973349'))
        self.assertEqual(correct_event(row),row)

    def test_nwmp_printed_year_error_is_uncertain_not_province(self):
        row=correct_event(dict(person_id='kgp_col1914-p840b13',year_start=1866,place_raw='Canada',
                               position='served in N.W. mounted police',place_qid='Q1121436',colony_qid='Q1121436'))
        self.assertTrue(row['date_uncertain'])
        self.assertEqual(location(row),('Q16','Canada'))
        self.assertEqual(project(row),(None,None))
        self.assertEqual(correct_event(row),row)


if __name__ == '__main__': unittest.main()
