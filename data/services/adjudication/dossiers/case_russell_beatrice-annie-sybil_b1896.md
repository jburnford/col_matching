<!-- {"case_id": "case_russell_beatrice-annie-sybil_b1896", "bio_ids": ["russell_beatrice-annie-sybil_b1896"], "stint_ids": ["Russell, B. A. S___Gold Coast___1932"]} -->
# Dossier case_russell_beatrice-annie-sybil_b1896

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 86 official(s) with this surname in the graph's staff lists; 58 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Russell, B. A. S___Gold Coast___1932` is also gate-compatible with biography(ies) outside this case: ['russell_benjamin_e1872'] (already linked elsewhere or filtered).

## Biography `russell_beatrice-annie-sybil_b1896`

- Printed name: **RUSSELL, Beatrice Annie Sybil**
- Birth year: 1896 (attested in editions [1948, 1949])
- Honours: F.R.C.P.E, M.D
- Appears in editions: [1948, 1949, 1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1948-L35657.v` — printed in editions [1948, 1949]:**

> RUSSELL, Beatrice Annie Sybil, M.D., F.R.C.P.E., D.T.M. & H. (Lond.). M.B., Ch.B. (Edin.).—b. 1896; ed. Edin. and London, Langley mem. prize, 1946; med. offr., Scottish Mission, G.C., 1924; lady med. offr., 1929; physician spec., 1948.

**Version `col1950-L39245.v` — printed in editions [1950, 1951]:**

> RUSSELL, Beatrice Annie Sybil, M.D., F.R.C.P.E., D.T.M. & H. (Lond.)—b. 1896; ed. Edin., Hse. Surg. Roy. Albert Hosp., Devonport; Bolton Inf., Lancs., Bruntfield Hosp., Edin.; hse. phys., Northamp. Gen. Hosp.; med. offr., Scottish Mission, G.C., 1924; med. offr., 1929; physician spec., 1948; author of *Malaria in Children under two years*, *Gold Coast*; *Macrocytic Anaemia, Pregnant Women, Gold Coast* (Langley Mem. Prize); and *Malnutrition in children, Kumasi*.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1924 | med. offr., Scottish Mission | Gold Coast | [1948, 1949, 1950, 1951] |
| 1 | 1929 | lady med. offr | Gold Coast *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |
| 2 | 1948 | physician spec | Gold Coast *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |

## Candidate stint `Russell, B. A. S___Gold Coast___1932`

- Staff-list name: **Russell, B. A. S** | colony: **Gold Coast** | listed 1932–1936 | editions [1932, 1936]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1932 | B. A. S. Russell | Women Medical Officer | Sanitation Branch | — | — |
| 1936 | B. A. S. Russell | Women Medical Officers | Health Branch | — | — |

### Deterministic checks: `russell_beatrice-annie-sybil_b1896` vs `Russell, B. A. S___Gold Coast___1932`

- [PASS] surname_gate: bio 'RUSSELL' vs stint 'Russell, B. A. S' (exact)
- [PASS] initials: bio ['B', 'A', 'S'] ~ stint ['B', 'A', 'S']
- [PASS] age_gate: stint starts 1932, birth 1896 (age 36)
- [PASS] colony: 3 placed event(s) resolve to 'Gold Coast'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1932-1936
- [FAIL] position_sim: best 47 vs bar 60: 'lady med. offr' ~ 'Women Medical Officer'
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

