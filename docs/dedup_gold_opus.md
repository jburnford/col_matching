# Opus-adjudicated dedup gold (20 clusters) — DeepSeek A/B validation set

Use this to test whether a cheaper model (DeepSeek etc.) reproduces Opus's
decisions BEFORE handing it the full ~2,090-cluster backlog. Agreement on these
20 (especially the non-merges and the discipline case) is the bar.

## Regenerate the EXACT dossiers Opus saw
The 7 merges have since collapsed those clusters, so revert pass F first:
```bash
cd ~/col_matching && export COL_USE_AUGMENTED=1 PYTHONHASHSEED=0
COL_NO_LLM_DEDUP=1 python3 -m col_match.services.cli compile   # pre-LLM-dedup bios
python3 dedup_review.py --limit 12 --min 2 --max 2 --ignore-ledger   # = BATCH 1 below
python3 dedup_review.py --limit 8  --min 3 --max 5 --ignore-ledger   # = BATCH 2 below
# ...feed each CLUSTER dossier + docs/DEDUP_LLM_METHOD.md rules to DeepSeek; compare to gold.
python3 -m col_match.services.cli compile   # restore (ledger/pass F active again)
```
Score = (merge groups match) AND (non-merges match). A FALSE merge by DeepSeek is
a hard fail (prime directive); a missed merge is a soft fail (recoverable).

## BATCH 1 — `--limit 12 --min 2 --max 2` (size-2 clusters), Opus verdicts
| # | surnames | verdict | merged versions |
|--|--|--|--|
| 1 | A'BECKETT / BECKETT (Thomas) | **no-merge** | — (b.1836 Victoria judge vs b.1898 Nigeria engineer) |
| 2 | AANENSEN / JANSEN (Ernest) | **no-merge** | — (Fenelon Trinidad CS vs George SA politician) |
| 3 | ABBOTT / IBBOTT (John) | **no-merge** | — (Myles John HK judge vs John Thomas 1860s Demerara) |
| 4 | ABERDEEN | **MERGE** | col1915-L44759.v, col1898-L31850.v |
| 5 | ABERY / CARBERY (Joseph) | **MERGE** | col1897-L31192.v, col1886-L32542.v |
| 6 | ABRAHAM / GRAHAM (Charles) | **no-merge** | — |
| 7 | ABRAMS / MIRAMS (Arthur) | **no-merge** | — |
| 8 | ABRAMSON / HYAMSON (Albert) | **no-merge** | — (Transjordan vs Palestine) |
| 9 | ACARLTHUR / McARTHUR (Malcolm Stewart) | **MERGE** | col1897-L33128.v, col1906-L46700.v, col1923-L56228.v, col1898-L34555.v |
| 10 | ADAMS (Alexander Samuel / Robert Patton) | **no-merge** | — |
| 11 | ADAMS (Ernest / Ernest Victor) | **no-merge** | — |
| 12 | ADAMS (Philip Francis Burnett b.1864 / Phillip Francis b.1914) | **no-merge** | — (likely father/son) |

## BATCH 2 — `--limit 8 --min 3 --max 5` (size-3 clusters), Opus verdicts
| # | surnames | verdict | merged versions |
|--|--|--|--|
| 1 | ABRAHAM / GRAHAM (Alexander) | **no-merge (all 3 distinct)** | — **DISCIPLINE CASE**: two "Alexander Graham" b.1896/1897 kept apart (marine A.M.I.N.A vs land M.I.S.W.A surveyor) |
| 2 | ACKROYD / HOLROYD | **MERGE the 2 Ackroyd; Holroyd separate** | col1883-L26129.v, col1899-L33336.v, col1898-L31854.v |
| 3 | ADAMS (Theodore/Thoroder Samuel; Alexander Samuel) | **MERGE Theodore+Thoroder; Alexander separate** | col1922-L50213.v, col1932-L57887.v |
| 4 | ADAMS (George P ×2; Wilfrid George) | **MERGE the 2 George P; Wilfrid separate** | col1886-L31826.v, col1888-L31734.v |
| 5 | ADAMSON / SIMSON / THOMSON (John) | **no-merge** | — (coincidental "John") |
| 6 | AGOSTINI / CELESTINI (Louis) | **no-merge** | — (3 distinct Louis) |
| 7 | AITKEN / ATTKEN (Colquhoun; Eric) | **MERGE the 2 C. Colquhoun; Eric separate** | col1886-L31849.v, col1898-L31881.v |
| 8 | AKERMANN / KAUFMANN / WARMANN | **no-merge** | — |

Totals: **7 merge decisions, 13 non-merge decisions.** The hardest tests are
Batch-2 #1 (must NOT merge same-name/adjacent-birth) and the partial-merge clusters
(#2/#3/#4/#7 — merge a subset, keep the namesake separate).

---

# SESSION 2 (2026-06-17b) — 52 more clusters (22 merge, 30 no-merge)

**Authoritative machine-diffable record:** `data/services/dedup/dedup_decisions_opus.jsonl`
— one line per cluster: `{session, cluster:[sorted bio_ids], verdict:"merge"|"no_merge", reason}`.
This is the file to diff DeepSeek against (the 22 merges are also in the pass-F ledger
`data/services/dedup/llm_merges.jsonl`; the 30 **no_merge** decisions exist ONLY here).

Score = for every cluster, DeepSeek's verdict == Opus's verdict. A **false merge**
(DeepSeek merges an Opus `no_merge`) is a HARD fail. A missed merge is a soft fail.

## Hardest tests in this set (DeepSeek must get these right)
- **angelo_e-fox** / **arnott_sandford**: careerless edition fragment with the *same
  distinctive name* but NO honour/event → Opus kept them **separate** (name alone is not
  enough). Contrast **archibald_adams-g** (careerless fragment shares the C.M.G. honour →
  **merged**) and **allan_gordon / angus_wm** (careerless-ish prefix-extension fragments with
  an identical dated event → **merged**). DeepSeek must learn: fragment needs a discriminator.
- **armstrong_robert b.1879 vs b.1906**: identical name, but divergent birth + disjoint
  career/education → **no_merge** (the same-name discipline case, like Alexander Graham).
- **aplin** Charles Edward vs Harold D'Auvergne: shared distinctive middle name (brothers) but
  different forenames → **no_merge**.
- Dropped-initial OCR surname merges DeepSeek must catch: An Buren=Van Buren, An de Velde=
  Van de Velde, Anderkoen=Vanderkoen, Andolo=Dandolo, Apper=Capper, Arkes=Parkes,
  Arley=Darley, Awcett=Fawcett — each has an IDENTICAL career confirming the merge.
- **anderson_maxwell-hendry = maxwell-anderson**: surname recorded with/without hyphenated
  prefix; identical career + honours → **merge**.

## Regenerate the EXACT dossiers Opus saw (these clusters were pulled AFTER Session-1 merges)
Session-2 was adjudicated with the 13 Session-1 merges applied but BEFORE the 22 Session-2
merges. To reproduce, revert ONLY Session-2's ledger lines:
```bash
cd ~/col_matching && export COL_USE_AUGMENTED=1 PYTHONHASHSEED=0
head -13 data/services/dedup/llm_merges.jsonl > /tmp/ledger_s1.jsonl     # Session-1 ledger
cp data/services/dedup/llm_merges.jsonl /tmp/ledger_full.jsonl           # backup full
cp /tmp/ledger_s1.jsonl data/services/dedup/llm_merges.jsonl
python3 -m col_match.services.cli compile                                # Session-1 state
python3 dedup_review.py --limit 50 --min 2 --max 3 --ignore-ledger       # pull 1 (clusters 1-50)
python3 dedup_review.py --limit 48 --min 2 --max 3 --ignore-ledger       # pull 2/3 (clusters past Archibald)
#   feed each NEW cluster dossier + docs/DEDUP_LLM_METHOD.md rules to DeepSeek;
#   diff its verdict per bio-id cluster against data/services/dedup/dedup_decisions_opus.jsonl
cp /tmp/ledger_full.jsonl data/services/dedup/llm_merges.jsonl           # RESTORE full ledger
python3 -m col_match.services.cli compile                                # restore pass-F state
```
(Session-2's new clusters are the alphabetical run AINLEY → BABBI; clusters before AINLEY in
the pull are Session-1 non-merges that recur because non-merges are never ledgered.)

---

# DeepSeek A/B RESULT (2026-06-17b) — deepseek/deepseek-v4-pro vs Opus

Harness: `deepseek_dedup_ab.py` (capped/ledgered OpenRouter client, key in `.env`).
Replayed all 52 Session-2 clusters in Session-1 compiled state; verdicts diffed against
`dedup_decisions_opus.jsonl`. Output: `data/services/dedup/deepseek_ab_results.jsonl`,
spend ledger `deepseek_ab_spend.jsonl`.

**Result: 50/51 agreement (98%). FALSE MERGES = 0. Missed merges = 1 (soft). 0 errors.**
(1 of 52 clusters — ainley/mckinley — was unresolvable to an exact component in the
current compile and skipped; it is a clear no_merge.) Spend $0.19 total (both runs;
deepseek-v4-pro is a reasoning model — needs max_output_tokens>=3000 or the JSON truncates).

- **0 false merges** on all 30 no_merge clusters incl. the hard ones: Armstrong Robert
  b.1879≠b.1906 (same-name divergent), Aplin D'Auvergne brothers, Angelo/Arnott careerless
  name-only fragments, Arthur≠McArthur. This is the prime-directive bar — PASSED.
- DeepSeek reproduced all 8 dropped-initial OCR-surname merges, Anderson=Maxwell-Anderson,
  Archibald (careerless fragment WITH shared C.M.G.), Athill (Junr same-person).
- **Only miss:** `archer_clyde` Harcourt/Hargouet — Opus MERGED (same Clyde Vernon Archer
  b.1904, Harrison Coll, OCR middle-name variant, teaching→law phases); DeepSeek declined
  because the two fragments share NO dated career event. A conservative (safe-direction)
  miss on the single borderline merge that rests on name+birth+school rather than a shared event.

**Verdict: deepseek-v4-pro is safe to hand volume** — it does not false-merge, and its only
divergence is to under-merge a borderline case (recoverable). Keep a 2nd-pass verifier on its
proposed merges anyway (the eval_known gate is necessary but not sufficient for non-gold merges).
Use max_output_tokens>=3000. NO GEMINI.
