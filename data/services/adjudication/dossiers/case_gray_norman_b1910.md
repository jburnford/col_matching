<!-- {"case_id": "case_gray_norman_b1910", "bio_ids": ["gray_norman_b1910"], "stint_ids": ["Gray, P. N___British Honduras___1946", "Gray, W. N___Federation of Malaya___1949"]} -->
# Dossier case_gray_norman_b1910

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 93 official(s) with this surname in the graph's staff lists; 50 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['gray_norman_b1910'] carry a single initial only — the namesake trap applies.
- NOTE: stint `Gray, W. N___Federation of Malaya___1949` is also gate-compatible with biography(ies) outside this case: ['gray_william-nicol_b1908'] (already linked elsewhere or filtered).

## Biography `gray_norman_b1910`

- Printed name: **GRAY, Norman**
- Birth year: 1910 (attested in editions [1951])
- Honours: M.B
- Appears in editions: [1951]

### Verbatim printed entry text (OCR)

**Version `col1951-L38566.v` — printed in editions [1951]:**

> GRAY, Norman, M.B., Ch.B. (Edin.), D.T.M. & H. (Liverp.).—b. 1910; ed. Barrow Gram. Sch. and Edin. Univ.; med. offr., Falkland Is., 1936; G.C., 1939.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1936 | med. offr., Falkland Is | — | [1951] |
| 1 | 1939 | med. offr., Falkland Is | Gold Coast | [1951] |

## Candidate stint `Gray, P. N___British Honduras___1946`

- Staff-list name: **Gray, P. N** | colony: **British Honduras** | listed 1946–1948 | editions [1946, 1948]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1946 | P. N. Gray | Legislative Council Member | Legislative Council | — | — |
| 1948 | P. N. Gray | Legislative Council Unofficial Member | LEGISLATIVE COUNCIL | — | — |

### Deterministic checks: `gray_norman_b1910` vs `Gray, P. N___British Honduras___1946`

- [PASS] surname_gate: bio 'GRAY' vs stint 'Gray, P. N' (exact)
- [PASS] initials: bio ['N'] ~ stint ['P', 'N']
- [PASS] age_gate: stint starts 1946, birth 1910 (age 36)
- [FAIL] colony: no placed event resolves to 'British Honduras'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1946-1948
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Gray, W. N___Federation of Malaya___1949`

- Staff-list name: **Gray, W. N** | colony: **Federation of Malaya** | listed 1949–1950 | editions [1949, 1950]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | W. N. Gray | Commissioner of Police | Civil Establishment | C.M.G., D.S.O. | Colonel |
| 1950 | W. N. Gray | Commissioner of Police | Civil Establishment | C.M.G., D.S.O. | Colonel |

### Deterministic checks: `gray_norman_b1910` vs `Gray, W. N___Federation of Malaya___1949`

- [PASS] surname_gate: bio 'GRAY' vs stint 'Gray, W. N' (exact)
- [PASS] initials: bio ['N'] ~ stint ['W', 'N']
- [PASS] age_gate: stint starts 1949, birth 1910 (age 39)
- [FAIL] colony: no placed event resolves to 'Federation of Malaya'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1949-1950
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

