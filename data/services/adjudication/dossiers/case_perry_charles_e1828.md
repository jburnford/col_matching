<!-- {"case_id": "case_perry_charles_e1828", "bio_ids": ["perry_charles_e1828"], "stint_ids": ["Perry, C. L___Victoria___1889"]} -->
# Dossier case_perry_charles_e1828

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 16 official(s) with this surname in the graph's staff lists; 15 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['perry_charles_e1828'] carry a single initial only — the namesake trap applies.

## Biography `perry_charles_e1828`

- Printed name: **PERRY, CHARLES**
- Birth year: not printed
- Appears in editions: [1886, 1888, 1889, 1890]

### Verbatim printed entry text (OCR)

**Version `col1886-L35254.v` — printed in editions [1886, 1888, 1889, 1890]:**

> PERRY, RIGHT REV. BISHOP CHARLES, D.D.—Was formerly fellow of Trinity College, Cambridge, where he graduated senior wrangler, first Smith's prizeman, and 1st class in classics, 1828; 1st bishop of Melbourne on the sub-division of the see of Australia, 1847 to 1876 (prelate of the Order of St. Michael and St. George, May, 1872).

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1828–1828 | fellow | — | [1886, 1888, 1889, 1890] |
| 1 | 1847–1876 | 1st bishop of Melbourne | Melbourne | [1886, 1888, 1889, 1890] |

## Candidate stint `Perry, C. L___Victoria___1889`

- Staff-list name: **Perry, C. L** | colony: **Victoria** | listed 1889–1894 | editions [1889, 1890, 1894]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1889 | C. L. Perry | — | Office of Titles | — | — |
| 1890 | C. L. Perry | Examiner of Titles | Office of Titles | — | — |
| 1894 | C. L. Perry | Police Magistrate, Coroner, or Warden of the Goldfields of Victoria | Police Magistrates, Coroners, and Wardens of the Goldfields of Victoria | — | — |

### Deterministic checks: `perry_charles_e1828` vs `Perry, C. L___Victoria___1889`

- [PASS] surname_gate: bio 'PERRY' vs stint 'Perry, C. L' (exact)
- [PASS] initials: bio ['C'] ~ stint ['C', 'L']
- [PASS] age_gate: stint starts 1889; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Victoria'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1889-1894
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
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

