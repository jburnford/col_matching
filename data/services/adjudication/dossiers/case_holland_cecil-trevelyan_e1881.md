<!-- {"case_id": "case_holland_cecil-trevelyan_e1881", "bio_ids": ["holland_cecil-trevelyan_e1881"], "stint_ids": ["Holland, C. T___Mauritius___1896"]} -->
# Dossier case_holland_cecil-trevelyan_e1881

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 28 official(s) with this surname in the graph's staff lists; 17 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `holland_cecil-trevelyan_e1881`

- Printed name: **HOLLAND, CECIL TREVELYAN**
- Birth year: not printed
- Appears in editions: [1896, 1897, 1898, 1899, 1900]

### Verbatim printed entry text (OCR)

**Version `col1896-L39497.v` — printed in editions [1896, 1897, 1898, 1899, 1900]:**

> HOLLAND, CAPT. THE HON. CECIL TREVELYAN.—Joined 3rd Batt. Queen's R.W.S. Regt., 1881; joined Coldstream Gds., 1884; capt., May, 1892; exchanged to 60th Rifles, Aug., 1892; served in Shikim campaign 1885; present at Hasheen, Tofrek, and Tamai (medal, clasp, and Khedive's star); attached to Egyptian army, Feb. to Aug., 1888; A.D.C. to gov't., Malta, Aug., 1888 to Feb., 1890, and to G.O.C., S. Africa, Feb., 1890 to Aug., 1891; attached to Lagos constab'y., Jan., 1894; acted as dist. comsrr.; inspr.-gen. of pol., Mauritius, 1895; nominated mem. coun. of gort., Mauritius, 1896.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1881 | Joined 3rd Batt. Queen's R.W.S. Regt | — | [1896, 1897, 1898, 1899, 1900] |
| 1 | 1884 | joined Coldstream Gds | — | [1896, 1897, 1898, 1899, 1900] |
| 2 | 1885 | served in Shikim campaign | — | [1896, 1897, 1898, 1899, 1900] |
| 3 | 1888 | attached to Egyptian army | — | [1896, 1897, 1898, 1899, 1900] |
| 4 | 1888–1890 | A.D.C. to gov't. | Malta | [1896, 1897, 1898, 1899, 1900] |
| 5 | 1890–1891 | to G.O.C., S. Africa | Malta *(inherited from previous clause)* | [1896, 1897, 1898, 1899, 1900] |
| 6 | 1892 | capt | — | [1896, 1897, 1898, 1899, 1900] |
| 7 | 1892 | exchanged to 60th Rifles | — | [1896, 1897, 1898, 1899, 1900] |
| 8 | 1894 | attached to Lagos constab'y | Malta *(inherited from previous clause)* | [1896, 1897, 1898, 1899, 1900] |
| 9 | 1895 | inspr.-gen. of pol. | Mauritius | [1896, 1897, 1898, 1899, 1900] |
| 10 | 1896 | nominated mem. coun. of gort. | Mauritius | [1896, 1897, 1898, 1899, 1900] |

## Candidate stint `Holland, C. T___Mauritius___1896`

- Staff-list name: **Holland, C. T** | colony: **Mauritius** | listed 1896–1898 | editions [1896, 1897, 1898]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1896 | Captain Hon. C. T. Holland | Inspector-General | Police Department | — | Captain |
| 1897 | C. T. Holland | Inspector-General | Police Department | — | Captain |
| 1898 | Captain Hon. C. T. Holland | Inspector-General | Police Department | — | Captain |

### Deterministic checks: `holland_cecil-trevelyan_e1881` vs `Holland, C. T___Mauritius___1896`

- [PASS] surname_gate: bio 'HOLLAND' vs stint 'Holland, C. T' (exact)
- [PASS] initials: bio ['C', 'T'] ~ stint ['C', 'T']
- [PASS] age_gate: stint starts 1896; no printed birth year — UNCHECKED
- [PASS] colony: 2 placed event(s) resolve to 'Mauritius'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1896-1898
- [FAIL] position_sim: best 58 vs bar 60: 'inspr.-gen. of pol.' ~ 'Inspector-General'
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

