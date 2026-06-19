<!-- {"case_id": "case_valladares_eric_b1908", "bio_ids": ["valladares_eric_b1908"], "stint_ids": ["Valladares, E___British Guiana___1929"]} -->
# Dossier case_valladares_eric_b1908

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['valladares_eric_b1908'] carry a single initial only — the namesake trap applies.

## Biography `valladares_eric_b1908`

- Printed name: **VALLADARES, ERIC**
- Birth year: 1908 (attested in editions [1939, 1940])
- Appears in editions: [1937, 1939, 1940]

### Verbatim printed entry text (OCR)

**Version `col1939-L71367.v` — printed in editions [1939, 1940]:**

> VALLADARES, ERIC.—B. 1908; ed. Dan. Stewart's Coll., Edinburgh; clk., transp. dept., Br. Guiana, 1924; cler. asst., med. dept., 1926; prob. offr. of cust., 1927; 6th cls. clerk., col. sec.'s office, 1932; 5th do., 1933; clk., leg. coun., May, 1936.

**Version `col1937-L65466.v` — printed in editions [1937]:**

> VALLADARES, ERIC, M.R.C.S. (Eng.), Stewart's Coll., Edinburgh; Br. Guiana, 1924; cler. and prob. offr. of cust., 1927; oiv. office, 1932; 5th do., 1933, 1936.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1924 | clk., transp. dept. | British Guiana | [1937, 1939, 1940] |
| 1 | 1926 | cler. asst., med. dept | British Guiana *(inherited from previous clause)* | [1939, 1940] |
| 2 | 1927 | prob. offr. of cust | British Guiana *(inherited from previous clause)* | [1937, 1939, 1940] |
| 3 | 1932 | 6th cls. clerk., col. sec.'s office | British Guiana *(inherited from previous clause)* | [1937, 1939, 1940] |
| 4 | 1933 | 5th do | British Guiana *(inherited from previous clause)* | [1937, 1939, 1940] |
| 5 | 1936 | clk., leg. coun | British Guiana *(inherited from previous clause)* | [1939, 1940] |

## Candidate stint `Valladares, E___British Guiana___1929`

- Staff-list name: **Valladares, E** | colony: **British Guiana** | listed 1929–1930 | editions [1929, 1930]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1929 | E. Valladares | Asst. Permanent Way Inspector | Engineering (Maintenance) Branch | — | — |
| 1930 | E. Valladares | Ass't Permanent Way Inspector | Engineering (Maintenance) Branch | — | — |

### Deterministic checks: `valladares_eric_b1908` vs `Valladares, E___British Guiana___1929`

- [PASS] surname_gate: bio 'VALLADARES' vs stint 'Valladares, E' (exact)
- [PASS] initials: bio ['E'] ~ stint ['E']
- [PASS] age_gate: stint starts 1929, birth 1908 (age 21)
- [PASS] colony: 6 placed event(s) resolve to 'British Guiana'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1929-1930
- [FAIL] position_sim: best 36 vs bar 60: 'prob. offr. of cust' ~ 'Asst. Permanent Way Inspector'
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

