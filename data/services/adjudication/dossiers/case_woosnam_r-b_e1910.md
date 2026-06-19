<!-- {"case_id": "case_woosnam_r-b_e1910", "bio_ids": ["woosnam_r-b_e1910"], "stint_ids": ["Woosnam, R. B___Kenya___1911"]} -->
# Dossier case_woosnam_r-b_e1910

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `woosnam_r-b_e1910`

- Printed name: **WOOSNAM, R. B**
- Birth year: not printed
- Appears in editions: [1912, 1913, 1914, 1915]

### Verbatim printed entry text (OCR)

**Version `col1912-L48509.v` — printed in editions [1912, 1913, 1914, 1915]:**

> WOOSNAM, R. B.—Game warden, E.A.P., 1910.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1910 | Game warden | East Africa Protectorate | [1912, 1913, 1914, 1915] |

## Candidate stint `Woosnam, R. B___Kenya___1911`

- Staff-list name: **Woosnam, R. B** | colony: **Kenya** | listed 1911–1915 | editions [1911, 1912, 1913, 1914, 1915]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1911 | R. B. Woosnam | Ranger | Game | — | — |
| 1912 | R. B. Woosnam | Ranger | Game | — | — |
| 1913 | R. B. Woosnam | Ranger | Game | — | — |
| 1914 | R. B. Woosnam | Ranger | Game | — | — |
| 1915 | R. B. Woosnam | Ranger | Game | — | — |

### Deterministic checks: `woosnam_r-b_e1910` vs `Woosnam, R. B___Kenya___1911`

- [PASS] surname_gate: bio 'WOOSNAM' vs stint 'Woosnam, R. B' (exact)
- [PASS] initials: bio ['R', 'B'] ~ stint ['R', 'B']
- [PASS] age_gate: stint starts 1911; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Kenya'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1911-1915
- [FAIL] position_sim: best 35 vs bar 60: 'Game warden' ~ 'Ranger'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

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

