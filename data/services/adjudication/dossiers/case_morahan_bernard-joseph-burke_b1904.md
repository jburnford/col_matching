<!-- {"case_id": "case_morahan_bernard-joseph-burke_b1904", "bio_ids": ["morahan_bernard-joseph-burke_b1904"], "stint_ids": ["Morahan, B. J. B___Hong Kong___1939", "Morahan, B. J. B___Hong Kong___1949"]} -->
# Dossier case_morahan_bernard-joseph-burke_b1904

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `morahan_bernard-joseph-burke_b1904`

- Printed name: **MORAHAN, Bernard Joseph Burke**
- Birth year: 1904 (attested in editions [1950, 1951])
- Honours: V.R.D
- Appears in editions: [1948, 1949, 1950, 1951, 1956]

### Verbatim printed entry text (OCR)

**Version `col1950-L38128.v` — printed in editions [1950, 1951]:**

> MORAHAN, Bernard Joseph Burke.—b. 1904; ed. The Tiffin Sch., Kingston-on-Thames, and Univ. of Lond. Goldsmiths Coll., L.P.E.A., M.R.S.T. (G.C.L.); on naval serv., 1939-46, lieut.-comdr.; physical training supvr., educ., dept., H.K., 1937; organiser, physical ed., 1947; o/c, H.K. R.N.V.R.

**Version `col1948-L34763.v` — printed in editions [1948, 1949]:**

> MORAHAN, Bernard Joseph Burke.—b. 1904; ed. The Tiffin Sch., Kingston-on-Thames (bd. of educ. cert., M.R.S.T.); on naval serv. 1939–46, lieut-comdr.; physical training supvr., educ. dept., H.K., 1937.

**Version `col1956-L23127.v` — printed in editions [1956]:**

> MORAHAN, B. J. B., V.R.D.—b. 1904; ed. Tiffin Sch., Kingston-on-Thames and Goldsmiths Coll., Univ. of London; mil. serv., 1939-46, lt.-cmdr.; organizer, physical educ., H.K., 1937; senr. educ. offr., 1954.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1937–1937 | physical training supvr., educ., dept. | Hong Kong | [1948, 1949, 1950, 1951, 1956] |
| 1 | 1939–1946 | lieut.-comdr. | — | [1948, 1949, 1950, 1951] |
| 2 | 1947–1947 | organiser, physical ed. | — | [1950, 1951] |
| 3 | 1954 | senr. educ. offr | Hong Kong *(inherited from previous clause)* | [1956] |

## Candidate stint `Morahan, B. J. B___Hong Kong___1939`

- Staff-list name: **Morahan, B. J. B** | colony: **Hong Kong** | listed 1939–1940 | editions [1939, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1939 | B. J. Morahan | Physical Training Supervisor | Department of Director of Education | — | — |
| 1940 | B. J. Morahan | Physical Training Supervisor | Department of Director of Education | — | — |

### Deterministic checks: `morahan_bernard-joseph-burke_b1904` vs `Morahan, B. J. B___Hong Kong___1939`

- [PASS] surname_gate: bio 'MORAHAN' vs stint 'Morahan, B. J. B' (exact)
- [PASS] initials: bio ['B', 'J', 'B'] ~ stint ['B', 'J', 'B']
- [PASS] age_gate: stint starts 1939, birth 1904 (age 35)
- [PASS] colony: 2 placed event(s) resolve to 'Hong Kong'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1939-1940
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Morahan, B. J. B___Hong Kong___1949`

- Staff-list name: **Morahan, B. J. B** | colony: **Hong Kong** | listed 1949–1951 | editions [1949, 1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | B. J. Morahan | Physical Training Supervisors | Education Department | — | — |
| 1950 | B. J. B. Morahan | Organizer, Physical Education | Education | — | — |
| 1951 | B. J. B. Morahan | Organizer, Physical Education | Education | — | — |
| 1951 | B. J. B. Morahan | Commanding Officer | Hong Kong Naval Force | — | Comdr. |

### Deterministic checks: `morahan_bernard-joseph-burke_b1904` vs `Morahan, B. J. B___Hong Kong___1949`

- [PASS] surname_gate: bio 'MORAHAN' vs stint 'Morahan, B. J. B' (exact)
- [PASS] initials: bio ['B', 'J', 'B'] ~ stint ['B', 'J', 'B']
- [PASS] age_gate: stint starts 1949, birth 1904 (age 45)
- [PASS] colony: 2 placed event(s) resolve to 'Hong Kong'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1949-1951
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

