<!-- {"case_id": "case_hogg_william_b1891", "bio_ids": ["hogg_william_b1891"], "stint_ids": ["Hogg, W. M. B___Gibraltar___1932", "Hogg, William___Australia___1912"]} -->
# Dossier case_hogg_william_b1891

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 13 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['hogg_william_b1891'] carry a single initial only — the namesake trap applies.

## Biography `hogg_william_b1891`

- Printed name: **HOGG, William**
- Birth year: 1891 (attested in editions [1948, 1949, 1950, 1951])
- Appears in editions: [1948, 1949, 1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1948-L33396.v` — printed in editions [1948, 1949, 1950, 1951]:**

> HOGG, William.—b. 1891; apptd., P.W.D., Nig., 1924; inspr., gr. I., 1925; gr. II., 1932; ch., 1941; ass't. wks. man., 1945.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1924 | apptd., P.W.D. | Nigeria | [1948, 1949, 1950, 1951] |
| 1 | 1925 | inspr., gr. I | Nigeria *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |
| 2 | 1932 | gr. II | Nigeria *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |
| 3 | 1941 | ch | Nigeria *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |
| 4 | 1945 | ass't. wks. man | Nigeria *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |

## Candidate stint `Hogg, W. M. B___Gibraltar___1932`

- Staff-list name: **Hogg, W. M. B** | colony: **Gibraltar** | listed 1932–1934 | editions [1932, 1933, 1934]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1932 | W. M. B. Hogg | Senior Chaplain to the Forces | Chief Military and Naval Officers | — | — |
| 1933 | W. M. B. Hogg | Senior Chaplain to the Forces | Chief Military and Naval Officers | — | — |
| 1933 | Hogg | — | — | — | — |
| 1934 | W. M. B. Hogg | Senior Chaplain to the Forces | Chief Military and Naval Officers | — | — |

### Deterministic checks: `hogg_william_b1891` vs `Hogg, W. M. B___Gibraltar___1932`

- [PASS] surname_gate: bio 'HOGG' vs stint 'Hogg, W. M. B' (exact)
- [PASS] initials: bio ['W'] ~ stint ['W', 'M', 'B']
- [PASS] age_gate: stint starts 1932, birth 1891 (age 41)
- [FAIL] colony: no placed event resolves to 'Gibraltar'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1932-1934
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Hogg, William___Australia___1912`

- Staff-list name: **Hogg, William** | colony: **Australia** | listed 1912–1927 | editions [1912, 1913, 1918, 1927]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1912 | W. Hogg | Deputy Commissioner | Office of Taxes | — | — |
| 1913 | W. Hogg | Deputy Commissioner | Office of Taxes | — | — |
| 1918 | W. Hogg | Deputy Commissioner | Office of Taxes | — | — |
| 1927 | William Hogg | Deputy-Commissioner of Taxes | Taxation Department | — | — |

### Deterministic checks: `hogg_william_b1891` vs `Hogg, William___Australia___1912`

- [PASS] surname_gate: bio 'HOGG' vs stint 'Hogg, William' (exact)
- [PASS] initials: bio ['W'] ~ stint ['W']
- [PASS] age_gate: stint starts 1912, birth 1891 (age 21)
- [FAIL] colony: no placed event resolves to 'Australia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1912-1927
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

