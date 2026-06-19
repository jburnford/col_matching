<!-- {"case_id": "case_allport_roland-harrison_b1876", "bio_ids": ["allport_roland-harrison_b1876"], "stint_ids": ["Allport, H___Northern Rhodesia___1925", "Allport, R. Harrison___Leeward Islands___1912"]} -->
# Dossier case_allport_roland-harrison_b1876

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 4 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `allport_roland-harrison_b1876`

- Printed name: **ALLPORT, ROLAND HARRISON**
- Birth year: 1876 (attested in editions [1912, 1913, 1914, 1915, 1917, 1918, 1919])
- Appears in editions: [1912, 1913, 1914, 1915, 1917, 1918, 1919]

### Verbatim printed entry text (OCR)

**Version `col1912-L42182.v` — printed in editions [1912, 1913, 1914, 1915, 1917, 1918, 1919]:**

> ALLPORT, ROLAND HARRISON, M.R.C.S., Eng.; L.R.C.P., Lond.; b. 1876; med. offr., Dist. A., Dominica, June, 1910.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1910 | med. offr., Dist. A. | Dominica | [1912, 1913, 1914, 1915, 1917, 1918, 1919] |

## Candidate stint `Allport, H___Northern Rhodesia___1925`

- Staff-list name: **Allport, H** | colony: **Northern Rhodesia** | listed 1925–1934 | editions [1925, 1927, 1928, 1929, 1930, 1931, 1933, 1934]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1925 | H. Allport | Lieutenant | Military Branch | — | — |
| 1927 | H. Allport | Lieutenants | Military Branch | — | — |
| 1928 | H. Allport | Captain | Military Branch | — | Captain |
| 1929 | H. Allport | Captain | Military Branch | — | Captain |
| 1930 | H. Allport | Captain | Military Branch | — | — |
| 1931 | H. Allport | Captain | Military Branch | — | Captain |
| 1933 | H. Allport | Captain | Northern Rhodesia Police (Military) | — | Captain |
| 1934 | H. Allport | Captain | Northern Rhodesia Police (Military) | — | — |

### Deterministic checks: `allport_roland-harrison_b1876` vs `Allport, H___Northern Rhodesia___1925`

- [PASS] surname_gate: bio 'ALLPORT' vs stint 'Allport, H' (exact)
- [PASS] initials: bio ['R', 'H'] ~ stint ['H']
- [PASS] age_gate: stint starts 1925, birth 1876 (age 49)
- [FAIL] colony: no placed event resolves to 'Northern Rhodesia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1925-1934
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Allport, R. Harrison___Leeward Islands___1912`

- Staff-list name: **Allport, R. Harrison** | colony: **Leeward Islands** | listed 1912–1919 | editions [1912, 1913, 1914, 1915, 1917, 1918, 1919]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1912 | R. Harrison Allport | Medical Officer, District A. | Medical Establishment | — | — |
| 1912 | R. H. Allport | Port Health Officers, Roseau | Medical Establishment | — | — |
| 1913 | R. H. Allport | Port Health Officer | Medical Establishment | — | — |
| 1913 | R. Harrison Allport | Medical Officer, District A. | Medical Establishment | — | — |
| 1914 | R. Harrison Allport | Medical Officer, District A. | Medical Establishment | — | — |
| 1914 | R. H. Allport | Port Health Officer | Medical Establishment | — | — |
| 1915 | R. Harrison Allport | Medical Officer, District A. | Medical Establishment | — | — |
| 1915 | R. H. Allport | Port Health Officer | Medical Establishment | — | — |
| 1917 | R. Harrison Allport | Medical Officer, District A. | Medical Establishment | — | — |
| 1917 | R. H. Allport | Port Health Officers | Medical Establishment | — | — |
| 1918 | R. Harrison Allport | Medical Officer, District A. | Medical Establishment | — | — |
| 1918 | R. H. Allport | Port Health Officer, Roseau | Medical Establishment | — | — |
| 1919 | R. Harrison Allport | Medical Officer, District A. | Medical Establishment | — | — |
| 1919 | R. H. Allport | Official Member | Legislative Council | — | — |
| 1919 | R. H. Allport | Port Health Officer | Medical Establishment | — | — |

### Deterministic checks: `allport_roland-harrison_b1876` vs `Allport, R. Harrison___Leeward Islands___1912`

- [PASS] surname_gate: bio 'ALLPORT' vs stint 'Allport, R. Harrison' (exact)
- [PASS] initials: bio ['R', 'H'] ~ stint ['R', 'H']
- [PASS] age_gate: stint starts 1912, birth 1876 (age 36)
- [FAIL] colony: no placed event resolves to 'Leeward Islands'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1912-1919
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

