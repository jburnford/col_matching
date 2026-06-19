<!-- {"case_id": "case_skipper_g-a_b1914", "bio_ids": ["skipper_g-a_b1914"], "stint_ids": ["Skipper, G. A___Western Pacific___1955"]} -->
# Dossier case_skipper_g-a_b1914

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `skipper_g-a_b1914`

- Printed name: **SKIPPER, G. A**
- Birth year: 1914 (attested in editions [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965])
- Honours: O.B.E (1962)
- Appears in editions: [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965]

### Verbatim printed entry text (OCR)

**Version `col1958-L26971.v` — printed in editions [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965]:**

> SKIPPER, G. A., O.B.E. (1962).—b. 1914; ed. Auckland Gram. Sch. and Auckland Univ. Coll., N.Z.; dist. offr., Ken., 1939; secon., W. Pac. High Comsn., 1952–56; senr. dist. comsnr., Ken., 1957; prov. comsnr., 1962–64. (Ken. Govt. service.)

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1939 | dist. offr. | Kenya | [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965] |
| 1 | 1952–1956 | secon., W. Pac. High Comsn | Western Pacific | [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965] |
| 2 | 1957 | senr. dist. comsnr. | Kenya | [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965] |
| 3 | 1962–1964 | prov. comsnr | Kenya *(inherited from previous clause)* | [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965] |

## Candidate stint `Skipper, G. A___Western Pacific___1955`

- Staff-list name: **Skipper, G. A** | colony: **Western Pacific** | listed 1955–1956 | editions [1955, 1956]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1955 | G. A. Skipper | Administrative Officer | Civil Establishment | — | — |
| 1956 | G. A. Skipper | Administrative Officer | Civil Establishment | — | — |

### Deterministic checks: `skipper_g-a_b1914` vs `Skipper, G. A___Western Pacific___1955`

- [PASS] surname_gate: bio 'SKIPPER' vs stint 'Skipper, G. A' (exact)
- [PASS] initials: bio ['G', 'A'] ~ stint ['G', 'A']
- [PASS] age_gate: stint starts 1955, birth 1914 (age 41)
- [PASS] colony: 1 placed event(s) resolve to 'Western Pacific'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1955-1956
- [FAIL] position_sim: best 27 vs bar 60: 'secon., W. Pac. High Comsn' ~ 'Administrative Officer'
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

