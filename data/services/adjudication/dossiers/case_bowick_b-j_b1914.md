<!-- {"case_id": "case_bowick_b-j_b1914", "bio_ids": ["bowick_b-j_b1914"], "stint_ids": ["Bowick, B. J___Gold Coast___1949"]} -->
# Dossier case_bowick_b-j_b1914

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `bowick_b-j_b1914`

- Printed name: **BOWICK, B. J**
- Birth year: 1914 (attested in editions [1953, 1954, 1955, 1956, 1957, 1958, 1959])
- Appears in editions: [1953, 1954, 1955, 1956, 1957, 1958, 1959]

### Verbatim printed entry text (OCR)

**Version `col1953-L16645.v` — printed in editions [1953, 1954, 1955, 1956, 1957, 1958, 1959]:**

> BOWICK, B. J.—b. 1914; ed. Ipswich Sch.; mil. serv., 1939-46; senr. assess. offr., inc. tax dept., G.C., 1946; asst. comsnr., 1948; dep. comsnr., 1951; comsnr., income tax, 1954-58 (Ghana civil service).

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1946 | senr. assess. offr., inc. tax dept. | Gold Coast | [1953, 1954, 1955, 1956, 1957, 1958, 1959] |
| 1 | 1948 | asst. comsnr | Gold Coast *(inherited from previous clause)* | [1953, 1954, 1955, 1956, 1957, 1958, 1959] |
| 2 | 1951 | dep. comsnr | Gold Coast *(inherited from previous clause)* | [1953, 1954, 1955, 1956, 1957, 1958, 1959] |
| 3 | 1954–1958 | comsnr., income tax | Gold Coast *(inherited from previous clause)* | [1953, 1954, 1955, 1956, 1957, 1958, 1959] |

## Candidate stint `Bowick, B. J___Gold Coast___1949`

- Staff-list name: **Bowick, B. J** | colony: **Gold Coast** | listed 1949–1951 | editions [1949, 1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | B. J. Bowick | Assistant Commissioner | Income Tax | — | — |
| 1950 | B. J. Bowick | Assistant Commissioners | Income Tax | — | — |
| 1951 | B. J. Bowick | Assistant Commissioner | Income Tax | — | — |

### Deterministic checks: `bowick_b-j_b1914` vs `Bowick, B. J___Gold Coast___1949`

- [PASS] surname_gate: bio 'BOWICK' vs stint 'Bowick, B. J' (exact)
- [PASS] initials: bio ['B', 'J'] ~ stint ['B', 'J']
- [PASS] age_gate: stint starts 1949, birth 1914 (age 35)
- [PASS] colony: 4 placed event(s) resolve to 'Gold Coast'
- [PASS] tenure_overlap: 3 event tenure(s) overlap stint years 1949-1951
- [PASS] position_sim: best 67 vs bar 60: 'asst. comsnr' ~ 'Assistant Commissioner'
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

