<!-- {"case_id": "case_king_francis_b1915", "bio_ids": ["king_francis_b1915"], "stint_ids": ["King, F. L___Jamaica___1937", "King, H. F. S___Mauritius___1931"]} -->
# Dossier case_king_francis_b1915

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 187 official(s) with this surname in the graph's staff lists; 68 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['king_francis_b1915'] carry a single initial only — the namesake trap applies.

## Biography `king_francis_b1915`

- Printed name: **KING, Francis**
- Birth year: 1915 (attested in editions [1950, 1951])
- Appears in editions: [1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1950-L37000.v` — printed in editions [1950, 1951]:**

> KING, Francis.—b. 1915; ed. Pui To High Sch., Canton and Shanghai Univ., 2nd yr., Shanghai; on war serv. (China), 1944-45; nurse, med. dept., H.K., 1933; nursing sister, 1949.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1933 | nurse, med. dept. | Hong Kong | [1950, 1951] |
| 1 | 1949 | nursing sister | Hong Kong *(inherited from previous clause)* | [1950, 1951] |

## Candidate stint `King, F. L___Jamaica___1937`

- Staff-list name: **King, F. L** | colony: **Jamaica** | listed 1937–1940 | editions [1937, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1937 | F. L. King | Principal Warder | General Penitentiary | — | — |
| 1940 | F. L. King | Overseers | Prison Department | — | — |

### Deterministic checks: `king_francis_b1915` vs `King, F. L___Jamaica___1937`

- [PASS] surname_gate: bio 'KING' vs stint 'King, F. L' (exact)
- [PASS] initials: bio ['F'] ~ stint ['F', 'L']
- [PASS] age_gate: stint starts 1937, birth 1915 (age 22)
- [FAIL] colony: no placed event resolves to 'Jamaica'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1937-1940
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `King, H. F. S___Mauritius___1931`

- Staff-list name: **King, H. F. S** | colony: **Mauritius** | listed 1931–1932 | editions [1931, 1932]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1931 | H. F. S. King | Chief Ordnance Officer | Military Officers | — | Captain |
| 1932 | H. F. S. King | Chief Ordnance Officer | Military Officers | — | Captain |

### Deterministic checks: `king_francis_b1915` vs `King, H. F. S___Mauritius___1931`

- [PASS] surname_gate: bio 'KING' vs stint 'King, H. F. S' (exact)
- [PASS] initials: bio ['F'] ~ stint ['H', 'F', 'S']
- [PASS] age_gate: stint starts 1931, birth 1915 (age 16)
- [FAIL] colony: no placed event resolves to 'Mauritius'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1931-1932
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

