"""Production DeepSeek dedup runner: propose -> adversarially verify -> commit.

For each unreviewed cluster (size in [--min,--max]) not already in the ledger:
  1. PROPOSE: deepseek-v4-pro partitions the cluster into same-person merge groups
     (the same rules the Opus A/B validated at 0 false merges on size-2/3).
  2. VERIFY: a SECOND, skeptical deepseek call tries to REFUTE each proposed group
     (default refuted=true when uncertain). Only groups that survive are committed.
  3. COMMIT (--commit): append surviving groups to data/services/dedup/llm_merges.jsonl
     in the pass-F format (versions = union of the group bios' version_ids), tagged
     source=deepseek-v4-pro so they are distinguishable from the Opus gold merges.

All spend flows through the capped/ledgered OpenRouterClient. Resumable: clusters
already in the ledger are skipped. Does NOT recompile mid-run (clusters are fixed at
start); run compile->infer_colony->attach->match->eval_known AFTER, and the 0-FP gate
is the final backstop.

  python3 deepseek_dedup_run.py --min 2 --max 3 --workers 5 --cap 8 --commit
  python3 deepseek_dedup_run.py --min 2 --max 3 --limit 20      # dry (no --commit): propose+verify only
"""
from __future__ import annotations
import argparse, json, re, threading
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

from col_match.config import Config
from col_match.services.schema import Biography, ParsedEntry
from col_match.services.match import _norm
from col_match.services.compile import _canon_token
from col_match.services.openrouter import OpenRouterClient

cfg = Config.from_env(); DD = Path(cfg.data_dir)
LEDGER = DD / "dedup" / "llm_merges.jsonl"
OUT = DD / "dedup" / "deepseek_run_results.jsonl"
SPEND = DD / "dedup" / "deepseek_run_spend.jsonl"

ap = argparse.ArgumentParser()
ap.add_argument("--min", type=int, default=2)
ap.add_argument("--max", type=int, default=3)
ap.add_argument("--limit", type=int, default=0, help="0 = all matching clusters")
ap.add_argument("--workers", type=int, default=5)
ap.add_argument("--cap", type=float, default=8.0)
ap.add_argument("--model", default="deepseek/deepseek-v4-pro")
ap.add_argument("--commit", action="store_true", help="append surviving merges to the ledger")
args = ap.parse_args()

PROPOSE_SYS = """You are given a CLUSTER of biographies from the Colonial Office List that share a \
surname-suffix and a spelled forename. Decide which bios are the SAME real person. Output merge groups.

MERGE two+ bios (same person) ONLY on POSITIVE same-person evidence:
1. Overlapping career: >=1 event agreeing on year (+/-1) AND place or position.
2. Distinctive education: near-identical education string (near-unique per person).
3. Shared honour+year, or shared death/terminal year.
4. OCR surname/headword variant: one surname is a clear garble/truncation of the other \
(dropped first letter ANDOLO->DANDOLO, APPER->CAPPER, AWCETT->FAWCETT; ATTKEN->AITKEN) AND \
the forename + career are consistent. A single identical dated event suffices here.
5. Thin/empty fragment with the SAME full given name AND a shared honour-year OR a shared \
distinctive dated event. A careerless fragment with NOTHING but a matching name is NOT enough.

Birth year is OCR-noisy: do NOT split on +/-1-2 or one-digit differences (1885/1886). A large \
multi-digit birth gap is weak evidence of DIFFERENT people but is not decisive alone.

DO NOT MERGE when: different spelled forenames; disjoint careers (different colonies/eras, no shared \
event); same name + adjacent birth but DIVERGENT education/specialty/career; same name + large birth \
gap + non-overlapping careers (father/son); brothers sharing a distinctive middle name but different \
forenames; coincidental shared forename across genuinely different surnames.

DEFAULT TO NOT MERGING when uncertain. A false merge is unrecoverable; a missed merge is recoverable.

OUTPUT JSON: {"merge_groups": [{"bios": [<bio_ids that are one person>], "reason": "<one line>"}]}. \
One group per distinct person that has >=2 bios. If NO bios should be merged, output {"merge_groups": []}."""

VERIFY_SYS = """You are an adversarial verifier. Another model proposed that a group of biographies \
are THE SAME real person. The proposal was based on same-person evidence. CONFIRM the merge unless you \
find concrete evidence they are DIFFERENT people.

CONFIRM (refuted=false) when the bios share ANY of: a dated career event agreeing on year (+/-1) with \
matching place or position; near-identical distinctive education; a shared honour-year or death-year; OR \
a clear OCR variant of the surname/forename/middle-name (dropped or garbled letters: Owald=Oswald, \
Whinford=Whinfield, ANDOLO=DANDOLO, Mac=Mc, reordered surnames) together with a consistent career. \
OCR garbles of NAMES ARE EXPECTED in this corpus -- do NOT refute merely because name strings differ. \
A one- or two-token name difference with an identical or strongly-overlapping career is the SAME person. \
Two people CANNOT hold the same singular post in the same year, so a year-aligned identical event is \
strong same-person evidence even if a name token differs. Birth-year differences of +/-1-2 or one digit \
are OCR noise, NOT grounds to refute.

REFUTE (refuted=true) ONLY on positive evidence of DIFFERENT people:
- Disjoint careers: different colonies/eras with NO shared dated event.
- A clean, non-OCR forename difference (e.g. Charles vs Francis, Alfred vs Edward, Myles vs John) AND no \
identical dated event tying them -- likely brothers.
- Same name but a large multi-digit birth gap AND non-overlapping careers -- likely father/son.
- A careerless fragment whose ONLY link is a common name (no shared honour-year, no shared dated event).
- A genuine specialty/discipline divergence under the same name (e.g. one a MARINE surveyor with A.M.I.N.A, \
one a LAND surveyor with M.I.S.W.A, different education).

Default to CONFIRM when the career evidence is strong; refute only on a concrete different-person signal.

OUTPUT JSON: {"refuted": <bool>, "reason": "<one line>"}."""

PROPOSE_SCHEMA = {
    "type": "object", "additionalProperties": False,
    "properties": {"merge_groups": {"type": "array", "items": {
        "type": "object", "additionalProperties": False,
        "properties": {"bios": {"type": "array", "items": {"type": "string"}},
                       "reason": {"type": "string"}},
        "required": ["bios", "reason"]}}},
    "required": ["merge_groups"]}
VERIFY_SCHEMA = {
    "type": "object", "additionalProperties": False,
    "properties": {"refuted": {"type": "boolean"}, "reason": {"type": "string"}},
    "required": ["refuted", "reason"]}

# ---- load bios + build clusters (same key as dedup_review / compile pass E) ----
bios = [Biography.model_validate_json(l)
        for l in (DD / "biographies" / "biographies.jsonl").open(encoding="utf-8")]
bymap = {b.bio_id: b for b in bios}
edu = {}
for name in ("llm.jsonl", "rules.jsonl"):
    p = DD / "parsed" / name
    if p.exists():
        for l in p.open(encoding="utf-8"):
            r = ParsedEntry.model_validate_json(l)
            edu[r.version_id] = r.education or ""
matched = set()
for fn in ("stint_matches.jsonl", "record_attachments.jsonl"):
    p = DD / "matches" / fn
    if p.exists():
        for l in p.open(encoding="utf-8"):
            matched.add(json.loads(l)["bio_id"])
reviewed_versions = set()
if LEDGER.exists():
    for l in LEDGER.open(encoding="utf-8"):
        reviewed_versions.update(json.loads(l).get("versions", []))

def spelled(b):
    return {_canon_token(t) for t in re.split(r"[ .]+", b.given_names or "") if len(_canon_token(t)) > 2}
idx = {b.bio_id: i for i, b in enumerate(bios)}
parent = list(range(len(bios)))
def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]; x = parent[x]
    return x
def union(a, b):
    ra, rb = find(a), find(b)
    if ra != rb: parent[ra] = rb
buckets = defaultdict(list)
for b in bios:
    sur = _norm(b.surname)
    if len(sur) < 5: continue
    suf = sur[-4:]
    for tok in spelled(b):
        buckets[(tok, suf)].append(b.bio_id)
for members in buckets.values():
    for k in range(1, len(members)):
        union(idx[members[0]], idx[members[k]])
comps = defaultdict(list)
for b in bios:
    comps[find(idx[b.bio_id])].append(b)
clusters = [c for c in comps.values() if len(c) >= 2]
def cluster_versions(c): return {v for b in c for v in b.version_ids}
todo = [c for c in clusters
        if args.min <= len(c) <= args.max and not (cluster_versions(c) & reviewed_versions)]
todo.sort(key=lambda c: (len(c), min(b.bio_id for b in c)))
if args.limit:
    todo = todo[:args.limit]

def line(b):
    tag = "MATCHED " if b.bio_id in matched else "unmatch."
    e = max((edu.get(v, "") for v in b.version_ids), key=len, default="")
    ev = [x for x in b.events if x.year_start]
    career = " | ".join(f"{x.year_start} {x.place or '-'} {(x.position or '')[:34]}" for x in ev[:14])
    hon = ";".join(f"{h.award}{('/'+str(h.year)) if h.year else ''}" for h in b.honours[:6])
    by = f"b.{b.birth_year.value}" if b.birth_year else "b.?"
    term = f" {b.terminal.kind}.{b.terminal.year}" if (b.terminal and b.terminal.year) else ""
    parts = [f"{b.surname}, {b.given_names or '?'}", by]
    if e: parts.append("ed. " + e[:90])
    if hon: parts.append("hon: " + hon)
    parts.append("career: " + (career or "(none)"))
    return (f"  [{tag}] bio={b.bio_id}\n      {'; '.join(parts)}{term}")

def dossier(blist):
    blist = sorted(blist, key=lambda b: (b.surname, b.given_names or ""))
    head = f"CLUSTER ({len(blist)} bios, surnames: {sorted({b.surname for b in blist})})\n"
    return head + "\n".join(line(b) for b in blist)

print(f"clusters to process: {len(todo)} (size {args.min}-{args.max}, unreviewed) | "
      f"workers={args.workers} cap=${args.cap} commit={args.commit}")

key = cfg.openrouter_api_key or (Path("api.txt").read_text().strip() if Path("api.txt").exists() else "")
if not key:
    raise SystemExit("No OPENROUTER_API_KEY in .env")
client = OpenRouterClient(api_key=key, cap_usd=args.cap, ledger_path=SPEND, max_output_tokens=6000)

ledger_lock = threading.Lock()
out_lock = threading.Lock()

def process(c):
    cset = {b.bio_id for b in c}
    sid = "|".join(sorted(cset))
    prop = client.complete(model=args.model, system=PROPOSE_SYS, user=dossier(c),
                           response_schema=PROPOSE_SCHEMA, section_id=sid, tier="propose")
    groups = [g for g in prop.get("merge_groups", [])
              if len([x for x in g.get("bios", []) if x in cset]) >= 2]
    confirmed, refused = [], []
    for g in groups:
        gb = [bymap[x] for x in g["bios"] if x in cset]
        v = client.complete(model=args.model, system=VERIFY_SYS, user=dossier(gb),
                            response_schema=VERIFY_SCHEMA, section_id=sid, tier="verify")
        if v.get("refuted", True):
            refused.append({"bios": sorted(b.bio_id for b in gb),
                            "propose_reason": g["reason"][:160], "refute_reason": v.get("reason","")[:160]})
        else:
            versions = sorted({ver for b in gb for ver in b.version_ids})
            confirmed.append({"versions": versions, "bios": sorted(b.bio_id for b in gb),
                              "reason": g["reason"][:200], "confidence": "high",
                              "source": "deepseek-v4-pro", "verified": True})
    if args.commit and confirmed:
        with ledger_lock, LEDGER.open("a", encoding="utf-8") as fh:
            for m in confirmed:
                fh.write(json.dumps(m) + "\n")
    row = {"cluster": sorted(cset), "n_proposed": len(groups),
           "confirmed": confirmed, "refused": refused}
    with out_lock, OUT.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(row) + "\n")
    return row

OUT.write_text("")  # fresh results log for this run
done = prop_merges = conf_merges = ref_merges = errs = 0
with ThreadPoolExecutor(max_workers=args.workers) as ex:
    futs = {ex.submit(process, c): c for c in todo}
    for f in as_completed(futs):
        done += 1
        try:
            r = f.result()
            prop_merges += r["n_proposed"]; conf_merges += len(r["confirmed"]); ref_merges += len(r["refused"])
        except Exception as e:
            errs += 1
            if "SpendCapExceeded" in type(e).__name__:
                print(f"!! {e}"); break
            if done <= 5 or errs <= 5:
                print(f"  err: {type(e).__name__}: {str(e)[:120]}")
        if done % 100 == 0:
            print(f"  {done}/{len(todo)} | proposed={prop_merges} confirmed={conf_merges} "
                  f"refused={ref_merges} err={errs} | ${client.running_spend():.3f}")

print(f"\n==== RUN DONE ====")
print(f"clusters: {done}/{len(todo)} | errors: {errs}")
print(f"merges proposed: {prop_merges} | confirmed (committed={args.commit}): {conf_merges} | "
      f"refused by verifier: {ref_merges}")
print(f"spend: ${client.running_spend():.4f} (cap ${args.cap})")
print(f"results -> {OUT}")
if args.commit:
    print(f"ledger now: {sum(1 for _ in LEDGER.open())} groups  (recompile->infer->attach->match->eval_known next)")
