<!-- {"case_id": "case_moore_s-h_b1905", "bio_ids": ["moore_s-h_b1905"], "stint_ids": ["Moore, S. H___Hong Kong___1949"]} -->
# Dossier case_moore_s-h_b1905

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 128 official(s) with this surname in the graph's staff lists; 38 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Moore, S. H___Hong Kong___1949` is also gate-compatible with biography(ies) outside this case: ['moore_s_e1879'] (already linked elsewhere or filtered).

## Biography `moore_s-h_b1905`

- Printed name: **MOORE, S. H**
- Birth year: 1905 (attested in editions [1957, 1958, 1959, 1960, 1961, 1962, 1963])
- Appears in editions: [1957, 1958, 1959, 1960, 1961, 1962, 1963]

### Verbatim printed entry text (OCR)

**Version `col1957-L25795.v` — printed in editions [1957, 1958, 1959, 1960, 1961, 1962, 1963]:**

> MOORE, S. H.—b. 1905; ed. Wesley Coll., Dublin, and Trinity Coll., Dublin; mil. serv., 1944-46, maj.; M.O., H.K., 1946; S.M.O., 1955; asst. dir., med. and health services, 1959-62.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1946 | M.O. | Hong Kong | [1957, 1958, 1959, 1960, 1961, 1962, 1963] |
| 1 | 1955 | S.M.O | Hong Kong *(inherited from previous clause)* | [1957, 1958, 1959, 1960, 1961, 1962, 1963] |
| 2 | 1959–1962 | asst. dir., med. and health services | Hong Kong *(inherited from previous clause)* | [1957, 1958, 1959, 1960, 1961, 1962, 1963] |

## Candidate stint `Moore, S. H___Hong Kong___1949`

- Staff-list name: **Moore, S. H** | colony: **Hong Kong** | listed 1949–1950 | editions [1949, 1950]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | S. H. Moore | Health Officer | Medical | — | — |
| 1950 | S. H. Moore | Medical and Health Officer | MEDICAL | — | — |

### Deterministic checks: `moore_s-h_b1905` vs `Moore, S. H___Hong Kong___1949`

- [PASS] surname_gate: bio 'MOORE' vs stint 'Moore, S. H' (exact)
- [PASS] initials: bio ['S', 'H'] ~ stint ['S', 'H']
- [PASS] age_gate: stint starts 1949, birth 1905 (age 44)
- [PASS] colony: 3 placed event(s) resolve to 'Hong Kong'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1949-1950
- [FAIL] position_sim: best 14 vs bar 60: 'M.O.' ~ 'Medical and Health Officer'
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

