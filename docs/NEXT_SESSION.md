# Next session — adjudicating the residual matches

Copy-paste prompt for a fresh session (state as of 2026-06-11 night; all
numbers verifiable from the artifacts listed at the bottom).

---

We are linking ~30k printed biographies of British colonial officials to the
annual staff-list records in a production Neo4j graph. **Prime directive: no
false merges.** A missed link is recoverable; a wrong one silently corrupts
the historical record. Every matching decision must be validated against the
hand-verified careers (see "Validation harness") before it ships.

## What exists (Phase 1, complete)

The repo `~/col_matching` (`col_match/services/`, CLI `col-services`) parses
the "Record of Services" biographical sections of the Colonial Office Lists
(1883–1966, raw olmOCR at `~/colonialofficelist/historical_document_pipeline/
processed_pdfs/`) and links them to the graph:

- **30,415 individuals** compiled from 199,099 printed entry-instances
  (`data/services/biographies/biographies.jsonl`), with per-fact edition
  provenance and OCR year-voting flags.
- **Careers are built by record-level attachment** (the architecture Jim
  chose): a biography attested in edition Y predicts (colony, position) at Y
  and claims that same volume's staff-list record directly
  (`attach.py` → `data/services/matches/record_attachments.jsonl`,
  18,244 record-years). The upstream stint layer (`COL_Official`) has known
  defects (ghosts, dual assignments, mis-named stints) and is only a
  cross-check (`match.py`, 6,799 stints) and audit surface.
- **Zero false positives at both levels** against 543 hand-verified careers
  including hard negatives.
- Coverage: 10% of the graph's 67,952 stints auto-matched; **801 of 11,731
  POSSIBLE_MATCH candidate components directly adjudicable** (≥2 member
  stints claimed by one biography); coverage skews senior because generic
  junior titles fail the conservative bar by design, not because juniors are
  absent from the sections.

## The remaining problem (this session's focus)

Both record types come from the *same printed volumes*, so for any
colonial-establishment career 1883+ the linking evidence physically exists.
The residue, in order of value:

1. **~13k biographies with same-surname candidates below the evidence bar**
   (generic positions, several same-name candidates). Plan: Fable dossier
   adjudication — serialize the biography + each candidate stint's record
   evidence + corpus context into one dossier, adversarial prompting, tiered
   verdicts (confirm / review-queue / leave-unlinked). Jim accepts hundreds
   of human-review cases; target ≈99.5% precision on the confirmed tier,
   calibrated on the known-careers set before anything is published.
2. **~6.5k biographies with no explicitly-placed event** — infer the colony
   from departments/positions/context first, then adjudicate as above.
3. **~1,080 ambiguity-dropped stint candidates + 44 residual record
   co-claim pairs** — already-identified contests needing case-by-case
   adjudication.
4. **616 hard-failure entries** (`data/services/failures/`,
   `llm_escalate.json`) — self-contradictory print or career-less stubs;
   build the hand-review export.
5. Adjudicate the 801 ready components into published career chains; design
   the output/export format (NO writes to the production graph, no SAME_AS —
   files / separate store only, per `docs/data_contract.md`).

## Validation harness (re-run after ANY matching change)

- Known-careers FP test: `~/textasdatacolonialofficelist/ml_data/
  known_careers.json` (543 careers, positives + `different_persons` hard
  negatives) — the FP count must stay 0; one known GT error (Q6264790
  Woodall: the 1961 Bermuda stint is actually J. G. Woodall, mis-named
  upstream).
- Gold set: `col-services eval_gold` (28 blind-annotated entries).
- Twin check: `col-services check_twins` (OCR error bound: ~1.7%/year/reading).

## Hard-won matching rules (each forced by a measured FP — do not relax)

1. No bare tenure-overlap matches: every match needs a strong dimension
   (position ≥60 after abbreviation expansion / shared honour / ≥2-edition
   co-occurrence).
2. Edition co-occurrence needs currency (posting not stale at year Y) and
   respects terminal years (honoured retirees stay listed after retiring).
3. Hard age gates: no stint before birth+15 or after death.
4. Fuzzy-OCR surname candidates need the strong bar and never displace an
   exact-surname match.
5. A fact used as a blocking key is never reused as a merge anchor.
6. Single-initial namesakes never merge on shared-stint evidence (the
   "J. Lewis" trap).

## Practicalities

- Graph: bolt://206.12.90.118:7687, READ-ONLY, quarantine filters mandatory
  (`docs/data_contract.md`); local cache already at
  `data/services/graph_cache/` (refresh with `col-services fetch_graph`).
- **NO GEMINI — DO NOT USE** (Jim, 2026-06-12): Phase 1's Gemini usage cost
  ~$100 against a sub-$10 estimate (the "~$6–7" figure previously recorded
  here was wrong), and the API key is dead. No metered LLM APIs at all
  without Jim's explicit sign-off; adjudication runs in-session via Claude
  Code. Any future API backend needs a printed pre-submit cost estimate, a
  hard spend cap that aborts, and a persistent token/cost ledger.
- Reports: `data/services/reports/{full_run_report,pilot_report,coverage}.md`.
- Upstream bugs to report to col_pipeline when convenient: Woodall 1961
  stint mis-named; Guggisberg Gold Coast 1946/48 ghost records unquarantined;
  known_careers Q6264790 wrong grouping.

Suggested first step: build the dossier serializer (biography + candidate
stints + records + Phase-2 annotations → one readable document), pilot Fable
adjudication on ~50 below-bar cases stratified by seniority, calibrate
against known careers, then scale.
