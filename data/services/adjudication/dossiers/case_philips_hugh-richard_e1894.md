<!-- {"case_id": "case_philips_hugh-richard_e1894", "bio_ids": ["philips_hugh-richard_e1894"], "stint_ids": ["Philips, H. R___Hong Kong___1925"]} -->
# Dossier case_philips_hugh-richard_e1894

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 9 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Philips, H. R___Hong Kong___1925` is also gate-compatible with biography(ies) outside this case: ['phelips_hugh-richard_e1894'] (already linked elsewhere or filtered).

## Biography `philips_hugh-richard_e1894`

- Printed name: **PHILIPS, HUGH RICHARD**
- Birth year: not printed
- Appears in editions: [1909, 1911, 1913, 1915]

### Verbatim printed entry text (OCR)

**Version `col1913-L48668.v` — printed in editions [1913, 1915]:**

> PHILIPS, HUGH RICHARD.—Ed. Weymouth Coll. and Queen's Coll., Oxford; local auditor, Niger Coast Prot., 27th Oct., 1894; asst. auditor, E. Africa Prot., 9th Dec., 1896; local auditor, Uganda, 29th Apr., 1897; served in Uganda mutiny (medal and clasp); local auditor, E. Africa and Uganda rly., 26th Dec., 1901; local auditor, Hong Kong, 1st Nov., 1904; J.P., 1905; hon. auditor, Hong Kong Univ., 2nd May, 1911.

**Version `col1909-L48989.v` — printed in editions [1909]:**

> PHILIPS, Hugh Richard.—Ed. Warrn Coll. and Queen's Coll., Oxford; local aud. Niger Coast Prot., 27th Oct., 1894; asst. aud. E. Africa Prot., 9th Dec., 1896; local aud. Uganda, 29th Apr., 1897; served in Usumutiny (medal and clasp); local auditer, Africa, 26th Dec., 1901; local auditer, H. Kong, 1st Nov., 1904; J.P., 1905.

**Version `col1911-L47290.v` — printed in editions [1911]:**

> PHILIPS, HUGH RICHARD.—Ed. Weymouth Coll. and Queen's Coll., Oxford; local auditor, Niger Coast Prot., 27th Oct., 1894; asst. auditor, E. Africa and Uganda rly., 26th Dec., 1901; local auditor, Hong Kong, 1st Nov., 1904; J.P., 1905.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1894 | local auditor, Niger Coast Prot | — | [1909, 1911, 1913, 1915] |
| 1 | 1896 | asst. auditor, E. Africa Prot | — | [1909, 1913, 1915] |
| 2 | 1897 | local auditor | Uganda | [1913, 1915] |
| 3 | 1897 | local aud. Uganda | — | [1909] |
| 4 | 1901 | local auditor, E. Africa and Uganda rly | Uganda *(inherited from previous clause)* | [1909, 1911, 1913, 1915] |
| 5 | 1904 | local auditor | Hong Kong | [1911, 1913, 1915] |
| 6 | 1904 | local auditer, H. Kong | — | [1909] |
| 7 | 1905 | J.P | Hong Kong *(inherited from previous clause)* | [1909, 1911, 1913, 1915] |
| 8 | 1911 | hon. auditor, Hong Kong Univ | Hong Kong | [1913, 1915] |

## Candidate stint `Philips, H. R___Hong Kong___1925`

- Staff-list name: **Philips, H. R** | colony: **Hong Kong** | listed 1925–1928 | editions [1925, 1928]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1925 | H. R. Philips | Auditor | Audit Department (under the Director of Colonial Audit, London) | — | — |
| 1928 | H. R. Philips | Auditor | Audit Department | — | — |

### Deterministic checks: `philips_hugh-richard_e1894` vs `Philips, H. R___Hong Kong___1925`

- [PASS] surname_gate: bio 'PHILIPS' vs stint 'Philips, H. R' (exact)
- [PASS] initials: bio ['H', 'R'] ~ stint ['H', 'R']
- [PASS] age_gate: stint starts 1925; no printed birth year — UNCHECKED
- [PASS] colony: 3 placed event(s) resolve to 'Hong Kong'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1925-1928
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

