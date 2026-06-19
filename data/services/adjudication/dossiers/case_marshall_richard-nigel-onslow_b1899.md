<!-- {"case_id": "case_marshall_richard-nigel-onslow_b1899", "bio_ids": ["marshall_richard-nigel-onslow_b1899"], "stint_ids": ["Marshall, N___Ceylon___1921"]} -->
# Dossier case_marshall_richard-nigel-onslow_b1899

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 79 official(s) with this surname in the graph's staff lists; 32 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `marshall_richard-nigel-onslow_b1899`

- Printed name: **MARSHALL, Richard Nigel Onslow**
- Birth year: 1899 (attested in editions [1949, 1950, 1951])
- Honours: D.S.C.
- Appears in editions: [1949, 1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1949-L34184.v` — printed in editions [1949, 1950, 1951]:**

> MARSHALL, Richard Nigel Onslow, D.S.C.—b. 1899; ed. Dean Close Memorial Sch., H.M.S. Conway and Corpus Christi Coll., Camb., B.A. (Cantab.); on nav. serv., 1915-20 and 1940-45; lieut.; admin. offr., cl. IV, Nig., 1924; cl. III, 1929; cl. II, 1948.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1915–1920 | on nav. serv. | — | [1949, 1950, 1951] |
| 1 | 1924 | admin. offr., cl. IV | Nigeria | [1949, 1950, 1951] |
| 2 | 1929 | cl. III | — | [1949, 1950, 1951] |
| 3 | 1940–1945 | on nav. serv. | — | [1949, 1950, 1951] |
| 4 | 1948 | cl. II | — | [1949, 1950, 1951] |

## Candidate stint `Marshall, N___Ceylon___1921`

- Staff-list name: **Marshall, N** | colony: **Ceylon** | listed 1921–1923 | editions [1921, 1922, 1923]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1921 | N. Marshall | Divisional Agricultural Officer, Northern | Department of Agriculture | — | — |
| 1922 | N. Marshall | Divisional Agricultural Officer | Agricultural Branch | — | — |
| 1923 | N. Marshall | Divisional Agricultural Officer, Northern | Agricultural Branch | — | — |

### Deterministic checks: `marshall_richard-nigel-onslow_b1899` vs `Marshall, N___Ceylon___1921`

- [PASS] surname_gate: bio 'MARSHALL' vs stint 'Marshall, N' (exact)
- [PASS] initials: bio ['R', 'N', 'O'] ~ stint ['N']
- [PASS] age_gate: stint starts 1921, birth 1899 (age 22)
- [FAIL] colony: no placed event resolves to 'Ceylon'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1921-1923
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

