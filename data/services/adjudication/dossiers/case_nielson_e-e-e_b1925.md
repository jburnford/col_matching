<!-- {"case_id": "case_nielson_e-e-e_b1925", "bio_ids": ["nielson_e-e-e_b1925"], "stint_ids": ["Nielsen, E. E. E___Western Pacific___1964"]} -->
# Dossier case_nielson_e-e-e_b1925

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 4 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `nielson_e-e-e_b1925`

- Printed name: **NIELSON, E. E. E**
- Birth year: 1925 (attested in editions [1965, 1966])
- Appears in editions: [1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1965-L17961.v` — printed in editions [1965, 1966]:**

> NIELSON, E. E. E.—b. 1925; ed. gram. schls. Haifa and Jerusalem; mil. serv., 1943–46; contrl. offr., dept. of civil aviat., Pal., 1946; air traffic contrl. offr., gr. 1, Mal., 1948; dep. dir. civil aviat., 1961–63; supt., civil aviat., B.S.I.P., 1963.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1946 | contrl. offr., dept. of civil aviat. | Palestine | [1965, 1966] |
| 1 | 1948 | air traffic contrl. offr., gr. 1 | Malaya | [1965, 1966] |
| 2 | 1961–1963 | dep. dir. civil aviat | Malaya *(inherited from previous clause)* | [1965, 1966] |
| 3 | 1963 | supt., civil aviat., B.S.I.P | Malaya *(inherited from previous clause)* | [1965, 1966] |

## Candidate stint `Nielsen, E. E. E___Western Pacific___1964`

- Staff-list name: **Nielsen, E. E. E** | colony: **Western Pacific** | listed 1964–1966 | editions [1964, 1965, 1966]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1964 | E. E. Nielsen | Superintendent of Civil Aviation | Civil Establishment | — | — |
| 1965 | E. E. E. Nielsen | Superintendent of Civil Aviation | Civil Establishment | — | — |
| 1966 | E. E. Nielsen | Superintendent of Civil Aviation | Civil Establishment | — | — |

### Deterministic checks: `nielson_e-e-e_b1925` vs `Nielsen, E. E. E___Western Pacific___1964`

- [PASS] surname_gate: bio 'NIELSON' vs stint 'Nielsen, E. E. E' (fuzzy:1)
- [PASS] initials: bio ['E', 'E', 'E'] ~ stint ['E', 'E', 'E']
- [PASS] age_gate: stint starts 1964, birth 1925 (age 39)
- [FAIL] colony: no placed event resolves to 'Western Pacific'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1964-1966
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

