<!-- {"case_id": "case_fenton_walter-raymond_b1900", "bio_ids": ["fenton_walter-raymond_b1900"], "stint_ids": ["Fenton, W. R___Kenya___1950"]} -->
# Dossier case_fenton_walter-raymond_b1900

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 20 official(s) with this surname in the graph's staff lists; 4 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `fenton_walter-raymond_b1900`

- Printed name: **FENTON, Walter Raymond**
- Birth year: 1900 (attested in editions [1950, 1951])
- Appears in editions: [1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1950-L35373.v` — printed in editions [1950, 1951]:**

> FENTON, Walter Raymond.—b. 1900; ed. Royal Naval Colls., Osborne and Dartmouth; midn., R.N., 1917, to lieut., R.N. (retd.), 1923; on war serv., 1939-45, comdr., R.N. (retd.); ch. offr., prisons serv., Ken., 1938; asst. supt., prisons, gr. II, 1945; gr. I, 1947.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1917–1923 | midn., R.N., to lieut., R.N. (retd.) | — | [1950, 1951] |
| 1 | 1938 | ch. offr., prisons serv. | Kenya | [1950, 1951] |
| 2 | 1939–1945 | on war serv., comdr., R.N. (retd.) | — | [1950, 1951] |
| 3 | 1945 | asst. supt., prisons, gr. II | — | [1950, 1951] |
| 4 | 1947 | gr. I | — | [1950, 1951] |

## Candidate stint `Fenton, W. R___Kenya___1950`

- Staff-list name: **Fenton, W. R** | colony: **Kenya** | listed 1950–1951 | editions [1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1950 | W. R. Fenton | Superintendents and Assistant Superintendents, Grade I | PRISONS | — | — |
| 1951 | W. R. Fenton | Superintendents and Assistant Superintendents, Grade I | PRISONS | — | — |

### Deterministic checks: `fenton_walter-raymond_b1900` vs `Fenton, W. R___Kenya___1950`

- [PASS] surname_gate: bio 'FENTON' vs stint 'Fenton, W. R' (exact)
- [PASS] initials: bio ['W', 'R'] ~ stint ['W', 'R']
- [PASS] age_gate: stint starts 1950, birth 1900 (age 50)
- [PASS] colony: 1 placed event(s) resolve to 'Kenya'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1950-1951
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

