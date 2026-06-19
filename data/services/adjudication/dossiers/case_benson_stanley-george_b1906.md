<!-- {"case_id": "case_benson_stanley-george_b1906", "bio_ids": ["benson_stanley-george_b1906"], "stint_ids": ["Benson, S. G. R___Trinidad and Tobago___1949"]} -->
# Dossier case_benson_stanley-george_b1906

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 26 official(s) with this surname in the graph's staff lists; 11 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `benson_stanley-george_b1906`

- Printed name: **BENSON, Stanley George**
- Birth year: 1906 (attested in editions [1948, 1949, 1950, 1951])
- Appears in editions: [1948, 1949, 1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1948-L31134.v` — printed in editions [1948, 1949, 1950, 1951]:**

> BENSON, Stanley George.—b. 1906; ed. Harrogate; on mil. serv. 1926–32; home prisons serv., 1934; dep. supt. of prisons, Trin., 1939; supt., 1946.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1934 | home prisons serv | — | [1948, 1949, 1950, 1951] |
| 1 | 1939 | dep. supt. of prisons | Trinidad | [1948, 1949, 1950, 1951] |
| 2 | 1946 | supt | Trinidad *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |

## Candidate stint `Benson, S. G. R___Trinidad and Tobago___1949`

- Staff-list name: **Benson, S. G. R** | colony: **Trinidad and Tobago** | listed 1949–1953 | editions [1949, 1952, 1953]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | S. G. Benson | Superintendent of Prisons | PRISONS | — | — |
| 1952 | S. G. R. Benson | Superintendent of Prisons | Civil Establishment | — | — |
| 1953 | S. G. Benson | Superintendent of Prisons | Civil Establishment | — | — |

### Deterministic checks: `benson_stanley-george_b1906` vs `Benson, S. G. R___Trinidad and Tobago___1949`

- [PASS] surname_gate: bio 'BENSON' vs stint 'Benson, S. G. R' (exact)
- [PASS] initials: bio ['S', 'G'] ~ stint ['S', 'G', 'R']
- [PASS] age_gate: stint starts 1949, birth 1906 (age 43)
- [FAIL] colony: no placed event resolves to 'Trinidad and Tobago'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1949-1953
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

