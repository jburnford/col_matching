<!-- {"case_id": "case_packer_stanley_b1878", "bio_ids": ["packer_stanley_b1878"], "stint_ids": ["Packer, S___Uganda___1911"]} -->
# Dossier case_packer_stanley_b1878

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 11 official(s) with this surname in the graph's staff lists; 5 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['packer_stanley_b1878'] carry a single initial only — the namesake trap applies.

## Biography `packer_stanley_b1878`

- Printed name: **PACKER, STANLEY**
- Birth year: 1878 (attested in editions [1914, 1915])
- Appears in editions: [1914, 1915]

### Verbatim printed entry text (OCR)

**Version `col1914-L49001.v` — printed in editions [1914, 1915]:**

> PACKER, STANLEY.—B. 1878; ed. Dulwich Coll. and Worcester Coll., Oxford, B.A.; Middle Temple, 1902; asst. sec. Bankers' Institute, 1905-7; called to the bar, 1908; dist. mag., Kampala, Uganda Prot., July, 1910; ag. dist. mag., Entebbe, adminstr.-gen., principal regar. of documents, regar. of companies and offi. recr. in bankruptcy, Dec., 1910 to Sept., 1912, and from Apl. to Nov., 1913; ag. crown advoc., Uganda Prot., Dec., 1910, to Nov., 1911.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1902–1902 | Middle Temple | — | [1914, 1915] |
| 1 | 1905–1907 | asst. sec. Bankers' Institute | — | [1914, 1915] |
| 2 | 1908–1908 | called to the bar | — | [1914, 1915] |
| 3 | 1910–1910 | dist. mag., Kampala | Uganda Protectorate | [1914, 1915] |
| 4 | 1910–1913 | ag. dist. mag., Entebbe, adminstr.-gen., principal regar. of documents, regar. of companies and offi. recr. in bankruptcy | — | [1914, 1915] |

## Candidate stint `Packer, S___Uganda___1911`

- Staff-list name: **Packer, S** | colony: **Uganda** | listed 1911–1915 | editions [1911, 1912, 1913, 1914, 1915]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1911 | S. Packer | Magistrate | Judicial | — | — |
| 1912 | S. Packer | Magistrate | Judicial | — | — |
| 1913 | S. Packer | Magistrate | Judicial | — | — |
| 1914 | S. Packer | Magistrate | Judicial | — | — |
| 1915 | S. Packer | Magistrate | Judicial | — | — |

### Deterministic checks: `packer_stanley_b1878` vs `Packer, S___Uganda___1911`

- [PASS] surname_gate: bio 'PACKER' vs stint 'Packer, S' (exact)
- [PASS] initials: bio ['S'] ~ stint ['S']
- [PASS] age_gate: stint starts 1911, birth 1878 (age 33)
- [PASS] colony: 1 placed event(s) resolve to 'Uganda'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1911-1915
- [FAIL] position_sim: best 31 vs bar 60: 'dist. mag., Kampala' ~ 'Magistrate'
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

