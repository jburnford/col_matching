<!-- {"case_id": "case_herwitt_frank-ernest_b1863", "bio_ids": ["herwitt_frank-ernest_b1863"], "stint_ids": ["Hewitt, F. E___South Africa___1912", "Hewitt, F___Kenya___1939"]} -->
# Dossier case_herwitt_frank-ernest_b1863

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 16 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `herwitt_frank-ernest_b1863`

- Printed name: **HERWITT, FRANK ERNEST**
- Birth year: 1863 (attested in editions [1913])
- Appears in editions: [1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921, 1923]

### Verbatim printed entry text (OCR)

**Version `col1913-L46689.v` — printed in editions [1913]:**

> HERWITT, FRANK ERNEST.—B. 1863; educ. at King Edward Schl., Birmingham and Trin. Coll., Camb., B.A., Math. Tripos, 1883; inspr. of schl., Transvaal, 10th May, 1902; regirn., educn. dept., Transvaal, 1st Mar., 1903.

**Version `col1914-L47119.v` — printed in editions [1914, 1915, 1917, 1918, 1919, 1920, 1921, 1923]:**

> HEWITT, FRANK ERNEST.—B. 1863; educ. at King Edward Schl., Birmingham and Trin. Coll., Camb., B.A., Math. Tripos., 1883; inspr. of schls., Transvaal, 10th May, 1902; registr., educn. dept., Transvaal, 1st Mar., 1903.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1902 | inspr. of schl. | Transvaal | [1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921, 1923] |
| 1 | 1903 | regirn., educn. dept. | Transvaal | [1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921, 1923] |

## Candidate stint `Hewitt, F. E___South Africa___1912`

- Staff-list name: **Hewitt, F. E** | colony: **South Africa** | listed 1912–1918 | editions [1912, 1914, 1918]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1912 | F. E. Hewitt | Registrar | Education Department | — | — |
| 1914 | F. E. Hewitt | Registrar | Education Department | — | — |
| 1918 | F. E. Hewitt | Registrar | Education Department | — | — |

### Deterministic checks: `herwitt_frank-ernest_b1863` vs `Hewitt, F. E___South Africa___1912`

- [PASS] surname_gate: bio 'HERWITT' vs stint 'Hewitt, F. E' (fuzzy:1)
- [PASS] initials: bio ['F', 'E'] ~ stint ['F', 'E']
- [PASS] age_gate: stint starts 1912, birth 1863 (age 49)
- [FAIL] colony: no placed event resolves to 'South Africa'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1912-1918
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Hewitt, F___Kenya___1939`

- Staff-list name: **Hewitt, F** | colony: **Kenya** | listed 1939–1940 | editions [1939, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1939 | F. Hewitt | Senior Sanitary Inspector | Medical Department | — | — |
| 1940 | F. Hewitt | Senior Health Inspector | Medical Department | — | — |

### Deterministic checks: `herwitt_frank-ernest_b1863` vs `Hewitt, F___Kenya___1939`

- [PASS] surname_gate: bio 'HERWITT' vs stint 'Hewitt, F' (fuzzy:1)
- [PASS] initials: bio ['F', 'E'] ~ stint ['F']
- [PASS] age_gate: stint starts 1939, birth 1863 (age 76)
- [FAIL] colony: no placed event resolves to 'Kenya'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1939-1940
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

