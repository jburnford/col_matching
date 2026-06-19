<!-- {"case_id": "case_murphy_m-p_b1903", "bio_ids": ["murphy_m-p_b1903"], "stint_ids": ["Murphy, M. P___Fiji___1918", "Murphy, M. P___Straits Settlements___1931"]} -->
# Dossier case_murphy_m-p_b1903

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 73 official(s) with this surname in the graph's staff lists; 29 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `murphy_m-p_b1903`

- Printed name: **MURPHY, M. P**
- Birth year: 1903 (attested in editions [1955, 1956, 1957])
- Appears in editions: [1955, 1956, 1957]

### Verbatim printed entry text (OCR)

**Version `col1955-L22036.v` — printed in editions [1955, 1956, 1957]:**

> MURPHY, M. P.—b. 1903; ed. Our Lady's Mount, Cork, and National Univ., Ireland; p.o.w., 1942-45; asst. engrnr., P.W.D., F.M.S., 1928; drainage and irrig. dept., 1932; engrnr., 1937; state engrnr., 1946; dep. dir., drainage and irrig., Fed. of Mal., 1953; dir., 1955.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1928 | asst. engrnr., P.W.D. | Federated Malay States | [1955, 1956, 1957] |
| 1 | 1932 | drainage and irrig. dept | Federated Malay States *(inherited from previous clause)* | [1955, 1956, 1957] |
| 2 | 1937 | engrnr | Federated Malay States *(inherited from previous clause)* | [1955, 1956, 1957] |
| 3 | 1942–1945 | p.o.w | — | [1955, 1956, 1957] |
| 4 | 1946 | state engrnr | Federated Malay States *(inherited from previous clause)* | [1955, 1956, 1957] |
| 5 | 1953 | dep. dir., drainage and irrig., Fed. of Mal | Federated Malay States *(inherited from previous clause)* | [1955, 1956, 1957] |
| 6 | 1955 | dir | Federated Malay States *(inherited from previous clause)* | [1955, 1956, 1957] |

## Candidate stint `Murphy, M. P___Fiji___1918`

- Staff-list name: **Murphy, M. P** | colony: **Fiji** | listed 1918–1919 | editions [1918, 1919]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1918 | M. P. Murphy | Junior Sub-Inspector | Fiji Constabulary | — | — |
| 1919 | M. P. Murphy | Junior Sub-Inspector | Department of Justice | — | — |

### Deterministic checks: `murphy_m-p_b1903` vs `Murphy, M. P___Fiji___1918`

- [PASS] surname_gate: bio 'MURPHY' vs stint 'Murphy, M. P' (exact)
- [PASS] initials: bio ['M', 'P'] ~ stint ['M', 'P']
- [PASS] age_gate: stint starts 1918, birth 1903 (age 15)
- [FAIL] colony: no placed event resolves to 'Fiji'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1918-1919
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Murphy, M. P___Straits Settlements___1931`

- Staff-list name: **Murphy, M. P** | colony: **Straits Settlements** | listed 1931–1933 | editions [1931, 1933]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1931 | M P Murphy | Assistant Engineers | PUBLIC WORKS | — | — |
| 1933 | M. P. Murphy | Assistant Drainage and Irrigation Engineer | Drainage and Irrigation Department | — | — |

### Deterministic checks: `murphy_m-p_b1903` vs `Murphy, M. P___Straits Settlements___1931`

- [PASS] surname_gate: bio 'MURPHY' vs stint 'Murphy, M. P' (exact)
- [PASS] initials: bio ['M', 'P'] ~ stint ['M', 'P']
- [PASS] age_gate: stint starts 1931, birth 1903 (age 28)
- [FAIL] colony: no placed event resolves to 'Straits Settlements'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1931-1933
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

