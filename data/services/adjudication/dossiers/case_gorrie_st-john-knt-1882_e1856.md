<!-- {"case_id": "case_gorrie_st-john-knt-1882_e1856", "bio_ids": ["gorrie_st-john-knt-1882_e1856"], "stint_ids": ["Gorrie, John___Fiji___1877", "Gorrie, John___Trinidad___1888"]} -->
# Dossier case_gorrie_st-john-knt-1882_e1856

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 4 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Gorrie, John___Fiji___1877` is also gate-compatible with biography(ies) outside this case: ['gorrie_john_e1856'] (already linked elsewhere or filtered).
- NOTE: stint `Gorrie, John___Trinidad___1888` is also gate-compatible with biography(ies) outside this case: ['gorrie_john_e1856'] (already linked elsewhere or filtered).

## Biography `gorrie_st-john-knt-1882_e1856`

- Printed name: **GORRIE, ST JOHN (KNT. 1882)**
- Birth year: not printed
- Appears in editions: [1883]

### Verbatim printed entry text (OCR)

**Version `col1883-L27703.v` — printed in editions [1883]:**

> GORRIE, ST JOHN (KNT. 1882).—Called to the bar of Scotland, 1856; Captain Q.E.R.V., 1859; one of the honorary advocate-deputies for Scotland, 1860; practised in London, 1862 to 1869; counsel for Jamaica Committee before Royal Commission in that colony, 1866; substitute-procurer and advocate-general, Mauritius, 10th Aug., 1869; 3rd puisne judge, supreme court, 5th Sept., 1870; 2nd puisne judge, 12th Sept., 1870; member of the police and old immigrants inquiry commission, 1872; president of the council of education, 1874-6; acting 1st puisne judge, April, 1875; chief justice of Fiji, March, 1876; chief justice of Leeward Islands, 1882.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1856 | Called to the bar of Scotland | — | [1883] |
| 1 | 1859 | Captain Q.E.R.V | — | [1883] |
| 2 | 1860 | one of the honorary advocate-deputies for Scotland | — | [1883] |
| 3 | 1862–1869 | practised in London | — | [1883] |
| 4 | 1866 | counsel for Jamaica Committee before Royal Commission in that colony | — | [1883] |
| 5 | 1869 | substitute-procurer and advocate-general | Mauritius | [1883] |
| 6 | 1870 | 3rd puisne judge, supreme court | Mauritius *(inherited from previous clause)* | [1883] |
| 7 | 1872 | member of the police and old immigrants inquiry commission | Mauritius *(inherited from previous clause)* | [1883] |
| 8 | 1874–1876 | president of the council of education | Mauritius *(inherited from previous clause)* | [1883] |
| 9 | 1875 | acting 1st puisne judge | Mauritius *(inherited from previous clause)* | [1883] |
| 10 | 1876 | chief justice of Fiji | Mauritius *(inherited from previous clause)* | [1883] |
| 11 | 1882 | chief justice of Leeward Islands | Mauritius *(inherited from previous clause)* | [1883] |

## Candidate stint `Gorrie, John___Fiji___1877`

- Staff-list name: **Gorrie, John** | colony: **Fiji** | listed 1877–1880 | editions [1877, 1878, 1879, 1880]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | John Gorrie | Acting Chief Justice | Civil Establishment | — | — |
| 1878 | John Gorrie | Chief Justice | — | — | — |
| 1879 | John Gorrie | Chief Justice | Civil Establishment | — | — |
| 1880 | John Gorrie | Chief Justice | — | — | — |

### Deterministic checks: `gorrie_st-john-knt-1882_e1856` vs `Gorrie, John___Fiji___1877`

- [PASS] surname_gate: bio 'GORRIE' vs stint 'Gorrie, John' (exact)
- [PASS] initials: bio ['S', 'J'] ~ stint ['J']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Fiji'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1877-1880
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Gorrie, John___Trinidad___1888`

- Staff-list name: **Gorrie, John** | colony: **Trinidad** | listed 1888–1890 | editions [1888, 1889, 1890]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1888 | Sir John Gorrie | Chief Justice | Judicial Department | — | — |
| 1889 | Sir John Gorrie | Chief Justice | Judicial Department | — | — |
| 1890 | John Gorrie | Chief Justice | Judicial Department | — | — |

### Deterministic checks: `gorrie_st-john-knt-1882_e1856` vs `Gorrie, John___Trinidad___1888`

- [PASS] surname_gate: bio 'GORRIE' vs stint 'Gorrie, John' (exact)
- [PASS] initials: bio ['S', 'J'] ~ stint ['J']
- [PASS] age_gate: stint starts 1888; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Trinidad'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1888-1890
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

