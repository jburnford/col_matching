<!-- {"case_id": "case_white_ernest-costley_e1900", "bio_ids": ["white_ernest-costley_e1900"], "stint_ids": ["White, E. C___British Central Africa___1906", "White, E. C___Nyasaland___1908"]} -->
# Dossier case_white_ernest-costley_e1900

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 128 official(s) with this surname in the graph's staff lists; 57 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `white_ernest-costley_e1900`

- Printed name: **WHITE, ERNEST COSTLEY**
- Birth year: not printed
- Honours: O.B.E (1918)
- Appears in editions: [1912, 1913, 1914, 1915, 1917, 1918, 1919]

### Verbatim printed entry text (OCR)

**Version `col1912-L48305.v` — printed in editions [1912, 1913, 1914, 1915, 1917, 1918, 1919]:**

> WHITE, ERNEST COSTLEY, O.B.E. (1918).—Clerk to armed forces, B.C. Africa, Apr., 1900; asst. collr., Nyassaland Prot., March, 1904; 2nd grade res., Jan., 1911; ag. supt. of native affairs.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1900 | Clerk to armed forces, B.C. Africa | British Columbia | [1912, 1913, 1914, 1915, 1917, 1918, 1919] |
| 1 | 1904 | asst. collr., Nyassaland Prot | British Columbia *(inherited from previous clause)* | [1912, 1913, 1914, 1915, 1917, 1918, 1919] |
| 2 | 1911 | 2nd grade res | British Columbia *(inherited from previous clause)* | [1912, 1913, 1914, 1915, 1917, 1918, 1919] |

## Candidate stint `White, E. C___British Central Africa___1906`

- Staff-list name: **White, E. C** | colony: **British Central Africa** | listed 1906–1907 | editions [1906, 1907]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1906 | E. C. White | 3rd class Assistant | Collectors | — | — |
| 1907 | E. C. White | Eighteen 3rd class | Residents | — | — |

### Deterministic checks: `white_ernest-costley_e1900` vs `White, E. C___British Central Africa___1906`

- [PASS] surname_gate: bio 'WHITE' vs stint 'White, E. C' (exact)
- [PASS] initials: bio ['E', 'C'] ~ stint ['E', 'C']
- [PASS] age_gate: stint starts 1906; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'British Central Africa'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1906-1907
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `White, E. C___Nyasaland___1908`

- Staff-list name: **White, E. C** | colony: **Nyasaland** | listed 1908–1912 | editions [1908, 1909, 1910, 1911, 1912]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1908 | E. C. White | Resident 3rd class | Residents | — | — |
| 1909 | E. C. White | Resident, 3rd class | Residents | — | — |
| 1910 | E. C. White | Eighteen 3rd Grade | Residents | — | — |
| 1911 | E. C. White | Eighteen 3rd Grade | Residents | — | — |
| 1912 | E. C. White | Twelve 2nd Grade | Residents | — | — |

### Deterministic checks: `white_ernest-costley_e1900` vs `White, E. C___Nyasaland___1908`

- [PASS] surname_gate: bio 'WHITE' vs stint 'White, E. C' (exact)
- [PASS] initials: bio ['E', 'C'] ~ stint ['E', 'C']
- [PASS] age_gate: stint starts 1908; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Nyasaland'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1908-1912
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

