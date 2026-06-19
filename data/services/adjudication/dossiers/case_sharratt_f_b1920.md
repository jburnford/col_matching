<!-- {"case_id": "case_sharratt_f_b1920", "bio_ids": ["sharratt_f_b1920"], "stint_ids": ["Jarratt, G. F___Seychelles___1961"]} -->
# Dossier case_sharratt_f_b1920

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['sharratt_f_b1920'] carry a single initial only — the namesake trap applies.
- NOTE: stint `Jarratt, G. F___Seychelles___1961` is also gate-compatible with biography(ies) outside this case: ['jarratt_g-f_b1909'] (already linked elsewhere or filtered).

## Biography `sharratt_f_b1920`

- Printed name: **SHARRATT, F**
- Birth year: 1920 (attested in editions [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964])
- Appears in editions: [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964]

### Verbatim printed entry text (OCR)

**Version `col1957-L27109.v` — printed in editions [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964]:**

> SHARRATT, F.—b. 1920; ed. Royal Gram. Sch., Worcester; mil. serv., 1940-46, R.E.; dist. engrnr., B. Guiana, 1946; exec. engrnr., 1951; div. engrnr., Ken., 1953; senr. engrnr., 1955-63. (Ken. Govt. service.)

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1946 | dist. engrnr., B. Guiana | — | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964] |
| 1 | 1951 | exec. engrnr | — | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964] |
| 2 | 1953 | div. engrnr. | Kenya | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964] |
| 3 | 1955–1963 | senr. engrnr | Kenya *(inherited from previous clause)* | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964] |

## Candidate stint `Jarratt, G. F___Seychelles___1961`

- Staff-list name: **Jarratt, G. F** | colony: **Seychelles** | listed 1961–1962 | editions [1961, 1962]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1961 | G. F. Jarratt | Director of Tourism and Information | Civil Establishment | — | — |
| 1962 | G. F. Jarratt | Director of Tourism and Information | Civil Establishment | — | — |

### Deterministic checks: `sharratt_f_b1920` vs `Jarratt, G. F___Seychelles___1961`

- [PASS] surname_gate: bio 'SHARRATT' vs stint 'Jarratt, G. F' (fuzzy:2)
- [PASS] initials: bio ['F'] ~ stint ['G', 'F']
- [PASS] age_gate: stint starts 1961, birth 1920 (age 41)
- [FAIL] colony: no placed event resolves to 'Seychelles'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1961-1962
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

