<!-- {"case_id": "case_hitchin_edw-wm_e1850", "bio_ids": ["hitchin_edw-wm_e1850"], "stint_ids": ["Hitchin, E. W___South Australia___1877"]} -->
# Dossier case_hitchin_edw-wm_e1850

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 5 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `hitchin_edw-wm_e1850`

- Printed name: **HITCHIN, Edw. Wm**
- Birth year: not printed
- Appears in editions: [1883]

### Verbatim printed entry text (OCR)

**Version `col1883-L28002.v` — printed in editions [1883]:**

> HITCHIN, Edw. Wm.—Clerk in the registrar-general's department, South Australia, 1850; clerk in colonial secretary's department, 1851; second assistant colonial secretary, 1856; secretary to commissioner of crown lands and immigration, 1857; secretary to commissioner of public works, 1859; under treasurer, 1860; auditor general, 1868.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1850 | Clerk in the registrar-general's department | South Australia | [1883] |
| 1 | 1851 | clerk in colonial secretary's department | South Australia *(inherited from previous clause)* | [1883] |
| 2 | 1856 | second assistant colonial secretary | South Australia *(inherited from previous clause)* | [1883] |
| 3 | 1857 | secretary to commissioner of crown lands and immigration | South Australia *(inherited from previous clause)* | [1883] |
| 4 | 1859 | secretary to commissioner of public works | South Australia *(inherited from previous clause)* | [1883] |
| 5 | 1860 | under treasurer | South Australia *(inherited from previous clause)* | [1883] |
| 6 | 1868 | auditor general | South Australia *(inherited from previous clause)* | [1883] |

## Candidate stint `Hitchin, E. W___South Australia___1877`

- Staff-list name: **Hitchin, E. W** | colony: **South Australia** | listed 1877–1880 | editions [1877, 1878, 1879, 1880]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | E. W. Hitchin | Auditor-General | Audit Department | — | — |
| 1878 | E. W. Hitchin | Auditor-General | Audit Department | — | — |
| 1879 | E. W. Hitchin | Auditor-General | Audit Department | — | — |
| 1880 | E. W. Hitchin | Auditor-General | Audit Department | — | — |

### Deterministic checks: `hitchin_edw-wm_e1850` vs `Hitchin, E. W___South Australia___1877`

- [PASS] surname_gate: bio 'HITCHIN' vs stint 'Hitchin, E. W' (exact)
- [PASS] initials: bio ['E', 'W'] ~ stint ['E', 'W']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [PASS] colony: 7 placed event(s) resolve to 'South Australia'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1877-1880
- [PASS] position_sim: best 97 vs bar 60: 'auditor general' ~ 'Auditor-General'
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

