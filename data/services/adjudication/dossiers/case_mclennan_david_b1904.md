<!-- {"case_id": "case_mclennan_david_b1904", "bio_ids": ["mclennan_david_b1904"], "stint_ids": ["McLennan, D___Gold Coast___1927"]} -->
# Dossier case_mclennan_david_b1904

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 8 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['mclennan_david_b1904'] carry a single initial only — the namesake trap applies.

## Biography `mclennan_david_b1904`

- Printed name: **MCLENNAN, DAVID**
- Birth year: 1904 (attested in editions [1940])
- Appears in editions: [1940]

### Verbatim printed entry text (OCR)

**Version `col1940-L66490.v` — printed in editions [1940]:**

> MCLENNAN, DAVID, M.A. (Cantab).—B. 1904; asst. mast., educn. dept., Hong Kong, 1931.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1931 | asst. mast., educn. dept. | Hong Kong | [1940] |

## Candidate stint `McLennan, D___Gold Coast___1927`

- Staff-list name: **McLennan, D** | colony: **Gold Coast** | listed 1927–1930 | editions [1927, 1928, 1929, 1930]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1927 | D. McLennan | District Surveyor | Posts and Telegraphs Department | — | — |
| 1928 | D. McLennan | District Surveyors | Posts and Telegraphs Department | — | — |
| 1929 | D. McLennan | District Surveyor | Posts and Telegraphs Department | — | — |
| 1930 | D. McLennan | District Surveyor | Posts and Telegraphs Department | — | — |

### Deterministic checks: `mclennan_david_b1904` vs `McLennan, D___Gold Coast___1927`

- [PASS] surname_gate: bio 'MCLENNAN' vs stint 'McLennan, D' (exact)
- [PASS] initials: bio ['D'] ~ stint ['D']
- [PASS] age_gate: stint starts 1927, birth 1904 (age 23)
- [FAIL] colony: no placed event resolves to 'Gold Coast'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1927-1930
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

