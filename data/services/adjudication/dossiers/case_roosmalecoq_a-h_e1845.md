<!-- {"case_id": "case_roosmalecoq_a-h_e1845", "bio_ids": ["roosmalecoq_a-h_e1845"], "stint_ids": ["Roosmalecocq, A. H___Ceylon___1877"]} -->
# Dossier case_roosmalecoq_a-h_e1845

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `roosmalecoq_a-h_e1845`

- Printed name: **ROOSMALECOQ, A. H**
- Birth year: not printed
- Appears in editions: [1883]

### Verbatim printed entry text (OCR)

**Version `col1883-L29314.v` — printed in editions [1883]:**

> ROOSMALECOQ, A. H.—Assistant commissioner of roads, Ceylon, 1845; assistant government agent, Galle, 1846; district judge of Tangalla, 1853; district judge, Trincomalee, 1862; ditto, Jaffna, 1869; acting district judge, Galle, May, 1873; confirmed, 1875.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1845 | Assistant commissioner of roads | Ceylon | [1883] |
| 1 | 1846 | assistant government agent, Galle | Ceylon *(inherited from previous clause)* | [1883] |
| 2 | 1853 | district judge of Tangalla | Ceylon *(inherited from previous clause)* | [1883] |
| 3 | 1862 | district judge, Trincomalee | Ceylon *(inherited from previous clause)* | [1883] |
| 4 | 1869 | ditto, Jaffna | Ceylon *(inherited from previous clause)* | [1883] |
| 5 | 1873 | acting district judge, Galle | Ceylon *(inherited from previous clause)* | [1883] |
| 6 | 1875 | confirmed | Ceylon *(inherited from previous clause)* | [1883] |

## Candidate stint `Roosmalecocq, A. H___Ceylon___1877`

- Staff-list name: **Roosmalecocq, A. H** | colony: **Ceylon** | listed 1877–1880 | editions [1877, 1878, 1879, 1880]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | A. H. Roosmalecocq | District Judge, Commissioner of Requests, Police Magistrate | District and Minor Courts | — | — |
| 1878 | A. H. Roosmalecocq | District Judge, Commissioner of Requests, Police Magistrate | District and Minor Courts | — | — |
| 1879 | A. H. Roosmalecocq | District Judge, Commissioner of Requests, Police Magistrate | Judicial Establishment | — | — |
| 1880 | A. H. Roosmalecocq | District Judge / Commissioner of Requests / Police Magistrate | District and Minor Courts | — | — |

### Deterministic checks: `roosmalecoq_a-h_e1845` vs `Roosmalecocq, A. H___Ceylon___1877`

- [PASS] surname_gate: bio 'ROOSMALECOQ' vs stint 'Roosmalecocq, A. H' (fuzzy:1)
- [PASS] initials: bio ['A', 'H'] ~ stint ['A', 'H']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [PASS] colony: 7 placed event(s) resolve to 'Ceylon'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1877-1880
- [FAIL] position_sim: best 21 vs bar 60: 'confirmed' ~ 'District Judge, Commissioner of Requests, Police Magistrate'
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

