<!-- {"case_id": "case_sharp_t-m-b_b1923", "bio_ids": ["sharp_t-m-b_b1923"], "stint_ids": ["Sharp, B___Northern Rhodesia___1949"]} -->
# Dossier case_sharp_t-m-b_b1923

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 28 official(s) with this surname in the graph's staff lists; 13 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Sharp, B___Northern Rhodesia___1949` is also gate-compatible with biography(ies) outside this case: ['sharp_frederick-brooke_b1891'] (already linked elsewhere or filtered).

## Biography `sharp_t-m-b_b1923`

- Printed name: **SHARP, T. M. B**
- Birth year: 1923 (attested in editions [1960, 1961, 1962, 1963, 1964, 1965, 1966])
- Honours: O.B.E (1966)
- Appears in editions: [1960, 1961, 1962, 1963, 1964, 1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1960-L27901.v` — printed in editions [1960, 1961, 1962, 1963, 1964, 1965, 1966]:**

> SHARP, T. M. B., O.B.E. (1966).—b. 1923; ed. Tonbridge Sch., and Aberdeen, Camb. and London Univs.; mil. serv., 1941-46, capt.; Indian civil serv., 1946; admin. offr., Nig., 1948; asst. D.O., 1952; D.O., N. Nig., 1954; senr., D.O., 1960; dep. perm. sec., min. of local govt., 1963. (Nig. Govt. service.)

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1946 | Indian civil serv | — | [1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 1 | 1948 | admin. offr. | Nigeria | [1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 2 | 1952 | asst. D.O | Nigeria *(inherited from previous clause)* | [1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 3 | 1954 | D.O. | Northern Nigeria | [1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 4 | 1960 | senr. | Dominions Office | [1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 5 | 1963 | dep. perm. sec., min. of local govt | Dominions Office *(inherited from previous clause)* | [1960, 1961, 1962, 1963, 1964, 1965, 1966] |

## Candidate stint `Sharp, B___Northern Rhodesia___1949`

- Staff-list name: **Sharp, B** | colony: **Northern Rhodesia** | listed 1949–1951 | editions [1949, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | B. Sharp | Superintendent | PRISONS | — | — |
| 1951 | B. Sharp | Superintendent | PRISONS | — | — |

### Deterministic checks: `sharp_t-m-b_b1923` vs `Sharp, B___Northern Rhodesia___1949`

- [PASS] surname_gate: bio 'SHARP' vs stint 'Sharp, B' (exact)
- [PASS] initials: bio ['T', 'M', 'B'] ~ stint ['B']
- [PASS] age_gate: stint starts 1949, birth 1923 (age 26)
- [FAIL] colony: no placed event resolves to 'Northern Rhodesia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1949-1951
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

