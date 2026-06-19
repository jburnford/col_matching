<!-- {"case_id": "case_carew_w-s_e1874", "bio_ids": ["carew_w-s_e1874"], "stint_ids": ["Carew, Walter S___Fiji___1877"]} -->
# Dossier case_carew_w-s_e1874

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 20 official(s) with this surname in the graph's staff lists; 5 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `carew_w-s_e1874`

- Printed name: **CAREW, W. S**
- Birth year: not printed
- Appears in editions: [1889, 1890, 1894, 1896]

### Verbatim printed entry text (OCR)

**Version `col1889-L32186.v` — printed in editions [1889, 1890, 1894, 1896]:**

> CAREW, W. S.—Special agent to interior tribes of Viti Levu, Fiji, Nov., 1874; stipendiary magistrate, 1875; land titles commiss'nr, and member native regulations board, 1877; native lds. boundary commiss'nr., Nov., 1880; member ex. coun., Sept., 1882; is now res. comm'r., Colo. East, and stipendiary magistrate, Rewa.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1874 | Special agent to interior tribes of Viti Levu | Fiji | [1889, 1890, 1894, 1896] |
| 1 | 1875 | stipendiary magistrate | Fiji *(inherited from previous clause)* | [1889, 1890, 1894, 1896] |
| 2 | 1877 | land titles commiss'nr, and member native regulations board | Fiji *(inherited from previous clause)* | [1889, 1890, 1894, 1896] |
| 3 | 1880 | native lds. boundary commiss'nr | Fiji *(inherited from previous clause)* | [1889, 1890, 1894, 1896] |
| 4 | 1882 | member ex. coun | Fiji *(inherited from previous clause)* | [1889, 1890, 1894, 1896] |

## Candidate stint `Carew, Walter S___Fiji___1877`

- Staff-list name: **Carew, Walter S** | colony: **Fiji** | listed 1877–1897 | editions [1877, 1878, 1879, 1880, 1883, 1886, 1888, 1889, 1894, 1897]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | W. S. Carew | Stipendiary Magistrate | Civil Establishment | — | — |
| 1878 | Walter S. Carew | Stipendiary Magistrate | — | — | — |
| 1879 | Walter S. Carew | Stipendiary Magistrate | Civil Establishment | — | — |
| 1880 | Walter S. Carew | Stipendiary Magistrates | — | — | — |
| 1883 | W. S. Carew | Stipendiary Magistrate | Department of Justice | — | — |
| 1886 | W. S. Carew | Commissioner of Colo East | Department of Justice | — | — |
| 1888 | W. S. Carew | Commissioner of Colo East | DEPARTMENT OF JUSTICE | — | — |
| 1889 | W. S. Carew | Commissioner of Colo East | DEPARTMENT OF JUSTICE | — | — |
| 1894 | W. S. Carew | Commissioner of Colo East and Stipendiary Magistrate, Rewa | Department of Justice | — | — |
| 1897 | W. S. Carew | Commissioner of Colo East and Stipendiary Magistrate, Rewa | Department of Justice | — | — |

### Deterministic checks: `carew_w-s_e1874` vs `Carew, Walter S___Fiji___1877`

- [PASS] surname_gate: bio 'CAREW' vs stint 'Carew, Walter S' (exact)
- [PASS] initials: bio ['W', 'S'] ~ stint ['W', 'S']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [PASS] colony: 5 placed event(s) resolve to 'Fiji'
- [PASS] tenure_overlap: 4 event tenure(s) overlap stint years 1877-1897
- [PASS] position_sim: best 100 vs bar 60: 'stipendiary magistrate' ~ 'Commissioner of Colo East and Stipendiary Magistrate, Rewa'
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

