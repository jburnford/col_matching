<!-- {"case_id": "case_dickson_richard-sebastian-willcox_b1897", "bio_ids": ["dickson_richard-sebastian-willcox_b1897"], "stint_ids": ["Dickson, Scott___Rhodesia___1921", "Dickson, W___Australia___1913"]} -->
# Dossier case_dickson_richard-sebastian-willcox_b1897

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 56 official(s) with this surname in the graph's staff lists; 18 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Dickson, W___Australia___1913` is also gate-compatible with biography(ies) outside this case: ['dickson_george-workman_e1869'] (already linked elsewhere or filtered).

## Biography `dickson_richard-sebastian-willcox_b1897`

- Printed name: **DICKSON, RICHARD SEBASTIAN WILLCOX**
- Birth year: 1897 (attested in editions [1934])
- Honours: D.S.O (1916)
- Appears in editions: [1934]

### Verbatim printed entry text (OCR)

**Version `col1934-L58445.v` — printed in editions [1934]:**

> DICKSON, THE HON. RICHARD SEBASTIAN WILLCOX, D.S.O. (1916).—B. 1897; ed. at Eton and Trinity Coll., Oxford; asst. dist. offr., Nigeria, 1922; priv. sec. to Sir Hugh Clifford, 1922-23; seconded as priv. sec. to Sir H. J. Stanley, gov. of N. Rhodesia, 1925-26; asst. ch. sec., N. Rhodesia, 1926; ag. prin. asst. ch. sec. on various occasions, 1929-32; ag. ch. sec., 1933.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1922 | asst. dist. offr. | Nigeria | [1934] |
| 1 | 1925–1926 | seconded as priv. sec. to Sir H. J. Stanley, gov. of N. Rhodesia | Nigeria *(inherited from previous clause)* | [1934] |
| 2 | 1926 | asst. ch. sec., N. Rhodesia | Nigeria *(inherited from previous clause)* | [1934] |
| 3 | 1929–1932 | ag. prin. asst. ch. sec. on various occasions | Nigeria *(inherited from previous clause)* | [1934] |
| 4 | 1933 | ag. ch. sec | Nigeria *(inherited from previous clause)* | [1934] |

## Candidate stint `Dickson, Scott___Rhodesia___1921`

- Staff-list name: **Dickson, Scott** | colony: **Rhodesia** | listed 1921–1923 | editions [1921, 1923]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1921 | Scott Dickson | — | — | — | — |
| 1923 | Scott Dickson | Member of the Judicial Committee of the Privy Council | — | — | — |

### Deterministic checks: `dickson_richard-sebastian-willcox_b1897` vs `Dickson, Scott___Rhodesia___1921`

- [PASS] surname_gate: bio 'DICKSON' vs stint 'Dickson, Scott' (exact)
- [PASS] initials: bio ['R', 'S', 'W'] ~ stint ['S']
- [PASS] age_gate: stint starts 1921, birth 1897 (age 24)
- [FAIL] colony: no placed event resolves to 'Rhodesia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1921-1923
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Dickson, W___Australia___1913`

- Staff-list name: **Dickson, W** | colony: **Australia** | listed 1913–1918 | editions [1913, 1918]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1913 | W. Dickson | Secretary | DEPARTMENT OF MINES | — | — |
| 1918 | W. Dickson | Secretary | Department of Mines | — | — |

### Deterministic checks: `dickson_richard-sebastian-willcox_b1897` vs `Dickson, W___Australia___1913`

- [PASS] surname_gate: bio 'DICKSON' vs stint 'Dickson, W' (exact)
- [PASS] initials: bio ['R', 'S', 'W'] ~ stint ['W']
- [PASS] age_gate: stint starts 1913, birth 1897 (age 16)
- [FAIL] colony: no placed event resolves to 'Australia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1913-1918
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

