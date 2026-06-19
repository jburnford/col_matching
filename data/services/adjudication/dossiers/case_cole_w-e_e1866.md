<!-- {"case_id": "case_cole_w-e_e1866", "bio_ids": ["cole_w-e_e1866"], "stint_ids": ["Cole, E___Windward Islands___1877"]} -->
# Dossier case_cole_w-e_e1866

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 96 official(s) with this surname in the graph's staff lists; 31 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Cole, E___Windward Islands___1877` is also gate-compatible with biography(ies) outside this case: ['cole_fred-edward_e1886'] (already linked elsewhere or filtered).

## Biography `cole_w-e_e1866`

- Printed name: **COLE, W. E**
- Birth year: not printed
- Appears in editions: [1883, 1886]

### Verbatim printed entry text (OCR)

**Version `col1883-L26918.v` — printed in editions [1883, 1886]:**

> COLE, W. E.—Landing-waiter, Gold Coast, Lagos, July, 1866; post-office clerk in 1871; copying clerk, treasury, 1872; 3rd clerk, 1875; and postmaster, August, 1874.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1866 | Landing-waiter, Gold Coast | Lagos | [1883, 1886] |
| 1 | 1871 | post-office clerk in | Lagos *(inherited from previous clause)* | [1883, 1886] |
| 2 | 1872 | copying clerk, treasury | Lagos *(inherited from previous clause)* | [1883, 1886] |
| 3 | 1874 | and postmaster | Lagos *(inherited from previous clause)* | [1883, 1886] |
| 4 | 1875 | 3rd clerk | Lagos *(inherited from previous clause)* | [1883, 1886] |

## Candidate stint `Cole, E___Windward Islands___1877`

- Staff-list name: **Cole, E** | colony: **Windward Islands** | listed 1877–1878 | editions [1877, 1878]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | E. Cole | Minister | Ministers of Religion | — | — |
| 1878 | E. Cole | Wesleyan Ministers | Ministers of Religion | — | — |

### Deterministic checks: `cole_w-e_e1866` vs `Cole, E___Windward Islands___1877`

- [PASS] surname_gate: bio 'COLE' vs stint 'Cole, E' (exact)
- [PASS] initials: bio ['W', 'E'] ~ stint ['E']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Windward Islands'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1877-1878
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

