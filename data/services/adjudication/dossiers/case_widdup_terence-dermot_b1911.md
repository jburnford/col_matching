<!-- {"case_id": "case_widdup_terence-dermot_b1911", "bio_ids": ["widdup_terence-dermot_b1911"], "stint_ids": ["Widdup, T. D___Gold Coast___1949"]} -->
# Dossier case_widdup_terence-dermot_b1911

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 5 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `widdup_terence-dermot_b1911`

- Printed name: **WIDDUP, Terence Dermot**
- Birth year: 1911 (attested in editions [1950, 1951])
- Appears in editions: [1948, 1949, 1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1950-L40716.v` — printed in editions [1950, 1951]:**

> WIDDUP, Terence Dermot.—b. 1911; ed. Queen's Coll., B. Guiana and Southern England; sub-inspr., police, B. Guiana, 1933; asst. supt., G.C., 1937; senr. asst., 1945; supt., 1946; seconded C.O. as supervisor, col. police courses, 1949.

**Version `col1948-L36841.v` — printed in editions [1948]:**

> WIDDUP, Terence Dermot.—b. 1911; sub-inspr. of police, Br. Guiana, 1933; G.C., 1937; ag. dist. comsnnr., Ashanti (seconded), 1944-46; supt. of police, G.C., 1946.

**Version `col1949-L36699.v` — printed in editions [1949]:**

> WIDDUP, Terence Dermot.—b. 1911; sub-inspr., police, B. Guiana, 1933; G.C., 1937; supt., police, G.C., 1946.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1933 | sub-inspr., police, B. Guiana | British Guiana | [1948, 1949, 1950, 1951] |
| 1 | 1937 | asst. supt. | Gold Coast | [1948, 1949, 1950, 1951] |
| 2 | 1944–1946 | ag. dist. comsnnr., Ashanti (seconded) | Ashanti | [1948] |
| 3 | 1945 | senr. asst | Gold Coast *(inherited from previous clause)* | [1950, 1951] |
| 4 | 1946 | supt | Gold Coast | [1948, 1949, 1950, 1951] |
| 5 | 1949 | seconded C.O. as supervisor, col. police courses | Colonial Office | [1950, 1951] |

## Candidate stint `Widdup, T. D___Gold Coast___1949`

- Staff-list name: **Widdup, T. D** | colony: **Gold Coast** | listed 1949–1951 | editions [1949, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | T. D. Widdup | Superintendents | Police | — | — |
| 1951 | T. D. Widdup | Superintendent of Police | Police | — | — |

### Deterministic checks: `widdup_terence-dermot_b1911` vs `Widdup, T. D___Gold Coast___1949`

- [PASS] surname_gate: bio 'WIDDUP' vs stint 'Widdup, T. D' (exact)
- [PASS] initials: bio ['T', 'D'] ~ stint ['T', 'D']
- [PASS] age_gate: stint starts 1949, birth 1911 (age 38)
- [PASS] colony: 4 placed event(s) resolve to 'Gold Coast'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1949-1951
- [FAIL] position_sim: best 42 vs bar 60: 'supt' ~ 'Superintendents'
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

