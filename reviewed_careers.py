"""Source-adjudicated fixes from the fixed top-500 review; never guess a successor post."""
import json
import re
from functools import lru_cache
from pathlib import Path

NON_HELD = {'electoral_defeat', 'appointment_not_taken_up', 'attribution_unresolved'}

@lru_cache(maxsize=1)
def rules():
    rows = json.loads((Path(__file__).parent / 'research/top-500-careers-2026-10-07/event-corrections.json').read_text())
    out = {}
    for row in rows: out.setdefault(row['person_id'], []).append(row)
    return out


def apply_review(r):
    reasons = set(r.get('historical_corrections', []))
    for rule in rules().get(r.get('person_id'), []):
        if rule['id'] in reasons or all(r.get(k) == v for k, v in rule['match'].items()):
            r.update(rule['set'])
            r['location_note'] = rule['reason']
            reasons.add(rule['id'])
    y = r.get('year_start')
    raw = (r.get('place_raw') or '').lower().strip()
    p, c = r.get('place_qid'), r.get('colony_qid')
    def locate(q, label, cq=None, cl=None):
        r.update(place_qid=q, place_label=label, colony_qid=cq, colony_label=cl, grounded=bool(q))
    def note(code, text):
        reasons.add(code)
        if not any(s.startswith('top500-') for s in reasons): r['location_note'] = text
    if c == 'Q84' and re.search(r'\b(w\.?\s*africa|west africa)', raw):
        locate('Q4412', 'West Africa')
        note('west-africa-not-london', 'West Africa is a region, not the UK metropole; regional point only.')
    if p == 'Q4373718' or c == 'Q4373718':
        cq = 'Q4373718' if y and 1946 <= y <= 1959 else 'Q376178' if y and 1826 <= y <= 1941 else None
        locate('Q1054746', 'Singapore', cq, 'Singapore Crown Colony' if cq == 'Q4373718' else 'Straits Settlements' if cq else None)
        note('singapore-dated-jurisdiction', 'Singapore locality retained; separate Crown Colony began in 1946. Wartime/transition jurisdiction is not inferred.')
    # These states were never members of the Federated Malay States.
    if c == 'Q1400154' and (p in {'Q183032','Q185944','Q188947','Q189701','Q231318'} or
            re.search(r'johor|kedah|kelantan|trengganu|terengganu|batu pahat|b\. pahat|muar|kukup|kluang|kota bharu|k\. bahru', raw)):
        r.update(colony_qid=None, colony_label=None)
        if p == c: r.update(place_qid=None, place_label=None, grounded=False)
        note('not-federated-malay-state', 'Named state/locality was not part of the Federated Malay States; invalid jurisdiction withdrawn.')
    if c == 'Q1400154' and re.search(r'^(alor gajah|jasin|dindings)$',raw):
        r.update(colony_qid=None, colony_label=None)
        if p == c:r.update(place_qid=None, place_label=None, grounded=False)
        note('straits-district-not-fms', 'Straits settlement district incorrectly assigned to Federated Malay States; named locality retained where grounded.')
    if y and (y < 1895 or y > 1946) and r.get('colony_qid') == 'Q1400154':
        r.update(colony_qid=None, colony_label=None)
        if r.get('place_qid') == 'Q1400154':r.update(place_qid=None, place_label=None, grounded=False)
        note('fms-outside-period', 'Federated Malay States is invalid for this date; named locality retained where grounded.')
    # Correct mislabelled QIDs, rather than treating every bad label as a bad entity.
    for field in ('place', 'colony'):
        q = r.get(field+'_qid')
        label = {'Q1796551':'British Leeward Islands','Q1772596':'Madras Presidency',
                 'Q1187978':'Transvaal Colony','Q796':'Iraq (geographic reference)'}.get(q)
        if label and r.get(field+'_label') != label:
            r[field+'_label'] = label
            note('reviewed-entity-label', 'Entity label corrected; geographic extent and legal status still require the event date.')
    # Specific cities in Mesopotamia and Jerusalem must not inherit later states.
    if c == 'Q796':
        r.update(colony_qid=None,colony_label=None)
        if raw in {'turkish arabia'}:
            r.update(place_qid=None,place_label=None,grounded=False)
        elif p == 'Q796' and raw in {'mesopotamia','mespot.'}:locate('Q11767','Mesopotamia')
        note('iraq-geographic-not-mandate', 'Mandatory Iraq label removed; retain the explicit town or geographic region, not an anachronistic government.')
    if p == 'Q1218' and c == 'Q801' and y and y < 1948:
        r.update(colony_qid=None,colony_label=None)
        note('jerusalem-before-israel', 'Jerusalem retained as a city; State of Israel is invalid before 1948.')
    if (p == 'Q109039320' or c == 'Q109039320') and y and y < 1975:
        r.update(colony_qid=None,colony_label=None)
        if p == 'Q109039320':r.update(place_qid=None,place_label=None,grounded=False)
        note('ellice-before-separate-colony', 'The separate Ellice colony did not exist at this date; raw island name retained, legal entity withdrawn.')
    # Date-limited legal forms identified in the review. Preserve towns, never
    # move a person to the capital of a successor state by inference.
    bounds={'Q1187978':(1902,1910),'Q370736':(1806,1910),'Q1301901':(1843,1910),
            'Q17513379':(1912,1947),'Q7522091':(1936,1947),'Q4126447':(1905,1912)}
    for field in ('colony','place'):
        q=r.get(field+'_qid')
        if y and q in bounds and not bounds[q][0] <= y <= bounds[q][1]:
            r[field+'_qid']=None;r[field+'_label']=None
            if field=='place':r['grounded']=False
            note('reviewed-jurisdiction-outside-period','This legal jurisdiction is invalid for the event date; named town retained where grounded, otherwise unresolved.')
    if reasons:r['historical_corrections']=sorted(reasons)
    return r
