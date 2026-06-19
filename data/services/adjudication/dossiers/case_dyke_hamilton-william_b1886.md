<!-- {"case_id": "case_dyke_hamilton-william_b1886", "bio_ids": ["dyke_hamilton-william_b1886"], "stint_ids": ["Dyke, Hamilton William___Basutoland___1920"]} -->
# Dossier case_dyke_hamilton-william_b1886

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 6 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Dyke, Hamilton William___Basutoland___1920` is also gate-compatible with biography(ies) outside this case: ['dyke_hamilton-william_b1881'] (already linked elsewhere or filtered).

## Biography `dyke_hamilton-william_b1886`

- Printed name: **DYKE, HAMILTON WILLIAM**
- Birth year: 1886 (attested in editions [1937])
- Honours: C.B, M.B
- Appears in editions: [1937]

### Verbatim printed entry text (OCR)

**Version `col1937-L60527.v` — printed in editions [1937]:**

> DYKE, HAMILTON WILLIAM, C.B., M.B., Ch.B., Glasgow, 1896—B. 1886; ed. African Coll., Cape Town and Glasgow; housephys., Glasgow Royal Infirmary; Glasgow Western Infirmary, Glasgow Inst. and Glasgow Royal Hosp. for succ. med., offr., Maseru, Basutoland, 1915; capt., R.A.M.C., 1915-19; serv., med., 1915-19; S.M.O., S.A. Native Le Rouen area, 1919; surg. spe., Jerusalem and gov't. of Palestine; med. offr., Bechuana Land Prot., Basutoland, 1935; author of "An Scurvy among South African Natives," Lancet, 1917; "A case of Madura Fever," S. African Med. Jnl.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1915 | Glasgow Western Infirmary, Glasgow Inst. and Glasgow Royal Hosp. for succ. med., offr., Maseru | Basutoland | [1937] |
| 1 | 1917 | author of "An Scurvy among South African Natives," Lancet | Basutoland *(inherited from previous clause)* | [1937] |
| 2 | 1919 | S.M.O., S.A. Native Le Rouen area | Basutoland *(inherited from previous clause)* | [1937] |
| 3 | 1935 | med. offr., Bechuana Land Prot. | Basutoland | [1937] |

## Candidate stint `Dyke, Hamilton William___Basutoland___1920`

- Staff-list name: **Dyke, Hamilton William** | colony: **Basutoland** | listed 1920–1925 | editions [1920, 1921, 1922, 1924, 1925]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1920 | Hamilton Dyke | Medical Officer | Establishment | — | — |
| 1921 | Hamilton Dyke | Medical Officer | Establishment | — | — |
| 1922 | Hamilton Dyke | Medical Officer, Moseru District | Establishment | — | — |
| 1924 | Hamilton William Dyke | Medical Officer | Medical | — | — |
| 1925 | Hamilton William Dyke | Medical Officer | Medical | — | — |

### Deterministic checks: `dyke_hamilton-william_b1886` vs `Dyke, Hamilton William___Basutoland___1920`

- [PASS] surname_gate: bio 'DYKE' vs stint 'Dyke, Hamilton William' (exact)
- [PASS] initials: bio ['H', 'W'] ~ stint ['H', 'W']
- [PASS] age_gate: stint starts 1920, birth 1886 (age 34)
- [PASS] colony: 4 placed event(s) resolve to 'Basutoland'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1920-1925
- [FAIL] position_sim: best 34 vs bar 60: 'S.M.O., S.A. Native Le Rouen area' ~ 'Medical Officer, Moseru District'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
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

