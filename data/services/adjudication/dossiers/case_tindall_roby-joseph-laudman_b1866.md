<!-- {"case_id": "case_tindall_roby-joseph-laudman_b1866", "bio_ids": ["tindall_roby-joseph-laudman_b1866"], "stint_ids": ["Tindall, R. J. L___South Africa___1912"]} -->
# Dossier case_tindall_roby-joseph-laudman_b1866

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 4 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `tindall_roby-joseph-laudman_b1866`

- Printed name: **TINDALL, ROBY JOSEPH LAUDMAN**
- Birth year: 1866 (attested in editions [1921])
- Appears in editions: [1921]

### Verbatim printed entry text (OCR)

**Version `col1921-L60453.v` — printed in editions [1921]:**

> TINDALL, ROBY JOSEPH LAUDMAN, B.A. (Cape).—B. 1866; ed. Paarl, Stellenbosch and Cape Town; barrister, Middle Temple, 1907; conveyancer, Transvaal, 1907; asst. crown prosecutor, 1908; crown prosecutor, W.W. Rand local divn. (Johannesburg) sup.cl., 1914.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1907 | barrister, Middle Temple | — | [1921] |
| 1 | 1907 | conveyancer | Transvaal | [1921] |
| 2 | 1908 | asst. crown prosecutor | Transvaal *(inherited from previous clause)* | [1921] |
| 3 | 1914 | crown prosecutor, W.W. Rand local divn. (Johannesburg) sup.cl | Transvaal *(inherited from previous clause)* | [1921] |

## Candidate stint `Tindall, R. J. L___South Africa___1912`

- Staff-list name: **Tindall, R. J. L** | colony: **South Africa** | listed 1912–1918 | editions [1912, 1914, 1918]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1912 | R. J. L. Tindall | Assistant Crown Prosecutor | Supreme Court of South Africa | — | — |
| 1914 | R. J. L. Tindall | Assistant Crown Prosecutor | Witwatersrand Local Division | — | — |
| 1918 | R. J. L. Tindall | Crown Prosecutor | Witwatersrand Local Division | — | — |

### Deterministic checks: `tindall_roby-joseph-laudman_b1866` vs `Tindall, R. J. L___South Africa___1912`

- [PASS] surname_gate: bio 'TINDALL' vs stint 'Tindall, R. J. L' (exact)
- [PASS] initials: bio ['R', 'J', 'L'] ~ stint ['R', 'J', 'L']
- [PASS] age_gate: stint starts 1912, birth 1866 (age 46)
- [FAIL] colony: no placed event resolves to 'South Africa'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1912-1918
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

