<!-- {"case_id": "case_verrier_w-l-i_b1907", "bio_ids": ["verrier_w-l-i_b1907"], "stint_ids": ["Verrier, W. L. I___Fiji___1950"]} -->
# Dossier case_verrier_w-l-i_b1907

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `verrier_w-l-i_b1907`

- Printed name: **VERRIER, W. L. I**
- Birth year: 1907 (attested in editions [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966])
- Appears in editions: [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1956-L24747.v` — printed in editions [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966]:**

> VERRIER, W. L. I.—b. 1907; ed. Blundell's Sch. and Univs. of Wales and London; M.O., Fiji, 1938; S.M.O., 1955.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1938 | M.O. | Fiji | [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 1 | 1955 | S.M.O | Fiji *(inherited from previous clause)* | [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |

## Candidate stint `Verrier, W. L. I___Fiji___1950`

- Staff-list name: **Verrier, W. L. I** | colony: **Fiji** | listed 1950–1951 | editions [1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1950 | W. L. I. Verrier | Medical Officer | Medical | — | — |
| 1951 | W. L. I. Verrier | Medical Officer | MEDICAL | — | — |

### Deterministic checks: `verrier_w-l-i_b1907` vs `Verrier, W. L. I___Fiji___1950`

- [PASS] surname_gate: bio 'VERRIER' vs stint 'Verrier, W. L. I' (exact)
- [PASS] initials: bio ['W', 'L', 'I'] ~ stint ['W', 'L', 'I']
- [PASS] age_gate: stint starts 1950, birth 1907 (age 43)
- [PASS] colony: 2 placed event(s) resolve to 'Fiji'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1950-1951
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

