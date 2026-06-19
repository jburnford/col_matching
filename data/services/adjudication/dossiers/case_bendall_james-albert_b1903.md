<!-- {"case_id": "case_bendall_james-albert_b1903", "bio_ids": ["bendall_james-albert_b1903"], "stint_ids": ["Bendall, J. A___Hong Kong___1939", "Bendall, J. A___Hong Kong___1949"]} -->
# Dossier case_bendall_james-albert_b1903

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 4 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `bendall_james-albert_b1903`

- Printed name: **BENDALL, James Albert**
- Birth year: 1903 (attested in editions [1950])
- Honours: A.L.A.A
- Appears in editions: [1950]

### Verbatim printed entry text (OCR)

**Version `col1950-L33615.v` — printed in editions [1950]:**

> BENDALL, James Albert, A.L.A.A.—b. 1903; ed. St. Matthias Boys Sch.; on mil. serv., 1941–45, capt.; 2nd cl. sany, inspr., H.K., 1928; senr. exec. offr., gr. II, 1947.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1928 | 2nd cl. sany, inspr. | Hong Kong | [1950] |
| 1 | 1947 | senr. exec. offr., gr. II | Hong Kong *(inherited from previous clause)* | [1950] |

## Candidate stint `Bendall, J. A___Hong Kong___1939`

- Staff-list name: **Bendall, J. A** | colony: **Hong Kong** | listed 1939–1940 | editions [1939, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1939 | J. A. Bendall | Accountant, P.W.D. | Public Works Department | — | — |
| 1940 | J. A. Bendall | Accountant, P.W.D. | Public Works Department | — | — |

### Deterministic checks: `bendall_james-albert_b1903` vs `Bendall, J. A___Hong Kong___1939`

- [PASS] surname_gate: bio 'BENDALL' vs stint 'Bendall, J. A' (exact)
- [PASS] initials: bio ['J', 'A'] ~ stint ['J', 'A']
- [PASS] age_gate: stint starts 1939, birth 1903 (age 36)
- [PASS] colony: 2 placed event(s) resolve to 'Hong Kong'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1939-1940
- [FAIL] position_sim: best 26 vs bar 60: '2nd cl. sany, inspr.' ~ 'Accountant, P.W.D.'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

## Candidate stint `Bendall, J. A___Hong Kong___1949`

- Staff-list name: **Bendall, J. A** | colony: **Hong Kong** | listed 1949–1950 | editions [1949, 1950]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | J. A. Bendall | Accountant | Public Works | — | — |
| 1950 | J. A. Bendall | Senior Accountant | Public Works | — | — |

### Deterministic checks: `bendall_james-albert_b1903` vs `Bendall, J. A___Hong Kong___1949`

- [PASS] surname_gate: bio 'BENDALL' vs stint 'Bendall, J. A' (exact)
- [PASS] initials: bio ['J', 'A'] ~ stint ['J', 'A']
- [PASS] age_gate: stint starts 1949, birth 1903 (age 46)
- [PASS] colony: 2 placed event(s) resolve to 'Hong Kong'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1949-1950
- [FAIL] position_sim: best 38 vs bar 60: 'senr. exec. offr., gr. II' ~ 'Senior Accountant'
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

