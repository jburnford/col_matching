<!-- {"case_id": "case_strathairen_george-cecil_e1901", "bio_ids": ["strathairen_george-cecil_e1901"], "stint_ids": ["Strathairn, G. C___Uganda___1906", "Strathairn, G. C___Uganda___1918"]} -->
# Dossier case_strathairen_george-cecil_e1901

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 4 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- Phase 1 found `strathairen_george-cecil_e1901` ↔ `Strathairn, G. C___Uganda___1906` passed its evidence bar but dropped it as ambiguous (a comparable-strength competitor existed).
- NOTE: stint `Strathairn, G. C___Uganda___1906` is also gate-compatible with biography(ies) outside this case: ['strathairn_george-cecil_e1901'] (already linked elsewhere or filtered).
- Phase 1 found `strathairen_george-cecil_e1901` ↔ `Strathairn, G. C___Uganda___1918` passed its evidence bar but dropped it as ambiguous (a comparable-strength competitor existed).
- NOTE: stint `Strathairn, G. C___Uganda___1918` is also gate-compatible with biography(ies) outside this case: ['strathairn_george-cecil_e1901'] (already linked elsewhere or filtered).

## Biography `strathairen_george-cecil_e1901`

- Printed name: **STRATHAIREN, GEORGE CECIL**
- Birth year: not printed
- Honours: M.B
- Appears in editions: [1925]

### Verbatim printed entry text (OCR)

**Version `col1925-L59679.v` — printed in editions [1925]:**

> STRATHAIREN, GEORGE CECIL, M.B., Ch.B. (Edin.).—D.P.H.; certif. from London S.T.M.—Med. offr., Orange River Colony Burgher Camps, 1901-03; med. offr., E. Africa and Uganda Prots., 1903; senr. med. offr., Uganda, 1914; war serv. with rank of major, 1914-18; ch. med. offr., Fiji, 1920; mem., leg. couns., Fiji, 1920-22; senr. sanv. med. offr., Jamaica, 1922.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1901–1903 | certif. from London S.T.M.—Med. offr., Orange River Colony Burgher Camps | Orange River Colony | [1925] |
| 1 | 1903 | med. offr., E. Africa and Uganda Prots | Orange River Colony *(inherited from previous clause)* | [1925] |
| 2 | 1914 | senr. med. offr. | Uganda | [1925] |
| 3 | 1920 | ch. med. offr. | Fiji | [1925] |
| 4 | 1922 | senr. sanv. med. offr. | Jamaica | [1925] |

## Candidate stint `Strathairn, G. C___Uganda___1906`

- Staff-list name: **Strathairn, G. C** | colony: **Uganda** | listed 1906–1913 | editions [1906, 1907, 1910, 1911, 1912, 1913]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1906 | G. C. Strathairn | Medical Officers | Medical | — | — |
| 1907 | G. C. Strathairn | Medical Officer | Medical | — | — |
| 1910 | G. C. Strathairn | Medical Officer | Medical | — | — |
| 1911 | G. C. Strathairn | Medical Officer | Medical | — | — |
| 1912 | G. C. Strathairn | Medical Officer | Medical | — | — |
| 1913 | G. C. Strathairn | Medical Officer | Medical | — | — |

### Deterministic checks: `strathairen_george-cecil_e1901` vs `Strathairn, G. C___Uganda___1906`

- [PASS] surname_gate: bio 'STRATHAIREN' vs stint 'Strathairn, G. C' (fuzzy:1)
- [PASS] initials: bio ['G', 'C'] ~ stint ['G', 'C']
- [PASS] age_gate: stint starts 1906; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Uganda'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1906-1913
- [PASS] position_sim: best 64 vs bar 60: 'senr. med. offr.' ~ 'Medical Officer'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

## Candidate stint `Strathairn, G. C___Uganda___1918`

- Staff-list name: **Strathairn, G. C** | colony: **Uganda** | listed 1918–1919 | editions [1918, 1919]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1918 | G. C. Strathairn | Senior Medical Officer | Medical | — | — |
| 1919 | G. C. Strathairn | Senior Medical Officer | Medical | — | — |

### Deterministic checks: `strathairen_george-cecil_e1901` vs `Strathairn, G. C___Uganda___1918`

- [PASS] surname_gate: bio 'STRATHAIREN' vs stint 'Strathairn, G. C' (fuzzy:1)
- [PASS] initials: bio ['G', 'C'] ~ stint ['G', 'C']
- [PASS] age_gate: stint starts 1918; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Uganda'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1918-1919
- [PASS] position_sim: best 74 vs bar 60: 'senr. med. offr.' ~ 'Senior Medical Officer'
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

