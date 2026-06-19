<!-- {"case_id": "case_gill_edwin-leonard_b1877", "bio_ids": ["gill_edwin-leonard_b1877"], "stint_ids": ["Gill, E___Seychelles___1905"]} -->
# Dossier case_gill_edwin-leonard_b1877

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 47 official(s) with this surname in the graph's staff lists; 21 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `gill_edwin-leonard_b1877`

- Printed name: **GILL, EDWIN LEONARD**
- Birth year: 1877 (attested in editions [1931, 1932, 1933, 1934, 1935, 1936, 1937, 1940])
- Appears in editions: [1931, 1932, 1933, 1934, 1935, 1936, 1937, 1940]

### Verbatim printed entry text (OCR)

**Version `col1931-L64722.v` — printed in editions [1931, 1932, 1933, 1934, 1935, 1936, 1937, 1940]:**

> GILL, EDWIN LEONARD, D.Sc.—B. 1877; asstt., Manchester Museum, June, 1900; curator, Hancock Museum, Newcastle-on-Tyne, July, 1901; asst. R. Scottish Museum, July, 1922; dir., S. African Museum, Cape Town, Jan., 1925.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1900 | asstt., Manchester Museum | — | [1931, 1932, 1933, 1934, 1935, 1936, 1937, 1940] |
| 1 | 1901 | curator, Hancock Museum, Newcastle-on-Tyne | — | [1931, 1932, 1933, 1934, 1935, 1936, 1937, 1940] |
| 2 | 1922 | asst. R. Scottish Museum | — | [1931, 1932, 1933, 1934, 1935, 1936, 1937, 1940] |
| 3 | 1925 | dir., S. African Museum, Cape Town | Cape of Good Hope | [1931, 1932, 1933, 1934, 1935, 1936, 1937, 1940] |

## Candidate stint `Gill, E___Seychelles___1905`

- Staff-list name: **Gill, E** | colony: **Seychelles** | listed 1905–1913 | editions [1905, 1906, 1907, 1908, 1909, 1910, 1911, 1912, 1913]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1905 | E. Gill | First Class Guards | Prison Department | — | — |
| 1906 | E. Gill | Sergeant | Police Department | — | — |
| 1907 | E. Gill | Sergeant | Police Department | — | — |
| 1908 | E. Gill | Sergeant | Police Department | — | — |
| 1909 | E. Gill | Sergeant | Police Department | — | — |
| 1910 | E. Gill | Sergeant | Police Department | — | — |
| 1911 | E. Gill | Sergeant | Police Department | — | — |
| 1912 | E. Gill | Sergeant | Police Department | — | — |
| 1913 | E. Gill | Sergeant | Police Department | — | — |

### Deterministic checks: `gill_edwin-leonard_b1877` vs `Gill, E___Seychelles___1905`

- [PASS] surname_gate: bio 'GILL' vs stint 'Gill, E' (exact)
- [PASS] initials: bio ['E', 'L'] ~ stint ['E']
- [PASS] age_gate: stint starts 1905, birth 1877 (age 28)
- [FAIL] colony: no placed event resolves to 'Seychelles'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1905-1913
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

