<!-- {"case_id": "case_craw_james_e1863", "bio_ids": ["craw_james_e1863"], "stint_ids": ["Craw, J___Natal___1879"]} -->
# Dossier case_craw_james_e1863

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['craw_james_e1863'] carry a single initial only — the namesake trap applies.

## Biography `craw_james_e1863`

- Printed name: **CRAW, JAMES**
- Birth year: not printed
- Appears in editions: [1883, 1886]

### Verbatim printed entry text (OCR)

**Version `col1883-L27002.v` — printed in editions [1883, 1886]:**

> CRAW, JAMES.—Secretary to the immigration board, and acting third clerk in the colonial office, Natal, 1863; and first clerk in the registry of deeds and stamp office of that colony, 1866.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1863 | Secretary to the immigration board, and acting third clerk in the colonial office | Natal | [1883, 1886] |
| 1 | 1866 | and first clerk in the registry of deeds and stamp office of that colony | Natal *(inherited from previous clause)* | [1883, 1886] |

## Candidate stint `Craw, J___Natal___1879`

- Staff-list name: **Craw, J** | colony: **Natal** | listed 1879–1883 | editions [1879, 1880, 1883]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1879 | J. Craw | 1st Clerk | Registrar of Deeds Department | — | — |
| 1880 | J. Craw | 1st Clerk | Registrar of Deeds | — | — |
| 1883 | J. Craw | 1st Clerk | Registrar of Deeds | — | — |

### Deterministic checks: `craw_james_e1863` vs `Craw, J___Natal___1879`

- [PASS] surname_gate: bio 'CRAW' vs stint 'Craw, J' (exact)
- [PASS] initials: bio ['J'] ~ stint ['J']
- [PASS] age_gate: stint starts 1879; no printed birth year — UNCHECKED
- [PASS] colony: 2 placed event(s) resolve to 'Natal'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1879-1883
- [PASS] position_sim: best 71 vs bar 60: 'and first clerk in the registry of deeds and stamp office of that colony' ~ '1st Clerk'
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

