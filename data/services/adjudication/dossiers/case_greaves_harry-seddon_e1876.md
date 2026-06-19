<!-- {"case_id": "case_greaves_harry-seddon_e1876", "bio_ids": ["greaves_harry-seddon_e1876"], "stint_ids": ["Greaves, H. S___Barbados___1905", "Greaves, H. S___Cape of Good Hope___1883"]} -->
# Dossier case_greaves_harry-seddon_e1876

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 33 official(s) with this surname in the graph's staff lists; 14 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `greaves_harry-seddon_e1876`

- Printed name: **GREAVES, HARRY SEDDON**
- Birth year: not printed
- Honours: F.R.I.B.A
- Appears in editions: [1894, 1896, 1897, 1898, 1899, 1900]

### Verbatim printed entry text (OCR)

**Version `col1894-L31816.v` — printed in editions [1894, 1896, 1897, 1898, 1899, 1900]:**

> GREAVES, HARRY SEDDON, F.R.I.B.A.—Superintendent erection of new parliament houses, Cape, 1876-85; architectural assistant in P.W. Dept., in which capacity he has carried out other important public works.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1876–1885 | Superintendent erection of new parliament houses | Cape of Good Hope | [1894, 1896, 1897, 1898, 1899, 1900] |

## Candidate stint `Greaves, H. S___Barbados___1905`

- Staff-list name: **Greaves, H. S** | colony: **Barbados** | listed 1905–1908 | editions [1905, 1906, 1907, 1908]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1905 | H. S. Greaves | Resident Surgeon | Medical | — | — |
| 1906 | H. S. Greaves | Resident Surgeon, General Hospital | Medical | — | — |
| 1907 | H. S. Greaves | Resident Surgeon, General Hospital | Medical | — | — |
| 1908 | H. S. Greaves | Resident Surgeon | Medical | — | — |

### Deterministic checks: `greaves_harry-seddon_e1876` vs `Greaves, H. S___Barbados___1905`

- [PASS] surname_gate: bio 'GREAVES' vs stint 'Greaves, H. S' (exact)
- [PASS] initials: bio ['H', 'S'] ~ stint ['H', 'S']
- [PASS] age_gate: stint starts 1905; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Barbados'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1905-1908
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Greaves, H. S___Cape of Good Hope___1883`

- Staff-list name: **Greaves, H. S** | colony: **Cape of Good Hope** | listed 1883–1894 | editions [1883, 1888, 1889, 1890, 1894]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1883 | H. S. Greaves | Architectural Assistant | Public Works Department | — | — |
| 1888 | H. S. Greaves | Architectural Assistant | Public Works Department | — | — |
| 1889 | H. S. Greaves | Architectural Assistant | Public Works Department | — | — |
| 1890 | H. S. Greaves | Architectural Assistant | Public Works Department | — | — |
| 1894 | H. S. Greaves | Architect | Public Works Department | — | — |

### Deterministic checks: `greaves_harry-seddon_e1876` vs `Greaves, H. S___Cape of Good Hope___1883`

- [PASS] surname_gate: bio 'GREAVES' vs stint 'Greaves, H. S' (exact)
- [PASS] initials: bio ['H', 'S'] ~ stint ['H', 'S']
- [PASS] age_gate: stint starts 1883; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Cape of Good Hope'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1883-1894
- [FAIL] position_sim: best 37 vs bar 60: 'Superintendent erection of new parliament houses' ~ 'Architectural Assistant'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

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

