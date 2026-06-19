<!-- {"case_id": "case_hern_w-stanley_b1876", "bio_ids": ["hern_w-stanley_b1876"], "stint_ids": ["Hern, W. S___Lagos___1905"]} -->
# Dossier case_hern_w-stanley_b1876

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `hern_w-stanley_b1876`

- Printed name: **HERN, W. STANLEY**
- Birth year: 1876 (attested in editions [1907, 1908, 1909, 1910, 1911, 1912, 1913, 1914, 1915])
- Appears in editions: [1907, 1908, 1909, 1910, 1911, 1912, 1913, 1914, 1915]

### Verbatim printed entry text (OCR)

**Version `col1907-L44854.v` — printed in editions [1907, 1908, 1909, 1910, 1911, 1912, 1913, 1914, 1915]:**

> HERN, W. STANLEY.—B. 1876; lieut., Duke of Edinburgh's Wiltshire Regt.; served in Mashonaland rebellion, 1896-1897; in S. Africa, 1900-1902; with W.A.F.F., 1904-05; offr. comdgy. preventive service, Lagos, 1906; dist. comsrr., June, 1906; offr. comdgy. Ijebu Ode, 1906; dist. comsrr., Ikorodu and Sagamu, 1907.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1896–1897 | served in Mashonaland rebellion | — | [1907, 1908, 1909, 1910, 1911, 1912, 1913, 1914, 1915] |
| 1 | 1900–1902 | in S. Africa | — | [1907, 1908, 1909, 1910, 1911, 1912, 1913, 1914, 1915] |
| 2 | 1904–1905 | with W.A.F.F | — | [1907, 1908, 1909, 1910, 1911, 1912, 1913, 1914, 1915] |
| 3 | 1906 | offr. comdgy. preventive service | Lagos | [1907, 1908, 1909, 1910, 1911, 1912, 1913, 1914, 1915] |
| 4 | 1907 | dist. comsrr., Ikorodu and Sagamu | Lagos *(inherited from previous clause)* | [1907, 1908, 1909, 1910, 1911, 1912, 1913, 1914, 1915] |

## Candidate stint `Hern, W. S___Lagos___1905`

- Staff-list name: **Hern, W. S** | colony: **Lagos** | listed 1905–1906 | editions [1905, 1906]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1905 | W. S. Hern | Lieutenants | West African Frontier Force | — | — |
| 1906 | W. S. Hern | Lieutenants | West African Frontier Force | — | Lieutenant |

### Deterministic checks: `hern_w-stanley_b1876` vs `Hern, W. S___Lagos___1905`

- [PASS] surname_gate: bio 'HERN' vs stint 'Hern, W. S' (exact)
- [PASS] initials: bio ['W', 'S'] ~ stint ['W', 'S']
- [PASS] age_gate: stint starts 1905, birth 1876 (age 29)
- [PASS] colony: 2 placed event(s) resolve to 'Lagos'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1905-1906
- [FAIL] position_sim: best 24 vs bar 60: 'offr. comdgy. preventive service' ~ 'Lieutenants'
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

