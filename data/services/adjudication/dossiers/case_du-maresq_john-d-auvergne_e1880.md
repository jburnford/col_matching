<!-- {"case_id": "case_du-maresq_john-d-auvergne_e1880", "bio_ids": ["du-maresq_john-d-auvergne_e1880"], "stint_ids": ["Dumaresq, J. D'A___Natal___1883"]} -->
# Dossier case_du-maresq_john-d-auvergne_e1880

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- Phase 1 found `du-maresq_john-d-auvergne_e1880` ↔ `Dumaresq, J. D'A___Natal___1883` passed its evidence bar but dropped it as ambiguous (a comparable-strength competitor existed).
- NOTE: stint `Dumaresq, J. D'A___Natal___1883` is also gate-compatible with biography(ies) outside this case: ['dumaresq_john-d-averge_e1880'] (already linked elsewhere or filtered).

## Biography `du-maresq_john-d-auvergne_e1880`

- Printed name: **Du MARESQ, John D'Auvergne**
- Birth year: not printed
- Appears in editions: [1886, 1888]

### Verbatim printed entry text (OCR)

**Version `col1886-L33165.v` — printed in editions [1886]:**

> Du MARESQ, John D'Auvergne.—Extra clerk in the governor's office, Natal, February, 1880; third clerk in the registrar of deeds office, April, 1880; transferred to colonial secretary's office as third clerk in February, 1881; second clerk colonial secretary's office, 1st January, 1882.

**Version `col1888-L33190.v` — printed in editions [1888]:**

> DUMARESQ, John D'AUVERGNE.—Extra clerk in the governor's office, Natal, February, 1880; third clerk in the registrar general's office, April, 1880; third clerk, colonial secretary's office, Feb., 1881; second clerk, colonial secretary's office, 1st Jan., 1882; has acted on several occasions as first clerk.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1880 | Extra clerk in the governor's office | Natal | [1886, 1888] |
| 1 | 1881 | transferred to colonial secretary's office as third clerk in | Natal *(inherited from previous clause)* | [1886, 1888] |
| 2 | 1882 | second clerk colonial secretary's office | Natal *(inherited from previous clause)* | [1886, 1888] |

## Candidate stint `Dumaresq, J. D'A___Natal___1883`

- Staff-list name: **Dumaresq, J. D'A** | colony: **Natal** | listed 1883–1899 | editions [1883, 1886, 1888, 1889, 1890, 1894, 1896, 1899]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1883 | J. D'A. Dumaresq | 2nd Clerk | Colonial Secretary's Department | — | — |
| 1886 | J. D'A. Dumaresq | Clerk | Colonial Secretary's Office | — | — |
| 1888 | J. D'A. Dumaresq | Clerk | Colonial Secretary's Office | — | — |
| 1889 | J. D'A. Dumaresq | First Clerk | Colonial Secretary's Office | — | — |
| 1890 | J. D'A. Dumaresq | First Clerk | Colonial Secretary's Office | — | — |
| 1894 | J. Dumaresq | First Clerk | Registrar of Deeds | — | — |
| 1896 | J. Dumaresq | Chief Clerk | Registrar of Deeds | — | — |
| 1899 | J. Dumaresq | Chief Clerk | Registrar of Deeds | — | — |

### Deterministic checks: `du-maresq_john-d-auvergne_e1880` vs `Dumaresq, J. D'A___Natal___1883`

- [PASS] surname_gate: bio 'Du MARESQ' vs stint 'Dumaresq, J. D'A' (fuzzy:1)
- [PASS] initials: bio ['J', 'D'] ~ stint ['J', 'D']
- [PASS] age_gate: stint starts 1883; no printed birth year — UNCHECKED
- [PASS] colony: 3 placed event(s) resolve to 'Natal'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1883-1899
- [PASS] position_sim: best 100 vs bar 60: 'transferred to colonial secretary's office as third clerk in' ~ 'Clerk'
- [FAIL] honour: no shared honour
- [PASS] edition_cooccurrence: 2 agreeing edition-year(s) [1886, 1888] pos~100 (bar: >=2)
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

