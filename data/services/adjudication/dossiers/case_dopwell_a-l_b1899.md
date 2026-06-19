<!-- {"case_id": "case_dopwell_a-l_b1899", "bio_ids": ["dopwell_a-l_b1899"], "stint_ids": ["Dopwell, A. L___Windward Islands___1922", "Dopwell, A. L___Windward Islands___1937"]} -->
# Dossier case_dopwell_a-l_b1899

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `dopwell_a-l_b1899`

- Printed name: **DOPWELL, A. L**
- Birth year: 1899 (attested in editions [1953, 1954, 1955, 1957, 1958, 1959])
- Appears in editions: [1953, 1954, 1955, 1957, 1958, 1959]

### Verbatim printed entry text (OCR)

**Version `col1953-L17174.v` — printed in editions [1953, 1954, 1955, 1957, 1958, 1959]:**

> DOPWELL, A. L.—b. 1899; clk., St. V., 1918; customs offr., 1923; ch. clk., G.P.O., 1930; ch. audit clk., 1933; contrlr., supp., and comp. authy., St. L., 1945; examr., acts., Grenada, 1947; dep. treas., 1948; acctnt.-gen., 1955-58.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1918 | clk. | St. Vincent | [1953, 1954, 1955, 1957, 1958, 1959] |
| 1 | 1923 | customs offr | St. Vincent *(inherited from previous clause)* | [1953, 1954, 1955, 1957, 1958, 1959] |
| 2 | 1930 | ch. clk., G.P.O | St. Vincent *(inherited from previous clause)* | [1953, 1954, 1955, 1957, 1958, 1959] |
| 3 | 1933 | ch. audit clk | St. Vincent *(inherited from previous clause)* | [1953, 1954, 1955, 1957, 1958, 1959] |
| 4 | 1945 | contrlr., supp., and comp. authy. | St. Lucia | [1953, 1954, 1955, 1957, 1958, 1959] |
| 5 | 1947 | examr., acts. | Grenada | [1953, 1954, 1955, 1957, 1958, 1959] |
| 6 | 1948 | dep. treas | Grenada *(inherited from previous clause)* | [1953, 1954, 1955, 1957, 1958, 1959] |
| 7 | 1955–1958 | acctnt.-gen | Grenada *(inherited from previous clause)* | [1953, 1954, 1955, 1957, 1958, 1959] |

## Candidate stint `Dopwell, A. L___Windward Islands___1922`

- Staff-list name: **Dopwell, A. L** | colony: **Windward Islands** | listed 1922–1923 | editions [1922, 1923]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1922 | A. Dopwell | Second Clerk | Postal Department | — | — |
| 1923 | A. Dopwell | Second Clerk | Postal Department | — | — |

### Deterministic checks: `dopwell_a-l_b1899` vs `Dopwell, A. L___Windward Islands___1922`

- [PASS] surname_gate: bio 'DOPWELL' vs stint 'Dopwell, A. L' (exact)
- [PASS] initials: bio ['A', 'L'] ~ stint ['A', 'L']
- [PASS] age_gate: stint starts 1922, birth 1899 (age 23)
- [FAIL] colony: no placed event resolves to 'Windward Islands'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1922-1923
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Dopwell, A. L___Windward Islands___1937`

- Staff-list name: **Dopwell, A. L** | colony: **Windward Islands** | listed 1937–1939 | editions [1937, 1939]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1937 | A. L. Dopwell | Audit Clerk | Audit | — | — |
| 1939 | A. L. Dopwell | Audit Clerk | Audit | — | — |

### Deterministic checks: `dopwell_a-l_b1899` vs `Dopwell, A. L___Windward Islands___1937`

- [PASS] surname_gate: bio 'DOPWELL' vs stint 'Dopwell, A. L' (exact)
- [PASS] initials: bio ['A', 'L'] ~ stint ['A', 'L']
- [PASS] age_gate: stint starts 1937, birth 1899 (age 38)
- [FAIL] colony: no placed event resolves to 'Windward Islands'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1937-1939
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

