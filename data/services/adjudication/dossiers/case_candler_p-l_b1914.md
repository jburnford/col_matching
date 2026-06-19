<!-- {"case_id": "case_candler_p-l_b1914", "bio_ids": ["candler_p-l_b1914"], "stint_ids": ["Candler, P. L___Kenya___1949"]} -->
# Dossier case_candler_p-l_b1914

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 4 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `candler_p-l_b1914`

- Printed name: **CANDLER, P. L**
- Birth year: 1914 (attested in editions [1964])
- Appears in editions: [1958, 1959, 1960, 1961, 1962, 1963, 1964]

### Verbatim printed entry text (OCR)

**Version `col1964-L15493.v` — printed in editions [1964]:**

> CANDLER, P. L.—b. 1914; ed. Sherborne Sch., Camb. Univ., and St. Bart's Hosp.; mil. serv., 1939-45, lt.-col., R.A.M.C.; M.O., Ken., 1946; speclst. (obstetrician and gynaecologist), 1962-63. (Ken. Govt. service.)

**Version `col1958-L21180.v` — printed in editions [1958, 1959, 1960, 1961, 1962, 1963]:**

> CANDLER, P. L.—b. 1914; ed. Sherborne Sch., Camb., Univ., and St. Bart's Hosp.; mil. serv., 1939-45, lt.-col., R.A.M.C.; M.O., Ken., 1946.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1946 | M.O. | Kenya | [1958, 1959, 1960, 1961, 1962, 1963, 1964] |
| 1 | 1962–1963 | speclst. (obstetrician and gynaecologist) | Kenya *(inherited from previous clause)* | [1964] |

## Candidate stint `Candler, P. L___Kenya___1949`

- Staff-list name: **Candler, P. L** | colony: **Kenya** | listed 1949–1951 | editions [1949, 1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | P. L. Candler | Medical Officer | Medical | — | — |
| 1950 | P. L. Candler | Medical Officer | Medical | — | — |
| 1951 | P. L. Candler | Medical Officer | Medical | — | — |

### Deterministic checks: `candler_p-l_b1914` vs `Candler, P. L___Kenya___1949`

- [PASS] surname_gate: bio 'CANDLER' vs stint 'Candler, P. L' (exact)
- [PASS] initials: bio ['P', 'L'] ~ stint ['P', 'L']
- [PASS] age_gate: stint starts 1949, birth 1914 (age 35)
- [PASS] colony: 2 placed event(s) resolve to 'Kenya'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1949-1951
- [FAIL] position_sim: best 24 vs bar 60: 'M.O.' ~ 'Medical Officer'
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

