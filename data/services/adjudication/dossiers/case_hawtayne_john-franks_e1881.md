<!-- {"case_id": "case_hawtayne_john-franks_e1881", "bio_ids": ["hawtayne_john-franks_e1881"], "stint_ids": ["Hawtayne, J. F. S___Cape of Good Hope___1905"]} -->
# Dossier case_hawtayne_john-franks_e1881

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 7 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `hawtayne_john-franks_e1881`

- Printed name: **HAWTAYNE, John Franks**
- Birth year: not printed
- Appears in editions: [1888, 1889]

### Verbatim printed entry text (OCR)

**Version `col1888-L33934.v` — printed in editions [1888, 1889]:**

> HAWTAYNE, John Franks.—Clerk, Army Pay department, Cape, 1881; excise officer, Pearl and Robertson, Sept., 1884; clerk to High Commissioner, Feb., 1886; clerk to receiver-general, Br. Bechuana land, Feb., 1887; ag. rec. gen. Mar., 1888.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1881 | Clerk, Army Pay department | Cape of Good Hope | [1888, 1889] |
| 1 | 1884 | excise officer, Pearl and Robertson | Cape of Good Hope *(inherited from previous clause)* | [1888, 1889] |
| 2 | 1886 | clerk to High Commissioner | Cape of Good Hope *(inherited from previous clause)* | [1888, 1889] |
| 3 | 1887 | clerk to receiver-general, Br. Bechuana land | Cape of Good Hope *(inherited from previous clause)* | [1888, 1889] |
| 4 | 1888 | ag. rec. gen | Cape of Good Hope *(inherited from previous clause)* | [1888, 1889] |

## Candidate stint `Hawtayne, J. F. S___Cape of Good Hope___1905`

- Staff-list name: **Hawtayne, J. F. S** | colony: **Cape of Good Hope** | listed 1905–1909 | editions [1905, 1906, 1907, 1908, 1909]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1905 | J. F. Hawtayne | Clerk and Accountant | Field Establishment | — | — |
| 1906 | J. F. Hawtayne | Clerks and Accountants | Field Establishment | — | — |
| 1907 | J. F. Hawtayne | Clerk and Accountant | Field Establishment | — | — |
| 1908 | J. F. Hawtayne | Clerk and Accountant | Field Establishment | — | — |
| 1909 | J. F. S. Hawtayne | Clerk | Police Branch | — | — |
| 1909 | J. F. Hawtayne | Clerk and Accountant | Field Establishment | — | — |

### Deterministic checks: `hawtayne_john-franks_e1881` vs `Hawtayne, J. F. S___Cape of Good Hope___1905`

- [PASS] surname_gate: bio 'HAWTAYNE' vs stint 'Hawtayne, J. F. S' (exact)
- [PASS] initials: bio ['J', 'F'] ~ stint ['J', 'F', 'S']
- [PASS] age_gate: stint starts 1905; no printed birth year — UNCHECKED
- [PASS] colony: 5 placed event(s) resolve to 'Cape of Good Hope'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1905-1909
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

