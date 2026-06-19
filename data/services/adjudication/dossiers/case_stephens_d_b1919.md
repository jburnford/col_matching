<!-- {"case_id": "case_stephens_d_b1919", "bio_ids": ["stephens_d_b1919"], "stint_ids": ["Stephens, D. S___Malta___1958"]} -->
# Dossier case_stephens_d_b1919

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 40 official(s) with this surname in the graph's staff lists; 15 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['stephens_d_b1919'] carry a single initial only — the namesake trap applies.
- NOTE: stint `Stephens, D. S___Malta___1958` is also gate-compatible with biography(ies) outside this case: ['stephens_d-s_b1916'] (already linked elsewhere or filtered).

## Biography `stephens_d_b1919`

- Printed name: **STEPHENS, D**
- Birth year: 1919 (attested in editions [1960, 1961, 1962, 1963, 1964, 1965, 1966])
- Appears in editions: [1960, 1961, 1962, 1963, 1964, 1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1960-L28337.v` — printed in editions [1960, 1961, 1962, 1963, 1964, 1965, 1966]:**

> STEPHENS, D.—b. 1919; ed. Haileybury Coll., and Oxford Univ.; mil. serv., 1940-46; capt.; spec. (chemistry) G.C. dept. of agric., 1952; senr. chemist, dept. of agric., Uga., 1958-65. (Uga. Govt. service.)

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1952 | spec. (chemistry) G.C. dept. of agric | — | [1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 1 | 1958–1965 | senr. chemist, dept. of agric. | Uganda | [1960, 1961, 1962, 1963, 1964, 1965, 1966] |

## Candidate stint `Stephens, D. S___Malta___1958`

- Staff-list name: **Stephens, D. S** | colony: **Malta** | listed 1958–1962 | editions [1958, 1959, 1960, 1961, 1962]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1958 | D. S. Stephens | Legal Secretary | Maltese Imperial Government | — | — |
| 1959 | D. S. Stephens | Legal Secretary | Maltese Imperial Government | — | — |
| 1960 | D. S. Stephens | Legal Secretary | Civil Establishment | — | — |
| 1961 | D. S. Stephens | Legal Secretary | Civil Establishment | — | — |
| 1962 | D. S. Stephens | Legal Secretary | Civil Establishment | — | — |

### Deterministic checks: `stephens_d_b1919` vs `Stephens, D. S___Malta___1958`

- [PASS] surname_gate: bio 'STEPHENS' vs stint 'Stephens, D. S' (exact)
- [PASS] initials: bio ['D'] ~ stint ['D', 'S']
- [PASS] age_gate: stint starts 1958, birth 1919 (age 39)
- [FAIL] colony: no placed event resolves to 'Malta'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1958-1962
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

