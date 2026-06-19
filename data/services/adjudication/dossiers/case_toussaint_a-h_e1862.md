<!-- {"case_id": "case_toussaint_a-h_e1862", "bio_ids": ["toussaint_a-h_e1862"], "stint_ids": ["Toussaint, A. H___Ceylon___1877", "Toussaint, A___Mauritius___1908"]} -->
# Dossier case_toussaint_a-h_e1862

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 10 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `toussaint_a-h_e1862`

- Printed name: **TOUSSAINT, A. H**
- Birth year: not printed
- Appears in editions: [1883, 1886, 1888, 1889, 1890]

### Verbatim printed entry text (OCR)

**Version `col1883-L29777.v` — printed in editions [1883, 1886, 1888, 1889, 1890]:**

> TOUSSAINT, A. H.—Medical assistant, Ceylon, 1862; assistant colonial surgeon, 1867.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1862 | Medical assistant | Ceylon | [1883, 1886, 1888, 1889, 1890] |
| 1 | 1867 | assistant colonial surgeon | Ceylon *(inherited from previous clause)* | [1883, 1886, 1888, 1889, 1890] |

## Candidate stint `Toussaint, A. H___Ceylon___1877`

- Staff-list name: **Toussaint, A. H** | colony: **Ceylon** | listed 1877–1890 | editions [1877, 1878, 1879, 1880, 1883, 1886, 1888, 1889, 1890]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | A. H. Toussaint | Assistant Colonial Surgeons | Medical Department | — | — |
| 1878 | A. H. Toussaint | Assistant Colonial Surgeons | Medical Department | — | — |
| 1879 | A. H. Toussaint | Assistant Colonial Surgeons | Medical Department | — | — |
| 1880 | A. H. Toussaint | Assistant Colonial Surgeons | Medical Department | — | — |
| 1883 | A. H. Toussaint | Assistant Colonial Surgeon | Medical Department | — | — |
| 1886 | A. H. Toussaint | Assistant Colonial Surgeon | Medical Department | — | — |
| 1888 | A. H. Toussaint | Assistant Colonial Surgeon | Medical Department | — | — |
| 1889 | A. H. Toussaint | Assistant Colonial Surgeon | Medical Department | — | — |
| 1890 | A. H. Toussaint | Assistant Colonial Surgeon | Medical Department | — | — |

### Deterministic checks: `toussaint_a-h_e1862` vs `Toussaint, A. H___Ceylon___1877`

- [PASS] surname_gate: bio 'TOUSSAINT' vs stint 'Toussaint, A. H' (exact)
- [PASS] initials: bio ['A', 'H'] ~ stint ['A', 'H']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [PASS] colony: 2 placed event(s) resolve to 'Ceylon'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1877-1890
- [PASS] position_sim: best 100 vs bar 60: 'assistant colonial surgeon' ~ 'Assistant Colonial Surgeon'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: ALL supporting events inherit their place from an earlier clause — weak evidence

## Candidate stint `Toussaint, A___Mauritius___1908`

- Staff-list name: **Toussaint, A** | colony: **Mauritius** | listed 1908–1918 | editions [1908, 1909, 1910, 1911, 1912, 1913, 1914, 1915, 1917, 1918]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1908 | A. Toussaint | Tidecutters | Outdoor Branch | — | — |
| 1909 | A. Toussaint | Tidewaiters | Outdoor Branch | — | — |
| 1910 | A. Toussaint | Tidewaiters | Outdoor Branch | — | — |
| 1911 | A. Toussaint | Tidewaiters | Outdoor Branch | — | — |
| 1912 | A. Toussaint | Tidewaiters | Outdoor Branch | — | — |
| 1913 | A. Toussaint | Tidewaiters | Outdoor Branch | — | — |
| 1914 | A. Toussaint | 1st Class Tidewaiters | Outdoor Branch | — | — |
| 1915 | A. Toussaint | 1st Class Tidewaiters | Outdoor Branch | — | — |
| 1917 | A. Toussaint | 1st Class Tidewaiters | Outdoor Branch | — | — |
| 1918 | A. Toussaint | 1st Class Tidewaiters | Outdoor Branch | — | — |

### Deterministic checks: `toussaint_a-h_e1862` vs `Toussaint, A___Mauritius___1908`

- [PASS] surname_gate: bio 'TOUSSAINT' vs stint 'Toussaint, A' (exact)
- [PASS] initials: bio ['A', 'H'] ~ stint ['A']
- [PASS] age_gate: stint starts 1908; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Mauritius'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1908-1918
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

