<!-- {"case_id": "case_bodeker_henry-albert_e1899", "bio_ids": ["bodeker_henry-albert_e1899"], "stint_ids": ["Bodeker, H. A___Kenya___1909"]} -->
# Dossier case_bodeker_henry-albert_e1899

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `bodeker_henry-albert_e1899`

- Printed name: **BODEKER, HENRY ALBERT**
- Birth year: not printed
- Honours: C.M, M.B
- Appears in editions: [1908, 1909, 1910, 1911, 1912, 1913]

### Verbatim printed entry text (OCR)

**Version `col1908-L43271.v` — printed in editions [1908, 1909, 1910, 1911, 1912, 1913]:**

> BODEKER, HENRY ALBERT, M.B., C.M., Glasgow.—Ed. at Glasgow Univ. and in Germany; med. offr., Uganda Prot., 1st Sept., 1899; med. offr., East Africa Prot., 1st Apr., 1902.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1899 | med. offr. | Uganda | [1908, 1909, 1910, 1911, 1912, 1913] |
| 1 | 1902 | med. offr., East Africa Prot | Uganda *(inherited from previous clause)* | [1908, 1909, 1910, 1911, 1912, 1913] |

## Candidate stint `Bodeker, H. A___Kenya___1909`

- Staff-list name: **Bodeker, H. A** | colony: **Kenya** | listed 1909–1913 | editions [1909, 1910, 1911, 1912, 1913]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1909 | H. A. Bodeker | Medical Officer | Medical | — | — |
| 1910 | H. A. Bodeker | Medical Officer | Medical (East Africa and Uganda) | — | — |
| 1911 | H. A. Bodeker | Medical Officer | Medical (East Africa and Uganda) | — | — |
| 1912 | H. A. Bodeker | Medical Officer | Medical (East Africa and Uganda) | — | — |
| 1913 | H. A. Bodeker | Medical Officer | Medical | — | — |

### Deterministic checks: `bodeker_henry-albert_e1899` vs `Bodeker, H. A___Kenya___1909`

- [PASS] surname_gate: bio 'BODEKER' vs stint 'Bodeker, H. A' (exact)
- [PASS] initials: bio ['H', 'A'] ~ stint ['H', 'A']
- [PASS] age_gate: stint starts 1909; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Kenya'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1909-1913
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

