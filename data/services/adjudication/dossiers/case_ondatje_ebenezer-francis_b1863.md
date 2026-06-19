<!-- {"case_id": "case_ondatje_ebenezer-francis_b1863", "bio_ids": ["ondatje_ebenezer-francis_b1863"], "stint_ids": ["Ondatje, E. F___Ceylon___1905"]} -->
# Dossier case_ondatje_ebenezer-francis_b1863

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `ondatje_ebenezer-francis_b1863`

- Printed name: **ONDATJE, Ebenezer Francis**
- Birth year: 1863 (attested in editions [1912, 1913])
- Appears in editions: [1912, 1913]

### Verbatim printed entry text (OCR)

**Version `col1912-L46545.v` — printed in editions [1912, 1913]:**

> ONDATJE, Ebenezer Francis.—B. 1863; ed. Royal Coll., Colombo; cadet, local div., Ceylon civ. ser., July, 1898; dep. fiscal, Colombo, July, 1898; ag. col. storekeeper, Aug., 1899; dep. fiscal, Colombo, Jan., 1900; ag. off. asts., Colombo, Kachcheri, Apr., 1900; dep. fiscal, Colombo, June, 1900; ag. comsnr. of requesta, Colombo, Apr., 1907; dep. fiscal, Colombo, Nov., 1907.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1898 | cadet, local div., Ceylon civ. ser | Ceylon | [1912, 1913] |
| 1 | 1899 | ag. col. storekeeper | Ceylon *(inherited from previous clause)* | [1912, 1913] |
| 2 | 1900 | dep. fiscal, Colombo | Ceylon *(inherited from previous clause)* | [1912, 1913] |
| 3 | 1907 | ag. comsnr. of requesta, Colombo | Ceylon *(inherited from previous clause)* | [1912, 1913] |

## Candidate stint `Ondatje, E. F___Ceylon___1905`

- Staff-list name: **Ondatje, E. F** | colony: **Ceylon** | listed 1905–1913 | editions [1905, 1906, 1907, 1908, 1909, 1910, 1911, 1912, 1913]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1905 | E. F. Ondatje | Deputy Fiscal | Fiscal, Western Province, The Government Agent, Western Province | — | — |
| 1906 | E. F. Ondatje | Deputy Fiscal | Northern Circuit | — | — |
| 1907 | E. F. Ondatje | Deputy Fiscal | Judicial Establishment | — | — |
| 1908 | E. F. Ondatje | Deputy Fiscal | Fiscal | — | — |
| 1909 | E. F. Ondatje | Deputy Fiscal | Northern Circuit | — | — |
| 1910 | E. F. Ondatje | Deputy Fiscal | Fiscal, Western Province, The Government Agent, Western Province | — | — |
| 1911 | E. F. Ondatje | Deputy Fiscal | NORTHERN CIRCUIT | — | — |
| 1912 | E. F. Ondatje | Deputy Fiscal | Northern Circuit | — | — |
| 1913 | E. F. Ondatje | Deputy Fiscal | Judicial Establishment | — | — |

### Deterministic checks: `ondatje_ebenezer-francis_b1863` vs `Ondatje, E. F___Ceylon___1905`

- [PASS] surname_gate: bio 'ONDATJE' vs stint 'Ondatje, E. F' (exact)
- [PASS] initials: bio ['E', 'F'] ~ stint ['E', 'F']
- [PASS] age_gate: stint starts 1905, birth 1863 (age 42)
- [PASS] colony: 4 placed event(s) resolve to 'Ceylon'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1905-1913
- [PASS] position_sim: best 65 vs bar 60: 'dep. fiscal, Colombo' ~ 'Deputy Fiscal'
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

