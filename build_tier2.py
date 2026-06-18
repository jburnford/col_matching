"""Build the tier-2A probable-match layer.

Adjudicates every below-bar candidate in bucket 2A (passed colony+tenure+
position/honour; dropped by the 0-FP matcher only on an ambiguity name-tie)
with the validated deepseek-v4-pro adjudicator. Writes:
  matches/stint_matches_tier2.jsonl  -- verdict=="match" only (the usable layer)
  candidates/tier2_2A_full.jsonl     -- every verdict (match|namesake|uncertain) for audit

This layer is SEPARATE from the 0-FP tier-1 union and is NEVER merged into it.
Measured base precision of bucket 2A ~89% (tier2_adjudicate_sample.py).

  python3 build_tier2.py --workers 5 --cap 8
"""
from __future__ import annotations
import argparse, json, threading
from collections import defaultdict, Counter
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from col_match.config import Config
from col_match.services.schema import Biography
from col_match.services.openrouter import OpenRouterClient

cfg = Config.from_env(); DD = Path(cfg.data_dir)
ap = argparse.ArgumentParser()
ap.add_argument("--workers", type=int, default=5)
ap.add_argument("--cap", type=float, default=8.0)
ap.add_argument("--model", default="deepseek/deepseek-v4-pro")
args = ap.parse_args()

SYS = """You decide whether a Colonial Office List BIOGRAPHY and a staff-list OFFICIAL RECORD are the \
SAME real person. The biography is a who's-who entry; the official record is one person's entries in the \
imperial staff lists (name, colony, positions by year).

Answer "match" ONLY on positive same-person evidence: the surname agrees (allow OCR garbles/truncation, \
e.g. Nuhan=Nunan, dropped letters), the forename/initials are compatible, AND the careers are consistent \
-- a year/place/position in the bio aligns with the official's record, or the bio's career plausibly \
continues into the official's stint.

Answer "namesake" if they are clearly DIFFERENT people who merely share a surname: incompatible \
forenames/initials, disjoint careers (different colonies/eras with no continuity), or the official is \
plainly another individual.

Answer "uncertain" if the evidence is too thin to decide.

A single shared initial + surname is NOT enough for "match" unless the career corroborates -- \
same-surname-same-initial collisions are common in this corpus.

OUTPUT JSON: {"verdict":"match|namesake|uncertain","reason":"<one line>"}"""
SCHEMA = {"type":"object","additionalProperties":False,
          "properties":{"verdict":{"type":"string","enum":["match","namesake","uncertain"]},
                        "reason":{"type":"string"}},"required":["verdict","reason"]}

bios = {}
for l in (DD/"biographies"/"biographies.jsonl").open():
    b = Biography.model_validate_json(l); bios[b.bio_id] = b
officials = {}
for l in (DD/"graph_cache"/"officials_augmented.jsonl").open():
    o = json.loads(l); officials[o["id"]] = o

def bio_block(b):
    ev = [x for x in b.events if x.year_start]
    car = " | ".join(f"{x.year_start} {x.place or '-'} {(x.position or '')[:36]}" for x in ev[:14])
    hon = ";".join(f"{h.award}{('/'+str(h.year)) if h.year else ''}" for h in b.honours[:6])
    by = f"b.{b.birth_year.value}" if b.birth_year else "b.?"
    return (f"BIOGRAPHY: {b.surname}, {b.given_names or '?'}; {by}"
            + (f"; honours: {hon}" if hon else "") + f"\n  career: {car or '(none)'}")
def off_block(o):
    recs = sorted(o.get("records", []), key=lambda r: r.get("year") or 0)
    pos = " | ".join(f"{r.get('year')} {r.get('position_raw') or '-'}" for r in recs[:14])
    return (f"OFFICIAL RECORD: {o['name']}; colony {o.get('colony')}; "
            f"{o.get('first_year')}-{o.get('last_year')}\n  postings: {pos or '(none)'}")
def chk(c, name):
    for x in c.get("checks", []):
        if x["name"] == name: return x["passed"]
    return False
def is_2A(c):
    return chk(c,"colony") and chk(c,"tenure_overlap") and (chk(c,"position_sim") or chk(c,"honour"))
def notes(c):
    failed = [x["name"] for x in c.get("checks",[]) if not x["passed"]]
    return f"(failed checks: {', '.join(failed) or 'none'}; surname_gate={c.get('surname_gate')})"

cands = []
for l in (DD/"candidates"/"below_bar.jsonl").open():
    c = json.loads(l)
    if c["bio_id"] in bios and c["official_id"] in officials and is_2A(c):
        cands.append(c)
print(f"tier-2A candidates to adjudicate: {len(cands)}  | workers={args.workers} cap=${args.cap}")

key = cfg.openrouter_api_key
client = OpenRouterClient(api_key=key, cap_usd=args.cap,
                          ledger_path=DD/"dedup"/"tier2_build_spend.jsonl", max_output_tokens=2000)
lock = threading.Lock()
full = (DD/"candidates"/"tier2_2A_full.jsonl").open("w")
tier2 = (DD/"matches"/"stint_matches_tier2.jsonl").open("w")
tally = Counter()

def work(c):
    b = bios[c["bio_id"]]; o = officials[c["official_id"]]
    user = f"{bio_block(b)}\n\n{off_block(o)}\n\nMATCHER NOTES: {notes(c)}"
    v = client.complete(model=args.model, system=SYS, user=user, response_schema=SCHEMA,
                        section_id=f"{c['bio_id']}|{c['official_id']}", tier="tier2build")
    verd = v.get("verdict","uncertain")
    row = {"bio_id":c["bio_id"], "official_id":c["official_id"], "verdict":verd,
           "reason":v.get("reason","")[:200], "bucket":"2A_passed_bar",
           "surname_gate":c.get("surname_gate"), "single_initial":c.get("single_initial",False),
           "source":"tier2_adjudicated", "tier":2}
    with lock:
        full.write(json.dumps(row)+"\n"); full.flush()
        if verd == "match":
            tier2.write(json.dumps(row)+"\n"); tier2.flush()
        tally[verd]+=1
    return verd

done=0; err=0
with ThreadPoolExecutor(max_workers=args.workers) as ex:
    futs={ex.submit(work,c):c for c in cands}
    for f in as_completed(futs):
        done+=1
        try: f.result()
        except Exception as e:
            err+=1
            if "SpendCapExceeded" in type(e).__name__: print("CAP HIT — stopping"); break
        if done % 250 == 0:
            print(f"  {done}/{len(cands)} | match={tally['match']} namesake={tally['namesake']} "
                  f"uncertain={tally['uncertain']} err={err} | ${client.running_spend():.2f}")
full.close(); tier2.close()
print(f"\n==== TIER-2A BUILD DONE ====")
print(f"adjudicated {done} (err {err}) | match={tally['match']} namesake={tally['namesake']} uncertain={tally['uncertain']}")
print(f"precision (match/(match+namesake)) = {100*tally['match']/max(1,tally['match']+tally['namesake']):.0f}%")
print(f"-> matches/stint_matches_tier2.jsonl ({tally['match']} probable matches, SEPARATE from 0-FP union)")
print(f"-> candidates/tier2_2A_full.jsonl (all verdicts) | spend ${client.running_spend():.4f}")
