<!-- {"case_id": "case_juste_joseph-william_b1889", "bio_ids": ["juste_joseph-william_b1889"], "stint_ids": ["Juste, W___Mauritius___1914"]} -->
# Dossier case_juste_joseph-william_b1889

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `juste_joseph-william_b1889`

- Printed name: **JUSTE, Joseph William**
- Birth year: 1889 (attested in editions [1948])
- Appears in editions: [1948]

### Verbatim printed entry text (OCR)

**Version `col1948-L33756.v` — printed in editions [1948]:**

> JUSTE, Joseph William.—b. 1889; ed. Royal Coll., Mauritius; writer, Maur., 1912; clk., 1913; acctnt., postal dept., 1937; ch. clk. and acctnt., med. and health, 1940; asst. P.M.G., 1941.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1912 | writer | Mauritius | [1948] |
| 1 | 1913 | clk | Mauritius *(inherited from previous clause)* | [1948] |
| 2 | 1937 | acctnt., postal dept | Mauritius *(inherited from previous clause)* | [1948] |
| 3 | 1940 | ch. clk. and acctnt., med. and health | Mauritius *(inherited from previous clause)* | [1948] |
| 4 | 1941 | asst. P.M.G | Mauritius *(inherited from previous clause)* | [1948] |

## Candidate stint `Juste, W___Mauritius___1914`

- Staff-list name: **Juste, W** | colony: **Mauritius** | listed 1914–1931 | editions [1914, 1915, 1917, 1918, 1919, 1920, 1921, 1922, 1923, 1927, 1928, 1929, 1931]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1914 | W. Juste | 6th Class Clerk | Account Branch | — | — |
| 1915 | W. Juste | 6th Class Clerk | Account Branch | — | — |
| 1917 | W. Juste | 6th Class Clerks | Examination of Accounts Branch | — | — |
| 1918 | W. Juste | 6th Class Clerk | Examination of Accounts Branch | — | — |
| 1919 | W. Juste | 5th Class Clerk | Clerical Staff | — | — |
| 1920 | W. Juste | 5th Class Clerk | Clerical Staff | — | — |
| 1921 | W. Juste | 5th Class Clerk | Clerical Staff | — | — |
| 1922 | W. Juste | 5th Class Clerk | Clerical Staff | — | — |
| 1923 | W. Juste | 5th Class Clerk | Clerical Staff | — | — |
| 1927 | W. Juste | 4th Class Clerk | General Branch | — | — |
| 1928 | W. Juste | 4th Class Clerk | General Branch | — | — |
| 1929 | W. Juste | 4th Class Clerks | General Branch | — | — |
| 1931 | W. Juste | 4th Class Clerk | General Branch | — | — |

### Deterministic checks: `juste_joseph-william_b1889` vs `Juste, W___Mauritius___1914`

- [PASS] surname_gate: bio 'JUSTE' vs stint 'Juste, W' (exact)
- [PASS] initials: bio ['J', 'W'] ~ stint ['W']
- [PASS] age_gate: stint starts 1914, birth 1889 (age 25)
- [PASS] colony: 5 placed event(s) resolve to 'Mauritius'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1914-1931
- [FAIL] position_sim: best 33 vs bar 60: 'clk' ~ '6th Class Clerk'
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

