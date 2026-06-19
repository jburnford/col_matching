<!-- {"case_id": "case_wiggett_archibald-douglas_b1884", "bio_ids": ["wiggett_archibald-douglas_b1884"], "stint_ids": ["Wiggett, A. D___Cape of Good Hope___1905"]} -->
# Dossier case_wiggett_archibald-douglas_b1884

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `wiggett_archibald-douglas_b1884`

- Printed name: **WIGGETT, ARCHIBALD DOUGLAS**
- Birth year: 1884 (attested in editions [1935, 1936, 1937, 1939, 1940])
- Appears in editions: [1935, 1936, 1937, 1939, 1940]

### Verbatim printed entry text (OCR)

**Version `dol1935-L63263.v` — printed in editions [1935, 1936, 1937, 1939, 1940]:**

> WIGGETT, ARCHIBALD DOUGLAS.—B. 1884; law and income tax depta., Cape Col., 1901-10; census office, 1911; accs. hr., dept. of int., 1912; income tax dept., 1914; inland rev. dept., 1916; recr., rev., Kimberley, 1931; accs., 1931; recr., rev., E. London, 1932; ch. clk., income tax, Feb., 1933; recr., rev., Pretoria, 1933; ch. rev. offr., June, 1934; asst. comsrr. for inland rev., Apr., 1939.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1901–1910 | law and income tax depta. | Cape of Good Hope | [1935, 1936, 1937, 1939, 1940] |
| 1 | 1911 | census office | Cape of Good Hope *(inherited from previous clause)* | [1935, 1936, 1937, 1939, 1940] |
| 2 | 1912 | accs. hr., dept. of int | Cape of Good Hope *(inherited from previous clause)* | [1935, 1936, 1937, 1939, 1940] |
| 3 | 1914 | income tax dept | Cape of Good Hope *(inherited from previous clause)* | [1935, 1936, 1937, 1939, 1940] |
| 4 | 1916 | inland rev. dept | Cape of Good Hope *(inherited from previous clause)* | [1935, 1936, 1937, 1939, 1940] |
| 5 | 1931 | recr., rev., Kimberley | Cape of Good Hope *(inherited from previous clause)* | [1935, 1936, 1937, 1939, 1940] |
| 6 | 1932 | recr., rev., E. London | Cape of Good Hope *(inherited from previous clause)* | [1935, 1936, 1937, 1939, 1940] |
| 7 | 1933 | ch. clk., income tax | Cape of Good Hope *(inherited from previous clause)* | [1935, 1936, 1937, 1939, 1940] |
| 8 | 1934 | ch. rev. offr | Cape of Good Hope *(inherited from previous clause)* | [1935, 1936, 1937, 1939, 1940] |
| 9 | 1939 | asst. comsrr. for inland rev | Cape of Good Hope *(inherited from previous clause)* | [1935, 1936, 1937, 1939, 1940] |

## Candidate stint `Wiggett, A. D___Cape of Good Hope___1905`

- Staff-list name: **Wiggett, A. D** | colony: **Cape of Good Hope** | listed 1905–1909 | editions [1905, 1907, 1908, 1909]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1905 | A. D. Wiggett | Examiners of Accounts | Accounting Branch | — | — |
| 1905 | A. D. Wiggett | Clerk | Income Tax Branch | — | — |
| 1907 | A. D. Wiggett | Clerk | Income Tax Branch | — | — |
| 1908 | A. D. Wiggett | Clerk | Income Tax Branch | — | — |
| 1909 | A. D. Wiggett | Clerk | Civil Commissioner, Cape, and Income Tax | — | — |

### Deterministic checks: `wiggett_archibald-douglas_b1884` vs `Wiggett, A. D___Cape of Good Hope___1905`

- [PASS] surname_gate: bio 'WIGGETT' vs stint 'Wiggett, A. D' (exact)
- [PASS] initials: bio ['A', 'D'] ~ stint ['A', 'D']
- [PASS] age_gate: stint starts 1905, birth 1884 (age 21)
- [PASS] colony: 10 placed event(s) resolve to 'Cape of Good Hope'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1905-1909
- [FAIL] position_sim: best 40 vs bar 60: 'law and income tax depta.' ~ 'Examiners of Accounts'
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

