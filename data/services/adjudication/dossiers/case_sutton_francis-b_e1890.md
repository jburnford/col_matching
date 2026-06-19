<!-- {"case_id": "case_sutton_francis-b_e1890", "bio_ids": ["sutton_francis-b_e1890"], "stint_ids": ["Sutton, F___Hong Kong___1909"]} -->
# Dossier case_sutton_francis-b_e1890

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 22 official(s) with this surname in the graph's staff lists; 14 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Sutton, F___Hong Kong___1909` is also gate-compatible with biography(ies) outside this case: ['sutton_fred_b1880'] (already linked elsewhere or filtered).

## Biography `sutton_francis-b_e1890`

- Printed name: **SUTTON, FRANCIS B.**
- Birth year: not printed
- Appears in editions: [1896]

### Verbatim printed entry text (OCR)

**Version `col1896-L41561.v` — printed in editions [1896]:**

> SUTTON, THE HON. FRANCIS B.—Postmaster-general, New South Wales, 11th Aug., 1890, at 13th Nov., 1891; minister of public instruction, 1891 to 1892, and again, 1891-4; representative of colony at Colonial conference, Ottawa, 1894.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1890–1891 | Postmaster-general | New South Wales | [1896] |
| 1 | 1891–1892 | minister of public instruction | — | [1896] |
| 2 | 1894–1894 | representative of colony at Colonial conference | — | [1896] |

## Candidate stint `Sutton, F___Hong Kong___1909`

- Staff-list name: **Sutton, F** | colony: **Hong Kong** | listed 1909–1934 | editions [1909, 1910, 1911, 1912, 1913, 1915, 1917, 1918, 1919, 1920, 1921, 1922, 1923, 1924, 1925, 1928, 1929, 1930, 1931, 1932, 1933, 1934]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1909 | F. Sutton | Land Surveyor | Crown Lands and Surveys | — | — |
| 1910 | F. Sutton | Land Surveyor | Crown Lands and Surveys | — | — |
| 1911 | F. Sutton | Land Surveyor | Crown Lands and Surveys | — | — |
| 1912 | F. Sutton | Land Surveyor | Crown Lands and Surveys | — | — |
| 1913 | F. Sutton | Second Grade Land Surveyor | Crown Lands and Surveys | — | — |
| 1915 | F. Sutton | Second Grade Land Surveyor | Crown Lands and Surveys | — | — |
| 1917 | F. Sutton | Second Grade Land Surveyors | Crown Lands and Surveys | — | — |
| 1918 | F. Sutton | Second Grade Land Surveyor | Crown Lands and Surveys | — | — |
| 1919 | F. Sutton | Second Grade Land Surveyors | Crown Lands and Surveys | — | — |
| 1920 | F. Sutton | Second Grade Land Surveyors | Crown Lands and Surveys | — | — |
| 1921 | F. Sutton | Land Surveyors, 1st Class | Crown Lands and Surveys | — | — |
| 1922 | F. Sutton | Land Surveyor, 1st Class | Crown Lands and Surveys | — | — |
| 1923 | F. Sutton | Surveyors, 1st Class | Crown Lands and Surveys | — | — |
| 1924 | F. Sutton | 1st Class Land Surveyors | Crown Lands and Surveys | — | — |
| 1925 | F. Sutton | Land Surveyors | Crown Lands and Surveys | — | — |
| 1928 | F. Sutton | Assistant Superintendent of Surveys | Surveys | — | — |
| 1929 | F. Sutton | Assistant Superintendent of Surveys | Surveys | — | — |
| 1930 | F. Sutton | Assistant Superintendent of Surveys | Surveys | — | — |
| 1931 | F. Sutton | Assistant Superintendent of Surveys | Surveys | — | — |
| 1932 | F. Sutton | Assistant Superintendent of Surveys | Public Works Department | — | — |
| 1933 | F. Sutton | Assistant Superintendent of Surveys | Public Works Department | — | — |
| 1934 | F. Sutton | Assistant Superintendent of Surveys | Public Works Department | — | — |

### Deterministic checks: `sutton_francis-b_e1890` vs `Sutton, F___Hong Kong___1909`

- [PASS] surname_gate: bio 'SUTTON' vs stint 'Sutton, F' (exact)
- [PASS] initials: bio ['F', 'B'] ~ stint ['F']
- [PASS] age_gate: stint starts 1909; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Hong Kong'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1909-1934
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

