<!-- {"case_id": "case_de-boer_henry-spelderwinde_b1889", "bio_ids": ["de-boer_henry-spelderwinde_b1889"], "stint_ids": ["de Boer, H. S___Kenya___1922", "de Boer, H. S___Northern Rhodesia___1931"]} -->
# Dossier case_de-boer_henry-spelderwinde_b1889

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 5 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `de-boer_henry-spelderwinde_b1889`

- Printed name: **De BOER, HENRY SPELDERWINDE**
- Birth year: 1889 (attested in editions [1932, 1934, 1935, 1936, 1937, 1939, 1940])
- Honours: M.C
- Appears in editions: [1932, 1934, 1935, 1936, 1937, 1939, 1940]

### Verbatim printed entry text (OCR)

**Version `col1932-L59589.v` — printed in editions [1932, 1934, 1935, 1936, 1937, 1939, 1940]:**

> De BOER, HENRY SPELDERWINDE, M.C., M.R.C.S. (Eng.), I.R.C.P. (Lond.), D.P.H. (Cantab.), D.T.M. and H. (Lond.).—B. 1889; ed. privately and at London Hosp.; served with R.A.M.C., 1915-20 (Gallipoli, Sinai, Palestine and Syria, ment. in desps.); med. offr., Kenya, May, 1920; senr. health offr., E. African med. serv., Jan., 1926; dep. dir., san. services, N. Rhodesia, Mar., 1931; do., med. services, 1933; dep. dir., med. services, Uganda, 1933; ag. D.M.S., Mar.-Dec., 1937; D.M.S., Nyasaland, 1938.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1915–1920 | served with R.A.M.C | — | [1932, 1934, 1935, 1936, 1937, 1939, 1940] |
| 1 | 1920 | med. offr. | Kenya | [1932, 1934, 1935, 1936, 1937, 1939, 1940] |
| 2 | 1926 | senr. health offr., E. African med. serv | Kenya *(inherited from previous clause)* | [1932, 1934, 1935, 1936, 1937, 1939, 1940] |
| 3 | 1931 | dep. dir., san. services, N. Rhodesia | Kenya *(inherited from previous clause)* | [1932, 1934, 1935, 1936, 1937, 1939, 1940] |
| 4 | 1933 | do., med. services | Uganda | [1932, 1934, 1935, 1936, 1937, 1939, 1940] |
| 5 | 1937 | ag. D.M.S., Mar.- | Uganda *(inherited from previous clause)* | [1932, 1934, 1935, 1936, 1937, 1939, 1940] |
| 6 | 1938 | D.M.S. | Nyasaland | [1932, 1934, 1935, 1936, 1937, 1939, 1940] |

## Candidate stint `de Boer, H. S___Kenya___1922`

- Staff-list name: **de Boer, H. S** | colony: **Kenya** | listed 1922–1925 | editions [1922, 1923, 1924, 1925]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1922 | H. S. de Boer | Medical Officer of Health | Medical | — | — |
| 1923 | H. S. de Boer | Medical Officer of Health | Medical | — | — |
| 1924 | H. S. de Boer | Medical Officer of Health | Medical | — | — |
| 1925 | H. S. de Boer | Medical Officer of Health | Medical Department | — | — |

### Deterministic checks: `de-boer_henry-spelderwinde_b1889` vs `de Boer, H. S___Kenya___1922`

- [PASS] surname_gate: bio 'De BOER' vs stint 'de Boer, H. S' (exact)
- [PASS] initials: bio ['H', 'S'] ~ stint ['H', 'S']
- [PASS] age_gate: stint starts 1922, birth 1889 (age 33)
- [PASS] colony: 3 placed event(s) resolve to 'Kenya'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1922-1925
- [FAIL] position_sim: best 57 vs bar 60: 'senr. health offr., E. African med. serv' ~ 'Medical Officer of Health'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

## Candidate stint `de Boer, H. S___Northern Rhodesia___1931`

- Staff-list name: **de Boer, H. S** | colony: **Northern Rhodesia** | listed 1931–1933 | editions [1931, 1933]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1931 | H. S. de Boer | Deputy Director of Sanitary Services | Health | — | — |
| 1933 | H. S. de Boer | Deputy Director of Sanitary Services | Health | — | — |

### Deterministic checks: `de-boer_henry-spelderwinde_b1889` vs `de Boer, H. S___Northern Rhodesia___1931`

- [PASS] surname_gate: bio 'De BOER' vs stint 'de Boer, H. S' (exact)
- [PASS] initials: bio ['H', 'S'] ~ stint ['H', 'S']
- [PASS] age_gate: stint starts 1931, birth 1889 (age 42)
- [FAIL] colony: no placed event resolves to 'Northern Rhodesia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1931-1933
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

