<!-- {"case_id": "case_bechgaard_kai_b1914", "bio_ids": ["bechgaard_kai_b1914"], "stint_ids": ["Bechgaard, K___Aden___1949"]} -->
# Dossier case_bechgaard_kai_b1914

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['bechgaard_kai_b1914'] carry a single initial only — the namesake trap applies.

## Biography `bechgaard_kai_b1914`

- Printed name: **BECHGAARD, Kai**
- Birth year: 1914 (attested in editions [1948])
- Appears in editions: [1948, 1951]

### Verbatim printed entry text (OCR)

**Version `col1948-L31072.v` — printed in editions [1948]:**

> BECHGAARD, Kai, LL.B. (hons.) (Lond.)—b. 1914; ed. Ash-Eton Sch., Folkestone, and King's Coll., Univ. of London; barrister-at-law, Gray's Inn, 1935; on mil. serv. 1941-46, flt.-lieut.; crown coun., Aden, 1946; proper offr. of the crown; ag. atty.-gen., Aden, Jan.-Oct., 1947.

**Version `col1951-L36068.v` — printed in editions [1951]:**

> BECHGAARD, Kai, LL.B. (hons.) (Lond.).—b. 1914; ed. Diocesan Coll., Lund, Sweden, Ash-Eton, Folkestone and King's Coll., Lond.; barrister-at-law, Gray's Inn; on war serv., 1941-46, flt.-lt.; cr. coun., Aden; asst. legal sec., E.A.H.C., 1950; sp. mag. (riot damage), Aden, 1948; D.C.A., Aden, 1947-50.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1935 | barrister-at-law, Gray's Inn | — | [1948] |
| 1 | 1946 | crown coun. | Aden | [1948] |
| 2 | 1947 | ag. atty.-gen., Aden, Jan.- | Aden | [1948, 1951] |
| 3 | 1948 | sp. mag. (riot damage) | Aden | [1951] |
| 4 | 1950 | asst. legal sec., E.A.H.C | — | [1951] |

## Candidate stint `Bechgaard, K___Aden___1949`

- Staff-list name: **Bechgaard, K** | colony: **Aden** | listed 1949–1950 | editions [1949, 1950]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | K. Bechgaard | Crown Counsel | LEGAL | — | — |
| 1950 | K. Bechgaard | Crown Counsel | LEGAL | — | — |

### Deterministic checks: `bechgaard_kai_b1914` vs `Bechgaard, K___Aden___1949`

- [PASS] surname_gate: bio 'BECHGAARD' vs stint 'Bechgaard, K' (exact)
- [PASS] initials: bio ['K'] ~ stint ['K']
- [PASS] age_gate: stint starts 1949, birth 1914 (age 35)
- [PASS] colony: 3 placed event(s) resolve to 'Aden'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1949-1950
- [FAIL] position_sim: best 26 vs bar 60: 'sp. mag. (riot damage)' ~ 'Crown Counsel'
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

