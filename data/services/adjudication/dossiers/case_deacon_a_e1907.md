<!-- {"case_id": "case_deacon_a_e1907", "bio_ids": ["deacon_a_e1907", "deacon_a_e1907-2"], "stint_ids": ["Deacon, A. J. E___Sierra Leone___1913"]} -->
# Dossier case_deacon_a_e1907

## Case context

- 2 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 10 official(s) with this surname in the graph's staff lists; 8 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['deacon_a_e1907', 'deacon_a_e1907-2'] carry a single initial only — the namesake trap applies.
- CONTESTED: stint(s) ['Deacon, A. J. E___Sierra Leone___1913'] have more than one claimant biography in this case.

## Biography `deacon_a_e1907`

- Printed name: **DEACON, A**
- Birth year: not printed
- Appears in editions: [1908, 1909, 1910]

### Verbatim printed entry text (OCR)

**Version `col1908-L44054.v` — printed in editions [1908, 1909, 1910]:**

> DEACON, A.—Apptd. after exam. 3rd cl. messenger, C.O., 1907.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1907 | Apptd. after exam. 3rd cl. messenger | Colonial Office | [1908, 1909, 1910] |

## Biography `deacon_a_e1907-2`

- Printed name: **DEACON, A**
- Birth year: not printed
- Appears in editions: [1911, 1912, 1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921, 1923, 1924, 1925]

### Verbatim printed entry text (OCR)

**Version `col1911-L44221.v` — printed in editions [1911, 1912, 1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921, 1923, 1924, 1925]:**

> DEACON, A.—Apptd. after exam. 3rd cls. mess., C.O., 1907; 2nd cls. mess., 30th Jan., 1911.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1907 | Apptd. after exam. 3rd cls. mess. | Colonial Office | [1911, 1912, 1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921, 1923, 1924, 1925] |
| 1 | 1911 | 2nd cls. mess | Colonial Office *(inherited from previous clause)* | [1911, 1912, 1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921, 1923, 1924, 1925] |

## Candidate stint `Deacon, A. J. E___Sierra Leone___1913`

- Staff-list name: **Deacon, A. J. E** | colony: **Sierra Leone** | listed 1913–1914 | editions [1913, 1914]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1913 | A. J. E. Deacon | Assistant Accountant | Railway Department | — | — |
| 1914 | A. J. E. Deacon | Assistant Accountant | Railway Department | — | — |

### Deterministic checks: `deacon_a_e1907` vs `Deacon, A. J. E___Sierra Leone___1913`

- [PASS] surname_gate: bio 'DEACON' vs stint 'Deacon, A. J. E' (exact)
- [PASS] initials: bio ['A'] ~ stint ['A', 'J', 'E']
- [PASS] age_gate: stint starts 1913; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Sierra Leone'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1913-1914
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

### Deterministic checks: `deacon_a_e1907-2` vs `Deacon, A. J. E___Sierra Leone___1913`

- [PASS] surname_gate: bio 'DEACON' vs stint 'Deacon, A. J. E' (exact)
- [PASS] initials: bio ['A'] ~ stint ['A', 'J', 'E']
- [PASS] age_gate: stint starts 1913; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Sierra Leone'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1913-1914
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

