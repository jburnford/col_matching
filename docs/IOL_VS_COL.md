# The India Office List corpus vs the Colonial Office List: identity-QA assessment

*Written 2026-07-11 from direct reading of editions across all publication
families and every data layer in `data/iol/`. Companion to
`IDENTITY_QA_ROADMAP.md` and `data/volume/identity/B1_MEASURED.md` (the COL
methodology this session extends).*

## 1. Corpus shape

139 edition directories under `iol_ocr_1860-1940/` (name is a misnomer — the
corpus runs to **1947**), five publication families:

| family | title | era | bios? |
|---|---|---|---|
| `iacsl` | Indian Army & Civil Service List | 1861–1890, semiannual (`_jan`/`_jul`) | only in `_supp` volumes from 1886 |
| `il` | India List, Civil and Military | 1882–1895, semiannual | only in `_supp` volumes |
| `iliol` | India List / India Office List | 1896–1937, annual | yes |
| `iol` | India Office List (duplicate OCR run) | 1896–1937 | (collapsed into `iliol`) |
| `iobol` | India Office and Burma Office List | 1938–1947 | yes |

16 physical volumes were OCR'd twice under two prefixes
(`data/iol/edition_sources.jsonl`); `col_match/volume/iol_reader.py` collapses
them with an era-preference rule, always choosing `iliol` over `iol`.
Half-yearly editions are distinct attestations, kept separate.

**The `_supp` volumes ARE the India Office List.** The 1886 "supplement" to
the IACSL is internally titled *THE INDIA OFFICE LIST* and contains the first
*RECORD OF THE PUBLIC SERVICES OF OFFICERS AND OTHERS* — the biographical
section. From 1886–1895 the biographical record lives ONLY in these annual
supplements; the semiannual main volumes stay roster-only. From 1896 the two
merge into the single annual India Office List. Consequence: **69 of 139
editions have no Record of Services at all** (`editions_no_bios.jsonl`) —
everything before 1886, all main `jan`/`jul` volumes 1886–1895, plus
`iliol_1918` (wartime volume genuinely lacks the section) and
`iobol_1947_supp`.

**Format**: unlike the COL's `result.json` layout blocks with bboxes, each
edition is flowed markdown + an HTML twin + page-level metadata (token counts
only). Provenance is char-offset + estimated page. Everything positional the
COL pipeline leans on (block categories, column geometry) is absent; the HTML
`<p>`/`<h1>`/`<table>` structure is what there is, and it is good.

## 2. Sections and the unparsed roster layer (Q1)

Read directly: iacsl_1865_jan, iacsl_1875_jan, iacsl_1880_jan, il_1884_jul,
il_1892_jan, iacsl_1886_supp, iliol_1901, iliol_1930/31/35, iobol_1938–47.
Consistent macro-structure, evolving with the constitutional era:

- **Front matter**: examination regulations, furlough/pension codes (huge —
  up to a third of early volumes), warrant of precedence.
- **Honours rolls**: Order of the Bath; from 1875+ the Star of India
  (G.C.S.I./K.C.S.I./C.S.I. by grade), Order of the Indian Empire, Imperial
  Order of the Crown of India — grade-sectioned name lists, same shape as
  the COL honours rolls we already parse.
- **India Office (London) establishment** — Secretary of State, Council,
  departments; the analogue of the CO front matter (SoS/PUS/CO staff layers).
- **Civil lists by government** (Government of India, each presidency/
  province): office—holder pairs rendered as
  `*Private Secretary*—J. D. Tyson, C.B.E., I.C.S.` — italic office, em-dash,
  name + honours. Extremely regular in 1896+ editions; department-sectioned.
- **Gradation lists**: seniority-ordered rosters (Covenanted Civil Servants
  per establishment; Army gradation by rank). Entries like
  `1795 Podmore, R., M.I., 20 June` grouped under year-of-entry headers, or
  two-column `<table>` cells of `<p>` lines in the HTML (column-major
  order preserved per `<td>` — no interleaving).
- **Record of Services** (1886+): the bio section, already parsed.
- **Casualties / Retirements** (tables), leave lists, addenda.

**Parseability verdict**: the roster layer is *more* parseable than feared.
Sections are separable — headings survive as `<h1>/<h2>` and section
boundaries are recoverable the same way `iol_bios.find_services_section`
does it (heading match + density scoring). The two roster genres are both
line-per-officer with strong local grammar (civil list: italic-office—name;
gradation: year headers + `surname, initials, corps, date` lines). The real
costs are (a) running headers OCR'd as headings, which pollute
section-boundary detection (see §6 — this already bit the bio extractor),
(b) two-column tables where year headers sit in one cell and their
continuation in the next, (c) abbreviation vocabularies per era (B./M./Bo.
establishment codes, corps codes). Estimate: a gradation/civil-list parser is
a COL-roster-scale project (weeks not days), family-by-family; the 1896+
civil lists alone would be a fast first tranche. **Out of scope this
session**, as directed.

## 3. Bio schema vs COL bios (Q2)

`data/iol/bios/` — 123 edition files, **258,103 bios** (plus `.xref.jsonl`
siblings: the bold `(see X)` cross-reference paragraphs, i.e. alias
redirects — ~100–150/edition after 1902, empty before 1903). Emitted by
`col_match/volume/iol_bios.py` in the same `VolumeBio` shape as
`volume/bios.py`, so field names match the COL exactly: `bio_id`,
`edition_year`, `surname`, `given_names`, `birth_year`, `honours`, `events`,
`raw_text`, `provenance`, `flags`.

What differs in content:

- **Birth years are an era feature, not an OCR failure.** The List only
  began printing `(b. <date>)` in headwords c. 1929: parsed birth_year is
  0% of bios through 1928, then 69–95% from 1930 on (1935: 5,825/7,602 raw
  texts carry `(b.` and 5,842 parse). The COL A2 birth-repair protocol
  applies unchanged to the late editions — same digit-garble exposure — but
  covers only the post-1929 cohort. In the person table, 48% of canonical
  persons (8,603/17,922) have a birth year, all sourced from late editions.
- **Events are terser early.** Bios with ≥1 parsed event: 23–30% before
  1927, 44–58% after (the LLM-structured layer, not this rules layer, is
  what feeds the person table — see §4).
- **Honours: the Indian orders dominate**, and they are already in
  `volume_identity_screens.ORDER_LADDERS` (Star of India CSI→KCSI→GCSI,
  Indian Empire CIE→KCIE→GCIE). New in the IOL: campaign decorations
  ("medal", "medal and clasp", named expeditions) which `award_token()`
  correctly ignores, and **Indian titles** (Khan Bahadur, Rai Bahadur,
  Sardar Bahadur, Diwan Bahadur) which print as name components/honorifics,
  not ladder awards — they leak into `given_names` ("ABDULLAH IBN YUSUF
  ALI, KHAN BAHADUR"), a name-completeness hazard for matching.
- **Education is richer and earlier**: "Educ. at Bath Coll., and Balliol
  Coll., Oxford; apptd. after exam. of 1891" is near-universal for ICS men
  — the competitive-examination system means IOL bios carry school +
  university + exam year as a matter of form. Already extracted:
  `graph_stage3/education.jsonl` (10,055 rows),
  `education_parsed.jsonl` (6,715 distinct strings, Qwen-parsed per
  `docs/PARSE_IOL_EDUCATION.md`). This is a stronger tie-breaker layer than
  the COL ever had (roadmap B4).
- **Swallowed headwords (parser defect)**: ~1.1% of bios contain a second
  bio appended (sampled 290/26,384 over five editions). Cause: the
  segmenter keys on the COL headword shape `SURNAME, Given` — headwords
  that open differently, chiefly **Indian names without the
  surname-comma** ("ABDUL GHAFUR KHAN OF ZAIDA (dist. judge...") and
  peerage headwords ("CONNAUGHT AND STRATHEARN..."), don't trigger a split
  and are absorbed into the preceding bio. Systematic bias: the missed
  entries are disproportionately Indian officers — worth fixing before any
  analysis of Indianization.

## 4. The person-identity stack and the dedup merge map (Q3)

The IOL person table is the OLD career-KG machinery (`kg_dedup_*.py`,
selected via `COL_KG_OUT=data/iol`), not the COL's new volume_bio_persons
spine. Five layers:

1. **Text chaining**: 258,103 bios → 82,011 chains
   (`persons.jsonl`; bios are cumulative across editions, so consecutive
   near-identical texts chain; `canonical_bio_id` = richest member).
2. **Stage-2 fold**: OCR-variant/reformat chain repairs → 30,496
   (`persons.deduped.jsonl`).
3. **LLM structuring**: one Qwen-structured record per chain →
   `llm_struct_corpus.valid.jsonl`, 30,446 records with clean events
   (position/place/years/org_type), honours (award+year), education,
   birth_year. `person_id` = `kgp_iol<edition>-c<char_offset>` of the
   canonical bio.
4. **Stage-3 dedup — THE MERGE MAP**: union-find over structured records,
   four chained passes, each composing onto the last
   (verified: row-subset chain, and only `dedup_stage3_merge_map.school.jsonl`
   reproduces the shipped person table):
   - **base** (10,084 edges): (surname, given) blocking →
     `dedup_stage3_candidates.jsonl` (7,662 groups with evidence tiers
     `A_birth`/`B_place`/`MERGE_RULE`/`WEAK`...), DeepSeek verdicts
     (`dedup_verdict_*.json`) + 149 hand-adjudicated held groups
     (`kg_dedup_stage3_adjudicate.py`).
   - **+crossform** (1,218 edges): surname-only blocking, merge on a shared
     exact appointment (job@place@year) — `dedup_crossform_edges.jsonl`.
   - **+roleyear** (690 edges): same role+colony+year_start, rank-stripped
     name match; hand-reviewed clusters.
   - **+school** (548 edges): school-blocked, `confident`/`likely`
     dispositions only.
5. **Apply** (`kg_dedup_stage3_apply.py`): fold members, richest-spine event
   union → `llm_struct_corpus.stage3.deduped.jsonl` = **17,922 canonical
   persons** = `graph_stage3/persons.jsonl` (cluster sizes: 10,204
   singletons, 4,335 pairs, 2,410 triples, ... 4 nines). Downstream:
   `graph_stage3/` KG (119,690 career events, 95% dated; 11,073 honours,
   56% dated; QID-grounded places), the mobility videos, transfers.

**What was never measured**: every one of those 12,540 merge edges — and the
82,011-chain text-chaining layer beneath them — carries a design-claim
precision only. This is the COL B1 story again, one layer up: B1 audited
bio→roster links; here the risky join is **bio-chain→person**. The audit
unit is the merge edge (pair of structured records united), stratified by:

- **evidence class**: which pass created the edge (base tier from the
  candidates file, split LLM-verdict vs auto-rule vs hand; crossform;
  roleyear; school) — the direct analogue of B1's link-strength stratum;
- **surname frequency** (corpus person-count per surname key, high/mid/low —
  the COL's dominant risk axis);
- **name completeness** (full given names both sides vs initials one side —
  initials-vs-full merges were exactly what crossform loosened blocking
  for).

Adjudication renders each member's structured record (name, birth,
education, honours, dated events) into `nibi/qwen_classc_worker.py --mode
ioldedup` pair format (an IOL-specific merge prompt added this session).

### MEASURED (Nibi job 17504437, 1,800-pair stratified sample)

**Corpus-wide stratum-weighted merge precision: 87.2%** — meaningfully
below the COL's 93.2% non-weak link precision. Full table in
`data/iol/identity/MERGE_MEASURED.md`; evidence-class rollups:

| class | edges | precision | note |
|---|---|---|---|
| base:A_birth | 4,477 | 91.7% | birth-anchored merges hold best |
| base:C_posting | 5,274 | 83.7% | **the weak class**; its high-risk tercile is 80.0% |
| base:B_other | 333 | 86.0% | |
| crossform | 1,218 | 85.9% | mid tercile 80.0%, low 94.0% |
| roleyear | 690 | 88.0% | |
| school | 548 | 88.0% | |

Extrapolating (1−precision)×edges per stratum: **~1,600 of the 12,540
merge edges are bad** (12.8%) — on the order of 1,400+ over-merged persons
in the 17,922-person table. Shared-posting evidence without birth-year
corroboration is the dominant failure mode, exactly where the pre-1929
absence of printed birth years bites. Refutation reasons are substantive
(entry-age impossibilities, non-overlapping trajectories, jurisdiction
conflicts), with the usual LLM-judge caveat — e.g. one sampled refutation
splits a Bombay high-court judge from a Sind one in 1887, when Sind was
administratively part of Bombay.

### APPLIED (Nibi job 17505330: full census + rebuild, same day)

All 12,540 edges then adjudicated in full (census keep rate 87.6%,
matching the sample estimate): **1,557 drops, 10,982 keeps, 1 error**;
the 35 A6 under-merge pairs judged alongside (28 same → unions).

**The judge over-splits, and the honours layer catches it**: rerunning
screen A6 on the first rebuilt table found 158 same-honour duplicate
pairs, of which **117 were edges the judge had just dropped** — identical
full names, identical birth years, same award+year (e.g. HARPER-NELSON,
JOHN JOSEPH, b. 1882, O.B.E. 1919 on both sides). Terse-vs-rich record
pairs (a 1945/1947 one-liner vs a full pre-war bio) read as "different
trajectories" to a strict judge. Per COL discipline the deterministic
fingerprint outranks a single judged verdict: **86 no-birth-conflict
drops were reinstated** by an `a6-honour-override` ledger entry.

Final state (all in `data/iol/identity/merge_decisions.jsonl`, an
append-only accumulative ledger; map `dedup_stage3_merge_map.audited
.jsonl`, flattened — the 16 broken chains are gone):
12,540 school edges − 1,557 drops + 113 unions (27 A6 + 86 reinstated)
= 11,095 flattened rows → **19,351 canonical persons** (was 17,922;
+1,429 net splits). Full KG re-emitted (career events, roles, orgs,
honours, career facts, education edges re-fanned from the LLM parse —
not remapped in place, which is lossy for split persons).
`iol_identity_check.py` green on the rebuilt table: unflattened 0,
age invariants 117→105, A6 residue 15 pairs (10 strong, the genuinely
new under-merge candidates for the next adjudication batch).

## 5. Rupee salaries (Q4)

**The question dissolves: the IOL prints almost no salaries.** `Rs.` appears
only ~200 times in a 3.6M-char 1901 volume, ~400 in 1935 — and inspection
shows these are *regulatory thresholds*, not per-officer pay: precedence
warrant bands ("Political Agents drawing Rs. 2,000 a month and upwards"),
the roster inclusion rule (officers under Rs. 500/month substantive pay are
omitted, except ICS), chaplains' pay scales in the front matter. Neither the
civil lists, nor the gradation lists, nor the Record of Services bios carry
a salary column the way COL rosters do. Consequences:

- The COL's flagged 15:1 Rs→£ conversion (`list_vs_bio_v2.py`) has no IOL
  counterpart to reconcile — nothing to convert.
- **Screen A3 (salary regression) does not transfer.** Rank/position-class
  regression is the only within-career signal available.
- Any future IOL salary analysis must come from the pay codes (scale by
  appointment class), not from printed per-person figures.

## 6. OCR/extraction defects found while exploring (evidence for §2–3)

1. **Services-section truncation, 2 editions** (found via bio-count
   anomalies, confirmed by heading-density sweep of all 123 editions):
   running headers "RECORD OF SERVICES." are OCR'd as real `<h1>`s
   mid-section; `iol_bios.find_services_section` picks the LAST
   density-qualifying heading (to skip TOC copies), so it starts the
   section at the final running-header copy. `iliol_1930` keeps only 987k
   of 2.69M chars (2,742 bios extracted vs 7,443 in the same-sized 1931 —
   ~4,700 bios lost, A–R missing); `iliol_1911` keeps 1.29M of 1.75M
   (3,495 vs 4,818 bios). **Fix**: choose the qualifying heading that
   maximizes span-to-next-non-services-heading, not the last one. Not
   applied this session — a bios rebuild invalidates the chain/person
   layers the audit below targets; fix and rebuild together after the
   audit.
2. **Swallowed non-comma headwords**, ~1.1% of bios, Indian-name-biased
   (§3). Fix belongs in `_is_headword` (accept `NAME OF PLACE (`-shaped
   and multi-token capitalized headwords without commas).
3. **`iliol_1918` is a partial OCR**: the markdown is 0.7MB against ~4.5MB
   for neighboring years — most of the volume (including the Record of
   Services, which its front matter references) was never captured. A
   re-OCR candidate; currently a silent bio gap between 1917 and 1919.
4. Honours dating is thin (56% of honour entries carry a year) — A1/A6
   screens run on the dated subset.
5. **The shipped merge map is unflattened in 16 chains** (found by
   `iol_identity_check.py` on its first run): `kg_dedup_school_apply.py`
   composed its 548 edges without rewriting older rows that point at ids
   the new edges absorb, so 16 X→K, K→C chains leave X's records under a
   canonical that itself folded away — 16 persons split from their true
   canonical in `llm_struct_corpus.stage3.deduped.jsonl` /
   `graph_stage3/`. Fix (flatten + re-apply + KG rebuild) is deferred to
   the post-audit apply cycle; pinned at 16 in the check baselines.

**Tier-A screen results on the shipped table** (`iol_identity_screens.py`,
outputs in `data/iol/identity/`): A1 = 1 person (Evan Jenkins, KCIE 1920 <
CIE 1936 — garbled year or fusion); A2 = 117 (104 one-digit birth repairs —
century flips like ADVANI b.1796/entry 1922 — 13 two-digit, **0 dynastic
candidates**); birth-from-honour = 0; A6 = 37 duplicate pairs, 31 strong
(e.g. COBURN "M. R." vs "MARMADUKE ROBERT", same OBE 1919 + birth 1885,
edition-disjoint — the initials-vs-full split crossform was built to catch).
An order of magnitude cleaner than the COL's first screen run (661 age
hits), consistent with typed late-era birth years and LLM-structured events.

## 7. Cross-corpus overlap: India → colonial careers (Q5)

Quick exact-join of the 17,922 IOL canonical persons against the 27,511 COL
bio-persons on normalized (surname, given_names): **211 matches**, 80 with
≥2 given-name tokens; of the 63 with birth years on both sides, **35 agree
within ±1** (near-certain same person) and 28 conflict (namesakes). This is
a floor — initials-vs-full-name forms and title/honorific pollution suppress
the exact join badly.

The confirmed matches are historically exactly right: Sir John Anderson
(b. 1882; IOL 1938 as Governor of Bengal, COL 1912 as a CO man), Evelyn
Baring (b. 1903; IOL 1940, then COL 1955 as Governor of Kenya), and a
visible cohort of **1945/1947-edition ICS officers reappearing in 1950s COL
editions** — the post-Partition exodus into the Colonial Service (Acton,
Barlow, Barrett, Barty... all IOL 1947 → COL 1950–59). That migration is a
findable, quantifiable population once both person tables are trustworthy:
the right join keys are honours (award+year is near-unique empire-wide),
birth year, education institution, and full names — in that order.

## 8. What transfers from the COL screens, what doesn't

| screen | transfers? | notes |
|---|---|---|
| A1 honours precedence | **yes, unchanged** | CSI/CIE ladders already in `ORDER_LADDERS`; dated honours only (56%) |
| A2 age invariants + digit repair | **yes** | but only the 48% of persons with birth years (post-1929 sources) |
| A2 birth-from-honour | **yes** | same parser-bug signature possible in LLM structuring |
| A2 birth-vote conflicts | no | IOL person table has no `birth_year_votes` (single-source births) |
| A6 rare-honour duplicates | **yes, unchanged** | strong here: honours 36% of persons, orders appoint once |
| A3 salary regression | **no** | no salaries printed (§5); rank-class regression is the residual idea |
| A4 place alternation | adapt | events carry `colony_qid`; structural pairs to learn (e.g. Calcutta hot/cold season, province splits: Bengal/Eastern Bengal & Assam 1905–12) |
| A5 multi-post years | partial | no `multi_post_years` field; derivable from overlapping dated events |
| B1-style link audit | **→ the merge-map audit** (§4) | the measured number this layer is missing |
| fail-loud check script | **yes** | `iol_identity_check.py`, baselines measured this session |

Ledger discipline carries over verbatim: append-only decisions ledger,
ACCUMULATIVE overrides (screens run post-apply), survivor-map resolution
for absorbed ids.
