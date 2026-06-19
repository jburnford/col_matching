<!-- {"case_id": "case_cochrane_g-c_b1904", "bio_ids": ["cochrane_g-c_b1904"], "stint_ids": ["Cochrane, G. C___Kenya___1949"]} -->
# Dossier case_cochrane_g-c_b1904

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 28 official(s) with this surname in the graph's staff lists; 11 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `cochrane_g-c_b1904`

- Printed name: **COCHRANE, G. C**
- Birth year: 1904 (attested in editions [1957, 1958, 1959])
- Appears in editions: [1957, 1958, 1959]

### Verbatim printed entry text (OCR)

**Version `col1957-L22019.v` — printed in editions [1957, 1958, 1959]:**

> COCHRANE, G. C.—b. 1904; ed. King William Coll., I. o. M., and London Univ.; mil. serv., 1940-47, maj.; M.O., Ken., 1947; S.M.O., 1952.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1947 | M.O. | Kenya | [1957, 1958, 1959] |
| 1 | 1952 | S.M.O | Kenya *(inherited from previous clause)* | [1957, 1958, 1959] |

## Candidate stint `Cochrane, G. C___Kenya___1949`

- Staff-list name: **Cochrane, G. C** | colony: **Kenya** | listed 1949–1951 | editions [1949, 1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | G. C. Cochrane | Medical Officer | Medical | — | — |
| 1950 | G. C. Cochrane | Medical Officer | Medical | — | — |
| 1951 | G. C. Cochrane | Medical Officer | Medical | — | — |

### Deterministic checks: `cochrane_g-c_b1904` vs `Cochrane, G. C___Kenya___1949`

- [PASS] surname_gate: bio 'COCHRANE' vs stint 'Cochrane, G. C' (exact)
- [PASS] initials: bio ['G', 'C'] ~ stint ['G', 'C']
- [PASS] age_gate: stint starts 1949, birth 1904 (age 45)
- [PASS] colony: 2 placed event(s) resolve to 'Kenya'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1949-1951
- [FAIL] position_sim: best 24 vs bar 60: 'M.O.' ~ 'Medical Officer'
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

