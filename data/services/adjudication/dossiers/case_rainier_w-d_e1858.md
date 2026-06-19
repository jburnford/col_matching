<!-- {"case_id": "case_rainier_w-d_e1858", "bio_ids": ["rainier_w-d_e1858", "rainier_w-d_e1880"], "stint_ids": ["Rainier, W. D___Cape of Good Hope___1877"]} -->
# Dossier case_rainier_w-d_e1858

## Case context

- 2 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 9 official(s) with this surname in the graph's staff lists; 6 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- CONTESTED: stint(s) ['Rainier, W. D___Cape of Good Hope___1877'] have more than one claimant biography in this case.

## Biography `rainier_w-d_e1858`

- Printed name: **RAINIER, W. D.**
- Birth year: not printed
- Appears in editions: [1888]

### Verbatim printed entry text (OCR)

**Version `col1888-L35636.v` — printed in editions [1888]:**

> RAINIER, W. D.—Clerk to R.M., Malmesbury, Cape, Oct., 1858; ditto, Clan William, April, 1863; ditto, Riversdale, 1869; acting C.C. and R.M., Ladismith, Oct., 1879, and C.C., Jan., 1880.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1858 | Clerk to R.M. | Cape | [1888] |
| 1 | 1863 | Clerk to R.M. | — | [1888] |
| 2 | 1869 | Clerk to R.M. | — | [1888] |
| 3 | 1879 | acting C.C. and R.M. | — | [1888] |
| 4 | 1880 | C.C. | — | [1888] |

## Biography `rainier_w-d_e1880`

- Printed name: **RAINIER, W. D**
- Birth year: not printed
- Appears in editions: [1886]

### Verbatim printed entry text (OCR)

**Version `col1886-L35381.v` — printed in editions [1886]:**

> RAINIER, W. D.—Resident magistrate, Ladismith division, Cape Colony, Jan., 1880.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1880 | Resident magistrate, Ladismith division | Cape of Good Hope | [1886] |

## Candidate stint `Rainier, W. D___Cape of Good Hope___1877`

- Staff-list name: **Rainier, W. D** | colony: **Cape of Good Hope** | listed 1877–1878 | editions [1877, 1878]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | W. D. Rainier | Clerk | Police Branch | — | — |
| 1878 | W. D. Rainier | Clerk | DIVISION OF RIVERSDALE | — | — |

### Deterministic checks: `rainier_w-d_e1858` vs `Rainier, W. D___Cape of Good Hope___1877`

- [PASS] surname_gate: bio 'RAINIER' vs stint 'Rainier, W. D' (exact)
- [PASS] initials: bio ['W', 'D'] ~ stint ['W', 'D']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Cape of Good Hope'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1877-1878
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

### Deterministic checks: `rainier_w-d_e1880` vs `Rainier, W. D___Cape of Good Hope___1877`

- [PASS] surname_gate: bio 'RAINIER' vs stint 'Rainier, W. D' (exact)
- [PASS] initials: bio ['W', 'D'] ~ stint ['W', 'D']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Cape of Good Hope'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1877-1878
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

