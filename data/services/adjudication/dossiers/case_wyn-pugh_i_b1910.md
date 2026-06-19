<!-- {"case_id": "case_wyn-pugh_i_b1910", "bio_ids": ["wyn-pugh_i_b1910"], "stint_ids": ["Wyn-Pugh, I___Nigeria___1958"]} -->
# Dossier case_wyn-pugh_i_b1910

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['wyn-pugh_i_b1910'] carry a single initial only — the namesake trap applies.

## Biography `wyn-pugh_i_b1910`

- Printed name: **WYN-PUGH, I**
- Birth year: 1910 (attested in editions [1957])
- Appears in editions: [1957]

### Verbatim printed entry text (OCR)

**Version `col1957-L28635.v` — printed in editions [1957]:**

> WYN-PUGH, I.—b. 1910; ed. Gram. Sch., Dolgellau; mil. serv., 1939-46; local govt., U.K., 1931-39; exec. engnr., gr. II, Tang., 1946; gr. I, 1947; asst. D.P.W., 1950; D.P.W., G.C., 1952 (Ghana civil service).

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1931–1939 | local govt., U.K | — | [1957] |
| 1 | 1946 | exec. engnr., gr. II | Tanganyika | [1957] |
| 2 | 1947 | gr. I | Tanganyika *(inherited from previous clause)* | [1957] |
| 3 | 1950 | asst. D.P.W | Tanganyika *(inherited from previous clause)* | [1957] |
| 4 | 1952 | D.P.W. | Gold Coast | [1957] |

## Candidate stint `Wyn-Pugh, I___Nigeria___1958`

- Staff-list name: **Wyn-Pugh, I** | colony: **Nigeria** | listed 1958–1960 | editions [1958, 1960]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1958 | I. Wyn-Pugh | Director of Federal Public Works | Civil Establishment | C.B.E. | — |
| 1958 | I. Wyn-Pugh | Director of Federal Public Works | — | — | — |
| 1960 | I. Wyn-Pugh | Director of Federal Public Works | Civil Establishment | — | — |

### Deterministic checks: `wyn-pugh_i_b1910` vs `Wyn-Pugh, I___Nigeria___1958`

- [PASS] surname_gate: bio 'WYN-PUGH' vs stint 'Wyn-Pugh, I' (exact)
- [PASS] initials: bio ['I'] ~ stint ['I']
- [PASS] age_gate: stint starts 1958, birth 1910 (age 48)
- [FAIL] colony: no placed event resolves to 'Nigeria'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1958-1960
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

