<!-- {"case_id": "case_joubert_august-ernst-godfried_b1913", "bio_ids": ["joubert_august-ernst-godfried_b1913"], "stint_ids": ["Joubert, A. E___Northern Rhodesia___1949"]} -->
# Dossier case_joubert_august-ernst-godfried_b1913

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 8 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `joubert_august-ernst-godfried_b1913`

- Printed name: **JOUBERT, August Ernst Godfried**
- Birth year: 1913 (attested in editions [1951])
- Appears in editions: [1951]

### Verbatim printed entry text (OCR)

**Version `col1951-L39644.v` — printed in editions [1951]:**

> JOUBERT, August Ernst Godfried, B.A.—b. 1913; ed. Paarl Boys' High Sch. (1st cl. senr. cert.) and Rhodes Univ. Coll., Grahamstown; dip. educ.; on war serv., 1940-42, sergt. pilot, R.A.F.; mstr., European educ. dept., N. Rhod., 1937.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1937 | mstr., European educ. dept. | Northern Rhodesia | [1951] |

## Candidate stint `Joubert, A. E___Northern Rhodesia___1949`

- Staff-list name: **Joubert, A. E** | colony: **Northern Rhodesia** | listed 1949–1951 | editions [1949, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | A. E. Joubert | Master | Education | — | — |
| 1951 | A. E. Joubert | Master | Education | — | — |

### Deterministic checks: `joubert_august-ernst-godfried_b1913` vs `Joubert, A. E___Northern Rhodesia___1949`

- [PASS] surname_gate: bio 'JOUBERT' vs stint 'Joubert, A. E' (exact)
- [PASS] initials: bio ['A', 'E', 'G'] ~ stint ['A', 'E']
- [PASS] age_gate: stint starts 1949, birth 1913 (age 36)
- [PASS] colony: 1 placed event(s) resolve to 'Northern Rhodesia'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1949-1951
- [FAIL] position_sim: best 28 vs bar 60: 'mstr., European educ. dept.' ~ 'Master'
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

