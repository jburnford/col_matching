<!-- {"case_id": "case_rienzi_adrian-cola_b1905", "bio_ids": ["rienzi_adrian-cola_b1905"], "stint_ids": ["Rienzi, A. C___Trinidad and Tobago___1953"]} -->
# Dossier case_rienzi_adrian-cola_b1905

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `rienzi_adrian-cola_b1905`

- Printed name: **RIENZI, Adrian Cola**
- Birth year: 1905 (attested in editions [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964])
- Appears in editions: [1948, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964]

### Verbatim printed entry text (OCR)

**Version `col1956-L23788.v` — printed in editions [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964]:**

> RIENZI, A. C.—b. 1905; ed. Naparima Coll., Trinity Coll., Dublin; barrister-at-law, Middle Temple; 2nd crown counsel, Trin., 1944; cr. coun., 1949; senr., 1951. (T'dad Govt. service.)

**Version `col1948-L35511.v` — printed in editions [1948]:**

> RIENZI, Adrian Cola, B.A. (Cen.), LL.B. (Chicago Sch. of Law).—b. 1905; ed. Naparima Coll., Trinidad, Trinity Coll., Dublin, barrister-at-law, Middle Temple, Central Univ. Chicago Sch. of Law; 2nd crown coun., Trin., 1944.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1944 | 2nd crown counsel | Trinidad | [1948, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964] |
| 1 | 1949 | cr. coun | Trinidad *(inherited from previous clause)* | [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964] |
| 2 | 1951 | senr | Trinidad *(inherited from previous clause)* | [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964] |

## Candidate stint `Rienzi, A. C___Trinidad and Tobago___1953`

- Staff-list name: **Rienzi, A. C** | colony: **Trinidad and Tobago** | listed 1953–1954 | editions [1953, 1954]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1953 | A. C. Rienzi | Crown Counsels | Civil Establishment | — | — |
| 1954 | A. C. Rienzi | Crown Counsel | Civil Establishment | — | — |

### Deterministic checks: `rienzi_adrian-cola_b1905` vs `Rienzi, A. C___Trinidad and Tobago___1953`

- [PASS] surname_gate: bio 'RIENZI' vs stint 'Rienzi, A. C' (exact)
- [PASS] initials: bio ['A', 'C'] ~ stint ['A', 'C']
- [PASS] age_gate: stint starts 1953, birth 1905 (age 48)
- [FAIL] colony: no placed event resolves to 'Trinidad and Tobago'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1953-1954
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

