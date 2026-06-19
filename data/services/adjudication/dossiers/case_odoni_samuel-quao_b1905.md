<!-- {"case_id": "case_odoni_samuel-quao_b1905", "bio_ids": ["odoni_samuel-quao_b1905"], "stint_ids": ["Odoi, S. Q___Gold Coast___1949"]} -->
# Dossier case_odoni_samuel-quao_b1905

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Odoi, S. Q___Gold Coast___1949` is also gate-compatible with biography(ies) outside this case: ['odoi_samuel-quao_b1905'] (already linked elsewhere or filtered).

## Biography `odoni_samuel-quao_b1905`

- Printed name: **ODONI, Samuel Quao**
- Birth year: 1905 (attested in editions [1951])
- Appears in editions: [1951]

### Verbatim printed entry text (OCR)

**Version `col1951-L41297.v` — printed in editions [1951]:**

> ODONI, Samuel Quao.—b. 1905; apptd. 4th cl. clk., G.C., 1921; 2nd div. clk. (reclass.), 1922; acctnt., 1943.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1921 | apptd. 4th cl. clk. | Gold Coast | [1951] |
| 1 | 1922 | 2nd div. clk. (reclass.) | Gold Coast *(inherited from previous clause)* | [1951] |
| 2 | 1943 | acctnt | Gold Coast *(inherited from previous clause)* | [1951] |

## Candidate stint `Odoi, S. Q___Gold Coast___1949`

- Staff-list name: **Odoi, S. Q** | colony: **Gold Coast** | listed 1949–1951 | editions [1949, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | S. Q. Odoi | Accountants | Posts and Telegraphs | — | — |
| 1951 | S. Q. Odoi | Accountants | Accounts Branch | — | — |

### Deterministic checks: `odoni_samuel-quao_b1905` vs `Odoi, S. Q___Gold Coast___1949`

- [PASS] surname_gate: bio 'ODONI' vs stint 'Odoi, S. Q' (fuzzy:1)
- [PASS] initials: bio ['S', 'Q'] ~ stint ['S', 'Q']
- [PASS] age_gate: stint starts 1949, birth 1905 (age 44)
- [PASS] colony: 3 placed event(s) resolve to 'Gold Coast'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1949-1951
- [PASS] position_sim: best 71 vs bar 60: 'acctnt' ~ 'Accountants'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): 1 agreeing edition-year(s) [1951] pos~71 (bar: >=2)
- [FAIL] place_inherited: ALL supporting events inherit their place from an earlier clause — weak evidence

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

