<!-- {"case_id": "case_harrison_newcome-herbert_b1885", "bio_ids": ["harrison_newcome-herbert_b1885"], "stint_ids": ["Harrison, N___South Africa___1914"]} -->
# Dossier case_harrison_newcome-herbert_b1885

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 85 official(s) with this surname in the graph's staff lists; 30 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `harrison_newcome-herbert_b1885`

- Printed name: **HARRISON, NEWCOME HERBERT**
- Birth year: 1885 (attested in editions [1932, 1933, 1934])
- Honours: L.D.S, L.R.C.P, L.S.T.M, M.R.C.S
- Appears in editions: [1932, 1933, 1934]

### Verbatim printed entry text (OCR)

**Version `col1932-L60929.v` — printed in editions [1932, 1933, 1934]:**

> HARRISON, NEWCOME HERBERT, M.R.C.S., L.R.C.P., L.D.S., R.C.S. (Eng.), L.S.T.M.—B. 1885; med. offr., Johore, Nov., 1920; med. offr., gen. hosp., Johore Bahru, Sept., 1923; med. offr., i/c, Trengganu, Sept., 1925; ch. med. offr., Trengganu, Jly., 1928.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1920 | med. offr. | Johore | [1932, 1933, 1934] |
| 1 | 1923 | med. offr., gen. hosp., Johore Bahru | Johore | [1932, 1933, 1934] |
| 2 | 1925 | med. offr., i/c | Trengganu | [1932, 1933, 1934] |
| 3 | 1928 | ch. med. offr., Trengganu, Jly | Trengganu *(inherited from previous clause)* | [1932, 1933, 1934] |

## Candidate stint `Harrison, N___South Africa___1914`

- Staff-list name: **Harrison, N** | colony: **South Africa** | listed 1914–1918 | editions [1914, 1918]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1914 | N. Harrison | Engineer-in-Chief | Department of Posts and Telegraphs | — | — |
| 1918 | N. Harrison | Engineer-in-Chief | Posts and Telegraphs | — | — |

### Deterministic checks: `harrison_newcome-herbert_b1885` vs `Harrison, N___South Africa___1914`

- [PASS] surname_gate: bio 'HARRISON' vs stint 'Harrison, N' (exact)
- [PASS] initials: bio ['N', 'H'] ~ stint ['N']
- [PASS] age_gate: stint starts 1914, birth 1885 (age 29)
- [FAIL] colony: no placed event resolves to 'South Africa'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1914-1918
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

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

