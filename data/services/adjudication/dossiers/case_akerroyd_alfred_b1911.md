<!-- {"case_id": "case_akerroyd_alfred_b1911", "bio_ids": ["akerroyd_alfred_b1911"], "stint_ids": ["Akeroyd, A___Northern Rhodesia___1949"]} -->
# Dossier case_akerroyd_alfred_b1911

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['akerroyd_alfred_b1911'] carry a single initial only — the namesake trap applies.

## Biography `akerroyd_alfred_b1911`

- Printed name: **AKERROYD, Alfred**
- Birth year: 1911 (attested in editions [1963])
- Honours: A.R.I.B.A
- Appears in editions: [1951, 1958, 1959, 1961, 1962, 1963, 1964, 1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1963-L16754.v` — printed in editions [1963]:**

> AKERROYD, A.—b. 1911; ed. St. Luke's Sch. and Cockburn High Sch., Leeds; asst. civ. engr., Admirty, 1943; civ. engr. 1945; archt. N. Rhod., 1947; senr. archt., 1955; dep. dir. wks. 1961.

**Version `col1962-L18181.v` — printed in editions [1962, 1964, 1965, 1966]:**

> AKEROYD, A.—b. 1911; ed. St. Luke's Sch. and Cockburn High Sch., Leeds; asst. civ. engr., Admirty., 1943; civ. engr., 1945; archt. N. Rhod., 1947; senr. archt., 1955; dep. dir. wks., 1961-64 (Zambia Govt. service.)

**Version `col1951-L35580.v` — printed in editions [1951]:**

> AKERROYD, Alfred, A.R.I.B.A., A.M.I. Struct.E.—b. 1911; ed. Cockburn High Sch., Leeds; civ. engnr., Admy., 1933; arch., P.W.D., N. Rhod., 1947.

**Version `col1958-L19928.v` — printed in editions [1958, 1959]:**

> AKERROYD, A.—b. 1911; ed. St. Luke's Sch. and Cockburn High Sch., Leeds; architect, N. Rhodesia, 1947; senr. architect, 1955.

**Version `col1961-L19069.v` — printed in editions [1961]:**

> AKEROYD, A.—b. 1911; ed. St. Luke's Sch. and Cockburn High Sch., Leeds; architect, N. Rhodesia, 1947; senr. architect, 1955.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1933 | civ. engnr., Admy | — | [1951] |
| 1 | 1943 | asst. civ. engr., Admirty | — | [1962, 1963, 1964, 1965, 1966] |
| 2 | 1945 | civ. engr | — | [1962, 1963, 1964, 1965, 1966] |
| 3 | 1947 | archt. N. Rhod | — | [1958, 1959, 1961, 1962, 1963, 1964, 1965, 1966] |
| 4 | 1947 | arch., P.W.D. | Northern Rhodesia | [1951] |
| 5 | 1955 | senr. archt | — | [1958, 1959, 1961, 1962, 1963, 1964, 1965, 1966] |
| 6 | 1961 | dep. dir. wks | — | [1962, 1963, 1964, 1965, 1966] |

## Candidate stint `Akeroyd, A___Northern Rhodesia___1949`

- Staff-list name: **Akeroyd, A** | colony: **Northern Rhodesia** | listed 1949–1951 | editions [1949, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | A. Akeroyd | Assistant Architects | PUBLIC WORKS | — | — |
| 1951 | A. Akeroyd | Architects | Public Works | — | — |

### Deterministic checks: `akerroyd_alfred_b1911` vs `Akeroyd, A___Northern Rhodesia___1949`

- [PASS] surname_gate: bio 'AKERROYD' vs stint 'Akeroyd, A' (fuzzy:1)
- [PASS] initials: bio ['A'] ~ stint ['A']
- [PASS] age_gate: stint starts 1949, birth 1911 (age 38)
- [PASS] colony: 1 placed event(s) resolve to 'Northern Rhodesia'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1949-1951
- [FAIL] position_sim: best 44 vs bar 60: 'arch., P.W.D.' ~ 'Architects'
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

