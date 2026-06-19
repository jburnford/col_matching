<!-- {"case_id": "case_buckle_dorothy-m_b1883", "bio_ids": ["buckle_dorothy-m_b1883"], "stint_ids": ["Buckle, D. M___Straits Settlements___1922", "Buckle, Miss D. M___Straits Settlements___1932"]} -->
# Dossier case_buckle_dorothy-m_b1883

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 13 official(s) with this surname in the graph's staff lists; 8 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `buckle_dorothy-m_b1883`

- Printed name: **BUCKLE, DOROTHY M**
- Birth year: 1883 (attested in editions [1925, 1927, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937])
- Honours: O.B.E (1951)
- Appears in editions: [1925, 1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937]

### Verbatim printed entry text (OCR)

**Version `col1925-L54477.v` — printed in editions [1925, 1927, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937]:**

> BUCKLE, DOROTHY M., O.B.E. (1951)—B. 1883; ed. Howard Gardens Munic. Secondary Schol., Cardiff and Whitleands Training Coll., Chelsea; 1st cls. B. of E. teachers' certif.; asst. prin., Raffles girls schol., Singapore, 1908; sg. prin., 1909; prin., 1911.

**Version `col1928-L64567.v` — printed in editions [1928]:**

> BUCKLEY, DOROTHY M.—B. 1883; ed. Howard Gardens Music Secondary Schol., Cardiff and Whitelands Training Coll., Chelsea; 1st cls. B. of E. teachers' certif.; asst. prin., Raffles girls schol., Singapore, 1908; ag. prin., 1909; prin., 1911.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1908 | asst. prin., Raffles girls schol. | Singapore | [1925, 1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937] |
| 1 | 1909 | sg. prin | Singapore *(inherited from previous clause)* | [1925, 1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937] |
| 2 | 1911 | prin | Singapore *(inherited from previous clause)* | [1925, 1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937] |

## Candidate stint `Buckle, D. M___Straits Settlements___1922`

- Staff-list name: **Buckle, D. M** | colony: **Straits Settlements** | listed 1922–1931 | editions [1922, 1925, 1931]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1922 | D. M. Buckle | Principal, Raffles Girls' School, Singapore | Education | — | — |
| 1925 | Miss D. M. Buckle | Principal, Raffles Girls' School, Singapore | Education | — | — |
| 1931 | D. M. Buckle | Principal, Raffles Girls' School | Education | — | — |

### Deterministic checks: `buckle_dorothy-m_b1883` vs `Buckle, D. M___Straits Settlements___1922`

- [PASS] surname_gate: bio 'BUCKLE' vs stint 'Buckle, D. M' (exact)
- [PASS] initials: bio ['D', 'M'] ~ stint ['D', 'M']
- [PASS] age_gate: stint starts 1922, birth 1883 (age 39)
- [FAIL] colony: no placed event resolves to 'Straits Settlements'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1922-1931
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Buckle, Miss D. M___Straits Settlements___1932`

- Staff-list name: **Buckle, Miss D. M** | colony: **Straits Settlements** | listed 1932–1933 | editions [1932, 1933]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1932 | Miss D. M. Buckle | Principal, Raffles Girls' School | Education | O.B.E. | — |
| 1933 | Miss D. M. Buckle | Principal, Raffles Girls' School, Singapore | Education | — | — |

### Deterministic checks: `buckle_dorothy-m_b1883` vs `Buckle, Miss D. M___Straits Settlements___1932`

- [PASS] surname_gate: bio 'BUCKLE' vs stint 'Buckle, Miss D. M' (exact)
- [PASS] initials: bio ['D', 'M'] ~ stint ['M', 'D', 'M']
- [PASS] age_gate: stint starts 1932, birth 1883 (age 49)
- [FAIL] colony: no placed event resolves to 'Straits Settlements'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1932-1933
- [FAIL] position_sim: no overlapping placed event to compare
- [PASS] honour: shared: O.B.E
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

