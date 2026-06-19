<!-- {"case_id": "case_feast_arthur-cooper_b1880", "bio_ids": ["feast_arthur-cooper_b1880"], "stint_ids": ["Feast, A. C___Kenya___1939"]} -->
# Dossier case_feast_arthur-cooper_b1880

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `feast_arthur-cooper_b1880`

- Printed name: **FEAST, Arthur Cooper**
- Birth year: 1880 (attested in editions [1949])
- Appears in editions: [1949]

### Verbatim printed entry text (OCR)

**Version `col1949-L31974.v` — printed in editions [1949]:**

> FEAST, Arthur Cooper.—b. 1880; ed. Merchant Taylors; on mil. serv. 1914-18, capt.; stores clk., P.W.D., Ken., 1928; clk., cent. rev. off., 1933; asst. rev. offr., 1934; senr., 1937; assessor, jt. inc. tax, 1940.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1928 | stores clk., P.W.D. | Kenya | [1949] |
| 1 | 1933 | clk., cent. rev. off | Kenya *(inherited from previous clause)* | [1949] |
| 2 | 1934 | asst. rev. offr | Kenya *(inherited from previous clause)* | [1949] |
| 3 | 1937 | senr | Kenya *(inherited from previous clause)* | [1949] |
| 4 | 1940 | assessor, jt. inc. tax | Kenya *(inherited from previous clause)* | [1949] |

## Candidate stint `Feast, A. C___Kenya___1939`

- Staff-list name: **Feast, A. C** | colony: **Kenya** | listed 1939–1940 | editions [1939, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1939 | A. C. Feast | Senior Assessor | Inland Revenue | — | — |
| 1940 | A. C. Feast | Senior Assessor | Inland Revenue | — | — |

### Deterministic checks: `feast_arthur-cooper_b1880` vs `Feast, A. C___Kenya___1939`

- [PASS] surname_gate: bio 'FEAST' vs stint 'Feast, A. C' (exact)
- [PASS] initials: bio ['A', 'C'] ~ stint ['A', 'C']
- [PASS] age_gate: stint starts 1939, birth 1880 (age 59)
- [PASS] colony: 5 placed event(s) resolve to 'Kenya'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1939-1940
- [PASS] position_sim: best 70 vs bar 60: 'assessor, jt. inc. tax' ~ 'Senior Assessor'
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

