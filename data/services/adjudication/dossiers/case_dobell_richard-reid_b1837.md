<!-- {"case_id": "case_dobell_richard-reid_b1837", "bio_ids": ["dobell_richard-reid_b1837", "dobell_richard-rud_e1857"], "stint_ids": ["Dobell, Richard Reid___Canada___1898"]} -->
# Dossier case_dobell_richard-reid_b1837

## Case context

- 2 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- CONTESTED: stint(s) ['Dobell, Richard Reid___Canada___1898'] have more than one claimant biography in this case.

## Biography `dobell_richard-reid_b1837`

- Printed name: **DOBELL, RICHARD REID**
- Birth year: 1837 (attested in editions [1897, 1899, 1900])
- Appears in editions: [1897, 1899, 1900]

### Verbatim printed entry text (OCR)

**Version `col1897-L31712.v` — printed in editions [1897, 1899, 1900]:**

> DOBELL, HON. RICHARD REID.—Born at Liverpool, 1837, his father being a prominent merchant of that city; went to Quebec in 1857, and, entering into the lumber business, became the head of one of the largest firms in the country; elected member of House of Commons for Quebec West, and became member of Mr. Laurier's govt. (without portfolio), June, 1896.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1857 | head of one of the largest firms | Quebec | [1897, 1899, 1900] |
| 1 | 1896 | member of House of Commons | Quebec | [1897, 1899, 1900] |

## Biography `dobell_richard-rud_e1857`

- Printed name: **DOBELL, RICHARD RUD.**
- Birth year: not printed
- Appears in editions: [1898]

### Verbatim printed entry text (OCR)

**Version `col1898-L33094.v` — printed in editions [1898]:**

> DOBELL, HON. RICHARD RUD.—Went to Quebec in 1857, and, entering into the lumber business, became the head of one of the largest firms in the country; elected mem. of House of Commons for Quebec West, and became mem. of Sir W. Laurier's govt. (without portfolio), June, 1896.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1857 | — | Quebec | [1898] |
| 1 | 1896 | mem. of House of Commons for Quebec West, and became mem. of Sir W. Laurier's govt. (without portfolio) | Quebec | [1898] |

## Candidate stint `Dobell, Richard Reid___Canada___1898`

- Staff-list name: **Dobell, Richard Reid** | colony: **Canada** | listed 1898–1900 | editions [1898, 1899, 1900]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1898 | Richard Reid Dobell | — | — | — | — |
| 1898 | Hon. R. R. Dobell | without Portfolio | Cabinet | — | — |
| 1899 | Richard Reid Dobell | — | — | — | — |
| 1900 | Hon. R. R. Dobell | without Portfolio | Cabinet | — | — |
| 1900 | Richard Reid Dobell | — | — | — | — |

### Deterministic checks: `dobell_richard-reid_b1837` vs `Dobell, Richard Reid___Canada___1898`

- [PASS] surname_gate: bio 'DOBELL' vs stint 'Dobell, Richard Reid' (exact)
- [PASS] initials: bio ['R', 'R'] ~ stint ['R', 'R']
- [PASS] age_gate: stint starts 1898, birth 1837 (age 61)
- [FAIL] colony: no placed event resolves to 'Canada'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1898-1900
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

### Deterministic checks: `dobell_richard-rud_e1857` vs `Dobell, Richard Reid___Canada___1898`

- [PASS] surname_gate: bio 'DOBELL' vs stint 'Dobell, Richard Reid' (exact)
- [PASS] initials: bio ['R', 'R'] ~ stint ['R', 'R']
- [PASS] age_gate: stint starts 1898; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Canada'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1898-1900
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

