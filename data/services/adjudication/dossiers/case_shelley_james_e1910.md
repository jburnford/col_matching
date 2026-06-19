<!-- {"case_id": "case_shelley_james_e1910", "bio_ids": ["shelley_james_e1910"], "stint_ids": ["Shelley, W. J___Ceylon___1928"]} -->
# Dossier case_shelley_james_e1910

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 7 official(s) with this surname in the graph's staff lists; 4 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['shelley_james_e1910'] carry a single initial only — the namesake trap applies.

## Biography `shelley_james_e1910`

- Printed name: **SHELLEY, JAMES**
- Birth year: not printed
- Appears in editions: [1939]

### Verbatim printed entry text (OCR)

**Version `col1939-L70564.v` — printed in editions [1939]:**

> SHELLEY, JAMES, M.A. Camb., Dipl. in Educn., Camb.—Ed. Bablake schl., Coventry and Christ's Coll., Camb.; lect. in educn., Manchester Univ., 1910-14; prof. of educn., Southampton Univ. Coll., 1914-20; prof. of educn., Canterbury Univ. Coll., N.Z., 1920-36; dir., broadcasting, nat. broadcasting serv., N.Z., 1936; served R.F.A., hon. rank major, 1916-20; prof., emeritus, Canterbury Univ. Coll., N.Z., 1937.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1910–1914 | lect. in educn., Manchester Univ | — | [1939] |
| 1 | 1914–1920 | prof. of educn., Southampton Univ. Coll | — | [1939] |
| 2 | 1916–1920 | served R.F.A., hon. rank major | New Zealand *(inherited from previous clause)* | [1939] |
| 3 | 1920–1936 | prof. of educn., Canterbury Univ. Coll. | New Zealand | [1939] |
| 4 | 1936 | dir., broadcasting, nat. broadcasting serv. | New Zealand | [1939] |
| 5 | 1937 | prof., emeritus, Canterbury Univ. Coll. | New Zealand | [1939] |

## Candidate stint `Shelley, W. J___Ceylon___1928`

- Staff-list name: **Shelley, W. J** | colony: **Ceylon** | listed 1928–1929 | editions [1928, 1929]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1928 | W. J. Shelley | Chief Assistant Construction Engineer | Railway Department | — | — |
| 1929 | W. J. Shelley | Chief Assistant Construction Engineer | Railway Department | — | — |

### Deterministic checks: `shelley_james_e1910` vs `Shelley, W. J___Ceylon___1928`

- [PASS] surname_gate: bio 'SHELLEY' vs stint 'Shelley, W. J' (exact)
- [PASS] initials: bio ['J'] ~ stint ['W', 'J']
- [PASS] age_gate: stint starts 1928; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Ceylon'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1928-1929
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

