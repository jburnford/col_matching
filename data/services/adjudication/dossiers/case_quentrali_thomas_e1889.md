<!-- {"case_id": "case_quentrali_thomas_e1889", "bio_ids": ["quentrali_thomas_e1889", "quentrall_thomas_e1889"], "stint_ids": ["Quentall, Thomas___Cape of Good Hope___1906"]} -->
# Dossier case_quentrali_thomas_e1889

## Case context

- 2 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['quentrali_thomas_e1889', 'quentrall_thomas_e1889'] carry a single initial only — the namesake trap applies.
- CONTESTED: stint(s) ['Quentall, Thomas___Cape of Good Hope___1906'] have more than one claimant biography in this case.

## Biography `quentrali_thomas_e1889`

- Printed name: **QUENTRALI, Thomas**
- Birth year: not printed
- Appears in editions: [1912]

### Verbatim printed entry text (OCR)

**Version `col1912-L47063.v` — printed in editions [1912]:**

> QUENTRALI, Thomas.—Mining eng., Kimberley, Cape, July, 1889; inspr. of Kimberley, July, 1891.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1889 | Mining eng., Kimberley | Cape of Good Hope | [1912] |
| 1 | 1891 | inspr. of Kimberley | Cape of Good Hope *(inherited from previous clause)* | [1912] |

## Biography `quentrall_thomas_e1889`

- Printed name: **QUENTRALL, THOMAS**
- Birth year: not printed
- Appears in editions: [1896, 1898, 1899, 1900, 1905, 1907, 1908, 1909, 1910, 1911, 1913, 1914, 1915, 1917]

### Verbatim printed entry text (OCR)

**Version `col1896-L40927.v` — printed in editions [1896]:**

> QUENTRALL, THOMAS.—Mining engineer, Kimberley, Cape, July, 1889; inspr. of mines, July, 1891; appointed to fixed establishment, July, 1892.

**Version `col1898-L35504.v` — printed in editions [1898, 1899, 1900, 1905, 1907, 1908, 1909, 1910, 1911, 1913, 1914, 1915, 1917]:**

> QUENTRALL, THOMAS.—Mining, engrnr., Kimberley, Cape, July, 1889; inspr. of mines, Kimberley, July, 1891.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1889 | Mining engineer, Kimberley | Cape of Good Hope | [1896, 1898, 1899, 1900, 1905, 1907, 1908, 1909, 1910, 1911, 1913, 1914, 1915, 1917] |
| 1 | 1891 | inspr. of mines | Cape of Good Hope *(inherited from previous clause)* | [1896, 1898, 1899, 1900, 1905, 1907, 1908, 1909, 1910, 1911, 1913, 1914, 1915, 1917] |
| 2 | 1892 | appointed to fixed establishment | Cape of Good Hope *(inherited from previous clause)* | [1896] |

## Candidate stint `Quentall, Thomas___Cape of Good Hope___1906`

- Staff-list name: **Quentall, Thomas** | colony: **Cape of Good Hope** | listed 1906–1907 | editions [1906, 1907]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1906 | Thomas Quentall | Inspector of Mines, Kimberley and Barkly West | Diamond Mines | — | — |
| 1907 | Thomas Quentall | Inspector of Mines, Kimberley and Barkly West | Diamond Mines | — | — |

### Deterministic checks: `quentrali_thomas_e1889` vs `Quentall, Thomas___Cape of Good Hope___1906`

- [PASS] surname_gate: bio 'QUENTRALI' vs stint 'Quentall, Thomas' (fuzzy:2)
- [PASS] initials: bio ['T'] ~ stint ['T']
- [PASS] age_gate: stint starts 1906; no printed birth year — UNCHECKED
- [PASS] colony: 2 placed event(s) resolve to 'Cape of Good Hope'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1906-1907
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

### Deterministic checks: `quentrall_thomas_e1889` vs `Quentall, Thomas___Cape of Good Hope___1906`

- [PASS] surname_gate: bio 'QUENTRALL' vs stint 'Quentall, Thomas' (fuzzy:1)
- [PASS] initials: bio ['T'] ~ stint ['T']
- [PASS] age_gate: stint starts 1906; no printed birth year — UNCHECKED
- [PASS] colony: 3 placed event(s) resolve to 'Cape of Good Hope'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1906-1907
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

