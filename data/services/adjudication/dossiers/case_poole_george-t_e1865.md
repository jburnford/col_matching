<!-- {"case_id": "case_poole_george-t_e1865", "bio_ids": ["poole_george-t_e1865"], "stint_ids": ["Poole, G. T___Western Australia___1889"]} -->
# Dossier case_poole_george-t_e1865

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 17 official(s) with this surname in the graph's staff lists; 9 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `poole_george-t_e1865`

- Printed name: **POOLE, GEORGE T**
- Birth year: not printed
- Appears in editions: [1886, 1888]

### Verbatim printed entry text (OCR)

**Version `col1886-L35320.v` — printed in editions [1886, 1888]:**

> POOLE, GEORGE T.—Assistant-instructor British architects; superintendent public works, Western Australia, 1865.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1865 | superintendent public works | Western Australia | [1886, 1888] |

## Candidate stint `Poole, G. T___Western Australia___1889`

- Staff-list name: **Poole, G. T** | colony: **Western Australia** | listed 1889–1898 | editions [1889, 1890, 1894, 1896, 1898]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1889 | G. T. Poole | Superintendent of Works | Works and Railways Department | — | — |
| 1890 | G. T. Poole | Superintendent of Works | Works and Railways Department | — | — |
| 1894 | G. T. Poole | Colonial Architect and Superintendent of Works | Works and Buildings | — | — |
| 1896 | G. T. Poole | Colonial Architect and Superintendent of Works | Works and Buildings | — | — |
| 1898 | G. T. Poole | Assistant Engineer-in-Chief | Works and Buildings | — | — |

### Deterministic checks: `poole_george-t_e1865` vs `Poole, G. T___Western Australia___1889`

- [PASS] surname_gate: bio 'POOLE' vs stint 'Poole, G. T' (exact)
- [PASS] initials: bio ['G', 'T'] ~ stint ['G', 'T']
- [PASS] age_gate: stint starts 1889; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Western Australia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1889-1898
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

