<!-- {"case_id": "case_cousins_james_b1891", "bio_ids": ["cousins_james_b1891"], "stint_ids": ["Cousins, E. R. J. R___Kenya___1950"]} -->
# Dossier case_cousins_james_b1891

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 11 official(s) with this surname in the graph's staff lists; 8 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['cousins_james_b1891'] carry a single initial only — the namesake trap applies.

## Biography `cousins_james_b1891`

- Printed name: **COUSINS, James**
- Birth year: 1891 (attested in editions [1954])
- Honours: K.B.E, Kt. Bach (1950)
- Appears in editions: [1954]

### Verbatim printed entry text (OCR)

**Version `col1954-L20024.v` — printed in editions [1954]:**

> COUSINS, Sir James, K.B.E., Kt. Bach. (1950).—b. 1891; ed. Hampton Gram. Sch.; barrister, Middle Temple, 1913; in practice, G.C., 1913–44; prov. M.E.C., 1943; puisne judge, 1944; chmn., comtee. for constitutional reform, 1949; justice of appeal, W.A. ct. of appeal, G.C., 1952.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1913 | barrister, Middle Temple | — | [1954] |
| 1 | 1913–1944 | in practice | Gold Coast | [1954] |
| 2 | 1943 | prov. M.E.C | Gold Coast *(inherited from previous clause)* | [1954] |
| 3 | 1944 | puisne judge | Gold Coast *(inherited from previous clause)* | [1954] |
| 4 | 1949 | chmn., comtee. for constitutional reform | Gold Coast *(inherited from previous clause)* | [1954] |
| 5 | 1952 | justice of appeal, W.A. ct. of appeal | Gold Coast | [1954] |

## Candidate stint `Cousins, E. R. J. R___Kenya___1950`

- Staff-list name: **Cousins, E. R. J. R** | colony: **Kenya** | listed 1950–1951 | editions [1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1950 | E. R. J. R. Cousins | Special Commissioner and Acting Commissioner of Lands | Lands | — | — |
| 1951 | E. R. J. R. Cousins | Special Commissioner and Acting Commissioner of Lands | Lands | — | — |

### Deterministic checks: `cousins_james_b1891` vs `Cousins, E. R. J. R___Kenya___1950`

- [PASS] surname_gate: bio 'COUSINS' vs stint 'Cousins, E. R. J. R' (exact)
- [PASS] initials: bio ['J'] ~ stint ['E', 'R', 'J', 'R']
- [PASS] age_gate: stint starts 1950, birth 1891 (age 59)
- [FAIL] colony: no placed event resolves to 'Kenya'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1950-1951
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

