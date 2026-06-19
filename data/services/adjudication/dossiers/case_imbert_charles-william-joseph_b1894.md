<!-- {"case_id": "case_imbert_charles-william-joseph_b1894", "bio_ids": ["imbert_charles-william-joseph_b1894"], "stint_ids": ["Imbert, C. W. J___St Lucia___1917", "Imbert, C. W. J___Windward Islands___1918"]} -->
# Dossier case_imbert_charles-william-joseph_b1894

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 5 official(s) with this surname in the graph's staff lists; 4 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `imbert_charles-william-joseph_b1894`

- Printed name: **IMBERT, Charles William Joseph**
- Birth year: 1894 (attested in editions [1948])
- Appears in editions: [1948]

### Verbatim printed entry text (OCR)

**Version `col1948-L33553.v` — printed in editions [1948]:**

> IMBERT, Charles William Joseph.—b. 1894; ed. St. Mary's Coll., St. L.; called to bar (Lincoln's Inn), 1924; mag. and registr., Montserrat, 1942; comsnr. of sup. ct., 1945; crown atty., Montserrat, 1946; off., M.L.C., 1946; M.E.C., 1947; mag. Trin., 1947.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1924 | called to bar (Lincoln's Inn) | — | [1948] |
| 1 | 1942 | mag. and registr. | Montserrat | [1948] |
| 2 | 1945 | comsnr. of sup. ct | Montserrat *(inherited from previous clause)* | [1948] |
| 3 | 1946 | crown atty. | Montserrat | [1948] |
| 4 | 1947 | M.E.C | Montserrat *(inherited from previous clause)* | [1948] |

## Candidate stint `Imbert, C. W. J___St Lucia___1917`

- Staff-list name: **Imbert, C. W. J** | colony: **St Lucia** | listed 1917–1921 | editions [1917, 1921]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1917 | C. W. J. Imbert | Clerk | Judicial | — | — |
| 1921 | C. W. J. Imbert | 3rd Clerk | Civil Establishment | — | — |

### Deterministic checks: `imbert_charles-william-joseph_b1894` vs `Imbert, C. W. J___St Lucia___1917`

- [PASS] surname_gate: bio 'IMBERT' vs stint 'Imbert, C. W. J' (exact)
- [PASS] initials: bio ['C', 'W', 'J'] ~ stint ['C', 'W', 'J']
- [PASS] age_gate: stint starts 1917, birth 1894 (age 23)
- [FAIL] colony: no placed event resolves to 'St Lucia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1917-1921
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Imbert, C. W. J___Windward Islands___1918`

- Staff-list name: **Imbert, C. W. J** | colony: **Windward Islands** | listed 1918–1923 | editions [1918, 1919, 1920, 1922, 1923]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1918 | C. W. J. Imbert | Clerk | Judicial | — | — |
| 1919 | C. W. J. Imbert | Clerk | Judicial | — | — |
| 1920 | C. W. J. Imbert | 3rd Clerk | Civil Establishment | — | — |
| 1922 | C. W. J. Imbert | 3rd Clerk | Civil Establishment | — | — |
| 1923 | C. W. J. Imbert | 3rd Clerk | Civil Establishment | — | — |

### Deterministic checks: `imbert_charles-william-joseph_b1894` vs `Imbert, C. W. J___Windward Islands___1918`

- [PASS] surname_gate: bio 'IMBERT' vs stint 'Imbert, C. W. J' (exact)
- [PASS] initials: bio ['C', 'W', 'J'] ~ stint ['C', 'W', 'J']
- [PASS] age_gate: stint starts 1918, birth 1894 (age 24)
- [FAIL] colony: no placed event resolves to 'Windward Islands'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1918-1923
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

