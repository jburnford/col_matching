<!-- {"case_id": "case_cleland_j-f_e1838", "bio_ids": ["cleland_j-f_e1838"], "stint_ids": ["Cleland, J. F___South Australia___1877", "Cleland, J. F___South Australia___1888"]} -->
# Dossier case_cleland_j-f_e1838

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 10 official(s) with this surname in the graph's staff lists; 6 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `cleland_j-f_e1838`

- Printed name: **CLELAND, J. F**
- Birth year: not printed
- Appears in editions: [1886, 1888, 1889, 1890]

### Verbatim printed entry text (OCR)

**Version `col1886-L32698.v` — printed in editions [1886, 1888, 1889, 1890]:**

> CLELAND, J. F.—Registrar-general, South Australia, 1st Jan., 1838.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1838 | Registrar-general | South Australia | [1886, 1888, 1889, 1890] |

## Candidate stint `Cleland, J. F___South Australia___1877`

- Staff-list name: **Cleland, J. F** | colony: **South Australia** | listed 1877–1880 | editions [1877, 1878, 1879, 1880]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | J. F. Cleland | Registrar-General | Registrar-General of Births, Deaths, and Marriages | — | — |
| 1878 | J. F. Cleland | Registrar-General | Registrar-General of Births, Deaths, and Marriages | — | — |
| 1879 | J. F. Cleland | Registrar-General | Registrar-General of Births, Deaths, and Marriages | — | — |
| 1880 | J. F. Cleland | Registrar-General | Registrar-General of Births, Deaths, and Marriages | — | — |

### Deterministic checks: `cleland_j-f_e1838` vs `Cleland, J. F___South Australia___1877`

- [PASS] surname_gate: bio 'CLELAND' vs stint 'Cleland, J. F' (exact)
- [PASS] initials: bio ['J', 'F'] ~ stint ['J', 'F']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'South Australia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1877-1880
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Cleland, J. F___South Australia___1888`

- Staff-list name: **Cleland, J. F** | colony: **South Australia** | listed 1888–1889 | editions [1888, 1889]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1888 | J. F. Cleland | Deputy Registrar-General | Registrar-General of Births, Deaths, and Marriages | — | — |
| 1889 | J. F. Cleland | Deputy Registrar-General | Registrar-General of Births, Deaths, and Marriages | — | — |

### Deterministic checks: `cleland_j-f_e1838` vs `Cleland, J. F___South Australia___1888`

- [PASS] surname_gate: bio 'CLELAND' vs stint 'Cleland, J. F' (exact)
- [PASS] initials: bio ['J', 'F'] ~ stint ['J', 'F']
- [PASS] age_gate: stint starts 1888; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'South Australia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1888-1889
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

