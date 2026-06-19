<!-- {"case_id": "case_ross_william-alston_b1875", "bio_ids": ["ross_william-alston_b1875"], "stint_ids": ["Ross, W. A___Lagos___1905"]} -->
# Dossier case_ross_william-alston_b1875

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 140 official(s) with this surname in the graph's staff lists; 64 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `ross_william-alston_b1875`

- Printed name: **ROSS, WILLIAM ALSTON**
- Birth year: 1875 (attested in editions [1930, 1931, 1932])
- Honours: C.M.G (1922)
- Appears in editions: [1930, 1931, 1932]

### Verbatim printed entry text (OCR)

**Version `col1930-L67910.v` — printed in editions [1930, 1931, 1932]:**

> ROSS, CAPT. WILLIAM ALSTON, C.M.G. (1922).—B. 1875; dist. comanr., Nigeria, 1903; dist. comanr., 1st grade, S. Nigeria, 1910; senr. dist. comanr., 1912; attd., Nigeria Regt., Cameroons, 1914-15; staff grade, 1920.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1903 | dist. comanr. | Nigeria | [1930, 1931, 1932] |
| 1 | 1910 | dist. comanr., 1st grade | Southern Nigeria | [1930, 1931, 1932] |
| 2 | 1912 | senr. dist. comanr | Southern Nigeria *(inherited from previous clause)* | [1930, 1931, 1932] |
| 3 | 1914–1915 | attd., Nigeria Regt. | Cameroons | [1930, 1931, 1932] |
| 4 | 1920 | staff grade | Cameroons *(inherited from previous clause)* | [1930, 1931, 1932] |

## Candidate stint `Ross, W. A___Lagos___1905`

- Staff-list name: **Ross, W. A** | colony: **Lagos** | listed 1905–1906 | editions [1905, 1906]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1905 | W. A. Ross | District Commissioner | Supreme Court | — | — |
| 1906 | W. A. Ross | District Commissioners | Supreme Court | — | — |

### Deterministic checks: `ross_william-alston_b1875` vs `Ross, W. A___Lagos___1905`

- [PASS] surname_gate: bio 'ROSS' vs stint 'Ross, W. A' (exact)
- [PASS] initials: bio ['W', 'A'] ~ stint ['W', 'A']
- [PASS] age_gate: stint starts 1905, birth 1875 (age 30)
- [FAIL] colony: no placed event resolves to 'Lagos'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1905-1906
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

