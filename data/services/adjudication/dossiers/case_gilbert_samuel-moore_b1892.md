<!-- {"case_id": "case_gilbert_samuel-moore_b1892", "bio_ids": ["gilbert_samuel-moore_b1892"], "stint_ids": ["Gilbert, S. Moore___Trinidad and Tobago___1931"]} -->
# Dossier case_gilbert_samuel-moore_b1892

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 33 official(s) with this surname in the graph's staff lists; 14 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `gilbert_samuel-moore_b1892`

- Printed name: **GILBERT, SAMUEL MOORE**
- Birth year: 1892 (attested in editions [1935, 1936, 1937, 1940])
- Appears in editions: [1935, 1936, 1937, 1940]

### Verbatim printed entry text (OCR)

**Version `dol1935-L58865.v` — printed in editions [1935, 1936, 1937, 1940]:**

> GILBERT, SAMUEL MOORE, B.Sc. (Lond.), N.D.A. Dip. Agr. (Wye).—B. 1892; ed. City of Norwich Schl., Wye Coll. and London Univ.; command, The 1st King's Regt.; served in War, 1914-18; supt., agr., Nigeria, 1923; asst. dir., agr., Trinidad, 1929; ag. dir., 1929-30; M.L.C., 1933; ch. scientific offr., coffee research and experimental station, Tanganyika Territory, Mar., 1934.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1914–1918 | served in War | — | [1935, 1936, 1937, 1940] |
| 1 | 1923 | supt., agr. | Nigeria | [1935, 1936, 1937, 1940] |
| 2 | 1929 | asst. dir., agr. | Trinidad | [1935, 1936, 1937, 1940] |
| 3 | 1933 | M.L.C | Trinidad *(inherited from previous clause)* | [1935, 1936, 1937, 1940] |
| 4 | 1934 | ch. scientific offr., coffee research and experimental station, Tanganyika Territory | Tanganyika | [1935, 1936, 1937, 1940] |

## Candidate stint `Gilbert, S. Moore___Trinidad and Tobago___1931`

- Staff-list name: **Gilbert, S. Moore** | colony: **Trinidad and Tobago** | listed 1931–1934 | editions [1931, 1933, 1934]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1931 | S. Moore Gilbert | Assistant Director and Plant Pathologist | Department of Agriculture | — | Captain |
| 1933 | S. Moore Gilbert | Assistant Director and Plant Pathologist | Department of Agriculture | — | Captain |
| 1934 | S. Moore Gilbert | Assistant Director and Plant Pathologist | Department of Agriculture | — | Captain |

### Deterministic checks: `gilbert_samuel-moore_b1892` vs `Gilbert, S. Moore___Trinidad and Tobago___1931`

- [PASS] surname_gate: bio 'GILBERT' vs stint 'Gilbert, S. Moore' (exact)
- [PASS] initials: bio ['S', 'M'] ~ stint ['S', 'M']
- [PASS] age_gate: stint starts 1931, birth 1892 (age 39)
- [FAIL] colony: no placed event resolves to 'Trinidad and Tobago'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1931-1934
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

