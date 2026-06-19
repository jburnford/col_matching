<!-- {"case_id": "case_fox_s-a_b1917", "bio_ids": ["fox_s-a_b1917"], "stint_ids": ["Fox, S. A___Northern Rhodesia___1949"]} -->
# Dossier case_fox_s-a_b1917

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 43 official(s) with this surname in the graph's staff lists; 18 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `fox_s-a_b1917`

- Printed name: **FOX, S. A**
- Birth year: 1917 (attested in editions [1956, 1957, 1958, 1959, 1960, 1961, 1962])
- Appears in editions: [1956, 1957, 1958, 1959, 1960, 1961, 1962]

### Verbatim printed entry text (OCR)

**Version `col1956-L21204.v` — printed in editions [1956, 1957, 1958, 1959, 1960, 1961, 1962]:**

> FOX, S. A.—b. 1917; ed. Lancing Coll. and Worcester Coll., Oxford; mil. serv., 1941-45, sqdn. idr.; cadet, G.C., 1939; asst. dist. offr., 1941; dist. offr., N. Rhod., 1946; admin. offr., N. Nig., 1956.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1939 | cadet | Gold Coast | [1956, 1957, 1958, 1959, 1960, 1961, 1962] |
| 1 | 1941 | asst. dist. offr | Gold Coast *(inherited from previous clause)* | [1956, 1957, 1958, 1959, 1960, 1961, 1962] |
| 2 | 1946 | dist. offr. | Northern Rhodesia | [1956, 1957, 1958, 1959, 1960, 1961, 1962] |
| 3 | 1956 | admin. offr. | Northern Nigeria | [1956, 1957, 1958, 1959, 1960, 1961, 1962] |

## Candidate stint `Fox, S. A___Northern Rhodesia___1949`

- Staff-list name: **Fox, S. A** | colony: **Northern Rhodesia** | listed 1949–1951 | editions [1949, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | S. A. Fox | Assistant Secretaries (Section Officers) | Secretariat | — | — |
| 1951 | S. A. Fox | Section Officers (seconded) | Secretariat | — | — |

### Deterministic checks: `fox_s-a_b1917` vs `Fox, S. A___Northern Rhodesia___1949`

- [PASS] surname_gate: bio 'FOX' vs stint 'Fox, S. A' (exact)
- [PASS] initials: bio ['S', 'A'] ~ stint ['S', 'A']
- [PASS] age_gate: stint starts 1949, birth 1917 (age 32)
- [PASS] colony: 1 placed event(s) resolve to 'Northern Rhodesia'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1949-1951
- [FAIL] position_sim: best 34 vs bar 60: 'dist. offr.' ~ 'Assistant Secretaries (Section Officers)'
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

