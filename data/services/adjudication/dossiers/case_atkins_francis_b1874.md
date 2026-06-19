<!-- {"case_id": "case_atkins_francis_b1874", "bio_ids": ["atkins_francis_b1874"], "stint_ids": ["Atkins, C. F___Kenya___1953"]} -->
# Dossier case_atkins_francis_b1874

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 14 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['atkins_francis_b1874'] carry a single initial only — the namesake trap applies.
- NOTE: stint `Atkins, C. F___Kenya___1953` is also gate-compatible with biography(ies) outside this case: ['atkins_charles-farquhar_b1907'] (already linked elsewhere or filtered).

## Biography `atkins_francis_b1874`

- Printed name: **ATKINS, Francis**
- Birth year: 1874 (attested in editions [1931])
- Appears in editions: [1931]

### Verbatim printed entry text (OCR)

**Version `col1931-L62090.v` — printed in editions [1931]:**

> ATKINS, Francis.—B. 1874; Imp. post office, 1893-1923; post & tels. divnl. engr., Nigeria, 1923; asst. engr.-in-ch., 1928.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1893–1923 | Imp. post office | — | [1931] |
| 1 | 1923 | post & tels. divnl. engr. | Nigeria | [1931] |
| 2 | 1928 | asst. engr.-in-ch | Nigeria *(inherited from previous clause)* | [1931] |

## Candidate stint `Atkins, C. F___Kenya___1953`

- Staff-list name: **Atkins, C. F** | colony: **Kenya** | listed 1953–1954 | editions [1953, 1954]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1953 | C. F. Atkins | Senior District Commissioner | Civil Establishment | — | — |
| 1954 | C. F. Atkins | Senior District Commissioner | Civil Establishment | — | — |

### Deterministic checks: `atkins_francis_b1874` vs `Atkins, C. F___Kenya___1953`

- [PASS] surname_gate: bio 'ATKINS' vs stint 'Atkins, C. F' (exact)
- [PASS] initials: bio ['F'] ~ stint ['C', 'F']
- [PASS] age_gate: stint starts 1953, birth 1874 (age 79)
- [FAIL] colony: no placed event resolves to 'Kenya'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1953-1954
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

