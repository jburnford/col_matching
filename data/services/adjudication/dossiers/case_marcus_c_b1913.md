<!-- {"case_id": "case_marcus_c_b1913", "bio_ids": ["marcus_c_b1913"], "stint_ids": ["Marcus, C___Singapore___1949"]} -->
# Dossier case_marcus_c_b1913

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['marcus_c_b1913'] carry a single initial only — the namesake trap applies.

## Biography `marcus_c_b1913`

- Printed name: **MARCUS, C**
- Birth year: 1913 (attested in editions [1957, 1958, 1959])
- Appears in editions: [1956, 1957, 1958, 1959]

### Verbatim printed entry text (OCR)

**Version `col1957-L25514.v` — printed in editions [1957, 1958, 1959]:**

> MARCUS, C.—b. 1913; ed. St. Joseph's Instn. and King Edward VII Coll. of Medicine, S'pore; asst. M.O., S.S., 1937; M.O., 1947; i/c out-patients' dept., gen. hosp., S'pore, 1953; med. supt., gen. hosp., 1957.

**Version `col1956-L22920.v` — printed in editions [1956]:**

> MARCUS, C.—b. 1913; ed. St. Joseph's Instn. and King Edward VII Coll. of Medicine, S'pore; asst. M.O., S.S., 1937; M.O., 1947.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1937 | asst. M.O. | Straits Settlements | [1956, 1957, 1958, 1959] |
| 1 | 1947 | M.O | Straits Settlements *(inherited from previous clause)* | [1956, 1957, 1958, 1959] |
| 2 | 1953 | i/c out-patients' dept., gen. hosp., S'pore | Straits Settlements *(inherited from previous clause)* | [1957, 1958, 1959] |
| 3 | 1957 | med. supt., gen. hosp | Straits Settlements *(inherited from previous clause)* | [1957, 1958, 1959] |

## Candidate stint `Marcus, C___Singapore___1949`

- Staff-list name: **Marcus, C** | colony: **Singapore** | listed 1949–1951 | editions [1949, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | C. Marcus | Medical Officer | Hospitals and Dispensaries | — | — |
| 1951 | C. Marcus | Medical Officer | Hospitals and Dispensaries | — | — |

### Deterministic checks: `marcus_c_b1913` vs `Marcus, C___Singapore___1949`

- [PASS] surname_gate: bio 'MARCUS' vs stint 'Marcus, C' (exact)
- [PASS] initials: bio ['C'] ~ stint ['C']
- [PASS] age_gate: stint starts 1949, birth 1913 (age 36)
- [FAIL] colony: no placed event resolves to 'Singapore'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1949-1951
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

