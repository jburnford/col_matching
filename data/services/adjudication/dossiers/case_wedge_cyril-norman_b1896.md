<!-- {"case_id": "case_wedge_cyril-norman_b1896", "bio_ids": ["wedge_cyril-norman_b1896"], "stint_ids": ["Wedge, C. N___Tanganyika___1924"]} -->
# Dossier case_wedge_cyril-norman_b1896

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `wedge_cyril-norman_b1896`

- Printed name: **WEDGE, CYRIL NORMAN**
- Birth year: 1896 (attested in editions [1928, 1929, 1930, 1931, 1932, 1933, 1934])
- Appears in editions: [1928, 1929, 1930, 1931, 1932, 1933, 1934]

### Verbatim printed entry text (OCR)

**Version `col1928-L70931.v` — printed in editions [1928, 1929, 1930, 1931, 1932, 1933, 1934]:**

> WEDGE, CAPT. CYRIL NORMAN.—B. 1896; schol., mod. hist., St. Catharine's Coll., Cambridge, Mar., 1915; 2nd lieut., Worcestershire Regt., Mar., 1915; served in Gallipoli (Suvla Bay), 1915; "1914-15" Star, Br. War and Victory Meds.; seconded 1st K.A.R., 1918; served in Portuguese E. Africa and Nyassaland, 1918-20; capt. and adjt., 2/1st K.A.R., Tanganyika Territory, 1920-23; pay and qrtmtr., pol. and prisons, Tanganyika Territory, January, 1923; supt., pol., Apr., 1931.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1915–1915 | schol., mod. hist. | — | [1928, 1929, 1930, 1931, 1932, 1933, 1934] |
| 1 | 1915–1915 | 2nd lieut., Worcestershire Regt. | — | [1928, 1929, 1930, 1931, 1932, 1933, 1934] |
| 2 | 1915–1915 | served | — | [1928, 1929, 1930, 1931, 1932, 1933, 1934] |
| 3 | 1918–1918 | seconded 1st K.A.R. | — | [1928, 1929, 1930, 1931, 1932, 1933, 1934] |
| 4 | 1918–1920 | served | Nyasaland | [1928, 1929, 1930, 1931, 1932, 1933, 1934] |
| 5 | 1920–1923 | capt. and adjt., 2/1st K.A.R. | Tanganyika Territory | [1928, 1929, 1930, 1931, 1932, 1933, 1934] |
| 6 | 1923–1923 | pay and qrtmtr., pol. and prisons | Tanganyika Territory | [1928, 1929, 1930, 1931, 1932, 1933, 1934] |
| 7 | 1931–1931 | supt., pol. | — | [1928, 1929, 1930, 1931, 1932, 1933, 1934] |

## Candidate stint `Wedge, C. N___Tanganyika___1924`

- Staff-list name: **Wedge, C. N** | colony: **Tanganyika** | listed 1924–1925 | editions [1924, 1925]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1924 | C. N. Wedge | Pay and Quartermaster | Police and Prisons Department | — | — |
| 1925 | C. N. Wedge | Pay and Quartermaster | Police and Prisons Department | — | — |

### Deterministic checks: `wedge_cyril-norman_b1896` vs `Wedge, C. N___Tanganyika___1924`

- [PASS] surname_gate: bio 'WEDGE' vs stint 'Wedge, C. N' (exact)
- [PASS] initials: bio ['C', 'N'] ~ stint ['C', 'N']
- [PASS] age_gate: stint starts 1924, birth 1896 (age 28)
- [FAIL] colony: no placed event resolves to 'Tanganyika'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1924-1925
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

