<!-- {"case_id": "case_colborne_d-a-r_b1928", "bio_ids": ["colborne_d-a-r_b1928"], "stint_ids": ["Colborne, D. A. R___Hong Kong___1951"]} -->
# Dossier case_colborne_d-a-r_b1928

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 4 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `colborne_d-a-r_b1928`

- Printed name: **COLBORNE, D. A. R**
- Birth year: 1928 (attested in editions [1960, 1961])
- Appears in editions: [1960, 1961]

### Verbatim printed entry text (OCR)

**Version `col1960-L21736.v` — printed in editions [1960, 1961]:**

> COLBORNE, D. A. R.—b. 1928; ed. Bournemouth and Reading; supt., police, H.K., 1949; supt., Sarawak constab., 1958.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1949 | supt., police | Hong Kong | [1960, 1961] |
| 1 | 1958 | supt., Sarawak constab | Sarawak | [1960, 1961] |

## Candidate stint `Colborne, D. A. R___Hong Kong___1951`

- Staff-list name: **Colborne, D. A. R** | colony: **Hong Kong** | listed 1951–1952 | editions [1951, 1952]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1951 | D. A. R. Colborne | Aide-de-Camp | Civil Establishment | — | — |
| 1952 | D. A. R. Colborne | Aide-de-Camp | Civil Establishment | — | — |

### Deterministic checks: `colborne_d-a-r_b1928` vs `Colborne, D. A. R___Hong Kong___1951`

- [PASS] surname_gate: bio 'COLBORNE' vs stint 'Colborne, D. A. R' (exact)
- [PASS] initials: bio ['D', 'A', 'R'] ~ stint ['D', 'A', 'R']
- [PASS] age_gate: stint starts 1951, birth 1928 (age 23)
- [PASS] colony: 1 placed event(s) resolve to 'Hong Kong'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1951-1952
- [FAIL] position_sim: best 29 vs bar 60: 'supt., police' ~ 'Aide-de-Camp'
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

