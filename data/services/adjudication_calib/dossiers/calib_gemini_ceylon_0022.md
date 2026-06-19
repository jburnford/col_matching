<!-- {"case_id": "calib_gemini_ceylon_0022", "bio_ids": ["browne_dodwell-f_e1892"], "stint_ids": ["Browne, Dodwell F___Ceylon___1894"]} -->
# Dossier calib_gemini_ceylon_0022

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 167 official(s) with this surname in the graph's staff lists; 48 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `browne_dodwell-f_e1892`

- Printed name: **BROWNE, DODWELL F**
- Birth year: not printed
- Appears in editions: [1894, 1896, 1898, 1899, 1900, 1905]

### Verbatim printed entry text (OCR)

**Version `col1894-L30545.v` — printed in editions [1894, 1896, 1898, 1899, 1900, 1905]:**

> BROWNE, DODWELL F.—District judge, Colombo, 1892.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1892 | District judge | Colombo | [1894, 1896, 1898, 1899, 1900, 1905] |

## Candidate stint `Browne, Dodwell F___Ceylon___1894`

- Staff-list name: **Browne, Dodwell F** | colony: **Ceylon** | listed 1894–1900 | editions [1894, 1896, 1898, 1900]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1894 | Dodwell F. Browne | District Judge | — | — | — |
| 1896 | Dodwell F. Browne | District Judge | District of Colombo and Midland Circuit | — | — |
| 1898 | Dodwell F. Browne | District Judge | District of Colombo and Midland Circuit | — | — |
| 1900 | Dodwell F. Browne | District Judge | District of Colombo and Midland Circuit | — | — |

### Deterministic checks: `browne_dodwell-f_e1892` vs `Browne, Dodwell F___Ceylon___1894`

- [PASS] surname_gate: bio 'BROWNE' vs stint 'Browne, Dodwell F' (exact)
- [PASS] initials: bio ['D', 'F'] ~ stint ['D', 'F']
- [PASS] age_gate: stint starts 1894; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Ceylon'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1894-1900
- [PASS] position_sim: best 100 vs bar 60: 'District judge' ~ 'District Judge'
- [FAIL] honour: no shared honour
- [PASS] edition_cooccurrence: 4 agreeing edition-year(s) [1894, 1896, 1898, 1900] pos~100 (bar: >=2)
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

