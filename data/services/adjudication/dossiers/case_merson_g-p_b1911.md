<!-- {"case_id": "case_merson_g-p_b1911", "bio_ids": ["merson_g-p_b1911"], "stint_ids": ["Merson, G. P___Zanzibar___1949"]} -->
# Dossier case_merson_g-p_b1911

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `merson_g-p_b1911`

- Printed name: **MERSON, G. P**
- Birth year: 1911 (attested in editions [1956, 1958, 1959, 1960, 1961, 1962])
- Appears in editions: [1956, 1957, 1958, 1959, 1960, 1961, 1962]

### Verbatim printed entry text (OCR)

**Version `col1956-L23036.v` — printed in editions [1956, 1958, 1959, 1960, 1961, 1962]:**

> MERSON, G. P.—b. 1911; ed. Aberdeen Gram. Sch. and Univ., and Lond. Univ.; M.O., Zanz., 1940; S.M.O., Tang., 1950.

**Version `col1957-L25656.v` — printed in editions [1957]:**

> MERSION, G. P.—b. 1911; ed. Aberdeen Gram. Sch. and Univ., and Lond. Univ.; M.O., Zanz., 1940; S.M.O., Tang., 1950.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1940 | M.O. | Zanzibar | [1956, 1957, 1958, 1959, 1960, 1961, 1962] |
| 1 | 1950 | S.M.O. | Tanganyika | [1956, 1957, 1958, 1959, 1960, 1961, 1962] |

## Candidate stint `Merson, G. P___Zanzibar___1949`

- Staff-list name: **Merson, G. P** | colony: **Zanzibar** | listed 1949–1951 | editions [1949, 1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | G. P. Merson | Medical Officers | Medical | — | — |
| 1950 | G. P. Merson | Medical Officers | Health | — | — |
| 1951 | G. P. Merson | Medical Officer | Health | — | — |

### Deterministic checks: `merson_g-p_b1911` vs `Merson, G. P___Zanzibar___1949`

- [PASS] surname_gate: bio 'MERSON' vs stint 'Merson, G. P' (exact)
- [PASS] initials: bio ['G', 'P'] ~ stint ['G', 'P']
- [PASS] age_gate: stint starts 1949, birth 1911 (age 38)
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

