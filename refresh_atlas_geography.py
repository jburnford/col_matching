#!/usr/bin/env python3
"""Explicit network refresh of the reproducible atlas geography evidence cache.

Normal atlas builds are offline. Keep P36 qualifiers instead of picking the first
capital. Cache only labels, coordinates, inception/dissolution and capital claims.
"""
import json, urllib.request, urllib.parse, time
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DEST = ROOT / 'research/geography-2026-10-07/wikidata.json'


def main():
    data = json.loads(DEST.read_text()) if DEST.exists() else {}
    qids = {'Q108223', 'Q1533', 'Q1348', 'Q987', 'Q3926', 'Q5465', 'Q37701'}
    for corpus in ('kg', 'iol'):
        for line in (ROOT / f'data/{corpus}/graph_stage3/career_events.jsonl').open():
            r = json.loads(line)
            for key in ('place_qid', 'colony_qid'):
                if (r.get(key) or '').startswith('Q'): qids.add(r[key])
    for e in data.values():
        for s in e.get('claims', {}).get('P36', []):
            cap = s.get('mainsnak', {}).get('datavalue', {}).get('value', {}).get('id')
            if cap: qids.add(cap)
    pending = sorted(qids - data.keys())
    while pending:
        time.sleep(3)
        batch, pending = pending[:40], pending[40:]
        url = 'https://www.wikidata.org/w/api.php?' + urllib.parse.urlencode({
            'action': 'wbgetentities', 'ids': '|'.join(batch), 'props': 'labels|claims',
            'languages': 'en', 'format': 'json', 'redirects': 'yes'})
        req = urllib.request.Request(url, headers={'User-Agent': 'ImperialCareersHistoricalAudit/1.0'})
        for attempt in range(4):
            try:
                with urllib.request.urlopen(req, timeout=45) as response: result = json.load(response)
                break
            except Exception:
                if attempt == 3: raise
                time.sleep(10 * (attempt + 1))
        entities = result['entities']
        for q in batch:
            redirected = next((x['to'] for x in result.get('redirects', []) if x['from'] == q), q)
            e = entities.get(redirected, {})
            claims = e.get('claims', {})
            data[q] = {'id': redirected, 'label': e.get('labels', {}).get('en', {}).get('value', q),
                       'claims': {p: claims[p] for p in ('P625', 'P571', 'P576', 'P36') if p in claims}}
            for s in claims.get('P36', []):
                cap = s.get('mainsnak', {}).get('datavalue', {}).get('value', {}).get('id')
                if cap and cap not in data and cap not in pending and cap not in batch: pending.append(cap)
        DEST.write_text(json.dumps(data, ensure_ascii=False, separators=(',', ':')) + '\n')
        print(f'{len(data)} cached; {len(pending)} remaining', flush=True)


if __name__ == '__main__': main()
