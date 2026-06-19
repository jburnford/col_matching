<!-- {"case_id": "case_morse_leonard-kearney_b1908", "bio_ids": ["morse_leonard-kearney_b1908"], "stint_ids": ["Morse, L. K___North Borneo___1930", "Morse, L. K___Sarawak___1949"]} -->
# Dossier case_morse_leonard-kearney_b1908

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 5 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `morse_leonard-kearney_b1908`

- Printed name: **MORSE, Leonard Kearney**
- Birth year: 1908 (attested in editions [1948, 1949, 1950, 1951, 1953, 1954, 1955])
- Appears in editions: [1948, 1949, 1950, 1951, 1953, 1954, 1955]

### Verbatim printed entry text (OCR)

**Version `col1948-L34794.v` — printed in editions [1948, 1949, 1950, 1951, 1953, 1954, 1955]:**

> MORSE, Leonard Kearney.—b. 1908; ed. Kingstown Gram. Sch., Eire; on mil. serv., 1942-46, capt.; cadet, Sarawak C.S., 1928; admin. offr., cl. III, 1933; cl. II, 1941; cl. IB, 1946.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1928 | cadet, Sarawak C.S | Sarawak | [1948, 1949, 1950, 1951, 1953, 1954, 1955] |
| 1 | 1933 | admin. offr., cl. III | Sarawak *(inherited from previous clause)* | [1948, 1949, 1950, 1951, 1953, 1954, 1955] |
| 2 | 1941 | cl. II | Sarawak *(inherited from previous clause)* | [1948, 1949, 1950, 1951, 1953, 1954, 1955] |
| 3 | 1946 | cl. IB | Sarawak *(inherited from previous clause)* | [1948, 1949, 1950, 1951, 1953, 1954, 1955] |

## Candidate stint `Morse, L. K___North Borneo___1930`

- Staff-list name: **Morse, L. K** | colony: **North Borneo** | listed 1930–1932 | editions [1930, 1932]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1930 | L. K. Morse | Cadet | Civil Establishment | — | — |
| 1932 | L. K. Morse | Cadet | Civil Establishment | — | — |

### Deterministic checks: `morse_leonard-kearney_b1908` vs `Morse, L. K___North Borneo___1930`

- [PASS] surname_gate: bio 'MORSE' vs stint 'Morse, L. K' (exact)
- [PASS] initials: bio ['L', 'K'] ~ stint ['L', 'K']
- [PASS] age_gate: stint starts 1930, birth 1908 (age 22)
- [FAIL] colony: no placed event resolves to 'North Borneo'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1930-1932
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Morse, L. K___Sarawak___1949`

- Staff-list name: **Morse, L. K** | colony: **Sarawak** | listed 1949–1954 | editions [1949, 1950, 1951, 1952, 1953, 1954]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | L. K. Morse | Resident | Administrative Service | — | — |
| 1950 | L. K. Morse | Residents | Administrative Service | — | — |
| 1951 | L. K. Morse | Residents | Administrative Service | — | — |
| 1952 | L. K. Morse | Resident | Civil Establishment | — | — |
| 1953 | L. K. Morse | Resident | Civil Establishment | — | — |
| 1954 | L. K. Morse | Resident | Civil Establishment | — | — |

### Deterministic checks: `morse_leonard-kearney_b1908` vs `Morse, L. K___Sarawak___1949`

- [PASS] surname_gate: bio 'MORSE' vs stint 'Morse, L. K' (exact)
- [PASS] initials: bio ['L', 'K'] ~ stint ['L', 'K']
- [PASS] age_gate: stint starts 1949, birth 1908 (age 41)
- [PASS] colony: 4 placed event(s) resolve to 'Sarawak'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1949-1954
- [FAIL] position_sim: best 15 vs bar 60: 'cl. IB' ~ 'Resident'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: ALL supporting events inherit their place from an earlier clause — weak evidence

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

