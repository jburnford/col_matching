<!-- {"case_id": "case_vilbro_robert_e1860", "bio_ids": ["vilbro_robert_e1860"], "stint_ids": ["Vilbro, R___Mauritius___1888"]} -->
# Dossier case_vilbro_robert_e1860

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['vilbro_robert_e1860'] carry a single initial only — the namesake trap applies.

## Biography `vilbro_robert_e1860`

- Printed name: **VILBRO, Robert**
- Birth year: not printed
- Appears in editions: [1894, 1896, 1897, 1898, 1899]

### Verbatim printed entry text (OCR)

**Version `col1894-L34384.v` — printed in editions [1894, 1896, 1897, 1898, 1899]:**

> VILBRO, Robert.—Asst. master, government schools, Mauritius, May, 1860; master, April, 1866; assistant statistician, registrar-general's office, June, 1877; joint district clerk, Port Louis, June, 1878; immigrant shipping officer, Dec., 1883; senior clerk, procurator-general's department, May, 1885; agent, depot, mercantile marine, July to Dec., 1896; received a large gold medal from the inhabitants of Pamplemousses for special public services as member of relief committee after the cyclone of April, 1892.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1860 | Asst. master, government schools | Mauritius | [1894, 1896, 1897, 1898, 1899] |
| 1 | 1866 | master | Mauritius *(inherited from previous clause)* | [1894, 1896, 1897, 1898, 1899] |
| 2 | 1877 | assistant statistician, registrar-general's office | Mauritius *(inherited from previous clause)* | [1894, 1896, 1897, 1898, 1899] |
| 3 | 1878 | joint district clerk, Port Louis | Mauritius *(inherited from previous clause)* | [1894, 1896, 1897, 1898, 1899] |
| 4 | 1883 | immigrant shipping officer | Mauritius *(inherited from previous clause)* | [1894, 1896, 1897, 1898, 1899] |
| 5 | 1885 | senior clerk, procurator-general's department | Mauritius *(inherited from previous clause)* | [1894, 1896, 1897, 1898, 1899] |
| 6 | 1892 | received a large gold medal from the inhabitants of Pamplemousses for special public services as member of relief committee after the cyclone of | Mauritius *(inherited from previous clause)* | [1894, 1896, 1897, 1898, 1899] |
| 7 | 1896 | agent, depot, mercantile marine | Mauritius *(inherited from previous clause)* | [1894, 1896, 1897, 1898, 1899] |

## Candidate stint `Vilbro, R___Mauritius___1888`

- Staff-list name: **Vilbro, R** | colony: **Mauritius** | listed 1888–1899 | editions [1888, 1890, 1894, 1896, 1897, 1898, 1899]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1888 | R. Vilbro | Clerks | Procureur General's Department | — | — |
| 1890 | R. Vilbro | Clerk | Procureur General's Department | — | — |
| 1894 | R. Vilbro | 3rd Class Clerk | Procureur-General's Department | — | — |
| 1896 | R. Vilbro | 3rd Class Clerk | Procureur-General's Department | — | — |
| 1897 | R. Vilbro | 3rd Class Clerk | Procureur-General's Department | — | — |
| 1898 | R. Vilbro | 3rd Class Clerk | Procureur-General's Department | — | — |
| 1899 | R. Vilbro | 3rd Class Clerk | Procureur-General's Department | — | — |

### Deterministic checks: `vilbro_robert_e1860` vs `Vilbro, R___Mauritius___1888`

- [PASS] surname_gate: bio 'VILBRO' vs stint 'Vilbro, R' (exact)
- [PASS] initials: bio ['R'] ~ stint ['R']
- [PASS] age_gate: stint starts 1888; no printed birth year — UNCHECKED
- [PASS] colony: 8 placed event(s) resolve to 'Mauritius'
- [PASS] tenure_overlap: 3 event tenure(s) overlap stint years 1888-1899
- [PASS] position_sim: best 100 vs bar 60: 'senior clerk, procurator-general's department' ~ 'Clerk'
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

