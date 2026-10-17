"""Reviewed historical corrections shared by the graph and atlas builders.

Raw source strings are retained. A removed jurisdiction is NOT replaced with a
neighbouring appointment. Sources and review limits: research/geography-2026-10-07/.
"""
from copy import deepcopy
import re
from reviewed_careers import apply_review, NON_HELD
from appointment_scope import classify_for_appointment_map

WODEHOUSE = {'kgp_col1878-p447b3', 'kgp_iol1889_jan-c2242376'}

# Colony of a named place before Confederation, where the graph said Canada.
# 'canadas' = The Canadas / Province of Canada by year. PEI joined in 1873; the
# graph's convention for the island colony is Q1978. Mackenzie River lay in
# HBC territory, not a colony: left unresolved.
PRE_CONFEDERATION_COLONY = {
    'Q202973': 'canadas',                                   # Kingston
    'Q2127': ('Q1978', 'Prince Edward Island (Province)'),  # Charlottetown
    'Q2957125': ('Q918861', 'Colony of British Columbia'),  # Lytton
}


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

    # These federal appointments inherited "province of Canada" from an
    # earlier source clause. Retain the raw wording, correct the jurisdiction.
    # Senate and ministry evidence: research/canada-geography-2026-10-08.json.
    if ((pid == 'kgp_col1879-p423b19' and y in (1871, 1872) and 'clerk' in pos) or
            (pid == 'kgp_col1905-p661b19' and y == 1867 and 'inland rev' in pos)):
        locate('Q16', 'Canada', 'Q16', 'Canada')
        reasons.append('canada-federal-office-after-confederation')

    # Walcott's 1840 commissions sat in London; "Canada" was inherited from
    # the preceding clause. Source: col1879-p464b17.
    if pid == 'kgp_col1879-p464b17' and y == 1840 and ('emigration' in pos or 'coloniz' in pos):
        locate('Q84', 'London', 'Q84', 'United Kingdom (metropole)')
        reasons.append('walcott-london-commissions')

    # "New York" after the Revolution is the city (consulates), not the
    # colonial Province of New York (Q769668, 1664-1783).
    if r.get('place_qid') == 'Q769668' and (not y or y > 1783):
        locate('Q60', 'New York City', 'Q30', 'United States')
        reasons.append('new-york-city-not-province')

    # D.W.W.I. = Development and Welfare Organisation, West Indies (1940-58),
    # headquartered in Barbados; it was grounded to the Danish West Indies.
    # Source: research/geography-2026-10-16-fable-review.json.
    if re.sub(r'[^a-z]', '', (r.get('place_raw') or '').lower()) == 'dwwi':
        locate(None, None, 'Q63973349', 'Barbados Colony')
        r['location_note'] = ('Development and Welfare Organisation, West Indies (HQ Barbados); '
                              'office, not a place.')
        reasons.append('development-welfare-west-indies')

    # Modern Canada (Q16) begins 1 July 1867. Before that a printed "Canada"
    # is the Canadas (Upper + Lower, 1791-1840) or the Province of Canada
    # (Act of Union in force Feb. 1841). Evidence: research/canada-geography-2026-10-16.json.
    if y and y < 1867 and 'Q16' in (r.get('place_qid'), r.get('colony_qid')):
        period = ('Q7721124', 'The Canadas') if y <= 1840 else ('Q1121436', 'Province of Canada')
        if r.get('place_qid') == 'Q16':
            locate(*period, *period)
        else:
            colony = PRE_CONFEDERATION_COLONY.get(r.get('place_qid'), 'unresolved')
            colony = period if colony == 'canadas' else colony
            if colony == 'unresolved':
                r.update(colony_qid=None, colony_label=None)
                r['location_note'] = 'Canada (1867) is invalid for this date; named place retained, colony unresolved.'
            else:
                r.update(colony_qid=colony[0], colony_label=colony[1])
        reasons.append('canada-before-confederation')

    normalized = re.sub(r'[^a-z ]', '', pos).strip()
    if r.get('org_type') == 'civil' and normalized in (
            'defeated', 'defeated at general elec', 'defeated at g e',
            'defeated at ge', 'defeated general el'):
        r.update(event_kind='electoral_defeat', year_end=None, role_id=None,
                 role_label=r.get('position') or r.get('position_raw'))
        reasons.append('explicit-electoral-defeat')

    if reasons:
        r['historical_corrections'] = sorted(set(r.get('historical_corrections', [])) | set(reasons))
    return classify_for_appointment_map(apply_review(r))


def location(r):
    """Prefer the explicit grounded place, then the recorded jurisdiction."""
    if r.get('event_kind') in NON_HELD:
        return None, None
    q = r.get('place_qid') or r.get('colony_qid')
    label = r.get('place_label') if r.get('place_qid') else r.get('colony_label')
    return q, label
