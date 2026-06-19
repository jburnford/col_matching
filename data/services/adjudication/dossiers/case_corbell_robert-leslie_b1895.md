<!-- {"case_id": "case_corbell_robert-leslie_b1895", "bio_ids": ["corbell_robert-leslie_b1895"], "stint_ids": ["Cornell, R. L___Tanganyika___1930"]} -->
# Dossier case_corbell_robert-leslie_b1895

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `corbell_robert-leslie_b1895`

- Printed name: **CORBELL, ROBERT LESLIE**
- Birth year: 1895 (attested in editions [1939])
- Honours: M.R.C.V.S
- Appears in editions: [1939]

### Verbatim printed entry text (OCR)

**Version `col1939-L65860.v` — printed in editions [1939]:**

> CORBELL, ROBERT LESLIE, B.Sc., M.R.C.V.S.—B. 1895; ed. Ipswich Schl. and Royal Vety. Coll., London; demonstr. of path. and bact., Royal Vety. Coll., 1923; res. asst., Inst. of Animal Path., Camb., 1924; R.A.V.O., 1915; srgt. dresser, transport corps for serv. in Palestine, 1919; vety. res. offr., Tanganyika Territory, Feb., 1928; seconded to Siam, 1937.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1915 | R.A.V.O | — | [1939] |
| 1 | 1919 | srgt. dresser, transport corps for serv. in Palestine | — | [1939] |
| 2 | 1923 | demonstr. of path. and bact., Royal Vety. Coll | — | [1939] |
| 3 | 1924 | res. asst., Inst. of Animal Path., Camb | — | [1939] |
| 4 | 1928 | vety. res. offr., Tanganyika Territory | Tanganyika | [1939] |
| 5 | 1937 | seconded to Siam | Tanganyika *(inherited from previous clause)* | [1939] |

## Candidate stint `Cornell, R. L___Tanganyika___1930`

- Staff-list name: **Cornell, R. L** | colony: **Tanganyika** | listed 1930–1940 | editions [1930, 1933, 1934, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1930 | R. L. Cornell | Research Officer | Veterinary | — | — |
| 1933 | R. L. Cornell | Research Officer | Veterinary | — | — |
| 1934 | R. L. Cornell | Research Officer | Veterinary | — | — |
| 1940 | R. L. Cornell | Veterinary Research Officer | Veterinary | — | — |

### Deterministic checks: `corbell_robert-leslie_b1895` vs `Cornell, R. L___Tanganyika___1930`

- [PASS] surname_gate: bio 'CORBELL' vs stint 'Cornell, R. L' (fuzzy:1)
- [PASS] initials: bio ['R', 'L'] ~ stint ['R', 'L']
- [PASS] age_gate: stint starts 1930, birth 1895 (age 35)
- [PASS] colony: 2 placed event(s) resolve to 'Tanganyika'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1930-1940
- [FAIL] position_sim: best 52 vs bar 60: 'vety. res. offr., Tanganyika Territory' ~ 'Veterinary Research Officer'
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

