<!-- {"case_id": "case_kapadia_k-k_b1919", "bio_ids": ["kapadia_k-k_b1919"], "stint_ids": ["Kapadia, K. K___Seychelles___1949"]} -->
# Dossier case_kapadia_k-k_b1919

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `kapadia_k-k_b1919`

- Printed name: **KAPADIA, K. K**
- Birth year: 1919 (attested in editions [1965, 1966])
- Appears in editions: [1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1965-L16669.v` — printed in editions [1965, 1966]:**

> KAPADIA, K. K.—b. 1919; ed. Bombay Univ.; asst. M.O., Sey., 1946; M.O., 1948; M.O., W. Nig., 1956. (W. Nig. Govt. service.)

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1946 | asst. M.O. | Seychelles | [1965, 1966] |
| 1 | 1948 | M.O | Seychelles *(inherited from previous clause)* | [1965, 1966] |
| 2 | 1956 | M.O. | Western Nigeria | [1965, 1966] |

## Candidate stint `Kapadia, K. K___Seychelles___1949`

- Staff-list name: **Kapadia, K. K** | colony: **Seychelles** | listed 1949–1951 | editions [1949, 1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | K. K. Kapadia | Medical Officers | Medical | — | — |
| 1950 | K. K. Kapadia | Medical Officer | MEDICAL | — | — |
| 1951 | K. K. Kapadia | Medical Officer | MEDICAL | — | — |

### Deterministic checks: `kapadia_k-k_b1919` vs `Kapadia, K. K___Seychelles___1949`

- [PASS] surname_gate: bio 'KAPADIA' vs stint 'Kapadia, K. K' (exact)
- [PASS] initials: bio ['K', 'K'] ~ stint ['K', 'K']
- [PASS] age_gate: stint starts 1949, birth 1919 (age 30)
- [PASS] colony: 2 placed event(s) resolve to 'Seychelles'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1949-1951
- [FAIL] position_sim: best 27 vs bar 60: 'asst. M.O.' ~ 'Medical Officer'
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

