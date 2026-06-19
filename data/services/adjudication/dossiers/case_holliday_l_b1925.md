<!-- {"case_id": "case_holliday_l_b1925", "bio_ids": ["holliday_l_b1925"], "stint_ids": ["Holliday, L___Singapore___1949"]} -->
# Dossier case_holliday_l_b1925

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['holliday_l_b1925'] carry a single initial only — the namesake trap applies.

## Biography `holliday_l_b1925`

- Printed name: **HOLLIDAY, L.**
- Birth year: 1925 (attested in editions [1959, 1960, 1961, 1962, 1963, 1964, 1965])
- Appears in editions: [1959, 1960, 1961, 1962, 1963, 1964, 1965]

### Verbatim printed entry text (OCR)

**Version `col1959-L24233.v` — printed in editions [1959, 1960, 1961, 1962, 1963, 1964, 1965]:**

> HOLLIDAY, L.—b. 1925; ed. Broughton Sec. Sch., Edin.; mil. serv., 1943-47, R.A.F.; air traffic control offr., Pal., 1947; S'pore, 1948: ops. offr., 1953; N. Borneo, 1955-64.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1943–1947 | mil. serv. | — | [1959, 1960, 1961, 1962, 1963, 1964, 1965] |
| 1 | 1947–1947 | air traffic control offr. | Palestine | [1959, 1960, 1961, 1962, 1963, 1964, 1965] |
| 2 | 1948–1948 | — | Singapore | [1959, 1960, 1961, 1962, 1963, 1964, 1965] |
| 3 | 1953–1953 | ops. offr. | — | [1959, 1960, 1961, 1962, 1963, 1964, 1965] |
| 4 | 1955–1964 | — | North Borneo | [1959, 1960, 1961, 1962, 1963, 1964, 1965] |

## Candidate stint `Holliday, L___Singapore___1949`

- Staff-list name: **Holliday, L** | colony: **Singapore** | listed 1949–1951 | editions [1949, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | L. Holliday | Air Traffic Control Officers, Grade I | Civil Aviation | — | — |
| 1951 | L. Holliday | Air Traffic Control Officers, Grade I | Civil Aviation | — | — |

### Deterministic checks: `holliday_l_b1925` vs `Holliday, L___Singapore___1949`

- [PASS] surname_gate: bio 'HOLLIDAY' vs stint 'Holliday, L' (exact)
- [PASS] initials: bio ['L'] ~ stint ['L']
- [PASS] age_gate: stint starts 1949, birth 1925 (age 24)
- [PASS] colony: 1 placed event(s) resolve to 'Singapore'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1949-1951
- [FAIL] position_sim: no overlapping placed event to compare
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

