<!-- {"case_id": "case_creasey_harold-william_b1908", "bio_ids": ["creasey_harold-william_b1908"], "stint_ids": ["Creasey, H. W___Uganda___1940"]} -->
# Dossier case_creasey_harold-william_b1908

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `creasey_harold-william_b1908`

- Printed name: **CREASEY, Harold William**
- Birth year: 1908 (attested in editions [1949, 1951])
- Honours: C.P.M. (1950)
- Appears in editions: [1948, 1949, 1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1949-L31390.v` — printed in editions [1949, 1951]:**

> CREASEY, Harold William, C.P.M. (1950).—b. 1908; ed. King Edward VII's Gram. Sch., King's Lynn, Norfolk; on naval serv., 1940–44, lieut.; police const., B.S.A., 1927; trooper, N. Rhod., 1929; asst. inspr., 1930; Uga., 1934; inspr., 1941; asst. supt., 1941; senr. supt., 1950.

**Version `col1948-L32022.v` — printed in editions [1948, 1950]:**

> CREASY, Harold William.—b. 1908; ed. King Edward VII’s Gram. Sch., King’s Lynn, Norfolk; on naval serv. 1940-44, lieut.; police const., Br.S.A., 1927; trooper, N. Rhod., 1929; asst. inspr., 1930; Uga., 1934; inspr., 1941; asst. supt., 1941.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1927–1927 | police const. | British South Africa | [1948, 1949, 1950, 1951] |
| 1 | 1929–1929 | trooper | Northern Rhodesia | [1948, 1949, 1950, 1951] |
| 2 | 1930–1930 | asst. inspr. | — | [1948, 1949, 1950, 1951] |
| 3 | 1934–1934 | — | Uganda | [1948, 1949, 1950, 1951] |
| 4 | 1940–1944 | lieut. | — | [1948, 1949, 1950, 1951] |
| 5 | 1941–1941 | inspr. | — | [1948, 1949, 1950, 1951] |
| 6 | 1941–1941 | asst. supt. | — | [1948, 1949, 1950, 1951] |
| 7 | 1950–1950 | senr. supt. | — | [1949, 1951] |

## Candidate stint `Creasey, H. W___Uganda___1940`

- Staff-list name: **Creasey, H. W** | colony: **Uganda** | listed 1940–1951 | editions [1940, 1949, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1940 | H. W. Creasey | Inspector | Police | — | — |
| 1949 | H. W. Creasey | Superintendents, Assistants and Cadets | Police | — | — |
| 1951 | H. W. Creasey | Senior Superintendents | Police | — | — |

### Deterministic checks: `creasey_harold-william_b1908` vs `Creasey, H. W___Uganda___1940`

- [PASS] surname_gate: bio 'CREASEY' vs stint 'Creasey, H. W' (exact)
- [PASS] initials: bio ['H', 'W'] ~ stint ['H', 'W']
- [PASS] age_gate: stint starts 1940, birth 1908 (age 32)
- [PASS] colony: 1 placed event(s) resolve to 'Uganda'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1940-1951
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

