<!-- {"case_id": "case_collings_a_b1919", "bio_ids": ["collings_a_b1919"], "stint_ids": ["Collings, M. A___Gibraltar___1950"]} -->
# Dossier case_collings_a_b1919

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 5 official(s) with this surname in the graph's staff lists; 4 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['collings_a_b1919'] carry a single initial only — the namesake trap applies.
- NOTE: stint `Collings, M. A___Gibraltar___1950` is also gate-compatible with biography(ies) outside this case: ['collings_maurice-arthur_b1915'] (already linked elsewhere or filtered).

## Biography `collings_a_b1919`

- Printed name: **COLLINGS, A**
- Birth year: 1919 (attested in editions [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966])
- Appears in editions: [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1957-L22060.v` — printed in editions [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966]:**

> COLLINGS, A.—b. 1919; ed. Collyer's Sch.; mil. serv., 1940–46; cadet, Tang., 1946; dist. offrr., 1948; admin. offrr., cl. IIB, 1959; gr. II, 1961. (Tanzania Govt. service.)

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1946 | cadet | Tanganyika | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 1 | 1948 | dist. offrr | Tanganyika *(inherited from previous clause)* | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 2 | 1959 | admin. offrr., cl. IIB | Tanganyika *(inherited from previous clause)* | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 3 | 1961 | gr. II | Tanganyika *(inherited from previous clause)* | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |

## Candidate stint `Collings, M. A___Gibraltar___1950`

- Staff-list name: **Collings, M. A** | colony: **Gibraltar** | listed 1950–1952 | editions [1950, 1951, 1952]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1950 | M. A. Collings | Principal Auditor | AUDIT | — | — |
| 1951 | M. A. Collings | Principal Auditor | Audit | — | — |
| 1952 | M. A. Collings | Principal Auditor | Civil Establishment | — | — |

### Deterministic checks: `collings_a_b1919` vs `Collings, M. A___Gibraltar___1950`

- [PASS] surname_gate: bio 'COLLINGS' vs stint 'Collings, M. A' (exact)
- [PASS] initials: bio ['A'] ~ stint ['M', 'A']
- [PASS] age_gate: stint starts 1950, birth 1919 (age 31)
- [FAIL] colony: no placed event resolves to 'Gibraltar'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1950-1952
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

