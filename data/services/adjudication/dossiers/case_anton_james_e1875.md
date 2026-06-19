<!-- {"case_id": "case_anton_james_e1875", "bio_ids": ["anton_james_e1875"], "stint_ids": ["Anton, James___Grenada___1879", "Anton, James___Windward Islands___1877"]} -->
# Dossier case_anton_james_e1875

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 10 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['anton_james_e1875'] carry a single initial only — the namesake trap applies.

## Biography `anton_james_e1875`

- Printed name: **ANTON, James**
- Birth year: not printed
- Appears in editions: [1883, 1886, 1888, 1889, 1890, 1894]

### Verbatim printed entry text (OCR)

**Version `col1883-L26219.v` — printed in editions [1883, 1888, 1889, 1890, 1894]:**

> ANTON, James.—Sanitary inspector and immigration agent, Grenada, 1875; postmaster, 1877.

**Version `col1886-L31930.v` — printed in editions [1886]:**

> ANTON, JAMES.—Sanitary inspector and immigration agent, Grenada, 1875; postmaster, 1877.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1875 | Sanitary inspector and immigration agent | Grenada | [1883, 1886, 1888, 1889, 1890, 1894] |
| 1 | 1877 | postmaster | Grenada *(inherited from previous clause)* | [1883, 1886, 1888, 1889, 1890, 1894] |

## Candidate stint `Anton, James___Grenada___1879`

- Staff-list name: **Anton, James** | colony: **Grenada** | listed 1879–1880 | editions [1879, 1880]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1879 | J. Anton | Rector | Ministers of Religion | — | — |
| 1879 | James Anton | Postmaster | Revenue Officers | — | — |
| 1880 | The Very Rev. J. Anton | Rectors | Anglican Church | — | — |
| 1880 | James Anton | Postmaster | Revenue Officers | — | — |

### Deterministic checks: `anton_james_e1875` vs `Anton, James___Grenada___1879`

- [PASS] surname_gate: bio 'ANTON' vs stint 'Anton, James' (exact)
- [PASS] initials: bio ['J'] ~ stint ['J']
- [PASS] age_gate: stint starts 1879; no printed birth year — UNCHECKED
- [PASS] colony: 2 placed event(s) resolve to 'Grenada'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1879-1880
- [PASS] position_sim: best 100 vs bar 60: 'postmaster' ~ 'Postmaster'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: ALL supporting events inherit their place from an earlier clause — weak evidence

## Candidate stint `Anton, James___Windward Islands___1877`

- Staff-list name: **Anton, James** | colony: **Windward Islands** | listed 1877–1883 | editions [1877, 1878, 1880, 1883]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | J. Anton | Immigration Agent and Sanitary Inspector | Medical Officers | — | — |
| 1878 | Rev. J. Anton | Rector | Ministers of Religion – Anglican | — | — |
| 1878 | J. Anton | Immigration Agent | Medical Officers | — | — |
| 1878 | James Anton | Postmaster | Revenue Officers | — | — |
| 1880 | J. Anton | Rector | Ministers of Religion | — | — |
| 1880 | James Anton | Postmaster | Revenue Officers | — | — |
| 1883 | J. A. Anton | Rectors | Ministers of Religion | — | — |
| 1883 | James Anton | Postmaster | Revenue Officers | — | — |

### Deterministic checks: `anton_james_e1875` vs `Anton, James___Windward Islands___1877`

- [PASS] surname_gate: bio 'ANTON' vs stint 'Anton, James' (exact)
- [PASS] initials: bio ['J'] ~ stint ['J']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Windward Islands'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1877-1883
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

