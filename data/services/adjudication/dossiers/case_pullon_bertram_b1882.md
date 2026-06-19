<!-- {"case_id": "case_pullon_bertram_b1882", "bio_ids": ["pullon_bertram_b1882"], "stint_ids": ["Pullon, B___Northern Rhodesia___1929"]} -->
# Dossier case_pullon_bertram_b1882

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['pullon_bertram_b1882'] carry a single initial only — the namesake trap applies.

## Biography `pullon_bertram_b1882`

- Printed name: **PULLON, BERTRAM**
- Birth year: 1882 (attested in editions [1934, 1935, 1936, 1939, 1940])
- Appears in editions: [1934, 1935, 1936, 1939, 1940]

### Verbatim printed entry text (OCR)

**Version `col1934-L62449.v` — printed in editions [1934, 1935, 1936, 1939, 1940]:**

> PULLON, BERTRAM.—B. 1882; asst. printer, N. Rhodesia, 1921; ag. gov't. printer, 1924-25; asst. gov't. printer, 1925; ag. gov't. printer for various periods during 1927-29, 1931 and 1932; gov't. printer, 1932.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1921 | asst. printer | Northern Rhodesia | [1934, 1935, 1936, 1939, 1940] |
| 1 | 1924–1925 | ag. gov't. printer | — | [1934, 1935, 1936, 1939, 1940] |
| 2 | 1925 | asst. gov't. printer | — | [1934, 1935, 1936, 1939, 1940] |
| 3 | 1927–1932 | ag. gov't. printer | — | [1934, 1935, 1936, 1939, 1940] |
| 4 | 1932 | gov't. printer | — | [1934, 1935, 1936, 1939, 1940] |

## Candidate stint `Pullon, B___Northern Rhodesia___1929`

- Staff-list name: **Pullon, B** | colony: **Northern Rhodesia** | listed 1929–1940 | editions [1929, 1930, 1931, 1933, 1934, 1936, 1937, 1939, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1929 | B. Pullon | Assistant Government Printer | Printing and Stationery | — | — |
| 1930 | B. Pullon | Assistant Government Printer | Printing and Stationery | — | — |
| 1931 | B. Pullon | Assistant Government Printer | Printing and Stationery | — | — |
| 1933 | B. Pullon | Government Printer | Printing and Stationery | — | — |
| 1934 | B. Pullon | Government Printer | Printing and Stationery | — | — |
| 1936 | B. Pullon | Government Printer | Printing and Stationery | — | — |
| 1937 | B. Pullon | Government Printer | Printing and Stationery | — | — |
| 1939 | B. Pullon | Government Printer | Printing and Stationery | — | — |
| 1940 | B. Pullon | Government Printer | Printing and Stationery | — | — |

### Deterministic checks: `pullon_bertram_b1882` vs `Pullon, B___Northern Rhodesia___1929`

- [PASS] surname_gate: bio 'PULLON' vs stint 'Pullon, B' (exact)
- [PASS] initials: bio ['B'] ~ stint ['B']
- [PASS] age_gate: stint starts 1929, birth 1882 (age 47)
- [PASS] colony: 1 placed event(s) resolve to 'Northern Rhodesia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1929-1940
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): 1 agreeing edition-year(s) [1934] pos~74 (bar: >=2)
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

