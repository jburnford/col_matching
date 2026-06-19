<!-- {"case_id": "case_rosedale_william-ormel-pelly_b1891", "bio_ids": ["rosedale_william-ormel-pelly_b1891"], "stint_ids": ["Rosedale, W. O. P___Nigeria___1918"]} -->
# Dossier case_rosedale_william-ormel-pelly_b1891

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `rosedale_william-ormel-pelly_b1891`

- Printed name: **ROSEDALE, William Ormel Pelly**
- Birth year: 1891 (attested in editions [1933, 1934, 1935, 1936, 1937, 1939, 1940])
- Appears in editions: [1933, 1934, 1935, 1936, 1937, 1939, 1940]

### Verbatim printed entry text (OCR)

**Version `col1933-L63037.v` — printed in editions [1933, 1934, 1935, 1936, 1937, 1939, 1940]:**

> ROSEDALE, William Ormel Pelly.—B. 1891; asst. dist. offr., Nigeria, Aug., 1914; dist. offr., 1924; asst. sec. and clk., exec. and leg. couns., 1937; ag. prin. asst. sec., 1930-31; admistr. offr., class I., Oct., 1930; staff grade, 1937.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1914 | asst. dist. offr. | Nigeria | [1933, 1934, 1935, 1936, 1937, 1939, 1940] |
| 1 | 1924 | dist. offr | Nigeria *(inherited from previous clause)* | [1933, 1934, 1935, 1936, 1937, 1939, 1940] |
| 2 | 1930–1931 | ag. prin. asst. sec | Nigeria *(inherited from previous clause)* | [1933, 1934, 1935, 1936, 1937, 1939, 1940] |
| 3 | 1937 | asst. sec. and clk., exec. and leg. couns | Nigeria *(inherited from previous clause)* | [1933, 1934, 1935, 1936, 1937, 1939, 1940] |

## Candidate stint `Rosedale, W. O. P___Nigeria___1918`

- Staff-list name: **Rosedale, W. O. P** | colony: **Nigeria** | listed 1918–1919 | editions [1918, 1919]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1918 | W. O. P. Rosedale | Sixty‑four Assistant District Officer | Northern Provinces | — | — |
| 1919 | W. O. P. Rosedale | Sixty-four Assistant District Officers | NORTHERN PROVINCES | — | — |

### Deterministic checks: `rosedale_william-ormel-pelly_b1891` vs `Rosedale, W. O. P___Nigeria___1918`

- [PASS] surname_gate: bio 'ROSEDALE' vs stint 'Rosedale, W. O. P' (exact)
- [PASS] initials: bio ['W', 'O', 'P'] ~ stint ['W', 'O', 'P']
- [PASS] age_gate: stint starts 1918, birth 1891 (age 27)
- [PASS] colony: 4 placed event(s) resolve to 'Nigeria'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1918-1919
- [FAIL] position_sim: best 56 vs bar 60: 'asst. dist. offr.' ~ 'Sixty‑four Assistant District Officer'
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

