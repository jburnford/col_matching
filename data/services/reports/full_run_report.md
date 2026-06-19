# Services-section pipeline — full-run report (2026-06-11)

Status: COMPLETE. (The pro batch stalled in Google's queue and was cancelled;
the 967 escalations ran interactively on gemini-pro-latest instead, 16 workers,
capped thinking.) Total LLM spend: ~$6-7.

## Pipeline results

| stage | result |
|---|---|
| Segmentation | 62 volumes, 199,099 raw entries; bounds verified against known headers; 1952 correctly detected as section-less (its preface confirms) |
| Cross-edition dedup | 42,231 distinct entry-versions (4.7×) |
| Rules parse | 32,522 (77.0%) accepted deterministically |
| LLM parse (flash batch + pro escalation) | 9,094 / 9,710 accepted; 616 hard failures to hand review (self-contradictory printed data, career-less stubs) |
| Compile | **30,415 individuals** (11,075 cross-version + 125 record-co-claim merges) |
| Record attachment (primary) | **18,244 record-year attachments**, 5,485 bios, 6,207 stints' records |
| Stint matching (cross-check) | 6,799 stints matched |

## Precision (543 hand-verified careers incl. hard negatives)

- **Stint-level: 0 false positives** (173 careers touched; 18 multi-stint
  careers consistent; the single "inconsistency" is a verified ground-truth
  error — Woodall, J. G. mis-named upstream).
- **Record-level: 0 false positives** (142 careers touched).
- Gold set: surname/given names 27/27, event recall 100%, precision 92–99%
  by tier; ~1 entry still pending (pro batch).
- Twin check (1,172 double-printed pairs): OCR flips a year digit
  ~1.7%/year/reading → year-voting flags minority readings at compile.

## Architecture (inverted per Jim, validated)

Person = biography. Careers are built by per-edition record attachment: a
biography attested in edition Y predicts (colony, position) at Y and claims
that volume's staff-list record directly, bypassing the stint layer's known
defects. Stint matching is retained as an independent cross-check (the two
agree at 0 FP each). Bios co-claiming records are residual OCR-variant
duplicates — fed back into compile as merge evidence (with guards so the
upstream stint over-grouping can't propagate in).

## Matching rules that survived adversarial testing

Every rule below was added or killed based on measured false positives
against the hard negatives:

1. No bare tenure-overlap path: every match needs a strong dimension
   (position ≥60 / shared honour / ≥2-edition co-occurrence).
2. Edition co-occurrence requires currency (posting not stale at year Y) and
   respects terminal years (honoured retirees stay listed).
3. Hard age gate: no stint may start before birth+15 or after death.
4. Fuzzy-OCR surname candidates need the strong bar AND never displace an
   exact-surname match.
5. A fact used as a blocking key is never reused as a merge anchor.
6. Single-initial namesakes never merge via shared-stint evidence (the
   "J. Lewis" trap).

## Coverage and what it means

- 6,799 / 67,952 stints (10.0%) auto-matched; 18,244 record-years with
  line-level provenance.
- POSSIBLE_MATCH components: **801 directly adjudicable** (≥2 stints, same
  biography), 2,183 partially covered, 8,750 untouched.
- Coverage skews senior (36% of governor-class stints vs 5% of clerk-class) —
  a matching-difficulty effect, not data scope: generic junior titles fail
  the conservative bar by design.
- The recoverable frontier: ~13k bios with candidates below the evidence bar
  + ~6.5k bios with no explicitly-placed event. Since biographies and staff
  lists come from the same printed volumes, near-complete linkage for
  1883+ colonial-establishment careers is the right target — via dossier
  adjudication (Phase 3), not threshold loosening: every loosening attempt
  in this run produced measurable FPs and was reverted.

## Structural limits on 100%

- Colonial Office / Dominions Office home staff: no colony stints exist.
- Pre-1883 retirees: no services section existed before 1883.
- Post-war scope narrowing: 1948+ sections cover "Senior Officers" only.

## Artifacts

- `data/services/biographies/biographies.jsonl` — 30,145 individuals,
  per-fact edition provenance
- `data/services/matches/record_attachments.jsonl` — record-level careers
- `data/services/matches/stint_matches.jsonl` — stint cross-check
- `data/services/reports/coverage.{md,json}` — coverage breakdowns
- upstream bug reports to file: Woodall 1961 stint mis-named; Gold Coast
  1946/48 Guggisberg ghost records unquarantined; known_careers Q6264790
  wrong grouping
