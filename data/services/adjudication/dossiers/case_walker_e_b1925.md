<!-- {"case_id": "case_walker_e_b1925", "bio_ids": ["walker_e_b1925"], "stint_ids": ["Walker, R. E___Gold Coast___1950"]} -->
# Dossier case_walker_e_b1925

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 124 official(s) with this surname in the graph's staff lists; 70 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['walker_e_b1925'] carry a single initial only — the namesake trap applies.
- NOTE: stint `Walker, R. E___Gold Coast___1950` is also gate-compatible with biography(ies) outside this case: ['walker_r-e_b1906', 'walker_richard_e1923', 'walker_robert_b1881'] (already linked elsewhere or filtered).

## Biography `walker_e_b1925`

- Printed name: **WALKER, E**
- Birth year: 1925 (attested in editions [1963, 1964, 1965, 1966])
- Appears in editions: [1963, 1964, 1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1963-L25962.v` — printed in editions [1963, 1964, 1965, 1966]:**

> WALKER, E.—b. 1925; ed. Barnard Castle Sch., and Durham Univ.; mil. serv., 1944-49; survr., Fiji, 1951; staff survr., 1954.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1951 | survr. | Fiji | [1963, 1964, 1965, 1966] |
| 1 | 1954 | staff survr | Fiji *(inherited from previous clause)* | [1963, 1964, 1965, 1966] |

## Candidate stint `Walker, R. E___Gold Coast___1950`

- Staff-list name: **Walker, R. E** | colony: **Gold Coast** | listed 1950–1956 | editions [1950, 1951, 1956]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1950 | R. E. Walker | Commissioner for Cocoa Rehabilitation | Cocoa Rehabilitation | — | — |
| 1951 | R. E. Walker | Commissioner for Cocoa Rehabilitation | Cocoa Rehabilitation | — | — |
| 1956 | R. E. Walker | Regional Officer | Civil Establishment | — | — |

### Deterministic checks: `walker_e_b1925` vs `Walker, R. E___Gold Coast___1950`

- [PASS] surname_gate: bio 'WALKER' vs stint 'Walker, R. E' (exact)
- [PASS] initials: bio ['E'] ~ stint ['R', 'E']
- [PASS] age_gate: stint starts 1950, birth 1925 (age 25)
- [FAIL] colony: no placed event resolves to 'Gold Coast'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1950-1956
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

