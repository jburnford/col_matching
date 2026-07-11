# Session kickoff: India Office List identity QA

Copy-paste prompt for a fresh session:

---

We're extending the Colonial Office List identity-QA work (July 2026) to
the **India Office List corpus**. Your first job is exploratory: dig
through the IOL documents and data layers, learn precisely how this
corpus is similar to and different from the COL, and write up what you
find before adapting any code. Read
`~/col_matching/docs/IDENTITY_QA_ROADMAP.md` and
`data/volume/identity/B1_MEASURED.md` first for the COL methodology and
its results; the memory files cover the rest of the context.

## Where everything lives (all in ~/col_matching)

- **OCR**: `iol_ocr_1860-1940/` — 139 editions in decade dirs
  (`1860s/`…`1940s/`). One subdir per edition; the publication was
  renamed repeatedly, so directory prefixes are era-dependent: `iacsl_`
  (Indian Army & Civil Service List, 1861+), `il_` (India List,
  1882–95), `iol_`/`iliol_` (India Office List families; see
  `data/iol/edition_sources.jsonl` for duplicate-volume collapse).
  Early editions are SEMIANNUAL (`_jan`/`_jul`, plus `_supp`).
- **Format gotcha**: unlike the COL's `result.json` layout blocks with
  bboxes, each IOL edition is a FLOWED MARKDOWN file (`<edition>.md` +
  `.html` twin + page-level `<edition>_metadata.json` with token counts
  only). `col_match/volume/iol_reader.py` and `iol_bios.py` are the
  existing readers — read their docstrings before anything else.
- **Extracted bios**: `data/iol/bios/` — 123 edition files, 258,103
  bios, plus `.xref.jsonl` siblings (check what the xrefs are).
- **Existing person identity**: the stage-3 dedup layer in `data/iol/`
  (`dedup_stage3_merge_map*.jsonl` — base + crossform + school +
  roleyear variants, held edges, verdict files). This is the old
  LLM-dedup person table used for the mobility videos
  (`build_iol_mobility_global.py`, `compute_transfers_iol.py`). Its
  precision was never measured — that is the COL B1 story all over
  again, and measuring it is the main prize.
- **Education layer**: `data/iol/education_parsed.jsonl` (see
  `docs/PARSE_IOL_EDUCATION.md`).

## Questions your exploration must answer

1. What sections do the markdown editions actually contain
   (gradation/civil lists? a Record of Services? honours rolls?), and
   how consistently across the four publication families? The roster
   layer was never parsed — assess how hard a gradation-list parser
   would be and whether sections are even separable in flowed markdown.
2. IOL bio schema vs COL bios (`data/volume/col*/bios.jsonl`): events,
   places, birth years, honours — what maps 1:1, what's missing, what's
   extra? Are birth years as OCR-fragile as the COL's? Do IOL bios
   carry the Indian orders (C.S.I./C.I.E. ladders are already in
   `volume_identity_screens.py`)?
3. How does the dedup merge map key persons, and what would a
   stratified precision audit look like (strata by surname frequency,
   name completeness, evidence class — mirror `volume_link_audit.py`)?
4. Rupee salaries: COL analysis converts Rs at 15:1 flagged
   (`list_vs_bio_v2.py`); how do IOL salaries print?
5. Cross-corpus: how many people plausibly appear in BOTH corpora
   (India->colonial career moves)? Honours + birth year + full names
   are the join keys.

## What transfers from the COL work (reuse, don't reinvent)

- Tier-A screens: `volume_identity_screens.py` (A1 honours precedence,
  A2 age invariants + birth-year OCR repair protocol 1-digit ->
  2-digit -> dynastic, birth-from-honour parser-bug signature, A6
  honour duplicates), `volume_identity_screens2.py` (A3-A5).
- Fail-loud invariants with measured baselines:
  `volume_identity_check.py` pattern.
- Nibi adjudication harness: `nibi/qwen_classc_worker.py` (pair format;
  `--mode merge` for person-vs-person), slurm pattern
  `nibi/qwen_b1_*.slurm`, ~14-16 pairs/s on one H100; ssh nibi works,
  worklists to `~/projects/def-jic823/qwen_roster/`.
- Ledger discipline: append-only decisions ledgers; override ledgers
  must be ACCUMULATIVE (screens run post-apply — regenerating fresh
  reverts applied fixes); absorbed-id resolution uses the survivor map,
  not the union-find root.
- Rules-first, LLM for residue; no agent fan-outs; commit+push as you
  go (github.com/jburnford/col_matching).

## Deliverables for the session

1. `docs/IOL_VS_COL.md` — the similarity/difference assessment, with
   evidence (read actual editions from several decades and all four
   families, not just one).
2. Adapted screens run on the IOL person table + an
   `iol_identity_check.py` with measured baselines.
3. A stratified Nibi worklist auditing the dedup merge map's precision
   (the measured number the IOL layer is missing).

Roster/gradation parsing is explicitly OUT of scope for this session —
assess it, don't build it.

---
