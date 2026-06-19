<!-- {"case_id": "case_martin_kenneth-septon_b1888", "bio_ids": ["martin_kenneth-septon_b1888"], "stint_ids": ["Martin, K. S___Nigeria___1927"]} -->
# Dossier case_martin_kenneth-septon_b1888

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 135 official(s) with this surname in the graph's staff lists; 55 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `martin_kenneth-septon_b1888`

- Printed name: **MARTIN, KENNETH SEPTON**
- Birth year: 1888 (attested in editions [1931, 1932, 1933, 1934, 1935, 1936, 1937, 1939, 1940])
- Honours: O.B.E (1939)
- Appears in editions: [1931, 1932, 1933, 1934, 1935, 1936, 1937, 1939, 1940]

### Verbatim printed entry text (OCR)

**Version `col1931-L66565.v` — printed in editions [1931, 1932, 1933, 1934, 1935, 1936, 1937, 1939, 1940]:**

> MARTIN, KENNETH SEPTON, O.B.E. (1939), B.A. (Oxon).—B. 1888; asst. dist. consur., S. Nigeria, 1911; supervisor, cust., 2nd grade, 1911; 1st grade, 1919; senr. collr., 1929; asst. comptr., 1933; ag. comptr. on various occasions, 1931-39; d-p. comptr., 1936.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1911 | asst. dist. consur. | Southern Nigeria | [1931, 1932, 1933, 1934, 1935, 1936, 1937, 1939, 1940] |
| 1 | 1919 | 1st grade | Southern Nigeria *(inherited from previous clause)* | [1931, 1932, 1933, 1934, 1935, 1936, 1937, 1939, 1940] |
| 2 | 1929 | senr. collr | Southern Nigeria *(inherited from previous clause)* | [1931, 1932, 1933, 1934, 1935, 1936, 1937, 1939, 1940] |
| 3 | 1931–1939 | ag. comptr. on various occasions | Southern Nigeria *(inherited from previous clause)* | [1931, 1932, 1933, 1934, 1935, 1936, 1937, 1939, 1940] |
| 4 | 1933 | asst. comptr | Southern Nigeria *(inherited from previous clause)* | [1931, 1932, 1933, 1934, 1935, 1936, 1937, 1939, 1940] |
| 5 | 1936 | d-p. comptr | Southern Nigeria *(inherited from previous clause)* | [1931, 1932, 1933, 1934, 1935, 1936, 1937, 1939, 1940] |

## Candidate stint `Martin, K. S___Nigeria___1927`

- Staff-list name: **Martin, K. S** | colony: **Nigeria** | listed 1927–1939 | editions [1927, 1929, 1933, 1934, 1939]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1927 | K. S. Martin | Collector/Supervisor | Customs | — | — |
| 1929 | K. S. Martin | Collectors and Supervisors | Customs | — | — |
| 1933 | K. S. Martin | Senior Collector | Customs | — | — |
| 1934 | K. S. Martin | Senior Collector | Customs | — | — |
| 1939 | K. S. Martin | Assistant Comptroller | Customs | — | — |

### Deterministic checks: `martin_kenneth-septon_b1888` vs `Martin, K. S___Nigeria___1927`

- [PASS] surname_gate: bio 'MARTIN' vs stint 'Martin, K. S' (exact)
- [PASS] initials: bio ['K', 'S'] ~ stint ['K', 'S']
- [PASS] age_gate: stint starts 1927, birth 1888 (age 39)
- [PASS] colony: 6 placed event(s) resolve to 'Nigeria'
- [PASS] tenure_overlap: 5 event tenure(s) overlap stint years 1927-1939
- [PASS] position_sim: best 77 vs bar 60: 'senr. collr' ~ 'Senior Collector'
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

