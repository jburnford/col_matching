<!-- {"case_id": "case_prentice_archibald-hepburn-gardiner_e1913", "bio_ids": ["prentice_archibald-hepburn-gardiner_e1913"], "stint_ids": ["Prentice, A. H. G___Uganda___1914", "Prentice, H___Mauritius___1912"]} -->
# Dossier case_prentice_archibald-hepburn-gardiner_e1913

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `prentice_archibald-hepburn-gardiner_e1913`

- Printed name: **PRENTICE, ARCHIBALD HEPBURN GARDINER**
- Birth year: not printed
- Appears in editions: [1925]

### Verbatim printed entry text (OCR)

**Version `col1925-L58754.v` — printed in editions [1925]:**

> PRENTICE, ARCHIBALD HEPBURN GARDINER—Ast. treas., Uganda, 1913; senr. ast. treas., Apr., 1919; ag. dep. treas., in 1919, 1920, 1921, and 1922; dep. treas., Tanganyika Terr., 22nd Sept., 1922; ag. treas., Dec., 1922 to Sept., 1923.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1913 | Ast. treas. | Uganda | [1925] |
| 1 | 1919 | senr. ast. treas. | — | [1925] |
| 2 | 1919–1922 | ag. dep. treas. | — | [1925] |
| 3 | 1922 | dep. treas. | Tanganyika Territory | [1925] |

## Candidate stint `Prentice, A. H. G___Uganda___1914`

- Staff-list name: **Prentice, A. H. G** | colony: **Uganda** | listed 1914–1922 | editions [1914, 1915, 1917, 1918, 1919, 1920, 1921, 1922]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1914 | A. H. G. Prentice | Assistant | Treasury and Savings Bank | — | — |
| 1915 | A. H. G. Prentice | Assistant | Treasury and Savings Bank | — | — |
| 1917 | A. H. G. Prentice | Assistant | Treasury and Savings Bank | — | — |
| 1918 | A. H. G. Prentice | Assistant | Treasury and Savings Bank | — | — |
| 1919 | A. H. G. Prentice | Assistant | Treasury and Savings Bank | — | — |
| 1920 | A. H. G. Prentice | Assistant | Treasury and Savings Bank | — | — |
| 1921 | A. H. G. Prentice | Senior Assistant Treasurer | Treasury and Savings Bank | — | — |
| 1922 | A. H. G. Prentice | Senior Assistant Treasurer | Treasury and Savings Bank | — | — |

### Deterministic checks: `prentice_archibald-hepburn-gardiner_e1913` vs `Prentice, A. H. G___Uganda___1914`

- [PASS] surname_gate: bio 'PRENTICE' vs stint 'Prentice, A. H. G' (exact)
- [PASS] initials: bio ['A', 'H', 'G'] ~ stint ['A', 'H', 'G']
- [PASS] age_gate: stint starts 1914; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Uganda'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1914-1922
- [FAIL] position_sim: best 51 vs bar 60: 'Ast. treas.' ~ 'Senior Assistant Treasurer'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

## Candidate stint `Prentice, H___Mauritius___1912`

- Staff-list name: **Prentice, H** | colony: **Mauritius** | listed 1912–1914 | editions [1912, 1913, 1914]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1912 | H. Prentice | Commanding Royal Engineers | Military Officers | — | — |
| 1913 | H. Prentice | Commanding Royal Engineers | Military Officers | — | Lieut.-Col. |
| 1914 | H. Prentice | Commanding Royal Engineers | Military Officers | — | Lieut.-Col. |

### Deterministic checks: `prentice_archibald-hepburn-gardiner_e1913` vs `Prentice, H___Mauritius___1912`

- [PASS] surname_gate: bio 'PRENTICE' vs stint 'Prentice, H' (exact)
- [PASS] initials: bio ['A', 'H', 'G'] ~ stint ['H']
- [PASS] age_gate: stint starts 1912; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Mauritius'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1912-1914
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

