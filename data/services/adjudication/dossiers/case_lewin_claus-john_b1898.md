<!-- {"case_id": "case_lewin_claus-john_b1898", "bio_ids": ["lewin_claus-john_b1898"], "stint_ids": ["Lewin, C. J___Northern Rhodesia___1933"]} -->
# Dossier case_lewin_claus-john_b1898

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 4 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Lewin, C. J___Northern Rhodesia___1933` is also gate-compatible with biography(ies) outside this case: ['lewin_claud-john_b1898'] (already linked elsewhere or filtered).

## Biography `lewin_claus-john_b1898`

- Printed name: **LEWIN, CLAUS JOHN**
- Birth year: 1898 (attested in editions [1933, 1934, 1935, 1936, 1937, 1939, 1940])
- Appears in editions: [1933, 1934, 1935, 1936, 1937, 1939, 1940]

### Verbatim printed entry text (OCR)

**Version `col1933-L61524.v` — printed in editions [1933, 1934, 1935, 1936, 1937, 1939, 1940]:**

> LEWIN, CLAUS JOHN, M.C., B.Sc.—B. 1898; ed. Sexey's Sch., Univ. Coll., Reading and Trinity Coll., Cambridge; on war serv., 1915-17; supt., agr., Nigeria, Dec., 1922; junr. botanist, 1923; senr. botanist, 1925; ch. agriculturist, N. Rhodesia, Nov., 1930; ag. sec., agr., Dec., 1932; dir., agr., July, 1933; temp. M.L.C., 1935, 1936 and 1937.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1915–1917 | on war serv. | — | [1933, 1934, 1935, 1936, 1937, 1939, 1940] |
| 1 | 1922 | supt., agr. | Nigeria | [1933, 1934, 1935, 1936, 1937, 1939, 1940] |
| 2 | 1923 | junr. botanist | — | [1933, 1934, 1935, 1936, 1937, 1939, 1940] |
| 3 | 1925 | senr. botanist | — | [1933, 1934, 1935, 1936, 1937, 1939, 1940] |
| 4 | 1930 | ch. agriculturist | N. Rhodesia | [1933, 1934, 1935, 1936, 1937, 1939, 1940] |
| 5 | 1932 | ag. sec., agr. | — | [1933, 1934, 1935, 1936, 1937, 1939, 1940] |
| 6 | 1933 | dir., agr. | — | [1933, 1934, 1935, 1936, 1937, 1939, 1940] |
| 7 | 1935–1937 | temp. M.L.C. | — | [1933, 1934, 1935, 1936, 1937, 1939, 1940] |

## Candidate stint `Lewin, C. J___Northern Rhodesia___1933`

- Staff-list name: **Lewin, C. J** | colony: **Northern Rhodesia** | listed 1933–1946 | editions [1933, 1934, 1936, 1939, 1940, 1946]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1933 | C. J. Lewin | Chief Agriculturalist | Agriculture | — | — |
| 1934 | C. J. Lewin | Director of Agriculture | Agriculture | M.C. | — |
| 1936 | C. J. Lewin | Director of Agriculture | Agriculture | — | — |
| 1939 | C. J. Lewin | Director of Agriculture | Agriculture | — | — |
| 1940 | C. J. Lewin | Director of Agriculture | Agriculture | — | — |
| 1946 | C. J. Lewin | Nominated Official Member | Legislative Council | — | — |

### Deterministic checks: `lewin_claus-john_b1898` vs `Lewin, C. J___Northern Rhodesia___1933`

- [PASS] surname_gate: bio 'LEWIN' vs stint 'Lewin, C. J' (exact)
- [PASS] initials: bio ['C', 'J'] ~ stint ['C', 'J']
- [PASS] age_gate: stint starts 1933, birth 1898 (age 35)
- [FAIL] colony: no placed event resolves to 'Northern Rhodesia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1933-1946
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

