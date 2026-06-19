<!-- {"case_id": "case_dawson_ernest-edward_b1886", "bio_ids": ["dawson_ernest-edward_b1886"], "stint_ids": ["Dawson, E. E___Tanganyika___1922", "Dawson, E___Trinidad and Tobago___1910"]} -->
# Dossier case_dawson_ernest-edward_b1886

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 42 official(s) with this surname in the graph's staff lists; 29 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Dawson, E___Trinidad and Tobago___1910` is also gate-compatible with biography(ies) outside this case: ['dawson_john-eugene_e1878'] (already linked elsewhere or filtered).

## Biography `dawson_ernest-edward_b1886`

- Printed name: **DAWSON, ERNEST EDWARD**
- Birth year: 1886 (attested in editions [1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937, 1939])
- Appears in editions: [1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937, 1939]

### Verbatim printed entry text (OCR)

**Version `col1929-L59517.v` — printed in editions [1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937, 1939]:**

> DAWSON, ERNEST EDWARD.—B. 1886; B.A. (engg.) Cambridge with 2nd cl. hons. and exempted from the A.M.I.C.S. exam.; N.E. rly., Jan., 1909; Canadian N. rly., 1910; asst. engrnr., Tanganyika rlys., Jan., 1921; dist. engrnr., Nov., 1928.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1909 | N.E. rly | — | [1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937, 1939] |
| 1 | 1910 | Canadian N. rly | — | [1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937, 1939] |
| 2 | 1921 | asst. engrnr., Tanganyika rlys | Tanganyika | [1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937, 1939] |
| 3 | 1928 | dist. engrnr | Tanganyika *(inherited from previous clause)* | [1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937, 1939] |

## Candidate stint `Dawson, E. E___Tanganyika___1922`

- Staff-list name: **Dawson, E. E** | colony: **Tanganyika** | listed 1922–1925 | editions [1922, 1923, 1924, 1925]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1922 | E. E. Dawson | Assistant Engineers | Railways | — | — |
| 1923 | E. E. Dawson | Assistant Engineers | Railways | — | — |
| 1924 | E. E. Dawson | Assistant Engineers | Railways | — | — |
| 1925 | E. E. Dawson | Assistant Engineers | Railways | — | — |

### Deterministic checks: `dawson_ernest-edward_b1886` vs `Dawson, E. E___Tanganyika___1922`

- [PASS] surname_gate: bio 'DAWSON' vs stint 'Dawson, E. E' (exact)
- [PASS] initials: bio ['E', 'E'] ~ stint ['E', 'E']
- [PASS] age_gate: stint starts 1922, birth 1886 (age 36)
- [PASS] colony: 2 placed event(s) resolve to 'Tanganyika'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1922-1925
- [FAIL] position_sim: best 48 vs bar 60: 'asst. engrnr., Tanganyika rlys' ~ 'Assistant Engineers'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

## Candidate stint `Dawson, E___Trinidad and Tobago___1910`

- Staff-list name: **Dawson, E** | colony: **Trinidad and Tobago** | listed 1910–1912 | editions [1910, 1912]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1910 | E. Dawson | Sergeant-Instructors | Military Department | — | — |
| 1912 | E. Dawson | Serjeant-Instructors | Military Department | — | — |

### Deterministic checks: `dawson_ernest-edward_b1886` vs `Dawson, E___Trinidad and Tobago___1910`

- [PASS] surname_gate: bio 'DAWSON' vs stint 'Dawson, E' (exact)
- [PASS] initials: bio ['E', 'E'] ~ stint ['E']
- [PASS] age_gate: stint starts 1910, birth 1886 (age 24)
- [FAIL] colony: no placed event resolves to 'Trinidad and Tobago'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1910-1912
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

