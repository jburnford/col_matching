<!-- {"case_id": "case_pryde_john-miller_b1895", "bio_ids": ["pryde_john-miller_b1895"], "stint_ids": ["Pryde, J. M___Nigeria___1933"]} -->
# Dossier case_pryde_john-miller_b1895

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `pryde_john-miller_b1895`

- Printed name: **PRYDE, John Miller**
- Birth year: 1895 (attested in editions [1948, 1949, 1950, 1951])
- Appears in editions: [1948, 1949, 1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1948-L35353.v` — printed in editions [1948, 1949, 1950, 1951]:**

> PRYDE, John Miller, E.D. (mil.).—b. 1895; ed. Stirling High Sch., Stirling, Scotland; on mil. serv., 1915-19, lieut.; asst. acctnt., P.W.D., Nig., 1925; asst. treas., 1932; senr. acctnt., 1944; prin. acctnt., 1946.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1925 | asst. acctnt., P.W.D. | Nigeria | [1948, 1949, 1950, 1951] |
| 1 | 1932 | asst. treas | Nigeria *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |
| 2 | 1944 | senr. acctnt | Nigeria *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |
| 3 | 1946 | prin. acctnt | Nigeria *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |

## Candidate stint `Pryde, J. M___Nigeria___1933`

- Staff-list name: **Pryde, J. M** | colony: **Nigeria** | listed 1933–1939 | editions [1933, 1934, 1936, 1939]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1933 | J. M. Pryde | Assistant Treasurer and Treasury Assistant | Treasury | — | — |
| 1934 | J. M. Pryde | Assistant Treasurer | Treasury | — | — |
| 1936 | J. M. Pryde | Assistant Treasurers | Treasury | — | — |
| 1939 | J. M. Pryde | Accountant and Assistant Accountant | Accountant-General's Department | — | — |

### Deterministic checks: `pryde_john-miller_b1895` vs `Pryde, J. M___Nigeria___1933`

- [PASS] surname_gate: bio 'PRYDE' vs stint 'Pryde, J. M' (exact)
- [PASS] initials: bio ['J', 'M'] ~ stint ['J', 'M']
- [PASS] age_gate: stint starts 1933, birth 1895 (age 38)
- [PASS] colony: 4 placed event(s) resolve to 'Nigeria'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1933-1939
- [PASS] position_sim: best 69 vs bar 60: 'asst. treas' ~ 'Assistant Treasurer'
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

