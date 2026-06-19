<!-- {"case_id": "case_meredith_ernest-adrian_b1891", "bio_ids": ["meredith_ernest-adrian_b1891"], "stint_ids": ["Meredith, E. A___Fiji___1929"]} -->
# Dossier case_meredith_ernest-adrian_b1891

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 15 official(s) with this surname in the graph's staff lists; 8 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `meredith_ernest-adrian_b1891`

- Printed name: **MEREDITH, Ernest Adrian**
- Birth year: 1891 (attested in editions [1948, 1949, 1950, 1951])
- Appears in editions: [1948, 1949, 1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1948-L34624.v` — printed in editions [1948, 1949, 1950, 1951]:**

> MEREDITH, Ernest Adrian.—b. 1891; ed. Lucton Sch., Kingsland, Herefordshire; on mil. serv. 1915-20, capt.; apptd., 1927; conjoint admin., 1932-33 and 1935-36; inspr., police, Fiji, 1938; assts. supt., 1943.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1915–1920 | capt. | — | [1948, 1949, 1950, 1951] |
| 1 | 1927–1927 | apptd. | — | [1948, 1949, 1950, 1951] |
| 2 | 1932–1936 | conjoint admin. | — | [1948, 1949, 1950, 1951] |
| 3 | 1938–1938 | inspr., police | Fiji | [1948, 1949, 1950, 1951] |
| 4 | 1943–1943 | assts. supt. | — | [1948, 1949, 1950, 1951] |

## Candidate stint `Meredith, E. A___Fiji___1929`

- Staff-list name: **Meredith, E. A** | colony: **Fiji** | listed 1929–1950 | editions [1929, 1930, 1933, 1934, 1936, 1937, 1939, 1940, 1950]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1929 | E. A. Meredith | Head Constable | Constabulary | — | — |
| 1930 | E. A. Meredith | Head Constable | Constabulary | — | — |
| 1933 | E. A. Meredith | Sub Inspector (2nd grade) | Constabulary | — | — |
| 1934 | E. A. Meredith | Sub Inspector (2nd grade) | Constabulary | — | — |
| 1936 | E. A. Meredith | Sub Inspector (2nd grade) | Police | — | — |
| 1937 | E. A. Meredith | Sub-Inspector (2nd grade) | Police | — | — |
| 1939 | E. A. Meredith | Inspector | Police | — | — |
| 1940 | E. A. Meredith | Inspector | Police | — | — |
| 1950 | E. A. Meredith | Assistant Superintendent | Police | — | — |

### Deterministic checks: `meredith_ernest-adrian_b1891` vs `Meredith, E. A___Fiji___1929`

- [PASS] surname_gate: bio 'MEREDITH' vs stint 'Meredith, E. A' (exact)
- [PASS] initials: bio ['E', 'A'] ~ stint ['E', 'A']
- [PASS] age_gate: stint starts 1929, birth 1891 (age 38)
- [PASS] colony: 1 placed event(s) resolve to 'Fiji'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1929-1950
- [FAIL] position_sim: best 48 vs bar 60: 'inspr., police' ~ 'Inspector'
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

