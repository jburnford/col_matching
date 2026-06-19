<!-- {"case_id": "case_gilbert_humphrey-raleigh_b1899", "bio_ids": ["gilbert_humphrey-raleigh_b1899"], "stint_ids": ["Gilbert, H. R. H___Kenya___1928"]} -->
# Dossier case_gilbert_humphrey-raleigh_b1899

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 33 official(s) with this surname in the graph's staff lists; 14 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `gilbert_humphrey-raleigh_b1899`

- Printed name: **GILBERT, HUMPHREY RALEIGH**
- Birth year: 1899 (attested in editions [1932, 1933, 1934, 1935, 1936, 1937, 1940])
- Appears in editions: [1932, 1933, 1934, 1935, 1936, 1937, 1940]

### Verbatim printed entry text (OCR)

**Version `col1932-L60482.v` — printed in editions [1932, 1933, 1934, 1935, 1936, 1937, 1940]:**

> GILBERT, HUMPHREY RALEIGH.—B. 1899; ent. R. Navy, 1912; served, Great War 1914-18; ret., Jan., 1923; lieut. commodr. (retd.), Feb., 1928; admin. offr., Tanganyika Territory, Jan., 1927; asst. dist. offr., Jan., 1929; ag. dist. offr., 1933; dist. offr., 1939.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1912 | ent. R. Navy | — | [1932, 1933, 1934, 1935, 1936, 1937, 1940] |
| 1 | 1914–1918 | served, Great War | — | [1932, 1933, 1934, 1935, 1936, 1937, 1940] |
| 2 | 1923 | ret | — | [1932, 1933, 1934, 1935, 1936, 1937, 1940] |
| 3 | 1927 | admin. offr., Tanganyika Territory | Tanganyika | [1932, 1933, 1934, 1935, 1936, 1937, 1940] |
| 4 | 1928 | lieut. commodr. (retd.) | — | [1932, 1933, 1934, 1935, 1936, 1937, 1940] |
| 5 | 1929 | asst. dist. offr | Tanganyika *(inherited from previous clause)* | [1932, 1933, 1934, 1935, 1936, 1937, 1940] |
| 6 | 1933 | ag. dist. offr | Tanganyika *(inherited from previous clause)* | [1932, 1933, 1934, 1935, 1936, 1937, 1940] |
| 7 | 1939 | dist. offr | Tanganyika *(inherited from previous clause)* | [1932, 1933, 1934, 1935, 1936, 1937, 1940] |

## Candidate stint `Gilbert, H. R. H___Kenya___1928`

- Staff-list name: **Gilbert, H. R. H** | colony: **Kenya** | listed 1928–1932 | editions [1928, 1929, 1930, 1931, 1932]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1928 | H. R. H. Gilbert | Foremen | Divisional Staff | — | — |
| 1929 | H. R. H. Gilbert | Overseers | Divisional Staff | — | — |
| 1930 | H. R. H. Gilbert | Overseers | Divisional Staff | — | — |
| 1931 | H. R. H. Gilbert | Overseers | Divisional Staff | — | — |
| 1932 | H. R. H. Gilbert | Overseer | Divisional Staff | — | — |

### Deterministic checks: `gilbert_humphrey-raleigh_b1899` vs `Gilbert, H. R. H___Kenya___1928`

- [PASS] surname_gate: bio 'GILBERT' vs stint 'Gilbert, H. R. H' (exact)
- [PASS] initials: bio ['H', 'R'] ~ stint ['H', 'R', 'H']
- [PASS] age_gate: stint starts 1928, birth 1899 (age 29)
- [FAIL] colony: no placed event resolves to 'Kenya'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1928-1932
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

