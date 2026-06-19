<!-- {"case_id": "case_phibbs_james-owen-talbot_b1908", "bio_ids": ["phibbs_james-owen-talbot_b1908"], "stint_ids": ["Phibbs, J. O. T___Northern Rhodesia___1939"]} -->
# Dossier case_phibbs_james-owen-talbot_b1908

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `phibbs_james-owen-talbot_b1908`

- Printed name: **PHIBBS, James Owen Talbot**
- Birth year: 1908 (attested in editions [1948])
- Appears in editions: [1948]

### Verbatim printed entry text (OCR)

**Version `col1948-L35213.v` — printed in editions [1948]:**

> PHIBBS, James Owen Talbot.—b. 1908; ed. Haileybury Coll., Trinity Coll., Dublin, Jesus Coll., Cambridge, B.A. (Cantab.), B.Comm. (Dub.), LL.B. (Dub.); cadet, N. Rhod., 1930; dist. offr., 1932.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1930 | cadet | Northern Rhodesia | [1948] |
| 1 | 1932 | dist. offr | Northern Rhodesia *(inherited from previous clause)* | [1948] |

## Candidate stint `Phibbs, J. O. T___Northern Rhodesia___1939`

- Staff-list name: **Phibbs, J. O. T** | colony: **Northern Rhodesia** | listed 1939–1940 | editions [1939, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1939 | J. O. T. Phibbs | District Officer | District Administration | — | — |
| 1940 | J. O. T. Phibbs | District Officer | District Administration | — | — |

### Deterministic checks: `phibbs_james-owen-talbot_b1908` vs `Phibbs, J. O. T___Northern Rhodesia___1939`

- [PASS] surname_gate: bio 'PHIBBS' vs stint 'Phibbs, J. O. T' (exact)
- [PASS] initials: bio ['J', 'O', 'T'] ~ stint ['J', 'O', 'T']
- [PASS] age_gate: stint starts 1939, birth 1908 (age 31)
- [PASS] colony: 2 placed event(s) resolve to 'Northern Rhodesia'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1939-1940
- [PASS] position_sim: best 72 vs bar 60: 'dist. offr' ~ 'District Officer'
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

