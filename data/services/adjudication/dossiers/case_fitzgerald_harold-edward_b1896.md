<!-- {"case_id": "case_fitzgerald_harold-edward_b1896", "bio_ids": ["fitzgerald_harold-edward_b1896"], "stint_ids": ["Fitzgerald, H. E___Uganda___1939"]} -->
# Dossier case_fitzgerald_harold-edward_b1896

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 52 official(s) with this surname in the graph's staff lists; 22 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `fitzgerald_harold-edward_b1896`

- Printed name: **FITZGERALD, Harold Edward**
- Birth year: 1896 (attested in editions [1948, 1949, 1950, 1951])
- Appears in editions: [1948, 1949, 1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1948-L32601.v` — printed in editions [1948, 1949, 1950, 1951]:**

> FITZGERALD, Harold Edward.—b. 1896; ed. Bishop Foy High Sch., Waterford and Lismore Coll., Co. Waterford, Ireland; on mil. serv., 1914-19 and 1940-43, capt.; apptd. to col. serv., Ken., 1935; trans. to Uga., 1938; senr. asst. supt. of prisons, 1946.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1935 | apptd. to col. serv. | Kenya | [1948, 1949, 1950, 1951] |
| 1 | 1938 | trans. to Uga | Kenya *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |
| 2 | 1946 | senr. asst. supt. of prisons | Kenya *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |

## Candidate stint `Fitzgerald, H. E___Uganda___1939`

- Staff-list name: **Fitzgerald, H. E** | colony: **Uganda** | listed 1939–1951 | editions [1939, 1940, 1949, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1939 | H. E. Fitzgerald | Head Gaolers | Prisons | — | Captain |
| 1940 | H. E. Fitzgerald | Head Gaolers | Prisons | — | Captain |
| 1949 | H. E. Fitzgerald | Senior Assistant Superintendents | Prisons | — | — |
| 1951 | H. E. Fitzgerald | Senior Assistant Superintendents | Prisons | — | — |

### Deterministic checks: `fitzgerald_harold-edward_b1896` vs `Fitzgerald, H. E___Uganda___1939`

- [PASS] surname_gate: bio 'FITZGERALD' vs stint 'Fitzgerald, H. E' (exact)
- [PASS] initials: bio ['H', 'E'] ~ stint ['H', 'E']
- [PASS] age_gate: stint starts 1939, birth 1896 (age 43)
- [FAIL] colony: no placed event resolves to 'Uganda'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1939-1951
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

