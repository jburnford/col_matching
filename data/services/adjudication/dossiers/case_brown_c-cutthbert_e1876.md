<!-- {"case_id": "case_brown_c-cutthbert_e1876", "bio_ids": ["brown_c-cutthbert_e1876"], "stint_ids": ["Brown, C. Carnegie___Gold Coast___1889"]} -->
# Dossier case_brown_c-cutthbert_e1876

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 250 official(s) with this surname in the graph's staff lists; 114 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- Phase 1 found `brown_c-cutthbert_e1876` ↔ `Brown, C. Carnegie___Gold Coast___1889` passed its evidence bar but dropped it as ambiguous (a comparable-strength competitor existed).
- NOTE: stint `Brown, C. Carnegie___Gold Coast___1889` is also gate-compatible with biography(ies) outside this case: ['brown_c-cuthbert_e1877'] (already linked elsewhere or filtered).

## Biography `brown_c-cutthbert_e1876`

- Printed name: **BROWN, C. CUTTHBERT**
- Birth year: not printed
- Appears in editions: [1883, 1886, 1888, 1889, 1890, 1894, 1896, 1897]

### Verbatim printed entry text (OCR)

**Version `col1883-L26595.v` — printed in editions [1883, 1886, 1888, 1889, 1890, 1894, 1896, 1897]:**

> BROWN, C. CUTTHBERT.—Acting chief clerk and book-keeper, treasury department, Gold Coast Colony, 1st March, 1876, confirmed 18th July, 1877.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1876 | Acting chief clerk and book-keeper, treasury department | Gold Coast | [1883, 1886, 1888, 1889, 1890, 1894, 1896, 1897] |
| 1 | 1877 | confirmed | — | [1883, 1886, 1888, 1889, 1890, 1894, 1896, 1897] |

## Candidate stint `Brown, C. Carnegie___Gold Coast___1889`

- Staff-list name: **Brown, C. Carnegie** | colony: **Gold Coast** | listed 1889–1899 | editions [1889, 1890, 1894, 1896, 1897, 1898, 1899]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1889 | C. C. Brown | Chief Clerk and Book-keeper | Treasury | — | — |
| 1890 | C. C. Brown | Chief Clerk and Book-keeper | Treasury | — | — |
| 1894 | C. C. Brown | Chief Clerk and Book-keeper | Treasury | — | — |
| 1896 | C. C. Brown | Chief Clerk and Book-keeper | Treasury | — | — |
| 1897 | C. C. Brown | Chief Clerk and Book-keeper | Treasury | — | — |
| 1898 | C. C. Brown | Chief Clerk and Book-keeper | Treasury | — | — |
| 1899 | C. C. Brown | Chief Clerk and Book-keeper | Treasury | — | — |

### Deterministic checks: `brown_c-cutthbert_e1876` vs `Brown, C. Carnegie___Gold Coast___1889`

- [PASS] surname_gate: bio 'BROWN' vs stint 'Brown, C. Carnegie' (exact)
- [PASS] initials: bio ['C', 'C'] ~ stint ['C', 'C']
- [PASS] age_gate: stint starts 1889; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Gold Coast'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1889-1899
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [PASS] edition_cooccurrence: 2 agreeing edition-year(s) [1889, 1890] pos~100 (bar: >=2)
- [FAIL] place_inherited: no supporting events

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

