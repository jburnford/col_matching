<!-- {"case_id": "case_gleddhill_eric-irvine_b1908", "bio_ids": ["gleddhill_eric-irvine_b1908"], "stint_ids": ["Gledhill, E. I___Kenya___1937"]} -->
# Dossier case_gleddhill_eric-irvine_b1908

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 4 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `gleddhill_eric-irvine_b1908`

- Printed name: **GLEDDHILL, Eric Irvine**
- Birth year: 1908 (attested in editions [1948])
- Appears in editions: [1948]

### Verbatim printed entry text (OCR)

**Version `col1948-L32864.v` — printed in editions [1948]:**

> GLEDDHILL, Eric Irvine.—b. 1908; ed. King's Sch., Pontefract, Leeds Univ., B.Com. (hons.), dip. in educ.; bd. of educ. cert.; on mil. serv. 1939-43, maj.; educ. offr., Ken., 1932.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1932 | educ. offr. | Kenya | [1948] |
| 1 | 1939–1943 | maj. | — | [1948] |

## Candidate stint `Gledhill, E. I___Kenya___1937`

- Staff-list name: **Gledhill, E. I** | colony: **Kenya** | listed 1937–1940 | editions [1937, 1939, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1937 | E. I. Gledhill | Education Officer—European Education | Education | — | — |
| 1939 | E. I. Gledhill | Education Officer, European Education | Education | — | — |
| 1940 | E. I. Gledhill | Education Officers—European Education | Education | — | — |

### Deterministic checks: `gleddhill_eric-irvine_b1908` vs `Gledhill, E. I___Kenya___1937`

- [PASS] surname_gate: bio 'GLEDDHILL' vs stint 'Gledhill, E. I' (fuzzy:1)
- [PASS] initials: bio ['E', 'I'] ~ stint ['E', 'I']
- [PASS] age_gate: stint starts 1937, birth 1908 (age 29)
- [PASS] colony: 1 placed event(s) resolve to 'Kenya'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1937-1940
- [FAIL] position_sim: best 53 vs bar 60: 'educ. offr.' ~ 'Education Officer—European Education'
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

