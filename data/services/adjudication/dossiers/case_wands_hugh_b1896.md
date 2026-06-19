<!-- {"case_id": "case_wands_hugh_b1896", "bio_ids": ["wands_hugh_b1896"], "stint_ids": ["Wands, H___North Borneo___1940"]} -->
# Dossier case_wands_hugh_b1896

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['wands_hugh_b1896'] carry a single initial only — the namesake trap applies.

## Biography `wands_hugh_b1896`

- Printed name: **WANDS, Hugh**
- Birth year: 1896 (attested in editions [1949, 1950, 1951])
- Honours: M.B, M.B.E
- Appears in editions: [1949, 1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1949-L36490.v` — printed in editions [1949, 1950, 1951]:**

> WANDS, Hugh, M.B.E., M.B., Ch.B. (Glas.).—b. 1896; ed. Hamilton Acad. and Glasgow Univ.; on mil. serv., 1918-21, capt.; med. offr. (Chartered Co.'s serv.), N. Borneo, 1936; col. admin. serv., 1946; D.D.M.S., N. Borneo, 1948.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1936 | med. offr. (Chartered Co.'s serv.) | North Borneo | [1949, 1950, 1951] |
| 1 | 1946 | col. admin. serv | North Borneo *(inherited from previous clause)* | [1949, 1950, 1951] |
| 2 | 1948 | D.D.M.S. | North Borneo | [1949, 1950, 1951] |

## Candidate stint `Wands, H___North Borneo___1940`

- Staff-list name: **Wands, H** | colony: **North Borneo** | listed 1940–1951 | editions [1940, 1949, 1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1940 | H. Wands | Medical Officer | Other Officers | — | — |
| 1949 | H. Wands | Medical Officer | MEDICAL | — | — |
| 1950 | H. Wands | Deputy Director | MEDICAL | — | — |
| 1951 | H. Wands | Deputy Director | MEDICAL | — | — |

### Deterministic checks: `wands_hugh_b1896` vs `Wands, H___North Borneo___1940`

- [PASS] surname_gate: bio 'WANDS' vs stint 'Wands, H' (exact)
- [PASS] initials: bio ['H'] ~ stint ['H']
- [PASS] age_gate: stint starts 1940, birth 1896 (age 44)
- [PASS] colony: 3 placed event(s) resolve to 'North Borneo'
- [PASS] tenure_overlap: 3 event tenure(s) overlap stint years 1940-1951
- [FAIL] position_sim: best 48 vs bar 60: 'col. admin. serv' ~ 'Medical Officer'
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

