<!-- {"case_id": "case_moriarty_edward-orpen_e1849", "bio_ids": ["moriarty_edward-orpen_e1849"], "stint_ids": ["Moriarty, E. O___New South Wales___1877"]} -->
# Dossier case_moriarty_edward-orpen_e1849

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 6 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `moriarty_edward-orpen_e1849`

- Printed name: **MORIARTY, EDWARD ORPEN**
- Birth year: not printed
- Honours: M.I.C.E
- Appears in editions: [1888, 1889, 1890]

### Verbatim printed entry text (OCR)

**Version `col1888-L34987.v` — printed in editions [1888, 1889, 1890]:**

> MORIARTY, EDWARD ORPEN, M.A. (Dublin), M.I.C.E.—Assistant surveyor, New South Wales, 1849; engineer, steam navigation board, 1853; ditto, Hunter River improvements, 1855; engineer-in-chief for harbours and rivers since 1858; carried out Sydney water supply and many other works.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1849 | Assistant surveyor | New South Wales | [1888, 1889, 1890] |
| 1 | 1853 | engineer, steam navigation board | New South Wales *(inherited from previous clause)* | [1888, 1889, 1890] |
| 2 | 1855 | ditto, Hunter River improvements | New South Wales *(inherited from previous clause)* | [1888, 1889, 1890] |
| 3 | 1858 | engineer-in-chief for harbours and rivers since | New South Wales *(inherited from previous clause)* | [1888, 1889, 1890] |

## Candidate stint `Moriarty, E. O___New South Wales___1877`

- Staff-list name: **Moriarty, E. O** | colony: **New South Wales** | listed 1877–1889 | editions [1877, 1878, 1879, 1880, 1886, 1888, 1889]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | E. O. Moriarty | Engineer-in-Chief for Harbours and River Navigation | Roads and Bridges | — | — |
| 1878 | E. O. Moriarty | Engineer-in-Chief for Harbours and River Navigation | Roads and Bridges | — | — |
| 1879 | E. O. Moriarty | Engineer-in-Chief for Harbours and River Navigation | Roads and Bridges | — | — |
| 1880 | E. O. Moriarty | Engineer-in-Chief for Harbours and River Navigation | Roads and Bridges | — | — |
| 1886 | E. O. Moriarty | Engineer-in-Chief for Harbours and River Navigation, and Water Supply | Electric Telegraph Department | — | — |
| 1888 | E. O. Moriarty | Engineer-in-Chief for Harbours and River Navigation, and Water Supply | Harbours and Rivers Department | — | — |
| 1889 | E. O. Moriarty | Engineer-in-Chief for Harbours and River Navigation, and Water Supply | Harbours and Rivers Department | — | — |

### Deterministic checks: `moriarty_edward-orpen_e1849` vs `Moriarty, E. O___New South Wales___1877`

- [PASS] surname_gate: bio 'MORIARTY' vs stint 'Moriarty, E. O' (exact)
- [PASS] initials: bio ['E', 'O'] ~ stint ['E', 'O']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [PASS] colony: 4 placed event(s) resolve to 'New South Wales'
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

