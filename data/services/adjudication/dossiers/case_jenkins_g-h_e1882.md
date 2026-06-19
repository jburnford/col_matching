<!-- {"case_id": "case_jenkins_g-h_e1882", "bio_ids": ["jenkins_g-h_e1882"], "stint_ids": ["Jenkins, G. H___Victoria___1894"]} -->
# Dossier case_jenkins_g-h_e1882

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 39 official(s) with this surname in the graph's staff lists; 20 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Jenkins, G. H___Victoria___1894` is also gate-compatible with biography(ies) outside this case: ['jenkins_george-henry_b1843'] (already linked elsewhere or filtered).

## Biography `jenkins_g-h_e1882`

- Printed name: **JENKINS, G. H**
- Birth year: not printed
- Appears in editions: [1886]

### Verbatim printed entry text (OCR)

**Version `col1886-L34209.v` — printed in editions [1886]:**

> JENKINS, G. H.—Clerk of the legislative assembly, Victoria, 1 April, 1882.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1882 | Clerk of the legislative assembly | Victoria | [1886] |

## Candidate stint `Jenkins, G. H___Victoria___1894`

- Staff-list name: **Jenkins, G. H** | colony: **Victoria** | listed 1894–1900 | editions [1894, 1897, 1898, 1899, 1900]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1894 | G. H. Jenkins | Clerk of the Council and Clerk of Parliaments | Legislative Council | C.M.G. | — |
| 1897 | G. H. Jenkins, C.M.G. | Clerk of the Council and Clerk of Parliaments | Legislative Council | C.M.G. | — |
| 1898 | G. H. Jenkins | Clerk of the Council and Clerk of Parliaments | Legislative Council | C.M.G. | — |
| 1899 | G. H. Jenkins | Clerk of the Council and Clerk of Parliaments | Legislative Council | C.M.G. | — |
| 1900 | G. H. Jenkins | Clerk of the Council and Clerk of Parliaments | Legislative Council | C.M.G. | — |

### Deterministic checks: `jenkins_g-h_e1882` vs `Jenkins, G. H___Victoria___1894`

- [PASS] surname_gate: bio 'JENKINS' vs stint 'Jenkins, G. H' (exact)
- [PASS] initials: bio ['G', 'H'] ~ stint ['G', 'H']
- [PASS] age_gate: stint starts 1894; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Victoria'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1894-1900
- [FAIL] position_sim: best 58 vs bar 60: 'Clerk of the legislative assembly' ~ 'Clerk of the Council and Clerk of Parliaments'
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

