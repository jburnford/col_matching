<!-- {"case_id": "case_evans_v_b1907", "bio_ids": ["evans_v_b1907"], "stint_ids": ["Evans, A. V___Northern Rhodesia___1949", "Evans, Vida___St Helena___1923"]} -->
# Dossier case_evans_v_b1907

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 143 official(s) with this surname in the graph's staff lists; 63 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['evans_v_b1907'] carry a single initial only — the namesake trap applies.
- NOTE: stint `Evans, A. V___Northern Rhodesia___1949` is also gate-compatible with biography(ies) outside this case: ['evans_albert-victor_b1899'] (already linked elsewhere or filtered).
- NOTE: stint `Evans, Vida___St Helena___1923` is also gate-compatible with biography(ies) outside this case: ['evans_albert-victor_b1899'] (already linked elsewhere or filtered).

## Biography `evans_v_b1907`

- Printed name: **EVANS, V**
- Birth year: 1907 (attested in editions [1964, 1965, 1966])
- Honours: O.B.E
- Appears in editions: [1964, 1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1964-L16798.v` — printed in editions [1964, 1965, 1966]:**

> EVANS, V., O.B.E.—b. 1907; ed. Canton High Sch., Cardiff, and Univ. of Wales, Cardiff; music offr., dept. educ., Trin., 1946; dir. of culture, 1957. (Trin. Govt. service.)

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1946 | music offr., dept. educ. | Trinidad | [1964, 1965, 1966] |
| 1 | 1957 | dir. of culture | Trinidad *(inherited from previous clause)* | [1964, 1965, 1966] |

## Candidate stint `Evans, A. V___Northern Rhodesia___1949`

- Staff-list name: **Evans, A. V** | colony: **Northern Rhodesia** | listed 1949–1951 | editions [1949, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | A. V. Evans | Senior Postmasters | POSTS AND TELEGRAPHS | — | — |
| 1949 | A. J. Evans | Medical Officers | HEALTH | — | — |
| 1951 | A. V. Evans | Senior Postmaster | Posts and Telegraphs | — | — |

### Deterministic checks: `evans_v_b1907` vs `Evans, A. V___Northern Rhodesia___1949`

- [PASS] surname_gate: bio 'EVANS' vs stint 'Evans, A. V' (exact)
- [PASS] initials: bio ['V'] ~ stint ['A', 'V']
- [PASS] age_gate: stint starts 1949, birth 1907 (age 42)
- [FAIL] colony: no placed event resolves to 'Northern Rhodesia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1949-1951
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Evans, Vida___St Helena___1923`

- Staff-list name: **Evans, Vida** | colony: **St Helena** | listed 1923–1925 | editions [1923, 1924, 1925]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1923 | Vida Evans | Government School Mistress, County School | Officers of Customs | — | — |
| 1924 | Vida Evans | County School | Civil Establishment | — | — |
| 1925 | Vida Evans | Government School Mistress | Civil Establishment | — | — |

### Deterministic checks: `evans_v_b1907` vs `Evans, Vida___St Helena___1923`

- [PASS] surname_gate: bio 'EVANS' vs stint 'Evans, Vida' (exact)
- [PASS] initials: bio ['V'] ~ stint ['V']
- [PASS] age_gate: stint starts 1923, birth 1907 (age 16)
- [FAIL] colony: no placed event resolves to 'St Helena'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1923-1925
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

