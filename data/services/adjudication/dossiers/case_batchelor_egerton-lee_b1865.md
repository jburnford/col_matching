<!-- {"case_id": "case_batchelor_egerton-lee_b1865", "bio_ids": ["batchelor_egerton-lee_b1865"], "stint_ids": ["Batchelor, E. L___Commonwealth Of Australia___1905", "Batchelor, E. L___South Australia___1898"]} -->
# Dossier case_batchelor_egerton-lee_b1865

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 8 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `batchelor_egerton-lee_b1865`

- Printed name: **BATCHELOR, EGERTON LEE**
- Birth year: 1865 (attested in editions [1911])
- Appears in editions: [1911]

### Verbatim printed entry text (OCR)

**Version `col1911-L43007.v` — printed in editions [1911]:**

> BATCHELOR, HON. EGERTON LEE.—B. 1865; M.H.A., South Australia, 1893-1901; leader of labour party, 1897-9; min. of educn. and agric., 1899-1901; elected to first H. of R., C. of A., 1901; re-elected, 1903 and 1906; min. for home affairs, 1904; min. of external affairs, Apr., 1910.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1893–1901 | M.H.A. | South Australia | [1911] |
| 1 | 1897–1899 | leader of labour party | — | [1911] |
| 2 | 1899–1901 | min. of educn. and agric. | — | [1911] |
| 3 | 1901–1901 | elected to first H. of R. | Commonwealth of Australia | [1911] |
| 4 | 1903–1906 | re-elected | — | [1911] |
| 5 | 1904–1904 | min. for home affairs | — | [1911] |
| 6 | 1910 | min. of external affairs | — | [1911] |

## Candidate stint `Batchelor, E. L___Commonwealth Of Australia___1905`

- Staff-list name: **Batchelor, E. L** | colony: **Commonwealth Of Australia** | listed 1905–1907 | editions [1905, 1907]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1905 | E. L. Batchelor | — | — | — | — |
| 1907 | Hon. E. L. Batchelor | — | — | — | — |

### Deterministic checks: `batchelor_egerton-lee_b1865` vs `Batchelor, E. L___Commonwealth Of Australia___1905`

- [PASS] surname_gate: bio 'BATCHELOR' vs stint 'Batchelor, E. L' (exact)
- [PASS] initials: bio ['E', 'L'] ~ stint ['E', 'L']
- [PASS] age_gate: stint starts 1905, birth 1865 (age 40)
- [PASS] colony: 1 placed event(s) resolve to 'Commonwealth Of Australia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1905-1907
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Batchelor, E. L___South Australia___1898`

- Staff-list name: **Batchelor, E. L** | colony: **South Australia** | listed 1898–1900 | editions [1898, 1900]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1898 | E. L. Batchelor | Member | House of Assembly | — | — |
| 1900 | E. L. Batchelor | Minister of Education and Agriculture | Executive Council | — | — |
| 1900 | E. L. Batchelor | Minister of Education and Agriculture | Departments under Direction of the Minister of Education and Agriculture | — | — |

### Deterministic checks: `batchelor_egerton-lee_b1865` vs `Batchelor, E. L___South Australia___1898`

- [PASS] surname_gate: bio 'BATCHELOR' vs stint 'Batchelor, E. L' (exact)
- [PASS] initials: bio ['E', 'L'] ~ stint ['E', 'L']
- [PASS] age_gate: stint starts 1898, birth 1865 (age 33)
- [PASS] colony: 1 placed event(s) resolve to 'South Australia'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1898-1900
- [FAIL] position_sim: best 22 vs bar 60: 'M.H.A.' ~ 'Member'
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

