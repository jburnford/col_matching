<!-- {"case_id": "case_drew_john-michael_e1900", "bio_ids": ["drew_john-michael_e1900"], "stint_ids": ["Drew, John Michael___Australia___1912"]} -->
# Dossier case_drew_john-michael_e1900

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 17 official(s) with this surname in the graph's staff lists; 10 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `drew_john-michael_e1900`

- Printed name: **DREW, JOHN MICHAEL**
- Birth year: not printed
- Appears in editions: [1914, 1915, 1917, 1918]

### Verbatim printed entry text (OCR)

**Version `col1914-L45950.v` — printed in editions [1914, 1915, 1917, 1918]:**

> DREW, HON. JOHN MICHAEL, M.L.C., W. Australia since 1900; min. for lands, 1904-5; col. sec., 1906; col. sec. since Oct., 1911.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1900 | — | Western Australia | [1914, 1915, 1917, 1918] |
| 1 | 1904–1905 | min. for lands | — | [1914, 1915, 1917, 1918] |
| 2 | 1906–1906 | col. sec. | — | [1914, 1915, 1917, 1918] |
| 3 | 1911 | col. sec. | — | [1914, 1915, 1917, 1918] |

## Candidate stint `Drew, John Michael___Australia___1912`

- Staff-list name: **Drew, John Michael** | colony: **Australia** | listed 1912–1927 | editions [1912, 1913, 1927]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1912 | John Michael Drew | Member of Legislative Council | Legislative Council | — | — |
| 1912 | The Hon. John Michael Drew | Colonial Secretary | Executive Council | — | — |
| 1912 | The Hon. John Michael Drew | Colonial Secretary | Colonial Secretary's Department | — | — |
| 1913 | John Michael Drew | Member | Legislative Council | — | — |
| 1913 | The Hon. John Michael Drew | Colonial Secretary | Colonial Secretary's Department | — | — |
| 1913 | John Michael Drew | Colonial Secretary | Executive Council | — | — |
| 1927 | J. Drew | Chief Secretary and Minister for Education | DEPARTMENT OF MINISTER FOR EDUCATION | — | — |
| 1927 | J. M. Drew | Chief Secretary | Chief Secretary's Department | — | — |

### Deterministic checks: `drew_john-michael_e1900` vs `Drew, John Michael___Australia___1912`

- [PASS] surname_gate: bio 'DREW' vs stint 'Drew, John Michael' (exact)
- [PASS] initials: bio ['J', 'M'] ~ stint ['J', 'M']
- [PASS] age_gate: stint starts 1912; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Australia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1912-1927
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

