<!-- {"case_id": "case_rundy_fred-e_e1890", "bio_ids": ["rundy_fred-e_e1890"], "stint_ids": ["Bundy, F. E___St Lucia___1896", "Grundy, F___Kenya___1949"]} -->
# Dossier case_rundy_fred-e_e1890

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- Phase 1 found `rundy_fred-e_e1890` ↔ `Bundy, F. E___St Lucia___1896` passed its evidence bar but dropped it as ambiguous (a comparable-strength competitor existed).
- NOTE: stint `Bundy, F. E___St Lucia___1896` is also gate-compatible with biography(ies) outside this case: ['bundy_fred-e_e1890'] (already linked elsewhere or filtered).
- NOTE: stint `Grundy, F___Kenya___1949` is also gate-compatible with biography(ies) outside this case: ['grundy_frank_b1889'] (already linked elsewhere or filtered).

## Biography `rundy_fred-e_e1890`

- Printed name: **RUNDY, Fred E**
- Birth year: not printed
- Appears in editions: [1897]

### Verbatim printed entry text (OCR)

**Version `col1897-L31083.v` — printed in editions [1897]:**

> RUNDY, Fred E.—Ed. St. Mary's Coll., Hammersmith; head master, St. Mary's Coll., St. Lucia, 1890; inspr. of schools, St. Lucia, July, 1895.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1890 | head master, St. Mary's Coll. | St. Lucia | [1897] |
| 1 | 1895 | inspr. of schools | St. Lucia | [1897] |

## Candidate stint `Bundy, F. E___St Lucia___1896`

- Staff-list name: **Bundy, F. E** | colony: **St Lucia** | listed 1896–1899 | editions [1896, 1897, 1898, 1899]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1896 | F. E. Bundy | Inspector of Schools | Education Department | — | — |
| 1897 | F. E. Bundy | Inspector of Schools | Education Department | — | — |
| 1898 | F. E. Bundy | Inspector of Schools | Education Department | — | — |
| 1899 | F. E. Bundy | Inspector of Schools | Education Department | — | — |

### Deterministic checks: `rundy_fred-e_e1890` vs `Bundy, F. E___St Lucia___1896`

- [PASS] surname_gate: bio 'RUNDY' vs stint 'Bundy, F. E' (fuzzy:1)
- [PASS] initials: bio ['F', 'E'] ~ stint ['F', 'E']
- [PASS] age_gate: stint starts 1896; no printed birth year — UNCHECKED
- [PASS] colony: 2 placed event(s) resolve to 'St Lucia'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1896-1899
- [PASS] position_sim: best 89 vs bar 60: 'inspr. of schools' ~ 'Inspector of Schools'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): 1 agreeing edition-year(s) [1897] pos~89 (bar: >=2)
- [PASS] place_inherited: at least one supporting event names its place in print

## Candidate stint `Grundy, F___Kenya___1949`

- Staff-list name: **Grundy, F** | colony: **Kenya** | listed 1949–1951 | editions [1949, 1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | F. Grundy | Engineer Hydrologist | Public Works | — | — |
| 1950 | F. Grundy | Engineer Hydrologist | Public Works | — | — |
| 1951 | F. Grundy | Engineer Hydrologist | Public Works | — | — |

### Deterministic checks: `rundy_fred-e_e1890` vs `Grundy, F___Kenya___1949`

- [PASS] surname_gate: bio 'RUNDY' vs stint 'Grundy, F' (fuzzy:1)
- [PASS] initials: bio ['F', 'E'] ~ stint ['F']
- [PASS] age_gate: stint starts 1949; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Kenya'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1949-1951
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

