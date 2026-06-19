<!-- {"case_id": "case_whitton_j_e1856", "bio_ids": ["whitton_j_e1856", "whitton_j_e1856-2"], "stint_ids": ["Whitton, John___New South Wales___1877"]} -->
# Dossier case_whitton_j_e1856

## Case context

- 2 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 4 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['whitton_j_e1856', 'whitton_j_e1856-2'] carry a single initial only — the namesake trap applies.
- CONTESTED: stint(s) ['Whitton, John___New South Wales___1877'] have more than one claimant biography in this case.

## Biography `whitton_j_e1856`

- Printed name: **WHITTON, J**
- Birth year: not printed
- Appears in editions: [1886, 1888]

### Verbatim printed entry text (OCR)

**Version `col1886-L36233.v` — printed in editions [1886, 1888]:**

> WHITTON, J.—Engineer-in-chief of extension railways, New South Wales, 27th March, 1856.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1856 | Engineer-in-chief of extension railways | New South Wales | [1886, 1888] |

## Biography `whitton_j_e1856-2`

- Printed name: **WHITTON, J**
- Birth year: not printed
- Appears in editions: [1889, 1890]

### Verbatim printed entry text (OCR)

**Version `col1889-L36291.v` — printed in editions [1889, 1890]:**

> WHITTON, J. —Engineer-in-chief for railways, N.S. Wales, Mar., 1856; had many years' experience on English railways; was resident engineer, Oxford, Worcester, and Wolverhampton railway, when, on the recommendation of the Pres. of the Bd. of Tr., appointed to his present post; has had sole charge of the construction of railways, and also of railway surveys, in the colony since that date; and for many years was also in charge of the locomotive and permanent way branches.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1856 | Engineer-in-chief for railways, N.S. Wales | Nova Scotia | [1889, 1890] |

## Candidate stint `Whitton, John___New South Wales___1877`

- Staff-list name: **Whitton, John** | colony: **New South Wales** | listed 1877–1889 | editions [1877, 1878, 1879, 1880, 1886, 1888, 1889]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | John Whitton | Engineer-in-Chief | Extensions | — | — |
| 1878 | John Whitton | Engineer-in-Chief | Extensions | — | — |
| 1879 | John Whitton | Engineer-in-Chief | Extensions | — | — |
| 1880 | John Whitton | Engineer-in-Chief | Extensions | — | — |
| 1886 | John Whitton | Engineer-in-Chief | Extensions | — | — |
| 1888 | John Whitton | Engineer-in-Chief | Extensions | — | — |
| 1889 | John Whitton | Engineer-in-Chief | Extensions | — | — |

### Deterministic checks: `whitton_j_e1856` vs `Whitton, John___New South Wales___1877`

- [PASS] surname_gate: bio 'WHITTON' vs stint 'Whitton, John' (exact)
- [PASS] initials: bio ['J'] ~ stint ['J']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'New South Wales'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1877-1889
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

### Deterministic checks: `whitton_j_e1856-2` vs `Whitton, John___New South Wales___1877`

- [PASS] surname_gate: bio 'WHITTON' vs stint 'Whitton, John' (exact)
- [PASS] initials: bio ['J'] ~ stint ['J']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'New South Wales'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1877-1889
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

