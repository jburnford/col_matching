#!/usr/bin/env python3
"""Build kg routes from explicit, date-aware event locations."""
import json
from pathlib import Path
from atlas_geography import transfers

if __name__ == '__main__':
    data = transfers('kg')
    Path('/tmp/transfers.json').write_text(json.dumps(data, ensure_ascii=False))
    Path('/tmp/transfer_qids.txt').write_text('\n'.join(sorted(data['nodes'])))
    Path('/tmp/transfer_coords.json').write_text(json.dumps({k: [v['lat'], v['lon']] for k, v in data['nodes'].items()}))
    print("kg: ", len(data['transfers']), "transfers;", len(data['nodes']), "mapped places")
