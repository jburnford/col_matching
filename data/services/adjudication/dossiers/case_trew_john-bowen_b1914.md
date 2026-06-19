<!-- {"case_id": "case_trew_john-bowen_b1914", "bio_ids": ["trew_john-bowen_b1914"], "stint_ids": ["Trew, J. B___Northern Rhodesia___1949"]} -->
# Dossier case_trew_john-bowen_b1914

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `trew_john-bowen_b1914`

- Printed name: **TREW, John Bowen**
- Birth year: 1914 (attested in editions [1951])
- Appears in editions: [1951]

### Verbatim printed entry text (OCR)

**Version `col1951-L43269.v` — printed in editions [1951]:**

> TREW, John Bowen, B.A. (Natal).—b. 1914; ed. Pietermaritzburg Coll. and Natal Univ., teach dip.; asst. mstr., European educ.-dept., N. Rhod., 1938.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1938 | asst. mstr., European educ.-dept. | Northern Rhodesia | [1951] |

## Candidate stint `Trew, J. B___Northern Rhodesia___1949`

- Staff-list name: **Trew, J. B** | colony: **Northern Rhodesia** | listed 1949–1951 | editions [1949, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | J. B. Trew | Master | Education | — | — |
| 1951 | J. B. Trew | Master | Education | — | — |

### Deterministic checks: `trew_john-bowen_b1914` vs `Trew, J. B___Northern Rhodesia___1949`

- [PASS] surname_gate: bio 'TREW' vs stint 'Trew, J. B' (exact)
- [PASS] initials: bio ['J', 'B'] ~ stint ['J', 'B']
- [PASS] age_gate: stint starts 1949, birth 1914 (age 35)
- [PASS] colony: 1 placed event(s) resolve to 'Northern Rhodesia'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1949-1951
- [FAIL] position_sim: best 30 vs bar 60: 'asst. mstr., European educ.-dept.' ~ 'Master'
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

