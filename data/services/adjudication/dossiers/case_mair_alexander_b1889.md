<!-- {"case_id": "case_mair_alexander_b1889", "bio_ids": ["mair_alexander_b1889"], "stint_ids": ["Mair, A. P___Trinidad and Tobago___1928"]} -->
# Dossier case_mair_alexander_b1889

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 10 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['mair_alexander_b1889'] carry a single initial only — the namesake trap applies.

## Biography `mair_alexander_b1889`

- Printed name: **MAIR, ALEXANDER**
- Birth year: 1889 (attested in editions [1940])
- Appears in editions: [1940]

### Verbatim printed entry text (OCR)

**Version `col1940-L66565.v` — printed in editions [1940]:**

> MAIR, HON. ALEXANDER.—B. 1889; M.L.A., Albury, N.S.W., June, 1932; astt. min., Apr., 1938; min. for lab. and industry, June, 1938; treas., Oct., 1938; premier, Aug., 1939.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1932 | M.L.A., Albury | New South Wales | [1940] |
| 1 | 1938 | astt. min | New South Wales *(inherited from previous clause)* | [1940] |
| 2 | 1939 | premier | New South Wales *(inherited from previous clause)* | [1940] |

## Candidate stint `Mair, A. P___Trinidad and Tobago___1928`

- Staff-list name: **Mair, A. P** | colony: **Trinidad and Tobago** | listed 1928–1934 | editions [1928, 1929, 1933, 1934]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1928 | A. P. Mair | Head Attendant (Female) | Lunatic Asylum | — | — |
| 1929 | A. P. Mair | Head Attendants (Female) | Lunatic Asylum | — | — |
| 1933 | Miss A. P. Mair | Head Attendant (Female) | Lunatic Asylum | — | — |
| 1934 | Miss A. P. Mair | Head Attendant (Female) | Lunatic Asylum | — | — |

### Deterministic checks: `mair_alexander_b1889` vs `Mair, A. P___Trinidad and Tobago___1928`

- [PASS] surname_gate: bio 'MAIR' vs stint 'Mair, A. P' (exact)
- [PASS] initials: bio ['A'] ~ stint ['A', 'P']
- [PASS] age_gate: stint starts 1928, birth 1889 (age 39)
- [FAIL] colony: no placed event resolves to 'Trinidad and Tobago'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1928-1934
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

