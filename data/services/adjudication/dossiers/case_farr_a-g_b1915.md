<!-- {"case_id": "case_farr_a-g_b1915", "bio_ids": ["farr_a-g_b1915"], "stint_ids": ["Farr, A. G___Aden___1960"]} -->
# Dossier case_farr_a-g_b1915

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 8 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `farr_a-g_b1915`

- Printed name: **FARR, A. G**
- Birth year: 1915 (attested in editions [1956, 1957, 1958, 1959, 1960, 1961, 1962])
- Honours: M.B.E (1951)
- Appears in editions: [1956, 1957, 1958, 1959, 1960, 1961, 1962]

### Verbatim printed entry text (OCR)

**Version `col1956-L21069.v` — printed in editions [1956, 1957, 1958, 1959, 1960, 1961, 1962]:**

> FARR, A. G., M.B.E. (1951).—b. 1915; ed. Blundell's Sch. and Sidney Sussex Coll., Camb.; M.O., Tang., 1942; spec. grade M.O., 1951; S.M.O., 1953; Aden, 1959-61.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1942 | M.O. | Tanganyika | [1956, 1957, 1958, 1959, 1960, 1961, 1962] |
| 1 | 1951 | spec. grade M.O | Tanganyika *(inherited from previous clause)* | [1956, 1957, 1958, 1959, 1960, 1961, 1962] |
| 2 | 1953 | S.M.O | Tanganyika *(inherited from previous clause)* | [1956, 1957, 1958, 1959, 1960, 1961, 1962] |
| 3 | 1959–1961 | S.M.O | Aden | [1956, 1957, 1958, 1959, 1960, 1961, 1962] |

## Candidate stint `Farr, A. G___Aden___1960`

- Staff-list name: **Farr, A. G** | colony: **Aden** | listed 1960–1961 | editions [1960, 1961]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1960 | A. G. Farr | Senior Medical Officer | Civil Establishment | — | — |
| 1961 | A. G. Farr | Senior Medical Officer | Civil Establishment | — | — |

### Deterministic checks: `farr_a-g_b1915` vs `Farr, A. G___Aden___1960`

- [PASS] surname_gate: bio 'FARR' vs stint 'Farr, A. G' (exact)
- [PASS] initials: bio ['A', 'G'] ~ stint ['A', 'G']
- [PASS] age_gate: stint starts 1960, birth 1915 (age 45)
- [PASS] colony: 1 placed event(s) resolve to 'Aden'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1960-1961
- [FAIL] position_sim: best 16 vs bar 60: 'S.M.O' ~ 'Senior Medical Officer'
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

