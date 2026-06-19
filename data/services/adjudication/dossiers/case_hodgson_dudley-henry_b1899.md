<!-- {"case_id": "case_hodgson_dudley-henry_b1899", "bio_ids": ["hodgson_dudley-henry_b1899"], "stint_ids": ["Hodgson, D. H___Sierra Leone___1949"]} -->
# Dossier case_hodgson_dudley-henry_b1899

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 37 official(s) with this surname in the graph's staff lists; 21 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Hodgson, D. H___Sierra Leone___1949` is also gate-compatible with biography(ies) outside this case: ['hodgson_d-h_b1899'] (already linked elsewhere or filtered).

## Biography `hodgson_dudley-henry_b1899`

- Printed name: **HODGSON, DUDLEY HENRY**
- Birth year: 1899 (attested in editions [1933, 1935, 1936, 1937, 1939, 1940])
- Appears in editions: [1932, 1933, 1935, 1936, 1937, 1939, 1940]

### Verbatim printed entry text (OCR)

**Version `col1933-L60704.v` — printed in editions [1933, 1935, 1936, 1937, 1939, 1940]:**

> HODGSON, DUDLEY HENRY, B.A. (Oxon.), Dip. in Forestry.—B. 1899; asst. conserv., forests, F.M.S., Sept., 1921; conserv. forests, Oct., 1930; ag. dep. dir., forestry, S.S. and F.M.S., in 1931, 1932 1933 and 1936.

**Version `col1932-L61155.v` — printed in editions [1932]:**

> HODGSON, DUDLEY HENRY, B.A. (Oxon.), Dip. in Forestry.—B. 1899; asst. conserv., forests, F.M.S., Sept., 1921; ag. forest resch. offr., F.M.S., Oct., -Dec., 1927; conserv. forests, Oct., 1930.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1921 | asst. conserv., forests | Federated Malay States | [1932, 1933, 1935, 1936, 1937, 1939, 1940] |
| 1 | 1927 | ag. forest resch. offr., F.M.S., Oct., - | Federated Malay States *(inherited from previous clause)* | [1932] |
| 2 | 1930 | conserv. forests | Federated Malay States *(inherited from previous clause)* | [1932, 1933, 1935, 1936, 1937, 1939, 1940] |
| 3 | 1931–1936 | ag. dep. dir., forestry | Straits Settlements and Federated Malay States | [1933, 1935, 1936, 1937, 1939, 1940] |

## Candidate stint `Hodgson, D. H___Sierra Leone___1949`

- Staff-list name: **Hodgson, D. H** | colony: **Sierra Leone** | listed 1949–1954 | editions [1949, 1950, 1951, 1952, 1953, 1954]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | D. H. Hodgson | Conservator of Forests | Forestry | — | — |
| 1950 | D. H. Hodgson | Conservator of Forests | FORESTRY | — | — |
| 1951 | D. H. Hodgson | Conservator of Forests | Forestry | — | — |
| 1952 | D. H. Hodgson | Chief Conservator of Forests | Civil Establishment | — | — |
| 1953 | D. H. Hodgson | Development Secretary | Civil Establishment | — | — |
| 1954 | D. H. Hodgson | Development Secretary | Civil Establishment | — | — |

### Deterministic checks: `hodgson_dudley-henry_b1899` vs `Hodgson, D. H___Sierra Leone___1949`

- [PASS] surname_gate: bio 'HODGSON' vs stint 'Hodgson, D. H' (exact)
- [PASS] initials: bio ['D', 'H'] ~ stint ['D', 'H']
- [PASS] age_gate: stint starts 1949, birth 1899 (age 50)
- [FAIL] colony: no placed event resolves to 'Sierra Leone'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1949-1954
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

