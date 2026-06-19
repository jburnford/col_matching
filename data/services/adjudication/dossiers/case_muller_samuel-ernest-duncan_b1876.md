<!-- {"case_id": "case_muller_samuel-ernest-duncan_b1876", "bio_ids": ["muller_samuel-ernest-duncan_b1876"], "stint_ids": ["Muller, S. E. D___Ceylon___1921"]} -->
# Dossier case_muller_samuel-ernest-duncan_b1876

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 23 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `muller_samuel-ernest-duncan_b1876`

- Printed name: **MULLER, SAMUEL ERNEST DUNCAN**
- Birth year: 1876 (attested in editions [1930])
- Appears in editions: [1922, 1923, 1925, 1930]

### Verbatim printed entry text (OCR)

**Version `col1930-L67014.v` — printed in editions [1930]:**

> MULLER, SAMUEL ERNEST DUNCAN.—B. 1876; cls. V, Ceylon civ. serv., Jan., 1921; addnl. acct. acct., gen. treas., Jan., 1921; acct., Colombo port commn., Feb., 1923; ditto, P.W.D., Oct., 1925.

**Version `col1925-L58094.v` — printed in editions [1925]:**

> MULLER, SAMUEL ERNEST DUNCAN.—cls. V, Ceylon civ. serv., Jan., 1921; addl. acct., gen. treas., Jan., 1921; acct. of port coman., Feb., 1923.

**Version `col1922-L54940.v` — printed in editions [1922, 1923]:**

> MULLER, SAMUEL ERNEST DUNCAN.—B. 1876; cls. V, Caylon civ. serv., Jan., 1921; addnl. asst. acctnt.-gen., treasy., Jan., 1921.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1921 | cls. V, Ceylon civ. serv | Ceylon | [1922, 1923, 1925, 1930] |
| 1 | 1921 | addnl. asst. acctnt.-gen., treasy | — | [1922, 1923] |
| 2 | 1923 | acct., Colombo port commn | Ceylon *(inherited from previous clause)* | [1925, 1930] |
| 3 | 1925 | ditto, P.W.D | Ceylon *(inherited from previous clause)* | [1930] |

## Candidate stint `Muller, S. E. D___Ceylon___1921`

- Staff-list name: **Muller, S. E. D** | colony: **Ceylon** | listed 1921–1929 | editions [1921, 1922, 1925, 1927, 1929]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1921 | S. E. Muller | Additional Assistant Accountant | Civil Establishment | — | — |
| 1922 | S. E. Muller | Additional Assistant Accountant | Civil Establishment | — | — |
| 1925 | S. E. D. Muller | Accountant | Colombo Port Commission | — | — |
| 1927 | S. E. D. Muller | Financial Assistant and Accountant | Public Works Department | — | — |
| 1929 | S. E. D. Muller | Financial Assistant and Accountant | Public Works Department | — | — |

### Deterministic checks: `muller_samuel-ernest-duncan_b1876` vs `Muller, S. E. D___Ceylon___1921`

- [PASS] surname_gate: bio 'MULLER' vs stint 'Muller, S. E. D' (exact)
- [PASS] initials: bio ['S', 'E', 'D'] ~ stint ['S', 'E', 'D']
- [PASS] age_gate: stint starts 1921, birth 1876 (age 45)
- [PASS] colony: 3 placed event(s) resolve to 'Ceylon'
- [PASS] tenure_overlap: 3 event tenure(s) overlap stint years 1921-1929
- [FAIL] position_sim: best 37 vs bar 60: 'acct., Colombo port commn' ~ 'Additional Assistant Accountant'
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

