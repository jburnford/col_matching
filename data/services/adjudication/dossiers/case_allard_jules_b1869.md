<!-- {"case_id": "case_allard_jules_b1869", "bio_ids": ["allard_jules_b1869"], "stint_ids": ["Allard, Louis Jules___Canada___1906", "Allard, Louis Jules___Canada___1917"]} -->
# Dossier case_allard_jules_b1869

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['allard_jules_b1869'] carry a single initial only — the namesake trap applies.

## Biography `allard_jules_b1869`

- Printed name: **ALLARD, JULES**
- Birth year: 1869 (attested in editions [1914])
- Appears in editions: [1914]

### Verbatim printed entry text (OCR)

**Version `col1914-L44241.v` — printed in editions [1914]:**

> ALLARD, HON. JULES.—B. 1869; ed. Nicolet Coll., Quebec; lawyer; elec. to legis. assem., Quebec, 1897, 1900, 1904, 1909; apptd. to legis.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1897–1909 | elec. to legis. assem. | Quebec | [1914] |

## Candidate stint `Allard, Louis Jules___Canada___1906`

- Staff-list name: **Allard, Louis Jules** | colony: **Canada** | listed 1906–1908 | editions [1906, 1908]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1906 | L. J. Allard | Minister of Public Works and Labour | Executive Council | — | — |
| 1908 | L. J. Allard | Minister of Agriculture | EXECUTIVE COUNCIL. | — | — |
| 1908 | L. J. Allard | Member | Constituencies | — | — |

### Deterministic checks: `allard_jules_b1869` vs `Allard, Louis Jules___Canada___1906`

- [PASS] surname_gate: bio 'ALLARD' vs stint 'Allard, Louis Jules' (exact)
- [PASS] initials: bio ['J'] ~ stint ['L', 'J']
- [PASS] age_gate: stint starts 1906, birth 1869 (age 37)
- [FAIL] colony: no placed event resolves to 'Canada'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1906-1908
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Allard, Louis Jules___Canada___1917`

- Staff-list name: **Allard, Louis Jules** | colony: **Canada** | listed 1917–1922 | editions [1917, 1918, 1919, 1922]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1917 | Captain Alphonse B. Allard | A.D.C. | Province of Saskatchewan | — | — |
| 1917 | Hon. Louis Jules Allard | Minister of Lands and Forests | Executive Council | — | — |
| 1917 | Victor Allard | District Puisne Judge | Judicial and Legal Departments | — | — |
| 1918 | Louis Jules Allard | Minister of Lands and Forests | Executive Council | — | — |
| 1919 | J. Allard | Member | Legislative Council | — | — |
| 1919 | Louis Jules Allard | Minister of Lands and Forests | Executive Council | — | — |
| 1922 | A. B. Allard | A.D.C., Capt. | Civil Establishment | — | — |
| 1922 | V. Allard | Puisne Judge, King's Bench | Judicial and Legal Departments | — | — |

### Deterministic checks: `allard_jules_b1869` vs `Allard, Louis Jules___Canada___1917`

- [PASS] surname_gate: bio 'ALLARD' vs stint 'Allard, Louis Jules' (exact)
- [PASS] initials: bio ['J'] ~ stint ['L', 'J']
- [PASS] age_gate: stint starts 1917, birth 1869 (age 48)
- [FAIL] colony: no placed event resolves to 'Canada'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1917-1922
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

