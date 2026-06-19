<!-- {"case_id": "case_cammell_bernard_b1898", "bio_ids": ["cammell_bernard_b1898"], "stint_ids": ["Cammell, V. B___Nyasaland___1932"]} -->
# Dossier case_cammell_bernard_b1898

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['cammell_bernard_b1898'] carry a single initial only — the namesake trap applies.

## Biography `cammell_bernard_b1898`

- Printed name: **CAMMELL, BERNARD**
- Birth year: 1898 (attested in editions [1939])
- Appears in editions: [1939]

### Verbatim printed entry text (OCR)

**Version `col1939-L65476.v` — printed in editions [1939]:**

> CAMMELL, MR. BERNARD.—B. 1898; ed. Malvern Coll. and Royal Milly Acad., Woolwich, 1915; R. Arty., 1915-21; active serv. (France), 1916-18; asst. dist. comsnr., Nyassaland Prot., 1927-30; asst. treas., 1930-36; seconded, Somaliland Prot., 1936.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1915–1921 | R. Arty | — | [1939] |
| 1 | 1927–1930 | asst. dist. comsnr., Nyassaland Prot | — | [1939] |
| 2 | 1930–1936 | asst. treas | — | [1939] |
| 3 | 1936 | seconded | Somaliland | [1939] |

## Candidate stint `Cammell, V. B___Nyasaland___1932`

- Staff-list name: **Cammell, V. B** | colony: **Nyasaland** | listed 1932–1936 | editions [1932, 1934, 1936]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1932 | V. B. Cammell | Assistant Treasurer | Treasury | — | — |
| 1934 | V. B. Cammell | Assistant Treasurer | Treasury | — | — |
| 1936 | V. B. Cammell | Assistant Treasurer | Treasury | — | — |

### Deterministic checks: `cammell_bernard_b1898` vs `Cammell, V. B___Nyasaland___1932`

- [PASS] surname_gate: bio 'CAMMELL' vs stint 'Cammell, V. B' (exact)
- [PASS] initials: bio ['B'] ~ stint ['V', 'B']
- [PASS] age_gate: stint starts 1932, birth 1898 (age 34)
- [FAIL] colony: no placed event resolves to 'Nyasaland'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1932-1936
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

