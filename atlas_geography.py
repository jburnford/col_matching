"""Date-aware, offline atlas plotting. A map point is not an asserted workplace.

Jurisdictions use a dated capital where evidence supports one; explicit places
without a jurisdiction use their own coordinate. Ambiguous capitals use a
regional point, never the arbitrary first P36 value.
"""
import json
from functools import lru_cache
from pathlib import Path
from historical_geography import correct_event, location
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
    q, label = location(r)
    y = r.get('year_start')
    if not q or not y: return None, None
    e = evidence().get(q, {})
    label = label or e.get('label') or q
    label = {'Q891827': 'Bombay Presidency', 'Q817165': 'Bengal Presidency'}.get(q, label)
    seat, coords, cap = '', None, None
    mode = 'regional point'
    is_jurisdiction = bool(r.get('colony_qid'))
    # Direct historical evidence supersedes inconsistent P36 dates (1971 in WD).
    if q == 'Q1643555':
        cap = 'Q108223' if y < 1970 else 'Q3043'
    elif q == 'Q129286':
        if y <= 1910: cap = 'Q1348'
        elif y >= 1912: cap = 'Q987'
        else: mode = 'capital changed in 1911; regional point'
        # Avoid claiming the Raj existed before Crown rule.
        label = 'India (Company period)' if y < 1858 else ('India' if y > 1947 else 'British Raj')
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
    key = q
    if q == 'Q129286':
        key += '@' + ('company' if y < 1858 else 'india' if y > 1947 else 'raj') + '-' + (cap or 'transition')
    elif cap and len(e.get('claims', {}).get('P36', [])) > 1:
        key += '@' + cap
    node = {'entity_qid': q, 'label': label, 'seat': seat, 'lat': coords[0], 'lon': coords[1],
            'coordinate_kind': mode, 'capital_qid': cap}
    return key, node


def transfers(corpus):
    from collections import defaultdict
    events, nodes = defaultdict(list), {}
    for r in records(corpus):
        if not r.get('year_start'): continue
        if r.get('event_kind') == 'electoral_defeat': continue
        key, node = project(r)
        if node: nodes[key] = node
        events[r['person_id']].append((r['year_start'], r['seq'], key))
    arcs = []
    for pid, rows in events.items():
        previous = None
        for y, seq, key in sorted(rows):
            if previous and key and previous != key and 1700 <= y <= 1970:
                if nodes[previous]['entity_qid'] != nodes[key]['entity_qid']:
                    arcs.append({'pid': pid, 'yr': y, 'from': previous, 'to': key})
            # Unknown location breaks a route; it must not invent a direct move.
            previous = key
    return {'transfers': sorted(arcs, key=lambda t: t['yr']),
            'labels': {k: v['label'] for k, v in nodes.items()}, 'nodes': nodes}
