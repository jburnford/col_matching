<!-- {"case_id": "case_kesselli_alfred-colenso_e1902", "bio_ids": ["kesselli_alfred-colenso_e1902"], "stint_ids": ["Kessell, A. C___Western Australia___1907", "Kessell, A. Colenso___Australia___1912"]} -->
# Dossier case_kesselli_alfred-colenso_e1902

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- Phase 1 found `kesselli_alfred-colenso_e1902` ↔ `Kessell, A. C___Western Australia___1907` passed its evidence bar but dropped it as ambiguous (a comparable-strength competitor existed).
- NOTE: stint `Kessell, A. C___Western Australia___1907` is also gate-compatible with biography(ies) outside this case: ['kessell_alfred-colenso_e1902'] (already linked elsewhere or filtered).
- NOTE: stint `Kessell, A. Colenso___Australia___1912` is also gate-compatible with biography(ies) outside this case: ['kessell_alfred-colenso_e1902'] (already linked elsewhere or filtered).

## Biography `kesselli_alfred-colenso_e1902`

- Printed name: **KESSELLI, Alfred Colenso**
- Birth year: not printed
- Appears in editions: [1920]

### Verbatim printed entry text (OCR)

**Version `col1920-L54876.v` — printed in editions [1920]:**

> KESSELLI, Alfred Colenso, F.R.G.S., J.P.—Fell. Inst. of Commerce, Lond.; Fell. of Nat. Shorthand Assoc.; Fell. R. Col. Inst.; conf. shorthand writer to commr. of rlyws., W. Australia, 1902; apptd. sec. to premier of W. Australia, 1903, and served in this capacity during six successive administrations; sec. to Sir Newton Moore, premier of W. Australia, on the occasion of his visit to England, 1910; sec. to Hon. J. Scaddan, premier of W. Australia, on the occasion of his visit to England, 1913; sec. to agent-general for W. Australia, London, 1914-1919.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1902–1902 | conf. shorthand writer to commr. of rlyws. | Western Australia | [1920] |
| 1 | 1903 | apptd. sec. to premier | Western Australia | [1920] |
| 2 | 1910–1910 | sec. to Sir Newton Moore, premier | Western Australia | [1920] |
| 3 | 1913–1913 | sec. to Hon. J. Scaddan, premier | Western Australia | [1920] |
| 4 | 1914–1919 | sec. to agent-general | Western Australia | [1920] |

## Candidate stint `Kessell, A. C___Western Australia___1907`

- Staff-list name: **Kessell, A. C** | colony: **Western Australia** | listed 1907–1917 | editions [1907, 1908, 1909, 1917]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1907 | A. C. Kessell | Secretary to Premier | Premier's Office | — | — |
| 1908 | A. C. Kessell | Secretary to Premier | Premier's Office | — | — |
| 1909 | A. C. Kessell | Secretary to Premier | Premier's Office | — | — |
| 1917 | A. C. Kessell | Secretary | London Agency | — | — |

### Deterministic checks: `kesselli_alfred-colenso_e1902` vs `Kessell, A. C___Western Australia___1907`

- [PASS] surname_gate: bio 'KESSELLI' vs stint 'Kessell, A. C' (fuzzy:1)
- [PASS] initials: bio ['A', 'C'] ~ stint ['A', 'C']
- [PASS] age_gate: stint starts 1907; no printed birth year — UNCHECKED
- [PASS] colony: 5 placed event(s) resolve to 'Western Australia'
- [PASS] tenure_overlap: 4 event tenure(s) overlap stint years 1907-1917
- [PASS] position_sim: best 70 vs bar 60: 'apptd. sec. to premier' ~ 'Secretary to Premier'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

## Candidate stint `Kessell, A. Colenso___Australia___1912`

- Staff-list name: **Kessell, A. Colenso** | colony: **Australia** | listed 1912–1913 | editions [1912, 1913]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1912 | A. C. Kessell | Secretary to Premier | Premier's Office | — | — |
| 1913 | A. Colenso Kessell | Secretary to Premier | Premier's Office | — | — |

### Deterministic checks: `kesselli_alfred-colenso_e1902` vs `Kessell, A. Colenso___Australia___1912`

- [PASS] surname_gate: bio 'KESSELLI' vs stint 'Kessell, A. Colenso' (fuzzy:1)
- [PASS] initials: bio ['A', 'C'] ~ stint ['A', 'C']
- [PASS] age_gate: stint starts 1912; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Australia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1912-1913
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

