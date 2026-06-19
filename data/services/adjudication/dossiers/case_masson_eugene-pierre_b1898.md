<!-- {"case_id": "case_masson_eugene-pierre_b1898", "bio_ids": ["masson_eugene-pierre_b1898"], "stint_ids": ["Masson, E. P. L. L___Trinidad and Tobago___1931", "Masson, E. P. L. L___Trinidad and Tobago___1949"]} -->
# Dossier case_masson_eugene-pierre_b1898

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 15 official(s) with this surname in the graph's staff lists; 8 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `masson_eugene-pierre_b1898`

- Printed name: **MASSON, Eugene Pierre**
- Birth year: 1898 (attested in editions [1948, 1949, 1950, 1951, 1953, 1954, 1955])
- Honours: D.P.M, M.B
- Appears in editions: [1948, 1949, 1950, 1951, 1953, 1954, 1955]

### Verbatim printed entry text (OCR)

**Version `col1948-L34560.v` — printed in editions [1948, 1949, 1950, 1951, 1953, 1954, 1955]:**

> MASSON, Eugene Pierre, M.B., Ch.B. (Edin.), D.P.M.—b. 1898; ed. Rebington Coll., U.K., Queen's Royal Coll., Trinidad, and Edin. Univ.; on mil. serv., 1915-18; med. offr., Trin., 1928; asst. med. supt., St. Ann's Mental Hosp., 1935; supt., 1940.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1928 | med. offr. | Trinidad | [1948, 1949, 1950, 1951, 1953, 1954, 1955] |
| 1 | 1935 | asst. med. supt., St. Ann's Mental Hosp | Trinidad *(inherited from previous clause)* | [1948, 1949, 1950, 1951, 1953, 1954, 1955] |
| 2 | 1940 | supt | Trinidad *(inherited from previous clause)* | [1948, 1949, 1950, 1951, 1953, 1954, 1955] |

## Candidate stint `Masson, E. P. L. L___Trinidad and Tobago___1931`

- Staff-list name: **Masson, E. P. L. L** | colony: **Trinidad and Tobago** | listed 1931–1934 | editions [1931, 1933, 1934]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1931 | E. P. L. L. Masson | — | Government Medical Officers | — | — |
| 1933 | E. P. L. L. Masson | Medical Officer | Medical Establishment | — | — |
| 1934 | E. P. L. L. Masson | Medical Officer | Government Medical Officers | — | — |

### Deterministic checks: `masson_eugene-pierre_b1898` vs `Masson, E. P. L. L___Trinidad and Tobago___1931`

- [PASS] surname_gate: bio 'MASSON' vs stint 'Masson, E. P. L. L' (exact)
- [PASS] initials: bio ['E', 'P'] ~ stint ['E', 'P', 'L', 'L']
- [PASS] age_gate: stint starts 1931, birth 1898 (age 33)
- [FAIL] colony: no placed event resolves to 'Trinidad and Tobago'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1931-1934
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Masson, E. P. L. L___Trinidad and Tobago___1949`

- Staff-list name: **Masson, E. P. L. L** | colony: **Trinidad and Tobago** | listed 1949–1954 | editions [1949, 1953, 1954]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | E. P. L. Masson | Medical Officer (Grade A) | Mental Hospital | — | — |
| 1953 | E. P. Masson | Superintendent Medical Officer, Mental Hospital | Civil Establishment | — | — |
| 1954 | E. P. Masson | Superintendent Medical Officer, Mental Hospital | Civil Establishment | — | — |

### Deterministic checks: `masson_eugene-pierre_b1898` vs `Masson, E. P. L. L___Trinidad and Tobago___1949`

- [PASS] surname_gate: bio 'MASSON' vs stint 'Masson, E. P. L. L' (exact)
- [PASS] initials: bio ['E', 'P'] ~ stint ['E', 'P', 'L', 'L']
- [PASS] age_gate: stint starts 1949, birth 1898 (age 51)
- [FAIL] colony: no placed event resolves to 'Trinidad and Tobago'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1949-1954
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

