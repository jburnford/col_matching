<!-- {"case_id": "case_faris_desmond-william-george_b1901", "bio_ids": ["faris_desmond-william-george_b1901"], "stint_ids": ["Faris, D. W. G___Straits Settlements___1931"]} -->
# Dossier case_faris_desmond-william-george_b1901

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `faris_desmond-william-george_b1901`

- Printed name: **FARIS, DESMOND WILLIAM GEORGE**
- Birth year: 1901 (attested in editions [1939, 1940])
- Honours: M.B
- Appears in editions: [1939, 1940]

### Verbatim printed entry text (OCR)

**Version `col1939-L66487.v` — printed in editions [1939, 1940]:**

> FARIS, DESMOND WILLIAM GEORGE, M.R.C.S. (Eng.), L.R.C.P. (Lond.), M.B., B.S. (Lond.), D.P.H. (Lond.), Certif. L.S.T.M.—B. 1901; ed. Epson Coll., Lond. Hosp. Med. Coll., Lond. Univ.; med. offr., Malaya, Mar., 1926; ag. sr. health offr., Penang, July, 1935; do., S'pore, Feb., 1937; superscale offr., "B", Sept., 1938.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1926 | med. offr. | Malaya | [1939, 1940] |
| 1 | 1935 | ag. sr. health offr., Penang | Malaya *(inherited from previous clause)* | [1939, 1940] |
| 2 | 1937 | do., S'pore | Malaya *(inherited from previous clause)* | [1939, 1940] |
| 3 | 1938 | superscale offr., "B" | Malaya *(inherited from previous clause)* | [1939, 1940] |

## Candidate stint `Faris, D. W. G___Straits Settlements___1931`

- Staff-list name: **Faris, D. W. G** | colony: **Straits Settlements** | listed 1931–1933 | editions [1931, 1933]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1931 | D. W. G. Faris | Health Officer | Health Branch | — | — |
| 1933 | D. W. G. Faris | Health Officer | Health Branch | — | — |

### Deterministic checks: `faris_desmond-william-george_b1901` vs `Faris, D. W. G___Straits Settlements___1931`

- [PASS] surname_gate: bio 'FARIS' vs stint 'Faris, D. W. G' (exact)
- [PASS] initials: bio ['D', 'W', 'G'] ~ stint ['D', 'W', 'G']
- [PASS] age_gate: stint starts 1931, birth 1901 (age 30)
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

