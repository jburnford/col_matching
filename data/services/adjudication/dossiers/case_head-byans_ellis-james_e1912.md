<!-- {"case_id": "case_head-byans_ellis-james_e1912", "bio_ids": ["head-byans_ellis-james_e1912"], "stint_ids": ["Head-Evans, E. J___Tanganyika___1923"]} -->
# Dossier case_head-byans_ellis-james_e1912

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Head-Evans, E. J___Tanganyika___1923` is also gate-compatible with biography(ies) outside this case: ['head-evans_ellis-james_e1912'] (already linked elsewhere or filtered).

## Biography `head-byans_ellis-james_e1912`

- Printed name: **HEAD-BYANS, ELLIS JAMES**
- Birth year: not printed
- Honours: A.M.S.B
- Appears in editions: [1928]

### Verbatim printed entry text (OCR)

**Version `col1928-L66941.v` — printed in editions [1928]:**

> HEAD-BYANS, ELLIS JAMES, M.I.M. & C.E., A.M.S.B.—Asst. engr., P.W.D., Nyassaland, Jan., 1912 to Aug., 1916; ag. asst. D.P.W., Nyassaland, Jan. to Sept., 1913; served with Nyassaland Vol. Res., 1914-15 (A.G.S. Med.); attd. as civil offr. to Nyassaland Field Force as ch. engr., road constrn. in operns. in German E. Africa, Mar., 1916 to Sept., 1917; seconded as asst. engr., P.W.D., Tanganyika Territory, Aug., 1916; exec. engr., Tanganyika Territory, Apr., 1920.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1912–1916 | Asst. engr., P.W.D., Nyassaland | — | [1928] |
| 1 | 1913 | ag. asst. D.P.W., Nyassaland | — | [1928] |
| 2 | 1914–1915 | served with Nyassaland Vol. Res | — | [1928] |
| 3 | 1916–1917 | attd. as civil offr. to Nyassaland Field Force as ch. engr., road constrn. in operns. in German E. Africa | — | [1928] |
| 4 | 1916 | seconded as asst. engr., P.W.D., Tanganyika Territory | Tanganyika | [1928] |
| 5 | 1920 | exec. engr., Tanganyika Territory | Tanganyika | [1928] |

## Candidate stint `Head-Evans, E. J___Tanganyika___1923`

- Staff-list name: **Head-Evans, E. J** | colony: **Tanganyika** | listed 1923–1925 | editions [1923, 1924, 1925]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1923 | E. J. Head-Evans | Executive Engineers | Public Works Department | — | — |
| 1924 | E. J. Head-Evans | Executive Engineers | Public Works Department | — | — |
| 1925 | E. J. Head-Evans | Executive Engineer | Public Works Department | — | — |

### Deterministic checks: `head-byans_ellis-james_e1912` vs `Head-Evans, E. J___Tanganyika___1923`

- [PASS] surname_gate: bio 'HEAD-BYANS' vs stint 'Head-Evans, E. J' (fuzzy:2)
- [PASS] initials: bio ['E', 'J'] ~ stint ['E', 'J']
- [PASS] age_gate: stint starts 1923; no printed birth year — UNCHECKED
- [PASS] colony: 2 placed event(s) resolve to 'Tanganyika'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1923-1925
- [FAIL] position_sim: best 50 vs bar 60: 'exec. engr., Tanganyika Territory' ~ 'Executive Engineer'
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

