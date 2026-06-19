<!-- {"case_id": "case_molesworth_robert_e1828", "bio_ids": ["molesworth_robert_e1828"], "stint_ids": ["Molesworth, R___Victoria___1877"]} -->
# Dossier case_molesworth_robert_e1828

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 6 official(s) with this surname in the graph's staff lists; 4 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['molesworth_robert_e1828'] carry a single initial only — the namesake trap applies.

## Biography `molesworth_robert_e1828`

- Printed name: **MOLESWORTH, ROBERT**
- Birth year: not printed
- Terminal: retired 1886 — “retired 1886.”
- Appears in editions: [1886, 1888, 1889, 1890]

### Verbatim printed entry text (OCR)

**Version `col1888-L34962.v` — printed in editions [1888, 1889, 1890]:**

> MOLESWORTH, SIR ROBERT, KNT. BACH, (1887).—Called to Irish bar 1828; Victoria bar, 1853; solicitor-general, 1854; puisne judge, 1856; retired 1886.

**Version `col1886-L34874.v` — printed in editions [1886]:**

> MOLESWORTH, R.—Educated at Trinity College, Dublin; called to the bar, 1828; solicitor-general, Victoria, January 4, 1856; puisne judge, 17th June, 1856.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1828 | Called to Irish bar | — | [1886, 1888, 1889, 1890] |
| 1 | 1853 | Victoria bar | Victoria | [1888, 1889, 1890] |
| 2 | 1854 | solicitor-general | Victoria *(inherited from previous clause)* | [1888, 1889, 1890] |
| 3 | 1856 | puisne judge | Victoria *(inherited from previous clause)* | [1886, 1888, 1889, 1890] |
| 4 | 1856 | solicitor-general, Victoria, January 4 | — | [1886] |

## Candidate stint `Molesworth, R___Victoria___1877`

- Staff-list name: **Molesworth, R** | colony: **Victoria** | listed 1877–1883 | editions [1877, 1879, 1880, 1883]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | R. Molesworth | Puisne Judges | Their Honours the Judges | — | — |
| 1879 | R. Molesworth | Puisne Judges | Their Honours the Judges | — | — |
| 1880 | R. Molesworth | — | Their Honours the Judges | — | — |
| 1883 | R. Molesworth | Puisne Judge | Their Honours the Judges | — | — |

### Deterministic checks: `molesworth_robert_e1828` vs `Molesworth, R___Victoria___1877`

- [PASS] surname_gate: bio 'MOLESWORTH' vs stint 'Molesworth, R' (exact)
- [PASS] initials: bio ['R'] ~ stint ['R']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [PASS] colony: 3 placed event(s) resolve to 'Victoria'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1877-1883
- [PASS] position_sim: best 100 vs bar 60: 'puisne judge' ~ 'Puisne Judge'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: ALL supporting events inherit their place from an earlier clause — weak evidence

## Adjudication constraints (binding)

- The prime directive is NO FALSE MERGES. A missed link is recoverable; a
  wrong one silently corrupts the historical record. When in doubt, leave
  the stint unassigned.
- Surname identity is NOT evidence: every candidate here already shares the
  surname (it is the blocking key). Only position, place, dates, honours,
  initials/forenames, and edition co-occurrence count.
- Single-initial biographies (e.g. "J. Lewis") must never be merged on
  shared-stint or tenure-overlap evidence alone; they need a strong
  independent dimension (specific position match, shared honour, or
  multi-edition co-occurrence).
- A stint belongs to AT MOST one biography. If two biographies in this case
  could plausibly hold the same stint, assign it to neither.
- Respect hard chronology: nobody serves before age ~15 or after death.
- Generic junior titles (clerk, cadet, assistant) recur constantly; a title
  match alone on a common office is weak evidence.

