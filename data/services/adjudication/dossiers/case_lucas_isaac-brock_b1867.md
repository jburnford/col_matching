<!-- {"case_id": "case_lucas_isaac-brock_b1867", "bio_ids": ["lucas_isaac-brock_b1867"], "stint_ids": ["Lucas, Isaac Benson___Canada___1914"]} -->
# Dossier case_lucas_isaac-brock_b1867

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 26 official(s) with this surname in the graph's staff lists; 14 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `lucas_isaac-brock_b1867`

- Printed name: **LUCAS, ISAAC BROCK**
- Birth year: 1867 (attested in editions [1913, 1914, 1915, 1917, 1918, 1919, 1920])
- Honours: K.C., M.L.A.
- Terminal: resigned 1919 — “defeated at g.e., Oct., 1919, and resigned portfolio.”
- Appears in editions: [1911, 1912, 1913, 1914, 1915, 1917, 1918, 1919, 1920]

### Verbatim printed entry text (OCR)

**Version `col1913-L47640.v` — printed in editions [1913, 1914, 1915, 1917, 1918, 1919, 1920]:**

> LUCAS, HON. ISAAC BROCK, K.C., Ontario.—B. 1867; ed. Strathroy collegiate; elec. to legis., Ontario, 1898, 1902, 1905, 1908, 1911 and 1914; chrmn. of private bills comteee.; min. without portfolio in Ontario cabinet, 1909; prov. treas., 1913; atty.-gen., 1914; defeated at g.e., Oct., 1919, and resigned portfolio.

**Version `col1911-L46309.v` — printed in editions [1911, 1912]:**

> LUCAS, Hon. Isaac Brock, K.C., M.L.A., Ontario.—B. 1867; ed. Strathroy collegiate; elec. to legis., Ontario, 1898, 1902, 1905 and 1908; chmn. of private bills comtce.; min. without portfolio in Ontario cabinet.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1898–1914 | elec. to legis. | Ontario | [1911, 1912, 1913, 1914, 1915, 1917, 1918, 1919, 1920] |
| 1 | 1909 | min. without portfolio | Ontario | [1913, 1914, 1915, 1917, 1918, 1919, 1920] |
| 2 | 1913 | prov. treas. | — | [1913, 1914, 1915, 1917, 1918, 1919, 1920] |
| 3 | 1914 | atty.-gen. | — | [1913, 1914, 1915, 1917, 1918, 1919, 1920] |

## Candidate stint `Lucas, Isaac Benson___Canada___1914`

- Staff-list name: **Lucas, Isaac Benson** | colony: **Canada** | listed 1914–1919 | editions [1914, 1917, 1918, 1919]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1914 | I. B. Lucas | Treasurer | Executive Council | — | — |
| 1917 | Isaac Benson Lucas | Member | Legislative Assembly | — | — |
| 1917 | Isaac Benson Lucas | Attorney-General | Executive Council | — | — |
| 1917 | Isaac Benson Lucas | Attorney-General | Attorney-General's Department | — | — |
| 1918 | Isaac Benson Lucas | Attorney-General | Attorney-General's Department | — | — |
| 1918 | Isaac Benson Lucas | Attorney-General | Executive Council | — | — |
| 1919 | Isaac Benson Lucas | Attorney-General | Attorney-General's Department | — | — |

### Deterministic checks: `lucas_isaac-brock_b1867` vs `Lucas, Isaac Benson___Canada___1914`

- [PASS] surname_gate: bio 'LUCAS' vs stint 'Lucas, Isaac Benson' (exact)
- [PASS] initials: bio ['I', 'B'] ~ stint ['I', 'B']
- [PASS] age_gate: stint starts 1914, birth 1867 (age 47)
- [PASS] colony: 2 placed event(s) resolve to 'Canada'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1914-1919
- [FAIL] position_sim: best 21 vs bar 60: 'elec. to legis.' ~ 'Attorney-General'
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

