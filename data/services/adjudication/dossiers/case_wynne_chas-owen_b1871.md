<!-- {"case_id": "case_wynne_chas-owen_b1871", "bio_ids": ["wynne_chas-owen_b1871"], "stint_ids": ["Wynne, C. O___Leeward Islands___1905"]} -->
# Dossier case_wynne_chas-owen_b1871

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 12 official(s) with this surname in the graph's staff lists; 6 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `wynne_chas-owen_b1871`

- Printed name: **WYNNE, CHAS. OWEN**
- Birth year: 1871 (attested in editions [1908, 1909, 1910, 1911, 1912])
- Appears in editions: [1908, 1909, 1910, 1911, 1912]

### Verbatim printed entry text (OCR)

**Version `col1908-L48352.v` — printed in editions [1908, 1909, 1910, 1911, 1912]:**

> WYNNE, CHAS. OWEN, L.R.C.P. and S.E.—B. 1871; dist. med. offr., St. Kitts, Leeward Is., May, 1903; ag. comsnr., mag., and med. offr., Virgin Is., May, 1906; dist. med. offr., Nevis, Feb., 1907; ag. sen. med. offr., med. offr. of health and mem. of bd. of health, Montserrat, Aug., 1911.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1903 | dist. med. offr., St. Kitts, Leeward Is | — | [1908, 1909, 1910, 1911, 1912] |
| 1 | 1906 | ag. comsnr., mag., and med. offr., Virgin Is | — | [1908, 1909, 1910, 1911, 1912] |
| 2 | 1907 | dist. med. offr. | Nevis | [1908, 1909, 1910, 1911, 1912] |
| 3 | 1911 | ag. sen. med. offr., med. offr. of health and mem. of bd. of health | Montserrat | [1908, 1909, 1910, 1911, 1912] |

## Candidate stint `Wynne, C. O___Leeward Islands___1905`

- Staff-list name: **Wynne, C. O** | colony: **Leeward Islands** | listed 1905–1912 | editions [1905, 1906, 1907, 1908, 1911, 1912]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1905 | C. O. Wynne | Additional Medical Officer, Dieppe Bay | District Medical Officers | — | — |
| 1906 | C. O. Wynne | Senior Medical Officer, District No. 4 | Hospitals | — | — |
| 1907 | C. O. Wynne | Senior Medical Officer, District No. 4 | District Medical Officers | — | — |
| 1908 | C. O. Wynne | Senior Medical Officer | District Medical Officers | — | — |
| 1911 | C. O. Wynne | District Medical Officer, No. 7 | District Medical Officers | — | — |
| 1912 | C. O. Wynne | District Medical Officer | Nevis | — | — |

### Deterministic checks: `wynne_chas-owen_b1871` vs `Wynne, C. O___Leeward Islands___1905`

- [PASS] surname_gate: bio 'WYNNE' vs stint 'Wynne, C. O' (exact)
- [PASS] initials: bio ['C', 'O'] ~ stint ['C', 'O']
- [PASS] age_gate: stint starts 1905, birth 1871 (age 34)
- [FAIL] colony: no placed event resolves to 'Leeward Islands'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1905-1912
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

