<!-- {"case_id": "case_pottinger_joseph-hector_b1898", "bio_ids": ["pottinger_joseph-hector_b1898"], "stint_ids": ["Pottinger, J___Gold Coast___1929"]} -->
# Dossier case_pottinger_joseph-hector_b1898

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `pottinger_joseph-hector_b1898`

- Printed name: **POTTINGER, Joseph Hector**
- Birth year: 1898 (attested in editions [1953, 1954])
- Honours: D.P.H, D.T.H, D.T.M, M.B
- Appears in editions: [1933, 1934, 1935, 1936, 1937, 1939, 1940, 1948, 1949, 1950, 1951, 1953, 1954]

### Verbatim printed entry text (OCR)

**Version `col1953-L18754.v` — printed in editions [1953, 1954]:**

> POTTINGER, J. H.—b. 1898 ; ed. Sec. Sch. for Boys, Bootle, Lancs., and Univ. of Liverpool ; mil. serv., 1915-18, 2nd lieut. ; M.O.H., G.C., 1928 ; asst. govt. M.O.H., B. Guiana, 1932 ; S.M.O., Pal., 1935 ; Nig., 1947 ; asst. D.M.S., 1948 ; D.M.S., W. regn., 1951.

**Version `col1948-L35310.v` — printed in editions [1948, 1949, 1950, 1951]:**

> POTTINGER, Joseph Hector, M.B., Ch.B. (Liv.), D.T.M., D.T.H., D.P.H.—b. 1898; ed. Sec. Sch. for Boys, Bootle, Lancs. and Univ. of Liverpool; on mil. serv. 1915-18, 2nd lieut.; M.O.H., G.C., 1928; asst. govt. M.O.H., B. Guiana, 1932; S.M.O., Pal., 1935; Nig., 1947; asst. D.M.S., 1948.

**Version `col1933-L62746.v` — printed in editions [1933, 1934, 1935, 1936, 1937, 1939]:**

> POTTINGER, JOSEPH HECTOR, M.B., Ch.B., D.P.H., D.T.M. & H. (I.pool).—B. 1898; on war serv., 1915-18; med. offr., health, W. African med. staff, Gold Coast, 1928; asst. gov't. med. offr. of health, Br. Guiana, 1932; senr. med. offr., Palestine, 1935.

**Version `col1940-L67671.v` — printed in editions [1940]:**

> POTTINGER, JOSEPH HECTOR, M.B., CH.B., D.P.H., D.T.M. & H. (LPOOL).—B. 1898; ON WAR SERV., 1915-18; MED. OFFR., HEALTH, W. AFRICAN MED. STAFF, GOLD COAST, 1928; ASST. GOV'T. MED. OFFR. OF HEALTH, BR. GUIANA, 1932; SENR. MED. OFFR., PALESTINE, 1935.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1928 | M.O.H. | Gold Coast | [1933, 1934, 1935, 1936, 1937, 1939, 1940, 1948, 1949, 1950, 1951, 1953, 1954] |
| 1 | 1932 | asst. govt. M.O.H., B. Guiana | Gold Coast *(inherited from previous clause)* | [1948, 1949, 1950, 1951, 1953, 1954] |
| 2 | 1932 | asst. gov't. med. offr. of health | British Guiana | [1933, 1934, 1935, 1936, 1937, 1939, 1940] |
| 3 | 1935 | S.M.O. | Palestine | [1933, 1934, 1935, 1936, 1937, 1939, 1940, 1948, 1949, 1950, 1951, 1953, 1954] |
| 4 | 1947 | S.M.O. | Nigeria | [1948, 1949, 1950, 1951, 1953, 1954] |
| 5 | 1948 | asst. D.M.S | Nigeria *(inherited from previous clause)* | [1948, 1949, 1950, 1951, 1953, 1954] |
| 6 | 1951 | D.M.S., W. regn | Nigeria *(inherited from previous clause)* | [1953, 1954] |

## Candidate stint `Pottinger, J___Gold Coast___1929`

- Staff-list name: **Pottinger, J** | colony: **Gold Coast** | listed 1929–1932 | editions [1929, 1932]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1929 | J. Pottinger | Medical Officer of Health | Sanitation Branch | — | — |
| 1932 | J. Pottinger | Medical Officer of Health | Sanitation Branch | — | — |

### Deterministic checks: `pottinger_joseph-hector_b1898` vs `Pottinger, J___Gold Coast___1929`

- [PASS] surname_gate: bio 'POTTINGER' vs stint 'Pottinger, J' (exact)
- [PASS] initials: bio ['J', 'H'] ~ stint ['J']
- [PASS] age_gate: stint starts 1929, birth 1898 (age 31)
- [PASS] colony: 2 placed event(s) resolve to 'Gold Coast'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1929-1932
- [FAIL] position_sim: best 30 vs bar 60: 'asst. govt. M.O.H., B. Guiana' ~ 'Medical Officer of Health'
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

