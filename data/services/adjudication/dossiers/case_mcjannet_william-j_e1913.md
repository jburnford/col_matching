<!-- {"case_id": "case_mcjannet_william-j_e1913", "bio_ids": ["mcjannet_william-j_e1913"], "stint_ids": ["McJannet, W. J___Kenya___1915"]} -->
# Dossier case_mcjannet_william-j_e1913

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `mcjannet_william-j_e1913`

- Printed name: **MCJANNET, WILLIAM J**
- Birth year: not printed
- Appears in editions: [1921, 1922, 1923, 1924, 1925]

### Verbatim printed entry text (OCR)

**Version `col1921-L58190.v` — printed in editions [1921, 1922, 1923, 1924, 1925]:**

> MCJANNET, WILLIAM J.—Ed., Irvine Royal Acad. and Technical Coll., Glasgow; astt. engrnr., Uganda Rly., Mar., 1913.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1913 | astt. engrnr., Uganda Rly | Uganda | [1921, 1922, 1923, 1924, 1925] |

## Candidate stint `McJannet, W. J___Kenya___1915`

- Staff-list name: **McJannet, W. J** | colony: **Kenya** | listed 1915–1924 | editions [1915, 1918, 1919, 1920, 1922, 1923, 1924]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1915 | W. J. McJannet | Assistant Engineer | Engineering | — | — |
| 1918 | W. J. McJannet | Assistant Engineer | Engineering | — | — |
| 1919 | W. J. McJannet | Assistant Engineer | Engineering | — | — |
| 1920 | W. J. McJannet | Assistant Engineer | Engineering | — | — |
| 1922 | W. J. McJannet | Assistant Engineers | Engineering | — | — |
| 1923 | W. J. McJannet | Assistant Engineers | Engineering | — | — |
| 1924 | W. J. McJannet | District Engineer | Engineering | — | — |

### Deterministic checks: `mcjannet_william-j_e1913` vs `McJannet, W. J___Kenya___1915`

- [PASS] surname_gate: bio 'MCJANNET' vs stint 'McJannet, W. J' (exact)
- [PASS] initials: bio ['W', 'J'] ~ stint ['W', 'J']
- [PASS] age_gate: stint starts 1915; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Kenya'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1915-1924
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

