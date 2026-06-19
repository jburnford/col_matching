<!-- {"case_id": "case_peries_herman-eric_b1906", "bio_ids": ["peries_herman-eric_b1906"], "stint_ids": ["Peries, H. E___Ceylon___1931"]} -->
# Dossier case_peries_herman-eric_b1906

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 7 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `peries_herman-eric_b1906`

- Printed name: **PERIES, HERMAN ERIC**
- Birth year: 1906 (attested in editions [1933, 1934, 1935])
- Appears in editions: [1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937, 1939]

### Verbatim printed entry text (OCR)

**Version `col1933-L62637.v` — printed in editions [1933, 1934, 1935]:**

> PERIES, HERMAN ERIC, B.A. (Cantab), B.Sc. (Lond.).—B. 1906; cadet, Ceylon civ. serv., 1929; addt. secretariat, July, 1929; addt., Puttalam kach., Jan., 1930; ag. office astt., Kegalla kach., Jan., 1931; addt., rubber contr. office, July, 1934.

**Version `col1936-L63672.v` — printed in editions [1936, 1937]:**

> PERIES, HERMAN ERIC, B.A. (Cantab), B.Sc. (Lond.)—B. 1906; cadet, Ceylon civ. serv., 1929; astd. secretariat, July, 1929; astd., Puttalam kach., Jan., 1930; astd., rubber contr. office for sp. wk., July, 1934; office ast., Anuradhapura kach., Aug., 1934.

**Version `col1931-L67333.v` — printed in editions [1931, 1932]:**

> PERIES, HERMAN ERIC.—B. 1906; cadet, Ceylon civ. serv., 1929; astt. secretariat, July, 1929; astt., Puttalam kach., Jan., 1930; ag. pol. mag., Puttalam, May, 1930.

**Version `col1939-L69747.v` — printed in editions [1939]:**

> PERRIES, HERMAN ERIC, B.A. (Cantab), B.Sc. (Lond.).—B. 1906; cadet, Ceylon civ. serv., 1929; office astt., Anuradhapura kach., Aug., 1934; astt. sec. to min. for agr. and lands, Mar., 1936; admnr. sec., dept. of income tax, estate duty and stamps, and clk. to the bd. of review, July, 1937.

**Version `col1930-L67420.v` — printed in editions [1930]:**

> PERIES, HERMAN ERIC.—B. 1906; cadet, Ceylon civ. serv., 1929; attd. to secretariat, July, 1929.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1929 | cadet, Ceylon civ. serv | Ceylon | [1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937, 1939] |
| 1 | 1930 | addt., Puttalam kach | Ceylon *(inherited from previous clause)* | [1931, 1932, 1933, 1934, 1935, 1936, 1937] |
| 2 | 1931 | ag. office astt., Kegalla kach | Ceylon *(inherited from previous clause)* | [1933, 1934, 1935] |
| 3 | 1934 | addt., rubber contr. office | Ceylon *(inherited from previous clause)* | [1933, 1934, 1935, 1936, 1937, 1939] |
| 4 | 1936 | astt. sec. to min. for agr. and lands | Ceylon *(inherited from previous clause)* | [1939] |
| 5 | 1937 | admnr. sec., dept. of income tax, estate duty and stamps, and clk. to the bd. of review | Ceylon *(inherited from previous clause)* | [1939] |

## Candidate stint `Peries, H. E___Ceylon___1931`

- Staff-list name: **Peries, H. E** | colony: **Ceylon** | listed 1931–1936 | editions [1931, 1934, 1936]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1931 | H. E. Peries | Clerk | Civil Establishment | — | — |
| 1934 | H. E. Peries | Office Assistant | PROVINCE OF SABARAGAMUWA | — | — |
| 1936 | H. E. Peries | Office Assistant | North Central Province | — | — |

### Deterministic checks: `peries_herman-eric_b1906` vs `Peries, H. E___Ceylon___1931`

- [PASS] surname_gate: bio 'PERIES' vs stint 'Peries, H. E' (exact)
- [PASS] initials: bio ['H', 'E'] ~ stint ['H', 'E']
- [PASS] age_gate: stint starts 1931, birth 1906 (age 25)
- [PASS] colony: 6 placed event(s) resolve to 'Ceylon'
- [PASS] tenure_overlap: 6 event tenure(s) overlap stint years 1931-1936
- [FAIL] position_sim: best 55 vs bar 60: 'addt., rubber contr. office' ~ 'Office Assistant'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): 1 agreeing edition-year(s) [1934] pos~55 (bar: >=2)
- [PASS] place_inherited: at least one supporting event names its place in print

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

