<!-- {"case_id": "case_isaac_charles-powys_e1890", "bio_ids": ["isaac_charles-powys_e1890"], "stint_ids": ["Isaac, C. P___South Africa___1908"]} -->
# Dossier case_isaac_charles-powys_e1890

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 6 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `isaac_charles-powys_e1890`

- Printed name: **ISAAC, CHARLES POWYS**
- Birth year: not printed
- Appears in editions: [1906, 1907, 1908, 1909, 1910, 1911, 1912, 1913, 1914, 1915]

### Verbatim printed entry text (OCR)

**Version `col1906-L46220.v` — printed in editions [1906, 1907, 1908, 1909, 1910, 1911, 1913, 1914, 1915]:**

> ISAAC, CHARLES POWYS.—Clk., col. branch, ex. and audit dep., Aug., 1890; clk. in charge of accnts., Jan., 1894; detached for service as loc. auditor, Uganda Prot., June, 1896, to Sept., 1897; and again as loc. audr., N. Nig., May, 1900, to Aug., 1901; prin. clk., Transvaal aud. off., Apr., 1902; asst. aud.-gen., Transvaal, Feb., 1903; aud. to I.C.C., S. Africa, Oct., 1904; asst. auditor-gen., Union of S. Africa, 1910.

**Version `col1912-L45155.v` — printed in editions [1912]:**

> ISAAC, CHARLES POWYS.—Cltk., coll. ex. and audit dep., Aug., 1890; clk. in acct., Jan., 1894; detached for service auditor, Uganda Prot., June, 1895, to Sept., and again as loc. audr., N. Nig., May, 1901; prin. clk., Transvaal aud. offr., Ass. ass. aud.-gen., Transvaal, Feb., 1903; I.C.C., S. Africa, Oct., 1904; ass. aud. Union of S. Africa, 1910.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1890 | Clk., col. branch, ex. and audit dep. | — | [1906, 1907, 1908, 1909, 1910, 1911, 1912, 1913, 1914, 1915] |
| 1 | 1894 | clk. in charge of accnts. | — | [1906, 1907, 1908, 1909, 1910, 1911, 1913, 1914, 1915] |
| 2 | 1894 | clk. in acct. | — | [1912] |
| 3 | 1895–1895 | service auditor | Uganda Protectorate | [1912] |
| 4 | 1896–1897 | loc. auditor | Uganda Protectorate | [1906, 1907, 1908, 1909, 1910, 1911, 1913, 1914, 1915] |
| 5 | 1900–1901 | loc. audr. | Northern Nigeria | [1906, 1907, 1908, 1909, 1910, 1911, 1913, 1914, 1915] |
| 6 | 1901 | loc. audr. | Northern Nigeria | [1912] |
| 7 | 1902 | prin. clk. | Transvaal | [1906, 1907, 1908, 1909, 1910, 1911, 1913, 1914, 1915] |
| 8 | 1903 | asst. aud.-gen. | Transvaal | [1906, 1907, 1908, 1909, 1910, 1911, 1912, 1913, 1914, 1915] |
| 9 | 1904 | aud. to I.C.C. | South Africa | [1906, 1907, 1908, 1909, 1910, 1911, 1912, 1913, 1914, 1915] |
| 10 | 1910 | asst. auditor-gen. | Union of South Africa | [1906, 1907, 1908, 1909, 1910, 1911, 1913, 1914, 1915] |
| 11 | 1910 | ass. aud. | South Africa | [1912] |

## Candidate stint `Isaac, C. P___South Africa___1908`

- Staff-list name: **Isaac, C. P** | colony: **South Africa** | listed 1908–1914 | editions [1908, 1912, 1914]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1908 | C. P. Isaac | Auditor to the Inter-Colonial Council | Inter-Colonial Council | — | — |
| 1912 | C. P. Isaac | Assistant Controller and Auditor-General | Control and Audit Office | — | — |
| 1914 | C. P. Isaac | Assistant Controller and Auditor-General | Assistant Controller and Auditor-General's Department | — | — |

### Deterministic checks: `isaac_charles-powys_e1890` vs `Isaac, C. P___South Africa___1908`

- [PASS] surname_gate: bio 'ISAAC' vs stint 'Isaac, C. P' (exact)
- [PASS] initials: bio ['C', 'P'] ~ stint ['C', 'P']
- [PASS] age_gate: stint starts 1908; no printed birth year — UNCHECKED
- [PASS] colony: 2 placed event(s) resolve to 'South Africa'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1908-1914
- [FAIL] position_sim: best 39 vs bar 60: 'aud. to I.C.C.' ~ 'Auditor to the Inter-Colonial Council'
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

