<!-- {"case_id": "case_adams_george-p_e1876", "bio_ids": ["adams_george-p_e1876", "adams_george-p_e1876-2"], "stint_ids": ["Adams, G. P___Tasmania___1877"]} -->
# Dossier case_adams_george-p_e1876

## Case context

- 2 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 96 official(s) with this surname in the graph's staff lists; 42 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- CONTESTED: stint(s) ['Adams, G. P___Tasmania___1877'] have more than one claimant biography in this case.
- Phase 1 found `adams_george-p_e1876` ↔ `Adams, G. P___Tasmania___1877` passed its evidence bar but dropped it as ambiguous (a comparable-strength competitor existed).
- Phase 1 found `adams_george-p_e1876-2` ↔ `Adams, G. P___Tasmania___1877` passed its evidence bar but dropped it as ambiguous (a comparable-strength competitor existed).

## Biography `adams_george-p_e1876`

- Printed name: **ADAMS, GEORGE P**
- Birth year: not printed
- Appears in editions: [1886]

### Verbatim printed entry text (OCR)

**Version `col1886-L31826.v` — printed in editions [1886]:**

> ADAMS, GEORGE P.—Recorder of titles, Tasmania, 3 July, 1876.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1876 | Recorder of titles | Tasmania | [1886] |

## Biography `adams_george-p_e1876-2`

- Printed name: **ADAMS, GEORGE P**
- Birth year: not printed
- Appears in editions: [1888, 1889, 1890, 1894, 1896, 1897, 1898]

### Verbatim printed entry text (OCR)

**Version `col1888-L31734.v` — printed in editions [1888, 1889, 1890, 1894, 1896, 1897, 1898]:**

> ADAMS, GEORGE P.—Recorder of titles, Tasmania, July, 1876; registrar, supreme court, April, 1885.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1876 | Recorder of titles | Tasmania | [1888, 1889, 1890, 1894, 1896, 1897, 1898] |
| 1 | 1885 | registrar, supreme court | Tasmania *(inherited from previous clause)* | [1888, 1889, 1890, 1894, 1896, 1897, 1898] |

## Candidate stint `Adams, G. P___Tasmania___1877`

- Staff-list name: **Adams, G. P** | colony: **Tasmania** | listed 1877–1894 | editions [1877, 1878, 1879, 1880, 1888, 1889, 1894]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | G. P. Adams | Solicitor-General | Judicial and Legal Departments | — | — |
| 1878 | G. P. Adams | Recorder of Titles | Miscellaneous Offices | — | — |
| 1879 | G. P. Adams | Recorder of Titles | Miscellaneous Offices | — | — |
| 1880 | G. P. Adams | Recorder of Titles | Miscellaneous Offices | — | — |
| 1888 | G. P. Adams | Registrar of Deeds and Collector of Stamp Duties, and Registrar and Collector of Probate Duties | Supreme Court | — | — |
| 1889 | G. P. Adams | Registrar of Deeds and Collector of Stamp Duties, and Registrar and Collector of Probate Duties | Supreme Court | — | — |
| 1894 | G. P. Adams | Registrar of Deeds and Collector of Stamp Duties, and Registrar and Collector of Probate Duties | Supreme Court | — | — |

### Deterministic checks: `adams_george-p_e1876` vs `Adams, G. P___Tasmania___1877`

- [PASS] surname_gate: bio 'ADAMS' vs stint 'Adams, G. P' (exact)
- [PASS] initials: bio ['G', 'P'] ~ stint ['G', 'P']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Tasmania'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1877-1894
- [PASS] position_sim: best 100 vs bar 60: 'Recorder of titles' ~ 'Recorder of Titles'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

### Deterministic checks: `adams_george-p_e1876-2` vs `Adams, G. P___Tasmania___1877`

- [PASS] surname_gate: bio 'ADAMS' vs stint 'Adams, G. P' (exact)
- [PASS] initials: bio ['G', 'P'] ~ stint ['G', 'P']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [PASS] colony: 2 placed event(s) resolve to 'Tasmania'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1877-1894
- [PASS] position_sim: best 100 vs bar 60: 'Recorder of titles' ~ 'Recorder of Titles'
- [FAIL] honour: no shared honour
- [PASS] edition_cooccurrence: 3 agreeing edition-year(s) [1888, 1889, 1894] pos~56 (bar: >=2)
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

