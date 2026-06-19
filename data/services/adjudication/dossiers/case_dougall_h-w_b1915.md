<!-- {"case_id": "case_dougall_h-w_b1915", "bio_ids": ["dougall_h-w_b1915"], "stint_ids": ["Dougall, H. W___Sierra Leone___1949"]} -->
# Dossier case_dougall_h-w_b1915

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 4 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `dougall_h-w_b1915`

- Printed name: **DOUGALL, H. W**
- Birth year: 1915 (attested in editions [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965])
- Honours: O.B.E (1964)
- Appears in editions: [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965]

### Verbatim printed entry text (OCR)

**Version `col1957-L22626.v` — printed in editions [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965]:**

> DOUGALL, H. W., O.B.E. (1964).—b. 1915; ed. Durham Univ.; mil. serv., 1939-47; agric. chmst., S. Leone, 1947; pasture research chmst., Ken., 1952; senr. research offr. (Ken. Govt. service.)

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1947 | agric. chmst., S. Leone | — | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965] |
| 1 | 1952 | pasture research chmst. | Kenya | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965] |

## Candidate stint `Dougall, H. W___Sierra Leone___1949`

- Staff-list name: **Dougall, H. W** | colony: **Sierra Leone** | listed 1949–1951 | editions [1949, 1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | H. W. Dougall | Agricultural Chemist | Agricultural | — | — |
| 1950 | H. W. Dougall | Agricultural Chemist | Agricultural | — | — |
| 1951 | H. W. Dougall | Agricultural Chemist | AGRICULTURE | — | — |

### Deterministic checks: `dougall_h-w_b1915` vs `Dougall, H. W___Sierra Leone___1949`

- [PASS] surname_gate: bio 'DOUGALL' vs stint 'Dougall, H. W' (exact)
- [PASS] initials: bio ['H', 'W'] ~ stint ['H', 'W']
- [PASS] age_gate: stint starts 1949, birth 1915 (age 34)
- [FAIL] colony: no placed event resolves to 'Sierra Leone'
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

