<!-- {"case_id": "case_portelli_a-m_e1882", "bio_ids": ["portelli_a-m_e1882"], "stint_ids": ["Portelli, A___Malta___1906", "Portelli, A___Malta___1924"]} -->
# Dossier case_portelli_a-m_e1882

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 7 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `portelli_a-m_e1882`

- Printed name: **PORTELLI, A. M.**
- Birth year: not printed
- Honours: C.M.G. (1882)
- Appears in editions: [1883, 1886, 1888, 1889, 1890, 1894, 1896, 1897, 1898, 1900, 1905, 1906, 1907, 1908, 1909, 1910]

### Verbatim printed entry text (OCR)

**Version `col1883-L29143.v` — printed in editions [1883, 1886, 1888, 1889, 1890, 1894, 1896, 1897, 1898, 1900, 1905, 1906, 1907, 1908, 1909, 1910]:**

> PORTELLI, LIEUT.-COL. A. M., of the Royal Malta Fencible Artillery.—C.M.G. (1882), for services in connection with the Egyptian expedition, 1882.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1882–1882 | — | Egypt | [1883, 1886, 1888, 1889, 1890, 1894, 1896, 1897, 1898, 1900, 1905, 1906, 1907, 1908, 1909, 1910] |

## Candidate stint `Portelli, A___Malta___1906`

- Staff-list name: **Portelli, A** | colony: **Malta** | listed 1906–1908 | editions [1906, 1907, 1908]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1906 | A. Portelli | Assistant Engineers | Electric Lighting Branch | — | — |
| 1907 | A. Portelli | Assistant Engineer | Electric Lighting Branch | — | — |
| 1908 | A. Portelli | Assistant Engineer | Electric Lighting Branch | — | — |

### Deterministic checks: `portelli_a-m_e1882` vs `Portelli, A___Malta___1906`

- [PASS] surname_gate: bio 'PORTELLI' vs stint 'Portelli, A' (exact)
- [PASS] initials: bio ['A', 'M'] ~ stint ['A']
- [PASS] age_gate: stint starts 1906; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Malta'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1906-1908
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Portelli, A___Malta___1924`

- Staff-list name: **Portelli, A** | colony: **Malta** | listed 1924–1925 | editions [1924, 1925]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1924 | A. Portelli | Vicar General | Ecclesiastical | — | — |
| 1925 | A. Portelli | Vicar General | Ecclesiastical | — | — |

### Deterministic checks: `portelli_a-m_e1882` vs `Portelli, A___Malta___1924`

- [PASS] surname_gate: bio 'PORTELLI' vs stint 'Portelli, A' (exact)
- [PASS] initials: bio ['A', 'M'] ~ stint ['A']
- [PASS] age_gate: stint starts 1924; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Malta'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1924-1925
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

