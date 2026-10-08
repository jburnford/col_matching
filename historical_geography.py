"""Reviewed historical corrections shared by the graph and atlas builders.

Raw source strings are retained. A removed jurisdiction is NOT replaced with a
neighbouring appointment. Sources and review limits: research/geography-2026-10-07/.
"""
from copy import deepcopy
import re
from reviewed_careers import apply_review, NON_HELD

WODEHOUSE = {'kgp_col1878-p447b3', 'kgp_iol1889_jan-c2242376'}


def correct_event(original):
    r = deepcopy(original)
    pid, y = r.get('person_id'), r.get('year_start')
    pos = (r.get('position') or r.get('position_raw') or '').lower()
    reasons = []

    def locate(q, label, colony=None, colony_label=None):
        r.update(place_qid=q, place_label=label, colony_qid=colony,
                 colony_label=colony_label, grounded=bool(q))

    if pid in WODEHOUSE:
        if y == 1858 and 'mission' in pos:
            locate('Q717', 'Venezuela')
            r.update(role_id=None, role_label='special mission to Venezuela')
            reasons.append('wodehouse-venezuela')
        elif y == 1851 and 'superintendent' in pos:
            locate('Q1643555', 'British Honduras', 'Q1643555', 'British Honduras')
            reasons.append('wodehouse-honduras')
        elif y == 1861 and 'high commissioner' in pos:
            locate('Q370736', 'Cape Colony', 'Q370736', 'Cape Colony')
            reasons.append('wodehouse-high-commissioner')
        elif y == 1840 and 'judge' in pos:
            locate('Q203197', 'Kandy', 'Q918153', 'Ceylon')
            reasons.append('wodehouse-kandy')
        elif y == 1843 and 'western province' in pos:
            locate('Q918153', 'Ceylon', 'Q918153', 'Ceylon')
            reasons.append('wodehouse-western-province')

    # A town can keep its grounded point even when the jurisdiction is invalid.
    # Bare "South Africa" cannot tell us which pre-Union jurisdiction was meant.
    if y and (y < 1910 or y > 1961):
        bad = False
        if r.get('colony_qid') == 'Q193619':
            r.update(colony_qid=None, colony_label=None)
            bad = True
        if r.get('place_qid') == 'Q193619':
            r.update(place_qid=None, place_label=None, grounded=False)
            bad = True
        if bad:
            reasons.append('union-outside-1910-1961')
            r['location_note'] = ('Union of South Africa is invalid for this date; '
                                  + ('named place retained, jurisdiction unresolved.' if r.get('place_qid')
                                     else 'historical jurisdiction unresolved.'))

    if pid == 'kgp_col1918-p696b8' and y == 1912 and ('victoria' in pos or 'defeated' in pos):
        r.update(event_kind='electoral_defeat', year_end=None, role_id=None,
                 role_label='defeated by Sir Richard McBride, in Victoria')
        reasons.append('brewster-1912-defeat')

    normalized = re.sub(r'[^a-z ]', '', pos).strip()
    if r.get('org_type') == 'civil' and normalized in (
            'defeated', 'defeated at general elec', 'defeated at g e',
            'defeated at ge', 'defeated general el'):
        r.update(event_kind='electoral_defeat', year_end=None, role_id=None,
                 role_label=r.get('position') or r.get('position_raw'))
        reasons.append('explicit-electoral-defeat')

    if reasons:
        r['historical_corrections'] = sorted(set(r.get('historical_corrections', [])) | set(reasons))
    return apply_review(r)


def location(r):
    """Prefer the explicit grounded place, then the recorded jurisdiction."""
    if r.get('event_kind') in NON_HELD:
        return None, None
    q = r.get('place_qid') or r.get('colony_qid')
    label = r.get('place_label') if r.get('place_qid') else r.get('colony_label')
    return q, label
