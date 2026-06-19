<!-- {"case_id": "case_holden_a_b1916", "bio_ids": ["holden_a_b1916"], "stint_ids": ["Holden, A___Kenya___1939"]} -->
# Dossier case_holden_a_b1916

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 11 official(s) with this surname in the graph's staff lists; 5 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['holden_a_b1916'] carry a single initial only — the namesake trap applies.

## Biography `holden_a_b1916`

- Printed name: **HOLDEN, A**
- Birth year: 1916 (attested in editions [1957])
- Appears in editions: [1957]

### Verbatim printed entry text (OCR)

**Version `col1957-L24135.v` — printed in editions [1957]:**

> HOLDEN, A.—b. 1916; ed. Lawrence Sheriff Sch., Rugby, and St. Edmund Hall, Oxford; Nig. police, 1939; admin. offr., 1942; cl. II, 1953; cl. I, 1954.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1939 | Nig. police | Nigeria | [1957] |
| 1 | 1942 | admin. offr | Nigeria *(inherited from previous clause)* | [1957] |
| 2 | 1953 | cl. II | Nigeria *(inherited from previous clause)* | [1957] |
| 3 | 1954 | cl. I | Nigeria *(inherited from previous clause)* | [1957] |

## Candidate stint `Holden, A___Kenya___1939`

- Staff-list name: **Holden, A** | colony: **Kenya** | listed 1939–1940 | editions [1939, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1939 | A. Holden | Assessors | Inland Revenue | — | — |
| 1940 | A. Holden | Assessors | Inland Revenue | — | — |

### Deterministic checks: `holden_a_b1916` vs `Holden, A___Kenya___1939`

- [PASS] surname_gate: bio 'HOLDEN' vs stint 'Holden, A' (exact)
- [PASS] initials: bio ['A'] ~ stint ['A']
- [PASS] age_gate: stint starts 1939, birth 1916 (age 23)
- [FAIL] colony: no placed event resolves to 'Kenya'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1939-1940
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

