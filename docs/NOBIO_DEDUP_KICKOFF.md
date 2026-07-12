# Session kickoff: IOL no-bio dedup — a measured person table for the roster-only 34k

Copy-paste prompt for a fresh session:

---

Deduplicate and identity-QA the IOL NO-BIO population (July 2026). Read
`~/.claude/.../memory/iol-identity-qa.md` and
`~/col_matching/docs/NOBIO_DEDUP_KICKOFF.md` first — corpus facts,
gotchas, and the queued work are all there. Build, don't re-explore.
You can ssh to nibi directly (scp/sbatch/squeue); the public site
(GitHub Pages off docs/) is FROZEN — no media/page pushes.

## State you inherit (col_matching @ HEAD, all pushed)

- Bio person table: **19,513 canonical persons** (audited, overlaid,
  check green — `iol_identity_check.py` baselines 30,252/10,739/19,513).
- No-bio census BUILT (`iol_nobio_census.py`, outputs in
  data/iol/identity/): **34,321 roster-only individuals** =
  19,849 civil person-chains (`nobio_civil_chains.jsonl`; unlinked
  civil records collapsed on (surname, initials, government), 8-year
  gap-split) + 14,984 unlinked gradation identities (9,044 army) − 512
  measured overlap. 9,681 unusable-name records excluded (floor).
- Cross-layer linkers live: civil→person (`iol_link_civil.py`, 38,552
  links, tiered strong/standard/weak), gradation→person
  (`iol_link_gradation.py`), exits (`iol_link_exits.py`,
  override-ledger-aware), rolls (`iol_link_rolls.py`, 99% agreement).
- The COL reference implementation for measuring "never-bio'd" lives in
  `data/volume/classc/` (CLASSC*.md + career_classes_measured.jsonl):
  class A (no compatible bio) / B (namesakes incompatible) / C
  (compatible namesake → pairwise LLM adjudication, deterministic
  gates). Mirror it.
- Nibi worker fleet in `nibi/`: qwen_classc_worker.py (modes link/
  merge/ioldedup/iolexit/iolroll/iolbirth), qwen_struct_worker.py,
  qwen_civil_parse_worker.py; slurm patterns qwen_iol_adjudicate/
  _struct/_deltadedup.slurm. All resumable via --out.

## FIRST: apply the pending micro-batch

Job **17542883** is queued behind NibiMaintenanceJuly (ends
**2026-07-13 12:00 EDT**) and runs automatically after. When done:
`scp 'nibi:~/projects/def-jic823/qwen_roster/res_*.jsonl'
data/iol/identity/adjudicate/` → `python3 iol_apply_adjudication.py` →
converge (map apply → stage3 apply --overlay → emit → linker rerun →
apply again until 0 appends) → screens → check → baselines in-commit.
Pools: a6 7, a7 4, exitamb 266 (most resume-skip), roll 25, a2 8,
civil 522 lines.

## The no-bio dedup, in order

1. **Within-population unification.** The 19,849 civil chains and
   14,984 gradation identities describe overlapping people three ways:
   chain↔chain across governments (transfers), chain↔gradation
   (the 512 name-key overlap is a floor — corroborate on entry year /
   establishment / corps), and chain↔casualty exit events (the 1861-85
   deaths whose linker residue awaits the gradation spine). Determinist
   keys first (covenant/commission year is gold), LLM residue on Nibi.
2. **A/B/C classification against the bio table** (the COL method):
   for every no-bio identity, find name-compatible bio persons; class A
   none / B era-or-place incompatible / C compatible → render C pairs
   for `--mode link`-style adjudication (roster career vs biography —
   the COL prompt nearly fits; add an ioln obio mode if needed).
   Verdict "same" → it WAS a bio person the linker missed (link it);
   "different" everywhere → measured no-bio. This turns the census
   estimate into a measured number with a precision statement.
3. **Chain-identity sampling.** Are the chains one person each?
   Stratified sample (initials-only vs fuller names × surname
   frequency × government) → Nibi judge → Wilson CIs, the
   iol_merge_measure.py pattern.
4. **Product**: `data/iol/identity/nobio_persons.jsonl` (canonical
   no-bio table with provenance to civil/gradation/casualty records),
   census + dashboard update (artifact
   https://claude.ai/code/artifact/d819b089-ed92-46ca-b805-d4da9ba38b61
   — republish with url= from the new conversation), extend
   iol_identity_check.py with no-bio baselines in the same commit.

## Gotchas that will bite

- `kg_textchain_dedup.py --write` and friends take CWD-RELATIVE paths;
  always pass full data/iol/ paths and `wc -l` the target after.
- Ledgers append-only + ACCUMULATIVE; regenerating fresh REVERTS fixes.
  Screens run post-apply; baselines change only in the rebuild commit.
- Worker resume is keyed on ids in --out: stale results for changed
  inputs must be evicted from the RESULTS FILE ON NIBI before rerun.
- Deterministic fingerprints outrank single judged verdicts (the
  honour-key and Nagpur/Cent.Provs precedents).
- Civil-list office field: `ditto_resolved` records are trustworthy;
  `llm_reparse` records carry re-parsed holders; residue flags in
  `iol_civil_residue.py` (522 lines still unfixed).
- 5 monster bios (170-330KB accumulator run-aways) remain
  unstructurable; a continuation-run cap in iol_bios is queued.
- 1918 re-OCR: blocked on the user locating the source scan.
- Public site frozen (memory: public-site-frozen) — viz to the private
  artifact or viz_private/, never docs/ media.

---
