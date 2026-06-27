#!/usr/bin/env python3
"""India Office List variant of compute_transfers.py.

Extract every career TRANSFER (an official moving between Indian presidencies/
provinces -- or to/from the imperial periphery: Burma, Aden, Mesopotamia, etc.)
from the IOL knowledge graph.  A transfer = consecutive events (ordered by year)
whose resolved colony/presidency changes.

The IOL spine already resolves each event's geography into colony_qid /
colony_label = a presidency (Bengal/Madras/Bombay), a province (Punjab, United
Provinces, Sind, Assam, ...), a princely state, or the all-India "Indian Empire
(British Raj)" central node -- so we read career_events.jsonl directly (the IOL
build has no fused career_facts.jsonl, unlike the CO corpus).

Output raw transfers (year, from_qid, to_qid) + the distinct place QIDs needing
coords."""
import json, collections

ev = collections.defaultdict(list)
for l in open("data/iol/graph_stage3/career_events.jsonl"):
    d = json.loads(l)
    col = d.get("colony_qid")            # resolved presidency/province/colony
    ys = d.get("year_start")
    if col and ys:
        ev[d["person_id"]].append((ys, d.get("year_end") or ys, col, d.get("colony_label")))

transfers = []
labels = {}
for pid, evs in ev.items():
    evs.sort()
    # collapse consecutive same-place events into "stints"
    stints = []
    for ys, ye, col, lab in evs:
        labels[col] = lab
        if stints and stints[-1][2] == col:
            stints[-1] = (stints[-1][0], max(stints[-1][1], ye), col)
        else:
            stints.append((ys, ye, col))
    for a, b in zip(stints, stints[1:]):
        yr = b[0]                        # the move happens when they arrive at b
        if 1700 <= yr <= 1970:
            transfers.append({"pid": pid, "yr": yr, "from": a[2], "to": b[2]})

transfers.sort(key=lambda t: t["yr"])
qids = sorted({t["from"] for t in transfers} | {t["to"] for t in transfers})
json.dump({"transfers": transfers, "labels": labels}, open("/tmp/iol_transfers.json", "w"))
open("/tmp/iol_transfer_qids.txt", "w").write("\n".join(qids))

yrs = [t["yr"] for t in transfers]
hist = collections.Counter((y // 10) * 10 for y in yrs)
print(f"transfers: {len(transfers):,}   distinct places: {len(qids)}   officials moving: {len({t['pid'] for t in transfers}):,}")
print(f"year range: {min(yrs)}-{max(yrs)}")
print("by decade:", dict(sorted(hist.items())))
