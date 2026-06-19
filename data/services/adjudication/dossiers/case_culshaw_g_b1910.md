<!-- {"case_id": "case_culshaw_g_b1910", "bio_ids": ["culshaw_g_b1910", "culshaw_lionel-george_b1904"], "stint_ids": ["Culshaw, L. G___Gambia___1949"]} -->
# Dossier case_culshaw_g_b1910

## Case context

- 2 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['culshaw_g_b1910'] carry a single initial only — the namesake trap applies.
- CONTESTED: stint(s) ['Culshaw, L. G___Gambia___1949'] have more than one claimant biography in this case.

## Biography `culshaw_g_b1910`

- Printed name: **CULSHAW, G**
- Birth year: 1910 (attested in editions [1963, 1964])
- Appears in editions: [1963, 1964]

### Verbatim printed entry text (OCR)

**Version `col1963-L18751.v` — printed in editions [1963, 1964]:**

> CULSHAW, G.—b. 1910; ed. Seaforth C. Sch., Christ Church Sch. and L'pool. Tech. Coll.; marine engrnr., Tang., 1948; mech. asst., Malaya, 1951; survr. (ships), Sarawak, 1952.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1948 | marine engrnr. | Tanganyika | [1963, 1964] |
| 1 | 1951 | mech. asst. | Malaya | [1963, 1964] |
| 2 | 1952 | survr. (ships) | Sarawak | [1963, 1964] |

## Biography `culshaw_lionel-george_b1904`

- Printed name: **CULSHAW, Lionel George**
- Birth year: 1904 (attested in editions [1948, 1949, 1950])
- Honours: A.C.G.I, A.I.N.A, A.M.I.C.E
- Appears in editions: [1948, 1949, 1950]

### Verbatim printed entry text (OCR)

**Version `col1948-L32062.v` — printed in editions [1948, 1949, 1950]:**

> CULSHAW, Lionel George, A.C.G.I., A.M.I.C.E., A.M.I.Mech.E., A.I.N.A.—b. 1904; ed. Felsted Sch. and Imperial Coll. of Science; asst. engrnr., Nig., 1928; exec. engrnr., gr. II, 1938; gr. I, 1945; dir. of public utilities, Gam., 1946.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1928 | asst. engrnr. | Nigeria | [1948, 1949, 1950] |
| 1 | 1938 | exec. engrnr., gr. II | Nigeria *(inherited from previous clause)* | [1948, 1949, 1950] |
| 2 | 1945 | gr. I | Nigeria *(inherited from previous clause)* | [1948, 1949, 1950] |
| 3 | 1946 | dir. of public utilities, Gam | Nigeria *(inherited from previous clause)* | [1948, 1949, 1950] |

## Candidate stint `Culshaw, L. G___Gambia___1949`

- Staff-list name: **Culshaw, L. G** | colony: **Gambia** | listed 1949–1950 | editions [1949, 1950]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | L. G. Culshaw | Director | Public Utilities | — | — |
| 1950 | L. G. Culshaw | Director | Public Utilities | — | — |

### Deterministic checks: `culshaw_g_b1910` vs `Culshaw, L. G___Gambia___1949`

- [PASS] surname_gate: bio 'CULSHAW' vs stint 'Culshaw, L. G' (exact)
- [PASS] initials: bio ['G'] ~ stint ['L', 'G']
- [PASS] age_gate: stint starts 1949, birth 1910 (age 39)
- [FAIL] colony: no placed event resolves to 'Gambia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1949-1950
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

### Deterministic checks: `culshaw_lionel-george_b1904` vs `Culshaw, L. G___Gambia___1949`

- [PASS] surname_gate: bio 'CULSHAW' vs stint 'Culshaw, L. G' (exact)
- [PASS] initials: bio ['L', 'G'] ~ stint ['L', 'G']
- [PASS] age_gate: stint starts 1949, birth 1904 (age 45)
- [FAIL] colony: no placed event resolves to 'Gambia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1949-1950
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

