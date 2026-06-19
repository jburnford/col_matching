<!-- {"case_id": "case_harmer_herbert-j_e1884-2", "bio_ids": ["harmer_herbert-j_e1884-2"], "stint_ids": ["Harmer, H. J___Straits Settlements___1888"]} -->
# Dossier case_harmer_herbert-j_e1884-2

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 7 official(s) with this surname in the graph's staff lists; 6 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `harmer_herbert-j_e1884-2`

- Printed name: **HARMER, HERBERT J.**
- Birth year: not printed
- Appears in editions: [1888, 1889, 1894, 1896, 1897, 1898]

### Verbatim printed entry text (OCR)

**Version `col1896-L39341.v` — printed in editions [1896, 1897, 1898]:**

> HARMER, HERBERT J.—Harbour master, Malacca, 21st April, 1884; asst. Indian Immigr. agent, Dec., 1884; ag. dep. master attendant, Singapore, Sept., 1893, to Apl., 1896.

**Version `col1888-L33887.v` — printed in editions [1888, 1889, 1894]:**

> HARMER, HERBERT J.—Harbour master, Malacca, 21st April, 1884; asst. Indian Immigr. agent, Dec., 1884.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1884 | Harbour master | Malacca | [1888, 1889, 1894, 1896, 1897, 1898] |
| 1 | 1884 | asst. Indian Immigr. agent | — | [1888, 1889, 1894, 1896, 1897, 1898] |
| 2 | 1893–1896 | ag. dep. master attendant | Singapore | [1896, 1897, 1898] |

## Candidate stint `Harmer, H. J___Straits Settlements___1888`

- Staff-list name: **Harmer, H. J** | colony: **Straits Settlements** | listed 1888–1897 | editions [1888, 1889, 1894, 1897]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1888 | H. J. Harmer | Harbour Master | Malacca | — | — |
| 1889 | H. J. Harmer | Official | Malacca | — | — |
| 1894 | H. J. Harmer | Harbour Master | Malacca | — | — |
| 1897 | H. J. Harmer | Harbour Master | Malacca | — | — |

### Deterministic checks: `harmer_herbert-j_e1884-2` vs `Harmer, H. J___Straits Settlements___1888`

- [PASS] surname_gate: bio 'HARMER' vs stint 'Harmer, H. J' (exact)
- [PASS] initials: bio ['H', 'J'] ~ stint ['H', 'J']
- [PASS] age_gate: stint starts 1888; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Straits Settlements'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1888-1897
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

