<!-- {"case_id": "case_johnson_vincent-kenneth_b1901", "bio_ids": ["johnson_vincent-kenneth_b1901"], "stint_ids": ["Johnson, O. V. K___Sierra Leone___1949", "Johnson, V___Cayman Islands___1965"]} -->
# Dossier case_johnson_vincent-kenneth_b1901

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 224 official(s) with this surname in the graph's staff lists; 86 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Johnson, O. V. K___Sierra Leone___1949` is also gate-compatible with biography(ies) outside this case: ['johnson_o-v-k_b1909', 'johnson_obadiah_e1888'] (already linked elsewhere or filtered).
- NOTE: stint `Johnson, V___Cayman Islands___1965` is also gate-compatible with biography(ies) outside this case: ['johnson_o-v-k_b1909'] (already linked elsewhere or filtered).

## Biography `johnson_vincent-kenneth_b1901`

- Printed name: **JOHNSON, Vincent Kenneth**
- Birth year: 1901 (attested in editions [1948, 1949, 1950, 1951, 1953])
- Honours: O.B.E (1951)
- Appears in editions: [1948, 1949, 1950, 1951, 1953]

### Verbatim printed entry text (OCR)

**Version `col1948-L33682.v` — printed in editions [1948, 1949, 1950, 1951, 1953]:**

> JOHNSON, Vincent Kenneth, O.B.E. (1951)—b. 1901; ed. Rottingdean and Harrow; cadet, Nig., 1926; senr. dist. offr., 1945; res., 1946.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1926 | cadet | Nigeria | [1948, 1949, 1950, 1951, 1953] |
| 1 | 1945 | senr. dist. offr | Nigeria *(inherited from previous clause)* | [1948, 1949, 1950, 1951, 1953] |
| 2 | 1946 | res | Nigeria *(inherited from previous clause)* | [1948, 1949, 1950, 1951, 1953] |

## Candidate stint `Johnson, O. V. K___Sierra Leone___1949`

- Staff-list name: **Johnson, O. V. K** | colony: **Sierra Leone** | listed 1949–1951 | editions [1949, 1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | O. V. K. Johnson | Nursing Sister | Medical | — | — |
| 1950 | O. V. K. Johnson | Nursing Sister | Medical | — | — |
| 1951 | O. V. K. Johnson | Nursing Sister | Medical | — | — |

### Deterministic checks: `johnson_vincent-kenneth_b1901` vs `Johnson, O. V. K___Sierra Leone___1949`

- [PASS] surname_gate: bio 'JOHNSON' vs stint 'Johnson, O. V. K' (exact)
- [PASS] initials: bio ['V', 'K'] ~ stint ['O', 'V', 'K']
- [PASS] age_gate: stint starts 1949, birth 1901 (age 48)
- [FAIL] colony: no placed event resolves to 'Sierra Leone'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1949-1951
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Johnson, V___Cayman Islands___1965`

- Staff-list name: **Johnson, V** | colony: **Cayman Islands** | listed 1965–1966 | editions [1965, 1966]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1965 | V. Johnson | Financial Secretary | Civil Establishment | — | — |
| 1966 | V. Johnson | Financial Secretary | Civil Establishment | — | — |

### Deterministic checks: `johnson_vincent-kenneth_b1901` vs `Johnson, V___Cayman Islands___1965`

- [PASS] surname_gate: bio 'JOHNSON' vs stint 'Johnson, V' (exact)
- [PASS] initials: bio ['V', 'K'] ~ stint ['V']
- [PASS] age_gate: stint starts 1965, birth 1901 (age 64)
- [FAIL] colony: no placed event resolves to 'Cayman Islands'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1965-1966
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

