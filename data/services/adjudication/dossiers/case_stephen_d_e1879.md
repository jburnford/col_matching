<!-- {"case_id": "case_stephen_d_e1879", "bio_ids": ["stephen_d_e1879"], "stint_ids": ["Stephen, D. A___Singapore___1949", "Stephen, D___Cape of Good Hope___1896"]} -->
# Dossier case_stephen_d_e1879

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 22 official(s) with this surname in the graph's staff lists; 13 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['stephen_d_e1879'] carry a single initial only — the namesake trap applies.
- NOTE: stint `Stephen, D. A___Singapore___1949` is also gate-compatible with biography(ies) outside this case: ['stephen_alfred_e1823'] (already linked elsewhere or filtered).

## Biography `stephen_d_e1879`

- Printed name: **STEPHEN, D.**
- Birth year: not printed
- Appears in editions: [1886]

### Verbatim printed entry text (OCR)

**Version `col1886-L35834.v` — printed in editions [1886]:**

> STEPHEN, D.—In Transvaal Civil Service from Mar., 1879 to 1881, as clerk in the Colonial Office; appointed third class clerk, Civil Service, Natal, 9th Aug., 1881; second class clerk, 14th Aug., 1881.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1879–1881 | clerk | Transvaal | [1886] |
| 1 | 1881 | third class clerk | Natal | [1886] |

## Candidate stint `Stephen, D. A___Singapore___1949`

- Staff-list name: **Stephen, D. A** | colony: **Singapore** | listed 1949–1951 | editions [1949, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | D. A. Stephen | Deputy Chief Administrative Officer | Broadcasting | — | — |
| 1951 | D. A. Stephen | Chief Administrative Officer | Broadcasting | — | — |
| 1951 | D. A. Stephen | Administrative Officers under Contract | Administration | — | — |

### Deterministic checks: `stephen_d_e1879` vs `Stephen, D. A___Singapore___1949`

- [PASS] surname_gate: bio 'STEPHEN' vs stint 'Stephen, D. A' (exact)
- [PASS] initials: bio ['D'] ~ stint ['D', 'A']
- [PASS] age_gate: stint starts 1949; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Singapore'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1949-1951
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Stephen, D___Cape of Good Hope___1896`

- Staff-list name: **Stephen, D** | colony: **Cape of Good Hope** | listed 1896–1908 | editions [1896, 1897, 1898, 1899, 1900, 1905, 1906, 1907, 1908]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1896 | D. Stephen | Acting Principal Clerk, General Correspondence | General Post Office | — | — |
| 1897 | D. Stephen | Assistant Secretary and Accountant, Telegraph Messages | General Post Office | — | — |
| 1898 | D. Stephen | Principal Clerk, General Correspondence Branch | General Post Office | — | — |
| 1899 | D. Stephen | Telegraph Messages Branch | Principal Clerks | — | — |
| 1900 | D. Stephen | Principal Clerk | Principal Clerks | — | — |
| 1905 | D. Stephen | Assistant Accountant | General Post Office | — | — |
| 1906 | D. Stephen | Assistant Accountant | General Post Office | — | — |
| 1907 | D. Stephen | Assistant Accountant | General Post Office | — | — |
| 1908 | D. Stephen | Assistant Accountant | General Post Office | — | — |

### Deterministic checks: `stephen_d_e1879` vs `Stephen, D___Cape of Good Hope___1896`

- [PASS] surname_gate: bio 'STEPHEN' vs stint 'Stephen, D' (exact)
- [PASS] initials: bio ['D'] ~ stint ['D']
- [PASS] age_gate: stint starts 1896; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Cape of Good Hope'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1896-1908
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

