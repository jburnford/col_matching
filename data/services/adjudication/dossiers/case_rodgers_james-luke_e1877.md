<!-- {"case_id": "case_rodgers_james-luke_e1877", "bio_ids": ["rodgers_james-luke_e1877"], "stint_ids": ["Rodgers, J___Malta___1909"]} -->
# Dossier case_rodgers_james-luke_e1877

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 7 official(s) with this surname in the graph's staff lists; 5 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `rodgers_james-luke_e1877`

- Printed name: **RODGERS, JAMES LUKE**
- Birth year: not printed
- Appears in editions: [1900, 1905, 1906]

### Verbatim printed entry text (OCR)

**Version `col1900-L36970.v` — printed in editions [1900, 1905]:**

> RODGERS, JAMES LUKE.—Joined the Leeward Is. pol., Nov., 1877; served in Antigua, Dominica, and Montserrat; corporal, Jan., 1888; ret., Nov., 1889; 3rd-cl. warder, Montserrat gaol, Dec., 1889; ag. gaoler, June, 1898.

**Version `col1906-L47706.v` — printed in editions [1906]:**

> RODGERS, JAMES LUKE.—JOINED THE LEEWARD IS. POL., NOV., 1877; SERVED IN ANTIGUA, DOMINICA, AND MONTSERRAT; CORPORAL, JAN., 1888; RES., NOV., 1889; 3RD CL. WARDER, MONTSERRAT GAOL, DEC., 1889; AG. GAOLER, JUNE, 1898.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1877 | Joined the Leeward Is. pol | — | [1900, 1905, 1906] |
| 1 | 1888 | corporal | — | [1900, 1905, 1906] |
| 2 | 1889 | ret | — | [1900, 1905] |
| 3 | 1889 | 3rd-cl. warder, Montserrat gaol | Montserrat | [1900, 1905, 1906] |
| 4 | 1889 | RES., NOV | — | [1906] |
| 5 | 1898 | ag. gaoler | Montserrat *(inherited from previous clause)* | [1900, 1905, 1906] |

## Candidate stint `Rodgers, J___Malta___1909`

- Staff-list name: **Rodgers, J** | colony: **Malta** | listed 1909–1912 | editions [1909, 1910, 1911, 1912]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1909 | J. Rodgers | Assistant Engineer | Electric Lighting Branch | — | — |
| 1910 | J. Rodgers | Assistant Engineer | Electric Lighting Branch | — | — |
| 1911 | J. Rodgers | Assistant Engineer | Electric Lighting Branch | — | — |
| 1912 | J. Rodgers | Assistant Engineer | Electric Lighting Branch | — | — |

### Deterministic checks: `rodgers_james-luke_e1877` vs `Rodgers, J___Malta___1909`

- [PASS] surname_gate: bio 'RODGERS' vs stint 'Rodgers, J' (exact)
- [PASS] initials: bio ['J', 'L'] ~ stint ['J']
- [PASS] age_gate: stint starts 1909; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Malta'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1909-1912
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

