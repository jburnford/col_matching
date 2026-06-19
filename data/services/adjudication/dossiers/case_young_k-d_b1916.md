<!-- {"case_id": "case_young_k-d_b1916", "bio_ids": ["young_k-d_b1916"], "stint_ids": ["Young, K. D___Zanzibar___1949"]} -->
# Dossier case_young_k-d_b1916

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 140 official(s) with this surname in the graph's staff lists; 58 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `young_k-d_b1916`

- Printed name: **YOUNG, K. D**
- Birth year: 1916 (attested in editions [1960, 1961, 1962, 1963])
- Honours: O.B.E (1961)
- Appears in editions: [1960, 1961, 1962, 1963]

### Verbatim printed entry text (OCR)

**Version `col1960-L29725.v` — printed in editions [1960, 1961, 1962, 1963]:**

> YOUNG, K. D., O.B.E. (1961), Brill. Star of Zanz.—b. 1916; ed. Sherborne, Trinity Hall, Camb., and St. Geo. Hosp., London; mil. serv., 1940-46, surg. lt.-com.; M.O., Zanz., 1947; S.M.O. (clinical), Som., 1955. (Som. Govt. service.)

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1947 | M.O. | Zanzibar | [1960, 1961, 1962, 1963] |
| 1 | 1955 | S.M.O. (clinical) | Somaliland | [1960, 1961, 1962, 1963] |

## Candidate stint `Young, K. D___Zanzibar___1949`

- Staff-list name: **Young, K. D** | colony: **Zanzibar** | listed 1949–1951 | editions [1949, 1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | K. D. Young | Medical Officers | Medical | — | — |
| 1950 | K. D. Young | Medical Officers | Health | — | — |
| 1951 | K. D. Young | Medical Officer | Health | — | — |

### Deterministic checks: `young_k-d_b1916` vs `Young, K. D___Zanzibar___1949`

- [PASS] surname_gate: bio 'YOUNG' vs stint 'Young, K. D' (exact)
- [PASS] initials: bio ['K', 'D'] ~ stint ['K', 'D']
- [PASS] age_gate: stint starts 1949, birth 1916 (age 33)
- [PASS] colony: 1 placed event(s) resolve to 'Zanzibar'
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

