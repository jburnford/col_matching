#!/usr/bin/env python3
"""Extract every career TRANSFER (a person moving from one colony to another) from the KG.
A transfer = consecutive events (ordered by year) whose resolved colony changes.
Output raw transfers (year, from_qid, to_qid) + the distinct colony QIDs needing coords."""
import json, collections

ev = collections.defaultdict(list)
for l in open("data/kg/graph_stage3/career_facts.jsonl"):
    d = json.loads(l)
    col = d.get("colony_qid")            # resolved British colony only (inter-colony mobility)
    ys = d.get("year_start")
    if col and ys:
        ev[d["person_id"]].append((ys, d.get("year_end") or ys, col, d.get("colony_label")))

transfers = []
labels = {}
for pid, evs in ev.items():
    evs.sort()
    # collapse consecutive same-colony events into colony "stints"
    stints = []
    for ys, ye, col, lab in evs:
        labels[col] = lab
        if stints and stints[-1][2] == col:
            stints[-1] = (stints[-1][0], max(stints[-1][1], ye), col)
        else:
            stints.append((ys, ye, col))
    for a, b in zip(stints, stints[1:]):
        # move happens when they arrive at b
        yr = b[0]
        if 1700 <= yr <= 1970:
            transfers.append({"pid": pid, "yr": yr, "from": a[2], "to": b[2]})

transfers.sort(key=lambda t: t["yr"])
qids = sorted({t["from"] for t in transfers} | {t["to"] for t in transfers})
json.dump({"transfers": transfers, "labels": labels}, open("/tmp/transfers.json", "w"))
open("/tmp/transfer_qids.txt", "w").write("\n".join(qids))

yrs = [t["yr"] for t in transfers]
hist = collections.Counter((y//10)*10 for y in yrs)
print(f"transfers: {len(transfers):,}   distinct colonies: {len(qids)}   persons moving: {len({t['pid'] for t in transfers}):,}")
print(f"year range: {min(yrs)}-{max(yrs)}")
print("by decade:", dict(sorted(hist.items())))
