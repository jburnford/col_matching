<!-- {"case_id": "case_tennant_robert-allan_b1901", "bio_ids": ["tennant_robert-allan_b1901"], "stint_ids": ["Tennant, R. A___Northern Rhodesia___1949"]} -->
# Dossier case_tennant_robert-allan_b1901

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 11 official(s) with this surname in the graph's staff lists; 6 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `tennant_robert-allan_b1901`

- Printed name: **TENNANT, Robert Allan**
- Birth year: 1901 (attested in editions [1948, 1949, 1950, 1951])
- Honours: A.M.I.C.E
- Appears in editions: [1948, 1949, 1950, 1951, 1953, 1954, 1955, 1956]

### Verbatim printed entry text (OCR)

**Version `col1948-L36335.v` — printed in editions [1948, 1949, 1950, 1951]:**

> TENNANT, Robert Allan, B.E. (N.U.I.), A.M.I.C.E., A.M.I.C.E. (Ire.).—b. 1901; ed. Galway Gram. Sch., Ireland and Nat. Univ. of Ireland; apptd. to Nig., 1928; exec. engrn., N. Rhod., 1946; D.D.P.W., 1948.

**Version `col1953-L19260.v` — printed in editions [1953, 1954, 1955, 1956]:**

> TENNANT, R. A.—b. 1901; ed. Galway Gram. Sch., Ireland, and Nat. Univ. of Ireland; apptd. Nig., 1928; exec. engnr., N. Rhod., 1946; dep. dir., wks., 1948.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1928 | apptd. to Nig | — | [1948, 1949, 1950, 1951, 1953, 1954, 1955, 1956] |
| 1 | 1946 | exec. engrn. | Northern Rhodesia | [1948, 1949, 1950, 1951, 1953, 1954, 1955, 1956] |
| 2 | 1948 | D.D.P.W | Northern Rhodesia *(inherited from previous clause)* | [1948, 1949, 1950, 1951, 1953, 1954, 1955, 1956] |

## Candidate stint `Tennant, R. A___Northern Rhodesia___1949`

- Staff-list name: **Tennant, R. A** | colony: **Northern Rhodesia** | listed 1949–1956 | editions [1949, 1951, 1953, 1954, 1955, 1956]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | R. A. Tennant | Deputy Director | PUBLIC WORKS | — | — |
| 1951 | R. A. Tennant | Deputy Director | Public Works | — | — |
| 1953 | R. A. Tennant | Deputy Director of Public Works | Civil Establishment | — | — |
| 1954 | R. A. Tennant | Deputy Director of Public Works | Civil Establishment | — | — |
| 1955 | R. A. Tennant | Deputy Director of Works | Civil Establishment | — | — |
| 1956 | R. A. Tennant | Deputy Director of Works | Civil Establishment | — | — |

### Deterministic checks: `tennant_robert-allan_b1901` vs `Tennant, R. A___Northern Rhodesia___1949`

- [PASS] surname_gate: bio 'TENNANT' vs stint 'Tennant, R. A' (exact)
- [PASS] initials: bio ['R', 'A'] ~ stint ['R', 'A']
- [PASS] age_gate: stint starts 1949, birth 1901 (age 48)
- [PASS] colony: 2 placed event(s) resolve to 'Northern Rhodesia'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1949-1956
- [FAIL] position_sim: best 32 vs bar 60: 'exec. engrn.' ~ 'Deputy Director'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

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

