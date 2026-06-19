<!-- {"case_id": "case_woodehouse_armine_b1860", "bio_ids": ["woodehouse_armine_b1860"], "stint_ids": ["Woodhouse, C. A___Nigeria___1915"]} -->
# Dossier case_woodehouse_armine_b1860

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 11 official(s) with this surname in the graph's staff lists; 8 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['woodehouse_armine_b1860'] carry a single initial only — the namesake trap applies.

## Biography `woodehouse_armine_b1860`

- Printed name: **WOODEHOUSE, ARMINE**
- Birth year: 1860 (attested in editions [1888])
- Appears in editions: [1888]

### Verbatim printed entry text (OCR)

**Version `col1888-L36855.v` — printed in editions [1888]:**

> WOODEHOUSE, THE HON. ARMINE.—Second son of the Earl of Kimberley, born 1860; appointed assistant secretary (unpaid) to the Earl of Kimberley, Nov., 1881; in same capacity at the India Office, 17th Dec., 1882, to June, 1885; first private secretary at the India Office, Feb. to Aug., 1886.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1881 | assistant secretary (unpaid) | — | [1888] |
| 1 | 1882–1885 | assistant secretary | India | [1888] |
| 2 | 1886–1886 | first private secretary | India | [1888] |

## Candidate stint `Woodhouse, C. A___Nigeria___1915`

- Staff-list name: **Woodhouse, C. A** | colony: **Nigeria** | listed 1915–1918 | editions [1915, 1918]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1915 | C. A. Woodhouse | Sixty-four Assistant District Officers | NORTHERN PROVINCES | — | — |
| 1918 | C. A. Woodhouse | Thirty‑Two Second Class District Officer | Northern Provinces | — | — |

### Deterministic checks: `woodehouse_armine_b1860` vs `Woodhouse, C. A___Nigeria___1915`

- [PASS] surname_gate: bio 'WOODEHOUSE' vs stint 'Woodhouse, C. A' (fuzzy:1)
- [PASS] initials: bio ['A'] ~ stint ['C', 'A']
- [PASS] age_gate: stint starts 1915, birth 1860 (age 55)
- [FAIL] colony: no placed event resolves to 'Nigeria'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1915-1918
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

