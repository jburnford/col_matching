<!-- {"case_id": "case_leitch_james_b1850", "bio_ids": ["leitch_james_b1850"], "stint_ids": ["Leitch, James___Canada___1913"]} -->
# Dossier case_leitch_james_b1850

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 5 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['leitch_james_b1850'] carry a single initial only — the namesake trap applies.

## Biography `leitch_james_b1850`

- Printed name: **LEITCH, James**
- Birth year: 1850 (attested in editions [1913, 1914, 1915, 1917])
- Appears in editions: [1913, 1914, 1915, 1917]

### Verbatim printed entry text (OCR)

**Version `col1913-L47496.v` — printed in editions [1913, 1914, 1915, 1917]:**

> LEITCH, Hon. James.—B. 1850; called to the bar, 1876; K.C., 1888; barrister at Cornwall, Ontario, for many years; mayor of Cornwall, 1885-6; unsuccessful cand. for legis. assem. of Ontario, 1886 and 1896, and for H. of C., 1896, chmn., Ontario rlyw. and mun. bd., 1906; judge of high ct., Ontario, 1912.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1876–1876 | called to the bar | — | [1913, 1914, 1915, 1917] |
| 1 | 1885–1886 | mayor | Ontario | [1913, 1914, 1915, 1917] |
| 2 | 1886–1896 | unsuccessful cand. for legis. assem. of Ontario and for H. of C. | Ontario | [1913, 1914, 1915, 1917] |
| 3 | 1888–1888 | K.C. | — | [1913, 1914, 1915, 1917] |
| 4 | 1906–1906 | chmn., Ontario rlyw. and mun. bd. | Ontario | [1913, 1914, 1915, 1917] |
| 5 | 1912–1912 | judge of high ct. | Ontario | [1913, 1914, 1915, 1917] |

## Candidate stint `Leitch, James___Canada___1913`

- Staff-list name: **Leitch, James** | colony: **Canada** | listed 1913–1915 | editions [1913, 1914, 1915]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1913 | James Leitch | Puisne Judge | Supreme Court of Ontario | — | — |
| 1914 | James Leitch | Puisne Judges | SUPREME COURT OF ONTARIO - HIGH COURT DIVISION | — | — |
| 1915 | James Leitch | Puisne Judges | Supreme Court of Ontario - High Court Division | — | — |

### Deterministic checks: `leitch_james_b1850` vs `Leitch, James___Canada___1913`

- [PASS] surname_gate: bio 'LEITCH' vs stint 'Leitch, James' (exact)
- [PASS] initials: bio ['J'] ~ stint ['J']
- [PASS] age_gate: stint starts 1913, birth 1850 (age 63)
- [PASS] colony: 4 placed event(s) resolve to 'Canada'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1913-1915
- [FAIL] position_sim: best 59 vs bar 60: 'judge of high ct.' ~ 'Puisne Judge'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): 1 agreeing edition-year(s) [1913] pos~59 (bar: >=2)
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

