<!-- {"case_id": "case_kent_r-g_e1891-2", "bio_ids": ["kent_r-g_e1891-2"], "stint_ids": ["Kent, R. G___Victoria___1880", "Kent, R. G___Victoria___1889"]} -->
# Dossier case_kent_r-g_e1891-2

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 12 official(s) with this surname in the graph's staff lists; 7 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Kent, R. G___Victoria___1880` is also gate-compatible with biography(ies) outside this case: ['kent_r-g_e1891'] (already linked elsewhere or filtered).
- NOTE: stint `Kent, R. G___Victoria___1889` is also gate-compatible with biography(ies) outside this case: ['kent_r-g_e1891'] (already linked elsewhere or filtered).

## Biography `kent_r-g_e1891-2`

- Printed name: **KENT, R. G**
- Birth year: not printed
- Appears in editions: [1898, 1899, 1900, 1905, 1906, 1907, 1908, 1909, 1910, 1911, 1912, 1913, 1914, 1915]

### Verbatim printed entry text (OCR)

**Version `col1898-L34223.v` — printed in editions [1898, 1899, 1900, 1905, 1906, 1907, 1908, 1909, 1910, 1911, 1912, 1913, 1914, 1915]:**

> KENT, R. G.—Acctnt., rly. dept., Victoria, 1891.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1891 | Acctnt., rly. dept. | Victoria | [1898, 1899, 1900, 1905, 1906, 1907, 1908, 1909, 1910, 1911, 1912, 1913, 1914, 1915] |

## Candidate stint `Kent, R. G___Victoria___1880`

- Staff-list name: **Kent, R. G** | colony: **Victoria** | listed 1880–1883 | editions [1880, 1883]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1880 | R. G. Kent | Sub-Accountant | Victorian Railways | — | — |
| 1883 | R. G. Kent | Sub-Accountant | Victorian Railways | — | — |

### Deterministic checks: `kent_r-g_e1891-2` vs `Kent, R. G___Victoria___1880`

- [PASS] surname_gate: bio 'KENT' vs stint 'Kent, R. G' (exact)
- [PASS] initials: bio ['R', 'G'] ~ stint ['R', 'G']
- [PASS] age_gate: stint starts 1880; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Victoria'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1880-1883
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Kent, R. G___Victoria___1889`

- Staff-list name: **Kent, R. G** | colony: **Victoria** | listed 1889–1900 | editions [1889, 1894, 1897, 1898, 1899, 1900]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1889 | R. G. Kent | Acting Accountant | Railways Division | — | — |
| 1894 | R. G. Kent | Secretary | VICTORIAN RAILWAYS | — | — |
| 1897 | R. G. Kent | Secretary | Victorian Railways | — | — |
| 1898 | R. G. Kent | Secretary | Victorian Railways | — | — |
| 1899 | R. G. Kent | Secretary | VICTORIAN RAILWAYS | — | — |
| 1900 | R. G. Kent | Secretary | Victorian Railways | — | — |

### Deterministic checks: `kent_r-g_e1891-2` vs `Kent, R. G___Victoria___1889`

- [PASS] surname_gate: bio 'KENT' vs stint 'Kent, R. G' (exact)
- [PASS] initials: bio ['R', 'G'] ~ stint ['R', 'G']
- [PASS] age_gate: stint starts 1889; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Victoria'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1889-1900
- [FAIL] position_sim: best 50 vs bar 60: 'Acctnt., rly. dept.' ~ 'Acting Accountant'
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

