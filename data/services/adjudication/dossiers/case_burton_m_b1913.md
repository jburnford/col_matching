<!-- {"case_id": "case_burton_m_b1913", "bio_ids": ["burton_m_b1913"], "stint_ids": ["Burton, Mrs. G. B. R___Barbados___1928"]} -->
# Dossier case_burton_m_b1913

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 38 official(s) with this surname in the graph's staff lists; 18 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['burton_m_b1913'] carry a single initial only — the namesake trap applies.
- NOTE: stint `Burton, Mrs. G. B. R___Barbados___1928` is also gate-compatible with biography(ies) outside this case: ['burton_g_e1868'] (already linked elsewhere or filtered).

## Biography `burton_m_b1913`

- Printed name: **BURTON, M**
- Birth year: 1913 (attested in editions [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966])
- Appears in editions: [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1958-L21059.v` — printed in editions [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966]:**

> BURTON, M.—b. 1913; ed. Royal Coll., Maur.; clk., customs and excise dept., Maur., 1937; 1st gr. clk., 1950; educ. off'r., 1952.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1937 | clk., customs and excise dept. | Mauritius | [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 1 | 1950 | 1st gr. clk | Mauritius *(inherited from previous clause)* | [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |

## Candidate stint `Burton, Mrs. G. B. R___Barbados___1928`

- Staff-list name: **Burton, Mrs. G. B. R** | colony: **Barbados** | listed 1928–1929 | editions [1928, 1929]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1928 | Mrs. G. B. R. Burton | Librarian | Public Library | — | — |
| 1929 | Mrs. G. B. R. Burton | Librarian | Public Library | — | — |

### Deterministic checks: `burton_m_b1913` vs `Burton, Mrs. G. B. R___Barbados___1928`

- [PASS] surname_gate: bio 'BURTON' vs stint 'Burton, Mrs. G. B. R' (exact)
- [PASS] initials: bio ['M'] ~ stint ['M', 'G', 'B', 'R']
- [PASS] age_gate: stint starts 1928, birth 1913 (age 15)
- [FAIL] colony: no placed event resolves to 'Barbados'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1928-1929
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

