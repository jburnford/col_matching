<!-- {"case_id": "case_penny_william-hughes_e1888", "bio_ids": ["penny_william-hughes_e1888"], "stint_ids": ["Penny, W___Ceylon___1877"]} -->
# Dossier case_penny_william-hughes_e1888

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 13 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `penny_william-hughes_e1888`

- Printed name: **PENNY, WILLIAM HUGHES**
- Birth year: not printed
- Appears in editions: [1910]

### Verbatim printed entry text (OCR)

**Version `col1910-L48041.v` — printed in editions [1910]:**

> PENNY, WILLIAM HUGHES.—Ed. Hymer's Coll., Yorkshire; apptd. to treasy. dept., B. N. Borneo, July, 1888; ag. treas.-genl., 1891; P.M.G., 1895; dis. mag., 1896; ag. res., Prov. Alcock, 1898; prot. of Chinese and mem. of coun., 1901; supt. of customs, 1902; resident and dep. gov., Labuan, Jan., 1903.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1888 | apptd. to treasy. dept., B. N. Borneo | — | [1910] |
| 1 | 1891 | ag. treas.-genl | — | [1910] |
| 2 | 1895 | P.M.G | — | [1910] |
| 3 | 1896 | dis. mag | — | [1910] |
| 4 | 1898 | ag. res., Prov. Alcock | — | [1910] |
| 5 | 1901 | prot. of Chinese and mem. of coun | — | [1910] |
| 6 | 1902 | supt. of customs | — | [1910] |
| 7 | 1903 | resident and dep. gov. | Labuan | [1910] |

## Candidate stint `Penny, W___Ceylon___1877`

- Staff-list name: **Penny, W** | colony: **Ceylon** | listed 1877–1878 | editions [1877, 1878]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | W. Penny | Office Assistant | Government Agencies | — | — |
| 1878 | W. Penny | Office Assistant | Government Agencies | — | — |

### Deterministic checks: `penny_william-hughes_e1888` vs `Penny, W___Ceylon___1877`

- [PASS] surname_gate: bio 'PENNY' vs stint 'Penny, W' (exact)
- [PASS] initials: bio ['W', 'H'] ~ stint ['W']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Ceylon'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1877-1878
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

