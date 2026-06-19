<!-- {"case_id": "case_markham_l-a_b1898", "bio_ids": ["markham_l-a_b1898"], "stint_ids": ["Markham, L. A___Gambia___1956", "Markham, L. A___Tanganyika___1922"]} -->
# Dossier case_markham_l-a_b1898

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 4 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `markham_l-a_b1898`

- Printed name: **MARKHAM, L. A**
- Birth year: 1898 (attested in editions [1956, 1957])
- Appears in editions: [1956, 1957]

### Verbatim printed entry text (OCR)

**Version `col1956-L22924.v` — printed in editions [1956, 1957]:**

> MARKHAM, L. A.—b. 1898; ed. St. George's Coll., London, Christ's Coll., Camb. and Imp. Forestry Inst., Oxford; mil. serv., 1916-19, lt.; col. forest service, Tang., 1921-48; forestry advr., Gam., 1955.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1921–1948 | col. forest service | Tanganyika | [1956, 1957] |
| 1 | 1955 | forestry advr., Gam | Tanganyika *(inherited from previous clause)* | [1956, 1957] |

## Candidate stint `Markham, L. A___Gambia___1956`

- Staff-list name: **Markham, L. A** | colony: **Gambia** | listed 1956–1957 | editions [1956, 1957]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1956 | L. A. Markham | Forestry Adviser | Civil Establishment | — | — |
| 1957 | L. A. Markham | Forestry Adviser | Civil Establishment | — | — |

### Deterministic checks: `markham_l-a_b1898` vs `Markham, L. A___Gambia___1956`

- [PASS] surname_gate: bio 'MARKHAM' vs stint 'Markham, L. A' (exact)
- [PASS] initials: bio ['L', 'A'] ~ stint ['L', 'A']
- [PASS] age_gate: stint starts 1956, birth 1898 (age 58)
- [FAIL] colony: no placed event resolves to 'Gambia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1956-1957
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Markham, L. A___Tanganyika___1922`

- Staff-list name: **Markham, L. A** | colony: **Tanganyika** | listed 1922–1925 | editions [1922, 1923, 1924, 1925]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1922 | L. A. Markham | Assistant Conservators of Forests | Forestry | — | — |
| 1923 | L. A. Markham | Assistant Conservators of Forests | Forestry | — | — |
| 1924 | L. A. Markham | Assistant Conservators of Forests | Forestry | — | — |
| 1925 | L. A. Markham | Assistant Conservators of Forests | Forestry | — | — |

### Deterministic checks: `markham_l-a_b1898` vs `Markham, L. A___Tanganyika___1922`

- [PASS] surname_gate: bio 'MARKHAM' vs stint 'Markham, L. A' (exact)
- [PASS] initials: bio ['L', 'A'] ~ stint ['L', 'A']
- [PASS] age_gate: stint starts 1922, birth 1898 (age 24)
- [PASS] colony: 2 placed event(s) resolve to 'Tanganyika'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1922-1925
- [FAIL] position_sim: best 39 vs bar 60: 'col. forest service' ~ 'Assistant Conservators of Forests'
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

