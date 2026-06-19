<!-- {"case_id": "case_harpur_isaac_b1885", "bio_ids": ["harpur_isaac_b1885"], "stint_ids": ["Harpur, I___Nyasaland___1919"]} -->
# Dossier case_harpur_isaac_b1885

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['harpur_isaac_b1885'] carry a single initial only — the namesake trap applies.

## Biography `harpur_isaac_b1885`

- Printed name: **HARPUR, ISAAC**
- Birth year: 1885 (attested in editions [1936, 1937])
- Honours: A.M.I.C.E
- Appears in editions: [1936, 1937]

### Verbatim printed entry text (OCR)

**Version `col1936-L61372.v` — printed in editions [1936, 1937]:**

> HARPUR, ISAAC, A.M.I.C.E., Chtd. Civ Engnr.—B. 1885; P.W.D., Nyasaland, 1917-20; ast. engrnr., P.W.D., F.M.S., Dec., 1920; ag. exec. engrnr., various occasions, 1923-29; exec. engrnr., div. pub. wks. office, Dec., 1929.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1917–1920 | P.W.D. | Nyasaland | [1936, 1937] |
| 1 | 1920 | ast. engrnr., P.W.D. | Federated Malay States | [1936, 1937] |
| 2 | 1923–1929 | ag. exec. engrnr., various occasions | Federated Malay States *(inherited from previous clause)* | [1936, 1937] |
| 3 | 1929 | exec. engrnr., div. pub. wks. office | Federated Malay States *(inherited from previous clause)* | [1936, 1937] |

## Candidate stint `Harpur, I___Nyasaland___1919`

- Staff-list name: **Harpur, I** | colony: **Nyasaland** | listed 1919–1920 | editions [1919, 1920]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1919 | I. Harpur | Assistant Engineer | Public Works Department | — | — |
| 1920 | I. Harpur | Assistant Engineer | Public Works Department | — | — |

### Deterministic checks: `harpur_isaac_b1885` vs `Harpur, I___Nyasaland___1919`

- [PASS] surname_gate: bio 'HARPUR' vs stint 'Harpur, I' (exact)
- [PASS] initials: bio ['I'] ~ stint ['I']
- [PASS] age_gate: stint starts 1919, birth 1885 (age 34)
- [PASS] colony: 1 placed event(s) resolve to 'Nyasaland'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1919-1920
- [FAIL] position_sim: no overlapping placed event to compare
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

