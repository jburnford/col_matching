<!-- {"case_id": "case_hopkins_herbert-oxley_b1895", "bio_ids": ["hopkins_herbert-oxley_b1895"], "stint_ids": ["Hopkins, H. O___Straits Settlements___1931"]} -->
# Dossier case_hopkins_herbert-oxley_b1895

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 29 official(s) with this surname in the graph's staff lists; 14 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `hopkins_herbert-oxley_b1895`

- Printed name: **HOPKINS, HERBERT OXLEY**
- Birth year: 1895 (attested in editions [1937, 1939, 1940])
- Appears in editions: [1937, 1939, 1940]

### Verbatim printed entry text (OCR)

**Version `col1937-L61884.v` — printed in editions [1937, 1939, 1940]:**

> HOPKINS, HERBERT OXLEY, M.A. (Oxon.), M.R.C.S. (Eng.), L.R.C.P. (Lond.), grad. L.S.T.M.—B. 1895; mil'y. serv. with 7th Battn. The King's Liverpool Reg., 1915-18; asst. bactlgst., Middlesex Hosp., 1926; Malaria resech., offr., inst. med. resech., F.M.S., Sept., 1927; bactlgst., S'pore, July, 1929; med. offr., Tan Toek Seng Hosp., S'pore, Jan., 1932; gov't. bactlgst., S'pore, Jan., 1933; pathologist, Penang, June, 1936; do., S.S., 1938.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1915–1918 | mil'y. serv. with 7th Battn. The King's Liverpool Reg | — | [1937, 1939, 1940] |
| 1 | 1926 | asst. bactlgst., Middlesex Hosp | — | [1937, 1939, 1940] |
| 2 | 1927 | Malaria resech., offr., inst. med. resech. | Federated Malay States | [1937, 1939, 1940] |
| 3 | 1929 | bactlgst., S'pore | Federated Malay States *(inherited from previous clause)* | [1937, 1939, 1940] |
| 4 | 1932 | med. offr., Tan Toek Seng Hosp., S'pore | Federated Malay States *(inherited from previous clause)* | [1937, 1939, 1940] |
| 5 | 1933 | gov't. bactlgst., S'pore | Federated Malay States *(inherited from previous clause)* | [1937, 1939, 1940] |
| 6 | 1936 | pathologist, Penang | Federated Malay States *(inherited from previous clause)* | [1937, 1939, 1940] |
| 7 | 1938 | pathologist, Penang | Straits Settlements | [1937, 1939, 1940] |

## Candidate stint `Hopkins, H. O___Straits Settlements___1931`

- Staff-list name: **Hopkins, H. O** | colony: **Straits Settlements** | listed 1931–1936 | editions [1931, 1933, 1934, 1936]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1931 | H. O. Hopkins | Bacteriologist | Medical | — | — |
| 1933 | H. O. Hopkins | Bacteriologist | Medical | — | — |
| 1934 | H. O. Hopkins | Bacteriologist | Singapore | — | — |
| 1936 | H. O. Hopkins | Bacteriologist | Medical | — | — |

### Deterministic checks: `hopkins_herbert-oxley_b1895` vs `Hopkins, H. O___Straits Settlements___1931`

- [PASS] surname_gate: bio 'HOPKINS' vs stint 'Hopkins, H. O' (exact)
- [PASS] initials: bio ['H', 'O'] ~ stint ['H', 'O']
- [PASS] age_gate: stint starts 1931, birth 1895 (age 36)
- [PASS] colony: 1 placed event(s) resolve to 'Straits Settlements'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1931-1936
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

