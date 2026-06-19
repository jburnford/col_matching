<!-- {"case_id": "case_mattetti_charles_e1891", "bio_ids": ["mattetti_charles_e1891"], "stint_ids": ["Mattei, Charles___Malta___1908"]} -->
# Dossier case_mattetti_charles_e1891

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['mattetti_charles_e1891'] carry a single initial only — the namesake trap applies.
- Phase 1 found `mattetti_charles_e1891` ↔ `Mattei, Charles___Malta___1908` passed its evidence bar but dropped it as ambiguous (a comparable-strength competitor existed).
- NOTE: stint `Mattei, Charles___Malta___1908` is also gate-compatible with biography(ies) outside this case: ['mattei_charles_e1891'] (already linked elsewhere or filtered).

## Biography `mattetti_charles_e1891`

- Printed name: **MATTETTI, CHARLES**
- Birth year: not printed
- Honours: D.P.H, L.F.P.S.G, L.M
- Appears in editions: [1922]

### Verbatim printed entry text (OCR)

**Version `col1922-L54619.v` — printed in editions [1922]:**

> MATTETTI, CHARLES, L.R.C.P. (Edin.), L.R.C.S. (Edin.), L.M., L.F.P.S.G., D.P.H.—Capt., Australian army medical corps, reserve of offrs.; med. offr., N. S. Wales, 1891; ditto, W. Australia, 1897; gov't med. offr., quarantine med. offr., res. mag., chmn. of quarter sess., chmn. of local ct., W. Australia, 1899; med. offr., Imperial Tasmanian cont.; S. African war, 1900 (medal and Cape Col. clasp); sec. for permits, East London, S. Africa, 1902; med. offr. in charge of new constructions, C.S.A.R., 1903; med. offr. of health, Malta, 1907.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1891 | med. offr., N. S. Wales | Nova Scotia | [1922] |
| 1 | 1897 | ditto, W. Australia | Nova Scotia *(inherited from previous clause)* | [1922] |
| 2 | 1899 | gov't med. offr., quarantine med. offr., res. mag., chmn. of quarter sess., chmn. of local ct., W. Australia | Nova Scotia *(inherited from previous clause)* | [1922] |
| 3 | 1900 | S. African war | Nova Scotia *(inherited from previous clause)* | [1922] |
| 4 | 1902 | sec. for permits, East London, S. Africa | Nova Scotia *(inherited from previous clause)* | [1922] |
| 5 | 1903 | med. offr. in charge of new constructions, C.S.A.R | Nova Scotia *(inherited from previous clause)* | [1922] |
| 6 | 1907 | med. offr. of health | Malta | [1922] |

## Candidate stint `Mattei, Charles___Malta___1908`

- Staff-list name: **Mattei, Charles** | colony: **Malta** | listed 1908–1914 | editions [1908, 1909, 1911, 1912, 1914]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1908 | Charles Mattei | Medical Officer of Health | Sanitary Branch | — | — |
| 1909 | Charles Mattei | Medical Officer of Health | Sanitary Branch | — | — |
| 1911 | Charles Mattei | Medical Officer of Health | Sanitary Branch | — | — |
| 1912 | Charles Mattei | Medical Officer of Health | Sanitary Branch | — | — |
| 1914 | Charles Mattei | Medical Officer of Health | Sanitary Branch | — | — |

### Deterministic checks: `mattetti_charles_e1891` vs `Mattei, Charles___Malta___1908`

- [PASS] surname_gate: bio 'MATTETTI' vs stint 'Mattei, Charles' (fuzzy:2)
- [PASS] initials: bio ['C'] ~ stint ['C']
- [PASS] age_gate: stint starts 1908; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Malta'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1908-1914
- [PASS] position_sim: best 84 vs bar 60: 'med. offr. of health' ~ 'Medical Officer of Health'
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

