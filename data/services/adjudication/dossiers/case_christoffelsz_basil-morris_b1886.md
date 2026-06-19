<!-- {"case_id": "case_christoffelsz_basil-morris_b1886", "bio_ids": ["christoffelsz_basil-morris_b1886"], "stint_ids": ["Christoffelsz, B. M___Ceylon___1934"]} -->
# Dossier case_christoffelsz_basil-morris_b1886

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 5 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `christoffelsz_basil-morris_b1886`

- Printed name: **CHRISTOFFELSZ, Basil Morris**
- Birth year: 1886 (attested in editions [1940])
- Appears in editions: [1933, 1934, 1935, 1936, 1939, 1940]

### Verbatim printed entry text (OCR)

**Version `col1940-L63124.v` — printed in editions [1940]:**

> CHRISTOFFELSZ, Basil Morris.—B. 1886; gen. cler. serv., Ceylon, Mar., 1904; Ceylon civ. serv., Feb., 1931; office asst., Kalutara kach., Feb., 1931; do., Matara kach., Jan., 1934; offr., cl. II, Nov., 1937; office asst., Ratnapura, Apr., 1938.

**Version `col1933-L58626.v` — printed in editions [1933, 1934, 1935, 1936, 1939]:**

> CHRISTOFFELSZ, BASIL MORRIS.—B. 1886; gen. cler. serv., Ceylon, Mar., 1904; Ceylon civ. serv., Feb., 1931; office asst., Kalutara kach., Feb., 1931; do., Matara kach., Jan., 1934.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1904 | gen. cler. serv. | Ceylon | [1933, 1934, 1935, 1936, 1939, 1940] |
| 1 | 1931 | Ceylon civ. serv | Ceylon | [1933, 1934, 1935, 1936, 1939, 1940] |
| 2 | 1934 | do., Matara kach | Ceylon *(inherited from previous clause)* | [1933, 1934, 1935, 1936, 1939, 1940] |
| 3 | 1937 | offr., cl. II | Ceylon *(inherited from previous clause)* | [1940] |
| 4 | 1938 | office asst., Ratnapura | Ceylon *(inherited from previous clause)* | [1940] |

## Candidate stint `Christoffelsz, B. M___Ceylon___1934`

- Staff-list name: **Christoffelsz, B. M** | colony: **Ceylon** | listed 1934–1937 | editions [1934, 1936, 1937]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1934 | B. M. Christoffelsz | Office Assistant | Western Province | — | — |
| 1936 | B. M. Christoffelsz | Office Assistant | Southern Province | — | — |
| 1937 | B. M. Christoffelsz | Office Assistant | SOUTHERN PROVINCE | — | — |

### Deterministic checks: `christoffelsz_basil-morris_b1886` vs `Christoffelsz, B. M___Ceylon___1934`

- [PASS] surname_gate: bio 'CHRISTOFFELSZ' vs stint 'Christoffelsz, B. M' (exact)
- [PASS] initials: bio ['B', 'M'] ~ stint ['B', 'M']
- [PASS] age_gate: stint starts 1934, birth 1886 (age 48)
- [PASS] colony: 5 placed event(s) resolve to 'Ceylon'
- [PASS] tenure_overlap: 4 event tenure(s) overlap stint years 1934-1937
- [PASS] position_sim: best 70 vs bar 60: 'office asst., Ratnapura' ~ 'Office Assistant'
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

