<!-- {"case_id": "case_stoodley_edwin-alan_b1890", "bio_ids": ["stoodley_edwin-alan_b1890"], "stint_ids": ["Stoodley, E. A___Nigeria___1918"]} -->
# Dossier case_stoodley_edwin-alan_b1890

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `stoodley_edwin-alan_b1890`

- Printed name: **STOODLEY, EDWIN ALAN**
- Birth year: 1890 (attested in editions [1935, 1937, 1939, 1940])
- Appears in editions: [1934, 1935, 1937, 1939, 1940]

### Verbatim printed entry text (OCR)

**Version `dol1935-L62482.v` — printed in editions [1935, 1937, 1939, 1940]:**

> STOODLEY, EDWIN ALAN.—B. 1890; ed. Cranleigh Schi.; coll. audlt. dept., Mar., 1915; asst. audr., Nigeria, May, 1915 (seconded to E. Africa, mily. audlt., 1916-19, asst. audr., Somaliland, 1919); dep. audr., Gold Coast, July, 1933; ag. audr., May, 1934.

**Version `col1934-L63291.v` — printed in editions [1934]:**

> STOODELEY, EDWIN ALAN.—B. 1890; ed. Cranleigh Sch.; col. audit dept., Mar., 1915; asst. audr., Nigeria, May, 1915 (seconded to E. Africa, mily. audit, 1916-19; asst. audr., Somaliland, 1919); dep. audr., Gold Coast, July, 1933.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1915–1915 | coll. audlt. dept. | — | [1934, 1935, 1937, 1939, 1940] |
| 1 | 1915–1915 | asst. audr. | Nigeria | [1934, 1935, 1937, 1939, 1940] |
| 2 | 1916–1919 | mily. audlt. | East Africa | [1934, 1935, 1937, 1939, 1940] |
| 3 | 1919–1919 | asst. audr. | Somaliland | [1934, 1935, 1937, 1939, 1940] |
| 4 | 1933–1933 | dep. audr. | Gold Coast | [1934, 1935, 1937, 1939, 1940] |
| 5 | 1934 | ag. audr. | — | [1935, 1937, 1939, 1940] |

## Candidate stint `Stoodley, E. A___Nigeria___1918`

- Staff-list name: **Stoodley, E. A** | colony: **Nigeria** | listed 1918–1919 | editions [1918, 1919]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1918 | E. A. Stoodley | Assistant Auditor | Audit | — | — |
| 1919 | E. A. Stoodley | Seventeen Assistant Auditors | Audit | — | — |

### Deterministic checks: `stoodley_edwin-alan_b1890` vs `Stoodley, E. A___Nigeria___1918`

- [PASS] surname_gate: bio 'STOODLEY' vs stint 'Stoodley, E. A' (exact)
- [PASS] initials: bio ['E', 'A'] ~ stint ['E', 'A']
- [PASS] age_gate: stint starts 1918, birth 1890 (age 28)
- [PASS] colony: 1 placed event(s) resolve to 'Nigeria'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1918-1919
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

