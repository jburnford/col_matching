<!-- {"case_id": "case_oxford_frederic-charles_b1899", "bio_ids": ["oxford_frederic-charles_b1899"], "stint_ids": ["Oxford, F. C___Kenya___1927"]} -->
# Dossier case_oxford_frederic-charles_b1899

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `oxford_frederic-charles_b1899`

- Printed name: **OXFORD, Frederic Charles**
- Birth year: 1899 (attested in editions [1957, 1958, 1959])
- Honours: I.S.O (1957)
- Appears in editions: [1948, 1949, 1950, 1951, 1957, 1958, 1959]

### Verbatim printed entry text (OCR)

**Version `col1957-L26149.v` — printed in editions [1957, 1958, 1959]:**

> OXFORD, F. C., I.S.O. (1957)—b. 1899; ed. King Edward Gram. Sch., Burton on Trent; mil. serv., 1917-19; accts. clk., E.A. posts and tels. dept., 1925; acctnt., 1937; dep. chief acctnt., 1944; senr. acctnt., 1949; accts. offr., 1953-58.

**Version `col1948-L35076.v` — printed in editions [1948, 1949, 1950, 1951]:**

> OXFORD, Frederic Charles.—b. 1899; ed. King Edward Gram. Sch., Burton-on-Trent; on mil. serv., 1917-19; accts., clk., post and tels. dep., Ken. and Uga., 1925; acctnt., jt. postal serv., Ken., Uga. and T.T., 1937; dep. ch. acctnt. (later, posts and tels., E.A.), 1944.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1925 | accts. clk., E.A. posts and tels. dept | Kenya | [1948, 1949, 1950, 1951, 1957, 1958, 1959] |
| 1 | 1937 | acctnt | Uganda | [1948, 1949, 1950, 1951, 1957, 1958, 1959] |
| 2 | 1944 | dep. chief acctnt | Uganda *(inherited from previous clause)* | [1948, 1949, 1950, 1951, 1957, 1958, 1959] |
| 3 | 1949 | senr. acctnt | — | [1957, 1958, 1959] |
| 4 | 1953–1958 | accts. offr | — | [1957, 1958, 1959] |

## Candidate stint `Oxford, F. C___Kenya___1927`

- Staff-list name: **Oxford, F. C** | colony: **Kenya** | listed 1927–1930 | editions [1927, 1928, 1929, 1930]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1927 | F. C. Oxford | Accounts Clerks | Post and Telegraph Department | — | — |
| 1928 | F. C. Oxford | Accounts Clerks | Post and Telegraph Department | — | — |
| 1929 | F. C. Oxford | Accounts Clerks | Posts and Telegraphs Department | — | — |
| 1930 | F. C. Oxford | Accounts Clerks | Posts and Telegraphs Department | — | — |

### Deterministic checks: `oxford_frederic-charles_b1899` vs `Oxford, F. C___Kenya___1927`

- [PASS] surname_gate: bio 'OXFORD' vs stint 'Oxford, F. C' (exact)
- [PASS] initials: bio ['F', 'C'] ~ stint ['F', 'C']
- [PASS] age_gate: stint starts 1927, birth 1899 (age 28)
- [PASS] colony: 1 placed event(s) resolve to 'Kenya'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1927-1930
- [FAIL] position_sim: best 43 vs bar 60: 'accts. clk., E.A. posts and tels. dept' ~ 'Accounts Clerks'
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

