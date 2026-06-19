<!-- {"case_id": "case_scott_eric-eleanor_e1913", "bio_ids": ["scott_eric-eleanor_e1913"], "stint_ids": ["Scott, E___Western Australia___1894"]} -->
# Dossier case_scott_eric-eleanor_e1913

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 151 official(s) with this surname in the graph's staff lists; 65 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `scott_eric-eleanor_e1913`

- Printed name: **SCOTT, ERIC ELEANOR**
- Birth year: not printed
- Appears in editions: [1934]

### Verbatim printed entry text (OCR)

**Version `col1934-L62856.v` — printed in editions [1934]:**

> SCOTT, ERIC ELEANOR.—Ent. C.O. as typist, July, 1913; shorthand writer, Aug., 1918; cler. offr., 9th Mar., 1922.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1913 | Ent. C.O. as typist | Colonial Office | [1934] |
| 1 | 1918 | shorthand writer | Colonial Office *(inherited from previous clause)* | [1934] |
| 2 | 1922 | cler. offr | Colonial Office *(inherited from previous clause)* | [1934] |

## Candidate stint `Scott, E___Western Australia___1894`

- Staff-list name: **Scott, E** | colony: **Western Australia** | listed 1894–1896 | editions [1894, 1896]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1894 | E. Scott | Assistant Inspector of Permanent Way | Eastern Railway | — | — |
| 1896 | E. Scott | Assistant Inspector of Permanent Way | Railways and Tramways | — | — |

### Deterministic checks: `scott_eric-eleanor_e1913` vs `Scott, E___Western Australia___1894`

- [PASS] surname_gate: bio 'SCOTT' vs stint 'Scott, E' (exact)
- [PASS] initials: bio ['E', 'E'] ~ stint ['E']
- [PASS] age_gate: stint starts 1894; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Western Australia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1894-1896
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

