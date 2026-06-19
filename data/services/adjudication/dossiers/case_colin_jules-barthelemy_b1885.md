<!-- {"case_id": "case_colin_jules-barthelemy_b1885", "bio_ids": ["colin_jules-barthelemy_b1885"], "stint_ids": ["Colin, J. B___Mauritius___1917"]} -->
# Dossier case_colin_jules-barthelemy_b1885

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 6 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `colin_jules-barthelemy_b1885`

- Printed name: **COLIN, Jules Barthelemy**
- Birth year: 1885 (attested in editions [1948, 1949])
- Appears in editions: [1948, 1949]

### Verbatim printed entry text (OCR)

**Version `col1948-L31855.v` — printed in editions [1948, 1949]:**

> COLIN, Jules Barthelemy.—b. 1885; ed. Royal Coll., Mauritius, Lincoln's Inn, barrister-at-law; on mil. serv. 1917–18; copyist, Maur., 1903; writer, 1906; inspec. of distilleries, 1906; clk., 1912; mag. for Maur. and Rodrigues, 1925.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1903 | copyist | Mauritius | [1948, 1949] |
| 1 | 1906 | writer | Mauritius *(inherited from previous clause)* | [1948, 1949] |
| 2 | 1912 | clk | Mauritius *(inherited from previous clause)* | [1948, 1949] |
| 3 | 1925 | mag. for Maur. and Rodrigues | Mauritius *(inherited from previous clause)* | [1948, 1949] |

## Candidate stint `Colin, J. B___Mauritius___1917`

- Staff-list name: **Colin, J. B** | colony: **Mauritius** | listed 1917–1939 | editions [1917, 1918, 1919, 1920, 1921, 1922, 1923, 1927, 1928, 1929, 1931, 1932, 1936, 1937, 1939]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1917 | J. B. Colin | 3rd Class Clerk | Account Branch | — | — |
| 1918 | J. B. Colin | 3rd Class Clerk | Account Branch | — | — |
| 1919 | J. B. Colin | 3rd Class Clerk | Account Branch | — | — |
| 1920 | J. B. Colin | 3rd Class Clerk | Account Branch | — | — |
| 1921 | J. B. Colin | District Cashiers | General Branch | — | — |
| 1922 | J. B. Colin | District Cashiers | General Branch | — | — |
| 1923 | J. B. Colin | 3rd Class Clerks | General Branch | — | — |
| 1927 | J. B. Colin | Magistrate | Electrical Department | — | — |
| 1928 | J. B. Colin | Magistrate | RODRIGUES | — | — |
| 1929 | J. B. Colin | Magistrate | RODRIGUES | — | — |
| 1931 | J. B. Colin | District and Stipendiary Magistrate | District and Stipendiary Magistracies | — | — |
| 1932 | J. B. Colin | District and Stipendiary Magistrate | District and Stipendiary Magistracies. | — | — |
| 1936 | J. B. Colin | Magistrate | District and Stipendiary Magistracies | — | — |
| 1937 | J. B. Colin | — | District and Stipendiary Magistracies | — | — |
| 1939 | J. B. Colin | Magistrate | District and Stipendiary Magistracies | — | — |

### Deterministic checks: `colin_jules-barthelemy_b1885` vs `Colin, J. B___Mauritius___1917`

- [PASS] surname_gate: bio 'COLIN' vs stint 'Colin, J. B' (exact)
- [PASS] initials: bio ['J', 'B'] ~ stint ['J', 'B']
- [PASS] age_gate: stint starts 1917, birth 1885 (age 32)
- [PASS] colony: 4 placed event(s) resolve to 'Mauritius'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1917-1939
- [FAIL] position_sim: best 43 vs bar 60: 'mag. for Maur. and Rodrigues' ~ 'District and Stipendiary Magistrate'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: ALL supporting events inherit their place from an earlier clause — weak evidence

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

