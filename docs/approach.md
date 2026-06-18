# Approach — building reliable career chains

## Architecture inversion (agreed 2026-06-11, evening)

Jim's reframe, validated by prototype: **the biography is the person; careers
are built by attaching annual records directly to biographies**, year by
year — for each edition a biography is attested in, it predicts (colony,
position) in that same volume's staff lists, and the matching
`COL_PersonRecord` is claimed directly (`col_match/services/attach.py`).
The upstream stint layer (`COL_Official`) is demoted from match target to
corroborating evidence + audit surface: it has measured defects (unquarantined
ghosts, dual-assigned stints, mis-named stints, surname+initial over-grouping)
that record-level attachment bypasses. Stint-level matching (`match.py`)
remains as an independent cross-check, and the stint residue (people never in
any services section: pre-1883 retirees, juniors) stays for later phases.

Prototype results (same conservative gates, zero false positives on the 543
hand-verified careers at both stint and record level): 18,212 record-year
attachments, 5,599 bios, 6,194 stints touched, only 10 record-ambiguity
drops. Bonus: bios co-claiming the same record are residual OCR-variant
duplicates — the attachment stage doubles as a duplicate-bio detector and the
shared-record signal should feed back into compile as a merge anchor.

## Original decisions (2026-06-11, morning):

- **Scope:** adjudicate *all* 25,623 `POSSIBLE_MATCH` edges (~11,700 connected
  components), ignoring the existing `uncertainty`/`ml_*` scores as gates. The
  production ML model was trained on 25 positive pairs; its scores are
  candidates' provenance, not evidence.
- **Precision goal:** ~99.5% on the confirmed tier, but the final publication
  cut is deferred — build calibrated tiers, measure precision per tier on held-
  out gold, decide then.
- **Human review:** capacity for hundreds of middle-tier cases exists; design
  for a ranked review queue with readable dossiers.
- **Asymmetry is the design principle:** a missed link is recoverable; a false
  merge silently corrupts the record. Every default resolves ties to *no merge*.

## Why the problem is reshaped by the services sections

The printed Colonial Office List itself contains a cumulative biographical
section — "RECORD of the Public Services of Officers…" — giving full given
names, dated appointment-by-appointment careers (including cross-colony moves),
honours with award years, and sometimes birth years. Verified present in the
1896 OCR (`~/SSHRC_demo/ColonialOfficeList1896.md`, lines 37540–~44600, roughly
3,500 entries). Example (Ackroyd, E. J.): Mauritius 1853 → Hong Kong registrar
1881 → puisne judge 1892 → retired 1895 — exactly the cross-colony chain the
stint-linking problem struggles to infer, printed as fact by the source itself.

This converts much of the task from *inference* ("are these two stints
plausibly one person?") to *citation* ("the 1896 List states this person served
in Mauritius, then Hong Kong"). It also fixes the gold-data bottleneck: the
existing labeled set has only 200 positives; a few thousand parsed service
records yield orders of magnitude more verified careers for calibration.

**Status — corpus inventory (verified 2026-06-11):** the full raw olmOCR
corpus is local at
`~/colonialofficelist/historical_document_pipeline/processed_pdfs/`
(85 volumes: COL 1867–1966, Commonwealth Relations Office List 1951–65,
Dominions Office List 1935; one `olmocr_results.md` per volume). The services
section is present in **every COL edition from 1883 through 1966** except the
slim 1946 restart (the 1948 preface confirms biographical notes were dropped
in 1946 and restored in 1948); pre-1883 editions never had it. Headers vary
("RECORD of the Public Services…", "RECORD OF SERVICES", none in 1966) so the
parser must detect entries by shape (`SURNAME, Names[, honours].—b. ….;
dated events…`), not by header. ~1,400–2,900 entries per edition ⇒ on the
order of 100k entry-instances, deduplicating to roughly 10–20k distinct
persons. Caveats seen so far: 1939 prints each entry twice (dedupe needed);
OCR quality is high (the 1930 Guggisberg entry is near-perfect).

## Pipeline

### Phase 0 — Evaluation harness first

- Freeze `~/textasdatacolonialofficelist/ml_data/ground_truth_pairs.csv`
  (200 pos / 1,445 hard-neg / 458 anchors) as **eval-only**. Nothing trains on
  it; nothing in the pipeline sees its labels.
- Primary metric: pairwise precision of the confirmed tier, computed over the
  person-partition (every pair of stints placed in one person counts).
  Secondary: recall, and per-tier precision with binomial CIs.
- Resolve the 10 documented ground-truth conflicts (same stint claimed by two
  sources) before treating the file as gold.

### Phase 1 — Services-section extraction

1. Locate the services section in each available raw volume (header regex +
   structure: `SURNAME, GIVEN NAMES[, honours].—dated career…`).
2. Parse entries into structured careers: name, honours(+years), birth year if
   present, ordered (date, position, colony) events. LLM-assisted parsing is
   fine here — errors are caught downstream because a service entry only acts
   when it *corroborates* graph records.
3. Match each service entry to `COL_Official` stints by surname + given-name
   compatibility + (colony, year-window) alignment of its dated events against
   the stint's annual records. Require multi-point alignment (≥2 independent
   colony/year/position agreements) before accepting a match.
4. Output: `service_career` objects, each linked to ≥1 stint, used twice —
   as direct high-confidence chain evidence in adjudication, and as an
   expanded calibration set.

### Phase 2 — Deterministic screening (no model)

Run over every candidate component before any LLM sees it:

- **Kill rules** (sever an edge outright): multi-year concurrent full-time
  service in different colonies (outside known federation/dual-listing
  contexts); contradictory *full* given names (initials never kill, full names
  can); career span exceeding plausible bounds (~55 years end-to-end);
  temporal impossibilities (stint B "continues" a record contradicted by
  stint A's overlapping records).
- **Ghost-stint detector**: the upstream `governor_chain_ghost` quarantine is
  incomplete — verified 2026-06-11: Guggisberg's British Guiana 1946/48
  records are quarantined but his Gold Coast 1946/48 records are not, despite
  his death in 1930. Flag stints that look like retrospective governor lists
  (long gap to the rest of the component, position = Governor, late editions,
  contradicted by a services entry's retirement/death date) rather than
  trusting the quarantine flag alone. Report instances upstream to
  `col_pipeline`.
- **Positive-evidence inventory** (annotate, don't decide): full-name match,
  honours/qualification/military-rank continuity, salary/position succession
  across the boundary (a_last vs b_first), services-section corroboration,
  edition interlocking (A's missing years are B's present years).
- **Surname-frequency prior** computed from all 68,335 stints. The evidence
  bar scales with name commonness: "Metzger" + plausible succession may
  suffice; "Lewis, J." requires an identifying discriminator. Note the corpus
  is honours-sparse (3% of records) and ~88% of given names are initials-only,
  so career-shape evidence (position/dept/salary trajectories, 97–98%/69%
  coverage) carries most decisions.

### Phase 3 — Fable adjudication over dossiers

- **Dossier serializer** (`col_match/dossier.py`, to build): one component →
  one compact chronological dossier. Per stint: years, colony, year-by-year
  position/department/salary, honours/quals/military rank, name forms as
  printed. Plus: surname frequency, Phase-2 annotations, matched service
  entries, and the candidate edges' structural facts (gap years, editions
  missed). No upstream scores.
- **Task framing: partition, not edge accept/reject.** The output is a
  partition of the component's stints into persons (the "J. Lewis" component
  is several people plus residue). Adversarial prompt: argue *against* each
  merge before concluding; surname+initial alone is stated as insufficient.
- **Structured verdict** per proposed person: member stints, confidence,
  cited evidence (specific records/years), and what evidence would overturn
  it. Borderline components get multiple independent passes; disagreement
  demotes to the review tier.
- **Tiers:** `confirmed` (auto, publishable subject to Phase 4 calibration) /
  `review` (ranked queue, human decides) / `unlinked` (insufficient — the
  default). Rank review cases by historical value: career length, cross-colony
  span, seniority.

### Phase 4 — Calibration and outputs

- Score the pipeline on held-out gold; map model confidence → empirical
  precision; place the confirmed-tier cut to meet the precision goal with CI.
- Re-adjudication of all components doubles as an audit of the existing
  `COL_Person` layer (which has 23 stints assigned to two persons).
- All outputs to files / a separate store. **No writes to production**, no
  `SAME_AS`, per the data contract. Review-queue export format designed for a
  human reader; a small review UI is optional later work.

## Order of work

Phase 0 and the Phase-2 screener are independent and start immediately.
Phase 1 starts with the 1896 volume now and widens as raw OCR for other
editions arrives from Nibi. Phase 3 prompts are developed against gold
components early, but the production adjudication run waits for Phase 1
output, since service entries materially raise both adjudication quality and
calibration power.
