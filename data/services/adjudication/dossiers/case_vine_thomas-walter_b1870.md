<!-- {"case_id": "case_vine_thomas-walter_b1870", "bio_ids": ["vine_thomas-walter_b1870"], "stint_ids": ["Vine, T. W___South Africa___1912", "Vine, T. W___Swaziland___1917"]} -->
# Dossier case_vine_thomas-walter_b1870

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 8 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `vine_thomas-walter_b1870`

- Printed name: **VINE, THOMAS WALTER**
- Birth year: 1870 (attested in editions [1930])
- Honours: D.C.M
- Appears in editions: [1930]

### Verbatim printed entry text (OCR)

**Version `col1930-L69105.v` — printed in editions [1930]:**

> VINE, THOMAS WALTER, D.C.M.—B. 1870; S.A. constab., 1901; Swaziland pol., 1907; sub-inspr., 1913; dep. asst. comsrr., 1925.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1901 | S.A. constab | — | [1930] |
| 1 | 1907 | Swaziland pol | Swaziland | [1930] |
| 2 | 1913 | sub-inspr | Swaziland *(inherited from previous clause)* | [1930] |
| 3 | 1925 | dep. asst. comsrr | Swaziland *(inherited from previous clause)* | [1930] |

## Candidate stint `Vine, T. W___South Africa___1912`

- Staff-list name: **Vine, T. W** | colony: **South Africa** | listed 1912–1918 | editions [1912, 1914, 1918]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1912 | T. W. Vine | Superintendent | Establishment | — | — |
| 1912 | T. W. Vine | Superintendent | Police | — | — |
| 1914 | T. W. Vine | Acting Sub-Inspector | Police | — | — |
| 1918 | T. W. Vine | Sub-Inspector | Police | — | — |

### Deterministic checks: `vine_thomas-walter_b1870` vs `Vine, T. W___South Africa___1912`

- [PASS] surname_gate: bio 'VINE' vs stint 'Vine, T. W' (exact)
- [PASS] initials: bio ['T', 'W'] ~ stint ['T', 'W']
- [PASS] age_gate: stint starts 1912, birth 1870 (age 42)
- [FAIL] colony: no placed event resolves to 'South Africa'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1912-1918
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Vine, T. W___Swaziland___1917`

- Staff-list name: **Vine, T. W** | colony: **Swaziland** | listed 1917–1927 | editions [1917, 1921, 1923, 1925, 1927]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1917 | T. W. Vine | Acting Sub-Inspector | Police | — | — |
| 1921 | T. W. Vine | Sub-Inspector | Police | — | — |
| 1923 | T. W. Vine | Sub-Inspector | Police | — | — |
| 1925 | T. W. Vine | Sub-Inspector | Police | — | — |
| 1927 | T. W. Vine | Deputy Assistant Commissioner, Mbabane (Pigg's Peak) | Administration Establishment | — | — |

### Deterministic checks: `vine_thomas-walter_b1870` vs `Vine, T. W___Swaziland___1917`

- [PASS] surname_gate: bio 'VINE' vs stint 'Vine, T. W' (exact)
- [PASS] initials: bio ['T', 'W'] ~ stint ['T', 'W']
- [PASS] age_gate: stint starts 1917, birth 1870 (age 47)
- [PASS] colony: 3 placed event(s) resolve to 'Swaziland'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1917-1927
- [PASS] position_sim: best 80 vs bar 60: 'sub-inspr' ~ 'Sub-Inspector'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: ALL supporting events inherit their place from an earlier clause — weak evidence

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

