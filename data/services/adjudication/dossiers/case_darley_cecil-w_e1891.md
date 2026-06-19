<!-- {"case_id": "case_darley_cecil-w_e1891", "bio_ids": ["darley_cecil-w_e1891"], "stint_ids": ["Darley, Cecil W___New South Wales___1886"]} -->
# Dossier case_darley_cecil-w_e1891

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `darley_cecil-w_e1891`

- Printed name: **DARLEY, Cecil W**
- Birth year: not printed
- Honours: I.S.O (1903)
- Appears in editions: [1894, 1896, 1898, 1899, 1900, 1905, 1907]

### Verbatim printed entry text (OCR)

**Version `col1894-L31094.v` — printed in editions [1894, 1896, 1898, 1899, 1900, 1905, 1907]:**

> DARLEY, Cecil W., I.S.O. (1903).—Engnr.-in-ch. for harbours and river navig. and water supply, N. S. Wales, 1891.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1891 | Engnr.-in-ch. for harbours and river navig. and water supply, N. S. Wales | Nova Scotia | [1894, 1896, 1898, 1899, 1900, 1905, 1907] |

## Candidate stint `Darley, Cecil W___New South Wales___1886`

- Staff-list name: **Darley, Cecil W** | colony: **New South Wales** | listed 1886–1900 | editions [1886, 1888, 1889, 1894, 1896, 1897, 1898, 1899, 1900]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1886 | Cecil W. Darley | Principal Assistant Engineer | Electric Telegraph Department | — | — |
| 1888 | Cecil W. Darley | Principal Assistant Engineer | Harbours and Rivers Department | — | — |
| 1889 | Cecil W. Darley | Principal Assistant Engineer | Harbours and Rivers Department | — | — |
| 1894 | Cecil W. Darley | Engineer-in-Chief for Harbours and River Navigation, and Water Supply | Harbours and Rivers Department | — | — |
| 1894 | C. W. Darley | President | Board of Water Supply and Sewerage | — | — |
| 1896 | C. W. Darley | President | Board of Water Supply and Sewerage. | — | — |
| 1897 | C. W. Darley | Engineer-in-Chief | Department of Works and Subordinate Departments. | — | — |
| 1898 | C. W. Darley | Engineer-in-Chief | Department of Works and Subordinate Departments | — | — |
| 1899 | C. W. Darley | Engineer-in-Chief | Department of Works and Subordinate Departments | — | — |
| 1900 | C. W. Darley | Engineer-in-Chief | Department of Works and Subordinate Departments | — | — |

### Deterministic checks: `darley_cecil-w_e1891` vs `Darley, Cecil W___New South Wales___1886`

- [PASS] surname_gate: bio 'DARLEY' vs stint 'Darley, Cecil W' (exact)
- [PASS] initials: bio ['C', 'W'] ~ stint ['C', 'W']
- [PASS] age_gate: stint starts 1886; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'New South Wales'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1886-1900
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

