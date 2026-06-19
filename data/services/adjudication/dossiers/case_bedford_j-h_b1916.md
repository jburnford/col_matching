<!-- {"case_id": "case_bedford_j-h_b1916", "bio_ids": ["bedford_j-h_b1916"], "stint_ids": ["Bedford, J. H___Sierra Leone___1957"]} -->
# Dossier case_bedford_j-h_b1916

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 7 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `bedford_j-h_b1916`

- Printed name: **BEDFORD, J. H**
- Birth year: 1916 (attested in editions [1956, 1957, 1958, 1959, 1960, 1961, 1962])
- Honours: M.B.E (1943)
- Appears in editions: [1956, 1957, 1958, 1959, 1960, 1961, 1962]

### Verbatim printed entry text (OCR)

**Version `col1956-L19697.v` — printed in editions [1956, 1957, 1958, 1959, 1960, 1961, 1962]:**

> BEDFORD, J. H., M.B.E. (1943).—b. 1916; collr., customs, Nig., 1946; senr. collr., 1951; dep. compt., customs, S.L., 1953; compt., 1955.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1946 | collr., customs | Nigeria | [1956, 1957, 1958, 1959, 1960, 1961, 1962] |
| 1 | 1951 | senr. collr | Nigeria *(inherited from previous clause)* | [1956, 1957, 1958, 1959, 1960, 1961, 1962] |
| 2 | 1953 | dep. compt., customs | Sierra Leone | [1956, 1957, 1958, 1959, 1960, 1961, 1962] |
| 3 | 1955 | compt | Sierra Leone *(inherited from previous clause)* | [1956, 1957, 1958, 1959, 1960, 1961, 1962] |

## Candidate stint `Bedford, J. H___Sierra Leone___1957`

- Staff-list name: **Bedford, J. H** | colony: **Sierra Leone** | listed 1957–1960 | editions [1957, 1958, 1959, 1960]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1957 | J. H. Bedford | Comptroller of Customs | Civil Establishment | — | — |
| 1958 | J. H. Bedford | Comptroller of Customs | Civil Establishment | — | — |
| 1959 | J. H. Bedford | Comptroller of Customs | Civil Establishment | — | — |
| 1960 | J. H. Bedford | Comptroller of Customs | Civil Establishment | — | — |

### Deterministic checks: `bedford_j-h_b1916` vs `Bedford, J. H___Sierra Leone___1957`

- [PASS] surname_gate: bio 'BEDFORD' vs stint 'Bedford, J. H' (exact)
- [PASS] initials: bio ['J', 'H'] ~ stint ['J', 'H']
- [PASS] age_gate: stint starts 1957, birth 1916 (age 41)
- [PASS] colony: 2 placed event(s) resolve to 'Sierra Leone'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1957-1960
- [FAIL] position_sim: best 37 vs bar 60: 'compt' ~ 'Comptroller of Customs'
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

