<!-- {"case_id": "case_snell_james_e1866", "bio_ids": ["snell_james_e1866"], "stint_ids": ["Snell, E. J___Gambia___1936", "Snell, James___South Australia___1877"]} -->
# Dossier case_snell_james_e1866

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 16 official(s) with this surname in the graph's staff lists; 5 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['snell_james_e1866'] carry a single initial only — the namesake trap applies.

## Biography `snell_james_e1866`

- Printed name: **SNELL, James**
- Birth year: not printed
- Appears in editions: [1886, 1888]

### Verbatim printed entry text (OCR)

**Version `col1886-L35781.v` — printed in editions [1886, 1888]:**

> SNELL, James.—Temporary clerk, chief secretary's office, South Australia, 11th January, 1866; clerk in audit office, 1st May, 1866; accountant engineer-in-chief's office, 1st May, 1873; chief clerk, 20th March, 1874; chief clerk, audit office, 11th July, 1874; chief clerk and accountant, office of agent-general, 12th August, 1874.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1866 | Temporary clerk, chief secretary's office | South Australia | [1886, 1888] |
| 1 | 1873 | accountant engineer-in-chief's office | South Australia *(inherited from previous clause)* | [1886, 1888] |
| 2 | 1874 | chief clerk | South Australia *(inherited from previous clause)* | [1886, 1888] |

## Candidate stint `Snell, E. J___Gambia___1936`

- Staff-list name: **Snell, E. J** | colony: **Gambia** | listed 1936–1940 | editions [1936, 1937, 1939, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1936 | E. J. Snell | Senior Sanitary Superintendent | Health Department | — | — |
| 1937 | E. J. Snell | Senior Sanitary Superintendent | Health Department | — | — |
| 1939 | E. J. Snell | Senior Sanitary Superintendent | Health Department | — | — |
| 1940 | E. J. Snell | Senior Sanitary Superintendent | Health Department | — | — |

### Deterministic checks: `snell_james_e1866` vs `Snell, E. J___Gambia___1936`

- [PASS] surname_gate: bio 'SNELL' vs stint 'Snell, E. J' (exact)
- [PASS] initials: bio ['J'] ~ stint ['E', 'J']
- [PASS] age_gate: stint starts 1936; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Gambia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1936-1940
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Snell, James___South Australia___1877`

- Staff-list name: **Snell, James** | colony: **South Australia** | listed 1877–1880 | editions [1877, 1878, 1879, 1880]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | James Snell | Chief Clerk | Agent-General's Department (London). | — | — |
| 1878 | James Snell | Chief Clerk | Agent-General's Department (London) | — | — |
| 1879 | James Snell | Chief Clerk | Agent-General's Department (London) | — | — |
| 1880 | James Snell | Chief Clerk | Agent-General's Department (London) | — | — |

### Deterministic checks: `snell_james_e1866` vs `Snell, James___South Australia___1877`

- [PASS] surname_gate: bio 'SNELL' vs stint 'Snell, James' (exact)
- [PASS] initials: bio ['J'] ~ stint ['J']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [PASS] colony: 3 placed event(s) resolve to 'South Australia'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1877-1880
- [PASS] position_sim: best 100 vs bar 60: 'chief clerk' ~ 'Chief Clerk'
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

