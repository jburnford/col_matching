<!-- {"case_id": "case_birt_charles-frederick_b1903", "bio_ids": ["birt_charles-frederick_b1903"], "stint_ids": ["Birt, C. F___Sarawak___1940"]} -->
# Dossier case_birt_charles-frederick_b1903

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 7 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `birt_charles-frederick_b1903`

- Printed name: **BIRT, Charles Frederick**
- Birth year: 1903 (attested in editions [1948, 1949, 1950, 1951, 1953, 1954, 1955, 1956])
- Honours: A.M.I.C.E
- Appears in editions: [1948, 1949, 1950, 1951, 1953, 1954, 1955, 1956]

### Verbatim printed entry text (OCR)

**Version `col1948-L31204.v` — printed in editions [1948, 1949, 1950, 1951, 1953, 1954, 1955, 1956]:**

> BIRT, Charles Frederick, B.Sc., A.M.I.C.E.—b. 1903; ed. King Edward's Sch., Birmingham and Birmingham Univ.; on mil. serv., 1941-46, liqut.-col.; asst. exec. engrn., Sarawak, P.W.D., 1928; exec. engrn., 1935; ag. D.P.W., 1941; ch. engrn., C.O., Borneo planning unit, 1944; super-scale "C," 1946.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1928 | asst. exec. engrn., Sarawak, P.W.D | — | [1948, 1949, 1950, 1951, 1953, 1954, 1955, 1956] |
| 1 | 1935 | exec. engrn | — | [1948, 1949, 1950, 1951, 1953, 1954, 1955, 1956] |
| 2 | 1941 | ag. D.P.W | — | [1948, 1949, 1950, 1951, 1953, 1954, 1955, 1956] |
| 3 | 1944 | ch. engrn., C.O., Borneo planning unit | Colonial Office | [1948, 1949, 1950, 1951, 1953, 1954, 1955, 1956] |
| 4 | 1946 | super-scale "C," | Colonial Office *(inherited from previous clause)* | [1948, 1949, 1950, 1951, 1953, 1954, 1955, 1956] |

## Candidate stint `Birt, C. F___Sarawak___1940`

- Staff-list name: **Birt, C. F** | colony: **Sarawak** | listed 1940–1955 | editions [1940, 1949, 1950, 1951, 1953, 1954, 1955]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1940 | C. F. Birt | Executive Engineer | Civil Establishment | — | — |
| 1949 | C. F. Birt | Executive Engineers | Public Works | — | — |
| 1950 | C. F. Birt | Deputy Director of Public Works | PUBLIC WORKS | — | — |
| 1951 | C. F. Birt | Deputy Director of Public Works | Public Works | — | — |
| 1953 | C. F. Birt | Director of Public Works | Civil Establishment | — | — |
| 1954 | C. F. Birt | Director of Public Works | Civil Establishment | — | — |
| 1955 | C. F. Birt | Director of Public Works | Civil Establishment | — | — |

### Deterministic checks: `birt_charles-frederick_b1903` vs `Birt, C. F___Sarawak___1940`

- [PASS] surname_gate: bio 'BIRT' vs stint 'Birt, C. F' (exact)
- [PASS] initials: bio ['C', 'F'] ~ stint ['C', 'F']
- [PASS] age_gate: stint starts 1940, birth 1903 (age 37)
- [FAIL] colony: no placed event resolves to 'Sarawak'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1940-1955
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

