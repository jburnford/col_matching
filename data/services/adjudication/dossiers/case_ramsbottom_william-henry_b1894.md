<!-- {"case_id": "case_ramsbottom_william-henry_b1894", "bio_ids": ["ramsbottom_william-henry_b1894"], "stint_ids": ["Ramsbottom, H___Kenya___1950"]} -->
# Dossier case_ramsbottom_william-henry_b1894

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `ramsbottom_william-henry_b1894`

- Printed name: **RAMSBOTTOM, WILLIAM HENRY**
- Birth year: 1894 (attested in editions [1940])
- Appears in editions: [1940]

### Verbatim printed entry text (OCR)

**Version `col1940-L67801.v` — printed in editions [1940]:**

> RAMSBOTTOM, WILLIAM HENRY.—B. 1894; ed. Grey Coll. Sch., Grey Univ. Coll., Bloemfontein and Emmanuel Coll., Cambridge; war serv., 1916-18, M.C.; called to bar, Inner Temple, 1920; practised Transvaal, 1921-39; K.C., 1935; judge, sup. cls., S. Africa, Transvaal prov. div., Sept., 1938.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1920 | called to bar, Inner Temple | — | [1940] |
| 1 | 1921–1939 | practised Transvaal | — | [1940] |
| 2 | 1935 | K.C | — | [1940] |
| 3 | 1938 | judge, sup. cls., S. Africa, Transvaal prov. div | Transvaal | [1940] |

## Candidate stint `Ramsbottom, H___Kenya___1950`

- Staff-list name: **Ramsbottom, H** | colony: **Kenya** | listed 1950–1951 | editions [1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1950 | H. Ramsbottom | Chief Draughtsman | Survey of Kenya | — | — |
| 1951 | H. Ramsbottom | Chief Draughtsman | Survey of Kenya | — | — |

### Deterministic checks: `ramsbottom_william-henry_b1894` vs `Ramsbottom, H___Kenya___1950`

- [PASS] surname_gate: bio 'RAMSBOTTOM' vs stint 'Ramsbottom, H' (exact)
- [PASS] initials: bio ['W', 'H'] ~ stint ['H']
- [PASS] age_gate: stint starts 1950, birth 1894 (age 56)
- [FAIL] colony: no placed event resolves to 'Kenya'
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

