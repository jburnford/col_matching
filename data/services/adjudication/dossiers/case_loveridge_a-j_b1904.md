<!-- {"case_id": "case_loveridge_a-j_b1904", "bio_ids": ["loveridge_a-j_b1904"], "stint_ids": ["Loveridge, A. J___Gold Coast___1934", "Loveridge, A___Tanganyika___1921"]} -->
# Dossier case_loveridge_a-j_b1904

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `loveridge_a-j_b1904`

- Printed name: **LOVERIDGE, A. J**
- Birth year: 1904 (attested in editions [1948, 1949, 1950, 1951, 1953, 1954, 1955, 1956])
- Honours: C.M.G (1954), O.B.E (1947)
- Appears in editions: [1948, 1949, 1950, 1951, 1953, 1954, 1955, 1956]

### Verbatim printed entry text (OCR)

**Version `col1948-L34147.v` — printed in editions [1948, 1949, 1950, 1951, 1953, 1954, 1955, 1956]:**

> LOVERIDGE, A. J., C.M.G. (1954), O.B.E. (1947).—b. 1904; ed. Emmanuel Sch. and St. John's Coll., Camb.; barrister-at-law, Middle Temple; admin. cadet, G.C., 1930; asst. dist. comsnr., 1931; dist. comsnr., 1939; jud. advr., 1945; senr., 1947; ch. regional offr., 1951.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1930 | admin. cadet | Gold Coast | [1948, 1949, 1950, 1951, 1953, 1954, 1955, 1956] |
| 1 | 1931 | asst. dist. comsnr | Gold Coast *(inherited from previous clause)* | [1948, 1949, 1950, 1951, 1953, 1954, 1955, 1956] |
| 2 | 1939 | dist. comsnr | Gold Coast *(inherited from previous clause)* | [1948, 1949, 1950, 1951, 1953, 1954, 1955, 1956] |
| 3 | 1945 | jud. advr | Gold Coast *(inherited from previous clause)* | [1948, 1949, 1950, 1951, 1953, 1954, 1955, 1956] |
| 4 | 1947 | senr | Gold Coast *(inherited from previous clause)* | [1948, 1949, 1950, 1951, 1953, 1954, 1955, 1956] |
| 5 | 1951 | ch. regional offr | Gold Coast *(inherited from previous clause)* | [1948, 1949, 1950, 1951, 1953, 1954, 1955, 1956] |

## Candidate stint `Loveridge, A. J___Gold Coast___1934`

- Staff-list name: **Loveridge, A. J** | colony: **Gold Coast** | listed 1934–1936 | editions [1934, 1936]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1934 | A. J. Loveridge | District Commissioner / Assistant District Commissioner | Administrative and Political Service | — | — |
| 1936 | A. J. Loveridge | District Commissioner | Civil Establishment | — | — |

### Deterministic checks: `loveridge_a-j_b1904` vs `Loveridge, A. J___Gold Coast___1934`

- [PASS] surname_gate: bio 'LOVERIDGE' vs stint 'Loveridge, A. J' (exact)
- [PASS] initials: bio ['A', 'J'] ~ stint ['A', 'J']
- [PASS] age_gate: stint starts 1934, birth 1904 (age 30)
- [PASS] colony: 6 placed event(s) resolve to 'Gold Coast'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1934-1936
- [PASS] position_sim: best 68 vs bar 60: 'asst. dist. comsnr' ~ 'District Commissioner / Assistant District Commissioner'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: ALL supporting events inherit their place from an earlier clause — weak evidence

## Candidate stint `Loveridge, A___Tanganyika___1921`

- Staff-list name: **Loveridge, A** | colony: **Tanganyika** | listed 1921–1923 | editions [1921, 1922, 1923]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1921 | A. Loveridge | Assistant Warden | Game | — | — |
| 1922 | A. Loveridge | Assistant Game Wardens | Game | — | — |
| 1923 | A. Loveridge | Assistant Game Wardens | Game | — | — |

### Deterministic checks: `loveridge_a-j_b1904` vs `Loveridge, A___Tanganyika___1921`

- [PASS] surname_gate: bio 'LOVERIDGE' vs stint 'Loveridge, A' (exact)
- [PASS] initials: bio ['A', 'J'] ~ stint ['A']
- [PASS] age_gate: stint starts 1921, birth 1904 (age 17)
- [FAIL] colony: no placed event resolves to 'Tanganyika'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1921-1923
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

