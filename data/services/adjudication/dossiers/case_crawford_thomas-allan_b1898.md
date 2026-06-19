<!-- {"case_id": "case_crawford_thomas-allan_b1898", "bio_ids": ["crawford_thomas-allan_b1898"], "stint_ids": ["Crawford, A___Togoland___1920", "Crawford, T___Palestine___1921"]} -->
# Dossier case_crawford_thomas-allan_b1898

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 47 official(s) with this surname in the graph's staff lists; 20 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `crawford_thomas-allan_b1898`

- Printed name: **CRAWFORD, Thomas Allan**
- Birth year: 1898 (attested in editions [1948, 1949, 1950, 1951])
- Appears in editions: [1948, 1949, 1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1948-L32012.v` — printed in editions [1948, 1949, 1950, 1951]:**

> CRAWFORD, Thomas Allan.—b. 1898; ed. Atkinson Road, Newcastle-on-Tyne Sec. Sch.; traff. inspr., gr. II., rlws., Nig., 1927; gr. I., 1933; asst. traff. offr., 1938; senr., 1945; dist. traff. supt., 1947.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1927 | traff. inspr., gr. II., rlws. | Nigeria | [1948, 1949, 1950, 1951] |
| 1 | 1933 | gr. I | Nigeria *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |
| 2 | 1938 | asst. traff. offr | Nigeria *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |
| 3 | 1945 | senr | Nigeria *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |
| 4 | 1947 | dist. traff. supt | Nigeria *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |

## Candidate stint `Crawford, A___Togoland___1920`

- Staff-list name: **Crawford, A** | colony: **Togoland** | listed 1920–1921 | editions [1920, 1921]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1920 | A. Crawford | Medical Officer | Medical Department | — | — |
| 1921 | A. Crawford | Dental Surgeon | Dental Branch | — | — |

### Deterministic checks: `crawford_thomas-allan_b1898` vs `Crawford, A___Togoland___1920`

- [PASS] surname_gate: bio 'CRAWFORD' vs stint 'Crawford, A' (exact)
- [PASS] initials: bio ['T', 'A'] ~ stint ['A']
- [PASS] age_gate: stint starts 1920, birth 1898 (age 22)
- [FAIL] colony: no placed event resolves to 'Togoland'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1920-1921
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Crawford, T___Palestine___1921`

- Staff-list name: **Crawford, T** | colony: **Palestine** | listed 1921–1929 | editions [1921, 1923, 1925, 1927, 1928, 1929]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1921 | T. Crawford | Paymaster | Palestine Railways | — | Captain |
| 1923 | T. Crawford | Chief Cashier | Palestine Railways | — | — |
| 1925 | T. Crawford | Chief Cashier | Palestine Railways | — | — |
| 1927 | T. Crawford | Cashier | Palestine Railways | — | — |
| 1928 | T. Crawford | Cashier | Palestine Railways | — | — |
| 1929 | T. Crawford | Cashier | Palestine Railways | — | — |

### Deterministic checks: `crawford_thomas-allan_b1898` vs `Crawford, T___Palestine___1921`

- [PASS] surname_gate: bio 'CRAWFORD' vs stint 'Crawford, T' (exact)
- [PASS] initials: bio ['T', 'A'] ~ stint ['T']
- [PASS] age_gate: stint starts 1921, birth 1898 (age 23)
- [FAIL] colony: no placed event resolves to 'Palestine'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1921-1929
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

