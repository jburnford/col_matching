<!-- {"case_id": "case_thomas_d-g_b1913", "bio_ids": ["thomas_d-g_b1913"], "stint_ids": ["Thomas, D. G___Uganda___1949"]} -->
# Dossier case_thomas_d-g_b1913

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 182 official(s) with this surname in the graph's staff lists; 53 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Thomas, D. G___Uganda___1949` is also gate-compatible with biography(ies) outside this case: ['thomas_david-gwynfor_b1923'] (already linked elsewhere or filtered).

## Biography `thomas_d-g_b1913`

- Printed name: **THOMAS, D. G**
- Birth year: 1913 (attested in editions [1958, 1959, 1960, 1961, 1962, 1963])
- Appears in editions: [1958, 1959, 1960, 1961, 1962, 1963]

### Verbatim printed entry text (OCR)

**Version `col1958-L27511.v` — printed in editions [1958, 1959, 1960, 1961, 1962, 1963]:**

> THOMAS, D. G.—b. 1913; ed. Towyn Gram. Sch., and Univ. Coll., Wales; solicitor; mil. serv., 1940-46, capt.; asst. land offr., Tang., 1950; registr. of titles and conveyancer, Uga., 1957-62. (Uga. Govt. service.)

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1950 | asst. land offr. | Tanganyika | [1958, 1959, 1960, 1961, 1962, 1963] |
| 1 | 1957–1962 | registr. of titles and conveyancer | Uganda | [1958, 1959, 1960, 1961, 1962, 1963] |

## Candidate stint `Thomas, D. G___Uganda___1949`

- Staff-list name: **Thomas, D. G** | colony: **Uganda** | listed 1949–1951 | editions [1949, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | D. G. Thomas | Botanist | Agricultural | — | — |
| 1951 | D. G. Thomas | Botanists | Agricultural | — | — |

### Deterministic checks: `thomas_d-g_b1913` vs `Thomas, D. G___Uganda___1949`

- [PASS] surname_gate: bio 'THOMAS' vs stint 'Thomas, D. G' (exact)
- [PASS] initials: bio ['D', 'G'] ~ stint ['D', 'G']
- [PASS] age_gate: stint starts 1949, birth 1913 (age 36)
- [PASS] colony: 1 placed event(s) resolve to 'Uganda'
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

