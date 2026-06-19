<!-- {"case_id": "case_frayling_bryan-edwin_b1893", "bio_ids": ["frayling_bryan-edwin_b1893"], "stint_ids": ["Frayling, B. E___Tanganyika___1930"]} -->
# Dossier case_frayling_bryan-edwin_b1893

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `frayling_bryan-edwin_b1893`

- Printed name: **FRAYLING, BRYAN EDWIN**
- Birth year: 1893 (attested in editions [1940])
- Honours: O.B.E
- Appears in editions: [1940]

### Verbatim printed entry text (OCR)

**Version `col1940-L64380.v` — printed in editions [1940]:**

> FRAYLING, BRYAN EDWIN, O.B.E.—B. 1893; ed. Denstone Coll. and R. Schl. of Mines; associate, R. Schl. of Mines; dipl., Imp. Coll. (Mining); associate, Instit. Mining and Metallurgy; el. mem., Geolog. Soc. of S. Africa; inspr., mines, Tanganyika, 1926; senr. inspr., mines, 1927; ch. inspr., mines, Nigeria, 1939.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1926 | inspr., mines | Tanganyika | [1940] |
| 1 | 1927 | senr. inspr., mines | Tanganyika *(inherited from previous clause)* | [1940] |
| 2 | 1939 | ch. inspr., mines | Nigeria | [1940] |

## Candidate stint `Frayling, B. E___Tanganyika___1930`

- Staff-list name: **Frayling, B. E** | colony: **Tanganyika** | listed 1930–1933 | editions [1930, 1933]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1930 | B. E. Frayling | Senior Inspector of Mines | Mines | — | — |
| 1933 | B. E. Frayling | Senior Inspector of Mines | Mines | — | — |

### Deterministic checks: `frayling_bryan-edwin_b1893` vs `Frayling, B. E___Tanganyika___1930`

- [PASS] surname_gate: bio 'FRAYLING' vs stint 'Frayling, B. E' (exact)
- [PASS] initials: bio ['B', 'E'] ~ stint ['B', 'E']
- [PASS] age_gate: stint starts 1930, birth 1893 (age 37)
- [PASS] colony: 2 placed event(s) resolve to 'Tanganyika'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1930-1933
- [PASS] position_sim: best 78 vs bar 60: 'senr. inspr., mines' ~ 'Senior Inspector of Mines'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: ALL supporting events inherit their place from an earlier clause — weak evidence

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

