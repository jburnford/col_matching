<!-- {"case_id": "case_bradshaw_arthur_b1900", "bio_ids": ["bradshaw_arthur_b1900"], "stint_ids": ["Bradshaw, H. A___Nigeria___1921"]} -->
# Dossier case_bradshaw_arthur_b1900

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 24 official(s) with this surname in the graph's staff lists; 5 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['bradshaw_arthur_b1900'] carry a single initial only — the namesake trap applies.

## Biography `bradshaw_arthur_b1900`

- Printed name: **BRADSHAW, Arthur**
- Birth year: 1900 (attested in editions [1950, 1951])
- Appears in editions: [1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1950-L33861.v` — printed in editions [1950, 1951]:**

> BRADSHAW, Arthur.—b. 1900; ed. Cent. Sch. and St. Martins Coll., Scarborough; R.N., 1915-20, 1939-40, lieut., R.N.V.R.; stn. mstr., rlwys., G.C., 1927; traffic inspr., 1935; asst. traffic supt., 1942; senr. asst., T.R. & P.S., 1945.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1915–1920 | R.N. | — | [1950, 1951] |
| 1 | 1927 | stn. mstr., rlwys. | Gold Coast | [1950, 1951] |
| 2 | 1935 | traffic inspr. | — | [1950, 1951] |
| 3 | 1939–1940 | lieut., R.N.V.R. | — | [1950, 1951] |
| 4 | 1942 | asst. traffic supt. | — | [1950, 1951] |
| 5 | 1945 | senr. asst., T.R. & P.S. | — | [1950, 1951] |

## Candidate stint `Bradshaw, H. A___Nigeria___1921`

- Staff-list name: **Bradshaw, H. A** | colony: **Nigeria** | listed 1921–1925 | editions [1921, 1922, 1925]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1921 | H. A. Bradshaw | Superintendent | Prisons, Southern Provinces | — | — |
| 1922 | H. A. Bradshaw | Superintendent | Prisons, Southern Provinces | — | — |
| 1925 | H. A. Bradshaw | Assistant Superintendent | Prisons, Southern Provinces | — | — |

### Deterministic checks: `bradshaw_arthur_b1900` vs `Bradshaw, H. A___Nigeria___1921`

- [PASS] surname_gate: bio 'BRADSHAW' vs stint 'Bradshaw, H. A' (exact)
- [PASS] initials: bio ['A'] ~ stint ['H', 'A']
- [PASS] age_gate: stint starts 1921, birth 1900 (age 21)
- [FAIL] colony: no placed event resolves to 'Nigeria'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1921-1925
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

