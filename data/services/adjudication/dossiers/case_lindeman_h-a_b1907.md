<!-- {"case_id": "case_lindeman_h-a_b1907", "bio_ids": ["lindeman_h-a_b1907", "lindeman_henry-alexander_b1907"], "stint_ids": ["Lindeman, H. A___Tanganyika___1940"]} -->
# Dossier case_lindeman_h-a_b1907

## Case context

- 2 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- CONTESTED: stint(s) ['Lindeman, H. A___Tanganyika___1940'] have more than one claimant biography in this case.

## Biography `lindeman_h-a_b1907`

- Printed name: **LINDEMAN, H. A**
- Birth year: 1907 (attested in editions [1956, 1957, 1958, 1959, 1960])
- Appears in editions: [1956, 1957, 1958, 1959, 1960]

### Verbatim printed entry text (OCR)

**Version `col1956-L22552.v` — printed in editions [1956, 1957, 1958, 1959, 1960]:**

> LINDEMAN, H. A.—b. 1907; ed. Dauntsey's Sch. and Reading Univ.; supt., educ., Tang., 1930; educ. offr., 1940; prin., 1952.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1930 | supt., educ. | Tanganyika | [1956, 1957, 1958, 1959, 1960] |
| 1 | 1952 | prin | Tanganyika *(inherited from previous clause)* | [1956, 1957, 1958, 1959, 1960] |

## Biography `lindeman_henry-alexander_b1907`

- Printed name: **LINDEMAN, Henry Alexander**
- Birth year: 1907 (attested in editions [1948, 1949, 1950, 1951])
- Appears in editions: [1948, 1949, 1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1948-L34067.v` — printed in editions [1948, 1949, 1950, 1951]:**

> LINDEMAN, Henry Alexander.—b.1907 ; ed. Dauntseys Sch., Reading Univ., F.L.S., dip. hort. (Reading) ; educ. offr., T.T., 1930 ; mem., science syll. comte., Uga., 1936 and 1939 ; science mstrs confce., Uga., 1944.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1930 | educ. offr. | Tanganyika Territory | [1948, 1949, 1950, 1951] |
| 1 | 1936–1939 | mem., science syll. comte. | Uganda | [1948, 1949, 1950, 1951] |
| 2 | 1944 | science mstrs confce. | Uganda | [1948, 1949, 1950, 1951] |

## Candidate stint `Lindeman, H. A___Tanganyika___1940`

- Staff-list name: **Lindeman, H. A** | colony: **Tanganyika** | listed 1940–1949 | editions [1940, 1949]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1940 | H. A. Lindeman | Superintendent of Education | Education | — | — |
| 1949 | H. A. Lindeman | Education Officer | Education | — | — |

### Deterministic checks: `lindeman_h-a_b1907` vs `Lindeman, H. A___Tanganyika___1940`

- [PASS] surname_gate: bio 'LINDEMAN' vs stint 'Lindeman, H. A' (exact)
- [PASS] initials: bio ['H', 'A'] ~ stint ['H', 'A']
- [PASS] age_gate: stint starts 1940, birth 1907 (age 33)
- [PASS] colony: 2 placed event(s) resolve to 'Tanganyika'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1940-1949
- [FAIL] position_sim: best 50 vs bar 60: 'supt., educ.' ~ 'Superintendent of Education'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

### Deterministic checks: `lindeman_henry-alexander_b1907` vs `Lindeman, H. A___Tanganyika___1940`

- [PASS] surname_gate: bio 'LINDEMAN' vs stint 'Lindeman, H. A' (exact)
- [PASS] initials: bio ['H', 'A'] ~ stint ['H', 'A']
- [PASS] age_gate: stint starts 1940, birth 1907 (age 33)
- [FAIL] colony: no placed event resolves to 'Tanganyika'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1940-1949
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

