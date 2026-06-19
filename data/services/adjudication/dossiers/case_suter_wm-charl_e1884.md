<!-- {"case_id": "case_suter_wm-charl_e1884", "bio_ids": ["suter_wm-charl_e1884"], "stint_ids": ["Suter, W. C___Straits Settlements___1899"]} -->
# Dossier case_suter_wm-charl_e1884

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 4 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `suter_wm-charl_e1884`

- Printed name: **SUTER, WM. CHARL**
- Birth year: not printed
- Appears in editions: [1905, 1906, 1907, 1908, 1909, 1910, 1911, 1912, 1913, 1914, 1915]

### Verbatim printed entry text (OCR)

**Version `col1905-L46223.v` — printed in editions [1905, 1906, 1907, 1908, 1909, 1910, 1911, 1912, 1913, 1914, 1915]:**

> SUTER, WM. CHARL.—Asst. master, govt. English schls., Singapore, 22nd Nov., 1884; ch. clk., col. sec.'s office, 1st July, 1888; shorthand reporter to leg. coun. in addition to other duties, 1st July, 1897.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1884 | Asst. master, govt. English schls. | Singapore | [1905, 1906, 1907, 1908, 1909, 1910, 1911, 1912, 1913, 1914, 1915] |
| 1 | 1888 | ch. clk., col. sec.'s office | Singapore *(inherited from previous clause)* | [1905, 1906, 1907, 1908, 1909, 1910, 1911, 1912, 1913, 1914, 1915] |
| 2 | 1897 | shorthand reporter to leg. coun. in addition to other duties | Singapore *(inherited from previous clause)* | [1905, 1906, 1907, 1908, 1909, 1910, 1911, 1912, 1913, 1914, 1915] |

## Candidate stint `Suter, W. C___Straits Settlements___1899`

- Staff-list name: **Suter, W. C** | colony: **Straits Settlements** | listed 1899–1911 | editions [1899, 1905, 1908, 1910, 1911]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1899 | W. C. Suter | Chief Clerk and Shorthand Reporter | Colonial Secretary's Department | — | — |
| 1905 | W. C. Suter | Chief Clerk and Shorthand Reporter | Colonial Secretary's Office | — | — |
| 1908 | W. C. Suter | Chief Clerk and Shorthand Reporter | Colonial Secretary's Office | — | — |
| 1910 | W. C. Suter | Chief Clerk and Shorthand Reporter | Colonial Secretary's Office | — | — |
| 1911 | W. C. Suter | Chief Clerk and Shorthand Reporter | Colonial Secretary's Office | — | — |

### Deterministic checks: `suter_wm-charl_e1884` vs `Suter, W. C___Straits Settlements___1899`

- [PASS] surname_gate: bio 'SUTER' vs stint 'Suter, W. C' (exact)
- [PASS] initials: bio ['W', 'C'] ~ stint ['W', 'C']
- [PASS] age_gate: stint starts 1899; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Straits Settlements'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1899-1911
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

