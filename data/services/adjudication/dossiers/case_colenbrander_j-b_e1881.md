<!-- {"case_id": "case_colenbrander_j-b_e1881", "bio_ids": ["colenbrander_j-b_e1881"], "stint_ids": ["Colenbrander, B___Natal___1899", "Colenbrander, B___Zululand___1894"]} -->
# Dossier case_colenbrander_j-b_e1881

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 4 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `colenbrander_j-b_e1881`

- Printed name: **COLENBRANDER, J. B**
- Birth year: not printed
- Appears in editions: [1883]

### Verbatim printed entry text (OCR)

**Version `col1883-L26921.v` — printed in editions [1883]:**

> COLENBRANDER, J. B.—Clerk to border agent, Lower Tugela, Natal, Oct., 1881.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1881 | Clerk to border agent, Lower Tugela | Natal | [1883] |

## Candidate stint `Colenbrander, B___Natal___1899`

- Staff-list name: **Colenbrander, B** | colony: **Natal** | listed 1899–1910 | editions [1899, 1905, 1906, 1907, 1910]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1899 | B. Colenbrander | Clerk and Interpreter | Resident Magistrates | — | — |
| 1905 | B. Colenbrander | Civil Commissioner | Province of Zululand | — | — |
| 1906 | B. Colenbrander | Commissioner for Native Affairs, Zululand | Province of Zululand | — | — |
| 1907 | B. Colenbrander | — | Zululand | — | — |
| 1910 | B. Colenbrander | Magistrate | Magistrates | — | — |

### Deterministic checks: `colenbrander_j-b_e1881` vs `Colenbrander, B___Natal___1899`

- [PASS] surname_gate: bio 'COLENBRANDER' vs stint 'Colenbrander, B' (exact)
- [PASS] initials: bio ['J', 'B'] ~ stint ['B']
- [PASS] age_gate: stint starts 1899; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Natal'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1899-1910
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Colenbrander, B___Zululand___1894`

- Staff-list name: **Colenbrander, B** | colony: **Zululand** | listed 1894–1897 | editions [1894, 1896, 1897]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1894 | B. Colenbrander | Clerk and Interpreter | Resident Magistrates | — | — |
| 1896 | B. Colenbrander | Clerk and Interpreter | Resident Magistrates | — | — |
| 1897 | B. Colenbrander | Clerk and Interpreter | Resident Magistrates | — | — |
| 1897 | B. Colenbrander | Interpreter, Entonjaneni | Mining Commissioner of Mines | — | — |

### Deterministic checks: `colenbrander_j-b_e1881` vs `Colenbrander, B___Zululand___1894`

- [PASS] surname_gate: bio 'COLENBRANDER' vs stint 'Colenbrander, B' (exact)
- [PASS] initials: bio ['J', 'B'] ~ stint ['B']
- [PASS] age_gate: stint starts 1894; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Zululand'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1894-1897
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

