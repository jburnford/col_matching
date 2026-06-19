<!-- {"case_id": "case_boyd_j_b1913", "bio_ids": ["boyd_j_b1913"], "stint_ids": ["Boyd, C. J___Straits Settlements___1931", "Boyd, J___North Borneo___1949"]} -->
# Dossier case_boyd_j_b1913

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 38 official(s) with this surname in the graph's staff lists; 16 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['boyd_j_b1913'] carry a single initial only — the namesake trap applies.
- NOTE: stint `Boyd, J___North Borneo___1949` is also gate-compatible with biography(ies) outside this case: ['boyd_john-alexander_b1837'] (already linked elsewhere or filtered).

## Biography `boyd_j_b1913`

- Printed name: **BOYD, J**
- Birth year: 1913 (attested in editions [1959, 1960])
- Appears in editions: [1959, 1960]

### Verbatim printed entry text (OCR)

**Version `col1959-L20987.v` — printed in editions [1959, 1960]:**

> BOYD, J.—b. 1913; ed. Ballymena Academy and Royal Coll., Edin.; mil. serv., 1940-46, capt., R.A.M.C.; M.O., N. Borneo, 1948-60.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1948–1960 | M.O. | North Borneo | [1959, 1960] |

## Candidate stint `Boyd, C. J___Straits Settlements___1931`

- Staff-list name: **Boyd, C. J** | colony: **Straits Settlements** | listed 1931–1933 | editions [1931, 1933]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1931 | C. J. Boyd | Health Officer | Health Branch | — | — |
| 1933 | C. J. Boyd | Health Officer | Health Branch | — | — |

### Deterministic checks: `boyd_j_b1913` vs `Boyd, C. J___Straits Settlements___1931`

- [PASS] surname_gate: bio 'BOYD' vs stint 'Boyd, C. J' (exact)
- [PASS] initials: bio ['J'] ~ stint ['C', 'J']
- [PASS] age_gate: stint starts 1931, birth 1913 (age 18)
- [FAIL] colony: no placed event resolves to 'Straits Settlements'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1931-1933
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Boyd, J___North Borneo___1949`

- Staff-list name: **Boyd, J** | colony: **North Borneo** | listed 1949–1951 | editions [1949, 1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | J. Boyd | Medical Officer | MEDICAL | — | — |
| 1950 | J. Boyd | Medical Officer | MEDICAL | — | — |
| 1951 | J. Boyd | Medical Officer | MEDICAL | — | — |

### Deterministic checks: `boyd_j_b1913` vs `Boyd, J___North Borneo___1949`

- [PASS] surname_gate: bio 'BOYD' vs stint 'Boyd, J' (exact)
- [PASS] initials: bio ['J'] ~ stint ['J']
- [PASS] age_gate: stint starts 1949, birth 1913 (age 36)
- [PASS] colony: 1 placed event(s) resolve to 'North Borneo'
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

