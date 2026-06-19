<!-- {"case_id": "case_truter_j-l_e1879", "bio_ids": ["truter_j-l_e1879"], "stint_ids": ["Truter, J. L___Cape of Good Hope___1883", "Truter, J. L___Griqualand West___1877"]} -->
# Dossier case_truter_j-l_e1879

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 8 official(s) with this surname in the graph's staff lists; 4 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `truter_j-l_e1879`

- Printed name: **TRUTER, J. L**
- Birth year: not printed
- Appears in editions: [1883, 1886, 1888, 1889, 1890, 1894]

### Verbatim printed entry text (OCR)

**Version `col1883-L29810.v` — printed in editions [1883, 1886, 1888, 1889, 1890, 1894]:**

> TRUTER, J. L.—Resident magistrate, Kimberley, Cape Colony, Jan., 1879.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1879 | Resident magistrate, Kimberley | Cape of Good Hope | [1883, 1886, 1888, 1889, 1890, 1894] |

## Candidate stint `Truter, J. L___Cape of Good Hope___1883`

- Staff-list name: **Truter, J. L** | colony: **Cape of Good Hope** | listed 1883–1894 | editions [1883, 1888, 1889, 1890, 1894]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1883 | J. L. Truter | Member | Special Court (Diamond Trade Act) | — | — |
| 1888 | J. L. Truter | Member, Judges of High Court | Special Court (Diamond Trude Act) | — | — |
| 1889 | J. L. Truter | Judge | Special Court (Diamond Trade Act) | — | — |
| 1890 | J. L. Truter | R.M. | DIVISION OF KIMBERLEY | — | — |
| 1890 | J. L. Truter | Judge | Special Court (Diamond Trade Act) | — | — |
| 1894 | J. L. Truter | Judge of High Court | Special Court (Diamond Trade Act) | — | — |

### Deterministic checks: `truter_j-l_e1879` vs `Truter, J. L___Cape of Good Hope___1883`

- [PASS] surname_gate: bio 'TRUTER' vs stint 'Truter, J. L' (exact)
- [PASS] initials: bio ['J', 'L'] ~ stint ['J', 'L']
- [PASS] age_gate: stint starts 1883; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Cape of Good Hope'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1883-1894
- [FAIL] position_sim: best 29 vs bar 60: 'Resident magistrate, Kimberley' ~ 'Member'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

## Candidate stint `Truter, J. L___Griqualand West___1877`

- Staff-list name: **Truter, J. L** | colony: **Griqualand West** | listed 1877–1880 | editions [1877, 1879, 1880]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | J. L. Truter | Chief Clerk and Accountant | Treasury | — | — |
| 1879 | J. L. Truter | Distributor of Stamps | Treasury | — | — |
| 1880 | J. L. Truter | Resident Magistrate | DIVISION AND DISTRICT OF KIMBERLEY | — | — |

### Deterministic checks: `truter_j-l_e1879` vs `Truter, J. L___Griqualand West___1877`

- [PASS] surname_gate: bio 'TRUTER' vs stint 'Truter, J. L' (exact)
- [PASS] initials: bio ['J', 'L'] ~ stint ['J', 'L']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Griqualand West'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1877-1880
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

