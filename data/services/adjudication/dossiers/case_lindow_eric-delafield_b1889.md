<!-- {"case_id": "case_lindow_eric-delafield_b1889", "bio_ids": ["lindow_eric-delafield_b1889"], "stint_ids": ["Lindow, E. D___Straits Settlements___1925"]} -->
# Dossier case_lindow_eric-delafield_b1889

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `lindow_eric-delafield_b1889`

- Printed name: **LINDOW, ERIC DELAFIELD**
- Birth year: 1889 (attested in editions [1935, 1936, 1937, 1939, 1940])
- Appears in editions: [1935, 1936, 1937, 1939, 1940]

### Verbatim printed entry text (OCR)

**Version `dol1935-L60296.v` — printed in editions [1935, 1936, 1937, 1939, 1940]:**

> LINDOW, ERIC DELAFIELD, M.R.C.S. (Eng.), L.R.C.P. Lond., certif. L.S.T.M.—B. 1889; ed. Christ's Coll. Blackheath, Lond. Univ., King's Coll. and King's Coll. Hosp.; med. offr., gen. hosp., S'pore, Apr., 1923; do., T.T.S. hosp., Dec., 1923, Oct., 1928 and Apr., 1932; ag. ch. med. offr., Malacca, Feb., 1928 and Apr., 1929; ag. supnmy. ch. med. offr., A, S'pore, June, 1933, sup-scale offr., gr. B., Jan., 1935; ag. ch. med. offr., Penang, Apr., 1936; sup-scale offr., gd. A, Sept., 1938.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1923 | med. offr., gen. hosp. | Singapore | [1935, 1936, 1937, 1939, 1940] |
| 1 | 1923 | do., T.T.S. hosp. | — | [1935, 1936, 1937, 1939, 1940] |
| 2 | 1928 | ag. ch. med. offr. | Malacca | [1935, 1936, 1937, 1939, 1940] |
| 3 | 1933 | ag. supnmy. ch. med. offr., A | Singapore | [1935, 1936, 1937, 1939, 1940] |
| 4 | 1935 | sup-scale offr., gr. B. | — | [1935, 1936, 1937, 1939, 1940] |
| 5 | 1936 | ag. ch. med. offr. | Penang | [1935, 1936, 1937, 1939, 1940] |
| 6 | 1938 | sup-scale offr., gd. A | — | [1935, 1936, 1937, 1939, 1940] |

## Candidate stint `Lindow, E. D___Straits Settlements___1925`

- Staff-list name: **Lindow, E. D** | colony: **Straits Settlements** | listed 1925–1939 | editions [1925, 1931, 1933, 1934, 1939]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1925 | E. D. Lindow | Medical Officer | SINGAPORE | — | — |
| 1931 | E. D. Lindow | Medical and Health Officer | Medical | — | — |
| 1933 | E. D. Lindow | Medical and Health Officer | Medical | — | — |
| 1934 | E. D. Lindow | Chief Medical Officer | Singapore | — | — |
| 1939 | E. D. Lindow | Supercase Medical Officer, Grade B. | Medical | — | — |

### Deterministic checks: `lindow_eric-delafield_b1889` vs `Lindow, E. D___Straits Settlements___1925`

- [PASS] surname_gate: bio 'LINDOW' vs stint 'Lindow, E. D' (exact)
- [PASS] initials: bio ['E', 'D'] ~ stint ['E', 'D']
- [PASS] age_gate: stint starts 1925, birth 1889 (age 36)
- [FAIL] colony: no placed event resolves to 'Straits Settlements'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1925-1939
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

