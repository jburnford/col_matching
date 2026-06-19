<!-- {"case_id": "case_mcbride_peter_b1867", "bio_ids": ["mcbride_peter_b1867"], "stint_ids": ["McBride, P___Australia___1912"]} -->
# Dossier case_mcbride_peter_b1867

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 10 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['mcbride_peter_b1867'] carry a single initial only — the namesake trap applies.

## Biography `mcbride_peter_b1867`

- Printed name: **McBRIDE, PETER**
- Birth year: 1867 (attested in editions [1918, 1919, 1920])
- Honours: HON. SIR PETER KT. BACH (1915), KT. BACH (1915)
- Appears in editions: [1914, 1915, 1917, 1918, 1919, 1920, 1922, 1923]

### Verbatim printed entry text (OCR)

**Version `col1918-L52353.v` — printed in editions [1918, 1919, 1920]:**

> McBRIDE, HON. SIR PETER, KT. BACH. (1915).—B. 1867; M.L.A., Victoria, 1897; min. of mines and forests, Jan., 1909; agent-gen. in London for Victoria, 1913; mem. of comtee. for settm't. of ex-serv. men within the Empire, 1917.

**Version `col1917-L51399.v` — printed in editions [1917, 1923]:**

> MOBRIDE, HON. SIR PETER, KT. BACH. (1915).—B. 1867; M.L.A., Victoria, 1897; min. of mines and forests, Jan., 1909; agent-gen. in London for Victoria, 1913; mem. of comttee. for settm. of ex-serv. men within the Empire, 1917.

**Version `col1922-L54176.v` — printed in editions [1922]:**

> MCEBRIDE, HON. SIR PETER KT. BACH (1915).—B. 1867; M.L.A., Victoria, 1897; min. of mines and forests, Jan., 1909; agent-gen. in London for Victoria, 1913; mem. of comte. for settm. of ex-serv. men within the Empire, 1917.

**Version `col1914-L48140.v` — printed in editions [1914, 1915]:**

> McBRIDE, HON. PETER.—B. 1867; mem. of legis. assembly, Victoria, 1897; min. of mines and forests, Jan., 1909; agent-gen. in London for Victoria, 1913.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1897 | M.L.A. | Victoria | [1914, 1915, 1917, 1918, 1919, 1920, 1922, 1923] |
| 1 | 1909 | min. of mines and forests | Victoria *(inherited from previous clause)* | [1914, 1915, 1917, 1918, 1919, 1920, 1922, 1923] |
| 2 | 1913 | agent-gen. in London for Victoria | Victoria *(inherited from previous clause)* | [1914, 1915, 1917, 1918, 1919, 1920, 1922, 1923] |
| 3 | 1917 | mem. of comtee. for settm't. of ex-serv. men within the Empire | Victoria *(inherited from previous clause)* | [1917, 1918, 1919, 1920, 1922, 1923] |

## Candidate stint `McBride, P___Australia___1912`

- Staff-list name: **McBride, P** | colony: **Australia** | listed 1912–1918 | editions [1912, 1913, 1918]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1912 | P. McBride | Minister of Mines and Forests | Cabinet | — | — |
| 1913 | P. McBride | Minister of Railways, Mines and Forests | Cabinet | — | — |
| 1913 | P. McBride | Minister of Mines and Forests | DEPARTMENT OF MINES | — | — |
| 1913 | P. McBride | Minister of Railways | VICTORIAN RAILWAYS | — | — |
| 1918 | P. McBride | Agent-General for Victoria in the United Kingdom | London Agency | — | — |

### Deterministic checks: `mcbride_peter_b1867` vs `McBride, P___Australia___1912`

- [PASS] surname_gate: bio 'McBRIDE' vs stint 'McBride, P' (exact)
- [PASS] initials: bio ['P'] ~ stint ['P']
- [PASS] age_gate: stint starts 1912, birth 1867 (age 45)
- [FAIL] colony: no placed event resolves to 'Australia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1912-1918
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

