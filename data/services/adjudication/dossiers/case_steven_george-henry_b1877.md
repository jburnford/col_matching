<!-- {"case_id": "case_steven_george-henry_b1877", "bio_ids": ["steven_george-henry_b1877"], "stint_ids": ["Steven, G. H___British Guiana___1927", "Steven, G. H___Windward Islands___1922"]} -->
# Dossier case_steven_george-henry_b1877

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 7 official(s) with this surname in the graph's staff lists; 5 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `steven_george-henry_b1877`

- Printed name: **STEVEN, GEORGE HENRY**
- Birth year: 1877 (attested in editions [1936, 1937])
- Honours: M.B
- Appears in editions: [1936, 1937]

### Verbatim printed entry text (OCR)

**Version `col1936-L64842.v` — printed in editions [1936, 1937]:**

> STEVEN, GEORGE HENRY, M.B., Ch.B., U. Edin., 1901.—B. 1877; ag. res. surg., St. Lucia, 1919; bac. M.O.H. and port health offr., Grenada, 1920-21; C.M.O. (col. surg.) St. Vincent, 1921-25; med. ser., B. Guiana, 1925; G.M.O., pub. hosp., ag. asst. res. surg., pub. hosp., Georgetown, 1926; ag. bac. and path., 1925-26; govt. bac. and path., 1926.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1919 | ag. res. surg. | St. Lucia | [1936, 1937] |
| 1 | 1920–1921 | bac. M.O.H. and port health offr. | Grenada | [1936, 1937] |
| 2 | 1921–1925 | C.M.O. (col. surg.) St. Vincent | Grenada *(inherited from previous clause)* | [1936, 1937] |
| 3 | 1925 | med. ser., B. Guiana | Grenada *(inherited from previous clause)* | [1936, 1937] |
| 4 | 1926 | G.M.O., pub. hosp., ag. asst. res. surg., pub. hosp., Georgetown | Grenada *(inherited from previous clause)* | [1936, 1937] |

## Candidate stint `Steven, G. H___British Guiana___1927`

- Staff-list name: **Steven, G. H** | colony: **British Guiana** | listed 1927–1930 | editions [1927, 1928, 1929, 1930]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1927 | G. H. Steven | Bacteriologist | Government Medical Officers | — | — |
| 1928 | G. H. Steven | Bacteriologist | Medical Department | — | — |
| 1929 | G. H. Steven | Bacteriologist | Medical Department | — | — |
| 1930 | G. H. Steven | Bacteriologist | Medical Department | — | — |

### Deterministic checks: `steven_george-henry_b1877` vs `Steven, G. H___British Guiana___1927`

- [PASS] surname_gate: bio 'STEVEN' vs stint 'Steven, G. H' (exact)
- [PASS] initials: bio ['G', 'H'] ~ stint ['G', 'H']
- [PASS] age_gate: stint starts 1927, birth 1877 (age 50)
- [FAIL] colony: no placed event resolves to 'British Guiana'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1927-1930
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Steven, G. H___Windward Islands___1922`

- Staff-list name: **Steven, G. H** | colony: **Windward Islands** | listed 1922–1925 | editions [1922, 1923, 1924, 1925]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1922 | Dr. G. H. Steven | Colonial Surgeon | Medical | — | — |
| 1923 | Dr. G. H. Steven | Colonial Surgeon | Medical | — | — |
| 1924 | G. H. Steven | Colonial Surgeon | Legislative Council | — | — |
| 1924 | Dr. G. H. Steven | Colonial Surgeon | Medical | — | — |
| 1925 | Dr. G. H. Steven | Colonial Surgeon | Medical | — | — |

### Deterministic checks: `steven_george-henry_b1877` vs `Steven, G. H___Windward Islands___1922`

- [PASS] surname_gate: bio 'STEVEN' vs stint 'Steven, G. H' (exact)
- [PASS] initials: bio ['G', 'H'] ~ stint ['G', 'H']
- [PASS] age_gate: stint starts 1922, birth 1877 (age 45)
- [FAIL] colony: no placed event resolves to 'Windward Islands'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1922-1925
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

