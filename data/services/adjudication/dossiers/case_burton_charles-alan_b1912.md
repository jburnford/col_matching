<!-- {"case_id": "case_burton_charles-alan_b1912", "bio_ids": ["burton_charles-alan_b1912"], "stint_ids": ["Burton, C. A___Barbados___1954"]} -->
# Dossier case_burton_charles-alan_b1912

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 38 official(s) with this surname in the graph's staff lists; 18 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Burton, C. A___Barbados___1954` is also gate-compatible with biography(ies) outside this case: ['burton_carlyle-archibald_b1921'] (already linked elsewhere or filtered).

## Biography `burton_charles-alan_b1912`

- Printed name: **BURTON, Charles Alan**
- Birth year: 1912 (attested in editions [1958, 1959, 1960, 1961, 1962, 1963])
- Appears in editions: [1948, 1958, 1959, 1960, 1961, 1962, 1963]

### Verbatim printed entry text (OCR)

**Version `col1958-L21057.v` — printed in editions [1958, 1959, 1960, 1961, 1962, 1963]:**

> BURTON, Charles Alan—b. 1912; ed. Repton Sch. and St. John's Coll., Camb.; magistrate, B. Guiana, 1945; crown coun., 1949; Nig., 1952; senr. crown coun., 1953; atty.-gen., Barb., 1957.

**Version `col1948-L31532.v` — printed in editions [1948]:**

> BURTON, Charles Alan.—b. 1912; ed. Repton Sch. and St. John's Coll., Cambridge, B.A. (Cantab.); barrister-at-law; mag., Br. Guiana, 1945.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1945 | magistrate, B. Guiana | — | [1958, 1959, 1960, 1961, 1962, 1963] |
| 1 | 1945 | mag. | British Guiana | [1948] |
| 2 | 1949 | crown coun | — | [1958, 1959, 1960, 1961, 1962, 1963] |
| 3 | 1952 | crown coun | Nigeria | [1958, 1959, 1960, 1961, 1962, 1963] |
| 4 | 1953 | senr. crown coun | Nigeria *(inherited from previous clause)* | [1958, 1959, 1960, 1961, 1962, 1963] |
| 5 | 1957 | atty.-gen. | Barbados | [1958, 1959, 1960, 1961, 1962, 1963] |

## Candidate stint `Burton, C. A___Barbados___1954`

- Staff-list name: **Burton, C. A** | colony: **Barbados** | listed 1954–1965 | editions [1954, 1955, 1956, 1957, 1963, 1964, 1965]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1954 | C. A. Burton | Librarian, Public Library | Civil Establishment | — | — |
| 1955 | C. A. Burton | Public Librarian | Civil Establishment | — | — |
| 1956 | C. A. Burton | Public Librarian | Civil Establishment | — | — |
| 1957 | C. A. Burton | Public Librarian | Civil Establishment | — | — |
| 1963 | C. A. Burton | Permanent Secretary | Civil Establishment | — | — |
| 1964 | C. A. Burton | Permanent Secretary | Civil Establishment | — | — |
| 1965 | C. A. Burton | Permanent Secretary | Civil Establishment | — | — |

### Deterministic checks: `burton_charles-alan_b1912` vs `Burton, C. A___Barbados___1954`

- [PASS] surname_gate: bio 'BURTON' vs stint 'Burton, C. A' (exact)
- [PASS] initials: bio ['C', 'A'] ~ stint ['C', 'A']
- [PASS] age_gate: stint starts 1954, birth 1912 (age 42)
- [PASS] colony: 1 placed event(s) resolve to 'Barbados'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1954-1965
- [FAIL] position_sim: best 31 vs bar 60: 'atty.-gen.' ~ 'Permanent Secretary'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

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

