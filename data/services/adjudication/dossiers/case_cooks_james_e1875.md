<!-- {"case_id": "case_cooks_james_e1875", "bio_ids": ["cooks_james_e1875"], "stint_ids": ["Cooks, James___Fiji___1883"]} -->
# Dossier case_cooks_james_e1875

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 4 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['cooks_james_e1875'] carry a single initial only — the namesake trap applies.

## Biography `cooks_james_e1875`

- Printed name: **COOKS, JAMES**
- Birth year: not printed
- Appears in editions: [1898]

### Verbatim printed entry text (OCR)

**Version `col1898-L32718.v` — printed in editions [1898]:**

> COOKS, JAMES.—Third clk., col. sec.'s office, Fiji, 1875; ch. clk. and interp. in native dept., 1876; also clk. and interp. to armed native constab., 1877.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1875 | Third clk., col. sec.'s office | Fiji | [1898] |
| 1 | 1876 | ch. clk. and interp. in native dept | Fiji *(inherited from previous clause)* | [1898] |
| 2 | 1877 | also clk. and interp. to armed native constab | Fiji *(inherited from previous clause)* | [1898] |

## Candidate stint `Cooks, James___Fiji___1883`

- Staff-list name: **Cooks, James** | colony: **Fiji** | listed 1883–1888 | editions [1883, 1888]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1883 | J. Cooks | Clerk and Interpreter | Armed Native Constabulary | — | — |
| 1888 | James Cooks | Assistant Native Commissioner and Clerk Native Regulation Board | Provincial Department | — | — |

### Deterministic checks: `cooks_james_e1875` vs `Cooks, James___Fiji___1883`

- [PASS] surname_gate: bio 'COOKS' vs stint 'Cooks, James' (exact)
- [PASS] initials: bio ['J'] ~ stint ['J']
- [PASS] age_gate: stint starts 1883; no printed birth year — UNCHECKED
- [PASS] colony: 3 placed event(s) resolve to 'Fiji'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1883-1888
- [PASS] position_sim: best 65 vs bar 60: 'also clk. and interp. to armed native constab' ~ 'Assistant Native Commissioner and Clerk Native Regulation Board'
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

