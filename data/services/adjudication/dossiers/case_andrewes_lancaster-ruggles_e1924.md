<!-- {"case_id": "case_andrewes_lancaster-ruggles_e1924", "bio_ids": ["andrewes_lancaster-ruggles_e1924"], "stint_ids": ["Andrewes, L. R___Hong Kong___1949"]} -->
# Dossier case_andrewes_lancaster-ruggles_e1924

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Andrewes, L. R___Hong Kong___1949` is also gate-compatible with biography(ies) outside this case: ['andrewes_lancelot-ruggles_b1897'] (already linked elsewhere or filtered).

## Biography `andrewes_lancaster-ruggles_e1924`

- Printed name: **ANDREWES, LANCASTER RUGGLES**
- Birth year: not printed
- Appears in editions: [1939, 1940]

### Verbatim printed entry text (OCR)

**Version `col1939-L64319.v` — printed in editions [1939, 1940]:**

> ANDREWES, LANCASTER RUGGLES.—Ed. Fort Street, Sydney; war serv., 1915-18; admitted solr., sup. ct., London, 1924; asst. crown solr., Hong Kong, 1928; J.P., 1931; ag. dep. regar. in 1932-35; dep. regar., sup. ct., 1935; ag. regar., sup. ct., offl. admistr., offl. trustee and regar., coys. in 1937; offl. recvr. and regar., trade mark and patents, Oct., 1937.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1924 | admitted solr., sup. ct., London | — | [1939, 1940] |
| 1 | 1928 | asst. crown solr. | Hong Kong | [1939, 1940] |
| 2 | 1931 | J.P | Hong Kong *(inherited from previous clause)* | [1939, 1940] |
| 3 | 1932–1935 | ag. dep. regar. in | Hong Kong *(inherited from previous clause)* | [1939, 1940] |
| 4 | 1935 | dep. regar., sup. ct | Hong Kong *(inherited from previous clause)* | [1939, 1940] |
| 5 | 1937 | ag. regar., sup. ct., offl. admistr., offl. trustee and regar., coys. in | Hong Kong *(inherited from previous clause)* | [1939, 1940] |

## Candidate stint `Andrewes, L. R___Hong Kong___1949`

- Staff-list name: **Andrewes, L. R** | colony: **Hong Kong** | listed 1949–1951 | editions [1949, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | L. R. Andrewes | Crown Solicitor | Legal | — | — |
| 1951 | L. R. Andrewes | Crown Solicitor | Legal | — | — |

### Deterministic checks: `andrewes_lancaster-ruggles_e1924` vs `Andrewes, L. R___Hong Kong___1949`

- [PASS] surname_gate: bio 'ANDREWES' vs stint 'Andrewes, L. R' (exact)
- [PASS] initials: bio ['L', 'R'] ~ stint ['L', 'R']
- [PASS] age_gate: stint starts 1949; no printed birth year — UNCHECKED
- [PASS] colony: 5 placed event(s) resolve to 'Hong Kong'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1949-1951
- [FAIL] position_sim: best 25 vs bar 60: 'ag. regar., sup. ct., offl. admistr., offl. trustee and regar., coys. in' ~ 'Crown Solicitor'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: ALL supporting events inherit their place from an earlier clause — weak evidence

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

