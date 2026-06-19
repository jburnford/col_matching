<!-- {"case_id": "case_rowlands_j-m_b1925", "bio_ids": ["rowlands_j-m_b1925"], "stint_ids": ["Rowlands, J. M___Hong Kong___1958"]} -->
# Dossier case_rowlands_j-m_b1925

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 5 official(s) with this surname in the graph's staff lists; 5 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `rowlands_j-m_b1925`

- Printed name: **ROWLANDS, J. M**
- Birth year: 1925 (attested in editions [1963, 1964, 1965, 1966])
- Appears in editions: [1963, 1964, 1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1963-L24419.v` — printed in editions [1963, 1964, 1965, 1966]:**

> ROWLANDS, J. M.—b. 1925; ed. Charterhouse and Selwyn Coll., Camb.; mil. serv., 1944-47, R.A., capt.; admin. offr., H.K., 1952; senr. admin. offr., 1961; asst. dir. urban services, 1962; admin. offr., staff gr. C, 1965.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1952 | admin. offr. | Hong Kong | [1963, 1964, 1965, 1966] |
| 1 | 1961 | senr. admin. offr | Hong Kong *(inherited from previous clause)* | [1963, 1964, 1965, 1966] |
| 2 | 1962 | asst. dir. urban services | Hong Kong *(inherited from previous clause)* | [1963, 1964, 1965, 1966] |
| 3 | 1965 | admin. offr., staff gr. C | Hong Kong *(inherited from previous clause)* | [1963, 1964, 1965, 1966] |

## Candidate stint `Rowlands, J. M___Hong Kong___1958`

- Staff-list name: **Rowlands, J. M** | colony: **Hong Kong** | listed 1958–1960 | editions [1958, 1959, 1960]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1958 | J. M. Rowlands | Chief Staff Officer, Civil Aid Services | Civil Establishment | — | — |
| 1959 | J. M. Rowlands | Chief Staff Officer, Civil Aid Services | Civil Establishment | — | — |
| 1960 | J. M. Rowlands | Chief Staff Officer, Civil Aid Services | Civil Establishment | — | — |

### Deterministic checks: `rowlands_j-m_b1925` vs `Rowlands, J. M___Hong Kong___1958`

- [PASS] surname_gate: bio 'ROWLANDS' vs stint 'Rowlands, J. M' (exact)
- [PASS] initials: bio ['J', 'M'] ~ stint ['J', 'M']
- [PASS] age_gate: stint starts 1958, birth 1925 (age 33)
- [PASS] colony: 4 placed event(s) resolve to 'Hong Kong'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1958-1960
- [FAIL] position_sim: best 45 vs bar 60: 'senr. admin. offr' ~ 'Chief Staff Officer, Civil Aid Services'
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

