<!-- {"case_id": "case_brown_d_b1928", "bio_ids": ["brown_d_b1928"], "stint_ids": ["Brown, D. R. N___Uganda___1957"]} -->
# Dossier case_brown_d_b1928

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 250 official(s) with this surname in the graph's staff lists; 114 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['brown_d_b1928'] carry a single initial only — the namesake trap applies.
- NOTE: stint `Brown, D. R. N___Uganda___1957` is also gate-compatible with biography(ies) outside this case: ['brown_donald-robert-norman_b1911'] (already linked elsewhere or filtered).

## Biography `brown_d_b1928`

- Printed name: **BROWN, D**
- Birth year: 1928 (attested in editions [1963, 1964, 1965, 1966])
- Appears in editions: [1962, 1963, 1964, 1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1963-L17770.v` — printed in editions [1963, 1964, 1965, 1966]:**

> BROWN, D.—b. 1928; ed. Rathgar Sch. and Avoca Sch., Dublin, Trinity Coll., Dublin; admin. cadet, Uga., 1951; dist. offr., 1953; hd. local law sch., 1962-65. (Uga. Govt. service.)

**Version `col1962-L19209.v` — printed in editions [1962]:**

> BROWN, D.—b. 1928; ed. Rathgar Sch. and Avoca Sch., Dublin, Trinity Coll., Dublin; admin. cadet, Uga., 1951; dist. offr., 1953.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1951 | admin. cadet | Uganda | [1962, 1963, 1964, 1965, 1966] |
| 1 | 1953 | dist. offr | Uganda *(inherited from previous clause)* | [1962, 1963, 1964, 1965, 1966] |
| 2 | 1962–1965 | hd. local law sch | Uganda *(inherited from previous clause)* | [1963, 1964, 1965, 1966] |

## Candidate stint `Brown, D. R. N___Uganda___1957`

- Staff-list name: **Brown, D. R. N** | colony: **Uganda** | listed 1957–1960 | editions [1957, 1959, 1960]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1957 | D. R. N. Brown | Deputy Director of Agriculture | Civil Establishment | — | — |
| 1959 | D. R. N. Brown | Deputy Directors of Agriculture | Civil Establishment | — | — |
| 1960 | D. R. N. Brown | Deputy Director of Agriculture | Civil Establishment | — | — |

### Deterministic checks: `brown_d_b1928` vs `Brown, D. R. N___Uganda___1957`

- [PASS] surname_gate: bio 'BROWN' vs stint 'Brown, D. R. N' (exact)
- [PASS] initials: bio ['D'] ~ stint ['D', 'R', 'N']
- [PASS] age_gate: stint starts 1957, birth 1928 (age 29)
- [PASS] colony: 3 placed event(s) resolve to 'Uganda'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1957-1960
- [FAIL] position_sim: best 31 vs bar 60: 'dist. offr' ~ 'Deputy Director of Agriculture'
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

