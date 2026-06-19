<!-- {"case_id": "case_burt_norman-frank_b1899", "bio_ids": ["burt_norman-frank_b1899"], "stint_ids": ["Burt, N. F___Tanganyika___1923"]} -->
# Dossier case_burt_norman-frank_b1899

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 18 official(s) with this surname in the graph's staff lists; 10 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `burt_norman-frank_b1899`

- Printed name: **BURT, NORMAN FRANK**
- Birth year: 1899 (attested in editions [1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1940])
- Appears in editions: [1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1940]

### Verbatim printed entry text (OCR)

**Version `col1928-L64633.v` — printed in editions [1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1940]:**

> BURT, NORMAN FRANK.—B. 1899; ed. Rugby Schl.; R. Mily. Academy, Woolwich and Jesus Coll., Cambridge; staff survr., Tanganyika Territory, Aug., 1922; cadet, Tanganyika, Sept., 1925; asst. dist. offr., Sept., 1926; dist. offr., Sept., 1936.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1922 | staff survr., Tanganyika Territory | Tanganyika | [1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1940] |
| 1 | 1925 | cadet | Tanganyika | [1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1940] |
| 2 | 1926 | asst. dist. offr | Tanganyika *(inherited from previous clause)* | [1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1940] |
| 3 | 1936 | dist. offr | Tanganyika *(inherited from previous clause)* | [1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1940] |

## Candidate stint `Burt, N. F___Tanganyika___1923`

- Staff-list name: **Burt, N. F** | colony: **Tanganyika** | listed 1923–1925 | editions [1923, 1924, 1925]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1923 | N. F. Burt | Junior Staff Surveyors | Land, Survey and Mines Department | — | — |
| 1924 | N. F. Burt | Junior Staff Surveyors | Land, Survey and Mines Department | — | — |
| 1925 | N. F. Burt | Junior Staff Surveyors | Land, Survey and Mines Department | — | — |

### Deterministic checks: `burt_norman-frank_b1899` vs `Burt, N. F___Tanganyika___1923`

- [PASS] surname_gate: bio 'BURT' vs stint 'Burt, N. F' (exact)
- [PASS] initials: bio ['N', 'F'] ~ stint ['N', 'F']
- [PASS] age_gate: stint starts 1923, birth 1899 (age 24)
- [PASS] colony: 4 placed event(s) resolve to 'Tanganyika'
- [PASS] tenure_overlap: 3 event tenure(s) overlap stint years 1923-1925
- [FAIL] position_sim: best 48 vs bar 60: 'staff survr., Tanganyika Territory' ~ 'Junior Staff Surveyors'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
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

