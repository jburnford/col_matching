<!-- {"case_id": "case_bisley_g-g_b1915", "bio_ids": ["bisley_g-g_b1915"], "stint_ids": ["Bisley, G. G___Kenya___1949"]} -->
# Dossier case_bisley_g-g_b1915

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `bisley_g-g_b1915`

- Printed name: **BISLEY, G. G**
- Birth year: 1915 (attested in editions [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966])
- Appears in editions: [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1957-L21188.v` — printed in editions [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966]:**

> BISLEY, G. G.—b. 1915; ed. King's Coll. Sch., Wimbledon, King's Coll. Hosp. and London Univ.; mil. serv., 1940-46, sqdn. ldr.; M.O., Ken., 1946; ophthalmic spec., 1955. (Ken. Govt. service.)

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1946 | M.O. | Kenya | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 1 | 1955 | ophthalmic spec | Kenya *(inherited from previous clause)* | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |

## Candidate stint `Bisley, G. G___Kenya___1949`

- Staff-list name: **Bisley, G. G** | colony: **Kenya** | listed 1949–1951 | editions [1949, 1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | G. G. Bisley | Medical Officer | Medical | — | — |
| 1950 | G. G. Bisley | Medical Officer | Medical | — | — |
| 1951 | G. G. Bisley | Medical Officer | Medical | — | — |

### Deterministic checks: `bisley_g-g_b1915` vs `Bisley, G. G___Kenya___1949`

- [PASS] surname_gate: bio 'BISLEY' vs stint 'Bisley, G. G' (exact)
- [PASS] initials: bio ['G', 'G'] ~ stint ['G', 'G']
- [PASS] age_gate: stint starts 1949, birth 1915 (age 34)
- [PASS] colony: 2 placed event(s) resolve to 'Kenya'
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

