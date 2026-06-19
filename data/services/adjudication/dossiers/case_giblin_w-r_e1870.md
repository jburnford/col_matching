<!-- {"case_id": "case_giblin_w-r_e1870", "bio_ids": ["giblin_w-r_e1870"], "stint_ids": ["Giblin, W. R___Australia___1912", "Giblin, W. R___Tasmania___1878"]} -->
# Dossier case_giblin_w-r_e1870

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 6 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `giblin_w-r_e1870`

- Printed name: **GIBLIN, W. R.**
- Birth year: not printed
- Appears in editions: [1886]

### Verbatim printed entry text (OCR)

**Version `col1886-L33669.v` — printed in editions [1886]:**

> GIBLIN, Hon. W. R.—Attorney-general Tasmania, 5 Feb., 1870, to 4 Nov., 1872, 4 Aug., 1873, to 20 July, 1876, and 9 to 13 Aug., 1877; colonial treasurer, 13 Aug., 1877, to 20 Dec., 1878; treasurer and premier, 3 Oct., 1879, to 1 Dec., 1871; attorney-general and premier, 1 Dec., 1881 to 1884; puisne judge, 1885.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1870–1872 | Attorney-general | Tasmania | [1886] |
| 1 | 1873–1876 | Attorney-general | — | [1886] |
| 2 | 1877–1877 | Attorney-general | — | [1886] |
| 3 | 1877–1878 | colonial treasurer | — | [1886] |
| 4 | 1879–1871 | treasurer and premier | — | [1886] |
| 5 | 1881–1884 | attorney-general and premier | — | [1886] |
| 6 | 1885 | puisne judge | — | [1886] |

## Candidate stint `Giblin, W. R___Australia___1912`

- Staff-list name: **Giblin, W. R** | colony: **Australia** | listed 1912–1927 | editions [1912, 1913, 1918, 1927]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1912 | W. R. Giblin | — | — | — | — |
| 1913 | W. R. Giblin | Minister | Ministries | — | — |
| 1913 | W. R. Giblin | Acting Chief Justice, Administrator | Governors | — | — |
| 1918 | W. R. Giblin | Minister | — | — | — |
| 1927 | W. R. Giblin | Premier | — | — | — |

### Deterministic checks: `giblin_w-r_e1870` vs `Giblin, W. R___Australia___1912`

- [PASS] surname_gate: bio 'GIBLIN' vs stint 'Giblin, W. R' (exact)
- [PASS] initials: bio ['W', 'R'] ~ stint ['W', 'R']
- [PASS] age_gate: stint starts 1912; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Australia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1912-1927
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Giblin, W. R___Tasmania___1878`

- Staff-list name: **Giblin, W. R** | colony: **Tasmania** | listed 1878–1880 | editions [1878, 1879, 1880]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1878 | Hon. W. R. Giblin | Colonial Treasurer | Treasury | — | — |
| 1879 | W. R. Giblin | Colonial Treasurer | Treasury | — | — |
| 1880 | W. R. Giblin | Colonial Treasurer | Treasury | — | — |

### Deterministic checks: `giblin_w-r_e1870` vs `Giblin, W. R___Tasmania___1878`

- [PASS] surname_gate: bio 'GIBLIN' vs stint 'Giblin, W. R' (exact)
- [PASS] initials: bio ['W', 'R'] ~ stint ['W', 'R']
- [PASS] age_gate: stint starts 1878; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Tasmania'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1878-1880
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

