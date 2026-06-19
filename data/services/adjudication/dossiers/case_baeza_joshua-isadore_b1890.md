<!-- {"case_id": "case_baeza_joshua-isadore_b1890", "bio_ids": ["baeza_joshua-isadore_b1890"], "stint_ids": ["Baeza, J___British Honduras___1911"]} -->
# Dossier case_baeza_joshua-isadore_b1890

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `baeza_joshua-isadore_b1890`

- Printed name: **BAEZA, JOSHUA ISADORE**
- Birth year: 1890 (attested in editions [1932, 1933, 1935, 1936, 1937, 1939, 1940])
- Honours: M.B
- Appears in editions: [1932, 1933, 1935, 1936, 1937, 1939, 1940]

### Verbatim printed entry text (OCR)

**Version `col1932-L58118.v` — printed in editions [1932, 1933, 1935, 1936, 1937, 1939, 1940]:**

> BAEZA, JOSHUA ISADORE, M.B., B.Ch. (Edin.), F.R.C.S. (Edin.), D.P.H. (Oxon.), certif. L.S.T.M.—B. 1890; jr. res. surgn., Barbados gen. hosp., Oct., 1913; med. offr., W., Africa, May, 1914; war serv., 1914-16; med. offr. and ag. bacteriologist, Trinidad, 1919-22; ag. sr. health offr., Penang, June, 1923; ag. ch. med. offr., Malacca, Feb., 1924; health offr., S'pore, Mar., 1924; sr. health offr., Kedah, June, 1929; ag. state med. and health offr., Pahang, Sept., 1934.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1913 | jr. res. surgn., Barbados gen. hosp | Barbados | [1932, 1933, 1935, 1936, 1937, 1939, 1940] |
| 1 | 1914 | med. offr., W., Africa | Barbados *(inherited from previous clause)* | [1932, 1933, 1935, 1936, 1937, 1939, 1940] |
| 2 | 1919–1922 | med. offr. and ag. bacteriologist | Trinidad | [1932, 1933, 1935, 1936, 1937, 1939, 1940] |
| 3 | 1923 | ag. sr. health offr., Penang | Trinidad *(inherited from previous clause)* | [1932, 1933, 1935, 1936, 1937, 1939, 1940] |
| 4 | 1924 | ag. ch. med. offr., Malacca | Trinidad *(inherited from previous clause)* | [1932, 1933, 1935, 1936, 1937, 1939, 1940] |
| 5 | 1929 | sr. health offr. | Kedah | [1932, 1933, 1935, 1936, 1937, 1939, 1940] |
| 6 | 1934 | ag. state med. and health offr., Pahang | Kedah *(inherited from previous clause)* | [1932, 1933, 1935, 1936, 1937, 1939, 1940] |

## Candidate stint `Baeza, J___British Honduras___1911`

- Staff-list name: **Baeza, J** | colony: **British Honduras** | listed 1911–1913 | editions [1911, 1912, 1913]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1911 | J. Baeza | Operators | Post Office and Telegraph Department | — | — |
| 1912 | J. Baeza | Operator | Post Office and Telegraph Department | — | — |
| 1913 | J. Baeza | Operator | Post Office and Telegraph Department | — | — |

### Deterministic checks: `baeza_joshua-isadore_b1890` vs `Baeza, J___British Honduras___1911`

- [PASS] surname_gate: bio 'BAEZA' vs stint 'Baeza, J' (exact)
- [PASS] initials: bio ['J', 'I'] ~ stint ['J']
- [PASS] age_gate: stint starts 1911, birth 1890 (age 21)
- [FAIL] colony: no placed event resolves to 'British Honduras'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1911-1913
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

