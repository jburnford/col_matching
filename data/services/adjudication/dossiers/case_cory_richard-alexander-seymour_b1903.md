<!-- {"case_id": "case_cory_richard-alexander-seymour_b1903", "bio_ids": ["cory_richard-alexander-seymour_b1903"], "stint_ids": ["Cory, R. A. S___Jamaica___1946"]} -->
# Dossier case_cory_richard-alexander-seymour_b1903

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 4 official(s) with this surname in the graph's staff lists; 4 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `cory_richard-alexander-seymour_b1903`

- Printed name: **CORY, Richard Alexander Seymour**
- Birth year: 1903 (attested in editions [1948, 1950, 1951])
- Honours: L.R.C.P, M.B, M.R.C.S, O.B.E (1953)
- Terminal: retired 1960 — “retd., apptd. chest speclst., Bah., 1960.”
- Appears in editions: [1948, 1950, 1951, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1948-L31922.v` — printed in editions [1948, 1950, 1951]:**

> CORY, Richard Alexander Seymour, M.B., Ch.B., M.R.C.S., L.R.C.P.—b. 1903; ed. Cornwall Coll., J'ca. and Bristol Univ. (fellow of Amer. Coll. of Chest Physicians); tuberculosis offr., J'ca., 1934; S.M.O., Jubilee memorial sanatorium, 1939.

**Version `col1958-L21637.v` — printed in editions [1958, 1959, 1960, 1961, 1962, 1963, 1964]:**

> CORY, R. A. S., O.B.E. (1953)—b. 1903; ed. Cornwall Coll., J'ca, and Bristol Univ.; T.B. offr., J'ca, 1934; S.M.O., 1939; assoc. dir., Univ. Coll. of W. Indies; author of pp. on T.B. and chest surgery.

**Version `col1965-L14460.v` — printed in editions [1965, 1966]:**

> CORY, R. A. S., O.B.E. (1953).—b. 1903; ed. Cornwall Coll., J'ca, and Bristol Univ.; T.B. offr., J'ca, 1934; S.M.O., 1939-60; retd., apptd. chest speclst., Bah., 1960.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1934 | tuberculosis offr. | Jamaica | [1948, 1950, 1951, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 1 | 1939 | S.M.O., Jubilee memorial sanatorium | Jamaica *(inherited from previous clause)* | [1948, 1950, 1951, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |

## Candidate stint `Cory, R. A. S___Jamaica___1946`

- Staff-list name: **Cory, R. A. S** | colony: **Jamaica** | listed 1946–1951 | editions [1946, 1948, 1949, 1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1946 | R. A. S. Cory | — | Jamaica Schools Commission | — | — |
| 1948 | R. A. S. Cory | Member | Jamaica Schools Commission | — | — |
| 1949 | R. A. S. Cory | Senior Medical Officer | Medical | — | — |
| 1950 | R. A. S. Cory | Senior Medical Officers | MEDICAL | — | — |
| 1951 | R. A. S. Cory | Senior Medical Officer | MEDICAL | — | — |

### Deterministic checks: `cory_richard-alexander-seymour_b1903` vs `Cory, R. A. S___Jamaica___1946`

- [PASS] surname_gate: bio 'CORY' vs stint 'Cory, R. A. S' (exact)
- [PASS] initials: bio ['R', 'A', 'S'] ~ stint ['R', 'A', 'S']
- [PASS] age_gate: stint starts 1946, birth 1903 (age 43)
- [PASS] colony: 2 placed event(s) resolve to 'Jamaica'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1946-1951
- [FAIL] position_sim: best 42 vs bar 60: 'S.M.O., Jubilee memorial sanatorium' ~ 'Senior Medical Officer'
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

