<!-- {"case_id": "case_crockford_a-c_b1898", "bio_ids": ["crockford_a-c_b1898"], "stint_ids": ["Crockford, A. C___Malta___1929", "Crockford, A. C___Malta___1949"]} -->
# Dossier case_crockford_a-c_b1898

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `crockford_a-c_b1898`

- Printed name: **CROCKFORD, A. C**
- Birth year: 1898 (attested in editions [1955, 1956])
- Appears in editions: [1955, 1956]

### Verbatim printed entry text (OCR)

**Version `col1955-L20305.v` — printed in editions [1955, 1956]:**

> CROCKFORD, A. C.—b. 1898; ed. Lyceum, Malta; civ. serv. (admin.), Malta, 1921; asst. manager, milk marketing undertaking, 1941; man., 1943; P.M.G., 1951.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1921 | civ. serv. (admin.) | Malta | [1955, 1956] |
| 1 | 1941 | asst. manager, milk marketing undertaking | Malta *(inherited from previous clause)* | [1955, 1956] |
| 2 | 1943 | man | Malta *(inherited from previous clause)* | [1955, 1956] |
| 3 | 1951 | P.M.G | Malta *(inherited from previous clause)* | [1955, 1956] |

## Candidate stint `Crockford, A. C___Malta___1929`

- Staff-list name: **Crockford, A. C** | colony: **Malta** | listed 1929–1930 | editions [1929, 1930]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1929 | A. Crockford | Clerks, 2nd Class | Customs and Port Department | — | — |
| 1930 | A. Crockford | Clerks, 2nd Class | Customs and Port Department | — | — |

### Deterministic checks: `crockford_a-c_b1898` vs `Crockford, A. C___Malta___1929`

- [PASS] surname_gate: bio 'CROCKFORD' vs stint 'Crockford, A. C' (exact)
- [PASS] initials: bio ['A', 'C'] ~ stint ['A', 'C']
- [PASS] age_gate: stint starts 1929, birth 1898 (age 31)
- [PASS] colony: 4 placed event(s) resolve to 'Malta'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1929-1930
- [FAIL] position_sim: best 40 vs bar 60: 'civ. serv. (admin.)' ~ 'Clerks, 2nd Class'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

## Candidate stint `Crockford, A. C___Malta___1949`

- Staff-list name: **Crockford, A. C** | colony: **Malta** | listed 1949–1955 | editions [1949, 1950, 1951, 1952, 1953, 1954, 1955]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | A. C. Crockford | Manager | Milk Marketing Undertaking | — | — |
| 1950 | A. C. Crockford | Manager | MILK MARKETING UNDERTAKING | — | — |
| 1951 | A. C. Crockford | Manager | Milk Marketing Undertaking | — | — |
| 1952 | A. C. Crockford | Postmaster-General | Maltese Government | — | — |
| 1953 | A. C. Crockford | Postmaster-General | The Maltese Government | — | — |
| 1954 | A. C. Crockford | Postmaster-General | The Maltese Government | — | — |
| 1955 | A. C. Crockford | Postmaster-General | THE MALTESE GOVERNMENT | — | — |

### Deterministic checks: `crockford_a-c_b1898` vs `Crockford, A. C___Malta___1949`

- [PASS] surname_gate: bio 'CROCKFORD' vs stint 'Crockford, A. C' (exact)
- [PASS] initials: bio ['A', 'C'] ~ stint ['A', 'C']
- [PASS] age_gate: stint starts 1949, birth 1898 (age 51)
- [PASS] colony: 4 placed event(s) resolve to 'Malta'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1949-1955
- [PASS] position_sim: best 60 vs bar 60: 'man' ~ 'Manager'
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

