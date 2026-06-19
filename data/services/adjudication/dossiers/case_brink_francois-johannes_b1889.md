<!-- {"case_id": "case_brink_francois-johannes_b1889", "bio_ids": ["brink_francois-johannes_b1889"], "stint_ids": ["Brink, F. J___Cape of Good Hope___1905"]} -->
# Dossier case_brink_francois-johannes_b1889

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 10 official(s) with this surname in the graph's staff lists; 6 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `brink_francois-johannes_b1889`

- Printed name: **BRINK, FRANCOIS JOHANNES**
- Birth year: 1889 (attested in editions [1939, 1940])
- Appears in editions: [1939, 1940]

### Verbatim printed entry text (OCR)

**Version `col1939-L65235.v` — printed in editions [1939, 1940]:**

> BRINK, FRANCOIS JOHANNES.—B. 1889; ed. Riebeek West Pub. Schol. and S.A. Coll., Cape Town; war serv., 1914-16; Union of S. Africa pub. serv. as asst. inspr., mines, Brakpan, 1925; dep. inspr., mines, Germiston, 1929; inspr., mines and mining commr., Bloemfontein, 1934; inspr., mines, Transvaal, 1935.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1925 | Union of S. Africa pub. serv. as asst. inspr., mines, Brakpan | — | [1939, 1940] |
| 1 | 1929 | dep. inspr., mines, Germiston | — | [1939, 1940] |
| 2 | 1934 | inspr., mines and mining commr., Bloemfontein | — | [1939, 1940] |
| 3 | 1935 | inspr., mines | Transvaal | [1939, 1940] |

## Candidate stint `Brink, F. J___Cape of Good Hope___1905`

- Staff-list name: **Brink, F. J** | colony: **Cape of Good Hope** | listed 1905–1909 | editions [1905, 1907, 1909]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1905 | F. J. Brink | Clerk | Chief Inspector's Office | — | — |
| 1907 | F. J. Brink | Clerk | Record Section | — | — |
| 1909 | F. J. Brink | Record Clerk | Record Section | — | — |

### Deterministic checks: `brink_francois-johannes_b1889` vs `Brink, F. J___Cape of Good Hope___1905`

- [PASS] surname_gate: bio 'BRINK' vs stint 'Brink, F. J' (exact)
- [PASS] initials: bio ['F', 'J'] ~ stint ['F', 'J']
- [PASS] age_gate: stint starts 1905, birth 1889 (age 16)
- [FAIL] colony: no placed event resolves to 'Cape of Good Hope'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1905-1909
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

