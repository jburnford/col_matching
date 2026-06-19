<!-- {"case_id": "case_apted_f-i-c_b1915", "bio_ids": ["apted_f-i-c_b1915"], "stint_ids": ["Apted, F. I. C___Sierra Leone___1949"]} -->
# Dossier case_apted_f-i-c_b1915

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `apted_f-i-c_b1915`

- Printed name: **APTED, F. I. C**
- Birth year: 1915 (attested in editions [1956, 1957, 1959, 1960, 1961])
- Appears in editions: [1956, 1957, 1959, 1960, 1961, 1962]

### Verbatim printed entry text (OCR)

**Version `col1956-L19467.v` — printed in editions [1956, 1957, 1959, 1960, 1961]:**

> APTED, F. I. C.—b. 1915; ed. Merchant Taylors' Sch. and St. Thos. Hosp.; M.O., S.L., 1941; sleeping sickness specialist, Tang., 1951; author of Treatment of Rhodesian Sleeping Sickness by Mel B., Trans. R. Soc. Trop. Med. and Hyg., 1953.

**Version `col1962-L18377.v` — printed in editions [1962]:**

> APTED, F. I. C.—b. 1915; ed. Merchant Taylors' Sch. and St. Thos. Hosp.; M.O., S.L., 1941; sleeping sickness specialist, Tang., 1951-61.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1941 | M.O. | Sierra Leone | [1956, 1957, 1959, 1960, 1961, 1962] |
| 1 | 1951 | sleeping sickness specialist | Tanganyika | [1956, 1957, 1959, 1960, 1961, 1962] |
| 2 | 1953 | author of Treatment of Rhodesian Sleeping Sickness by Mel B., Trans. R. Soc. Trop. Med. and Hyg | Tanganyika *(inherited from previous clause)* | [1956, 1957, 1959, 1960, 1961] |

## Candidate stint `Apted, F. I. C___Sierra Leone___1949`

- Staff-list name: **Apted, F. I. C** | colony: **Sierra Leone** | listed 1949–1951 | editions [1949, 1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | F. I. C. Apted | Medical Officer | Medical | — | — |
| 1950 | F. I. C. Apted | Medical Officer | Medical | — | — |
| 1951 | F. I. C. Apted | Medical Officer | Medical | — | — |

### Deterministic checks: `apted_f-i-c_b1915` vs `Apted, F. I. C___Sierra Leone___1949`

- [PASS] surname_gate: bio 'APTED' vs stint 'Apted, F. I. C' (exact)
- [PASS] initials: bio ['F', 'I', 'C'] ~ stint ['F', 'I', 'C']
- [PASS] age_gate: stint starts 1949, birth 1915 (age 34)
- [PASS] colony: 1 placed event(s) resolve to 'Sierra Leone'
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

