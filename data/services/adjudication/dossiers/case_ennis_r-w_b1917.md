<!-- {"case_id": "case_ennis_r-w_b1917", "bio_ids": ["ennis_r-w_b1917"], "stint_ids": ["Ennis, R. W___Nigeria___1958"]} -->
# Dossier case_ennis_r-w_b1917

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 6 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `ennis_r-w_b1917`

- Printed name: **ENNIS, R. W**
- Birth year: 1917 (attested in editions [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964])
- Honours: O.B.E (1956)
- Appears in editions: [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964]

### Verbatim printed entry text (OCR)

**Version `col1957-L22828.v` — printed in editions [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964]:**

> ENNIS, R. W., O.B.E. (1956).—b. 1917; ed. Perth Modern Sch. and Univ. of W. Australia; mil. serv., 1940-46, lieut.; cadet, Nig., 1947; admin. offr., cl. II, 1954; cl. I, W. Nig., 1957; staff gr., 1957. (Nig. Govt. service.)

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1947 | cadet | Nigeria | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964] |
| 1 | 1954 | admin. offr., cl. II | Nigeria *(inherited from previous clause)* | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964] |
| 2 | 1957 | cl. I | Western Nigeria | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964] |

## Candidate stint `Ennis, R. W___Nigeria___1958`

- Staff-list name: **Ennis, R. W** | colony: **Nigeria** | listed 1958–1960 | editions [1958, 1960]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1958 | R. W. Ennis | Permanent Secretaries and Administrative Officers (Staff Grade) | Civil Establishment | — | — |
| 1960 | R. W. Ennis | Permanent Secretaries and Administrative Officers (Staff Grade) | Civil Establishment, Western Region | — | — |

### Deterministic checks: `ennis_r-w_b1917` vs `Ennis, R. W___Nigeria___1958`

- [PASS] surname_gate: bio 'ENNIS' vs stint 'Ennis, R. W' (exact)
- [PASS] initials: bio ['R', 'W'] ~ stint ['R', 'W']
- [PASS] age_gate: stint starts 1958, birth 1917 (age 41)
- [PASS] colony: 3 placed event(s) resolve to 'Nigeria'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1958-1960
- [FAIL] position_sim: best 31 vs bar 60: 'admin. offr., cl. II' ~ 'Permanent Secretaries and Administrative Officers (Staff Grade)'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

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

