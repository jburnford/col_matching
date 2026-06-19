<!-- {"case_id": "case_o-may_lily-stewart_b1883", "bio_ids": ["o-may_lily-stewart_b1883"], "stint_ids": ["O'May, L. S___Straits Settlements___1922"]} -->
# Dossier case_o-may_lily-stewart_b1883

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `o-may_lily-stewart_b1883`

- Printed name: **O'MAY, LILY STEWART**
- Birth year: 1883 (attested in editions [1932, 1933, 1934, 1935])
- Honours: M.B
- Appears in editions: [1932, 1933, 1934, 1935]

### Verbatim printed entry text (OCR)

**Version `col1932-L62953.v` — printed in editions [1932, 1933, 1934, 1935]:**

> O'MAY, LILY STEWART, M.B., Ch.B. (St. Andrews, 1909).—B. 1883; med. offr., Warren's hosp., K. Kangsar, June, 1913; grade II, May, 1914; med. offr., girls' schls., Penang, P.W. and Dindings, and i/c women and children's clinic, maternity hosp., Penang, Feb., 1926; i/c women and children's disp., Kandang Kerbau, Singapore, Oct., 1929; med. offr., Malacca, June, 1930; seconded for serv. under govt., Kedah, May, 1931.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1913 | med. offr., Warren's hosp., K. Kangsar | — | [1932, 1933, 1934, 1935] |
| 1 | 1914 | grade II | — | [1932, 1933, 1934, 1935] |
| 2 | 1926 | med. offr., girls' schls., Penang, P.W. and Dindings, and i/c women and children's clinic, maternity hosp., Penang | — | [1932, 1933, 1934, 1935] |
| 3 | 1929 | i/c women and children's disp., Kandang Kerbau | Singapore | [1932, 1933, 1934, 1935] |
| 4 | 1930 | med. offr., Malacca | Singapore *(inherited from previous clause)* | [1932, 1933, 1934, 1935] |
| 5 | 1931 | seconded for serv. under govt. | Kedah | [1932, 1933, 1934, 1935] |

## Candidate stint `O'May, L. S___Straits Settlements___1922`

- Staff-list name: **O'May, L. S** | colony: **Straits Settlements** | listed 1922–1931 | editions [1922, 1923, 1925, 1931]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1922 | L. O'May | Medical Officer and Health Officer | Medical | — | — |
| 1923 | L. S. O'May | Medical Officers and Health Officers | Medical | — | — |
| 1925 | L. S. O'May | Lady Medical Officer | SINGAPORE | — | — |
| 1931 | L. S. O'May | Medical and Health Officer | Malacca | — | — |

### Deterministic checks: `o-may_lily-stewart_b1883` vs `O'May, L. S___Straits Settlements___1922`

- [PASS] surname_gate: bio 'O'MAY' vs stint 'O'May, L. S' (exact)
- [PASS] initials: bio ['L', 'S'] ~ stint ['L', 'S']
- [PASS] age_gate: stint starts 1922, birth 1883 (age 39)
- [FAIL] colony: no placed event resolves to 'Straits Settlements'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1922-1931
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

