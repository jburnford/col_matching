<!-- {"case_id": "case_halliday_l-g_b1883", "bio_ids": ["halliday_l-g_b1883"], "stint_ids": ["Halliday, L. G___Tanganyika___1922"]} -->
# Dossier case_halliday_l-g_b1883

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `halliday_l-g_b1883`

- Printed name: **HALLIDAY, L. G**
- Birth year: 1883 (attested in editions [1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936])
- Appears in editions: [1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936]

### Verbatim printed entry text (OCR)

**Version `col1929-L60813.v` — printed in editions [1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936]:**

> HALLIDAY, L. G.—B. 1883; ed. Holt Schol. and Liverpool Univ.; mily. serv., Mesopotamia, 1916-1920; ch. engrnr., "Lord Milner," Tanganyika Territory, Apr., 1924; in charge, reconditioning "Liamba," Dec., 1925; ch. engrnr., "Liamba," 1927.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1916–1920 | mily. serv. | Mesopotamia | [1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936] |
| 1 | 1924 | ch. engrnr., "Lord Milner," Tanganyika Territory | " Tanganyika | [1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936] |
| 2 | 1925 | in charge, reconditioning "Liamba," | " Tanganyika *(inherited from previous clause)* | [1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936] |
| 3 | 1927 | ch. engrnr., "Liamba," | " Tanganyika *(inherited from previous clause)* | [1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936] |

## Candidate stint `Halliday, L. G___Tanganyika___1922`

- Staff-list name: **Halliday, L. G** | colony: **Tanganyika** | listed 1922–1925 | editions [1922, 1923, 1924, 1925]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1922 | L. G. Halliday | Chief Engineer, S.S. "Lord Milner" | Port and Marine | — | — |
| 1923 | L. G. Halliday | Chief Engineer | Port and Marine | — | — |
| 1924 | L. G. Halliday | Chief Engineer | Port and Marine | — | — |
| 1925 | L. G. Halliday | Chief Engineer, S.S. "Lord Milner" | Port and Marine | — | — |

### Deterministic checks: `halliday_l-g_b1883` vs `Halliday, L. G___Tanganyika___1922`

- [PASS] surname_gate: bio 'HALLIDAY' vs stint 'Halliday, L. G' (exact)
- [PASS] initials: bio ['L', 'G'] ~ stint ['L', 'G']
- [PASS] age_gate: stint starts 1922, birth 1883 (age 39)
- [PASS] colony: 3 placed event(s) resolve to 'Tanganyika'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1922-1925
- [FAIL] position_sim: best 59 vs bar 60: 'ch. engrnr., "Lord Milner," Tanganyika Territory' ~ 'Chief Engineer, S.S. "Lord Milner"'
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

