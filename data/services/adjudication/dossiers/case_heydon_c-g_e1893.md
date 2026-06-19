<!-- {"case_id": "case_heydon_c-g_e1893", "bio_ids": ["heydon_c-g_e1893"], "stint_ids": ["Heydon, C. G___New South Wales___1905"]} -->
# Dossier case_heydon_c-g_e1893

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `heydon_c-g_e1893`

- Printed name: **HEYDON, C. G**
- Birth year: not printed
- Appears in editions: [1911, 1912, 1913, 1914, 1915, 1917, 1918, 1919]

### Verbatim printed entry text (OCR)

**Version `col1911-L45444.v` — printed in editions [1911, 1912, 1913, 1914, 1915, 1917, 1918, 1919]:**

> HEYDON, C. G., K.C.—Atty.-gen. and M.L.C., N.S. Wales, 1893; dist. ct. judge, Mar., 1900; pres. of arbitn. ct., and pres. of indust. ct., June, 1905; sole comsnr. for consolidating statutes of N.S. Wales, 1906.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1893 | Atty.-gen. and M.L.C., N.S. Wales | Nova Scotia | [1911, 1912, 1913, 1914, 1915, 1917, 1918, 1919] |
| 1 | 1900 | dist. ct. judge | Nova Scotia *(inherited from previous clause)* | [1911, 1912, 1913, 1914, 1915, 1917, 1918, 1919] |
| 2 | 1905 | pres. of arbitn. ct., and pres. of indust. ct | Nova Scotia *(inherited from previous clause)* | [1911, 1912, 1913, 1914, 1915, 1917, 1918, 1919] |
| 3 | 1906 | sole comsnr. for consolidating statutes of N.S. Wales | Nova Scotia *(inherited from previous clause)* | [1911, 1912, 1913, 1914, 1915, 1917, 1918, 1919] |

## Candidate stint `Heydon, C. G___New South Wales___1905`

- Staff-list name: **Heydon, C. G** | colony: **New South Wales** | listed 1905–1917 | editions [1905, 1906, 1917]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1905 | C. G. Heydon | District Court Judge | Department of the Attorney-General and of Justice. | — | — |
| 1906 | C. G. Heydon | District Court Judge | Department of the Attorney-General and of Justice | — | — |
| 1917 | C. G. Heydon | Judge | Court of Industrial Arbitration | — | — |

### Deterministic checks: `heydon_c-g_e1893` vs `Heydon, C. G___New South Wales___1905`

- [PASS] surname_gate: bio 'HEYDON' vs stint 'Heydon, C. G' (exact)
- [PASS] initials: bio ['C', 'G'] ~ stint ['C', 'G']
- [PASS] age_gate: stint starts 1905; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'New South Wales'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1905-1917
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

