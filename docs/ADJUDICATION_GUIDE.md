# Adjudication guide — instructions for future sessions

How to recover bio↔stint links that the deterministic matcher can't make on its
own, **without ever creating a false merge**. Read this whole file before
adjudicating. Prerequisite context: `docs/LOOP_HANDOFF.md` (deterministic
levers), memory `adjudication-harness-state.md`, `NEXT_SESSION.md`.

---

## 0. The strategic principle: GENERAL FIRST, one-offs last

This is the most important section. The question that governs the work:

> Is this mismatch an instance of a CLASS that a deterministic rule could fix
> (and thereby fix thousands of others), or is it a genuine one-off that only
> human/LLM judgment can resolve?

**Always prefer the general fix.** The two biggest wins this project has had were
general, cascading code changes, each gated to 0 false positives:
- `fuzzy_surname` (dist-2 surname blocking) → +92 union from one change.
- `position_fuzz` (`_pos_norm` abbreviation + hyphen expansion) → **+1,146** union
  from one change.

Adjudication is the OPPOSITE: each case is read and judged individually and the
verdict fixes only that case. It is the **last resort**, for the irreducible
residue. Do not grind through it while generalizable patterns remain unharvested.

### The triage rule (apply on every batch)
While adjudicating, watch for a pattern repeating. **The moment a pattern recurs
~3+ times, stop and ask: could a deterministic rule (parser / matcher /
gazetteer) catch this class?** If yes, escalate it to a lever (build it, gate it
on `eval_known` = 0 FP, re-run the chain) instead of hand-confirming each
instance. A lever fixes the unseen thousands; an adjudication fixes one.

### Patterns observed so far, classified

**GENERALIZABLE (escalate to a deterministic lever — do NOT just hand-adjudicate):**
1. **Prose states the colony/office but the structured event wasn't place-attached.
   — DONE 2026-06-17a (+107 union, 0 FP).** Harvested as the `prose_colony` lever:
   `compile.recover_places_from_prose` attaches a mid-clause gazetteer colony the
   parser (last-segment-only) missed. Smaller than hoped (3,755 recovered but only
   ~122 had a matchable record — the rest are colonial politicians/local officials
   not in the imperial staff lists). `measure_prose_colony.py` is the harness. Do
   NOT re-adjudicate this class by hand.
2. **Ambiguity guard over-drops. — DONE 2026-06-16d (+533 union, 0 FP).** Harvested
   as the `ambiguity_guard` lever (see LOOP_HANDOFF "Already done"): `match._disambiguate`
   now keeps duplicate-bio-fragment contests and same-official re-listings, and prunes
   loose initial-deficient namesakes (tight-beats-loose, which also kills the de Kretser
   FP). Do NOT re-adjudicate `ambiguity_drop` cases by hand — the class fell 9%→2% and the
   residue is genuine different-person contests / single-initial bios. `measure_ambiguity.py`
   is the harness if you want to re-inspect.
3. **Territory-label evolution.** One role recorded under Rhodesia / Southern
   Rhodesia / South Africa (Newton), or Malaya sub-states, etc. Candidate lever:
   gazetteer aliasing (some already done — see `colony-inference-built.md`).
4. **Position abbreviations / hyphens.** ALREADY shipped (`position_fuzz`). The
   stale queue still contains cases this now solves — see step 1 below.

**GENUINE ONE-OFFS (hand-adjudication is the right tool):**
- Upstream **mis-colonied** staff-list records (Micallef: Malta offices filed
  under "Leeward Islands"/"Virgin Islands"). A data defect, case-specific.
- Same-initial, same-surname, DIFFERENT-career namesakes (Logan: administrator
  W.M. vs forester W.E.M.; Saunders: Ceylon administrator vs Jamaica doctor vs
  S.Australia police). Rejecting these needs reading the careers.
- **No-match** bios (McLeod: a P.E.I. provincial premier absent from the imperial
  staff lists; every candidate is a different McLeod).
- **Name-rendering unification** of one person (Caron "Adolphe" + "J.P.R.A.";
  Grannum "A." + "E.A."; Sukuna ±"Ratu"). Partially generalizable but FP-risky;
  safer to confirm by hand.
- Career ambiguities (Azopardi 1922: a demotion + military rank — same man or a
  relative?).

**Bottom line:** the residue is a MIX. Roughly a third of the current queue
smells generalizable (patterns 1–2 above). Harvest those as levers first; the
rest are true one-offs for adjudication.

---

## 1. ALWAYS regenerate candidates/dossiers first (the queue goes stale)

The adjudication queue is a snapshot of what the matcher COULDN'T do at the time
it was built. Every deterministic lever shipped since then shrinks the real
queue. The current `data/services/adjudication/` was built 2026-06-12, **before**
this session's `fuzzy_surname` + `position_fuzz` levers — so it contains cases
the matcher now auto-resolves. Before adjudicating, rebuild:

```bash
cd ~/col_matching && export COL_USE_AUGMENTED=1   # ALWAYS export this first
# re-run the deterministic chain so candidates reflect the current matcher:
python3 -m col_match.services.cli compile          # if parser/dedup changed
python3 -m col_match.services.cli augment_officials
python3 -m col_match.services.cli infer_colony
python3 -m col_match.services.cli attach
python3 -m col_match.services.cli match
python3 -m col_match.services.cli eval_known        # MUST be 0 FP
python3 -m col_match.services.cli candidates        # enumerate below-bar pairs
python3 -m col_match.services.cli dossiers          # build cases.jsonl + dossiers/*.md
```
Regenerating preserves verdicts already written in `verdicts_raw/` whose
`case_id` still exists; stale ones become harmless "unknown case_id"
parse_failures at compile.

---

## 2. Calibrate before publishing (mandatory, do once per matcher change)

The gate: **0 confirm-tier false positives** against the 543 known careers.
```bash
python3 -m col_match.services.cli calib_build       # blind cases + hidden labels.json
# adjudicate the calib dossiers exactly as production (below), then:
python3 -m col_match.services.cli adjudicate_compile --calib
python3 -m col_match.services.cli calib_score        # exits 1 if gate fails
```
A prior session + this one validated the loop: precision 1.0, 0 FP, ~65% recall.
`gen_calib_pilot_verdicts.py` shows the calib verdict format.

---

## 3. Pick high-value cases (ranking)

Single-bio, uncontested, strong-dimension cases are the safest, highest-yield.
Ranking heuristic used (surfaced 763 such cases):
- un-adjudicated AND single biography (no inter-bio contest) AND not CONTESTED,
- has a strong dimension: `position_sim ≥ 60` OR `honour` PASS,
- score = `position + 30*honour + 15*n_stints + 8*n_honours − 25*single_initial`.

See the inline python in the session transcript / `adjudication-harness-state.md`
for the exact scan. Senior officials (many honours, long multi-colony careers)
are the richest — one confirm can recover 3–6 stints.

---

## 4. Read each dossier and decide (the core protocol)

A case = one connected bio↔stint component. For each case:

1. **Read the biography PROSE** (verbatim entry text), not just the structured
   timeline. The prose routinely states the colony and office that the structured
   events dropped — that is where most recoveries come from.
2. **For EACH candidate stint, decide independently** whether it belongs to this
   bio. A bio may own some stints and not others. Check: surname (allow OCR
   garble), initials/forename as an ordered subsequence, colony, tenure overlap,
   position match (read abbreviations: `asst. supt.`=`Assistant Superintendent`),
   shared honour, edition co-occurrence, and hard chronology (no service before
   birth+15 or after death).
3. **Unify name renderings of one person** under one bio (Caron Adolphe/J.P.R.A.).
4. **Reject namesakes**: different colony + different career + different middle
   initial usually means a different person. When two bios could plausibly hold
   one stint, assign it to NEITHER.
5. **No-match is a valid verdict.** If every candidate is a different person,
   assign nothing (see §5 "no-match").

**The prime directive: NO FALSE MERGES.** A missed link is recoverable; a wrong
one corrupts the record. When genuinely unsure, leave it unassigned / mark
`probable` (→ review), not `certain`.

---

## 5. Write the verdict JSON (+ an independent second pass)

Write `data/services/adjudication/verdicts_raw/{case_id}.json` AND an independent
`{case_id}.pass2.json`. **`confirm` requires the pass2 to assign the same stints
to the same bio at `certain`** — no agreeing pass2, no confirm (it drops to
review). Copy the exact format from `gen_prod_slice{,2,3,4}_verdicts.py`.

Schema (`schema.Verdict`):
```json
{
  "case_id": "...",
  "persons": [{
    "bio_id": "...",
    "stint_ids": ["...only the stints you verified..."],
    "confidence": "certain | probable | uncertain",
    "arguments_against": "the strongest case this is WRONG (mandatory, substantive)",
    "evidence_cited": [{"stint_id": "...", "year": 1888, "fact": "verbatim string from the dossier"}],
    "would_overturn": "what new evidence would reverse this"
  }],
  "unassigned_stints": [{"stint_id": "...", "reason": "why not assigned (namesake / anomaly / weak)"}],
  "duplicate_bio_groups": [],
  "notes": "..."
}
```
- `confidence` maps: certain→confirm, probable→review, uncertain→unlinked.
- **Cited `fact` MUST appear verbatim-ish in the dossier** (fuzz.partial_ratio ≥ 92)
  — it's an anti-hallucination guard. Cite stint-record position strings or exact
  bio phrases. Never cite the bare surname (it's the blocking key; stripped).
- For a **no-match** case: `"persons": []` + a `notes` explaining; all stints
  auto-unlink.

### GOTCHA — single-initial biographies (e.g. "George", "William", "R.")
The `single_initial` guard demotes the WHOLE person to review if ANY assigned
stint lacks an independent strong dimension (position ≥ 60 / shared honour /
≥2-edition co-occurrence). So for a single-initial bio, **assign ONLY stints that
are each individually strong**, and route weak-but-likely-same stints to
`unassigned_stints` (review). Otherwise one weak stint drags a solid confirm down
to review. (Berkley: assigned only the Leeward governorship (position 100 +
C.M.G.); the St Vincent roster stint → unassigned.)

---

## 6. Compile, verify, and what the guards do

```bash
python3 -m col_match.services.cli adjudicate_compile        # production
# (--calib for the calibration set)
```
Output: `verdicts.jsonl`, `review_queue.jsonl` (ranked by seniority),
`merge_review.jsonl`, `reports/adjudication_report.md`. The compiler re-applies
deterministic guards and DEMOTES anything that fails — the model never gets the
last word:
- `unknown_pair` — assigned a stint that isn't a gate-enumerated candidate → stripped.
- `age_gate` — re-checked from the graph cache.
- `citation` — cited fact not in dossier → demote.
- `blocking_key` — surname-only citation stripped.
- `single_initial` — see gotcha above.
- `contested` — comparable-strength competitor in-case → can't confirm.
- `second_pass` — confirm needs an agreeing `certain` pass2.

After compiling, verify your cases landed as intended:
```bash
python3 -c "import json;[print(r['tier'],r['case_id'],len(r['stint_ids']),r['guard_trace']) for r in (json.loads(l) for l in open('data/services/adjudication/verdicts.jsonl')) if r['bio_id'] and r['case_id'] in {YOUR_CASE_IDS}]"
```
A `guard_trace` of `[]` on a `confirm` means a clean, fully-corroborated link.

---

## 7. Output discipline (hard constraints)

- **NO writes to the production Neo4j graph. No SAME_AS.** Confirmed careers are a
  files-only store (`verdicts.jsonl`), per `docs/data_contract.md`. The graph is
  READ-ONLY with quarantine filters.
- **NO metered LLM APIs without Jim's sign-off. NO GEMINI** (banned — cost
  overrun). In-session Claude Code adjudication is $0 and the chosen method; any
  paid backend needs a printed capped estimate + a hard abort + a token ledger.
- Adjudication confirms feed the SEPARATE careers store; they do NOT change the
  deterministic "matched union" percentage (that's stint_matches ∪
  record_attachments). Report them as their own number.

---

## 8. Status (update this when you work)

- Calibration: gate passing, 0 FP, precision 1.0.
- Production: ~67 / 5,813 cases adjudicated (31 confirm / 60 stints) as of
  2026-06-16. ~5,446 remain — BUT regenerate the queue first (§1); the post-lever
  matcher will have shrunk it. Generators for reference:
  `gen_prod_slice{,2,3,4}_verdicts.py`, `gen_calib_pilot_verdicts.py`.
- Throughput is bounded by careful per-case reading; this is a many-session
  effort. Prioritise §0 (harvest generalizable patterns as levers) to shrink it.
