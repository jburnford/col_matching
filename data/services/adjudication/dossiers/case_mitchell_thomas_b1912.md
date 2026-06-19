<!-- {"case_id": "case_mitchell_thomas_b1912", "bio_ids": ["mitchell_thomas_b1912"], "stint_ids": ["Mitchell, T. A___Bermuda___1927"]} -->
# Dossier case_mitchell_thomas_b1912

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 118 official(s) with this surname in the graph's staff lists; 46 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['mitchell_thomas_b1912'] carry a single initial only — the namesake trap applies.

## Biography `mitchell_thomas_b1912`

- Printed name: **MITCHELL, Thomas**
- Birth year: 1912 (attested in editions [1960, 1961, 1962])
- Honours: A.M.I.C.E, A.M.I.W.E
- Appears in editions: [1951, 1960, 1961, 1962]

### Verbatim printed entry text (OCR)

**Version `col1960-L26125.v` — printed in editions [1960, 1961, 1962]:**

> MITCHELL, T., T.D.—b. 1912; ed. Royal High Sch., Edin., and Edin. Univ.; mil. serv., 1939-46, lt. col.; exec. engrnr., Trin., 1947-48; Tang., 1949; senr. exec. engrnr., 1957.

**Version `col1951-L40912.v` — printed in editions [1951]:**

> MITCHELL, Thomas, B.Sc. (civ. eng.) (Edin.), A.M.I.C.E., A.M.I.W.E.—b. 1912; ed. Royal High Sch., Edin. and Edin. Univ.; on mil. serv., 1939-46, lt.-col.; ag. water engr., Trin., 1947; exec. engr., water dev., Tang., 1949.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1947–1948 | exec. engrnr. | Trinidad | [1951, 1960, 1961, 1962] |
| 1 | 1949 | exec. engrnr. | Tanganyika | [1951, 1960, 1961, 1962] |
| 2 | 1957 | senr. exec. engrnr | Tanganyika *(inherited from previous clause)* | [1960, 1961, 1962] |

## Candidate stint `Mitchell, T. A___Bermuda___1927`

- Staff-list name: **Mitchell, T. A** | colony: **Bermuda** | listed 1927–1932 | editions [1927, 1928, 1929, 1930, 1931, 1932]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1927 | Miss T. A. Mitchell | 2nd Stenographer | Colonial Secretary's Department | — | — |
| 1928 | T. A. Mitchell | 2nd Stenographer | Colonial Secretary's Department | — | — |
| 1929 | Miss T. A. Mitchell | 2nd Stenographer | Senior Clerk and Clerk to Legislative Council | — | — |
| 1930 | Miss T. A. Mitchell | Stenographer | Colonial Secretary's Department | — | — |
| 1931 | T. A. Mitchell | Stenographer | Colonial Secretary’s Department | — | — |
| 1932 | T. A. Mitchell | Stenographer | Colonial Secretary's Department | — | — |

### Deterministic checks: `mitchell_thomas_b1912` vs `Mitchell, T. A___Bermuda___1927`

- [PASS] surname_gate: bio 'MITCHELL' vs stint 'Mitchell, T. A' (exact)
- [PASS] initials: bio ['T'] ~ stint ['T', 'A']
- [PASS] age_gate: stint starts 1927, birth 1912 (age 15)
- [FAIL] colony: no placed event resolves to 'Bermuda'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1927-1932
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

