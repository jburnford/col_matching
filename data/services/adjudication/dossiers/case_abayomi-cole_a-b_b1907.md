<!-- {"case_id": "case_abayomi-cole_a-b_b1907", "bio_ids": ["abayomi-cole_a-b_b1907"], "stint_ids": ["Abayomi-Cole, A. B___Sierra Leone___1949"]} -->
# Dossier case_abayomi-cole_a-b_b1907

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `abayomi-cole_a-b_b1907`

- Printed name: **ABAYOMI-COLE, A. B**
- Birth year: 1907 (attested in editions [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963])
- Honours: O.B.E (1960)
- Appears in editions: [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963]

### Verbatim printed entry text (OCR)

**Version `col1956-L19291.v` — printed in editions [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963]:**

> ABAYOMI-COLE, A. B., O.B.E. (1960)—b. 1907; ed. Govt. Model Sch., Prince of Wales Sch., S.L., and Durham Univ.; M.O., S.L., 1944; S.M.O., 1955; D.D.M.S., 1959; prin. M.O., 1960. (S.L. Govt. service.)

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1944 | M.O. | Sierra Leone | [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963] |
| 1 | 1955 | S.M.O | Sierra Leone *(inherited from previous clause)* | [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963] |
| 2 | 1959 | D.D.M.S | Sierra Leone *(inherited from previous clause)* | [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963] |
| 3 | 1960 | prin. M.O | Sierra Leone *(inherited from previous clause)* | [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963] |

## Candidate stint `Abayomi-Cole, A. B___Sierra Leone___1949`

- Staff-list name: **Abayomi-Cole, A. B** | colony: **Sierra Leone** | listed 1949–1951 | editions [1949, 1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | A. B. Abayomi-Cole | Medical Officer | Medical | — | — |
| 1950 | A. B. Abayomi-Cole | Medical Officer | Medical | — | — |
| 1951 | A. B. Abayomi-Cole | Medical Officer | Medical | — | — |

### Deterministic checks: `abayomi-cole_a-b_b1907` vs `Abayomi-Cole, A. B___Sierra Leone___1949`

- [PASS] surname_gate: bio 'ABAYOMI-COLE' vs stint 'Abayomi-Cole, A. B' (exact)
- [PASS] initials: bio ['A', 'B'] ~ stint ['A', 'B']
- [PASS] age_gate: stint starts 1949, birth 1907 (age 42)
- [PASS] colony: 4 placed event(s) resolve to 'Sierra Leone'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1949-1951
- [FAIL] position_sim: best 24 vs bar 60: 'M.O.' ~ 'Medical Officer'
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

