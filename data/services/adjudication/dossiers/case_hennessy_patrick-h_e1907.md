<!-- {"case_id": "case_hennessy_patrick-h_e1907", "bio_ids": ["hennessy_patrick-h_e1907"], "stint_ids": ["Hennessy, P.H___Straits Settlements___1931"]} -->
# Dossier case_hennessy_patrick-h_e1907

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 6 official(s) with this surname in the graph's staff lists; 4 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `hennessy_patrick-h_e1907`

- Printed name: **HENNESSY, PATRICK H.**
- Birth year: not printed
- Appears in editions: [1911, 1919, 1921, 1923, 1924]

### Verbatim printed entry text (OCR)

**Version `col1919-L53014.v` — printed in editions [1919, 1921, 1923, 1924]:**

> HENNESSY, PATRICK H.—M.R.C.S. (Eng.), L.R.C.P. (Lond.); house surg., S. Sttlmte., Feb., 1907; supernumerary med. offr., Penang, Feb., 1908; med. offr., gen. hosp., Singapore, 1st May, 1908; ag. med. offr., Malacca, 14th Oct., 1908; med. offr., grade II, Kuala Pilah, and med. offr., rly. construction, 1st Apr., 1909; ag. med. offr., grade I, 6th May, 1914; ag. senr. med. offr., Selangor, 2nd to 26th Nov., 1918, in addition, and again 3rd Dec., 1918 to 9th Feb., 1919, and from 9th Apr. to 23rd Dec., 1919; ophthalmologist physician in addition; med. offr., gen. hosp., K. Lumpur, 1st Sept., 1920.

**Version `col1911-L45420.v` — printed in editions [1911]:**

> HENNESSY, PATRICK H.—M.R.C.S. (Eng.), L.R.C.P. (Loud.) house surg., S. Sttlmts., Feb., 1907; supernumerary med. offr., Penang, Feb., 1908.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1907–1907 | house surg. | Straits Settlements | [1911, 1919, 1921, 1923, 1924] |
| 1 | 1908–1908 | supernumerary med. offr. | Penang | [1911, 1919, 1921, 1923, 1924] |
| 2 | 1908–1908 | med. offr., gen. hosp. | Singapore | [1919, 1921, 1923, 1924] |
| 3 | 1909–1909 | med. offr., grade II, and med. offr., rly. construction | Kuala Pilah | [1919, 1921, 1923, 1924] |
| 4 | 1914–1914 | ag. med. offr., grade I | — | [1919, 1921, 1923, 1924] |
| 5 | 1918–1919 | ag. senr. med. offr. | Selangor | [1919, 1921, 1923, 1924] |
| 6 | 1920–1920 | med. offr., gen. hosp. | Kuala Lumpur | [1919, 1921, 1923, 1924] |

## Candidate stint `Hennessy, P.H___Straits Settlements___1931`

- Staff-list name: **Hennessy, P.H** | colony: **Straits Settlements** | listed 1931–1932 | editions [1931, 1932]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1931 | P. H. Hennessy | Medical Officer and Ophthalmic Surgeon | Medical | — | — |
| 1932 | P. H. Hennessy | Medical Officer and Ophthalmic Surgeon | Medical | — | — |
| 1932 | P.H. Hennessy | Medical Officer and Ophthalmic Surgeon | Medical | — | — |

### Deterministic checks: `hennessy_patrick-h_e1907` vs `Hennessy, P.H___Straits Settlements___1931`

- [PASS] surname_gate: bio 'HENNESSY' vs stint 'Hennessy, P.H' (exact)
- [PASS] initials: bio ['P', 'H'] ~ stint ['P', 'H']
- [PASS] age_gate: stint starts 1931; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Straits Settlements'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1931-1932
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

