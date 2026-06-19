<!-- {"case_id": "case_jacques_evelyn-bessie_e1921", "bio_ids": ["jacques_evelyn-bessie_e1921"], "stint_ids": ["Jacques, E. B___Straits Settlements___1931"]} -->
# Dossier case_jacques_evelyn-bessie_e1921

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 4 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `jacques_evelyn-bessie_e1921`

- Printed name: **JACQUES, EVELYN BESSIE**
- Birth year: not printed
- Honours: M.B
- Appears in editions: [1933, 1934, 1935, 1936, 1940]

### Verbatim printed entry text (OCR)

**Version `col1940-L65541.v` — printed in editions [1940]:**

> JACQUES, EVELYN BESSIE, M.B., Ch.B. (Bristol), D.T.M. & H. (Eng.).—Lady med. offr., Seremban, F.M.S., Feb., 1921; do., K. Lumpur, Feb., 1922; do., Ipoh, Apr., 1924; do., Taiping, June, 1926; do., K. Bahru, Sept., 1934; do., Seremban, Nov., 1937.

**Version `col1933-L60994.v` — printed in editions [1933, 1934, 1935, 1936]:**

> JACQUES, EVELYN BESSIE, M.B., Ch.B. (Bristol), D.T.M. & H. (Lond.).—Lady med. offr., Seremban, F.M.S., Feb., 1921; do., K. Lumpur, Feb., 1922; do., Ipoh, Apr., 1924; do., Taiping, June, 1926.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1921 | Lady med. offr., Seremban | Federated Malay States | [1933, 1934, 1935, 1936, 1940] |
| 1 | 1922 | do., K. Lumpur | Federated Malay States *(inherited from previous clause)* | [1933, 1934, 1935, 1936, 1940] |
| 2 | 1924 | do., Ipoh | Federated Malay States *(inherited from previous clause)* | [1933, 1934, 1935, 1936, 1940] |
| 3 | 1926 | do., Taiping | Federated Malay States *(inherited from previous clause)* | [1933, 1934, 1935, 1936, 1940] |
| 4 | 1934 | do., K. Bahru | Federated Malay States *(inherited from previous clause)* | [1940] |
| 5 | 1937 | do., Seremban | Federated Malay States *(inherited from previous clause)* | [1940] |

## Candidate stint `Jacques, E. B___Straits Settlements___1931`

- Staff-list name: **Jacques, E. B** | colony: **Straits Settlements** | listed 1931–1933 | editions [1931, 1932, 1933]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1931 | E. B. Jacques | Lady Medical Officer | Medical | — | — |
| 1932 | E. B. Jacques | Lady Medical Officer | Medical | — | — |
| 1933 | E. B. Jacques | Lady Medical Officer | Medical | — | — |

### Deterministic checks: `jacques_evelyn-bessie_e1921` vs `Jacques, E. B___Straits Settlements___1931`

- [PASS] surname_gate: bio 'JACQUES' vs stint 'Jacques, E. B' (exact)
- [PASS] initials: bio ['E', 'B'] ~ stint ['E', 'B']
- [PASS] age_gate: stint starts 1931; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Straits Settlements'
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

