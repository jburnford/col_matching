<!-- {"case_id": "case_lindsay_k-g_e1921", "bio_ids": ["lindsay_k-g_e1921", "lindsay_k-g_e1921-2"], "stint_ids": ["Lindsay, K. G___Kenya___1940"]} -->
# Dossier case_lindsay_k-g_e1921

## Case context

- 2 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 13 official(s) with this surname in the graph's staff lists; 6 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- CONTESTED: stint(s) ['Lindsay, K. G___Kenya___1940'] have more than one claimant biography in this case.
- NOTE: stint `Lindsay, K. G___Kenya___1940` is also gate-compatible with biography(ies) outside this case: ['lindsay_kenneth-gordon_b1899'] (already linked elsewhere or filtered).
- NOTE: stint `Lindsay, K. G___Kenya___1940` is also gate-compatible with biography(ies) outside this case: ['lindsay_kenneth-gordon_b1899'] (already linked elsewhere or filtered).

## Biography `lindsay_k-g_e1921`

- Printed name: **LINDSAY, K. G**
- Birth year: not printed
- Appears in editions: [1924, 1925, 1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937]

### Verbatim printed entry text (OCR)

**Version `col1924-L55964.v` — printed in editions [1924, 1925, 1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937]:**

> LINDSAY, K. G.—Astt. dist. comsnr., Kenya, June, 1921.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1921 | Astt. dist. comsnr. | Kenya | [1924, 1925, 1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937] |

## Biography `lindsay_k-g_e1921-2`

- Printed name: **LINDSAY, K. G**
- Birth year: not printed
- Appears in editions: [1939, 1940]

### Verbatim printed entry text (OCR)

**Version `col1939-L68660.v` — printed in editions [1939, 1940]:**

> LINDSAY, K. G.—Asst. dist. commnr., Kenya, June, 1921; dist. offr., Kenya, 1923; junr. sec., native affrs., 1927.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1921 | Asst. dist. commnr. | Kenya | [1939, 1940] |
| 1 | 1923 | dist. offr. | Kenya | [1939, 1940] |
| 2 | 1927 | junr. sec., native affrs | Kenya *(inherited from previous clause)* | [1939, 1940] |

## Candidate stint `Lindsay, K. G___Kenya___1940`

- Staff-list name: **Lindsay, K. G** | colony: **Kenya** | listed 1940–1946 | editions [1940, 1946]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1940 | K. G. Lindsay | District Officers | Provincial Administration | — | — |
| 1946 | K. G. Lindsay | Deputy Chief Secretary (Acting) | Nominated Official Members | O.B.E. | — |

### Deterministic checks: `lindsay_k-g_e1921` vs `Lindsay, K. G___Kenya___1940`

- [PASS] surname_gate: bio 'LINDSAY' vs stint 'Lindsay, K. G' (exact)
- [PASS] initials: bio ['K', 'G'] ~ stint ['K', 'G']
- [PASS] age_gate: stint starts 1940; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Kenya'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1940-1946
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

### Deterministic checks: `lindsay_k-g_e1921-2` vs `Lindsay, K. G___Kenya___1940`

- [PASS] surname_gate: bio 'LINDSAY' vs stint 'Lindsay, K. G' (exact)
- [PASS] initials: bio ['K', 'G'] ~ stint ['K', 'G']
- [PASS] age_gate: stint starts 1940; no printed birth year — UNCHECKED
- [PASS] colony: 3 placed event(s) resolve to 'Kenya'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1940-1946
- [FAIL] position_sim: best 36 vs bar 60: 'junr. sec., native affrs' ~ 'Deputy Chief Secretary (Acting)'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: ALL supporting events inherit their place from an earlier clause — weak evidence

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

