<!-- {"case_id": "case_kibble_edmund-david_b1881", "bio_ids": ["kibble_edmund-david_b1881"], "stint_ids": ["Kibble, E. D___Straits Settlements___1931"]} -->
# Dossier case_kibble_edmund-david_b1881

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `kibble_edmund-david_b1881`

- Printed name: **KIBBLE, EDMUND DAVID**
- Birth year: 1881 (attested in editions [1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936])
- Honours: A.M.I.C.E
- Appears in editions: [1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936]

### Verbatim printed entry text (OCR)

**Version `col1928-L67573.v` — printed in editions [1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936]:**

> KIBBLE, EDMUND DAVID, A.M.I.C.E.—B. 1881; ed. Highgate Schl. and City & Guilds (Engnr.) Coll., S. Kensington; asst. engrnr., pub. wks. dept., F.M.S., Dec., 1907; ex. engrnr., pub. wks. dept., F.M.S., 1914; senr. ex. engrnr., 1923; ag. state engrnr., Kedah, Nov., 1923; senr. ex. engrnr., F.M.S., July, 1924; attd., govt. town planning dept., F.M.S., Aug., 1924; ag. state engrnr., Negeri Sembilan, Apr., 1927; state engrnr., Pahang, June, 1927.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1907 | asst. engrnr., pub. wks. dept. | Federated Malay States | [1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936] |
| 1 | 1914 | ex. engrnr., pub. wks. dept. | Federated Malay States | [1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936] |
| 2 | 1923 | senr. ex. engrnr | Federated Malay States *(inherited from previous clause)* | [1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936] |
| 3 | 1923 | ag. state engrnr. | Kedah | [1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936] |
| 4 | 1924 | senr. ex. engrnr. | Federated Malay States | [1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936] |
| 5 | 1927 | ag. state engrnr., Negeri Sembilan | Federated Malay States *(inherited from previous clause)* | [1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936] |

## Candidate stint `Kibble, E. D___Straits Settlements___1931`

- Staff-list name: **Kibble, E. D** | colony: **Straits Settlements** | listed 1931–1932 | editions [1931, 1932]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1931 | E D Kibble | State Engineer | PUBLIC WORKS | — | — |
| 1931 | E. D. Kibble | State Engineer | Public Works | — | — |
| 1932 | E. D. Kibble | State Engineer | Public Works | — | — |

### Deterministic checks: `kibble_edmund-david_b1881` vs `Kibble, E. D___Straits Settlements___1931`

- [PASS] surname_gate: bio 'KIBBLE' vs stint 'Kibble, E. D' (exact)
- [PASS] initials: bio ['E', 'D'] ~ stint ['E', 'D']
- [PASS] age_gate: stint starts 1931, birth 1881 (age 50)
- [FAIL] colony: no placed event resolves to 'Straits Settlements'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1931-1932
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

