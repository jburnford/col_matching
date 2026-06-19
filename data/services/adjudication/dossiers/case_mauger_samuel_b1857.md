<!-- {"case_id": "case_mauger_samuel_b1857", "bio_ids": ["mauger_samuel_b1857"], "stint_ids": ["Mauger, S___Commonwealth Of Australia___1905"]} -->
# Dossier case_mauger_samuel_b1857

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['mauger_samuel_b1857'] carry a single initial only — the namesake trap applies.

## Biography `mauger_samuel_b1857`

- Printed name: **MAUGER, Samuel**
- Birth year: 1857 (attested in editions [1907, 1908, 1909, 1910, 1912, 1913, 1914, 1915, 1917, 1918, 1919])
- Terminal: retired (year not printed) — “has ret. from politics.”
- Appears in editions: [1907, 1908, 1909, 1910, 1912, 1913, 1914, 1915, 1917, 1918, 1919]

### Verbatim printed entry text (OCR)

**Version `col1907-L45788.v` — printed in editions [1907, 1908, 1909, 1910, 1912, 1913, 1914, 1915, 1917, 1918, 1919]:**

> MAUGER, Hon. Samuel.—B. 1857; M.L.A. of Victoria, 1898-1901; elected to 1st house of rep., Commonwealth of Aust., 1901; re-elected, 1903 and 1906; min. without portfolio, 13th Oct., 1906; P.M.G., July, 1907; has ret. from politics.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1898–1901 | M.L.A. | Victoria | [1907, 1908, 1909, 1910, 1912, 1913, 1914, 1915, 1917, 1918, 1919] |
| 1 | 1901–1901 | elected to 1st house of rep. | Australia | [1907, 1908, 1909, 1910, 1912, 1913, 1914, 1915, 1917, 1918, 1919] |
| 2 | 1903–1906 | re-elected | — | [1907, 1908, 1909, 1910, 1912, 1913, 1914, 1915, 1917, 1918, 1919] |
| 3 | 1906–1906 | min. without portfolio | — | [1907, 1908, 1909, 1910, 1912, 1913, 1914, 1915, 1917, 1918, 1919] |
| 4 | 1907–1907 | P.M.G. | — | [1907, 1908, 1909, 1910, 1912, 1913, 1914, 1915, 1917, 1918, 1919] |

## Candidate stint `Mauger, S___Commonwealth Of Australia___1905`

- Staff-list name: **Mauger, S** | colony: **Commonwealth Of Australia** | listed 1905–1907 | editions [1905, 1907]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1905 | S. Mauger | Member of Legislative Assembly | Parliament | — | — |
| 1907 | S. Mauger | Kooyong | — | — | — |

### Deterministic checks: `mauger_samuel_b1857` vs `Mauger, S___Commonwealth Of Australia___1905`

- [PASS] surname_gate: bio 'MAUGER' vs stint 'Mauger, S' (exact)
- [PASS] initials: bio ['S'] ~ stint ['S']
- [PASS] age_gate: stint starts 1905, birth 1857 (age 48)
- [FAIL] colony: no placed event resolves to 'Commonwealth Of Australia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1905-1907
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

