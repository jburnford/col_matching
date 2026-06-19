<!-- {"case_id": "case_doyly_john_e1869", "bio_ids": ["doyly_john_e1869"], "stint_ids": ["D'Oyly, John___St Vincent___1879", "D'Oyly, John___Windward Islands___1877"]} -->
# Dossier case_doyly_john_e1869

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['doyly_john_e1869'] carry a single initial only — the namesake trap applies.

## Biography `doyly_john_e1869`

- Printed name: **DOYLY, JOHN**
- Birth year: not printed
- Appears in editions: [1883]

### Verbatim printed entry text (OCR)

**Version `col1883-L27248.v` — printed in editions [1883]:**

> DOYLY, JOHN.—Police magistrate, Windward district, St. Vincent, 1872; acting postmaster from 1869 to 1872; immigration agent, 1870 to 1872. Is an assistant justice of the supreme court of judicature.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1869–1872 | acting postmaster | — | [1883] |
| 1 | 1870–1872 | immigration agent | — | [1883] |
| 2 | 1872–1872 | Police magistrate | St. Vincent | [1883] |

## Candidate stint `D'Oyly, John___St Vincent___1879`

- Staff-list name: **D'Oyly, John** | colony: **St Vincent** | listed 1879–1880 | editions [1879, 1880]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1879 | John D'Oyly | — | Judicial Establishment | — | — |
| 1879 | J. D'Oyly | Assistant Justices | Judicial Establishment | — | — |
| 1880 | J D'Oyly | Assistant Justices | Judicial Establishment | — | — |
| 1880 | John D'Oyly | Police Magistrates | Judicial Establishment | — | — |

### Deterministic checks: `doyly_john_e1869` vs `D'Oyly, John___St Vincent___1879`

- [PASS] surname_gate: bio 'DOYLY' vs stint 'D'Oyly, John' (exact)
- [PASS] initials: bio ['J'] ~ stint ['J']
- [PASS] age_gate: stint starts 1879; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'St Vincent'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1879-1880
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `D'Oyly, John___Windward Islands___1877`

- Staff-list name: **D'Oyly, John** | colony: **Windward Islands** | listed 1877–1883 | editions [1877, 1878, 1880, 1883]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | J D'Oyly | Assistant Justices | Judicial Establishment | — | — |
| 1877 | John D'Oyly | — | Judicial Establishment | — | — |
| 1878 | John D'Oyly | Police Magistrates | Judicial Establishment | — | — |
| 1878 | J D'Oyly | Assistant Justices | Judicial Establishment | — | — |
| 1880 | J D'Oyly | Assistant Justices | Judicial Establishment | — | — |
| 1880 | John D'Oyly | — | Judicial Establishment | — | — |
| 1883 | John D'Oyly | Police Magistrates | Judicial Establishment | — | — |

### Deterministic checks: `doyly_john_e1869` vs `D'Oyly, John___Windward Islands___1877`

- [PASS] surname_gate: bio 'DOYLY' vs stint 'D'Oyly, John' (exact)
- [PASS] initials: bio ['J'] ~ stint ['J']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Windward Islands'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1877-1883
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

