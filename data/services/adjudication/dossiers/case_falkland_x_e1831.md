<!-- {"case_id": "case_falkland_x_e1831", "bio_ids": ["falkland_x_e1831"], "stint_ids": ["Falkland, Lord___Canada___1886"]} -->
# Dossier case_falkland_x_e1831

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['falkland_x_e1831'] carry a single initial only — the namesake trap applies.

## Biography `falkland_x_e1831`

- Printed name: **FALKLAND, (no given names printed)**
- Birth year: not printed
- Honours: G.C.H. (1831), Privy Councillor (1837)
- Appears in editions: [1886]

### Verbatim printed entry text (OCR)

**Version `col1886-L33300.v` — printed in editions [1886]:**

> FALKLAND, LORD VISCOUNT (Scotland, creat. 1620); BARON HUNSDON, 1832 (United Kingdom), by which title he holds his seat in the House of Lords; Privy Councillor, 1837; G.C.H., 1831.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1831 | G.C.H. | — | [1886] |
| 1 | 1832 | BARON HUNSDON | United Kingdom | [1886] |
| 2 | 1837 | Privy Councillor | — | [1886] |

## Candidate stint `Falkland, Lord___Canada___1886`

- Staff-list name: **Falkland, Lord** | colony: **Canada** | listed 1886–1890 | editions [1886, 1888, 1889, 1890]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1886 | Falkland | Lieutenant-Governor | Lieutenant-Governors | — | — |
| 1888 | Lord Falkland | Lieutenant-Governor | Lieutenant-Governors | — | — |
| 1889 | Falkland | Lieutenant-Governor | Lieutenant-Governors | — | — |
| 1890 | Lord Falkland | Lieutenant-Governor | Lieutenant-Governors since 1800.* | — | — |

### Deterministic checks: `falkland_x_e1831` vs `Falkland, Lord___Canada___1886`

- [PASS] surname_gate: bio 'FALKLAND' vs stint 'Falkland, Lord' (exact)
- [PASS] initials: bio ['?'] ~ stint ['L']
- [PASS] age_gate: stint starts 1886; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Canada'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1886-1890
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

