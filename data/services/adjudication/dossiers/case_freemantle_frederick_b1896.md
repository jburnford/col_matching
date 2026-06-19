<!-- {"case_id": "case_freemantle_frederick_b1896", "bio_ids": ["freemantle_frederick_b1896"], "stint_ids": ["Freemantle, F___British Guiana___1929"]} -->
# Dossier case_freemantle_frederick_b1896

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['freemantle_frederick_b1896'] carry a single initial only — the namesake trap applies.

## Biography `freemantle_frederick_b1896`

- Printed name: **FREEMANTLE, Frederick**
- Birth year: 1896 (attested in editions [1948])
- Appears in editions: [1948]

### Verbatim printed entry text (OCR)

**Version `col1948-L32704.v` — printed in editions [1948]:**

> FREEMANTLE, Frederick.—b. 1896; ed. Swanmore; on mil. serv. 1914–19; line foreman, govt. elec. dept., Br. Guiana; line inspr., 1924; senr. tel. inspr., P.O. engnrng. dept., 1927; tel. inspr., posts and tels. dept., Pal., 1934; asst. engnr., 1943.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1924 | line inspr | — | [1948] |
| 1 | 1927 | senr. tel. inspr., P.O. engnrng. dept | — | [1948] |
| 2 | 1934 | tel. inspr., posts and tels. dept. | Palestine | [1948] |
| 3 | 1943 | asst. engnr | Palestine *(inherited from previous clause)* | [1948] |

## Candidate stint `Freemantle, F___British Guiana___1929`

- Staff-list name: **Freemantle, F** | colony: **British Guiana** | listed 1929–1930 | editions [1929, 1930]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1929 | F. Freemantle | Telephone Inspector | Post Office, Engineering Branch | — | — |
| 1930 | F. Freemantle | Telephone Inspector | Engineering Branch | — | — |

### Deterministic checks: `freemantle_frederick_b1896` vs `Freemantle, F___British Guiana___1929`

- [PASS] surname_gate: bio 'FREEMANTLE' vs stint 'Freemantle, F' (exact)
- [PASS] initials: bio ['F'] ~ stint ['F']
- [PASS] age_gate: stint starts 1929, birth 1896 (age 33)
- [FAIL] colony: no placed event resolves to 'British Guiana'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1929-1930
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

