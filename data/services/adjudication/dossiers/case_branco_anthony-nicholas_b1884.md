<!-- {"case_id": "case_branco_anthony-nicholas_b1884", "bio_ids": ["branco_anthony-nicholas_b1884"], "stint_ids": ["Branco, A. N___Cyprus___1908", "Branco, A. N___Cyprus___1929"]} -->
# Dossier case_branco_anthony-nicholas_b1884

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `branco_anthony-nicholas_b1884`

- Printed name: **BRANCO, ANTHONY NICHOLAS**
- Birth year: 1884 (attested in editions [1935, 1936, 1939, 1940])
- Appears in editions: [1935, 1936, 1939, 1940]

### Verbatim printed entry text (OCR)

**Version `dol1935-L57140.v` — printed in editions [1935, 1936, 1939, 1940]:**

> BRANCO, ANTHONY NICHOLAS.—B. 1884; clk. secretariat, Cyprus, 1907; asst. regist. and interp., dist. ct., 1913; examr., accts., 1926; local asst. audr., 1927; ag. audr. for various periods, 1928-34.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1907 | clk. secretariat | Cyprus | [1935, 1936, 1939, 1940] |
| 1 | 1913 | asst. regist. and interp., dist. ct | Cyprus *(inherited from previous clause)* | [1935, 1936, 1939, 1940] |
| 2 | 1926 | examr., accts | Cyprus *(inherited from previous clause)* | [1935, 1936, 1939, 1940] |
| 3 | 1927 | local asst. audr | Cyprus *(inherited from previous clause)* | [1935, 1936, 1939, 1940] |
| 4 | 1928–1934 | ag. audr. for various periods | Cyprus *(inherited from previous clause)* | [1935, 1936, 1939, 1940] |

## Candidate stint `Branco, A. N___Cyprus___1908`

- Staff-list name: **Branco, A. N** | colony: **Cyprus** | listed 1908–1909 | editions [1908, 1909]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1908 | A. N. Branco | 5th Clerk | Office of the Chief Secretary to Government | — | — |
| 1909 | A. Branco | Clerk and Interpreter | Prison Department | — | — |

### Deterministic checks: `branco_anthony-nicholas_b1884` vs `Branco, A. N___Cyprus___1908`

- [PASS] surname_gate: bio 'BRANCO' vs stint 'Branco, A. N' (exact)
- [PASS] initials: bio ['A', 'N'] ~ stint ['A', 'N']
- [PASS] age_gate: stint starts 1908, birth 1884 (age 24)
- [PASS] colony: 5 placed event(s) resolve to 'Cyprus'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1908-1909
- [FAIL] position_sim: best 50 vs bar 60: 'clk. secretariat' ~ 'Clerk and Interpreter'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

## Candidate stint `Branco, A. N___Cyprus___1929`

- Staff-list name: **Branco, A. N** | colony: **Cyprus** | listed 1929–1939 | editions [1929, 1930, 1934, 1936, 1939]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1929 | A. N. Branco | Local Assistant Auditor | Audit Department | — | — |
| 1930 | A. N. Branco | Local Assistant Auditor | Audit Department | — | — |
| 1934 | A. N. Branco | Local Assistant Auditor | Audit Department | — | — |
| 1936 | A. N. Branco | Local Assistant Auditor | Audit Department | — | — |
| 1939 | A. N. Branco | Local Assistant Auditor | Audit Department | — | — |

### Deterministic checks: `branco_anthony-nicholas_b1884` vs `Branco, A. N___Cyprus___1929`

- [PASS] surname_gate: bio 'BRANCO' vs stint 'Branco, A. N' (exact)
- [PASS] initials: bio ['A', 'N'] ~ stint ['A', 'N']
- [PASS] age_gate: stint starts 1929, birth 1884 (age 45)
- [PASS] colony: 5 placed event(s) resolve to 'Cyprus'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1929-1939
- [PASS] position_sim: best 79 vs bar 60: 'local asst. audr' ~ 'Local Assistant Auditor'
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

