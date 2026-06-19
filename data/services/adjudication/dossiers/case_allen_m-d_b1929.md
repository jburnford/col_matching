<!-- {"case_id": "case_allen_m-d_b1929", "bio_ids": ["allen_m-d_b1929"], "stint_ids": ["Allen, M. D___Western Pacific___1959"]} -->
# Dossier case_allen_m-d_b1929

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 103 official(s) with this surname in the graph's staff lists; 49 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `allen_m-d_b1929`

- Printed name: **ALLEN, M. D**
- Birth year: 1929 (attested in editions [1965, 1966])
- Appears in editions: [1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1965-L13179.v` — printed in editions [1965, 1966]:**

> ALLEN, M. D.—b. 1929; ed. Abbots-holme Sch., Derbyshire and St. Andrews Univ.; mil. serv., 1947-49, 13th/18th Hussars; cadet, Aden, 1954; admin. offr., cl. B, N. Heb., 1958; B.S.I.P., 1963.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1954 | cadet | Aden | [1965, 1966] |
| 1 | 1958 | admin. offr., cl. B, N. Heb | Aden *(inherited from previous clause)* | [1965, 1966] |
| 2 | 1963 | B.S.I.P | Aden *(inherited from previous clause)* | [1965, 1966] |

## Candidate stint `Allen, M. D___Western Pacific___1959`

- Staff-list name: **Allen, M. D** | colony: **Western Pacific** | listed 1959–1962 | editions [1959, 1960, 1961, 1962]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1959 | M. D. Allen | Administrative Officer, Class B | British National Administration | — | — |
| 1960 | M. D. Allen | Administrative Officer, Class B | British National Administration | — | — |
| 1961 | M. D. Allen | Administrative Officer, Class B | British National Administration | — | — |
| 1962 | M. D. Allen | Administrative Officer, Class B | British National Administration | — | — |

### Deterministic checks: `allen_m-d_b1929` vs `Allen, M. D___Western Pacific___1959`

- [PASS] surname_gate: bio 'ALLEN' vs stint 'Allen, M. D' (exact)
- [PASS] initials: bio ['M', 'D'] ~ stint ['M', 'D']
- [PASS] age_gate: stint starts 1959, birth 1929 (age 30)
- [FAIL] colony: no placed event resolves to 'Western Pacific'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1959-1962
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

