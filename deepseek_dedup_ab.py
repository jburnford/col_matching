"""DeepSeek A/B replay of the Opus dedup decisions.

Feeds each Opus-adjudicated cluster's dossier + the DEDUP_LLM_METHOD rules to a
cheaper model (deepseek/deepseek-v4-pro) via the capped/ledgered OpenRouter
client, then diffs DeepSeek's merge verdict against Opus's recorded verdict in
data/services/dedup/dedup_decisions_opus.jsonl.

Run in the SESSION-1 compiled state (only the 13 pre-session-2 merges applied) so
the 22 merged clusters are still un-collapsed. Read-only w.r.t. the ledger.

  python3 deepseek_dedup_ab.py --dry-run            # estimate spend only, no calls
  python3 deepseek_dedup_ab.py --limit 50 --cap 1.0 # run the A/B
"""
from __future__ import annotations
import argparse, json, re
from collections import defaultdict
from pathlib import Path

from col_match.config import Config
from col_match.services.schema import Biography, ParsedEntry
from col_match.services.match import _norm
from col_match.services.compile import _canon_token
from col_match.services.openrouter import OpenRouterClient, estimate_tokens, cost_of, price_of

cfg = Config.from_env(); DD = Path(cfg.data_dir)
DECISIONS = DD / "dedup" / "dedup_decisions_opus.jsonl"
OUT = DD / "dedup" / "deepseek_ab_results.jsonl"
SPEND_LEDGER = DD / "dedup" / "deepseek_ab_spend.jsonl"

ap = argparse.ArgumentParser()
ap.add_argument("--limit", type=int, default=50)
ap.add_argument("--model", default="deepseek/deepseek-v4-pro")
ap.add_argument("--cap", type=float, default=1.0, help="hard USD cap")
ap.add_argument("--dry-run", action="store_true")
args = ap.parse_args()

RULES = """You are given a CLUSTER of biographies from the Colonial Office List that share a \
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
multi-digit birth gap is weak evidence of DIFFERENT people (e.g. father/son) but is not decisive alone.

DO NOT MERGE when:
- Different spelled forenames (Myles John vs John Thomas; Charles vs Harold).
- Disjoint careers: different colonies/eras, no shared event.
- Same name + adjacent birth year but DIVERGENT education/specialty/career = different people.
- Same name but large birth gap + non-overlapping careers (father/son namesakes); brothers \
sharing a distinctive middle name but different forenames are DIFFERENT people.
- Coincidental shared forename across genuinely different surnames.

DEFAULT TO NOT MERGING when uncertain. A false merge is unrecoverable; a missed merge is recoverable.

OUTPUT JSON: {"merge_groups": [{"bios": [<bio_ids that are one person>], "reason": "<one line>"}]}. \
Emit one group per distinct person that has >=2 bios. If NO bios should be merged, output \
{"merge_groups": []}. Singletons need no group."""

SCHEMA = {
    "type": "object", "additionalProperties": False,
    "properties": {
        "merge_groups": {
            "type": "array",
            "items": {
                "type": "object", "additionalProperties": False,
                "properties": {
                    "bios": {"type": "array", "items": {"type": "string"}},
                    "reason": {"type": "string"},
                },
                "required": ["bios", "reason"],
            },
        }
    },
    "required": ["merge_groups"],
}

# ---- load bios + build the same clusters dedup_review uses ----
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
# map frozenset(bio_ids) -> component bios, for exact lookup of the recorded clusters
comp_by_set = {frozenset(b.bio_id for b in c): c for c in comps.values()}

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
    return (f"  [{tag}] bio={b.bio_id}\n      versions={b.version_ids}\n      {'; '.join(parts)}{term}")

def dossier(c):
    c = sorted(c, key=lambda b: (b.surname, b.given_names or ""))
    head = f"CLUSTER ({len(c)} bios, surnames: {sorted({b.surname for b in c})})\n"
    return head + "\n".join(line(b) for b in c)

# ---- load Opus decisions ----
decisions = [json.loads(l) for l in DECISIONS.open(encoding="utf-8")]
decisions = decisions[:args.limit]

# resolve each decision to its current cluster (exact bio_id set)
jobs, missing = [], []
for d in decisions:
    key = frozenset(d["cluster"])
    c = comp_by_set.get(key)
    if c is None:
        missing.append(d["cluster"])
        continue
    jobs.append((d, c))

print(f"decisions: {len(decisions)} | resolved to clusters: {len(jobs)} | unresolvable: {len(missing)}")
if missing:
    print("  (unresolvable — not in current compiled state, need SESSION-1 revert):")
    for m in missing[:8]:
        print("   ", m)

# ---- cost estimate ----
pin, pout = price_of(args.model)
tin = sum(estimate_tokens(RULES) + estimate_tokens(dossier(c)) for _, c in jobs)
est_out = 200 * len(jobs)            # ~200 tok/verdict typical
worst_out = 800 * len(jobs)          # ceiling used for the cap projection
print(f"\nmodel={args.model}  price=${pin}/${pout} per 1M (in/out)")
print(f"input tokens (est): {tin:,}  ->  ${cost_of(args.model, tin, 0):.4f}")
print(f"typical total (est ~200 out/call): ${cost_of(args.model, tin, est_out):.4f}")
print(f"WORST CASE (800 out/call ceiling): ${cost_of(args.model, tin, worst_out):.4f}   cap=${args.cap:.2f}")

if args.dry_run:
    print("\n[dry-run] no calls made.")
    raise SystemExit

# ---- run the A/B ----
key = cfg.openrouter_api_key or (Path("api.txt").read_text().strip() if Path("api.txt").exists() else "")
if not key:
    raise SystemExit("No OPENROUTER_API_KEY in .env (or api.txt).")
client = OpenRouterClient(api_key=key, cap_usd=args.cap, ledger_path=SPEND_LEDGER,
                          max_output_tokens=3000)  # reasoning model needs room before the JSON

def opus_merged_partition(d):
    # all Opus merges in this session merged the WHOLE cluster (size 2-3); no_merge = none
    return frozenset(d["cluster"]) if d["verdict"] == "merge" else frozenset()

results = []
with OUT.open("w", encoding="utf-8") as fh:
    for i, (d, c) in enumerate(jobs, 1):
        cset = frozenset(b.bio_id for b in c)
        try:
            resp = client.complete(model=args.model, system=RULES, user=dossier(c),
                                   response_schema=SCHEMA, section_id="|".join(sorted(cset)),
                                   tier="dedup_ab")
        except Exception as e:
            print(f"[{i}/{len(jobs)}] ERROR {type(e).__name__}: {e}")
            row = {"cluster": sorted(cset), "opus": d["verdict"], "error": str(e)[:200]}
            results.append(row); fh.write(json.dumps(row) + "\n"); fh.flush()
            if "SpendCapExceeded" in type(e).__name__: break
            continue
        groups = [g for g in resp.get("merge_groups", []) if len(g.get("bios", [])) >= 2]
        ds_merged = frozenset(bid for g in groups for bid in g["bios"] if bid in cset)
        opus_set = opus_merged_partition(d)
        # classify
        if d["verdict"] == "no_merge":
            agree = (len(ds_merged) == 0)
            fail = None if agree else "FALSE_MERGE"     # hard fail
        else:  # opus merge
            agree = (ds_merged == opus_set)
            if agree: fail = None
            elif len(ds_merged) == 0: fail = "MISSED_MERGE"  # soft fail
            else: fail = "PARTIAL"                            # subset / different grouping
        row = {"cluster": sorted(cset), "opus": d["verdict"],
               "deepseek_merged": sorted(ds_merged), "agree": agree, "fail": fail,
               "ds_reason": (groups[0]["reason"] if groups else "")[:160]}
        results.append(row); fh.write(json.dumps(row) + "\n"); fh.flush()
        mark = "OK " if agree else ("!!!" if fail == "FALSE_MERGE" else "x  ")
        print(f"[{i}/{len(jobs)}] {mark} opus={d['verdict']:<8} ds={'merge' if ds_merged else 'no_merge':<8} "
              f"{fail or ''}  {sorted(cset)}")

# ---- summary ----
n = len(results)
agree = sum(1 for r in results if r.get("agree"))
false_merge = [r for r in results if r.get("fail") == "FALSE_MERGE"]
missed = [r for r in results if r.get("fail") == "MISSED_MERGE"]
partial = [r for r in results if r.get("fail") == "PARTIAL"]
errs = [r for r in results if r.get("error")]
print(f"\n==== A/B SUMMARY ({n} clusters) ====")
print(f"agreement: {agree}/{n}  ({100*agree/max(n,1):.0f}%)")
print(f"FALSE MERGES (hard fail): {len(false_merge)}")
for r in false_merge: print("   !!!", r["cluster"], "->", r["deepseek_merged"], "|", r["ds_reason"])
print(f"missed merges (soft): {len(missed)}")
print(f"partial/diff grouping: {len(partial)}")
print(f"errors: {len(errs)}")
print(f"actual spend: ${client.running_spend():.4f}  (cap ${args.cap:.2f})")
print(f"results -> {OUT}")
