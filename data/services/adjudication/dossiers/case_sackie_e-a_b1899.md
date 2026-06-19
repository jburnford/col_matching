<!-- {"case_id": "case_sackie_e-a_b1899", "bio_ids": ["sackie_e-a_b1899"], "stint_ids": ["Mackie, A___Palestine___1923"]} -->
# Dossier case_sackie_e-a_b1899

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 19 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Mackie, A___Palestine___1923` is also gate-compatible with biography(ies) outside this case: ['mackie_a-s_b1891'] (already linked elsewhere or filtered).

## Biography `sackie_e-a_b1899`

- Printed name: **SACKIE, E. A**
- Birth year: 1899 (attested in editions [1956])
- Honours: O.B.E (1954)
- Appears in editions: [1956]

### Verbatim printed entry text (OCR)

**Version `col1956-L23938.v` — printed in editions [1956]:**

> SACKIE, E. A., O.B.E. (1954)—b. 1899; ed. Mfantsipim Sch., Cape Coast, and Faraday Hse., Lond.; elec. improver, G.C., 1928; African asst. elec. engrnr., 1931; elec. engrnr., 1947; senr., 1949; dep. ch., 1952; ch. elec. engrnr., G.C. local service, 1955.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1928 | elec. improver | Gold Coast | [1956] |
| 1 | 1931 | African asst. elec. engrnr | Gold Coast *(inherited from previous clause)* | [1956] |
| 2 | 1947 | elec. engrnr | Gold Coast *(inherited from previous clause)* | [1956] |
| 3 | 1949 | senr | Gold Coast *(inherited from previous clause)* | [1956] |
| 4 | 1952 | dep. ch | Gold Coast *(inherited from previous clause)* | [1956] |
| 5 | 1955 | ch. elec. engrnr., G.C. local service | Gold Coast | [1956] |

## Candidate stint `Mackie, A___Palestine___1923`

- Staff-list name: **Mackie, A** | colony: **Palestine** | listed 1923–1925 | editions [1923, 1925]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1923 | A. Mackie | Inspector Ghaffar Force | Palestine Railways | — | — |
| 1925 | A. Mackie | Inspector Ghaffir Force | Palestine Railways | — | — |

### Deterministic checks: `sackie_e-a_b1899` vs `Mackie, A___Palestine___1923`

- [PASS] surname_gate: bio 'SACKIE' vs stint 'Mackie, A' (fuzzy:1)
- [PASS] initials: bio ['E', 'A'] ~ stint ['A']
- [PASS] age_gate: stint starts 1923, birth 1899 (age 24)
- [FAIL] colony: no placed event resolves to 'Palestine'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1923-1925
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

