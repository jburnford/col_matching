<!-- {"case_id": "case_macgregor_ian-gregor_b1897", "bio_ids": ["macgregor_ian-gregor_b1897"], "stint_ids": ["MacGregor, I___Uganda___1939"]} -->
# Dossier case_macgregor_ian-gregor_b1897

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 33 official(s) with this surname in the graph's staff lists; 30 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `macgregor_ian-gregor_b1897`

- Printed name: **MacGREGOR, Ian Gregor**
- Birth year: 1897 (attested in editions [1949, 1950, 1951])
- Honours: M.B
- Appears in editions: [1949, 1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1949-L33950.v` — printed in editions [1949, 1950, 1951]:**

> MacGREGOR, Ian Gregor, M.B., Ch.B. (Edin.), 1924, F.R.C.S. (Edin.), 1938, D.T.M. & H. (Eng.)—b. 1897; ed. High Sch., Ladysmith, George Heriots Sch., and Edin. Univ.; on mil. serv., 1914-19; apptd. med. serv., Nig., 1926; speclst., 1938; senr. speclst., 1943.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1926 | apptd. med. serv. | Nigeria | [1949, 1950, 1951] |
| 1 | 1938 | speclst | Nigeria *(inherited from previous clause)* | [1949, 1950, 1951] |
| 2 | 1943 | senr. speclst | Nigeria *(inherited from previous clause)* | [1949, 1950, 1951] |

## Candidate stint `MacGregor, I___Uganda___1939`

- Staff-list name: **MacGregor, I** | colony: **Uganda** | listed 1939–1940 | editions [1939, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1939 | I. MacGregor | Superintendents, Assistant Superintendents and Cadets | Police | — | — |
| 1940 | I. MacGregor | Superintendent, Assistant Superintendent and Cadet | Police | — | — |

### Deterministic checks: `macgregor_ian-gregor_b1897` vs `MacGregor, I___Uganda___1939`

- [PASS] surname_gate: bio 'MacGREGOR' vs stint 'MacGregor, I' (exact)
- [PASS] initials: bio ['I', 'G'] ~ stint ['I']
- [PASS] age_gate: stint starts 1939, birth 1897 (age 42)
- [FAIL] colony: no placed event resolves to 'Uganda'
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

