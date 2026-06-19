<!-- {"case_id": "case_sedgwick_a-w_b1932", "bio_ids": ["sedgwick_a-w_b1932"], "stint_ids": ["Sedgwick, A. W___Bermuda___1961"]} -->
# Dossier case_sedgwick_a-w_b1932

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 10 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `sedgwick_a-w_b1932`

- Printed name: **SEDGWICK, A. W**
- Birth year: 1932 (attested in editions [1966])
- Appears in editions: [1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1966-L17843.v` — printed in editions [1966]:**

> SEDGWICK, A. W.—b. 1932; ed. Brasenose Coll., Oxford; barrister-at-law, Middle Temple; mag., Berm., 1959; senr. mag., 1962; sol.-gen., 1965.

**Version `col1965-L19000.v` — printed in editions [1965]:**

> SEDGEWICK, A. W.—b. 1932; ed. Brasenose Coll., Oxford; barrister-at-law, Middle Temple; mag., Berm., 1959; senr. mag., 1962.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1959 | mag. | Bermuda | [1965, 1966] |
| 1 | 1962 | senr. mag | Bermuda *(inherited from previous clause)* | [1965, 1966] |
| 2 | 1965 | sol.-gen | Bermuda *(inherited from previous clause)* | [1966] |

## Candidate stint `Sedgwick, A. W___Bermuda___1961`

- Staff-list name: **Sedgwick, A. W** | colony: **Bermuda** | listed 1961–1966 | editions [1961, 1962, 1963, 1964, 1965, 1966]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1961 | A. W. Sedgwick | Magistrate | Judiciary | — | — |
| 1962 | A. W. Sedgwick | Magistrate | Judiciary | — | — |
| 1963 | A. W. Sedgwick | Senior Magistrate | Judiciary | — | — |
| 1964 | A. W. Sedgwick | Senior Magistrate | Judiciary | — | — |
| 1965 | A. W. Sedgwick | Senior Magistrate | Civil Establishment | — | — |
| 1966 | A. W. Sedgwick | Solicitor-General | Civil Establishment | — | — |

### Deterministic checks: `sedgwick_a-w_b1932` vs `Sedgwick, A. W___Bermuda___1961`

- [PASS] surname_gate: bio 'SEDGWICK' vs stint 'Sedgwick, A. W' (exact)
- [PASS] initials: bio ['A', 'W'] ~ stint ['A', 'W']
- [PASS] age_gate: stint starts 1961, birth 1932 (age 29)
- [PASS] colony: 3 placed event(s) resolve to 'Bermuda'
- [PASS] tenure_overlap: 3 event tenure(s) overlap stint years 1961-1966
- [PASS] position_sim: best 64 vs bar 60: 'senr. mag' ~ 'Senior Magistrate'
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

