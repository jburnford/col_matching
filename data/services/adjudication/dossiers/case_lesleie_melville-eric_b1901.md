<!-- {"case_id": "case_lesleie_melville-eric_b1901", "bio_ids": ["lesleie_melville-eric_b1901"], "stint_ids": ["Leslie, M. E___Nyasaland___1930", "Leslie, M. E___Nyasaland___1939"]} -->
# Dossier case_lesleie_melville-eric_b1901

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 20 official(s) with this surname in the graph's staff lists; 4 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `lesleie_melville-eric_b1901`

- Printed name: **LESLEIE, Melville Eric**
- Birth year: 1901 (attested in editions [1949, 1950])
- Honours: O.B.E. (1948)
- Appears in editions: [1948, 1949, 1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1949-L33630.v` — printed in editions [1949, 1950]:**

> LESLEIE, Melville Eric, O.B.E. (1948).—b. 1901; ed. R.N. Coils., Osborne and Dartmouth; on naval serv. 1915-20 and mil. serv. 1940, 2nd lieut.; cadet, Nyasa., 1925; labour comsnt., 1944; O/C refugee camp, internment camp, fiscal survey, 1947.

**Version `col1951-L40023.v` — printed in editions [1951]:**

> LESLIE, Melville Eric, O.B.E. (1948).—b. 1901; ed. R.N. Colls., Osborne and Dartmouth; on naval serv. 1915–20 and mil. serv. 1940, 2nd lieut.; cadet, Nyasa, 1925; labour comsnr., 1944; O/C refugee camp, internment camp, fiscal survey, 1947.

**Version `col1948-L34012.v` — printed in editions [1948]:**

> LESLEI, Melville Eric.—b. 1901; ed. R.N. Colls., Osborne and Dartmouth; on naval serv. 1915-20 and mil. serv. 1940, 2nd lieut.; cadet, Nyasa., 1925; labour comsnr., 1944; O/C refugee camp, internment camp, fiscal survey, 1947.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1915–1920 | on naval serv. | — | [1948, 1949, 1950, 1951] |
| 1 | 1925–1925 | cadet | Nyasaland | [1948, 1949, 1950, 1951] |
| 2 | 1940–1940 | mil. serv., 2nd lieut. | — | [1948, 1949, 1950, 1951] |
| 3 | 1944–1944 | labour comsnt. | — | [1948, 1949, 1950, 1951] |
| 4 | 1947–1947 | O/C refugee camp, internment camp, fiscal survey | — | [1948, 1949, 1950, 1951] |

## Candidate stint `Leslie, M. E___Nyasaland___1930`

- Staff-list name: **Leslie, M. E** | colony: **Nyasaland** | listed 1930–1934 | editions [1930, 1931, 1932, 1934]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1930 | M. E. Leslie | Assistant District Officers | District Staff | — | — |
| 1931 | M. E. Leslie | Assistant District Officer | District Staff | — | — |
| 1932 | M. E. Leslie | Assistant District Officer | District Staff | — | — |
| 1934 | M. E. Leslie | Assistant District Officer | District Staff | — | — |

### Deterministic checks: `lesleie_melville-eric_b1901` vs `Leslie, M. E___Nyasaland___1930`

- [PASS] surname_gate: bio 'LESLEIE' vs stint 'Leslie, M. E' (fuzzy:1)
- [PASS] initials: bio ['M', 'E'] ~ stint ['M', 'E']
- [PASS] age_gate: stint starts 1930, birth 1901 (age 29)
- [PASS] colony: 1 placed event(s) resolve to 'Nyasaland'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1930-1934
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Leslie, M. E___Nyasaland___1939`

- Staff-list name: **Leslie, M. E** | colony: **Nyasaland** | listed 1939–1940 | editions [1939, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1939 | M. E. Leslie | District Officer | District Staff | — | — |
| 1940 | M. E. Leslie | District Officer | District Staff | — | — |

### Deterministic checks: `lesleie_melville-eric_b1901` vs `Leslie, M. E___Nyasaland___1939`

- [PASS] surname_gate: bio 'LESLEIE' vs stint 'Leslie, M. E' (fuzzy:1)
- [PASS] initials: bio ['M', 'E'] ~ stint ['M', 'E']
- [PASS] age_gate: stint starts 1939, birth 1901 (age 38)
- [PASS] colony: 1 placed event(s) resolve to 'Nyasaland'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1939-1940
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

