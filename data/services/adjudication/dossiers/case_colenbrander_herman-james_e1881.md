<!-- {"case_id": "case_colenbrander_herman-james_e1881", "bio_ids": ["colenbrander_herman-james_e1881"], "stint_ids": ["Colenbrander, H. J___Natal___1905"]} -->
# Dossier case_colenbrander_herman-james_e1881

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 4 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Colenbrander, H. J___Natal___1905` is also gate-compatible with biography(ies) outside this case: ['colenbrander_herman-james_b1863'] (already linked elsewhere or filtered).

## Biography `colenbrander_herman-james_e1881`

- Printed name: **COLENBRANDER, HERMAN JAMES**
- Birth year: not printed
- Appears in editions: [1888]

### Verbatim printed entry text (OCR)

**Version `col1888-L32727.v` — printed in editions [1888]:**

> COLENBRANDER, HERMAN JAMES.—Clerk for Immigration purposes, Zulu Border Agency, Lower Tugela Division, Natal, Nov., 1881.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1881 | Clerk for Immigration purposes, Zulu Border Agency, Lower Tugela Division | Natal | [1888] |

## Candidate stint `Colenbrander, H. J___Natal___1905`

- Staff-list name: **Colenbrander, H. J** | colony: **Natal** | listed 1905–1910 | editions [1905, 1907, 1910]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1905 | H. J. Colenbrander | Magistrate | Native High Court | — | — |
| 1907 | H. J. Colenbrander | Assistant Magistrate | Magistrates | — | — |
| 1910 | H. J. Colenbrander | Magistrate | Magistrates | — | — |

### Deterministic checks: `colenbrander_herman-james_e1881` vs `Colenbrander, H. J___Natal___1905`

- [PASS] surname_gate: bio 'COLENBRANDER' vs stint 'Colenbrander, H. J' (exact)
- [PASS] initials: bio ['H', 'J'] ~ stint ['H', 'J']
- [PASS] age_gate: stint starts 1905; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Natal'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1905-1910
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

