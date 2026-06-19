<!-- {"case_id": "case_catterall_n_b1920", "bio_ids": ["catterall_n_b1920"], "stint_ids": ["Catterall, N___St Helena___1952", "Catterall, N___Windward Islands___1955"]} -->
# Dossier case_catterall_n_b1920

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['catterall_n_b1920'] carry a single initial only — the namesake trap applies.

## Biography `catterall_n_b1920`

- Printed name: **CATTERALL, N**
- Birth year: 1920 (attested in editions [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965])
- Honours: M.B.E (1958)
- Appears in editions: [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965]

### Verbatim printed entry text (OCR)

**Version `col1958-L21272.v` — printed in editions [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965]:**

> CATTERALL, N., M.B.E. (1958).—b. 1920; ed. Bury Gram. Sch.; mil. serv., 1940-47; asst. audr., Nig., 1947; audr., 1950; St. H., 1951; prin. audr., Windward Is., 1955; Ken., 1958. (Ken. Govt. service.)

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1947 | asst. audr. | Nigeria | [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965] |
| 1 | 1950 | audr | Nigeria *(inherited from previous clause)* | [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965] |
| 2 | 1951 | St. H | Nigeria *(inherited from previous clause)* | [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965] |
| 3 | 1955 | prin. audr., Windward Is | Nigeria *(inherited from previous clause)* | [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965] |
| 4 | 1958 | prin. audr., Windward Is | Kenya | [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965] |

## Candidate stint `Catterall, N___St Helena___1952`

- Staff-list name: **Catterall, N** | colony: **St Helena** | listed 1952–1954 | editions [1952, 1953, 1954]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1952 | N. Catterall | Aide de Camp (Honorary) | Civil Establishment | — | — |
| 1953 | N. Catterall | Aide-de-Camp (Honorary) | Civil Establishment | — | — |
| 1954 | N. Catterall | Aide-de-Camp (Honorary) | Civil Establishment | — | — |

### Deterministic checks: `catterall_n_b1920` vs `Catterall, N___St Helena___1952`

- [PASS] surname_gate: bio 'CATTERALL' vs stint 'Catterall, N' (exact)
- [PASS] initials: bio ['N'] ~ stint ['N']
- [PASS] age_gate: stint starts 1952, birth 1920 (age 32)
- [FAIL] colony: no placed event resolves to 'St Helena'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1952-1954
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Catterall, N___Windward Islands___1955`

- Staff-list name: **Catterall, N** | colony: **Windward Islands** | listed 1955–1957 | editions [1955, 1956, 1957]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1955 | N. Catterall | Principal Auditor | Civil Establishment | — | — |
| 1956 | N. Catterall | Principal Auditor | Civil Establishment | — | — |
| 1957 | N. Catterall | Principal Auditor | Civil Establishment | — | — |

### Deterministic checks: `catterall_n_b1920` vs `Catterall, N___Windward Islands___1955`

- [PASS] surname_gate: bio 'CATTERALL' vs stint 'Catterall, N' (exact)
- [PASS] initials: bio ['N'] ~ stint ['N']
- [PASS] age_gate: stint starts 1955, birth 1920 (age 35)
- [FAIL] colony: no placed event resolves to 'Windward Islands'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1955-1957
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

