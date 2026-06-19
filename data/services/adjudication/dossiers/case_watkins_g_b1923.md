<!-- {"case_id": "case_watkins_g_b1923", "bio_ids": ["watkins_g_b1923"], "stint_ids": ["Watkins, H. G___Kenya___1950"]} -->
# Dossier case_watkins_g_b1923

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 25 official(s) with this surname in the graph's staff lists; 11 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['watkins_g_b1923'] carry a single initial only — the namesake trap applies.

## Biography `watkins_g_b1923`

- Printed name: **WATKINS, G**
- Birth year: 1923 (attested in editions [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966])
- Appears in editions: [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1956-L24868.v` — printed in editions [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966]:**

> WATKINS, G.—b. 1923; ed. Swansea Gram. Sch., Univ. Coll. of N. Wales and Univ. Coll., Oxford; asst. consvr., forests, Tang., 1944; prin. of forest sch., 1951; senr. asst. consvr., Fiji, 1958; consvr., forests, 1964.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1944 | asst. consvr., forests | Tanganyika | [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 1 | 1951 | prin. of forest sch | Tanganyika *(inherited from previous clause)* | [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 2 | 1958 | senr. asst. consvr. | Fiji | [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 3 | 1964 | consvr., forests | Fiji *(inherited from previous clause)* | [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |

## Candidate stint `Watkins, H. G___Kenya___1950`

- Staff-list name: **Watkins, H. G** | colony: **Kenya** | listed 1950–1951 | editions [1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1950 | H. G. Watkins | Accountant | ACCOUNTANT GENERAL | — | — |
| 1951 | H. G. Watkins | Accountant | ACCOUNTANT GENERAL | — | — |

### Deterministic checks: `watkins_g_b1923` vs `Watkins, H. G___Kenya___1950`

- [PASS] surname_gate: bio 'WATKINS' vs stint 'Watkins, H. G' (exact)
- [PASS] initials: bio ['G'] ~ stint ['H', 'G']
- [PASS] age_gate: stint starts 1950, birth 1923 (age 27)
- [FAIL] colony: no placed event resolves to 'Kenya'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1950-1951
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

