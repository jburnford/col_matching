<!-- {"case_id": "case_hanlon_e-l_b1913", "bio_ids": ["hanlon_e-l_b1913"], "stint_ids": ["Hannon, L___Gibraltar___1963"]} -->
# Dossier case_hanlon_e-l_b1913

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Hannon, L___Gibraltar___1963` is also gate-compatible with biography(ies) outside this case: ['hannon_l_b1916'] (already linked elsewhere or filtered).

## Biography `hanlon_e-l_b1913`

- Printed name: **HANLON, E. L**
- Birth year: 1913 (attested in editions [1957, 1958, 1960, 1961, 1962, 1963, 1964, 1965, 1966])
- Appears in editions: [1957, 1958, 1960, 1961, 1962, 1963, 1964, 1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1957-L23796.v` — printed in editions [1957, 1958, 1960, 1961, 1962, 1963, 1964, 1965, 1966]:**

> HANLON, E. L.—b. 1913; ed. St. Margaret's Sch., Manchester and Fire Services Coll.; U.K. fire service, 1937; asst. divisional offr., 1948; dep. chief fire offr., Trin., 1952; chief fire offr., 1958; fire advr. on legislation to various municipal authes., 1948–52.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1937 | U.K. fire service | — | [1957, 1958, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 1 | 1948 | asst. divisional offr | — | [1957, 1958, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 2 | 1948–1952 | fire advr. on legislation to various municipal authes | Trinidad *(inherited from previous clause)* | [1957, 1958, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 3 | 1952 | dep. chief fire offr. | Trinidad | [1957, 1958, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 4 | 1958 | chief fire offr | Trinidad *(inherited from previous clause)* | [1957, 1958, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |

## Candidate stint `Hannon, L___Gibraltar___1963`

- Staff-list name: **Hannon, L** | colony: **Gibraltar** | listed 1963–1966 | editions [1963, 1964, 1965, 1966]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1963 | L. Hannon | Commissioner of Police | Civil Establishment | — | — |
| 1964 | L. Hannon | Commissioner of Police | Civil Establishment | — | — |
| 1965 | L. Hannon | Commissioner of Police | Civil Establishment | — | — |
| 1966 | L. Hannon | Commissioner of Police | Civil Establishment | — | — |

### Deterministic checks: `hanlon_e-l_b1913` vs `Hannon, L___Gibraltar___1963`

- [PASS] surname_gate: bio 'HANLON' vs stint 'Hannon, L' (fuzzy:1)
- [PASS] initials: bio ['E', 'L'] ~ stint ['L']
- [PASS] age_gate: stint starts 1963, birth 1913 (age 50)
- [FAIL] colony: no placed event resolves to 'Gibraltar'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1963-1966
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

