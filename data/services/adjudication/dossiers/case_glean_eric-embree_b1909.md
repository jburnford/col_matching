<!-- {"case_id": "case_glean_eric-embree_b1909", "bio_ids": ["glean_eric-embree_b1909"], "stint_ids": ["Glean, E. E___Windward Islands___1950"]} -->
# Dossier case_glean_eric-embree_b1909

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `glean_eric-embree_b1909`

- Printed name: **GLEAN, Eric Embree**
- Birth year: 1909 (attested in editions [1950, 1951, 1953, 1954])
- Appears in editions: [1950, 1951, 1953, 1954]

### Verbatim printed entry text (OCR)

**Version `col1950-L35743.v` — printed in editions [1950, 1951, 1953, 1954]:**

> GLEAN, Eric Embree, E. & M.E.—b. 1909; ed. Grenada Boys' Sec. Sch.; asst. engrn., elec. dept., Grenada, 1941; elec. inspr., 1945; supt., elec. and tel., St. V., 1946; engrn.-in-charge, elec. and tel. dept., Grenada, 1947.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1941 | asst. engrn., elec. dept. | Grenada | [1950, 1951, 1953, 1954] |
| 1 | 1945 | elec. inspr | Grenada *(inherited from previous clause)* | [1950, 1951, 1953, 1954] |
| 2 | 1946 | supt., elec. and tel. | St. Vincent | [1950, 1951, 1953, 1954] |
| 3 | 1947 | engrn.-in-charge, elec. and tel. dept. | Grenada | [1950, 1951, 1953, 1954] |

## Candidate stint `Glean, E. E___Windward Islands___1950`

- Staff-list name: **Glean, E. E** | colony: **Windward Islands** | listed 1950–1952 | editions [1950, 1952]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1950 | E. E. Glean | Engineer in charge | Electricity, Telephone and Refrigeration | — | — |
| 1952 | E. E. Glean | Engineer in Charge, Electricity, Telephone and Refrigeration Department | Civil Establishment | — | — |

### Deterministic checks: `glean_eric-embree_b1909` vs `Glean, E. E___Windward Islands___1950`

- [PASS] surname_gate: bio 'GLEAN' vs stint 'Glean, E. E' (exact)
- [PASS] initials: bio ['E', 'E'] ~ stint ['E', 'E']
- [PASS] age_gate: stint starts 1950, birth 1909 (age 41)
- [FAIL] colony: no placed event resolves to 'Windward Islands'
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

