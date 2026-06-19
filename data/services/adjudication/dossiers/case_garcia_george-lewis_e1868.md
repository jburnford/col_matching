<!-- {"case_id": "case_garcia_george-lewis_e1868", "bio_ids": ["garcia_george-lewis_e1868"], "stint_ids": ["Garcia, George___Trinidad___1894"]} -->
# Dossier case_garcia_george-lewis_e1868

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 13 official(s) with this surname in the graph's staff lists; 6 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `garcia_george-lewis_e1868`

- Printed name: **GARCIA, GEORGE LEWIS**
- Birth year: not printed
- Appears in editions: [1889, 1890, 1894, 1896, 1897]

### Verbatim printed entry text (OCR)

**Version `col1889-L33253.v` — printed in editions [1889, 1890, 1894, 1896, 1897]:**

> GARCIA, GEORGE LEWIS.—Ed., Stonyhurst Coll., First B.A., Univ. of Lond., 1866; called to the bar, Inner Temple, Hilary, 1868; member leg. coun., Trinidad, 1882; agr. solicitor-general, April to Dec., 1885, Feb. to May, 1886, June to July, 1888; confirmed Aug., 1888; attorney-general, 1892; member of the royal commission on the franchise and division of the colony into electoral districts, Jan., 1888.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1868–1868 | called to the bar | — | [1889, 1890, 1894, 1896, 1897] |
| 1 | 1882–1882 | member leg. coun. | Trinidad | [1889, 1890, 1894, 1896, 1897] |
| 2 | 1885–1888 | agr. solicitor-general | — | [1889, 1890, 1894, 1896, 1897] |
| 3 | 1888–1888 | solicitor-general | — | [1889, 1890, 1894, 1896, 1897] |
| 4 | 1888–1888 | member of the royal commission on the franchise and division of the colony into electoral districts | — | [1889, 1890, 1894, 1896, 1897] |
| 5 | 1892–1892 | attorney-general | — | [1889, 1890, 1894, 1896, 1897] |

## Candidate stint `Garcia, George___Trinidad___1894`

- Staff-list name: **Garcia, George** | colony: **Trinidad** | listed 1894–1897 | editions [1894, 1896, 1897]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1894 | G. L. Garcia | Attorney-General | Judicial Department | — | — |
| 1896 | G. L. Garcia | Attorney-General | Judicial Department | — | — |
| 1897 | G. L. Garcia | Attorney-General | Judicial Department | — | — |

### Deterministic checks: `garcia_george-lewis_e1868` vs `Garcia, George___Trinidad___1894`

- [PASS] surname_gate: bio 'GARCIA' vs stint 'Garcia, George' (exact)
- [PASS] initials: bio ['G', 'L'] ~ stint ['G']
- [PASS] age_gate: stint starts 1894; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Trinidad'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1894-1897
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

