"""Date-aware, offline atlas plotting. A map point is not an asserted workplace.

Jurisdictions use a dated capital where evidence supports one; explicit places
without a jurisdiction use their own coordinate. Ambiguous capitals use a
regional point, never the arbitrary first P36 value.
"""
import json
from functools import lru_cache
from pathlib import Path
from historical_geography import correct_event, location
from reviewed_careers import NON_HELD
from improve_place_coords import SEATS

ROOT = Path(__file__).resolve().parent


@lru_cache(maxsize=1)
def evidence():
    return json.loads((ROOT / 'research/geography-2026-10-07/wikidata.json').read_text())


def value(s):
    return s.get('mainsnak', {}).get('datavalue', {}).get('value')


def year(v):
    try: return int(v['time'][:5]) if v.get('precision', 0) >= 9 else None
    except (KeyError, TypeError, ValueError): return None


def point(q):
    # Reviewed schematic point inside the historical province, NOT a workplace
    # or centroid. Wikidata's 60 N, 100 W falls outside its territory.
    # Evidence and capital chronology: research/canada-geography-2026-10-08.json.
    if q == 'Q1121436': return [46.0, -76.0]
    for s in evidence().get(q, {}).get('claims', {}).get('P625', []):
        v = value(s)
        if v and s.get('rank') != 'deprecated' and v.get('globe', '').endswith('/Q2'):
            return [round(v['latitude'], 5), round(v['longitude'], 5)]


def cap_year(s, prop):
    dates = [year(x.get('datavalue', {}).get('value')) for x in s.get('qualifiers', {}).get(prop, [])]
    return next((x for x in dates if x is not None), None)


def records(corpus):
    gd = ROOT / f'data/{corpus}/graph_stage3'
    # Source place strings and event types must survive the denormalised overlay.
    spine = {}
    for line in (gd / 'career_events.jsonl').open():
        r = json.loads(line)
        spine[(r['person_id'], r['seq'])] = r
    for line in (gd / 'career_facts.jsonl').open():
        fact = json.loads(line)
        event = spine.get((fact['person_id'], fact['seq']), {})
        merged = {**event, **fact}
        yield correct_event(merged)


def project(r):
    r = correct_event(r)
    if r.get('appointment_map_excluded'): return None, None
    q, label = location(r)
    y = r.get('year_start')
    if not q or not y or r.get('date_uncertain'): return None, None
    e = evidence().get(q, {})
    label = label or e.get('label') or q
    label = {'Q891827': 'Bombay Presidency', 'Q817165': 'Bengal Presidency'}.get(q, label)
    seat, coords, cap = '', None, None
    mode = 'regional point'
    is_jurisdiction = q == r.get('colony_qid')
    explicit = bool(r.get('place_qid') and r.get('place_qid') != r.get('colony_qid'))
    if explicit:
        coords = point(q)
        if not coords: return None, None
        mode, seat = 'named place (approximate)', label
    # Direct historical evidence supersedes inconsistent P36 dates (1971 in WD).
    if explicit:
        pass
    elif q == 'Q1643555':
        cap = 'Q108223' if y < 1970 else 'Q3043'
    elif q == 'Q129286':
        if y <= 1910: cap = 'Q1348'
        elif y >= 1912: cap = 'Q987'
        else: mode = 'capital changed in 1911; regional point'
        # Avoid claiming the Raj existed before Crown rule.
        label = 'India (Company period)' if y < 1858 else ('India' if y > 1947 else 'British Raj')
    elif q == 'Q1121436' and is_jurisdiction:
        if not 1841 <= y <= 1867: return None, None
        # Offices moved within these years; a year-only event cannot identify
        # which seat was occupied. Legislative sessions can start later than
        # the actual government move (notably Ottawa in 1865/66).
        if y in (1844, 1849, 1851, 1855, 1859, 1865):
            mode = 'capital changed during year; schematic regional point'
        elif y <= 1843: cap = 'Q202973'
        elif y <= 1848: cap = 'Q340'
        elif y <= 1850: cap = 'Q172'
        elif y <= 1854: cap = 'Q2145'
        elif y <= 1858: cap = 'Q172'
        elif y <= 1864: cap = 'Q2145'
        else: cap = 'Q1930'
    elif is_jurisdiction:
        caps = []
        for s in e.get('claims', {}).get('P36', []):
            v = value(s)
            if not v or s.get('rank') == 'deprecated': continue
            start, end = cap_year(s, 'P580'), cap_year(s, 'P582')
            if (start is None or y >= start) and (end is None or y <= end):
                caps.append(v['id'])
        caps = sorted(set(caps))
        if len(caps) == 1: cap = caps[0]
        elif len(caps) > 1: mode = 'multiple capitals; regional point'
        elif q in SEATS and not e.get('claims', {}).get('P36'):
            coords, seat = SEATS[q]
            mode = 'administrative seat (approximate)'
    if cap:
        coords = point(cap)
        city = evidence().get(cap, {})
        founded = [year(value(s)) for s in city.get('claims', {}).get('P571', []) if s.get('rank') != 'deprecated']
        founded = [v for v in founded if v is not None]
        if founded and y < min(founded):
            coords, cap = None, None
            mode = 'capital did not yet exist; regional point'
        elif coords:
            seat = {'Q1348': 'Calcutta', 'Q1156': 'Bombay', 'Q1354': 'Dacca'}.get(cap, city.get('label', cap))
            mode = 'administrative seat (approximate)'
        else:
            cap = None
            mode = 'capital coordinate unresolved; regional point'
    coords = coords or point(q)
    if not coords: return None, None
    if not seat: seat = mode
    # Different seats need separate plotting nodes. These are not new QIDs.
    key = q if is_jurisdiction else q + '@place'
    if q == 'Q129286':
        key += '@' + ('company' if y < 1858 else 'india' if y > 1947 else 'raj') + '-' + (cap or 'transition')
    elif cap and len(e.get('claims', {}).get('P36', [])) > 1:
        key += '@' + cap
    node = {'entity_qid': q, 'label': label, 'seat': seat, 'lat': coords[0], 'lon': coords[1],
            'coordinate_kind': mode, 'capital_qid': cap}
    return key, node


def ordered_arcs(pid, rows, nodes):
    """Preserve dated career connectivity and identify uncertainty explicitly.

    A multi-place year is a set of possible endpoints, not a missing career.
    Solid corridors require a single ordered endpoint on both sides. Dashed
    connections show alternatives, never an invented order within a year.
    Unknown locations can make a connection incomplete but cannot erase its
    known endpoints. No coordinate is assigned to an unknown event.
    """
    from itertools import groupby, combinations
    previous = set()
    previous_uncertain = False
    gap = False

    def edge(y, left, right, reason=None):
        if left == right or not 1700 <= y <= 1970:
            return None
        a, b = nodes[left], nodes[right]
        if a['entity_qid'] == b['entity_qid'] or (a['lat'], a['lon']) == (b['lat'], b['lon']):
            return None
        arc = {'pid': pid, 'yr': y, 'from': left, 'to': right}
        if reason: arc['uncertain'] = reason
        return arc

    for y, group in groupby(sorted(rows, key=lambda row: (row[0], row[1])), key=lambda row: row[0]):
        group = list(group)
        keys = {row[2] for row in group}
        known = keys - {None}
        if not known:
            gap = True
            continue
        groups = [known]
        if len(known) > 1 and None not in keys and all(len(row) > 3 and row[3] is not None for row in group):
            ordered = sorted(group, key=lambda row: row[3])
            groups = [{row[2] for row in batch} for _, batch in groupby(ordered, key=lambda row: row[3])]
        for current in groups:
            uncertain = len(current) > 1 or None in keys
            reason = ('unlocated event between recorded places' if gap or None in keys else
                      'alternative endpoints; within-year order unresolved' if previous_uncertain or uncertain else None)
            for left in sorted(previous):
                for right in sorted(current):
                    arc = edge(y, left, right, reason)
                    if arc: yield arc
            # Undirected associations: alphabetical storage is not a travel order.
            for left, right in combinations(sorted(current), 2):
                arc = edge(y, left, right, 'same-year places; direction and order unresolved')
                if arc: yield arc
            previous, previous_uncertain, gap = current, uncertain, False


def transfers(corpus):
    from collections import defaultdict
    from build_static_atlas import build_canon
    canon = build_canon()
    events, nodes = defaultdict(list), {}
    for r in records(corpus):
        if not r.get('year_start'): continue
        if r.get('event_kind') in NON_HELD or r.get('appointment_map_excluded'): continue
        key, node = project(r)
        if node: nodes[key] = node
        if r.get('route_neutral'): continue
        if r.get('mobility_excluded'): key = None
        events[canon(r['person_id'])].append((r['year_start'], r['seq'], key, r.get('route_order')))
    arcs = [a for pid, rows in events.items() for a in ordered_arcs(pid, rows, nodes)]
    return {'transfers': sorted((a for a in arcs if not a.get('uncertain')), key=lambda t: t['yr']),
            'uncertain_transfers': sorted((a for a in arcs if a.get('uncertain')), key=lambda t: t['yr']),
            'labels': {k: v['label'] for k, v in nodes.items()}, 'nodes': nodes}
