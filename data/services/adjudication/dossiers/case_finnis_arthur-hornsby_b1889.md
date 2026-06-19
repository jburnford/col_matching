<!-- {"case_id": "case_finnis_arthur-hornsby_b1889", "bio_ids": ["finnis_arthur-hornsby_b1889"], "stint_ids": ["Finnis, A. H___Tanganyika___1924"]} -->
# Dossier case_finnis_arthur-hornsby_b1889

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `finnis_arthur-hornsby_b1889`

- Printed name: **FINNIS, ARTHUR HORNSBY**
- Birth year: 1889 (attested in editions [1930, 1931])
- Honours: A.C.G.I, A.M.I.E.E
- Appears in editions: [1930, 1931]

### Verbatim printed entry text (OCR)

**Version `col1930-L64395.v` — printed in editions [1930, 1931]:**

> FINNIS, ARTHUR HORNSBY, A.C.G.I., A.M.I.E.E.—B. 1889; ed. Cranleigh, City and Guilds Coll., Imp. Coll. of Sci. and Technology; mil. serv., E. Africa, 1915-19; asst. elecl. engr., Tanganyika Territory, 1923.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1923 | asst. elecl. engr., Tanganyika Territory | Tanganyika | [1930, 1931] |

## Candidate stint `Finnis, A. H___Tanganyika___1924`

- Staff-list name: **Finnis, A. H** | colony: **Tanganyika** | listed 1924–1925 | editions [1924, 1925]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1924 | A. H. Finnis | Assistant Electrical Engineers | Electric Power Plant | — | — |
| 1925 | A. H. Finnis | Assistant Electrical Engineer | Electric Power Plant | — | — |

### Deterministic checks: `finnis_arthur-hornsby_b1889` vs `Finnis, A. H___Tanganyika___1924`

- [PASS] surname_gate: bio 'FINNIS' vs stint 'Finnis, A. H' (exact)
- [PASS] initials: bio ['A', 'H'] ~ stint ['A', 'H']
- [PASS] age_gate: stint starts 1924, birth 1889 (age 35)
- [PASS] colony: 1 placed event(s) resolve to 'Tanganyika'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1924-1925
- [FAIL] position_sim: best 52 vs bar 60: 'asst. elecl. engr., Tanganyika Territory' ~ 'Assistant Electrical Engineer'
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

