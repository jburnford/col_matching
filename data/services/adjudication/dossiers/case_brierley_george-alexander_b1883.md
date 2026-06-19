<!-- {"case_id": "case_brierley_george-alexander_b1883", "bio_ids": ["brierley_george-alexander_b1883"], "stint_ids": ["Brierley, G. A___Barbados___1927"]} -->
# Dossier case_brierley_george-alexander_b1883

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 5 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `brierley_george-alexander_b1883`

- Printed name: **BRIERLEY, George Alexander**
- Birth year: 1883 (attested in editions [1928, 1929, 1930, 1932])
- Appears in editions: [1928, 1929, 1930, 1931, 1932]

### Verbatim printed entry text (OCR)

**Version `col1928-L64461.v` — printed in editions [1928, 1929, 1930, 1932]:**

> BRIERLEY, George Alexander.—B. 1883; ed. Queen's Royal Coll., Trinidad; cler. asst., harbmr'a. office, Mar., 1904; 3rd junr., clk., cust., Feb., 1906; 2nd ditto, Apr., 1906; 3rd cls. landing waiter, Sept., 1907; 2nd cls. ditto, July, 1913; senr. check clk., cust., Oct., 1920; comptr., cust., Barbados, Feb., 1926.

**Version `col1931-L62788.v` — printed in editions [1931]:**

> BRIERLEY, GEORGE ALEXANDER.—B. 1883; ed. Queen's Royal Coll., Trinidad; cler. asst., harbour's office, Mar., 1904; 3rd junr. elk., cust.,

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1904 | cler. asst., harbmr'a. office | — | [1928, 1929, 1930, 1931, 1932] |
| 1 | 1906 | 3rd junr., clk., cust | — | [1928, 1929, 1930, 1932] |
| 2 | 1906 | 2nd ditto | — | [1928, 1929, 1930, 1932] |
| 3 | 1907 | 3rd cls. landing waiter | — | [1928, 1929, 1930, 1932] |
| 4 | 1913 | 2nd cls. ditto | — | [1928, 1929, 1930, 1932] |
| 5 | 1920 | senr. check clk., cust | — | [1928, 1929, 1930, 1932] |
| 6 | 1926 | comptr., cust. | Barbados | [1928, 1929, 1930, 1932] |

## Candidate stint `Brierley, G. A___Barbados___1927`

- Staff-list name: **Brierley, G. A** | colony: **Barbados** | listed 1927–1930 | editions [1927, 1928, 1929, 1930]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1927 | G. A. Brierley | Controller | Customs | — | — |
| 1928 | G. A. Brierley | Controller | Customs | — | — |
| 1929 | G. A. Brierley | Controller | Customs | — | — |
| 1930 | G. A. Brierley | Controller | Customs | — | — |

### Deterministic checks: `brierley_george-alexander_b1883` vs `Brierley, G. A___Barbados___1927`

- [PASS] surname_gate: bio 'BRIERLEY' vs stint 'Brierley, G. A' (exact)
- [PASS] initials: bio ['G', 'A'] ~ stint ['G', 'A']
- [PASS] age_gate: stint starts 1927, birth 1883 (age 44)
- [PASS] colony: 1 placed event(s) resolve to 'Barbados'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1927-1930
- [FAIL] position_sim: best 38 vs bar 60: 'comptr., cust.' ~ 'Controller'
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

