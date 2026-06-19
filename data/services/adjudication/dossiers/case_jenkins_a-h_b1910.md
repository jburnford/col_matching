<!-- {"case_id": "case_jenkins_a-h_b1910", "bio_ids": ["jenkins_a-h_b1910"], "stint_ids": ["Jenkins, A. H___British Guiana___1963", "Jenkins, A. H___Falkland Islands___1949"]} -->
# Dossier case_jenkins_a-h_b1910

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 39 official(s) with this surname in the graph's staff lists; 20 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `jenkins_a-h_b1910`

- Printed name: **JENKINS, A. H**
- Birth year: 1910 (attested in editions [1960, 1964])
- Honours: C.P.M (1959), Q.P.M (1963)
- Appears in editions: [1960, 1964]

### Verbatim printed entry text (OCR)

**Version `col1960-L24615.v` — printed in editions [1960, 1964]:**

> JENKINS, Lt-Col. A. H., Q.P.M. (1963), C.P.M. (1959).—b. 1910; ed. Ardwyn Sch., Aberystwyth; mil. serv., 1927-31 (R.A.F.); Cardiganshire police, 1931-45; senr. cler. and acctng. serv., H.K., 1946; ch. const., Falk. Is., 1948; dep. supt., police, Grenada, 1951; supt., St. V., 1952; senr., B. Guiana, 1954; asst. comsnr., 1960; dep. comsnr., 1962.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1931–1945 | Cardiganshire police | — | [1960, 1964] |
| 1 | 1946 | senr. cler. and acctng. serv. | Hong Kong | [1960, 1964] |
| 2 | 1948 | ch. const. | Falkland Islands | [1960, 1964] |
| 3 | 1951 | dep. supt., police | Grenada | [1960, 1964] |
| 4 | 1952 | supt. | St. Vincent | [1960, 1964] |
| 5 | 1954 | senr., B. Guiana | St. Vincent *(inherited from previous clause)* | [1960, 1964] |
| 6 | 1960 | asst. comsnr | St. Vincent *(inherited from previous clause)* | [1960, 1964] |
| 7 | 1962 | dep. comsnr | St. Vincent *(inherited from previous clause)* | [1960, 1964] |

## Candidate stint `Jenkins, A. H___British Guiana___1963`

- Staff-list name: **Jenkins, A. H** | colony: **British Guiana** | listed 1963–1965 | editions [1963, 1964, 1965]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1963 | A. H. Jenkins | Deputy Commissioner of Police | Civil Establishment | — | — |
| 1964 | A. H. Jenkins | Deputy Commissioner of Police | Civil Establishment | — | — |
| 1965 | A. H. Jenkins | Deputy Commissioner of Police | Civil Establishment | Q.P.M. | — |

### Deterministic checks: `jenkins_a-h_b1910` vs `Jenkins, A. H___British Guiana___1963`

- [PASS] surname_gate: bio 'JENKINS' vs stint 'Jenkins, A. H' (exact)
- [PASS] initials: bio ['A', 'H'] ~ stint ['A', 'H']
- [PASS] age_gate: stint starts 1963, birth 1910 (age 53)
- [FAIL] colony: no placed event resolves to 'British Guiana'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1963-1965
- [FAIL] position_sim: no overlapping placed event to compare
- [PASS] honour: shared: Q.P.M
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Jenkins, A. H___Falkland Islands___1949`

- Staff-list name: **Jenkins, A. H** | colony: **Falkland Islands** | listed 1949–1951 | editions [1949, 1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | A. H. Jenkins | Chief Constable and Keeper of Prisons | Police and Prisons | — | — |
| 1950 | A. H. Jenkins | Chief Constable and Keeper of Prisons | POLICE AND PRISONS | — | — |
| 1951 | A. H. Jenkins | Chief Constable and Keeper of Prisons | Police and Prisons | — | — |

### Deterministic checks: `jenkins_a-h_b1910` vs `Jenkins, A. H___Falkland Islands___1949`

- [PASS] surname_gate: bio 'JENKINS' vs stint 'Jenkins, A. H' (exact)
- [PASS] initials: bio ['A', 'H'] ~ stint ['A', 'H']
- [PASS] age_gate: stint starts 1949, birth 1910 (age 39)
- [PASS] colony: 1 placed event(s) resolve to 'Falkland Islands'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1949-1951
- [FAIL] position_sim: best 36 vs bar 60: 'ch. const.' ~ 'Chief Constable and Keeper of Prisons'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

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

