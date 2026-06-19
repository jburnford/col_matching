<!-- {"case_id": "case_hargreaves_a_b1913", "bio_ids": ["hargreaves_a_b1913"], "stint_ids": ["Hargreaves, A. L___Western Pacific___1961"]} -->
# Dossier case_hargreaves_a_b1913

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 17 official(s) with this surname in the graph's staff lists; 6 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['hargreaves_a_b1913'] carry a single initial only — the namesake trap applies.

## Biography `hargreaves_a_b1913`

- Printed name: **HARGREAVES, A**
- Birth year: 1913 (attested in editions [1957, 1958, 1959, 1960, 1961, 1962, 1963])
- Appears in editions: [1957, 1958, 1959, 1960, 1961, 1962, 1963]

### Verbatim printed entry text (OCR)

**Version `col1957-L23833.v` — printed in editions [1957, 1958, 1959, 1960, 1961, 1962, 1963]:**

> HARGREAVES, A.—b. 1913; ed. Lancaster Royal Gram. Sch., Downing Coll., Camb., Univ. Coll. Hosp., London, Columbia Univ., N.Y. and Berne Univ.; mil. serv., 1940-45, sqdn.-ldr.; M.O., Ken., 1949; S.M.O., 1956; asst. C.M.O., 1962.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1949 | M.O. | Kenya | [1957, 1958, 1959, 1960, 1961, 1962, 1963] |
| 1 | 1956 | S.M.O | Kenya *(inherited from previous clause)* | [1957, 1958, 1959, 1960, 1961, 1962, 1963] |
| 2 | 1962 | asst. C.M.O | Kenya *(inherited from previous clause)* | [1957, 1958, 1959, 1960, 1961, 1962, 1963] |

## Candidate stint `Hargreaves, A. L___Western Pacific___1961`

- Staff-list name: **Hargreaves, A. L** | colony: **Western Pacific** | listed 1961–1965 | editions [1961, 1962, 1964, 1965]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1961 | A. L. Hargreaves | Administrative Officer – Class B | Civil Establishment | — | — |
| 1962 | A. L. Hargreaves | Administrative Officer (Class B) | Civil Establishment | — | — |
| 1964 | A. L. Hargreaves | Administrative Officer | Civil Establishment | — | — |
| 1965 | A. L. Hargreaves | Administrative Officer | Civil Establishment | — | — |

### Deterministic checks: `hargreaves_a_b1913` vs `Hargreaves, A. L___Western Pacific___1961`

- [PASS] surname_gate: bio 'HARGREAVES' vs stint 'Hargreaves, A. L' (exact)
- [PASS] initials: bio ['A'] ~ stint ['A', 'L']
- [PASS] age_gate: stint starts 1961, birth 1913 (age 48)
- [FAIL] colony: no placed event resolves to 'Western Pacific'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1961-1965
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

