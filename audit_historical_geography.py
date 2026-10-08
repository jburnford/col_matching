#!/usr/bin/env python3
"""Reproducible, corpus-wide geography audit; candidates are not adjudications.

Run --baseline before repairs, then without it after rebuilding. Baseline outputs
are retained as evidence; normal runs only replace the current audit.
"""
import argparse, collections, csv, json
from pathlib import Path
from atlas_geography import evidence, value, year, project
from historical_geography import correct_event

ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'research/geography-2026-10-07'


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--baseline', action='store_true')
    args = parser.parse_args()
    prefix = 'baseline' if args.baseline else 'current'
    counts, candidates, changes = {}, [], []
    for corpus in ('kg', 'iol'):
        n = collections.Counter()
        for line in (ROOT / f'data/{corpus}/graph_stage3/career_events.jsonl').open():
            r = json.loads(line)
            n['events'] += 1
            y, pq, cq = r.get('year_start'), r.get('place_qid'), r.get('colony_qid')
            if not y: n['undated'] += 1
            if y and y < 1910 and 'Q193619' in (pq, cq): n['pre_1910_union'] += 1
            if pq and not cq: n['explicit_place_without_colony'] += 1
            if y and not cq: n['dated_without_colony_nearest_fallback_risk'] += 1
            if y and cq == 'Q1643555' and y < 1970: n['honduras_before_belmopan'] += 1
            if y and cq == 'Q129286' and y < 1911: n['india_before_delhi'] += 1
            fixed = correct_event(r)
            diff = {k: [r.get(k), v] for k, v in fixed.items() if r.get(k) != v and k != 'historical_corrections'}
            if diff:
                changes.append({'corpus': corpus, 'person_id': r['person_id'], 'seq': r['seq'],
                                'year': y, 'position': r.get('position'), 'place_raw': r.get('place_raw'), 'changes': diff})
            if not y or not cq: continue
            claims = evidence().get(cq, {}).get('claims', {})
            starts = [year(value(s)) for s in claims.get('P571', []) if s.get('rank') != 'deprecated']
            ends = [year(value(s)) for s in claims.get('P576', []) if s.get('rank') != 'deprecated']
            starts, ends = [v for v in starts if v], [v for v in ends if v]
            # Coarse screen only: establishment dates can describe a legal form,
            # not the first use of a geographical name. Preserve for source review.
            reason = ('before entity inception' if starts and y < min(starts) else
                      'after entity dissolution' if ends and y > max(ends) else None)
            if reason:
                n['temporal_candidates'] += 1
                candidates.append([corpus, r['person_id'], r['seq'], y, cq, r.get('colony_label'),
                                   r.get('place_raw'), r.get('position'), reason,
                                   min(starts) if starts else 'unknown', max(ends) if ends else 'unknown'])
        counts[corpus] = dict(n)
    (OUT / f'{prefix}-counts.json').write_text(json.dumps(counts, indent=2) + '\n')
    (OUT / f'{prefix}-corrections.json').write_text(json.dumps(changes, ensure_ascii=False, indent=1) + '\n')
    with (OUT / f'{prefix}-temporal-review.tsv').open('w') as f:
        writer = csv.writer(f, delimiter='\t', lineterminator='\n')
        writer.writerow(['corpus', 'person_id', 'seq', 'year', 'qid', 'label', 'place_raw', 'position', 'reason', 'inception', 'dissolution'])
        writer.writerows(candidates)
    print(json.dumps(counts, indent=2))
    print(len(changes), 'events would change under reviewed rules;', len(candidates), 'temporal candidates')


if __name__ == '__main__': main()
