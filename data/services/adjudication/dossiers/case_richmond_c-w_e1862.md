<!-- {"case_id": "case_richmond_c-w_e1862", "bio_ids": ["richmond_c-w_e1862"], "stint_ids": ["Richmond, C. W___New Zealand___1877", "Richmond, W___Cape of Good Hope___1907"]} -->
# Dossier case_richmond_c-w_e1862

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 16 official(s) with this surname in the graph's staff lists; 11 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `richmond_c-w_e1862`

- Printed name: **RICHMOND, C. W**
- Birth year: not printed
- Appears in editions: [1886, 1888, 1889, 1890, 1894]

### Verbatim printed entry text (OCR)

**Version `col1886-L35452.v` — printed in editions [1886, 1888, 1889, 1890, 1894]:**

> RICHMOND, C. W.—Puisne judge, New Zealand, 20th Oct., 1862.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1862 | Puisne judge | New Zealand | [1886, 1888, 1889, 1890, 1894] |

## Candidate stint `Richmond, C. W___New Zealand___1877`

- Staff-list name: **Richmond, C. W** | colony: **New Zealand** | listed 1877–1894 | editions [1877, 1878, 1880, 1883, 1886, 1888, 1889, 1890, 1894]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | C. W. Richmond | Puisne Judges | Judicial | — | — |
| 1878 | C. W. Richmond | Puisne Judges | General Government | — | — |
| 1880 | C. W. Richmond | Puisne Judges | Judicial | — | — |
| 1883 | C. W. Richmond | Puisne Judge | Judicial | — | — |
| 1886 | C. W. Richmond | Puisne Judges | Judicial | — | — |
| 1888 | C. W. Richmond | Puisne Judges | Judicial | — | — |
| 1889 | C. W. Richmond | Puisme Judges | Judicial | — | — |
| 1890 | C. W. Richmond | Puisne Judges | Judicial | — | — |
| 1894 | C. W. Richmond | Puisne Judge | Judicial | — | — |

### Deterministic checks: `richmond_c-w_e1862` vs `Richmond, C. W___New Zealand___1877`

- [PASS] surname_gate: bio 'RICHMOND' vs stint 'Richmond, C. W' (exact)
- [PASS] initials: bio ['C', 'W'] ~ stint ['C', 'W']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'New Zealand'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1877-1894
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Richmond, W___Cape of Good Hope___1907`

- Staff-list name: **Richmond, W** | colony: **Cape of Good Hope** | listed 1907–1909 | editions [1907, 1908, 1909]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1907 | W. Richmond | Clerk | Educational Department | — | — |
| 1908 | W. Richmond | Clerks | Educational Department | — | — |
| 1909 | W. Richmond | Clerks | Educational Department | — | — |

### Deterministic checks: `richmond_c-w_e1862` vs `Richmond, W___Cape of Good Hope___1907`

- [PASS] surname_gate: bio 'RICHMOND' vs stint 'Richmond, W' (exact)
- [PASS] initials: bio ['C', 'W'] ~ stint ['W']
- [PASS] age_gate: stint starts 1907; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Cape of Good Hope'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1907-1909
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

