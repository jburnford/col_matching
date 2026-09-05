#!/usr/bin/env python3
"""Death-date veto for the person->Wikidata grounding layer (review D27).

kg_ground_persons.py vetoes on BIRTH contradiction only; a namesake whose
Wikidata entry DIED before the KG person's attested career (STEWART
kgp_col1929-p1058b14 = Q130573420, STOTT kgp_col1966-p313b9 = Q5295192) sailed
through on a birth-year coincidence. This screen fetches P570 (and P569) for
every grounded QID from QLever and drops a grounding when the KG person is
attested (career-event year, or List edition) more than DEATH_SLACK years
after the Wikidata death. Edition attestations get extra slack because a
late-edition entry can be a posthumous reprint / obituary-year listing.

Outputs (data/kg/):
  person_death_conflicts.jsonl          every conflict (kept for review)
  graph_stage3/person_grounding.final.jsonl   rewritten WITHOUT the conflicts
  person_grounding_death_dropped.jsonl  ledger of the dropped rows (append)
Usage: python3 verify_person_deaths.py [--dates cached.json] [--apply]
"""
import argparse, json, re, urllib.request
from collections import defaultdict
from pathlib import Path

GD = Path("data/kg/graph_stage3")
FINAL = GD / "person_grounding.final.jsonl"
DEATH_SLACK, EDITION_SLACK = 1, 3
QLEVER = "https://qlever.dev/api/wikidata"


def fetch_dates(qids):
    vals = " ".join("wd:" + q for q in qids)
    q = ("PREFIX wd: <http://www.wikidata.org/entity/> PREFIX wdt: <http://www.wikidata.org/prop/direct/> "
         f"SELECT ?item ?dod ?dob WHERE {{ VALUES ?item {{ {vals} }} "
         "OPTIONAL { ?item wdt:P570 ?dod } OPTIONAL { ?item wdt:P569 ?dob } }")
    req = urllib.request.Request(QLEVER, data=q.encode(), headers={
        "Content-Type": "application/sparql-query", "Accept": "application/sparql-results+json"})
    out = {}
    for b in json.load(urllib.request.urlopen(req, timeout=180))["results"]["bindings"]:
        qid = b["item"]["value"].rsplit("/", 1)[-1]
        d = out.setdefault(qid, {"dod": None, "dob": None})
        for k in ("dod", "dob"):
            v = b.get(k, {}).get("value", "")
            if v[:4].isdigit():
                d[k] = int(v[:4])
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dates", help="cached {qid: {dod, dob}} json (else fetch)")
    ap.add_argument("--apply", action="store_true")
    a = ap.parse_args()
    rows = [json.loads(l) for l in FINAL.open(encoding="utf-8")]
    dates = json.load(open(a.dates)) if a.dates else fetch_dates(sorted({r["qid"] for r in rows}))
    last_ev, last_ed = defaultdict(int), defaultdict(int)
    for l in (GD / "career_events.jsonl").open(encoding="utf-8"):
        e = json.loads(l)
        for y in (e.get("year_start"), e.get("year_end")):
            if y:
                last_ev[e["person_id"]] = max(last_ev[e["person_id"]], y)
    for l in (GD / "persons.jsonl").open(encoding="utf-8"):
        p = json.loads(l)
        for a_ in p.get("attestations") or []:
            m = re.search(r"(?:col|dol|iol)(\d{4})", a_ if isinstance(a_, str) else json.dumps(a_))
            if m:
                last_ed[p["person_id"]] = max(last_ed[p["person_id"]], int(m.group(1)))
    conflicts, keep = [], []
    for r in rows:
        d = dates.get(r["qid"]) or {}
        dod = d.get("dod")
        ev, ed = last_ev.get(r["person_id"], 0), last_ed.get(r["person_id"], 0)
        why = None
        if dod and ev and ev > dod + DEATH_SLACK:
            why = f"career event {ev} > WD death {dod}"
        elif dod and ed and ed > dod + EDITION_SLACK:
            why = f"List edition {ed} > WD death {dod}"
        if why:
            conflicts.append({**r, "wd_death": dod, "kg_last_event": ev or None,
                              "kg_last_edition": ed or None, "reason": why})
        else:
            keep.append(r)
    with open("data/kg/person_death_conflicts.jsonl", "w", encoding="utf-8") as fh:
        for c in conflicts:
            fh.write(json.dumps(c, ensure_ascii=False) + "\n")
    print(f"grounded {len(rows)}  with WD death {sum(1 for r in rows if (dates.get(r['qid']) or {}).get('dod'))}  "
          f"death conflicts {len(conflicts)}")
    for c in conflicts[:40]:
        print(f"  {c['person_id']:28s} {c['qid']:12s} {c['wd_name'][:28]:28s} tier {c['tier']}  {c['reason']}")
    if a.apply:
        with FINAL.open("w", encoding="utf-8") as fh:
            for r in keep:
                fh.write(json.dumps(r, ensure_ascii=False) + "\n")
        with open("data/kg/person_grounding_death_dropped.jsonl", "a", encoding="utf-8") as fh:
            for c in conflicts:
                fh.write(json.dumps(c, ensure_ascii=False) + "\n")
        print(f"applied: {len(keep)} rows kept -> {FINAL}")


if __name__ == "__main__":
    main()
