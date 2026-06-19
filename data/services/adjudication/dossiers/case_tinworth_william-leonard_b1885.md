<!-- {"case_id": "case_tinworth_william-leonard_b1885", "bio_ids": ["tinworth_william-leonard_b1885"], "stint_ids": ["Ainsworth, L___Australia___1918"]} -->
# Dossier case_tinworth_william-leonard_b1885

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 5 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `tinworth_william-leonard_b1885`

- Printed name: **TINWORTH, WILLIAM LEONARD**
- Birth year: 1885 (attested in editions [1934, 1935, 1937, 1939, 1940])
- Appears in editions: [1934, 1935, 1936, 1937, 1939, 1940]

### Verbatim printed entry text (OCR)

**Version `col1934-L63569.v` — printed in editions [1934, 1935, 1937, 1939, 1940]:**

> TINWORTH, WILLIAM LEONARD, A.M.Inst.T.—B. 1885; mil. serv., India and Mesopotamia, 1917-19; assr. acctnt., F.M.S. rlyas., 1921; ag. dep. acctnt., 1926, 1929 and 1930; ag. acctnt., pub. wks. dept., 1929; dep. ch. acctnt., Tanganyika rlyas., 1931; ag. ch. acctnt., 1933; ch. acctnt., 1936; ag. gen. man., 1938.

**Version `col1936-L65152.v` — printed in editions [1936]:**

> TINTWORTH, WILLIAM LEONARD, A.M.Inst.T.—B. 1885; mil. surv., India and Mesopotamia, 1917-19; asst. acctnt., F.M.S. riya, 1921; ag. dep. acctnt., 1926, 1929 and 1930; ag. acctnt., pub. wks. dept., 1929; dep. ch. acctnt., Tanganyika rly., 1931; ag. ch. acctnt., 1933.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1917–1919 | mil. serv. | India and Mesopotamia | [1934, 1935, 1936, 1937, 1939, 1940] |
| 1 | 1921–1921 | assr. acctnt. | Federated Malay States | [1934, 1935, 1936, 1937, 1939, 1940] |
| 2 | 1926–1930 | ag. dep. acctnt. | — | [1934, 1935, 1936, 1937, 1939, 1940] |
| 3 | 1929–1929 | ag. acctnt., pub. wks. dept. | — | [1934, 1935, 1936, 1937, 1939, 1940] |
| 4 | 1931–1931 | dep. ch. acctnt. | Tanganyika | [1934, 1935, 1936, 1937, 1939, 1940] |
| 5 | 1933–1933 | ag. ch. acctnt. | — | [1934, 1935, 1936, 1937, 1939, 1940] |
| 6 | 1936–1936 | ch. acctnt. | — | [1934, 1935, 1937, 1939, 1940] |
| 7 | 1938–1938 | ag. gen. man. | — | [1934, 1935, 1937, 1939, 1940] |

## Candidate stint `Ainsworth, L___Australia___1918`

- Staff-list name: **Ainsworth, L** | colony: **Australia** | listed 1918–1927 | editions [1918, 1927]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1918 | L. Ainsworth | Assistant | Home Affairs' Department | — | — |
| 1927 | L. Ainsworth | Divisional Returning Officer | Commonwealth Departments in Tasmania | — | — |

### Deterministic checks: `tinworth_william-leonard_b1885` vs `Ainsworth, L___Australia___1918`

- [PASS] surname_gate: bio 'TINWORTH' vs stint 'Ainsworth, L' (fuzzy:2)
- [PASS] initials: bio ['W', 'L'] ~ stint ['L']
- [PASS] age_gate: stint starts 1918, birth 1885 (age 33)
- [FAIL] colony: no placed event resolves to 'Australia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1918-1927
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

