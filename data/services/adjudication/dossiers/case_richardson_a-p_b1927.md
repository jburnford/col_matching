<!-- {"case_id": "case_richardson_a-p_b1927", "bio_ids": ["richardson_a-p_b1927"], "stint_ids": ["Richardson, A. P___Hong Kong___1950"]} -->
# Dossier case_richardson_a-p_b1927

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 76 official(s) with this surname in the graph's staff lists; 30 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `richardson_a-p_b1927`

- Printed name: **RICHARDSON, A. P**
- Birth year: 1927 (attested in editions [1962, 1963, 1964, 1965, 1966])
- Appears in editions: [1961, 1962, 1963, 1964, 1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1962-L25793.v` — printed in editions [1962, 1963, 1964, 1965, 1966]:**

> RICHARDSON, A. P.—b. 1927; ed. St. Andrew's Coll. and Trinity Coll., Dublin; cadet, H.K., asst. sec. for Chinese affrs., 1950; lab. offr., 1952; D.O., 1955; estab. offr., 1957; redesign. admin. offr., 1959; ag. chief asst. sec. for Chinese affrs., 1959; admin. sec., police force, 1960; asst. estab. offr., 1960; senr. admin. offr., 1962.

**Version `col1961-L26666.v` — printed in editions [1961]:**

> RICHARDSON, A. P.—b. 1927; ed. St. Andrew's Coll. and Trinity Coll., Dublin; cadet, H.K., 1950; redesig. admin. offr., 1959; ag. chief asst. sec. for Chinese affrs., 1959.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1950 | cadet, H.K., asst. sec. for Chinese affrs | Hong Kong | [1961, 1962, 1963, 1964, 1965, 1966] |
| 1 | 1952 | lab. offr | — | [1962, 1963, 1964, 1965, 1966] |
| 2 | 1955 | lab. offr | Dominions Office | [1962, 1963, 1964, 1965, 1966] |
| 3 | 1957 | estab. offr | Dominions Office *(inherited from previous clause)* | [1962, 1963, 1964, 1965, 1966] |
| 4 | 1959 | redesign. admin. offr | Dominions Office *(inherited from previous clause)* | [1961, 1962, 1963, 1964, 1965, 1966] |
| 5 | 1959 | ag. chief asst. sec. for Chinese affrs | Hong Kong *(inherited from previous clause)* | [1961] |
| 6 | 1960 | admin. sec., police force | Dominions Office *(inherited from previous clause)* | [1962, 1963, 1964, 1965, 1966] |
| 7 | 1962 | senr. admin. offr | Dominions Office *(inherited from previous clause)* | [1962, 1963, 1964, 1965, 1966] |

## Candidate stint `Richardson, A. P___Hong Kong___1950`

- Staff-list name: **Richardson, A. P** | colony: **Hong Kong** | listed 1950–1951 | editions [1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1950 | A. P. Richardson | Cadet, Training | Cadet Service | — | — |
| 1951 | A. P. Richardson | Cadets on Probation | Cadet Service | — | — |

### Deterministic checks: `richardson_a-p_b1927` vs `Richardson, A. P___Hong Kong___1950`

- [PASS] surname_gate: bio 'RICHARDSON' vs stint 'Richardson, A. P' (exact)
- [PASS] initials: bio ['A', 'P'] ~ stint ['A', 'P']
- [PASS] age_gate: stint starts 1950, birth 1927 (age 23)
- [PASS] colony: 2 placed event(s) resolve to 'Hong Kong'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1950-1951
- [FAIL] position_sim: best 53 vs bar 60: 'cadet, H.K., asst. sec. for Chinese affrs' ~ 'Cadet, Training'
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

