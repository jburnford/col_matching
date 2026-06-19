<!-- {"case_id": "case_chopping_john-campbell_b1903", "bio_ids": ["chopping_john-campbell_b1903"], "stint_ids": ["Coppini, C___Malta___1929"]} -->
# Dossier case_chopping_john-campbell_b1903

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `chopping_john-campbell_b1903`

- Printed name: **CHOPPING, John Campbell**
- Birth year: 1903 (attested in editions [1948, 1949, 1950, 1951])
- Appears in editions: [1948, 1949, 1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1948-L31759.v` — printed in editions [1948, 1949, 1950, 1951]:**

> CHOPPING, John Campbell.—b. 1903; ed. Northgate Sch., Ipswich; apptd. elec. dept., Nig., 1929; elec. engrnr., 1946.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1929 | apptd. elec. dept. | Nigeria | [1948, 1949, 1950, 1951] |
| 1 | 1946 | elec. engrnr | Nigeria *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |

## Candidate stint `Coppini, C___Malta___1929`

- Staff-list name: **Coppini, C** | colony: **Malta** | listed 1929–1931 | editions [1929, 1930, 1931]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1929 | C. Coppini | Postal Clerks, 1st Class | Post Office | — | — |
| 1930 | C. Coppini | Postal Clerks, 1st Class | Post Office | — | — |
| 1931 | C. Coppini | Postal Clerks, 1st Class | Post Office | — | — |

### Deterministic checks: `chopping_john-campbell_b1903` vs `Coppini, C___Malta___1929`

- [PASS] surname_gate: bio 'CHOPPING' vs stint 'Coppini, C' (fuzzy:2)
- [PASS] initials: bio ['J', 'C'] ~ stint ['C']
- [PASS] age_gate: stint starts 1929, birth 1903 (age 26)
- [FAIL] colony: no placed event resolves to 'Malta'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1929-1931
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

