<!-- {"case_id": "case_mackilligan_robert-springett_b1890", "bio_ids": ["mackilligan_robert-springett_b1890"], "stint_ids": ["Mackilliggin, R. S___Trinidad and Tobago___1937"]} -->
# Dossier case_mackilligan_robert-springett_b1890

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `mackilligan_robert-springett_b1890`

- Printed name: **MACKILLIGAN, ROBERT SPRINGETT**
- Birth year: 1890 (attested in editions [1939])
- Honours: M.C, M.I.M.M, M.I.P.T, O.B.E
- Appears in editions: [1939, 1940]

### Verbatim printed entry text (OCR)

**Version `col1939-L68810.v` — printed in editions [1939]:**

> MACKILLIGAN, ROBERT SPRINGETT, O.B.E., M.C., M.I.M.M., M.I.P.T.—B. 1890; ed. Cranbrook Schol. Kent and Schol. of Mines, Camborne, Cornwall; inspr., mines and petroleum technologist, Trinidad, Mar., 1936.

**Version `col1939-L68944.v` — printed in editions [1939, 1940]:**

> MACKILLIGIN, ROBERT SPRINGETT, O.B.E., M.C., M.I.M.M., F.Inst.Pet.—B. 1890; ed. Cranbrook Sch., Kent and Schol. of Mines, Camborne, Cornwall; inspr., mines and petroleum technologies, Trinidad, Mar., 1936.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1936 | inspr., mines and petroleum technologist | Trinidad | [1939, 1940] |

## Candidate stint `Mackilliggin, R. S___Trinidad and Tobago___1937`

- Staff-list name: **Mackilliggin, R. S** | colony: **Trinidad and Tobago** | listed 1937–1940 | editions [1937, 1939, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1937 | R. S. Mackilliggin | Inspector of Mines and Petroleum Technologist | MINES DEPARTMENT | — | — |
| 1939 | R. S. Mackilliggin | Inspector of Mines and Petroleum Technologist | Mines Department | — | — |
| 1940 | R. S. Mackilliggin | Inspector of Mines and Petroleum Technology | Miners | — | — |

### Deterministic checks: `mackilligan_robert-springett_b1890` vs `Mackilliggin, R. S___Trinidad and Tobago___1937`

- [PASS] surname_gate: bio 'MACKILLIGAN' vs stint 'Mackilliggin, R. S' (fuzzy:2)
- [PASS] initials: bio ['R', 'S'] ~ stint ['R', 'S']
- [PASS] age_gate: stint starts 1937, birth 1890 (age 47)
- [FAIL] colony: no placed event resolves to 'Trinidad and Tobago'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1937-1940
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

