# Session kickoff: IOL consolidation — overlays, adjudication batch, cross-layer linkers

Copy-paste prompt for a fresh session:

---

Continue the India Office List work (July 2026). Read
`~/.claude/.../memory/iol-identity-qa.md` (the index memory) and
`~/col_matching/docs/IOL_VS_COL.md` first — they hold all corpus facts,
the measured numbers, and every gotcha. Everything below is queued work
with the analysis already done; build, don't re-explore.

## State you inherit (all pushed, github.com/jburnford/col_matching)

- Person table AUDITED + REBUILT: **19,351 canonical persons**
  (`data/iol/llm_struct_corpus.stage3.deduped.jsonl`, live map
  `dedup_stage3_merge_map.audited.jsonl`, census precision 87.6%,
  1,557 judged drops + 86 honour-key reinstatements applied).
  `iol_identity_check.py` is the fail-loud gate — keep it green;
  baselines change ONLY in the same commit as a rebuild.
- Roster layers extracted: civil lists 119,527 (1861–1947, `data/iol/
  civil/`), gradation 119,429 (1861–1919), honours rolls 81,435
  (1875–1937), casualties 18,178 incl. 7,720 deaths (1861–1948).
- Exit linker run: 4,504 links (`data/iol/identity/exit_links.jsonl`),
  A7 events-after-death = 15, ambiguous pool = 253.

## The work, in order

1. **One Nibi adjudication batch for ALL pending pools** (~700 pairs,
   minutes on one H100; worker `nibi/qwen_classc_worker.py --mode
   ioldedup`, slurm pattern `nibi/qwen_iol_full.slurm`):
   A7 events-after-death 15 + exit-ambiguous 253 + A6 residue 15
   (`a6_honour_duplicates.jsonl` on the REBUILT table) + the 282
   roll-vs-bio honour-date conflicts + ~100 A2 ambiguous birth repairs.
   Append verdicts to `merge_decisions.jsonl` (accumulative!) and the
   birth/death overlay ledgers.
2. **Overlay ledgers -> person table enrichment** (no re-dedup needed):
   death dates from `exit_links.jsonl` (2,058), the 516 unique roll
   dates onto undated bio honours, birth-year repairs (95 unambiguous
   one-digit from `a2_age_invariants.jsonl`). COL discipline: an
   ACCUMULATIVE overlay file the build consumes — never edit the table
   in place; rerun screens + check after, update baselines in-commit.
3. **Civil-list cleanup**: resolve the 1,513 Ditto offices (verified
   100% deterministic against the preceding office in-block); Qwen
   re-parse of the ~2,930 flagged records' raw_lines (~2k unique
   prompts) in the same Nibi job as (1).
4. **Cross-layer linkers** (the B2 payoff; mirror `iol_link_exits.py`):
   civil→person (measured baseline: 54% of 1935 names match exactly one
   person on surname+initials; office/department/year corroboration
   lifts precision), then gradation→person (extends careers to 1861 and
   catches pre-1886 deaths whose people have no bios).
5. **Later, as its own deliberate cycle** (invalidates the person
   table — do NOT mix with 1–4): bios fixes (1911/1930 services-section
   truncation fix = max-span heading rule; no-comma Indian-name
   headwords; re-OCR iliol_1918) + rechain + LLM restructure on Nibi;
   then downstream reruns (mobility videos, transfers, IOL↔COL 1947
   exodus join).

## Gotchas that will bite if forgotten

- Ledgers are append-only and ACCUMULATIVE; screens run post-apply, so
  regenerating a ledger fresh REVERTS applied fixes.
- The audited map supersedes the pass-variant maps — never union them
  (kg_remap_edge_layers is already patched; nothing else may glob
  `dedup_stage3_merge_map*`).
- `kg_education_worklist.py` hardcodes data/kg — for IOL use
  `kg_parse_education.py worklist`. Always `COL_KG_OUT=data/iol`.
- Section labels print as bare gap text between HTML elements in every
  layer; running headers ("X—continued") must consume without killing
  parser state.
- Deterministic fingerprints outrank single judged verdicts (the 117
  honour-key wrong-drops proved it) — rerun screens after every apply.
- Rerun `iol_link_exits.py` after any person-table change (the check
  pins A7 from its output file).

---
