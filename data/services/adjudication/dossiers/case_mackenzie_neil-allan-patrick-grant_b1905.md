<!-- {"case_id": "case_mackenzie_neil-allan-patrick-grant_b1905", "bio_ids": ["mackenzie_neil-allan-patrick-grant_b1905"], "stint_ids": ["MacKenzie, G___Uganda___1927"]} -->
# Dossier case_mackenzie_neil-allan-patrick-grant_b1905

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 52 official(s) with this surname in the graph's staff lists; 23 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `MacKenzie, G___Uganda___1927` is also gate-compatible with biography(ies) outside this case: ['mackenzie_john-gurney_b1907'] (already linked elsewhere or filtered).

## Biography `mackenzie_neil-allan-patrick-grant_b1905`

- Printed name: **MACKENZIE, Neil Allan Patrick Grant**
- Birth year: 1905 (attested in editions [1957, 1958, 1959, 1960, 1961])
- Appears in editions: [1949, 1950, 1951, 1957, 1958, 1959, 1960, 1961]

### Verbatim printed entry text (OCR)

**Version `col1957-L25342.v` — printed in editions [1957, 1958, 1959, 1960, 1961]:**

> MACKENZIE, N. A. P. G.—b. 1905; ed. Dollar Academy and Edin. Univ.; mil. serv., 1939, 1940-43, lieut.; admin. offr., Nig., 1928; E. Nig., cl. II, 1957-60.

**Version `col1949-L33999.v` — printed in editions [1949]:**

> McKENZIE, Neil Allan Patrick Grant, lower standard Ibo.—b. 1905; ed. Dollar Acad. and Edin. Univ. (engnr course); on mil. serv. 1940-43, lieut.; apptd. admin. serv., Nig., 1928.

**Version `col1950-L37660.v` — printed in editions [1950, 1951]:**

> MACKENZIE, Neil Allan Patrick Grant, lower standard Ibo.—b. 1905; ed. Dollar Acad. and Edin. Univ. (engng course); on mil. serv. 1940-43, lieut.; apptd. admin. serv., Nig., 1928.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1928 | admin. offr. | Nigeria | [1949, 1950, 1951, 1957, 1958, 1959, 1960, 1961] |
| 1 | 1957–1960 | E. Nig., cl. II | Nigeria *(inherited from previous clause)* | [1957, 1958, 1959, 1960, 1961] |

## Candidate stint `MacKenzie, G___Uganda___1927`

- Staff-list name: **MacKenzie, G** | colony: **Uganda** | listed 1927–1928 | editions [1927, 1928]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1927 | G. MacKenzie | Superintendent of Conservancy and Sanitary Inspector | Municipal | — | — |
| 1928 | G. MacKenzie | Superintendent of Conservancy and Sanitary Inspector | Municipal | — | — |

### Deterministic checks: `mackenzie_neil-allan-patrick-grant_b1905` vs `MacKenzie, G___Uganda___1927`

- [PASS] surname_gate: bio 'MACKENZIE' vs stint 'MacKenzie, G' (exact)
- [PASS] initials: bio ['N', 'A', 'P', 'G'] ~ stint ['G']
- [PASS] age_gate: stint starts 1927, birth 1905 (age 22)
- [FAIL] colony: no placed event resolves to 'Uganda'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1927-1928
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

