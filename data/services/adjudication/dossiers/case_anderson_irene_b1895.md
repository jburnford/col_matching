<!-- {"case_id": "case_anderson_irene_b1895", "bio_ids": ["anderson_irene_b1895"], "stint_ids": ["Anderson, M. I___Bahamas___1921"]} -->
# Dossier case_anderson_irene_b1895

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 180 official(s) with this surname in the graph's staff lists; 91 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['anderson_irene_b1895'] carry a single initial only — the namesake trap applies.

## Biography `anderson_irene_b1895`

- Printed name: **ANDERSON, Irene**
- Birth year: 1895 (attested in editions [1950, 1951])
- Appears in editions: [1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1950-L33203.v` — printed in editions [1950, 1951]:**

> ANDERSON, Irene.—b. 1895; ed. Pub. Sch., Shanghai; nurse, med. dept., H.K., 1931; nursing sister, 1946.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1931 | nurse, med. dept. | Hong Kong | [1950, 1951] |
| 1 | 1946 | nursing sister | Hong Kong *(inherited from previous clause)* | [1950, 1951] |

## Candidate stint `Anderson, M. I___Bahamas___1921`

- Staff-list name: **Anderson, M. I** | colony: **Bahamas** | listed 1921–1940 | editions [1921, 1922, 1923, 1924, 1925, 1928, 1929, 1930, 1931, 1932, 1933, 1934, 1936, 1937, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1921 | M. I. Anderson | Asst. Clerk | Post Office | — | — |
| 1922 | M. I. Anderson | Asst. Clerk | Post Office | — | — |
| 1923 | M. I. Anderson | Assistant Clerk | Post Office | — | — |
| 1924 | M. I. Anderson | Assistant Clerk | Post Office | — | — |
| 1925 | Miss M. I. Anderson | Assistant Clerk | Post Office | — | — |
| 1928 | Miss M. I. Anderson | Clerk, Grade IV | Post Office Department | — | — |
| 1929 | M. Anderson | Clerk, Grade IV | Post Office Department | — | — |
| 1930 | Miss M. Anderson | Clerk, Grade IV. | Post Office Department | — | — |
| 1931 | Miss M. Anderson | Clerk, Grade IV | Post Office Department | — | — |
| 1932 | Miss M. I. Anderson | Clerks, Grade III. | Post Office Department | — | — |
| 1933 | Miss M. I. Anderson | Clerks, Grade III | Post Office Department | — | — |
| 1934 | Miss M. I. Anderson | Clerks, Grade III | Post Office Department | — | — |
| 1936 | Miss M. I. Anderson | Clerks, Grade III | Post Office Department | — | — |
| 1937 | M. I. Anderson | Clerks, Grade III | Post Office Department | — | — |
| 1940 | M. I. Anderson | Clerks, Grade III | Post Office Department | — | — |

### Deterministic checks: `anderson_irene_b1895` vs `Anderson, M. I___Bahamas___1921`

- [PASS] surname_gate: bio 'ANDERSON' vs stint 'Anderson, M. I' (exact)
- [PASS] initials: bio ['I'] ~ stint ['M', 'I']
- [PASS] age_gate: stint starts 1921, birth 1895 (age 26)
- [FAIL] colony: no placed event resolves to 'Bahamas'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1921-1940
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

