<!-- {"case_id": "case_bernasko_p-w_e1882", "bio_ids": ["bernasko_p-w_e1882"], "stint_ids": ["Bernasko, P. W___Gold Coast___1889"]} -->
# Dossier case_bernasko_p-w_e1882

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `bernasko_p-w_e1882`

- Printed name: **BERNASKO, P. W.**
- Birth year: not printed
- Appears in editions: [1896, 1897]

### Verbatim printed entry text (OCR)

**Version `col1896-L37539.v` — printed in editions [1896, 1897]:**

> BERNASKO, P. W.—Clk. (temp.) col. sec. off. G. Coast, 1882; dep. regtr. and interpr. Saltpond, 1886; regtr. and interpr. Divn. Ct. Cape Coast, 1889, also regtr. of deeds, West Prov.; 1st Class regtr., 1893; asst. sec. to commiss. of enquiry into native cts., Aug., 1894; 2nd liut. G. C. Volrs., 1894.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1882 | Clk. (temp.) col. sec. off. | Gold Coast | [1896, 1897] |
| 1 | 1886 | dep. regtr. and interpr. | Saltpond | [1896, 1897] |
| 2 | 1889 | regtr. and interpr. Divn. Ct., also regtr. of deeds | Cape Coast | [1896, 1897] |
| 3 | 1893 | 1st Class regtr. | — | [1896, 1897] |
| 4 | 1894 | asst. sec. to commiss. of enquiry into native cts. | — | [1896, 1897] |
| 5 | 1894 | 2nd liut. | Gold Coast | [1896, 1897] |

## Candidate stint `Bernasko, P. W___Gold Coast___1889`

- Staff-list name: **Bernasko, P. W** | colony: **Gold Coast** | listed 1889–1906 | editions [1889, 1890, 1894, 1896, 1897, 1898, 1900, 1905, 1906]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1889 | P. W. Bernasko | Deputy Registrar | Deputy Registrars and Interpreters | — | — |
| 1890 | P. W. Bernasko | — | Deputy Registrars and Interpreters | — | — |
| 1894 | P. W. Bernasko | 1st Class Registrar | Registrars and Clerks | — | — |
| 1896 | P. W. Bernasko | 1st-Class Registrar | Registrars and Clerks | — | — |
| 1897 | P. W. Bernasko | 1st-Class Registrar | Registrars and Clerks | — | — |
| 1898 | P. W. Bernasko | 1st-Class Registrar | Registrars and Clerks | — | — |
| 1900 | P. W. Bernasko | 1st-Class Registrar | Registrars and Clerks | — | — |
| 1905 | P. W. Bernasko | District Commissioner | Judicial Department | — | — |
| 1906 | P. W. Bernasko | District Commissioner | Judicial Department | — | — |

### Deterministic checks: `bernasko_p-w_e1882` vs `Bernasko, P. W___Gold Coast___1889`

- [PASS] surname_gate: bio 'BERNASKO' vs stint 'Bernasko, P. W' (exact)
- [PASS] initials: bio ['P', 'W'] ~ stint ['P', 'W']
- [PASS] age_gate: stint starts 1889; no printed birth year — UNCHECKED
- [PASS] colony: 2 placed event(s) resolve to 'Gold Coast'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1889-1906
- [FAIL] position_sim: best 33 vs bar 60: '2nd liut.' ~ 'Deputy Registrar'
- [FAIL] honour: no shared honour
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

