<!-- {"case_id": "case_macdougall_donald-keith_e1900", "bio_ids": ["macdougall_donald-keith_e1900"], "stint_ids": ["MacDougall, K___Kenya___1905"]} -->
# Dossier case_macdougall_donald-keith_e1900

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 9 official(s) with this surname in the graph's staff lists; 9 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `macdougall_donald-keith_e1900`

- Printed name: **MACDOUGALL, DONALD KEITH**
- Birth year: not printed
- Honours: C. M. G. (1901)
- Appears in editions: [1906, 1908, 1909]

### Verbatim printed entry text (OCR)

**Version `col1906-L46729.v` — printed in editions [1906, 1908, 1909]:**

> MACDOUGALL, DONALD KEITH, C. M. G. (1901).—Prin. med. offr. of W.A.F.F.; accompanied Ashanti expdn., 1900, in that capacity; prin. civ. med. offr., Straits Settlements, Mar., 1903, and inspr. of hospitals, F.M.S., 1905.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1900–1900 | — | Ashanti | [1906, 1908, 1909] |
| 1 | 1903–1903 | prin. civ. med. offr. | Straits Settlements | [1906, 1908, 1909] |
| 2 | 1905–1905 | inspr. of hospitals | Federated Malay States | [1906, 1908, 1909] |

## Candidate stint `MacDougall, K___Kenya___1905`

- Staff-list name: **MacDougall, K** | colony: **Kenya** | listed 1905–1906 | editions [1905, 1906]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1905 | K. MacDougall | Sub-Commissioner (Tana-land) | — | — | — |
| 1906 | K. MacDougall | Sub-Commissioner (Tanalond) | — | — | — |

### Deterministic checks: `macdougall_donald-keith_e1900` vs `MacDougall, K___Kenya___1905`

- [PASS] surname_gate: bio 'MACDOUGALL' vs stint 'MacDougall, K' (exact)
- [PASS] initials: bio ['D', 'K'] ~ stint ['K']
- [PASS] age_gate: stint starts 1905; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Kenya'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1905-1906
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

