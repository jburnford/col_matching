<!-- {"case_id": "case_stone_j-p_e1864", "bio_ids": ["stone_j-p_e1864"], "stint_ids": ["Stone, J___Victoria___1877"]} -->
# Dossier case_stone_j-p_e1864

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 45 official(s) with this surname in the graph's staff lists; 20 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Stone, J___Victoria___1877` is also gate-compatible with biography(ies) outside this case: ['stone_j-f_e1866'] (already linked elsewhere or filtered).

## Biography `stone_j-p_e1864`

- Printed name: **STONE, J. P**
- Birth year: not printed
- Appears in editions: [1888]

### Verbatim printed entry text (OCR)

**Version `col1888-L36228.v` — printed in editions [1888]:**

> STONE, J. P.—J.P., South Australia, 1864; explored northern coast, 1865; author of "Voyage of the Forlorn Hope," and "History of South Australia;" magistrate, 1884; commissioner of insolvency and magistrate, Mount Gambier (S.A.), 1886.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1864 | J.P. | South Australia | [1888] |
| 1 | 1865 | explored northern coast | South Australia *(inherited from previous clause)* | [1888] |
| 2 | 1884 | " magistrate | South Australia *(inherited from previous clause)* | [1888] |
| 3 | 1886 | commissioner of insolvency and magistrate, Mount Gambier (S.A.) | South Australia *(inherited from previous clause)* | [1888] |

## Candidate stint `Stone, J___Victoria___1877`

- Staff-list name: **Stone, J** | colony: **Victoria** | listed 1877–1883 | editions [1877, 1879, 1880, 1883]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | J. Stone | Accountant | Penal Department | — | — |
| 1879 | J. Stone | Accountant | Penal Department | — | — |
| 1880 | J. Stone | Accountant | Penal Department | — | — |
| 1883 | J. Stone | Chief Clerk and Accountant | Penal Department | — | — |

### Deterministic checks: `stone_j-p_e1864` vs `Stone, J___Victoria___1877`

- [PASS] surname_gate: bio 'STONE' vs stint 'Stone, J' (exact)
- [PASS] initials: bio ['J', 'P'] ~ stint ['J']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Victoria'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1877-1883
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

