<!-- {"case_id": "case_eastwood_benjamin_e1877", "bio_ids": ["eastwood_benjamin_e1877"], "stint_ids": ["Eastwood, B___Kenya___1907"]} -->
# Dossier case_eastwood_benjamin_e1877

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 4 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['eastwood_benjamin_e1877'] carry a single initial only — the namesake trap applies.

## Biography `eastwood_benjamin_e1877`

- Printed name: **EASTWOOD, BENJAMIN**
- Birth year: not printed
- Honours: C.M.G (1918)
- Terminal: retired 1918 — “retired, 1918.”
- Appears in editions: [1908, 1909, 1910, 1911, 1914, 1915, 1917, 1918, 1919, 1920, 1921]

### Verbatim printed entry text (OCR)

**Version `col1917-L49302.v` — printed in editions [1917, 1918, 1919, 1920, 1921]:**

> EASTWOOD, BENJAMIN, C.M.G. (1918).—Ed. at Fleetwood with John Aird & Sons (now Sir John Aird & Co.) from 1877; chief acctnt., Uganda rly., 1897; gen. man., Uganda rly., Jan., 1915; mem. exec. and legis. couns., 1915; retired, 1918.

**Version `col1908-L44274.v` — printed in editions [1908, 1909, 1910, 1911, 1914, 1915]:**

> EASTWOOD, BENJAMIN.—Ed. at Fleetwood; with John Aird & Sons (now Sir John Aird & Co.) from 1877; chief accntn., Uganda rly., 1897.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1877 | with John Aird & Sons (now Sir John Aird & Co.) from | — | [1908, 1909, 1910, 1911, 1914, 1915] |
| 1 | 1897 | chief acctnt., Uganda rly | Uganda | [1908, 1909, 1910, 1911, 1914, 1915, 1917, 1918, 1919, 1920, 1921] |
| 2 | 1915 | gen. man., Uganda rly | Uganda | [1917, 1918, 1919, 1920, 1921] |

## Candidate stint `Eastwood, B___Kenya___1907`

- Staff-list name: **Eastwood, B** | colony: **Kenya** | listed 1907–1918 | editions [1907, 1908, 1909, 1910, 1911, 1912, 1913, 1914, 1915, 1917, 1918]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1907 | B. Eastwood | Chief Accountant | Uganda Railway | — | — |
| 1908 | B. Eastwood | Chief Accountant, Uganda Railway | Civil Establishment | — | — |
| 1909 | B. Eastwood | Chief Accountant | Railway | — | — |
| 1910 | B. Eastwood | Chief Accountant | Accounts | — | — |
| 1911 | B. Eastwood | Chief Accountant | Accounts | — | — |
| 1912 | B. Eastwood | Chief Accountant | Accounts | — | — |
| 1913 | B. Eastwood | Chief Accountant | Railway | — | — |
| 1914 | B. Eastwood | Chief Accountant | Accounts | — | — |
| 1915 | B. Eastwood | Chief Accountant | Accounts | — | — |
| 1917 | B. Eastwood | General Manager | Railway | — | — |
| 1918 | B. Eastwood | General Manager | Railway | — | — |

### Deterministic checks: `eastwood_benjamin_e1877` vs `Eastwood, B___Kenya___1907`

- [PASS] surname_gate: bio 'EASTWOOD' vs stint 'Eastwood, B' (exact)
- [PASS] initials: bio ['B'] ~ stint ['B']
- [PASS] age_gate: stint starts 1907; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Kenya'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1907-1918
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

