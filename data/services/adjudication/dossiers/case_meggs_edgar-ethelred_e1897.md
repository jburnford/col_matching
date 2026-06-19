<!-- {"case_id": "case_meggs_edgar-ethelred_e1897", "bio_ids": ["meggs_edgar-ethelred_e1897"], "stint_ids": ["Meggs, Edgar E___Leeward Islands___1915"]} -->
# Dossier case_meggs_edgar-ethelred_e1897

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `meggs_edgar-ethelred_e1897`

- Printed name: **MEGGS, EDGAR ETHELRED**
- Birth year: not printed
- Appears in editions: [1917, 1918]

### Verbatim printed entry text (OCR)

**Version `col1917-L51789.v` — printed in editions [1917, 1918]:**

> MEGGS, EDGAR ETHELRED.—Called to the bar, Middle Temple, 30th June, 1897; ag. mag., St. Kitts-Nevis, 1907 and 1911; ag. asst. to atty.-gen., St. Kitts, and dep. judge of summary juris. ct., and addtl. mag., Anguilla, 1910 and 1911; ag. crown attorney, 1915; unoffl. M.L.C., St. Kitts-Nevis, and of gen. legis. coun.; crown attorney, St. Kitts-Nevis, Aug., 1916; mem. exec. coun., Sept., 1916.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1897–1897 | Called to the bar | — | [1917, 1918] |
| 1 | 1907–1911 | ag. mag. | St. Kitts-Nevis | [1917, 1918] |
| 2 | 1910–1911 | ag. asst. to atty.-gen., and dep. judge of summary juris. ct., and addtl. mag. | St. Kitts | [1917, 1918] |
| 3 | 1915–1915 | ag. crown attorney | — | [1917, 1918] |
| 4 | 1916–1916 | crown attorney | St. Kitts-Nevis | [1917, 1918] |
| 5 | 1916–1916 | mem. exec. coun. | — | [1917, 1918] |

## Candidate stint `Meggs, Edgar E___Leeward Islands___1915`

- Staff-list name: **Meggs, Edgar E** | colony: **Leeward Islands** | listed 1915–1918 | editions [1915, 1917, 1918]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1915 | E. E. Meggs | Member | Legislative Council | — | — |
| 1917 | Hon. E. E. Meggs | Legislative Council Member | Legislative Council | — | — |
| 1917 | Edgar E. Meggs | Crown-Attorney | Judicial | — | — |
| 1917 | E. E. Meggs | Crown Attorney | Judicial Establishment | — | — |
| 1918 | Edgar E. Meggs | Crown-Attorney | Judicial | — | — |
| 1918 | E. E. Meggs | Crown Attorney | Judicial Establishment | — | — |
| 1918 | E. E. Meggs | Crown Attorney | Executive Council | — | — |
| 1918 | E. E. Meggs | Visiting Justices | Gaol | — | — |

### Deterministic checks: `meggs_edgar-ethelred_e1897` vs `Meggs, Edgar E___Leeward Islands___1915`

- [PASS] surname_gate: bio 'MEGGS' vs stint 'Meggs, Edgar E' (exact)
- [PASS] initials: bio ['E', 'E'] ~ stint ['E', 'E']
- [PASS] age_gate: stint starts 1915; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Leeward Islands'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1915-1918
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

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

