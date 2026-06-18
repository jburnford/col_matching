"""Stratified-sample adjudication of the tier-2 (below-bar) candidate pool.

For each evidence bucket, draw a deterministic random sample of below-bar
candidates, build a BIO-vs-OFFICIAL dossier, and have the validated
deepseek-v4-pro adjudicator label each match | namesake | uncertain. Gives an
UNBIASED per-bucket precision (the 543-career gold can't — see transcript).

  python3 tier2_adjudicate_sample.py --per-bucket 50 --cap 3
"""
from __future__ import annotations
import argparse, json, random
from collections import defaultdict, Counter
from pathlib import Path
from col_match.config import Config
from col_match.services.schema import Biography
from col_match.services.openrouter import OpenRouterClient

cfg = Config.from_env(); DD = Path(cfg.data_dir)
ap = argparse.ArgumentParser()
ap.add_argument("--per-bucket", type=int, default=50)
ap.add_argument("--cap", type=float, default=3.0)
ap.add_argument("--model", default="deepseek/deepseek-v4-pro")
ap.add_argument("--seed", type=int, default=0)
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
def bucket(c):
    if chk(c,"colony") and chk(c,"tenure_overlap") and (chk(c,"position_sim") or chk(c,"honour")):
        return "2A_passed_bar"
    if str(c.get("surname_gate","")).startswith("fuzzy"): return "2B_fuzzy_surname"
    if c.get("single_initial"): return "2C_single_initial"
    return "2D_other"
def notes(c):
    failed = [x["name"] for x in c.get("checks",[]) if not x["passed"]]
    return f"(matcher dropped this; failed checks: {', '.join(failed) or 'none'}; surname_gate={c.get('surname_gate')})"

# load + bucket all candidates that resolve to a known bio & official
byb = defaultdict(list)
for l in (DD/"candidates"/"below_bar.jsonl").open():
    c = json.loads(l)
    if c["bio_id"] in bios and c["official_id"] in officials:
        byb[bucket(c)].append(c)

rng = random.Random(args.seed)
sample = {bk: rng.sample(v, min(args.per_bucket, len(v))) for bk, v in byb.items()}
print("pool sizes:", {k: len(v) for k, v in byb.items()})
print("sampling:", {k: len(v) for k, v in sample.items()}, "\n")

key = cfg.openrouter_api_key
client = OpenRouterClient(api_key=key, cap_usd=args.cap,
                          ledger_path=DD/"dedup"/"tier2_adjudicate_spend.jsonl", max_output_tokens=2000)

out = (DD/"candidates"/"tier2_adjudicated_sample.jsonl").open("w")
tally = defaultdict(Counter); egs = defaultdict(lambda: defaultdict(list))
for bk in ["2A_passed_bar","2B_fuzzy_surname","2C_single_initial","2D_other"]:
    for c in sample.get(bk, []):
        b = bios[c["bio_id"]]; o = officials[c["official_id"]]
        user = f"{bio_block(b)}\n\n{off_block(o)}\n\nMATCHER NOTES: {notes(c)}"
        try:
            v = client.complete(model=args.model, system=SYS, user=user, response_schema=SCHEMA,
                                section_id=f"{c['bio_id']}|{c['official_id']}", tier="tier2adj")
        except Exception as e:
            tally[bk]["error"] += 1
            if "SpendCapExceeded" in type(e).__name__: print("CAP HIT"); break
            continue
        verdict = v.get("verdict","uncertain")
        tally[bk][verdict] += 1
        if len(egs[bk][verdict]) < 3:
            egs[bk][verdict].append(f"{c['bio_id']} -> {c['official_id']} :: {v.get('reason','')[:90]}")
        out.write(json.dumps({"bucket":bk,"bio_id":c["bio_id"],"official_id":c["official_id"],
                              "verdict":verdict,"reason":v.get("reason","")}) + "\n")
out.close()

print("\n==== TIER-2 SAMPLE ADJUDICATION (deepseek-v4-pro) ====")
for bk in ["2A_passed_bar","2B_fuzzy_surname","2C_single_initial","2D_other"]:
    t = tally[bk]; m=t["match"]; n=t["namesake"]; u=t["uncertain"]; judged=m+n
    prec = f"{100*m/judged:.0f}%" if judged else "n/a"
    print(f"\n[{bk}] pool={len(byb[bk])}  sampled={sum(t.values())}  "
          f"-> match={m} namesake={n} uncertain={u}  PRECISION(match/(match+namesake))={prec}")
    for verd in ("match","namesake"):
        for e in egs[bk][verd]: print(f"    [{verd}] {e}")
print(f"\nspend ${client.running_spend():.4f}")
