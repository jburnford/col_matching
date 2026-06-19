<!-- {"case_id": "case_millard_pierce-arthur_b1878", "bio_ids": ["millard_pierce-arthur_b1878"], "stint_ids": ["Millard, P. A___Cape of Good Hope___1896", "Millard, P. A___South Africa___1912"]} -->
# Dossier case_millard_pierce-arthur_b1878

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 14 official(s) with this surname in the graph's staff lists; 9 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `millard_pierce-arthur_b1878`

- Printed name: **MILLARD, PIERCE ARTHUR**
- Birth year: 1878 (attested in editions [1934])
- Appears in editions: [1934]

### Verbatim printed entry text (OCR)

**Version `col1934-L61681.v` — printed in editions [1934]:**

> MILLARD, PIERCE ARTHUR.—B. 1878; ed. at Normal Coll., Capetown; joined staff, Cape educn. dept., 1893; after serv. in various branches of dept. apptd. ch. clk., 1918 and sec., 1930.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1893 | staff | Cape Colony | [1934] |
| 1 | 1918 | ch. clk. | — | [1934] |
| 2 | 1930 | sec. | — | [1934] |

## Candidate stint `Millard, P. A___Cape of Good Hope___1896`

- Staff-list name: **Millard, P. A** | colony: **Cape of Good Hope** | listed 1896–1908 | editions [1896, 1897, 1898, 1899, 1900, 1905, 1907, 1908]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1896 | P. A. Millard | Clerk | Educational Department | — | — |
| 1897 | P. A. Millard | Clerk | Educational Department | — | — |
| 1898 | P. A. Millard | Statistician | Educational Department | — | — |
| 1899 | P. A. Millard | Statistician | Educational Department | — | — |
| 1900 | P. A. Millard | Statistician | Educational Department | — | — |
| 1905 | P. A. Millard | Statistician | Educational Department | — | — |
| 1907 | P. A. Millard | Clerk | Educational Department | — | — |
| 1908 | P. A. Millard | Clerks | Educational Department | — | — |

### Deterministic checks: `millard_pierce-arthur_b1878` vs `Millard, P. A___Cape of Good Hope___1896`

- [PASS] surname_gate: bio 'MILLARD' vs stint 'Millard, P. A' (exact)
- [PASS] initials: bio ['P', 'A'] ~ stint ['P', 'A']
- [PASS] age_gate: stint starts 1896, birth 1878 (age 18)
- [PASS] colony: 1 placed event(s) resolve to 'Cape of Good Hope'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1896-1908
- [FAIL] position_sim: best 35 vs bar 60: 'staff' ~ 'Statistician'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

## Candidate stint `Millard, P. A___South Africa___1912`

- Staff-list name: **Millard, P. A** | colony: **South Africa** | listed 1912–1918 | editions [1912, 1914, 1918]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1912 | P. A. Millard | Principal Clerk | Education Department | — | — |
| 1914 | P. A. Millard | Principal Clerk | Education Department | — | — |
| 1918 | P. A. Millard | Principal Clerk | Education Department | — | — |

### Deterministic checks: `millard_pierce-arthur_b1878` vs `Millard, P. A___South Africa___1912`

- [PASS] surname_gate: bio 'MILLARD' vs stint 'Millard, P. A' (exact)
- [PASS] initials: bio ['P', 'A'] ~ stint ['P', 'A']
- [PASS] age_gate: stint starts 1912, birth 1878 (age 34)
- [FAIL] colony: no placed event resolves to 'South Africa'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1912-1918
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

