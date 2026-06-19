<!-- {"case_id": "case_guthrie_r-i_b1916", "bio_ids": ["guthrie_r-i_b1916"], "stint_ids": ["Guthrie, R. I___Kenya___1949"]} -->
# Dossier case_guthrie_r-i_b1916

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 20 official(s) with this surname in the graph's staff lists; 7 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `guthrie_r-i_b1916`

- Printed name: **GUTHRIE, R. I**
- Birth year: 1916 (attested in editions [1958, 1959, 1960, 1961, 1962, 1963, 1964])
- Appears in editions: [1958, 1959, 1960, 1961, 1962, 1963, 1964]

### Verbatim printed entry text (OCR)

**Version `col1958-L23197.v` — printed in editions [1958, 1959, 1960, 1961, 1962, 1963, 1964]:**

> GUTHRIE, R. I.—b. 1916; ed. Kirkcaldy High Sch. and Edin. Univ.; advocate, Scots Bar; mil. serv., 1939-45, capt.; ast. audr., Ken., 1946; audr., 1948; legal ast., 1951; crown coun., 1953; legal dftsman., 1957; solr.-gen., 1962-63. (Ken. Govt. service.)

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1946 | ast. audr. | Kenya | [1958, 1959, 1960, 1961, 1962, 1963, 1964] |
| 1 | 1948 | audr | Kenya *(inherited from previous clause)* | [1958, 1959, 1960, 1961, 1962, 1963, 1964] |
| 2 | 1951 | legal ast | Kenya *(inherited from previous clause)* | [1958, 1959, 1960, 1961, 1962, 1963, 1964] |
| 3 | 1953 | crown coun | Kenya *(inherited from previous clause)* | [1958, 1959, 1960, 1961, 1962, 1963, 1964] |
| 4 | 1957 | legal dftsman | Kenya *(inherited from previous clause)* | [1958, 1959, 1960, 1961, 1962, 1963, 1964] |
| 5 | 1962–1963 | solr.-gen | Kenya *(inherited from previous clause)* | [1958, 1959, 1960, 1961, 1962, 1963, 1964] |

## Candidate stint `Guthrie, R. I___Kenya___1949`

- Staff-list name: **Guthrie, R. I** | colony: **Kenya** | listed 1949–1951 | editions [1949, 1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | R. I. Guthrie | Auditors and Assistant Auditors | Audit | — | — |
| 1950 | R. I. Guthrie | Auditors and Assistant Auditors | AUDIT | — | — |
| 1951 | R. I. Guthrie | Auditors and Assistant Auditors | Audit | — | — |

### Deterministic checks: `guthrie_r-i_b1916` vs `Guthrie, R. I___Kenya___1949`

- [PASS] surname_gate: bio 'GUTHRIE' vs stint 'Guthrie, R. I' (exact)
- [PASS] initials: bio ['R', 'I'] ~ stint ['R', 'I']
- [PASS] age_gate: stint starts 1949, birth 1916 (age 33)
- [PASS] colony: 6 placed event(s) resolve to 'Kenya'
- [PASS] tenure_overlap: 3 event tenure(s) overlap stint years 1949-1951
- [FAIL] position_sim: best 53 vs bar 60: 'ast. audr.' ~ 'Auditors and Assistant Auditors'
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

