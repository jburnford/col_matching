<!-- {"case_id": "case_garling_henry-chas_e1894", "bio_ids": ["garling_henry-chas_e1894"], "stint_ids": ["Garling, H___Antigua___1909", "Garling, H___Leeward Islands___1906"]} -->
# Dossier case_garling_henry-chas_e1894

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Garling, H___Antigua___1909` is also gate-compatible with biography(ies) outside this case: ['garling_henry-charles_e1894'] (already linked elsewhere or filtered).
- NOTE: stint `Garling, H___Leeward Islands___1906` is also gate-compatible with biography(ies) outside this case: ['garling_henry-charles_e1894'] (already linked elsewhere or filtered).

## Biography `garling_henry-chas_e1894`

- Printed name: **GARLING, HENRY CHAS**
- Birth year: not printed
- Appears in editions: [1911]

### Verbatim printed entry text (OCR)

**Version `col1911-L44892.v` — printed in editions [1911]:**

> GARLING, HENRY CHAS.—Supt.'s asst., Skerrett's farm and school, Antigua, 18th Apr., 1894; ag. asst. supt. of agric., Feb., 1904; outdoor offr., treasy., Feb., 1905; visiting for port of St. John's, Mar., 1905; rec. wrecks, June, 1905; ag. harbmr. and 1st offr., Jan. and Feb., 1907; ag. 1st outdoor, June, 1909.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1894 | Supt.'s asst., Skerrett's farm and school | Antigua | [1911] |
| 1 | 1904 | ag. asst. supt. of agric | Antigua *(inherited from previous clause)* | [1911] |
| 2 | 1905 | outdoor offr., treasy | Antigua *(inherited from previous clause)* | [1911] |
| 3 | 1907 | ag. harbmr. and 1st offr., Jan. and | Antigua *(inherited from previous clause)* | [1911] |
| 4 | 1909 | ag. 1st outdoor | Antigua *(inherited from previous clause)* | [1911] |

## Candidate stint `Garling, H___Antigua___1909`

- Staff-list name: **Garling, H** | colony: **Antigua** | listed 1909–1921 | editions [1909, 1910, 1921]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1909 | H. Garling | Second Outdoor Officer | Treasury and Customs | — | — |
| 1910 | H. Garling | Second Outdoor Officer | Treasury and Customs | — | — |
| 1921 | H. Garling | First Outdoor Officer | Treasury and Customs | — | — |

### Deterministic checks: `garling_henry-chas_e1894` vs `Garling, H___Antigua___1909`

- [PASS] surname_gate: bio 'GARLING' vs stint 'Garling, H' (exact)
- [PASS] initials: bio ['H', 'C'] ~ stint ['H']
- [PASS] age_gate: stint starts 1909; no printed birth year — UNCHECKED
- [PASS] colony: 5 placed event(s) resolve to 'Antigua'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1909-1921
- [PASS] position_sim: best 67 vs bar 60: 'ag. 1st outdoor' ~ 'Second Outdoor Officer'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: ALL supporting events inherit their place from an earlier clause — weak evidence

## Candidate stint `Garling, H___Leeward Islands___1906`

- Staff-list name: **Garling, H** | colony: **Leeward Islands** | listed 1906–1920 | editions [1906, 1907, 1908, 1911, 1912, 1913, 1914, 1915, 1917, 1918, 1919, 1920]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1906 | H. Garling | Second Outdoor Officer | Treasury and Customs | — | — |
| 1907 | H. Garling | Second Outdoor Officer | Treasury and Customs | — | — |
| 1908 | H. Garling | Second Outdoor Officer | Treasury and Customs | — | — |
| 1911 | H. Garling | Second Outdoor Officer | Treasury and Customs | — | — |
| 1912 | H. Garling | Second Outdoor Officer | Civil Establishment | — | — |
| 1913 | H. Garling | Second Outdoor Officer | Civil Establishment | — | — |
| 1914 | H. Garling | Second Outdoor Officer | Treasury and Customs | — | — |
| 1915 | H. Garling | Second Outdoor Officer | Civil Establishment | — | — |
| 1917 | H. Garling | Second Outdoor Officer | Treasury and Customs | — | — |
| 1918 | H. Garling | Second Outdoor Officer | Treasury and Customs | — | — |
| 1919 | H. Garling | Second Outdoor Officer | Treasury and Customs | — | — |
| 1920 | H. Garling | First Outdoor Officer | Civil Establishment | — | — |

### Deterministic checks: `garling_henry-chas_e1894` vs `Garling, H___Leeward Islands___1906`

- [PASS] surname_gate: bio 'GARLING' vs stint 'Garling, H' (exact)
- [PASS] initials: bio ['H', 'C'] ~ stint ['H']
- [PASS] age_gate: stint starts 1906; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Leeward Islands'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1906-1920
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

