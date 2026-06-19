<!-- {"case_id": "case_markowski_b_b1908", "bio_ids": ["markowski_b_b1908"], "stint_ids": ["Markowski, B___British Honduras___1953"]} -->
# Dossier case_markowski_b_b1908

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['markowski_b_b1908'] carry a single initial only — the namesake trap applies.

## Biography `markowski_b_b1908`

- Printed name: **MARKOWSKI, B.**
- Birth year: 1908 (attested in editions [1954, 1956, 1957, 1958, 1959, 1960, 1961])
- Honours: O.B.E. (1962)
- Appears in editions: [1954, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965]

### Verbatim printed entry text (OCR)

**Version `col1954-L21498.v` — printed in editions [1954, 1956, 1957, 1958, 1959, 1960, 1961]:**

> MARKOWSKI, B.—b. 1908; ed. Warsaw Univ.; Polish navy, 1933-47, surg. cmdr.; residt. surg., B. Hond., 1951; surg. spec., 1952; author of articles in various med. journals.

**Version `col1962-L24243.v` — printed in editions [1962, 1963, 1964, 1965]:**

> MARKOWSKI, B., O.B.E. (1962).—b. 1908; ed. Warsaw Univ.; Polish navy, and R.N., 1939-47, surg. cmdr.; resdt. surg., B. Hond., 1951; surg. spec., 1952-64.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1933–1947 | surg. cmdr. | — | [1954, 1956, 1957, 1958, 1959, 1960, 1961] |
| 1 | 1939–1947 | surg. cmdr. | — | [1962, 1963, 1964, 1965] |
| 2 | 1951–1951 | residt. surg. | British Honduras | [1954, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965] |
| 3 | 1952–1952 | surg. spec. | — | [1954, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965] |

## Candidate stint `Markowski, B___British Honduras___1953`

- Staff-list name: **Markowski, B** | colony: **British Honduras** | listed 1953–1964 | editions [1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1953 | B. Markowski | Surgeon Specialist | Civil Establishment | — | — |
| 1954 | B. Markowski | Surgeon Specialist | Civil Establishment | — | — |
| 1955 | B. Markowski | Surgeon Specialist | Civil Establishment | — | — |
| 1956 | B. Markowski | Surgeon Specialist | Civil Establishment | — | — |
| 1957 | B. Markowski | Surgeon Specialist | Civil Establishment | — | — |
| 1958 | B. Markowski | Surgeon Specialist | Civil Establishment | — | — |
| 1959 | B. Markowski | Surgeon Specialist | Civil Establishment | — | — |
| 1960 | B. Markowski | Surgeon Specialist | Civil Establishment | — | — |
| 1961 | B. Markowski | Surgeon Specialist | Law Officers | — | — |
| 1962 | B. Markowski | Surgeon Specialist | Civil Establishment | — | — |
| 1963 | B. Markowski | Surgeon Specialist | Civil Establishment | — | — |
| 1964 | B. Markowski | Surgeon Specialist | Civil Establishment | — | — |

### Deterministic checks: `markowski_b_b1908` vs `Markowski, B___British Honduras___1953`

- [PASS] surname_gate: bio 'MARKOWSKI' vs stint 'Markowski, B' (exact)
- [PASS] initials: bio ['B'] ~ stint ['B']
- [PASS] age_gate: stint starts 1953, birth 1908 (age 45)
- [PASS] colony: 1 placed event(s) resolve to 'British Honduras'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1953-1964
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

