<!-- {"case_id": "case_unger_charles-john-alexander_b1910", "bio_ids": ["unger_charles-john-alexander_b1910"], "stint_ids": ["Unger, C. J. A___Northern Rhodesia___1949"]} -->
# Dossier case_unger_charles-john-alexander_b1910

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `unger_charles-john-alexander_b1910`

- Printed name: **UNGER, Charles John Alexander**
- Birth year: 1910 (attested in editions [1951])
- Appears in editions: [1951]

### Verbatim printed entry text (OCR)

**Version `col1951-L43360.v` — printed in editions [1951]:**

> UNGER, Charles John Alexander, B.Sc. (S.A.)—b. 1910; ed. Bishops (S.A.) Rhodes Univ. Coll. (S.A.) and Cambridge, educ. cert.; on mil. serv., 1940-44; lieut.; mstr., European educ. dept., N. Rhod., 1936.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1936 | mstr., European educ. dept. | Northern Rhodesia | [1951] |

## Candidate stint `Unger, C. J. A___Northern Rhodesia___1949`

- Staff-list name: **Unger, C. J. A** | colony: **Northern Rhodesia** | listed 1949–1951 | editions [1949, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | C. J. A. Unger | Master | Education | — | — |
| 1951 | C. J. A. Unger | Master | Education | — | — |

### Deterministic checks: `unger_charles-john-alexander_b1910` vs `Unger, C. J. A___Northern Rhodesia___1949`

- [PASS] surname_gate: bio 'UNGER' vs stint 'Unger, C. J. A' (exact)
- [PASS] initials: bio ['C', 'J', 'A'] ~ stint ['C', 'J', 'A']
- [PASS] age_gate: stint starts 1949, birth 1910 (age 39)
- [PASS] colony: 1 placed event(s) resolve to 'Northern Rhodesia'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1949-1951
- [FAIL] position_sim: best 28 vs bar 60: 'mstr., European educ. dept.' ~ 'Master'
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

