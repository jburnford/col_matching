<!-- {"case_id": "case_bland_ronald-heywood_b1904", "bio_ids": ["bland_ronald-heywood_b1904"], "stint_ids": ["Bland, R. H___Singapore___1955"]} -->
# Dossier case_bland_ronald-heywood_b1904

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 7 official(s) with this surname in the graph's staff lists; 6 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `bland_ronald-heywood_b1904`

- Printed name: **BLAND, Ronald Heywood**
- Birth year: 1904 (attested in editions [1955, 1956, 1957])
- Honours: M.R.C.P, O.B.E (1943)
- Appears in editions: [1948, 1953, 1954, 1955, 1956, 1957]

### Verbatim printed entry text (OCR)

**Version `col1955-L19785.v` — printed in editions [1955, 1956, 1957]:**

> BLAND, R. H., O.B.E. (1943).—b. 1904; ed. Mountjoy Sch., Dublin, Trent Coll. and Trinity Coll., Dublin; mil. serv., 1940-45, lt.-col.; S.M.O., Pal., 1946; asst. D.M.S., 1947; senr. leprosy offr., Nig., 1948; D.D.M.S. (regl.) 1951; D.M.S., E. regn., 1952; S'pore, 1954; perm. sec., min. of health, and D.M.S., 1955; med. mission, Sudan, 1929-40.

**Version `col1953-L16594.v` — printed in editions [1953, 1954]:**

> BLAND, R. H., O.B.E.—b. 1904; ed. Trent Coll. and Trinity Coll., Dublin; mil. serv., 1940-45, lt.-col.; S.M.O., Pal., 1946; asst. D.M.S., 1947; senr. leprosy offr., Nig., 1948; asst. dir., leprosy cont., 1950; D.D.M.S. (regl.), 1951; D.M.S., E. regn., 1952.

**Version `col1948-L31245.v` — printed in editions [1948]:**

> BLAND, Ronald Heywood, O.B.E., M.D. (Dub.), M.R.C.P.—b. 1904; ed. Trent Coll., Derby and Trinity Coll., Dublin; on mil. serv. 1940-45, lieut.-col.; S.M.O., Pal., 1946; prin. med offr., Br. mil. admin., Eritrea, 1941-44.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1929–1940 | med. mission, Sudan | Nigeria *(inherited from previous clause)* | [1955, 1956, 1957] |
| 1 | 1941–1944 | prin. med offr., Br. mil. admin., Eritrea | Palestine *(inherited from previous clause)* | [1948] |
| 2 | 1946 | S.M.O. | Palestine | [1948, 1953, 1954, 1955, 1956, 1957] |
| 3 | 1947 | asst. D.M.S | Palestine *(inherited from previous clause)* | [1953, 1954, 1955, 1956, 1957] |
| 4 | 1948 | senr. leprosy offr. | Nigeria | [1953, 1954, 1955, 1956, 1957] |
| 5 | 1950 | asst. dir., leprosy cont | Nigeria *(inherited from previous clause)* | [1953, 1954] |
| 6 | 1951 | D.D.M.S. (regl.) | Nigeria *(inherited from previous clause)* | [1953, 1954, 1955, 1956, 1957] |
| 7 | 1952 | D.M.S., E. regn | Nigeria *(inherited from previous clause)* | [1953, 1954, 1955, 1956, 1957] |
| 8 | 1954 | S'pore | Nigeria *(inherited from previous clause)* | [1955, 1956, 1957] |
| 9 | 1955 | perm. sec., min. of health, and D.M.S | Nigeria *(inherited from previous clause)* | [1955, 1956, 1957] |

## Candidate stint `Bland, R. H___Singapore___1955`

- Staff-list name: **Bland, R. H** | colony: **Singapore** | listed 1955–1957 | editions [1955, 1956, 1957]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1955 | R. H. Bland | Director of Medical Services | Civil Establishment | — | — |
| 1956 | R. H. Bland | Permanent Secretary to Ministry of Health and Director of Medical Services | Civil Establishment | — | — |
| 1957 | R. H. Bland | Permanent Secretary to Ministry of Health and Director of Medical Services | Civil Establishment | — | — |

### Deterministic checks: `bland_ronald-heywood_b1904` vs `Bland, R. H___Singapore___1955`

- [PASS] surname_gate: bio 'BLAND' vs stint 'Bland, R. H' (exact)
- [PASS] initials: bio ['R', 'H'] ~ stint ['R', 'H']
- [PASS] age_gate: stint starts 1955, birth 1904 (age 51)
- [FAIL] colony: no placed event resolves to 'Singapore'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1955-1957
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

