<!-- {"case_id": "case_burnham_harold-rayleigh_b1902", "bio_ids": ["burnham_harold-rayleigh_b1902"], "stint_ids": ["Burnham, H. R___Kenya___1939"]} -->
# Dossier case_burnham_harold-rayleigh_b1902

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 5 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `burnham_harold-rayleigh_b1902`

- Printed name: **BURNHAM, Harold Rayleigh**
- Birth year: 1902 (attested in editions [1948, 1949, 1950, 1951])
- Appears in editions: [1948, 1949, 1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1948-L31514.v` — printed in editions [1948, 1949, 1950, 1951]:**

> BURNHAM, Harold Rayleigh.—b. 1902; ed. Berkhampsted Sch. and Camb. Univ., B.A. (econ.); on mil. serv. 1939-43, capt.; asst. to inc. tax advsr., Ken., 1933; clk., inland rev. dept., 1934; assessor, inc. tax dept., 1937; dep. comsnr., inc. tax, S.L., 1944; asst. comsnr., inc. tax, Ken., 1949.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1933 | asst. to inc. tax advsr. | Kenya | [1948, 1949, 1950, 1951] |
| 1 | 1934 | clk., inland rev. dept | Kenya *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |
| 2 | 1937 | assessor, inc. tax dept | Kenya *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |
| 3 | 1944 | dep. comsnr., inc. tax | Sierra Leone | [1948, 1949, 1950, 1951] |
| 4 | 1949 | asst. comsnr., inc. tax | Kenya | [1948, 1949, 1950, 1951] |

## Candidate stint `Burnham, H. R___Kenya___1939`

- Staff-list name: **Burnham, H. R** | colony: **Kenya** | listed 1939–1940 | editions [1939, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1939 | H. R. Burnham | Assessors | Inland Revenue | — | — |
| 1940 | H. R. Burnham | Assessors | Inland Revenue | — | — |

### Deterministic checks: `burnham_harold-rayleigh_b1902` vs `Burnham, H. R___Kenya___1939`

- [PASS] surname_gate: bio 'BURNHAM' vs stint 'Burnham, H. R' (exact)
- [PASS] initials: bio ['H', 'R'] ~ stint ['H', 'R']
- [PASS] age_gate: stint starts 1939, birth 1902 (age 37)
- [PASS] colony: 4 placed event(s) resolve to 'Kenya'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1939-1940
- [FAIL] position_sim: best 53 vs bar 60: 'assessor, inc. tax dept' ~ 'Assessors'
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

