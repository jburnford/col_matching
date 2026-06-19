<!-- {"case_id": "case_soulsby_hugh-graham_b1904", "bio_ids": ["soulsby_hugh-graham_b1904"], "stint_ids": ["Soulsby, H. G___Uganda___1936"]} -->
# Dossier case_soulsby_hugh-graham_b1904

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `soulsby_hugh-graham_b1904`

- Printed name: **SOULSBY, Hugh Graham**
- Birth year: 1904 (attested in editions [1948, 1949, 1950])
- Appears in editions: [1948, 1949, 1950]

### Verbatim printed entry text (OCR)

**Version `col1948-L36047.v` — printed in editions [1948, 1949, 1950]:**

> SOULSBY, Hugh Graham, D.Ph. (Hopkins).—b. 1904; ed. King’s Coll., Newcastle-on-Tyne, Peterhouse, Cambridge, and Johns Hopkins, Baltimore; asst. dist. offr., Uga., 1933; seconded to secretariat, 1944; dist. offr. and ag. fin. sec.; compiled Uga. estimates 1946–47–48; author of The Right of Search and the Slave Trade, 1933.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1933–1933 | asst. dist. offr. | Uganda | [1948, 1949, 1950] |
| 1 | 1944–1944 | seconded to secretariat | — | [1948, 1949, 1950] |
| 2 | 1946–1948 | compiled Uga. estimates | Uganda | [1948, 1949, 1950] |

## Candidate stint `Soulsby, H. G___Uganda___1936`

- Staff-list name: **Soulsby, H. G** | colony: **Uganda** | listed 1936–1951 | editions [1936, 1937, 1940, 1949, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1936 | H. G. Soulsby | Cadet | Civil Establishment | — | — |
| 1937 | H. G. Soulsby | District Officers and Assistant District Officers | Provincial Administration | — | — |
| 1940 | H. G. Soulsby | District Officers and Assistant District Officers | Provincial Administration | — | — |
| 1949 | H. G. Soulsby | Secretaries (Seconded from the Provincial Administration) | Secretariat | — | — |
| 1949 | H. G. Soulsby | District Officers and Assistant District Officers | Provincial Administration | — | — |
| 1951 | H. G. Soulsby | District Officers and Assistant District Officers | Provincial Administration | — | — |
| 1951 | H. G. Soulsby | Secretaries (Seconded from the Provincial Administration) | Secretariat | — | — |

### Deterministic checks: `soulsby_hugh-graham_b1904` vs `Soulsby, H. G___Uganda___1936`

- [PASS] surname_gate: bio 'SOULSBY' vs stint 'Soulsby, H. G' (exact)
- [PASS] initials: bio ['H', 'G'] ~ stint ['H', 'G']
- [PASS] age_gate: stint starts 1936, birth 1904 (age 32)
- [PASS] colony: 2 placed event(s) resolve to 'Uganda'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1936-1951
- [FAIL] position_sim: best 36 vs bar 60: 'compiled Uga. estimates' ~ 'Secretaries (Seconded from the Provincial Administration)'
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

