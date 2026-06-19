<!-- {"case_id": "case_beyers_frederick-william_e1907", "bio_ids": ["beyers_frederick-william_e1907", "beyers_fredrik-william_b1867"], "stint_ids": ["Beyers, F. W___South Africa___1912"]} -->
# Dossier case_beyers_frederick-william_e1907

## Case context

- 2 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 4 official(s) with this surname in the graph's staff lists; 4 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- CONTESTED: stint(s) ['Beyers, F. W___South Africa___1912'] have more than one claimant biography in this case.

## Biography `beyers_frederick-william_e1907`

- Printed name: **BEYERS, FREDERICK WILLIAM**
- Birth year: not printed
- Appears in editions: [1925, 1927, 1928, 1929]

### Verbatim printed entry text (OCR)

**Version `col1925-L54116.v` — printed in editions [1925, 1927, 1928, 1929]:**

> BEYERS, FREDERICK WILLIAM, B.A., LL.B., K.C., M.L.A.—Ed. S. African Coll., Schol. and at S. African Coll., Cape Town; called to the bar in 1908; mem., Transvaal parlt., for Turffontein, 1907-10; attended Col. Confoe, with General Botha, London, Mar.-May, 1907; atty.-gen., Transvaal, 1911-14 and for Cape Prov., 1914-15; resigned as atty.-gen., Aug., 1915; elec. to Union parl., as mem. for Edenburg, O.F.S., since 1918; min. of mines and industries in Hertzog cabinet, 30th June, 1924.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1907–1910 | mem., Transvaal parlt. | Transvaal | [1925, 1927, 1928, 1929] |
| 1 | 1907–1907 | attended Col. Confoe | — | [1925, 1927, 1928, 1929] |
| 2 | 1908–1908 | called to the bar | — | [1925, 1927, 1928, 1929] |
| 3 | 1911–1914 | atty.-gen. | Transvaal | [1925, 1927, 1928, 1929] |
| 4 | 1914–1915 | atty.-gen. | Cape Province | [1925, 1927, 1928, 1929] |
| 5 | 1915–1915 | atty.-gen. | — | [1925, 1927, 1928, 1929] |
| 6 | 1918 | mem. for Edenburg | Orange Free State | [1925, 1927, 1928, 1929] |
| 7 | 1924 | min. of mines and industries | — | [1925, 1927, 1928, 1929] |

## Biography `beyers_fredrik-william_b1867`

- Printed name: **BEYERS, FREDRIK WILLIAM**
- Birth year: 1867 (attested in editions [1913, 1914, 1915])
- Appears in editions: [1913, 1914, 1915]

### Verbatim printed entry text (OCR)

**Version `col1913-L43889.v` — printed in editions [1913, 1914, 1915]:**

> BEYERS, FREDRIK WILLIAM.—B.A., LL.B. (Cape); B. 1867; ed. at S. African Coll., Cape Town; advoc. of sup. ct., Cape and Transvaal; atty.-gen., Transvaal Province, June, 1911.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1911 | atty.-gen., Transvaal Province | Transvaal | [1913, 1914, 1915] |

## Candidate stint `Beyers, F. W___South Africa___1912`

- Staff-list name: **Beyers, F. W** | colony: **South Africa** | listed 1912–1914 | editions [1912, 1914]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1912 | F. W. Beyers | Attorney-General, Transvaal | Department of Justice | — | — |
| 1914 | F. W. Beyers | Attorney-General, Transvaal | Department of Justice | — | — |

### Deterministic checks: `beyers_frederick-william_e1907` vs `Beyers, F. W___South Africa___1912`

- [PASS] surname_gate: bio 'BEYERS' vs stint 'Beyers, F. W' (exact)
- [PASS] initials: bio ['F', 'W'] ~ stint ['F', 'W']
- [PASS] age_gate: stint starts 1912; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'South Africa'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1912-1914
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

### Deterministic checks: `beyers_fredrik-william_b1867` vs `Beyers, F. W___South Africa___1912`

- [PASS] surname_gate: bio 'BEYERS' vs stint 'Beyers, F. W' (exact)
- [PASS] initials: bio ['F', 'W'] ~ stint ['F', 'W']
- [PASS] age_gate: stint starts 1912, birth 1867 (age 45)
- [FAIL] colony: no placed event resolves to 'South Africa'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1912-1914
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

