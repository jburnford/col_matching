<!-- {"case_id": "case_sullivan_daniel-giles_b1882", "bio_ids": ["sullivan_daniel-giles_b1882"], "stint_ids": ["Sullivan, D___Mauritius___1898"]} -->
# Dossier case_sullivan_daniel-giles_b1882

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 24 official(s) with this surname in the graph's staff lists; 16 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `sullivan_daniel-giles_b1882`

- Printed name: **SULLIVAN, DANIEL GILES**
- Birth year: 1882 (attested in editions [1937, 1939, 1940])
- Appears in editions: [1937, 1939, 1940]

### Verbatim printed entry text (OCR)

**Version `col1937-L65169.v` — printed in editions [1937, 1939, 1940]:**

> SULLIVAN, HON. DANIEL GILES, J.P.—B. 1882; ed. Marist Bros. schl., Christchurch, N.Z.; mem., N.Z. H. of R. since 1919; min. of rlys. and min. of industries and commerce, 1935; min. of supply, 1939.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1919 | mem., N.Z. H. of R. since | New Zealand | [1937, 1939, 1940] |
| 1 | 1935 | min. of rlys. and min. of industries and commerce | New Zealand *(inherited from previous clause)* | [1937, 1939, 1940] |
| 2 | 1939 | min. of supply | New Zealand *(inherited from previous clause)* | [1937, 1939, 1940] |

## Candidate stint `Sullivan, D___Mauritius___1898`

- Staff-list name: **Sullivan, D** | colony: **Mauritius** | listed 1898–1920 | editions [1898, 1899, 1900, 1905, 1906, 1907, 1908, 1909, 1910, 1911, 1912, 1913, 1914, 1915, 1917, 1918, 1919, 1920]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1898 | D. Sullivan | 5th Class Clerks | POST OFFICE | — | — |
| 1899 | D. Sullivan | 5th Class Clerks | Post Office | — | — |
| 1900 | D. Sullivan | 5th Class Clerks | POST OFFICE | — | — |
| 1905 | D. Sullivan | 5th Class Clerk | POST OFFICE | — | — |
| 1906 | D. Sullivan | 5th Class Clerk | Post Office | — | — |
| 1907 | D. Sullivan | 5th Class Clerks | Post Office | — | — |
| 1908 | D. Sullivan | 5th Class Clerk | Post Office | — | — |
| 1909 | D. Sullivan | 5th Class Clerk | Post Office | — | — |
| 1910 | D. Sullivan | 5th Class Clerk | Post Office | — | — |
| 1911 | D. Sullivan | 5th Class Clerk | POST OFFICE | — | — |
| 1912 | D. Sullivan | 5th Class Clerk | POST OFFICE | — | — |
| 1913 | D. Sullivan | 5th Class Clerks | Post Office | — | — |
| 1914 | D. Sullivan | 5th Class Clerks | Postal and Telegraph Department | — | — |
| 1915 | D. Sullivan | 5th Class Clerks | Postal and Telegraph Department | — | — |
| 1917 | D. Sullivan | 5th Class Clerk | Postal and Telegraph Department | — | — |
| 1918 | D. Sullivan | 5th Class Clerk | Postal and Telegraph Department | — | — |
| 1919 | D. Sullivan | 5th Class Clerks | Postal and Telegraph Department | — | — |
| 1920 | D. Sullivan | 5th Class Clerk | Postal and Telegraph Department | — | — |

### Deterministic checks: `sullivan_daniel-giles_b1882` vs `Sullivan, D___Mauritius___1898`

- [PASS] surname_gate: bio 'SULLIVAN' vs stint 'Sullivan, D' (exact)
- [PASS] initials: bio ['D', 'G'] ~ stint ['D']
- [PASS] age_gate: stint starts 1898, birth 1882 (age 16)
- [FAIL] colony: no placed event resolves to 'Mauritius'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1898-1920
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

