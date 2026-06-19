<!-- {"case_id": "case_borden_john-william_b1856", "bio_ids": ["borden_john-william_b1856"], "stint_ids": ["Borden, J. W___Canada___1899"]} -->
# Dossier case_borden_john-william_b1856

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 9 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `borden_john-william_b1856`

- Printed name: **BORDEN, JOHN WILLIAM**
- Birth year: 1856 (attested in editions [1910, 1911, 1912, 1913, 1914, 1915, 1918])
- Appears in editions: [1910, 1911, 1912, 1913, 1914, 1915, 1917, 1918]

### Verbatim printed entry text (OCR)

**Version `col1910-L44399.v` — printed in editions [1910, 1911, 1912, 1913, 1914, 1915, 1918]:**

> BORDEN, JOHN WILLIAM.—B. 1856; acctnt. dep. of mil. and def., Canada, 1897; paymr.-gen., mil. forces, 1906; civil mem. of militia council.

**Version `col1917-L47783.v` — printed in editions [1917]:**

> BORDEEN, JOHN WILLIAM.—B. 1856; acctnt. dep. of mil. and def., Canada, 1897; paymr.-gen., mil. forces, 1906; civil mem. of militia council.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1897 | acctnt. dep. of mil. and def. | Canada | [1910, 1911, 1912, 1913, 1914, 1915, 1917, 1918] |
| 1 | 1906 | paymr.-gen., mil. forces | Canada *(inherited from previous clause)* | [1910, 1911, 1912, 1913, 1914, 1915, 1917, 1918] |

## Candidate stint `Borden, J. W___Canada___1899`

- Staff-list name: **Borden, J. W** | colony: **Canada** | listed 1899–1918 | editions [1899, 1900, 1905, 1906, 1907, 1908, 1912, 1913, 1914, 1915, 1917, 1918]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1899 | J. W. Borden | Accountant | Department of Militia and Defence | — | — |
| 1900 | J. W. Borden | Accountant | Militia and Defence | — | — |
| 1905 | J. W. Borden | Chief Clerk, Accountant | Department of Militia and Defence | — | — |
| 1906 | J. W. Borden | Chief Clerk, Accountant | Department of Militia and Defence | — | — |
| 1907 | J. W. Borden | Chief Clerk, Accountant | Militia and Defence | — | — |
| 1908 | J. W. Borden | Chief Clerk, Accountant | Department of Militia and Defence | — | — |
| 1912 | J. W. Borden | Accountant and Paymaster-General | Department of Militia and Defence | — | — |
| 1913 | J. W. Borden | Accountant and Paymaster-General | Militia and Defence | — | — |
| 1914 | J. W. Borden | Accountant and Paymaster-General | Department of Militia and Defence | — | — |
| 1915 | J. W. Borden | Accountant and Paymaster-General | Department of Militia and Defence | — | — |
| 1917 | J. W. Borden | Accountant and Paymaster-General | Department of Militia and Defence | — | — |
| 1918 | J. W. Borden | Accountant and Paymaster-General | Department of Militia and Defence | — | — |

### Deterministic checks: `borden_john-william_b1856` vs `Borden, J. W___Canada___1899`

- [PASS] surname_gate: bio 'BORDEN' vs stint 'Borden, J. W' (exact)
- [PASS] initials: bio ['J', 'W'] ~ stint ['J', 'W']
- [PASS] age_gate: stint starts 1899, birth 1856 (age 43)
- [PASS] colony: 2 placed event(s) resolve to 'Canada'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1899-1918
- [FAIL] position_sim: best 51 vs bar 60: 'acctnt. dep. of mil. and def.' ~ 'Chief Clerk, Accountant'
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

