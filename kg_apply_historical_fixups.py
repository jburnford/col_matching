#!/usr/bin/env python3
"""Idempotent, source-preserving corrections after each graph emit."""
import json
from pathlib import Path
from historical_geography import correct_event
from reviewed_careers import NON_HELD

ROOT = Path(__file__).resolve().parent


def main():
    for corpus in ('kg', 'iol'):
        gd = ROOT / 'data' / corpus / 'graph_stage3'
        events = {}
        for line in (gd / 'career_events.jsonl').open():
            r = json.loads(line)
            events[(r['person_id'], r['seq'])] = r
        for name in ('career_events', 'career_facts', 'role_edges'):
            path = gd / (name + '.jsonl')
            tmp = path.with_suffix('.tmp')
            changed = 0
            with path.open() as src, tmp.open('w') as dst:
                for line in src:
                    row = json.loads(line)
                    event = events.get((row.get('person_id'), row.get('seq')))
                    fixed = correct_event(event) if event else row
                    if event and name == 'role_edges' and fixed.get('event_kind') in NON_HELD:
                        changed += 1
                        continue  # this is not a HELD_ROLE assertion
                    if event and (fixed != event or fixed.get('historical_corrections')):
                        keys = ('place_qid', 'place_label', 'colony_qid', 'colony_label',
                                'grounded', 'year_start', 'year_end', 'date_uncertain', 'mobility_excluded', 'route_order', 'route_neutral', 'event_kind', 'location_note',
                                'historical_corrections', 'role_id', 'role_label')
                        for key in keys:
                            if key in fixed and (name != 'role_edges' or key in
                                    ('role_id', 'role_label', 'year_start', 'year_end', 'historical_corrections')):
                                row[key] = fixed[key]
                    output = json.dumps(row, ensure_ascii=False) + '\n'
                    changed += output != line
                    dst.write(output)
            tmp.replace(path)
            print(f'{corpus}/{name}: {changed} changed')


if __name__ == '__main__':
    main()
