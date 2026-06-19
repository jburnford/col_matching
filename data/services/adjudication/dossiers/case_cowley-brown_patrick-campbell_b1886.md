<!-- {"case_id": "case_cowley-brown_patrick-campbell_b1886", "bio_ids": ["cowley-brown_patrick-campbell_b1886"], "stint_ids": ["Cowley-Brown, P. C___Straits Settlements___1923"]} -->
# Dossier case_cowley-brown_patrick-campbell_b1886

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `cowley-brown_patrick-campbell_b1886`

- Printed name: **COWLEY-BROWN, PATRICK CAMPBELL**
- Birth year: 1886 (attested in editions [1923, 1924, 1925, 1927, 1928])
- Appears in editions: [1923, 1924, 1925, 1927, 1928]

### Verbatim printed entry text (OCR)

**Version `col1923-L53488.v` — printed in editions [1923, 1924, 1925, 1927, 1928]:**

> COWLEY-BROWN, PATRICK CAMPBELL, M.B.E. (Civil).—B. 1886; sp. offr. in charge of locust destruction, Malacca, Aug., 1914; asst. cable censor and latterly senr. asst. cable censor, S. Sttlmts. and F.M.S., Nov., 1915; passport offr. and conf. clk., col. sec.'s office, Singapore, Apr., 1919 to Dec., 1921; conf. clk., col. sec.'s office, Dec., 1921.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1914 | sp. offr. in charge of locust destruction, Malacca | — | [1923, 1924, 1925, 1927, 1928] |
| 1 | 1915 | asst. cable censor and latterly senr. asst. cable censor, S. Sttlmts. and F.M.S | — | [1923, 1924, 1925, 1927, 1928] |
| 2 | 1919–1921 | passport offr. and conf. clk., col. sec.'s office | Singapore | [1923, 1924, 1925, 1927, 1928] |
| 3 | 1921 | conf. clk., col. sec.'s office | Singapore *(inherited from previous clause)* | [1923, 1924, 1925, 1927, 1928] |

## Candidate stint `Cowley-Brown, P. C___Straits Settlements___1923`

- Staff-list name: **Cowley-Brown, P. C** | colony: **Straits Settlements** | listed 1923–1925 | editions [1923, 1925]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1923 | P. C. Cowley-Brown | Confidential Clerk | Colonial Secretary's Office | — | — |
| 1925 | P. C. Cowley-Brown | Confidential Clerk | Colonial Secretary's Office | — | — |

### Deterministic checks: `cowley-brown_patrick-campbell_b1886` vs `Cowley-Brown, P. C___Straits Settlements___1923`

- [PASS] surname_gate: bio 'COWLEY-BROWN' vs stint 'Cowley-Brown, P. C' (exact)
- [PASS] initials: bio ['P', 'C'] ~ stint ['P', 'C']
- [PASS] age_gate: stint starts 1923, birth 1886 (age 37)
- [FAIL] colony: no placed event resolves to 'Straits Settlements'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1923-1925
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

