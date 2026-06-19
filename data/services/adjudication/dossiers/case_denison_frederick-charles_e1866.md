<!-- {"case_id": "case_denison_frederick-charles_e1866", "bio_ids": ["denison_frederick-charles_e1866"], "stint_ids": ["Denison, F. C___Canada___1888"]} -->
# Dossier case_denison_frederick-charles_e1866

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 4 official(s) with this surname in the graph's staff lists; 4 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `denison_frederick-charles_e1866`

- Printed name: **DENISON, FREDERICK CHARLES**
- Birth year: not printed
- Honours: C.M.G. (1885)
- Appears in editions: [1888, 1889, 1890, 1894, 1896]

### Verbatim printed entry text (OCR)

**Version `col1888-L33022.v` — printed in editions [1888, 1889, 1894]:**

> DENISON, LIBUT.—COL. FREDERICK CHARLES, C.M.G. (1885).—Cornet in governor-general's body guard during Fenian raid into Canada in 1866; in Red River expedition, 1870, as A.D.C. to Col. (now Viscount) Wolsley; and in command of Canadian voyageurs in the Soudan campaign, 1884-85; medal with two clasps.

**Version `col1890-L33576.v` — printed in editions [1890, 1896]:**

> DENISON, Lieut.-Col. FREDERICK CHARLES, C.M.G. (1886).—Cornet in governor-general's body guard during Fenian raid into Canada in 1866; in Red River expedition, 1870, as A.D.C. to Col. (now Viscount) Wolseley; and in command of Canadian voyageurs in the Soudan campaign, 1884-85; medal with two clasps.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1866–1866 | Cornet | Canada | [1888, 1889, 1890, 1894, 1896] |
| 1 | 1870–1870 | A.D.C. to Col. (now Viscount) Wolsley | — | [1888, 1889, 1890, 1894, 1896] |
| 2 | 1884–1885 | in command of Canadian voyageurs | Soudan | [1888, 1889, 1890, 1894, 1896] |

## Candidate stint `Denison, F. C___Canada___1888`

- Staff-list name: **Denison, F. C** | colony: **Canada** | listed 1888–1896 | editions [1888, 1890, 1894, 1896]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1888 | Lt.-Col. F. C. Denison | Member of Parliament | House of Commons | C.M.G. | Lt.-Col. |
| 1890 | Lt.-Col. F. C. Denison | Member | House of Commons | C.M.G. | Lt.-Col. |
| 1894 | F. C. Denison | Member of Parliament | House of Commons | C.M.G. | Lt.-Col. |
| 1896 | F. C. Denison | Member | House of Commons | — | Lt.-Col. |

### Deterministic checks: `denison_frederick-charles_e1866` vs `Denison, F. C___Canada___1888`

- [PASS] surname_gate: bio 'DENISON' vs stint 'Denison, F. C' (exact)
- [PASS] initials: bio ['F', 'C'] ~ stint ['F', 'C']
- [PASS] age_gate: stint starts 1888; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Canada'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1888-1896
- [FAIL] position_sim: no overlapping placed event to compare
- [PASS] honour: shared: C.M.G.
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

