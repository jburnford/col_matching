<!-- {"case_id": "case_huggins_s-a_b1907", "bio_ids": ["huggins_s-a_b1907"], "stint_ids": ["Huggins, S. A___Trinidad and Tobago___1949"]} -->
# Dossier case_huggins_s-a_b1907

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 34 official(s) with this surname in the graph's staff lists; 13 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `huggins_s-a_b1907`

- Printed name: **HUGGINS, S. A**
- Birth year: 1907 (attested in editions [1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966])
- Appears in editions: [1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1953-L17828.v` — printed in editions [1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966]:**

> HUGGINS, S. A.—b. 1907; ed. Iere Cent. High Sch., and Queen's Royal Coll.; dep. registr.-gen., Trin., 1938; registr.-gen., 1946; dep. crown solr., 1949; crown solr., admnr. gen. and public trustee, 1954. (T'dad Govt. service.)

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1938 | dep. registr.-gen. | Trinidad | [1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 1 | 1946 | registr.-gen | Trinidad *(inherited from previous clause)* | [1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 2 | 1949 | dep. crown solr | Trinidad *(inherited from previous clause)* | [1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 3 | 1954 | crown solr., admnr. gen. and public trustee | Trinidad *(inherited from previous clause)* | [1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |

## Candidate stint `Huggins, S. A___Trinidad and Tobago___1949`

- Staff-list name: **Huggins, S. A** | colony: **Trinidad and Tobago** | listed 1949–1962 | editions [1949, 1953, 1954, 1962]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | S. A. Huggins | Registrar General | REGISTRAR GENERAL | — | — |
| 1953 | S. A. Huggins | Deputy Crown Solicitor | Civil Establishment | — | — |
| 1954 | S. A. Huggins | Deputy Crown Solicitor | Civil Establishment | — | — |
| 1962 | S. A. Huggins | Crown Solicitor, Administrator-General and Public Trustee | Civil Establishment | — | — |

### Deterministic checks: `huggins_s-a_b1907` vs `Huggins, S. A___Trinidad and Tobago___1949`

- [PASS] surname_gate: bio 'HUGGINS' vs stint 'Huggins, S. A' (exact)
- [PASS] initials: bio ['S', 'A'] ~ stint ['S', 'A']
- [PASS] age_gate: stint starts 1949, birth 1907 (age 42)
- [FAIL] colony: no placed event resolves to 'Trinidad and Tobago'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1949-1962
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

