<!-- {"case_id": "case_jameson_adam_e1901", "bio_ids": ["jameson_adam_e1901"], "stint_ids": ["Jameson, A___Transvaal___1906"]} -->
# Dossier case_jameson_adam_e1901

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 16 official(s) with this surname in the graph's staff lists; 9 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['jameson_adam_e1901'] carry a single initial only — the namesake trap applies.

## Biography `jameson_adam_e1901`

- Printed name: **JAMESON, ADAM**
- Birth year: not printed
- Appears in editions: [1905, 1906, 1907, 1908, 1909, 1910, 1912, 1913, 1914]

### Verbatim printed entry text (OCR)

**Version `col1905-L44118.v` — printed in editions [1905, 1906, 1907, 1908, 1909, 1910, 1912, 1913, 1914]:**

> JAMESON, ADAM.—M.B. (1883), M.D. (1897), Edin.; M.L.C., metropolitan suburban province, W. Aust., 1901; hon. minister, 1901; min. for lands, 1901-2; ditto, 1902; comsnr. of crown lands, Transvaal, 1903; mem. exec. and legis. couns.; mem. I.C.C.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1901–1901 | M.L.C., metropolitan suburban province | Western Australia | [1905, 1906, 1907, 1908, 1909, 1910, 1912, 1913, 1914] |
| 1 | 1901–1901 | hon. minister | — | [1905, 1906, 1907, 1908, 1909, 1910, 1912, 1913, 1914] |
| 2 | 1901–1902 | min. for lands | — | [1905, 1906, 1907, 1908, 1909, 1910, 1912, 1913, 1914] |
| 3 | 1902–1902 | ditto | — | [1905, 1906, 1907, 1908, 1909, 1910, 1912, 1913, 1914] |
| 4 | 1903–1903 | comsnr. of crown lands | Transvaal | [1905, 1906, 1907, 1908, 1909, 1910, 1912, 1913, 1914] |

## Candidate stint `Jameson, A___Transvaal___1906`

- Staff-list name: **Jameson, A** | colony: **Transvaal** | listed 1906–1907 | editions [1906, 1907]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1906 | A. Jameson | Commissioner for Lands | Land Department | — | — |
| 1907 | A Jameson | Commissioner for Lands | Land Department | — | — |

### Deterministic checks: `jameson_adam_e1901` vs `Jameson, A___Transvaal___1906`

- [PASS] surname_gate: bio 'JAMESON' vs stint 'Jameson, A' (exact)
- [PASS] initials: bio ['A'] ~ stint ['A']
- [PASS] age_gate: stint starts 1906; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Transvaal'
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

