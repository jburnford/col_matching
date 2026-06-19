<!-- {"case_id": "case_litt_william-george_b1877", "bio_ids": ["litt_william-george_b1877"], "stint_ids": ["Litt, W. G___Palestine___1923"]} -->
# Dossier case_litt_william-george_b1877

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `litt_william-george_b1877`

- Printed name: **LITT, WILLIAM GEORGE**
- Birth year: 1877 (attested in editions [1927, 1928, 1929, 1930])
- Appears in editions: [1927, 1928, 1929, 1930]

### Verbatim printed entry text (OCR)

**Version `col1927-L60754.v` — printed in editions [1927, 1928, 1929, 1930]:**

> LITT, WILLIAM GEORGE.—B. 1877; ed. Shrewsbury schol.; barrister-at-law (Inner Temple); served in Impl. yeomanry in S. African War, 1900-01; Queen's Med., 4 clasps; comsn. in The King's Shropshire Light Infy. (vol. and territorial battn.), 1901-20; territorial decorn.; substantive major, June, 1916; A.P.M., Hongkong, 1915-16; B.E.F., France, 1917; administrative commdts., Aleppo, E.E.F., 1919; Gen. Service, Territorial, War and Victory medls.; ret. with hon. rank of major; judl. offr., O.E.T.A. (South), Dec., 1919; pres., dist. ct., Haifa, 1920.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1900–1901 | served in Impl. yeomanry in S. African War | — | [1927, 1928, 1929, 1930] |
| 1 | 1901–1920 | comsn. in The King's Shropshire Light Infy. (vol. and territorial battn.) | — | [1927, 1928, 1929, 1930] |
| 2 | 1915–1916 | A.P.M. | Hongkong | [1927, 1928, 1929, 1930] |
| 3 | 1916 | substantive major | — | [1927, 1928, 1929, 1930] |
| 4 | 1917 | B.E.F., France | Hongkong *(inherited from previous clause)* | [1927, 1928, 1929, 1930] |
| 5 | 1919 | administrative commdts., Aleppo, E.E.F | Hongkong *(inherited from previous clause)* | [1927, 1928, 1929, 1930] |
| 6 | 1920 | pres., dist. ct., Haifa | Hongkong *(inherited from previous clause)* | [1927, 1928, 1929, 1930] |

## Candidate stint `Litt, W. G___Palestine___1923`

- Staff-list name: **Litt, W. G** | colony: **Palestine** | listed 1923–1928 | editions [1923, 1924, 1925, 1927, 1928]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1923 | W. G. Litt | Presidents | District Courts | — | — |
| 1924 | W. G. Litt | President | District Courts | — | — |
| 1925 | W. G. Litt | Presidents | District Courts | — | — |
| 1927 | W. G. Litt | President | District Courts | — | — |
| 1928 | W. G. Litt | President | District Courts | — | — |

### Deterministic checks: `litt_william-george_b1877` vs `Litt, W. G___Palestine___1923`

- [PASS] surname_gate: bio 'LITT' vs stint 'Litt, W. G' (exact)
- [PASS] initials: bio ['W', 'G'] ~ stint ['W', 'G']
- [PASS] age_gate: stint starts 1923, birth 1877 (age 46)
- [FAIL] colony: no placed event resolves to 'Palestine'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1923-1928
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

