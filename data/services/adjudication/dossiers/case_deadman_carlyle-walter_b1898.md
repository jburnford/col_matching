<!-- {"case_id": "case_deadman_carlyle-walter_b1898", "bio_ids": ["deadman_carlyle-walter_b1898"], "stint_ids": ["Deadman, C. W___Kenya___1939"]} -->
# Dossier case_deadman_carlyle-walter_b1898

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `deadman_carlyle-walter_b1898`

- Printed name: **DEADMAN, Carlyle Walter**
- Birth year: 1898 (attested in editions [1948, 1949, 1950, 1951])
- Appears in editions: [1948, 1949, 1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1948-L32174.v` — printed in editions [1948, 1949, 1950, 1951]:**

> DEADMAN, Carlyle Walter.—b. 1898; ed. Normal Coll., Pretoria, S.A. (bursary and schol.) ; on mil. serv. 1917-21; clk., cent. rev. off., Ken., 1933; assessor, inland rev., Ken., 1937; asst. comsnr., jt. inc. tax dept., 1940; reg. comsnr., 1946.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1933 | clk., cent. rev. off. | Kenya | [1948, 1949, 1950, 1951] |
| 1 | 1937 | assessor, inland rev. | Kenya | [1948, 1949, 1950, 1951] |
| 2 | 1940 | asst. comsnr., jt. inc. tax dept | Kenya *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |
| 3 | 1946 | reg. comsnr | Kenya *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |

## Candidate stint `Deadman, C. W___Kenya___1939`

- Staff-list name: **Deadman, C. W** | colony: **Kenya** | listed 1939–1940 | editions [1939, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1939 | C. W. Deadman | Assessors | Inland Revenue | — | — |
| 1940 | C. W. Deadman | Assessors | Inland Revenue | — | — |

### Deterministic checks: `deadman_carlyle-walter_b1898` vs `Deadman, C. W___Kenya___1939`

- [PASS] surname_gate: bio 'DEADMAN' vs stint 'Deadman, C. W' (exact)
- [PASS] initials: bio ['C', 'W'] ~ stint ['C', 'W']
- [PASS] age_gate: stint starts 1939, birth 1898 (age 41)
- [PASS] colony: 4 placed event(s) resolve to 'Kenya'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1939-1940
- [FAIL] position_sim: best 57 vs bar 60: 'assessor, inland rev.' ~ 'Assessors'
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

