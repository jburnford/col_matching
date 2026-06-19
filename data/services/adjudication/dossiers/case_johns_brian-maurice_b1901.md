<!-- {"case_id": "case_johns_brian-maurice_b1901", "bio_ids": ["johns_brian-maurice_b1901"], "stint_ids": ["Johns, B. M___Singapore___1949", "Johns, B. M___Straits Settlements___1931"]} -->
# Dossier case_johns_brian-maurice_b1901

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 21 official(s) with this surname in the graph's staff lists; 8 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `johns_brian-maurice_b1901`

- Printed name: **JOHNS, BRIAN MAURICE**
- Birth year: 1901 (attested in editions [1933, 1934, 1935, 1936, 1939, 1940])
- Honours: M.B
- Appears in editions: [1933, 1934, 1935, 1936, 1939, 1940]

### Verbatim printed entry text (OCR)

**Version `col1933-L61079.v` — printed in editions [1933, 1934, 1935, 1936, 1939, 1940]:**

> JOHNS, BRIAN MAURICE, M.B., Ch.B. (N.Z.), F.R.C.S. (Ed.), D.T.M. & H. (Eng.).—B. 1901; med. offr., S.S., Mar., 1928; prof., clin. surgery, King Edward VII Coll. of Med., S'pore, Aug., 1928; ag. senr. surg., Dec., 1935.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1928 | med. offr. | Straits Settlements | [1933, 1934, 1935, 1936, 1939, 1940] |
| 1 | 1935 | ag. senr. surg | Straits Settlements *(inherited from previous clause)* | [1933, 1934, 1935, 1936, 1939, 1940] |

## Candidate stint `Johns, B. M___Singapore___1949`

- Staff-list name: **Johns, B. M** | colony: **Singapore** | listed 1949–1951 | editions [1949, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | B. M. Johns | Surgeon | Hospitals and Dispensaries | — | — |
| 1951 | B. M. Johns | Surgeon | Hospitals and Dispensaries | — | — |

### Deterministic checks: `johns_brian-maurice_b1901` vs `Johns, B. M___Singapore___1949`

- [PASS] surname_gate: bio 'JOHNS' vs stint 'Johns, B. M' (exact)
- [PASS] initials: bio ['B', 'M'] ~ stint ['B', 'M']
- [PASS] age_gate: stint starts 1949, birth 1901 (age 48)
- [FAIL] colony: no placed event resolves to 'Singapore'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1949-1951
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Johns, B. M___Straits Settlements___1931`

- Staff-list name: **Johns, B. M** | colony: **Straits Settlements** | listed 1931–1939 | editions [1931, 1933, 1934, 1936, 1939]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1931 | B. M. Johns | Professor of Clinical Surgery | King Edward VII College of Medicine | — | — |
| 1933 | B. M. Johns | Professor of Clinical Surgery | King Edward VII College of Medicine | — | — |
| 1934 | B. M. Johns | Professor of Clinical Surgery | King Edward VII College of Medicine, Singapore | — | — |
| 1936 | B. M. Johns | Professor of Clinical Surgery | Medical | — | — |
| 1939 | B. M. Johns | Surgeon, Grade B. | Medical | — | — |

### Deterministic checks: `johns_brian-maurice_b1901` vs `Johns, B. M___Straits Settlements___1931`

- [PASS] surname_gate: bio 'JOHNS' vs stint 'Johns, B. M' (exact)
- [PASS] initials: bio ['B', 'M'] ~ stint ['B', 'M']
- [PASS] age_gate: stint starts 1931, birth 1901 (age 30)
- [PASS] colony: 2 placed event(s) resolve to 'Straits Settlements'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1931-1939
- [FAIL] position_sim: best 52 vs bar 60: 'ag. senr. surg' ~ 'Surgeon, Grade B.'
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

