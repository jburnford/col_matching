<!-- {"case_id": "case_oudekerk_g_e1866", "bio_ids": ["oudekerk_g_e1866"], "stint_ids": ["Oudkerk, G. O___British Guiana___1877"]} -->
# Dossier case_oudekerk_g_e1866

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['oudekerk_g_e1866'] carry a single initial only — the namesake trap applies.
- Phase 1 found `oudekerk_g_e1866` ↔ `Oudkerk, G. O___British Guiana___1877` passed its evidence bar but dropped it as ambiguous (a comparable-strength competitor existed).
- NOTE: stint `Oudkerk, G. O___British Guiana___1877` is also gate-compatible with biography(ies) outside this case: ['oudkerk_g_e1866'] (already linked elsewhere or filtered).

## Biography `oudekerk_g_e1866`

- Printed name: **OUDEKERK, G**
- Birth year: not printed
- Appears in editions: [1883]

### Verbatim printed entry text (OCR)

**Version `col1883-L28979.v` — printed in editions [1883]:**

> OUDEKERK, G.—Revenue clerk, audit office, British Guiana, 1866.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1866 | Revenue clerk, audit office | British Guiana | [1883] |

## Candidate stint `Oudkerk, G. O___British Guiana___1877`

- Staff-list name: **Oudkerk, G. O** | colony: **British Guiana** | listed 1877–1889 | editions [1877, 1878, 1879, 1880, 1883, 1886, 1888, 1889]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | G. Oudkerk | Clerk | Audit Office | — | — |
| 1878 | G. O. Oudkerk | Assistant Wharfinger | Customs | — | — |
| 1878 | G. Oudkerk | Clerk | Audit Office | — | — |
| 1879 | G. Oudkerk | Aid Waiter | Customs | — | — |
| 1879 | G. Oudkerk | Clerk | Audit Office | — | — |
| 1880 | G. Oudkerk | Clerk | Audit Office | — | — |
| 1880 | G. Oudkerk | Aid Waiter | Customs | — | — |
| 1883 | G. Oudkerk | Revenue Clerk | Audit Office | — | — |
| 1886 | G. Oudkerk | Revenue Clerk | Audit Office | — | — |
| 1888 | G. Oudkerk | Revenue Clerk | Audit Office | — | — |
| 1889 | G. Oudkerk | Revenue Clerk | Audit Office | — | — |

### Deterministic checks: `oudekerk_g_e1866` vs `Oudkerk, G. O___British Guiana___1877`

- [PASS] surname_gate: bio 'OUDEKERK' vs stint 'Oudkerk, G. O' (fuzzy:1)
- [PASS] initials: bio ['G'] ~ stint ['G', 'O']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'British Guiana'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1877-1889
- [PASS] position_sim: best 100 vs bar 60: 'Revenue clerk, audit office' ~ 'Clerk'
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

