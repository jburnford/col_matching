<!-- {"case_id": "case_waterman_james-arnold_b1895", "bio_ids": ["waterman_james-arnold_b1895"], "stint_ids": ["Waterman, J. A___Trinidad and Tobago___1927"]} -->
# Dossier case_waterman_james-arnold_b1895

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `waterman_james-arnold_b1895`

- Printed name: **WATERMAN, James Arnold**
- Birth year: 1895 (attested in editions [1954, 1955])
- Honours: M.B
- Appears in editions: [1948, 1949, 1950, 1951, 1954, 1955]

### Verbatim printed entry text (OCR)

**Version `col1954-L22758.v` — printed in editions [1954, 1955]:**

> WATERMAN, J. A.—b. 1895; ed. Queen's Royal Coll., Trin., and Univ. of Glasgow; asst. surg., col. hosp., Trin., 1925; M.O., 1935; obstetrician, 1940; D.D.M.S., 1953.

**Version `col1948-L36683.v` — printed in editions [1948, 1949, 1950, 1951]:**

> WATERMAN, James Arnold, M.B., Ch.B. (Glas.), D.T.M. & H., L.M.Rotunda, M.D. (comd.), M.R.C.O.G. (Lond.).—b. 1895; ed. Queen’s Royal Coll., Trinidad, Univ. of Glasgow; asst. surg., col. hosp., Trin., 1925; med. offr., 1935; med. offr., obstetrician, 1940; founder and edr. of the Caribbean Med. Journal, author of Some notes on scorpion poisoning (T. trinitatis), Some observations on the Habits and Life of the Common Scorpion of Trinidad, Haemorrhagic Retinitis in Vomiting of Pregnancy; Acute Rheumatic Fever and Rheumatic Carditis in the Tropics with special reference to Trinidad.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1925 | asst. surg., col. hosp. | Trinidad | [1948, 1949, 1950, 1951, 1954, 1955] |
| 1 | 1935 | M.O | Trinidad *(inherited from previous clause)* | [1948, 1949, 1950, 1951, 1954, 1955] |
| 2 | 1940 | obstetrician | Trinidad *(inherited from previous clause)* | [1948, 1949, 1950, 1951, 1954, 1955] |
| 3 | 1953 | D.D.M.S | Trinidad *(inherited from previous clause)* | [1954, 1955] |

## Candidate stint `Waterman, J. A___Trinidad and Tobago___1927`

- Staff-list name: **Waterman, J. A** | colony: **Trinidad and Tobago** | listed 1927–1937 | editions [1927, 1928, 1929, 1931, 1933, 1934, 1937]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1927 | J. A. Waterman | Medical Officer | Government Medical Officers | — | — |
| 1928 | J. A. Waterman | — | Government Medical Officers | — | — |
| 1929 | J. A. Waterman | — | Government Medical Officers | — | — |
| 1931 | J. A. Waterman | — | Government Medical Officers | — | — |
| 1933 | J. A. Waterman | Medical Officer | Medical Establishment | — | — |
| 1934 | J. A. Waterman | Medical Officer | Government Medical Officers | — | — |
| 1937 | J. A. Waterman | Medical Officer | Medical Officers | — | — |

### Deterministic checks: `waterman_james-arnold_b1895` vs `Waterman, J. A___Trinidad and Tobago___1927`

- [PASS] surname_gate: bio 'WATERMAN' vs stint 'Waterman, J. A' (exact)
- [PASS] initials: bio ['J', 'A'] ~ stint ['J', 'A']
- [PASS] age_gate: stint starts 1927, birth 1895 (age 32)
- [FAIL] colony: no placed event resolves to 'Trinidad and Tobago'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1927-1937
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

