<!-- {"case_id": "case_burke_i-w_b1897", "bio_ids": ["burke_i-w_b1897"], "stint_ids": ["Burke, William___Leeward Islands___1923"]} -->
# Dossier case_burke_i-w_b1897

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 30 official(s) with this surname in the graph's staff lists; 11 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `burke_i-w_b1897`

- Printed name: **BURKE, I. W**
- Birth year: 1897 (attested in editions [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964])
- Appears in editions: [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964]

### Verbatim printed entry text (OCR)

**Version `col1957-L21583.v` — printed in editions [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964]:**

> BURKE, I. W.—b. 1897; ed. Barb., and McGill and Glasgow Univs.; civil serv., 1939-46; med. offr. of health, Trin., 1953; M.O. gr. A, public health, 1954. (T'dad Govt. service.)

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1939–1946 | civil serv | — | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964] |
| 1 | 1953 | med. offr. of health | Trinidad | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964] |
| 2 | 1954 | M.O. gr. A, public health | Trinidad *(inherited from previous clause)* | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964] |

## Candidate stint `Burke, William___Leeward Islands___1923`

- Staff-list name: **Burke, William** | colony: **Leeward Islands** | listed 1923–1925 | editions [1923, 1924, 1925]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1923 | William Burke | Keeper, Leper Asylum | Lunatic and Leper Asylums | — | — |
| 1924 | William Burke | Keeper, Leper Asylum | Lunatic and Leper Asylums | — | — |
| 1925 | William Burke | Keeper, Leper Asylum | Lunatic and Leper Asylums | — | — |

### Deterministic checks: `burke_i-w_b1897` vs `Burke, William___Leeward Islands___1923`

- [PASS] surname_gate: bio 'BURKE' vs stint 'Burke, William' (exact)
- [PASS] initials: bio ['I', 'W'] ~ stint ['W']
- [PASS] age_gate: stint starts 1923, birth 1897 (age 26)
- [FAIL] colony: no placed event resolves to 'Leeward Islands'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1923-1925
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

