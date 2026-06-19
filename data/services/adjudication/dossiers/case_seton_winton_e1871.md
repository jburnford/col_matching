<!-- {"case_id": "case_seton_winton_e1871", "bio_ids": ["seton_winton_e1871"], "stint_ids": ["Seton, C. R. W___Palestine___1921", "Seton, C. R. W___Transjordan___1927"]} -->
# Dossier case_seton_winton_e1871

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 5 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['seton_winton_e1871'] carry a single initial only — the namesake trap applies.
- NOTE: stint `Seton, C. R. W___Palestine___1921` is also gate-compatible with biography(ies) outside this case: ['seton_claud-ramsay-wilmot_b1888'] (already linked elsewhere or filtered).
- NOTE: stint `Seton, C. R. W___Transjordan___1927` is also gate-compatible with biography(ies) outside this case: ['seton_claud-ramsay-wilmot_b1888'] (already linked elsewhere or filtered).

## Biography `seton_winton_e1871`

- Printed name: **SETON, WINTON**
- Birth year: not printed
- Appears in editions: [1897, 1898, 1899, 1900]

### Verbatim printed entry text (OCR)

**Version `col1897-L34463.v` — printed in editions [1897, 1898, 1899, 1900]:**

> SETON, MAJOR WINTON.—Roy. Can. regt., Lieut. 1871; capt. 1883; major 1892; adjt., British Guiana Militia, 1894.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1871 | Roy. Can. regt., Lieut | — | [1897, 1898, 1899, 1900] |
| 1 | 1883 | capt | — | [1897, 1898, 1899, 1900] |
| 2 | 1892 | major | — | [1897, 1898, 1899, 1900] |
| 3 | 1894 | adjt., British Guiana Militia | British Guiana | [1897, 1898, 1899, 1900] |

## Candidate stint `Seton, C. R. W___Palestine___1921`

- Staff-list name: **Seton, C. R. W** | colony: **Palestine** | listed 1921–1932 | editions [1921, 1923, 1924, 1925, 1927, 1928, 1929, 1930, 1931, 1932]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1921 | C. R. W. Seton | President | Jaffa District Court | — | — |
| 1923 | C. R. W. Seton | Presidents | District Courts | — | — |
| 1924 | C. R. W. Seton | President | District Courts | — | — |
| 1925 | C. R. W. Seton | Presidents | District Courts | M.C. | — |
| 1927 | C. R. W. Seton | President | District Courts | — | — |
| 1928 | C. R. W. Seton | President | District Courts | — | — |
| 1929 | C. R. W. Seton | President | District Courts | — | — |
| 1930 | C. R. W. Seton | President | District Courts | — | — |
| 1931 | C. R. W. Seton | Presidents | District Courts | — | — |
| 1932 | C. R. W. Seton | President | District Courts | — | — |

### Deterministic checks: `seton_winton_e1871` vs `Seton, C. R. W___Palestine___1921`

- [PASS] surname_gate: bio 'SETON' vs stint 'Seton, C. R. W' (exact)
- [PASS] initials: bio ['W'] ~ stint ['C', 'R', 'W']
- [PASS] age_gate: stint starts 1921; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Palestine'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1921-1932
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Seton, C. R. W___Transjordan___1927`

- Staff-list name: **Seton, C. R. W** | colony: **Transjordan** | listed 1927–1931 | editions [1927, 1928, 1929, 1931]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1927 | C. R. W. Seton | Judicial Adviser | — | — | — |
| 1928 | C. R. W. Seton | Judicial Adviser | Trans-Jordan Administration | — | — |
| 1929 | C. R. W. Seton | Judicial Adviser | Trans-Jordan Administration | — | — |
| 1931 | C. R. W. Seton | Judicial Adviser | — | — | — |

### Deterministic checks: `seton_winton_e1871` vs `Seton, C. R. W___Transjordan___1927`

- [PASS] surname_gate: bio 'SETON' vs stint 'Seton, C. R. W' (exact)
- [PASS] initials: bio ['W'] ~ stint ['C', 'R', 'W']
- [PASS] age_gate: stint starts 1927; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Transjordan'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1927-1931
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

