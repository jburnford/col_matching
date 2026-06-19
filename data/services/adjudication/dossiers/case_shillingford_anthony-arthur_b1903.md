<!-- {"case_id": "case_shillingford_anthony-arthur_b1903", "bio_ids": ["shillingford_anthony-arthur_b1903"], "stint_ids": ["Shillingford, A. A___Nigeria___1956"]} -->
# Dossier case_shillingford_anthony-arthur_b1903

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 12 official(s) with this surname in the graph's staff lists; 4 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `shillingford_anthony-arthur_b1903`

- Printed name: **SHILLINGFORD, Anthony Arthur**
- Birth year: 1903 (attested in editions [1948, 1949, 1950, 1951])
- Appears in editions: [1948, 1949, 1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1948-L35866.v` — printed in editions [1948, 1949, 1950, 1951]:**

> SHILLINGFORD, Anthony Arthur.—b. 1903; ed. Dulwich Coll and Worcester Coll., Oxford, B.A. (Oxon.); educ. offr., Nig., 1926.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1926 | educ. offr. | Nigeria | [1948, 1949, 1950, 1951] |

## Candidate stint `Shillingford, A. A___Nigeria___1956`

- Staff-list name: **Shillingford, A. A** | colony: **Nigeria** | listed 1956–1958 | editions [1956, 1958]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1956 | A. A. Shillingford | Director of Education | Civil Establishment | — | — |
| 1958 | A. A. Shillingford | Chief Federal Adviser on Education | Civil Establishment | C.B.E. | — |

### Deterministic checks: `shillingford_anthony-arthur_b1903` vs `Shillingford, A. A___Nigeria___1956`

- [PASS] surname_gate: bio 'SHILLINGFORD' vs stint 'Shillingford, A. A' (exact)
- [PASS] initials: bio ['A', 'A'] ~ stint ['A', 'A']
- [PASS] age_gate: stint starts 1956, birth 1903 (age 53)
- [PASS] colony: 1 placed event(s) resolve to 'Nigeria'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1956-1958
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

