<!-- {"case_id": "case_magrath_thos-henry_e1853", "bio_ids": ["magrath_thos-henry_e1853"], "stint_ids": ["Magrath, T. H___Tasmania___1877"]} -->
# Dossier case_magrath_thos-henry_e1853

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 5 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `magrath_thos-henry_e1853`

- Printed name: **MAGRATH, THOS. HENRY**
- Birth year: not printed
- Appears in editions: [1896, 1897, 1898, 1900, 1905, 1906, 1907, 1908, 1909, 1910, 1911, 1912, 1913]

### Verbatim printed entry text (OCR)

**Version `col1896-L40227.v` — printed in editions [1896, 1897, 1898, 1900, 1905, 1906, 1907, 1908, 1909, 1910, 1911, 1912, 1913]:**

> MAGRATH, THOS. HENRY.—Junior clerk, P.O., Tasmania, 1853; chief clerk, 1869; comptroller of money orders, 1879 and of savings bank, 1882; sec. to P.O., 1888.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1853 | Junior clerk, P.O. | Tasmania | [1896, 1897, 1898, 1900, 1905, 1906, 1907, 1908, 1909, 1910, 1911, 1912, 1913] |
| 1 | 1869 | chief clerk | — | [1896, 1897, 1898, 1900, 1905, 1906, 1907, 1908, 1909, 1910, 1911, 1912, 1913] |
| 2 | 1879 | comptroller of money orders | — | [1896, 1897, 1898, 1900, 1905, 1906, 1907, 1908, 1909, 1910, 1911, 1912, 1913] |
| 3 | 1882 | comptroller of savings bank | — | [1896, 1897, 1898, 1900, 1905, 1906, 1907, 1908, 1909, 1910, 1911, 1912, 1913] |
| 4 | 1888 | sec. to P.O. | — | [1896, 1897, 1898, 1900, 1905, 1906, 1907, 1908, 1909, 1910, 1911, 1912, 1913] |

## Candidate stint `Magrath, T. H___Tasmania___1877`

- Staff-list name: **Magrath, T. H** | colony: **Tasmania** | listed 1877–1888 | editions [1877, 1878, 1879, 1880, 1888]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | T. H. Magrath | Clerk | Post Office | — | — |
| 1878 | T. H. Magrath | Clerk | Post Office | — | — |
| 1879 | T. H. Magrath | Clerk | Post Office | — | — |
| 1880 | T. H. Magrath | Clerk | Post Office | — | — |
| 1888 | T. H. Magrath | Comptroller and Actuary of Money Order Branch | Post Office | — | — |

### Deterministic checks: `magrath_thos-henry_e1853` vs `Magrath, T. H___Tasmania___1877`

- [PASS] surname_gate: bio 'MAGRATH' vs stint 'Magrath, T. H' (exact)
- [PASS] initials: bio ['T', 'H'] ~ stint ['T', 'H']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Tasmania'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1877-1888
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

