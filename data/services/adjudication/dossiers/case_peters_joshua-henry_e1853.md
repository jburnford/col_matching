<!-- {"case_id": "case_peters_joshua-henry_e1853", "bio_ids": ["peters_joshua-henry_e1853"], "stint_ids": ["Peters, James H___Canada___1877"]} -->
# Dossier case_peters_joshua-henry_e1853

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 32 official(s) with this surname in the graph's staff lists; 12 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `peters_joshua-henry_e1853`

- Printed name: **PETERS, JOSHUA HENRY**
- Birth year: not printed
- Appears in editions: [1888, 1889, 1890, 1894, 1896, 1897, 1898]

### Verbatim printed entry text (OCR)

**Version `col1888-L35506.v` — printed in editions [1888, 1889, 1890, 1894, 1896, 1897, 1898]:**

> PETERS, JOSHUA HENRY.—Officer, Antigua gaol, 1853; superintendent of convicts, June, 1864; acting governor of the gaol, 1866; confirmed, 1868; keeper of the common gaol of Leeward Islands, 1871.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1853 | Officer, Antigua gaol | Antigua | [1888, 1889, 1890, 1894, 1896, 1897, 1898] |
| 1 | 1864 | superintendent of convicts | Antigua *(inherited from previous clause)* | [1888, 1889, 1890, 1894, 1896, 1897, 1898] |
| 2 | 1866 | acting governor of the gaol | Antigua *(inherited from previous clause)* | [1888, 1889, 1890, 1894, 1896, 1897, 1898] |
| 3 | 1868 | confirmed | Antigua *(inherited from previous clause)* | [1888, 1889, 1890, 1894, 1896, 1897, 1898] |
| 4 | 1871 | keeper of the common gaol of Leeward Islands | Antigua *(inherited from previous clause)* | [1888, 1889, 1890, 1894, 1896, 1897, 1898] |

## Candidate stint `Peters, James H___Canada___1877`

- Staff-list name: **Peters, James H** | colony: **Canada** | listed 1877–1888 | editions [1877, 1878, 1879, 1880, 1883, 1886, 1888]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | James H. Peters | Master of the Rolls and Senior Assistant Judge of the Supreme Court | Judicial Establishment, Supreme Court | — | — |
| 1878 | James H. Peters | Master of the Rolls and Senior Assistant Judge of the Supreme Court | — | — | — |
| 1879 | James H. Peters | Master of the Rolls and Senior Assistant Judge of the Supreme Court | — | — | — |
| 1880 | James H. Peters | Master of the Rolls and Senior Assistant Judge of the Supreme Court | — | — | — |
| 1883 | Hon. James H. Peters | Master of the Rolls and Senior Assistant Judge of the Supreme Court | Judicial Establishment, Supreme Court | — | — |
| 1886 | James H. Peters | Master of the Rolls and Senior Assistant Judge of the Supreme Court | Judicial Establishment, Supreme Court | — | — |
| 1888 | Hon. James H. Peters | Master of the Rolls and Senior Assistant Judge of the Supreme Court | Judicial Establishment, Supreme Court | — | — |

### Deterministic checks: `peters_joshua-henry_e1853` vs `Peters, James H___Canada___1877`

- [PASS] surname_gate: bio 'PETERS' vs stint 'Peters, James H' (exact)
- [PASS] initials: bio ['J', 'H'] ~ stint ['J', 'H']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Canada'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1877-1888
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

