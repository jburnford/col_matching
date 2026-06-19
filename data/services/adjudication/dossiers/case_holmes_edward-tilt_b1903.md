<!-- {"case_id": "case_holmes_edward-tilt_b1903", "bio_ids": ["holmes_edward-tilt_b1903"], "stint_ids": ["Holmes, E. T___Nigeria___1934"]} -->
# Dossier case_holmes_edward-tilt_b1903

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 49 official(s) with this surname in the graph's staff lists; 24 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `holmes_edward-tilt_b1903`

- Printed name: **HOLMES, Edward Tilt**
- Birth year: 1903 (attested in editions [1948, 1949, 1950, 1951])
- Appears in editions: [1948, 1949, 1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1948-L33413.v` — printed in editions [1948, 1949, 1950, 1951]:**

> HOLMES, Edward Tilt.—b. 1903; ed. Westminster Sch. and Reading Univ., dip. of agric., Reading Univ.; apptd. Nig., 1926; senr. agric. offr., S.L., 1940; Nig., 1944.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1926 | apptd. Nig | — | [1948, 1949, 1950, 1951] |
| 1 | 1940 | senr. agric. offr. | Sierra Leone | [1948, 1949, 1950, 1951] |
| 2 | 1944 | senr. agric. offr. | Nigeria | [1948, 1949, 1950, 1951] |

## Candidate stint `Holmes, E. T___Nigeria___1934`

- Staff-list name: **Holmes, E. T** | colony: **Nigeria** | listed 1934–1939 | editions [1934, 1939]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1934 | E. T. Holmes | Superintendents | Agriculture | — | — |
| 1939 | E. T. Holmes | Senior Agricultural Officers | Agriculture | — | — |

### Deterministic checks: `holmes_edward-tilt_b1903` vs `Holmes, E. T___Nigeria___1934`

- [PASS] surname_gate: bio 'HOLMES' vs stint 'Holmes, E. T' (exact)
- [PASS] initials: bio ['E', 'T'] ~ stint ['E', 'T']
- [PASS] age_gate: stint starts 1934, birth 1903 (age 31)
- [PASS] colony: 1 placed event(s) resolve to 'Nigeria'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1934-1939
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

