<!-- {"case_id": "case_de-la-bastide_k-p_b1908", "bio_ids": ["de-la-bastide_k-p_b1908"], "stint_ids": ["de la Bastide, K. P___Trinidad and Tobago___1949"]} -->
# Dossier case_de-la-bastide_k-p_b1908

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 7 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `de-la-bastide_k-p_b1908`

- Printed name: **De LA BASTIDE, K. P**
- Birth year: 1908 (attested in editions [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964])
- Appears in editions: [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964]

### Verbatim printed entry text (OCR)

**Version `col1956-L20790.v` — printed in editions [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964]:**

> De LA BASTIDE, K. P.—b. 1908; ed. St. Mary's Coll., Port of Spain, and Stonyhurst Coll.; barrister-at-law, Gray's Inn; mag., Trin., 1945; junr. cr. coun., Trin., 1950; senr., 1951; asst. to atty.-gen., 1954; puisne judge, 1958. (T'dad Govt. service.)

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1945 | mag. | Trinidad | [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964] |
| 1 | 1950 | junr. cr. coun. | Trinidad | [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964] |
| 2 | 1951 | senr | Trinidad *(inherited from previous clause)* | [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964] |
| 3 | 1954 | asst. to atty.-gen | Trinidad *(inherited from previous clause)* | [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964] |
| 4 | 1958 | puisne judge | Trinidad *(inherited from previous clause)* | [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964] |

## Candidate stint `de la Bastide, K. P___Trinidad and Tobago___1949`

- Staff-list name: **de la Bastide, K. P** | colony: **Trinidad and Tobago** | listed 1949–1962 | editions [1949, 1953, 1954, 1962]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | K. de la Bastide | Magistrates | Judicial | — | — |
| 1953 | K. P. de la Bastide | Crown Counsels | Civil Establishment | — | — |
| 1954 | K. P. de la Bastide | Crown Counsel | Civil Establishment | — | — |
| 1962 | K. P. de la Bastide | Puisne Judge | Judiciary | — | — |

### Deterministic checks: `de-la-bastide_k-p_b1908` vs `de la Bastide, K. P___Trinidad and Tobago___1949`

- [PASS] surname_gate: bio 'De LA BASTIDE' vs stint 'de la Bastide, K. P' (exact)
- [PASS] initials: bio ['K', 'P'] ~ stint ['K', 'P']
- [PASS] age_gate: stint starts 1949, birth 1908 (age 41)
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

