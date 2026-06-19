<!-- {"case_id": "case_blenkiron_james-ernest_b1870", "bio_ids": ["blenkiron_james-ernest_b1870"], "stint_ids": ["Blenkiron, J. E___British Central Africa___1906"]} -->
# Dossier case_blenkiron_james-ernest_b1870

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `blenkiron_james-ernest_b1870`

- Printed name: **BLENKIRON, JAMES ERNEST**
- Birth year: 1870 (attested in editions [1906, 1907, 1908, 1909])
- Appears in editions: [1906, 1907, 1908, 1909]

### Verbatim printed entry text (OCR)

**Version `col1906-L44311.v` — printed in editions [1906, 1907, 1908, 1909]:**

> BLENKIRON, JAMES ERNEST.—B. 1870; 3rd acctnt., B. Cent. Africa Prot., Dec., 1893; 1st asst. treas., 1901; ag. treas., Apl. to Dec., 1902, Nov., 1904, to June, 1905, and Mar. to Oct., 1907.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1893 | 3rd acctnt. | British Central Africa Protectorate | [1906, 1907, 1908, 1909] |
| 1 | 1901 | 1st asst. treas. | — | [1906, 1907, 1908, 1909] |
| 2 | 1902–1902 | ag. treas. | — | [1906, 1907, 1908, 1909] |
| 3 | 1904–1905 | ag. treas. | — | [1906, 1907, 1908, 1909] |
| 4 | 1907–1907 | ag. treas. | — | [1906, 1907, 1908, 1909] |

## Candidate stint `Blenkiron, J. E___British Central Africa___1906`

- Staff-list name: **Blenkiron, J. E** | colony: **British Central Africa** | listed 1906–1907 | editions [1906, 1907]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1906 | J. E. Blenkiron | Assistant Treasurer | Treasury | — | — |
| 1907 | J. E. Blenkiron | Assistant Treasurers | Treasury | — | — |

### Deterministic checks: `blenkiron_james-ernest_b1870` vs `Blenkiron, J. E___British Central Africa___1906`

- [PASS] surname_gate: bio 'BLENKIRON' vs stint 'Blenkiron, J. E' (exact)
- [PASS] initials: bio ['J', 'E'] ~ stint ['J', 'E']
- [PASS] age_gate: stint starts 1906, birth 1870 (age 36)
- [PASS] colony: 1 placed event(s) resolve to 'British Central Africa'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1906-1907
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

