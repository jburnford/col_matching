<!-- {"case_id": "case_fortescue_trevor-victor-norman_b1916", "bio_ids": ["fortescue_trevor-victor-norman_b1916"], "stint_ids": ["Fortescue, T. V. N___Hong Kong___1939"]} -->
# Dossier case_fortescue_trevor-victor-norman_b1916

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 5 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `fortescue_trevor-victor-norman_b1916`

- Printed name: **FORTESCUE, Trevor Victor Norman**
- Birth year: 1916 (attested in editions [1949])
- Appears in editions: [1949, 1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1949-L32097.v` — printed in editions [1949]:**

> FORTESCUE, Trevor Victor Norman.—b. 1916; cadet, H.K., 1939; asst. p.s. to gov., 1939; asst. def. sec., 1941; interned 1941-45; asst. fin. sec., 1946.

**Version `col1950-L35497.v` — printed in editions [1950, 1951]:**

> FORTESCUE, Trevor Victor Norman.—b. 1916; cadet, H.K., 1939; asst. fin. sec., 1946; seconded to U.N.O., 1947; admin. offr., Ken., 1949.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1939 | cadet | Hong Kong | [1949, 1950, 1951] |
| 1 | 1941 | asst. def. sec | Hong Kong *(inherited from previous clause)* | [1949] |
| 2 | 1946 | asst. fin. sec | Hong Kong *(inherited from previous clause)* | [1949, 1950, 1951] |
| 3 | 1947 | seconded to U.N.O | Hong Kong *(inherited from previous clause)* | [1950, 1951] |
| 4 | 1949 | admin. offr. | Kenya | [1950, 1951] |

## Candidate stint `Fortescue, T. V. N___Hong Kong___1939`

- Staff-list name: **Fortescue, T. V. N** | colony: **Hong Kong** | listed 1939–1940 | editions [1939, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1939 | T. V. N. Fortescue | — | Cadet Officers | — | — |
| 1940 | T. V. N. Fortescue | — | Cadets on Probation | — | — |

### Deterministic checks: `fortescue_trevor-victor-norman_b1916` vs `Fortescue, T. V. N___Hong Kong___1939`

- [PASS] surname_gate: bio 'FORTESCUE' vs stint 'Fortescue, T. V. N' (exact)
- [PASS] initials: bio ['T', 'V', 'N'] ~ stint ['T', 'V', 'N']
- [PASS] age_gate: stint starts 1939, birth 1916 (age 23)
- [PASS] colony: 4 placed event(s) resolve to 'Hong Kong'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1939-1940
- [FAIL] position_sim: no overlapping placed event to compare
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

