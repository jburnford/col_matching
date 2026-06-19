<!-- {"case_id": "case_stubbs_james-nelson-stubbs_e1889", "bio_ids": ["stubbs_james-nelson-stubbs_e1889"], "stint_ids": ["Stubbs, J. N___Palestine___1921"]} -->
# Dossier case_stubbs_james-nelson-stubbs_e1889

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 16 official(s) with this surname in the graph's staff lists; 9 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `stubbs_james-nelson-stubbs_e1889`

- Printed name: **STUBBS, James Nelson Stubbs**
- Birth year: not printed
- Appears in editions: [1948, 1949]

### Verbatim printed entry text (OCR)

**Version `col1948-L36216.v` — printed in editions [1948, 1949]:**

> STUBBS, James Nelson Stubbs, M.C.—1889; ed. Napen High Sch. and Auckland Univ., New Zealand; on mil. serv. 1915–20; capt.; asst. contrl. of land registries, Pal., 1920; dir. of land registration.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1889 | — | — | [1948, 1949] |
| 1 | 1920 | asst. contrl. of land registries | Palestine | [1948, 1949] |

## Candidate stint `Stubbs, J. N___Palestine___1921`

- Staff-list name: **Stubbs, J. N** | colony: **Palestine** | listed 1921–1940 | editions [1921, 1923, 1925, 1927, 1928, 1929, 1930, 1931, 1932, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1921 | J. N. Stubbs | Assistant Controller | Land Registration | — | — |
| 1923 | J. N. Stubbs | Director | Lands | — | — |
| 1925 | J. N. Stubbs | Director | Department of Lands | — | — |
| 1927 | J. N. Stubbs | Director | Department of Lands | — | — |
| 1928 | J. N. Stubbs | Director | Department of Lands | — | — |
| 1929 | J. N. Stubbs | Director | Department of Lands | — | — |
| 1930 | J. N. Stubbs | Director | Department of Lands | — | — |
| 1931 | J. N. Stubbs | Director | Department of Lands | — | — |
| 1932 | J. N. Stubbs | Director | Department of Lands | — | — |
| 1940 | J. N. Stubbs | Director | Land Registration | — | — |

### Deterministic checks: `stubbs_james-nelson-stubbs_e1889` vs `Stubbs, J. N___Palestine___1921`

- [PASS] surname_gate: bio 'STUBBS' vs stint 'Stubbs, J. N' (exact)
- [PASS] initials: bio ['J', 'N', 'S'] ~ stint ['J', 'N']
- [PASS] age_gate: stint starts 1921; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Palestine'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1921-1940
- [FAIL] position_sim: best 56 vs bar 60: 'asst. contrl. of land registries' ~ 'Assistant Controller'
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

