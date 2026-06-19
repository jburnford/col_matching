<!-- {"case_id": "case_mathews_d-o_b1901", "bio_ids": ["mathews_d-o_b1901"], "stint_ids": ["Mathews, D. O___Uganda___1922"]} -->
# Dossier case_mathews_d-o_b1901

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 22 official(s) with this surname in the graph's staff lists; 11 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `mathews_d-o_b1901`

- Printed name: **MATHEWS, D. O**
- Birth year: 1901 (attested in editions [1966])
- Honours: C.M.G (1965), O.B.E (1959)
- Appears in editions: [1966]

### Verbatim printed entry text (OCR)

**Version `col1966-L16613.v` — printed in editions [1966]:**

> MATHEWS, D. O., C.M.G. (1965), O.B.E. (1959).—b. 1901; ed. Latymer, St. Pauls, London, and Varndean, Brighton; mil. serv., 1918; cadet, R.A.F. and 1940-43; lt., R.E.; survey dept., Uga., 1921-46; gen. manager, E.A. tourist travel ass., 1948-64; U.N. tech. expert (tourism), 1965; dir. of tourism, Sey., 1965.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1921–1946 | survey dept. | Uganda | [1966] |
| 1 | 1940–1943 | cadet, R.A.F. and | — | [1966] |
| 2 | 1948–1964 | gen. manager, E.A. tourist travel ass | Uganda *(inherited from previous clause)* | [1966] |
| 3 | 1965 | U.N. tech. expert (tourism) | Uganda *(inherited from previous clause)* | [1966] |
| 4 | 1965 | dir. of tourism | Seychelles | [1966] |

## Candidate stint `Mathews, D. O___Uganda___1922`

- Staff-list name: **Mathews, D. O** | colony: **Uganda** | listed 1922–1940 | editions [1922, 1923, 1924, 1925, 1927, 1928, 1929, 1930, 1933, 1936, 1937, 1939, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1922 | D. O. Mathews | Draughtsman | Land and Survey Department | — | — |
| 1923 | D. O. Mathews | Draughtsmen | Land and Survey Department | — | — |
| 1924 | D. O. Mathews | Draughtsman | Land and Survey Department | — | — |
| 1925 | D. O. Mathews | Draughtsman | Land and Survey Department | — | — |
| 1927 | D. O. Mathews | Draughtsman | Land and Survey Department | — | — |
| 1928 | D. O. Mathews | Draughtsman | Land and Survey Department | — | — |
| 1929 | D. O. Mathews | Draughtsman | Land and Survey Department | — | — |
| 1930 | D. O. Mathews | Draughtsman | Land and Survey Department | — | — |
| 1933 | D. O. Mathews | Chief Draughtsman | Land and Survey Department | — | — |
| 1936 | D. O. Mathews | Chief Draughtsman | Land and Survey Department | — | — |
| 1937 | D. O. Mathews | Chief Draughtsman | Land and Survey Department | — | — |
| 1939 | D. O. Mathews | Chief Draughtsman | Land and Survey Department | — | — |
| 1940 | D. O. Mathews | Chief Draughtsman | Land and Survey Department | — | — |

### Deterministic checks: `mathews_d-o_b1901` vs `Mathews, D. O___Uganda___1922`

- [PASS] surname_gate: bio 'MATHEWS' vs stint 'Mathews, D. O' (exact)
- [PASS] initials: bio ['D', 'O'] ~ stint ['D', 'O']
- [PASS] age_gate: stint starts 1922, birth 1901 (age 21)
- [PASS] colony: 3 placed event(s) resolve to 'Uganda'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1922-1940
- [FAIL] position_sim: best 36 vs bar 60: 'survey dept.' ~ 'Draughtsmen'
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

