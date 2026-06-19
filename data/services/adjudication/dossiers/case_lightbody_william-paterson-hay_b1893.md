<!-- {"case_id": "case_lightbody_william-paterson-hay_b1893", "bio_ids": ["lightbody_william-paterson-hay_b1893"], "stint_ids": ["Lightbody, W. P. H___Palestine___1921"]} -->
# Dossier case_lightbody_william-paterson-hay_b1893

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 7 official(s) with this surname in the graph's staff lists; 6 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Lightbody, W. P. H___Palestine___1921` is also gate-compatible with biography(ies) outside this case: ['lightbody_william-patterson-hay_e1920'] (already linked elsewhere or filtered).

## Biography `lightbody_william-paterson-hay_b1893`

- Printed name: **LIGHTBODY, William Paterson Hay**
- Birth year: 1893 (attested in editions [1948])
- Honours: C.B.E
- Appears in editions: [1948]

### Verbatim printed entry text (OCR)

**Version `col1948-L34051.v` — printed in editions [1948]:**

> LIGHTBODY, William Paterson Hay, C.B.E., L.R.C.S. (Edin.), L.R.C.P. (Edin.), L.R.F.P. & S. (Glasg.), D.T.M. & H. (Cantab.), D.P.H. (Glasg.).—b. 1893 ; ed. Glasgow Acad., High Sch. and Univ. and Extra Mural Schs. ; on mil. serv. 1916-20, capt. ; S.M.O., Pal., 1920 ; asst. D.M.S. (health), S.L., 1937 ; D.M.S., 1938.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1920 | S.M.O. | Palestine | [1948] |
| 1 | 1937 | asst. D.M.S. (health) | Sierra Leone | [1948] |
| 2 | 1938 | D.M.S | Sierra Leone *(inherited from previous clause)* | [1948] |

## Candidate stint `Lightbody, W. P. H___Palestine___1921`

- Staff-list name: **Lightbody, W. P. H** | colony: **Palestine** | listed 1921–1932 | editions [1921, 1923, 1925, 1927, 1928, 1929, 1930, 1931, 1932]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1921 | W. P. H. Lightbody | Principal Medical Officer | Phoenicia District | — | — |
| 1923 | W. P. Lightbody | Principal Medical Officer | DEPARTMENT OF HEALTH | — | — |
| 1925 | W. P. H. Lightbody | Senior Medical Officer | Department of Health | — | — |
| 1927 | W. P. H. Lightbody | Senior Medical Officer | Department of Health | — | — |
| 1928 | W. P. H. Lightbody | Senior Medical Officer | Department of Health | — | — |
| 1929 | W. P. H. Lightbody | Senior Medical Officers | Department of Health | — | — |
| 1930 | W. P. H. Lightbody | Senior Medical Officers | Department of Health | — | — |
| 1931 | W. P. H. Lightbody | Senior Medical Officers | Department of Health | — | — |
| 1932 | W. P. H. Lightbody | Senior Medical Officers | Department of Health | — | — |

### Deterministic checks: `lightbody_william-paterson-hay_b1893` vs `Lightbody, W. P. H___Palestine___1921`

- [PASS] surname_gate: bio 'LIGHTBODY' vs stint 'Lightbody, W. P. H' (exact)
- [PASS] initials: bio ['W', 'P', 'H'] ~ stint ['W', 'P', 'H']
- [PASS] age_gate: stint starts 1921, birth 1893 (age 28)
- [PASS] colony: 1 placed event(s) resolve to 'Palestine'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1921-1932
- [FAIL] position_sim: best 16 vs bar 60: 'S.M.O.' ~ 'Senior Medical Officer'
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

