<!-- {"case_id": "case_savona_sigismondo_e1875", "bio_ids": ["savona_sigismondo_e1875"], "stint_ids": ["Savona, S___Malta___1883", "Savona, S___Virgin Islands___1890"]} -->
# Dossier case_savona_sigismondo_e1875

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 7 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['savona_sigismondo_e1875'] carry a single initial only — the namesake trap applies.

## Biography `savona_sigismondo_e1875`

- Printed name: **SAVONA, Sigismondo**
- Birth year: not printed
- Terminal: resigned 1887 — “resigned, 1887”
- Appears in editions: [1883, 1886, 1888]

### Verbatim printed entry text (OCR)

**Version `col1883-L29416.v` — printed in editions [1883, 1886, 1888]:**

> SAVONA, Sigismondo.—Elected member of the Council of Government (Malta), Dec., 1875; appointed Director of Education, June, 1880, and ex officio member of Council; member of Executive Council, 1883; resigned, 1887.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1875 | member of the Council of Government | Malta | [1883, 1886, 1888] |
| 1 | 1880 | Director of Education | — | [1883, 1886, 1888] |
| 2 | 1883 | member of Executive Council | — | [1883, 1886, 1888] |

## Candidate stint `Savona, S___Malta___1883`

- Staff-list name: **Savona, S** | colony: **Malta** | listed 1883–1886 | editions [1883, 1886]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1883 | S. Savona | Director of Education | Educational | — | — |
| 1886 | S. Savona | Director of Education | Educational | — | — |

### Deterministic checks: `savona_sigismondo_e1875` vs `Savona, S___Malta___1883`

- [PASS] surname_gate: bio 'SAVONA' vs stint 'Savona, S' (exact)
- [PASS] initials: bio ['S'] ~ stint ['S']
- [PASS] age_gate: stint starts 1883; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Malta'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1883-1886
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Savona, S___Virgin Islands___1890`

- Staff-list name: **Savona, S** | colony: **Virgin Islands** | listed 1890–1894 | editions [1890, 1894]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1890 | S. Savona | Member | Unofficial Members | — | — |
| 1894 | S. Savona | Unofficial Member | Unofficial Members | — | — |

### Deterministic checks: `savona_sigismondo_e1875` vs `Savona, S___Virgin Islands___1890`

- [PASS] surname_gate: bio 'SAVONA' vs stint 'Savona, S' (exact)
- [PASS] initials: bio ['S'] ~ stint ['S']
- [PASS] age_gate: stint starts 1890; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Virgin Islands'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1890-1894
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

