<!-- {"case_id": "case_husband_j-i_b1919", "bio_ids": ["husband_j-i_b1919"], "stint_ids": ["Husband, J. I___Sierra Leone___1949"]} -->
# Dossier case_husband_j-i_b1919

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 4 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `husband_j-i_b1919`

- Printed name: **HUSBAND, J. I**
- Birth year: 1919 (attested in editions [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965])
- Honours: C.B.E (1965)
- Appears in editions: [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965]

### Verbatim printed entry text (OCR)

**Version `col1957-L24342.v` — printed in editions [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965]:**

> HUSBAND, J. I., C.B.E. (1965).—b. 1919; ed. Wellington Coll. and Trinity Coll., Oxford; cadet, S. Leone, 1940; dist. comsnr., 1946; prin. labr. offr., Ken., 1952; asst. labr. comsnr., 1954; dep. labr. comsnr., 1957; ch. labr. offr., 1962-64. (Ken. Govt. service.)

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1940 | cadet, S. Leone | — | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965] |
| 1 | 1946 | dist. comsnr | — | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965] |
| 2 | 1952 | prin. labr. offr. | Kenya | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965] |
| 3 | 1954 | asst. labr. comsnr | Kenya *(inherited from previous clause)* | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965] |
| 4 | 1957 | dep. labr. comsnr | Kenya *(inherited from previous clause)* | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965] |
| 5 | 1962–1964 | ch. labr. offr | Kenya *(inherited from previous clause)* | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965] |

## Candidate stint `Husband, J. I___Sierra Leone___1949`

- Staff-list name: **Husband, J. I** | colony: **Sierra Leone** | listed 1949–1951 | editions [1949, 1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | J. I. Husband | Assistant District Commissioners and Cadets | Provincial Administration | — | — |
| 1949 | J. I. Husband | Labour Officers | Labour | — | — |
| 1950 | J. I. Husband | District Commissioners | Provincial Administration | — | — |
| 1950 | J. I. Husband | Labour Officer | LABOUR | — | — |
| 1951 | J. I. Husband | District Commissioner | Provincial Administration | — | — |
| 1951 | J. I. Husband | Labour Officer | Labour | — | — |

### Deterministic checks: `husband_j-i_b1919` vs `Husband, J. I___Sierra Leone___1949`

- [PASS] surname_gate: bio 'HUSBAND' vs stint 'Husband, J. I' (exact)
- [PASS] initials: bio ['J', 'I'] ~ stint ['J', 'I']
- [PASS] age_gate: stint starts 1949, birth 1919 (age 30)
- [FAIL] colony: no placed event resolves to 'Sierra Leone'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1949-1951
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

