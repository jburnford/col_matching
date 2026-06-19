<!-- {"case_id": "case_carson_james-coburn_b1894", "bio_ids": ["carson_james-coburn_b1894"], "stint_ids": ["Carson, J. C___Straits Settlements___1933"]} -->
# Dossier case_carson_james-coburn_b1894

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 5 official(s) with this surname in the graph's staff lists; 4 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `carson_james-coburn_b1894`

- Printed name: **CARSON, JAMES COBURN**
- Birth year: 1894 (attested in editions [1936, 1937, 1940])
- Honours: M.B
- Appears in editions: [1936, 1937, 1940]

### Verbatim printed entry text (OCR)

**Version `col1936-L59580.v` — printed in editions [1936, 1937, 1940]:**

> CARSON, JAMES COBURN, M.B., B. Ch., B.A.O. (Queens Univ., Belfast), D.T.M. (Meth. Coll., Belfast).—B. 1894; 11th Battn. R. Irish Rifles and 126th Baluchistan Infry., 1915-18; med. offr., S.S., Apr., 1924; gen. hosp., Penang, May, 1924; ag. prof., anatomy, med. coll., S'pore, May, 1926-Jan., 1927; med. offr., S'pore, June, 1927; ag. ch. med. offr., Malacca, Jan., 1928 and Sept., 1931; med. offr., P. Wellesley, Jan., 1932; do. S'pore, June, 1933; do., K. Lumpur, Nov., 1933; dep. state med. and health offr., Perak, Apr., 1936; ag. state surgeon, Kedah, Aug., 1938.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1915–1918 | 11th Battn. R. Irish Rifles and 126th Baluchistan Infry | — | [1936, 1937, 1940] |
| 1 | 1924 | med. offr. | Straits Settlements | [1936, 1937, 1940] |
| 2 | 1926–1927 | ag. prof., anatomy, med. coll., S'pore | Straits Settlements *(inherited from previous clause)* | [1936, 1937, 1940] |
| 3 | 1927 | med. offr., S'pore | Straits Settlements *(inherited from previous clause)* | [1936, 1937, 1940] |
| 4 | 1928 | ag. ch. med. offr., Malacca | Straits Settlements *(inherited from previous clause)* | [1936, 1937, 1940] |
| 5 | 1931 | ag. ch. med. offr., Malacca | Straits Settlements *(inherited from previous clause)* | [1936, 1937, 1940] |
| 6 | 1932 | med. offr., P. Wellesley | Straits Settlements *(inherited from previous clause)* | [1936, 1937, 1940] |
| 7 | 1933 | do. S'pore | Dominions Office | [1936, 1937, 1940] |
| 8 | 1936 | dep. state med. and health offr., Perak | Dominions Office *(inherited from previous clause)* | [1936, 1937, 1940] |
| 9 | 1938 | ag. state surgeon | Kedah | [1936, 1937, 1940] |

## Candidate stint `Carson, J. C___Straits Settlements___1933`

- Staff-list name: **Carson, J. C** | colony: **Straits Settlements** | listed 1933–1939 | editions [1933, 1936, 1939]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1933 | J. C. Carson | Medical and Health Officer | Medical | — | — |
| 1936 | J. C. Carson | Chief Medical Officer | Medical | — | — |
| 1939 | J. C. Carson | Supercase Medical Officer, Grade B. | Medical | — | — |

### Deterministic checks: `carson_james-coburn_b1894` vs `Carson, J. C___Straits Settlements___1933`

- [PASS] surname_gate: bio 'CARSON' vs stint 'Carson, J. C' (exact)
- [PASS] initials: bio ['J', 'C'] ~ stint ['J', 'C']
- [PASS] age_gate: stint starts 1933, birth 1894 (age 39)
- [PASS] colony: 6 placed event(s) resolve to 'Straits Settlements'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1933-1939
- [FAIL] position_sim: best 58 vs bar 60: 'ag. ch. med. offr., Malacca' ~ 'Medical and Health Officer'
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

