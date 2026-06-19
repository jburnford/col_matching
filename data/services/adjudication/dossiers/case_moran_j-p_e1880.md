<!-- {"case_id": "case_moran_j-p_e1880", "bio_ids": ["moran_j-p_e1880"], "stint_ids": ["Moran, James___Newfoundland___1877"]} -->
# Dossier case_moran_j-p_e1880

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 6 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `moran_j-p_e1880`

- Printed name: **MORAN, J. P**
- Birth year: not printed
- Terminal: died 1889 — “died 1889.”
- Appears in editions: [1888, 1889, 1890]

### Verbatim printed entry text (OCR)

**Version `col1888-L34974.v` — printed in editions [1888, 1889, 1890]:**

> MORAN, J. P.—Galway artillery militia, Oct., 1880; attached 46th brigade depot, Maidstone, Jan., 1881; passed qualifying examination in gunnery, Aug., 1881; obtained P.S. certificate in gunnery, 1882; assistant-inspector, G.C.C., May, 1884; detailed for services in the Quittah disturbances, Jan., 1885; assigned to Lagos constabulary, and acting inspector-general and sheriff, Lagos, Feb., 1886; asst. inspector constab. G. Coast, 1888; died 1889.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1880 | Galway artillery militia | — | [1888, 1889, 1890] |
| 1 | 1881 | attached 46th brigade depot, Maidstone | — | [1888, 1889, 1890] |
| 2 | 1881 | passed qualifying examination in gunnery | — | [1888, 1889, 1890] |
| 3 | 1882 | obtained P.S. certificate in gunnery | — | [1888, 1889, 1890] |
| 4 | 1884 | assistant-inspector, G.C.C | — | [1888, 1889, 1890] |
| 5 | 1885 | detailed for services in the Quittah disturbances | — | [1888, 1889, 1890] |
| 6 | 1886 | assigned to Lagos constabulary, and acting inspector-general and sheriff | Lagos | [1888, 1889, 1890] |
| 7 | 1888 | asst. inspector constab. G. Coast | Lagos *(inherited from previous clause)* | [1888, 1889, 1890] |

## Candidate stint `Moran, James___Newfoundland___1877`

- Staff-list name: **Moran, James** | colony: **Newfoundland** | listed 1877–1880 | editions [1877, 1878, 1879, 1880]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | James Moran | Magistrate | Judicial Establishment | — | — |
| 1878 | James Moran | Magistrate | Magistrates | — | — |
| 1879 | James Moran | Magistrate | Judicial Establishment | — | — |
| 1880 | James Moran | Magistrate | Judicial Establishment | — | — |

### Deterministic checks: `moran_j-p_e1880` vs `Moran, James___Newfoundland___1877`

- [PASS] surname_gate: bio 'MORAN' vs stint 'Moran, James' (exact)
- [PASS] initials: bio ['J', 'P'] ~ stint ['J']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Newfoundland'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1877-1880
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

