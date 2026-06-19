<!-- {"case_id": "case_irving_henry-t_b1833", "bio_ids": ["irving_henry-t_b1833"], "stint_ids": ["Irving, Henry Turner___British Guiana___1883", "Irving, Henry Turner___Trinidad___1877"]} -->
# Dossier case_irving_henry-t_b1833

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 28 official(s) with this surname in the graph's staff lists; 15 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Irving, Henry Turner___British Guiana___1883` is also gate-compatible with biography(ies) outside this case: ['irving_henry-t_e1854'] (already linked elsewhere or filtered).
- NOTE: stint `Irving, Henry Turner___Trinidad___1877` is also gate-compatible with biography(ies) outside this case: ['irving_henry-t_e1854'] (already linked elsewhere or filtered).

## Biography `irving_henry-t_b1833`

- Printed name: **IRVING, Henry T**
- Birth year: 1833 (attested in editions [1915])
- Honours: C.M.G (1878), G.C.M.G (1888)
- Appears in editions: [1915]

### Verbatim printed entry text (OCR)

**Version `col1915-L48031.v` — printed in editions [1915]:**

> IRVING, Sir Henry T., G.C.M.G. (1888), C.M.G. (1878), C.M.G. (1874).—B. 1833; clk. to admnstr., O.F.S. Prov., 10th Aug., 1852; clk. to admnstr., O.F.S. Prov., 10th Aug., 1852.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1852 | clk. to admnstr., O.F.S. Prov | Orange Free State | [1915] |

## Candidate stint `Irving, Henry Turner___British Guiana___1883`

- Staff-list name: **Irving, Henry Turner** | colony: **British Guiana** | listed 1883–1886 | editions [1883, 1886]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1883 | Sir Henry Turner Irving | Governor | Civil Establishment | K.C.M.G. | — |

### Deterministic checks: `irving_henry-t_b1833` vs `Irving, Henry Turner___British Guiana___1883`

- [PASS] surname_gate: bio 'IRVING' vs stint 'Irving, Henry Turner' (exact)
- [PASS] initials: bio ['H', 'T'] ~ stint ['H', 'T']
- [PASS] age_gate: stint starts 1883, birth 1833 (age 50)
- [FAIL] colony: no placed event resolves to 'British Guiana'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1883-1886
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Irving, Henry Turner___Trinidad___1877`

- Staff-list name: **Irving, Henry Turner** | colony: **Trinidad** | listed 1877–1880 | editions [1877, 1879, 1880]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | Henry Turner Irving | Governor and Commander-in-Chief | Civil Establishment | C.M.G. | — |

### Deterministic checks: `irving_henry-t_b1833` vs `Irving, Henry Turner___Trinidad___1877`

- [PASS] surname_gate: bio 'IRVING' vs stint 'Irving, Henry Turner' (exact)
- [PASS] initials: bio ['H', 'T'] ~ stint ['H', 'T']
- [PASS] age_gate: stint starts 1877, birth 1833 (age 44)
- [FAIL] colony: no placed event resolves to 'Trinidad'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1877-1880
- [FAIL] position_sim: no overlapping placed event to compare
- [PASS] honour: shared: C.M.G
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

