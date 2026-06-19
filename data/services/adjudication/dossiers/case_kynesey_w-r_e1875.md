<!-- {"case_id": "case_kynesey_w-r_e1875", "bio_ids": ["kynesey_w-r_e1875"], "stint_ids": ["Kynsey, William R___Ceylon___1878"]} -->
# Dossier case_kynesey_w-r_e1875

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- Phase 1 found `kynesey_w-r_e1875` ↔ `Kynsey, William R___Ceylon___1878` passed its evidence bar but dropped it as ambiguous (a comparable-strength competitor existed).
- NOTE: stint `Kynsey, William R___Ceylon___1878` is also gate-compatible with biography(ies) outside this case: ['kynsey_w-r-f-k-q-c-p-c-m-g-1888_b1840'] (already linked elsewhere or filtered).

## Biography `kynesey_w-r_e1875`

- Printed name: **KYNESEY, W.R**
- Birth year: not printed
- Honours: C.M.G (1888), F.K.Q.C.P
- Appears in editions: [1894]

### Verbatim printed entry text (OCR)

**Version `col1894-L32497.v` — printed in editions [1894]:**

> KYNESEY, W.R., F.K.Q.C.P., C.M.G. (1888).—Principal civil medical officer, and inspector-general of hospitals, Ceylon, Feb., 1875.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1875 | Principal civil medical officer, and inspector-general of hospitals | Ceylon | [1894] |

## Candidate stint `Kynsey, William R___Ceylon___1878`

- Staff-list name: **Kynsey, William R** | colony: **Ceylon** | listed 1878–1896 | editions [1878, 1879, 1883, 1886, 1888, 1889, 1890, 1894, 1896]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1878 | W. R. Kynsey | Principal Civil Medical Officer and Inspector-General of Hospitals | Medical Department | — | — |
| 1879 | W. R. Kynsey | Principal Civil Medical Officer and Inspector-General of Hospitals | Medical Department | — | — |
| 1883 | W. R. Kynsey | Principal Civil Medical Officer and Inspector-General of Hospitals | Medical Department | — | — |
| 1886 | W. R. Kynsey | Principal Civil Medical Officer and Inspector-General of Hospitals | Medical Department | — | — |
| 1888 | W. R. Kynsey | Principal Civil Medical Officer and Inspector-General of Hospitals | Medical Department | — | — |
| 1889 | W. R. Kynsey | Principal Civil Medical Officer and Inspector-General of Hospitals | Medical Department | — | — |
| 1890 | W. R. Kynsey | Principal Civil Medical Officer and Inspector-General of Hospitals | Medical Department | — | — |
| 1894 | William R. Kynsey | Principal Civil Medical Officer and Inspector-General of Hospitals | Medical Department | C.M.G. | — |
| 1896 | William R. Kynsey | Principal Civil Medical Officer and Inspector-General of Hospitals | Medical Department | C.M.G. | — |

### Deterministic checks: `kynesey_w-r_e1875` vs `Kynsey, William R___Ceylon___1878`

- [PASS] surname_gate: bio 'KYNESEY' vs stint 'Kynsey, William R' (fuzzy:1)
- [PASS] initials: bio ['W', 'R'] ~ stint ['W', 'R']
- [PASS] age_gate: stint starts 1878; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Ceylon'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1878-1896
- [PASS] position_sim: best 100 vs bar 60: 'Principal civil medical officer, and inspector-general of hospitals' ~ 'Principal Civil Medical Officer and Inspector-General of Hospitals'
- [PASS] honour: shared: C.M.G
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

