<!-- {"case_id": "case_dutton_a-p-h_b1918", "bio_ids": ["dutton_a-p-h_b1918"], "stint_ids": ["Dutton, A. H___Aden___1953", "Dutton, A. H___Cyprus___1949"]} -->
# Dossier case_dutton_a-p-h_b1918

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 21 official(s) with this surname in the graph's staff lists; 13 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Dutton, A. H___Aden___1953` is also gate-compatible with biography(ies) outside this case: ['dutton_a-h_b1913'] (already linked elsewhere or filtered).
- NOTE: stint `Dutton, A. H___Cyprus___1949` is also gate-compatible with biography(ies) outside this case: ['dutton_a-h_b1913'] (already linked elsewhere or filtered).

## Biography `dutton_a-p-h_b1918`

- Printed name: **DUTTON, A. P. H**
- Birth year: 1918 (attested in editions [1960, 1961, 1962, 1963, 1964, 1965])
- Honours: C.P.M, D.F.C
- Appears in editions: [1960, 1961, 1962, 1963, 1964, 1965]

### Verbatim printed entry text (OCR)

**Version `col1960-L22538.v` — printed in editions [1960, 1961, 1962, 1963, 1964, 1965]:**

> DUTTON, A. P. H., D.F.C., C.P.M.—b. 1918; ed. Diocesan Coll., Cape Town; mil. serv., 1941–46, R.A.F.; police, Bech. Prot., 1939; asst. comsnr., police, Cyp., 1956; chief police offr., Sey., 1959.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1939 | police | Bechuanaland | [1960, 1961, 1962, 1963, 1964, 1965] |
| 1 | 1956 | asst. comsnr., police | Cyprus | [1960, 1961, 1962, 1963, 1964, 1965] |
| 2 | 1959 | chief police offr. | Seychelles | [1960, 1961, 1962, 1963, 1964, 1965] |

## Candidate stint `Dutton, A. H___Aden___1953`

- Staff-list name: **Dutton, A. H** | colony: **Aden** | listed 1953–1959 | editions [1953, 1954, 1955, 1956, 1957, 1958, 1959]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1953 | A. H. Dutton | Assistant Chief Secretaries | Civil Establishment | — | — |
| 1954 | A. H. Dutton | Assistant Chief Secretary | Civil Establishment | — | — |
| 1955 | A. H. Dutton | Assistant Chief Secretary | Civil Establishment | M.V.O. | — |
| 1956 | A. H. Dutton | Financial Secretary | Civil Establishment | — | — |
| 1957 | A. H. Dutton | Financial Secretary | Civil Establishment | — | — |
| 1958 | A. H. Dutton | Financial Secretary | Civil Establishment | C.M.G. | — |
| 1959 | A. H. Dutton | Financial Secretary | Civil Establishment | C.M.G. | — |

### Deterministic checks: `dutton_a-p-h_b1918` vs `Dutton, A. H___Aden___1953`

- [PASS] surname_gate: bio 'DUTTON' vs stint 'Dutton, A. H' (exact)
- [PASS] initials: bio ['A', 'P', 'H'] ~ stint ['A', 'H']
- [PASS] age_gate: stint starts 1953, birth 1918 (age 35)
- [FAIL] colony: no placed event resolves to 'Aden'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1953-1959
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Dutton, A. H___Cyprus___1949`

- Staff-list name: **Dutton, A. H** | colony: **Cyprus** | listed 1949–1952 | editions [1949, 1951, 1952]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | A. H. Dutton | Senior Assistant Secretaries | Secretariat | — | — |
| 1951 | A. H. Dutton | Senior Assistant Secretaries | Secretariat | — | — |
| 1952 | A. H. Dutton | Commissioner | Civil Establishment | — | — |

### Deterministic checks: `dutton_a-p-h_b1918` vs `Dutton, A. H___Cyprus___1949`

- [PASS] surname_gate: bio 'DUTTON' vs stint 'Dutton, A. H' (exact)
- [PASS] initials: bio ['A', 'P', 'H'] ~ stint ['A', 'H']
- [PASS] age_gate: stint starts 1949, birth 1918 (age 31)
- [PASS] colony: 1 placed event(s) resolve to 'Cyprus'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1949-1952
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

