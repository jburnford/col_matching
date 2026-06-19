<!-- {"case_id": "case_templeton_j-s_b1906", "bio_ids": ["templeton_j-s_b1906"], "stint_ids": ["Templeton, J. S___Kenya___1949"]} -->
# Dossier case_templeton_j-s_b1906

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 8 official(s) with this surname in the graph's staff lists; 5 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `templeton_j-s_b1906`

- Printed name: **TEMPLETON, J. S**
- Birth year: 1906 (attested in editions [1958, 1959, 1960, 1961, 1962, 1963, 1964])
- Appears in editions: [1958, 1959, 1960, 1961, 1962, 1963, 1964]

### Verbatim printed entry text (OCR)

**Version `col1958-L27480.v` — printed in editions [1958, 1959, 1960, 1961, 1962, 1963, 1964]:**

> TEMPLETON, J. S.—b. 1906; barrister-at-law, Lincoln's Inn; shorthand writer, jud. dept., Ken., 1936; legal asst. 1944; crown coun., 1949; senr., 1955; puisne judge, 1957-63. (Ken. Govt. service.)

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1936 | shorthand writer, jud. dept. | Kenya | [1958, 1959, 1960, 1961, 1962, 1963, 1964] |
| 1 | 1944 | legal asst | Kenya *(inherited from previous clause)* | [1958, 1959, 1960, 1961, 1962, 1963, 1964] |
| 2 | 1949 | crown coun | Kenya *(inherited from previous clause)* | [1958, 1959, 1960, 1961, 1962, 1963, 1964] |
| 3 | 1955 | senr | Kenya *(inherited from previous clause)* | [1958, 1959, 1960, 1961, 1962, 1963, 1964] |
| 4 | 1957–1963 | puisne judge | Kenya *(inherited from previous clause)* | [1958, 1959, 1960, 1961, 1962, 1963, 1964] |

## Candidate stint `Templeton, J. S___Kenya___1949`

- Staff-list name: **Templeton, J. S** | colony: **Kenya** | listed 1949–1951 | editions [1949, 1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | J. S. Templeton | Legal Assistant | Legal | — | — |
| 1950 | J. S. Templeton | Legal Assistant | LEGAL | — | — |
| 1951 | J. S. Templeton | Crown Counsel | LEGAL | — | — |

### Deterministic checks: `templeton_j-s_b1906` vs `Templeton, J. S___Kenya___1949`

- [PASS] surname_gate: bio 'TEMPLETON' vs stint 'Templeton, J. S' (exact)
- [PASS] initials: bio ['J', 'S'] ~ stint ['J', 'S']
- [PASS] age_gate: stint starts 1949, birth 1906 (age 43)
- [PASS] colony: 5 placed event(s) resolve to 'Kenya'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1949-1951
- [PASS] position_sim: best 87 vs bar 60: 'crown coun' ~ 'Crown Counsel'
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

