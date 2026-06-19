<!-- {"case_id": "case_de-boissiere_george-anthony-vallen-ton_b1898", "bio_ids": ["de-boissiere_george-anthony-vallen-ton_b1898"], "stint_ids": ["de Boissiere, G. A. V___Nigeria___1933", "de Boissiere, G___Trinidad and Tobago___1922"]} -->
# Dossier case_de-boissiere_george-anthony-vallen-ton_b1898

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 9 official(s) with this surname in the graph's staff lists; 4 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `de Boissiere, G. A. V___Nigeria___1933` is also gate-compatible with biography(ies) outside this case: ['de-boissiere_arnauld_b1872'] (already linked elsewhere or filtered).

## Biography `de-boissiere_george-anthony-vallen-ton_b1898`

- Printed name: **DE BOISSIERE, George Anthony Vallen-ton**
- Birth year: 1898 (attested in editions [1951])
- Appears in editions: [1951]

### Verbatim printed entry text (OCR)

**Version `col1951-L37499.v` — printed in editions [1951]:**

> DE BOISSIERE, George Anthony Vallen-ton.—b. 1898; ed. St. Mary’s Coll., Trin. and Lodge Sch., Barbados; on mil. serv., 1915–19, F.O.; apptd. col. police, Trin., 1920; asst. comsnr., Nig., 1926; supt., 1940.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1920 | apptd. col. police | Trinidad | [1951] |
| 1 | 1926 | asst. comsnr. | Nigeria | [1951] |
| 2 | 1940 | supt | Nigeria *(inherited from previous clause)* | [1951] |

## Candidate stint `de Boissiere, G. A. V___Nigeria___1933`

- Staff-list name: **de Boissiere, G. A. V** | colony: **Nigeria** | listed 1933–1939 | editions [1933, 1934, 1936, 1939]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1933 | G. A. V. de Boissiere | Commissioner/Assistant Commissioner | Police | — | — |
| 1934 | G. A. V. de Boissiere | Commissioner/Assistant Commissioner | Police | — | — |
| 1936 | G. A. V. de Boissiere | Commissioners and Assistant Commissioners | Police | — | — |
| 1939 | G. A. V. de Boissiere | Senior Assistant Superintendent | Police | — | — |

### Deterministic checks: `de-boissiere_george-anthony-vallen-ton_b1898` vs `de Boissiere, G. A. V___Nigeria___1933`

- [PASS] surname_gate: bio 'DE BOISSIERE' vs stint 'de Boissiere, G. A. V' (exact)
- [PASS] initials: bio ['G', 'A', 'V'] ~ stint ['G', 'A', 'V']
- [PASS] age_gate: stint starts 1933, birth 1898 (age 35)
- [PASS] colony: 2 placed event(s) resolve to 'Nigeria'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1933-1939
- [FAIL] position_sim: best 58 vs bar 60: 'asst. comsnr.' ~ 'Commissioners and Assistant Commissioners'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

## Candidate stint `de Boissiere, G___Trinidad and Tobago___1922`

- Staff-list name: **de Boissiere, G** | colony: **Trinidad and Tobago** | listed 1922–1925 | editions [1922, 1923, 1925]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1922 | G. de Boissiere | Sub-Inspector | Constabulary and Gaols | — | — |
| 1923 | G. de Boissiere | Sub-Inspector | Constabulary and Gaols | — | — |
| 1925 | G. de Boissiere | Sub-Inspector | Constabulary and Gaols | — | — |

### Deterministic checks: `de-boissiere_george-anthony-vallen-ton_b1898` vs `de Boissiere, G___Trinidad and Tobago___1922`

- [PASS] surname_gate: bio 'DE BOISSIERE' vs stint 'de Boissiere, G' (exact)
- [PASS] initials: bio ['G', 'A', 'V'] ~ stint ['G']
- [PASS] age_gate: stint starts 1922, birth 1898 (age 24)
- [FAIL] colony: no placed event resolves to 'Trinidad and Tobago'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1922-1925
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

