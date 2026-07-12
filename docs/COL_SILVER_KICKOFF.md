# Session kickoff: COL no-bio silver standard — 200 hand-labeled careers

Copy-paste prompt for a fresh session:

---

Build a 200-item hand-labeled SILVER STANDARD for the COL (Colonial
Office List) never-bio'd population, mirroring the IOL one
(`data/iol/identity/nobio_silver.jsonl`, 200 items @52f3d31, built
2026-07-12). Read `~/col_matching/docs/COL_SILVER_KICKOFF.md` and the
memory file `iol-identity-qa.md` first. Build, don't re-explore. The
public site (GitHub Pages off docs/) is FROZEN — no media/page pushes;
unlinked method .md docs are the established exception.

## Why

The COL headline numbers — 27,511 bio persons, 134,433 measured
never-bio'd, 10,559 applied class-C links, the 216-226k combined
census — rest on a verification basis of only 34 closely-read pairs +
10 skeptic promotions (CLASSC_LINKS.md). The IOL silver standard is a
reusable labeled instrument (per-item verdict + evidence, ids joining
the machine outputs); COL deserves the same. KEY DIFFERENCE from the
IOL round: the COL judge verdicts ALREADY EXIST
(`data/volume/classc/classc_results.jsonl`, 29,596 pairs judged), so
judge-agreement rates come out the SAME SESSION — no GPU dependency.

## The instrument (mirror the IOL one exactly)

One file `data/volume/classc/nobio_silver.jsonl`, one row per item:
  {"id", "pool", "silver_verdict", "confidence", "evidence"}
- ids MUST match the existing machine outputs so results join directly
  (classc pair ids as in classc_results.jsonl; career_id for
  chain-coherence items).
- verdicts: same | different | unsure (pairs); confirm | reject |
  unsure (career coherence); junk (non-person careers).
- evidence: one sentence citing the deciding printed facts.
- FORCE-TRACK the file if the path is gitignored (`git add -f`) and
  scp a backup to nibi:~/projects/def-jic823/qwen_roster/.
- Build `volume_silver_compare.py` mirroring
  `iol_nobio_silver_compare.py`: score (a) the APPLIED links vs
  silver, (b) classc_results verdicts vs silver, (c) A/B spot-checks;
  print disagreement list for hand re-adjudication. Output
  data/volume/classc/NOBIO_SILVER.md.

## Pools (~50 each, stratified)

1. **Applied class-C links** (`career_person_links.jsonl` /
   CLASSC_LINKS.md policy): stratify by tier (tier1/tier2/tier3
   skeptic) x corroboration class (hard/place/possim/llm_only) x
   salary rank. These went into the table under the 0-FP claim —
   silver tests that claim at 10x the original sample.
2. **Class-C judged 'different'** (measured never-bio'd from
   `career_classes_measured.jsonl` + classc_results): the NEGATIVES
   were never hand-verified. Oversample high-risk: rare surname +
   era-overlapping candidates (a wrong 'different' hides a real link).
3. **Career-chain coherence** (`data/volume/careers/careers.jsonl`):
   is a within-volume career one person? Strata: name form
   (initials-only vs forename) x surname frequency tercile x colony
   size x salary rank; include a high-risk stratum (span >= 20 yrs OR
   >= 10 records with <= 2 initials) — that's where the IOL sample
   found its two conflations. Verdicts confirm/reject/junk.
4. **Class A/B spot-check** (`career_classes.jsonl` cls A and B):
   verify no compatible bio person truly exists — search
   bio_persons.jsonl by surname variants yourself (OCR variants,
   hyphenation, Mc/Mac). A wrong A/B inflates never-bio'd directly.

## Method (what worked on the IOL round)

- HYDRATE FULL CONTEXT before judging: career = per-year
  position/department/salary records; person = full event list with
  places + honours + birth year. Judge nothing from summaries.
- Corroborators that decide: exact office-string matches, honours
  printed on both sides, entry/covenant-year fits, salary-rank
  trajectory (a clerk on 100l. is not a colonial secretary), rare
  surnames. Contradictory full forenames = different, always.
- Label `unsure` when genuinely torn — unsure items leave the
  precision denominator; a forced guess poisons it.
- EXPECT data defects and record them as labels, not just fixes:
  IOL round found junk name classes (office phrases as names),
  SURNAME-first inverted names, annuitant rows whose entry year is a
  retirement date. The COL analogues are unknown — that discovery is
  half the value. Fix cheap parser-level defects at source only if
  ids are stable under rebuild (check first! IOL needed
  content-derived ids); otherwise record and move on.
- After writing: verify EVERY id resolves against its source file
  (transcription errors happen — the IOL round caught 3), check dup
  ids = 0, then commit + push + scp backup.

## Gotchas

- careers.jsonl rows have `suspect` and `weak_key` flags and
  `bio_ids` (linked careers — exclude from never-bio'd pools).
- Salary parsing/rank buckets: reuse salary_peak/rank_class from
  volume_classc_worklist.py so strata line up with CLASSC.md tables.
- classc_results ids are `<career_id>::<person_id>`; some careers
  have up to 4 candidate pairs (cap) — label the PAIR you read, not
  the career.
- The applied-link policy recomputed corroboration deterministically
  and ignored LLM confidence (CLASSC_LINKS.md) — silver scores the
  POLICY output (career_person_links.jsonl), not raw verdicts.
- Colony gating used the volume linker's gazetteer
  (_colony_target_set); unresolvable places stay compatible — an A/B
  spot-check must honour the same rule or it will miscount.
- Known priors to compare against: link precision 93.2% non-weak /
  47.5% weak (2026-07-11 audit); classc 0 observed FPs in applied
  strata (34-pair basis); IOL det-tier 39/40.

---
