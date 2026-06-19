<!-- {"case_id": "case_robb_james-alexander_b1889", "bio_ids": ["robb_james-alexander_b1889"], "stint_ids": ["Robb, Alex___Cape of Good Hope___1905", "Robb, James Alexander___Canada___1919"]} -->
# Dossier case_robb_james-alexander_b1889

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 10 official(s) with this surname in the graph's staff lists; 4 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `robb_james-alexander_b1889`

- Printed name: **ROBB, JAMES ALEXANDER**
- Birth year: 1889 (attested in editions [1922, 1923, 1924, 1925, 1927, 1928, 1929])
- Appears in editions: [1922, 1923, 1924, 1925, 1927, 1928, 1929]

### Verbatim printed entry text (OCR)

**Version `col1922-L55717.v` — printed in editions [1922, 1923, 1924, 1925, 1927, 1928, 1929]:**

> ROBB, HON. JAMES ALEXANDER.—B. 1889; ed. at dist. schl. and Huntingdon Acad.; mayor of Valleyfield, 1906-10; el. to H.C., 1908, 1911, 1917 and 1921; min. of trade and commerce in King admstr., 29th Dec., 1921; min. of immigr. and colonisation, 1923; min. of finance and recvr.-gen., 5th Sept., 1925; min. of finance and recvr.-gen., Sept., 1925 to Sept., 1926.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1906–1910 | mayor | Valleyfield | [1922, 1923, 1924, 1925, 1927, 1928, 1929] |
| 1 | 1908–1921 | el. to H.C. | — | [1922, 1923, 1924, 1925, 1927, 1928, 1929] |
| 2 | 1921–1921 | min. of trade and commerce | — | [1922, 1923, 1924, 1925, 1927, 1928, 1929] |
| 3 | 1923–1923 | min. of immigr. and colonisation | — | [1922, 1923, 1924, 1925, 1927, 1928, 1929] |
| 4 | 1925–1925 | min. of finance and recvr.-gen. | — | [1922, 1923, 1924, 1925, 1927, 1928, 1929] |

## Candidate stint `Robb, Alex___Cape of Good Hope___1905`

- Staff-list name: **Robb, Alex** | colony: **Cape of Good Hope** | listed 1905–1909 | editions [1905, 1906, 1907, 1908, 1909]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1905 | A. A. Robb | Clerk | Administrative and Convict Branch | — | — |
| 1906 | A. A. Robb | Clerks | Administrative and Convict Branch | — | — |
| 1906 | A. J. Robb | Assistant General Manager | Railways | — | — |
| 1907 | A. J. Robb | Assistant General Manager | Railways | — | — |
| 1907 | A. A. Robb | Clerk | Administrative and Convict Branch | — | — |
| 1908 | A. J. Robb | Assistant General Manager | Railways | — | — |
| 1908 | A. A. Robb | Clerk | Administrative and Convict Branch | — | — |
| 1909 | A. A. Robb | Clerks | Administrative, Convict and Hospitals Branch | — | — |
| 1909 | A. J. Robb | Assistant General Manager | Railways | — | — |

### Deterministic checks: `robb_james-alexander_b1889` vs `Robb, Alex___Cape of Good Hope___1905`

- [PASS] surname_gate: bio 'ROBB' vs stint 'Robb, Alex' (exact)
- [PASS] initials: bio ['J', 'A'] ~ stint ['A']
- [PASS] age_gate: stint starts 1905, birth 1889 (age 16)
- [FAIL] colony: no placed event resolves to 'Cape of Good Hope'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1905-1909
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Robb, James Alexander___Canada___1919`

- Staff-list name: **Robb, James Alexander** | colony: **Canada** | listed 1919–1922 | editions [1919, 1922]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1919 | J. A. Robb | Member of Parliament | House of Commons | — | — |
| 1922 | James Alexander Robb | Minister of Trade and Commerce | Department of Trade and Commerce | — | — |
| 1922 | James Alexander Robb | Minister of Trade and Commerce | THE MINISTRY | — | — |

### Deterministic checks: `robb_james-alexander_b1889` vs `Robb, James Alexander___Canada___1919`

- [PASS] surname_gate: bio 'ROBB' vs stint 'Robb, James Alexander' (exact)
- [PASS] initials: bio ['J', 'A'] ~ stint ['J', 'A']
- [PASS] age_gate: stint starts 1919, birth 1889 (age 30)
- [FAIL] colony: no placed event resolves to 'Canada'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1919-1922
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

