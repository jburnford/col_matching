# Within-volume bio↔roster linking on the new (Infinity-2) OCR — pilot + handoff

**Goal.** Set the old cross-edition pipeline aside and test, inside a *single*
edition, whether we can link services-section **biographies** to that same
edition's by-colony **staff-list (roster) records** — both come from the same
document, so a bio clause ("cadet, Ceylon civ. ser., 1893") should resolve to
that volume's Ceylon establishment. Everything is grounded to the raw-OCR
block by a provenance key `(edition_year, page, block, bbox)`.

## What was built (this machine, deterministic — no LLM)

New isolated package `col_match/volume/` (the old `col_match/services/` pipeline
is untouched; helpers are reused by import only):

| file | role |
|--|--|
| `reader.py` | load `…/plato/colonial_office_lists/json/<Doc><YEAR>.pdf/result.json` → reading-ordered `Block`s with provenance |
| `bios.py` | find "RECORD OF (THE PUBLIC) SERVICES", segment one bio per text block by intact headword, parse via `services.rules_parse` |
| `roster.py` | walk colony sections (running `header`=colony, `title`=dept), parse `Position, Name, salary.` (and late-era `Position—Name.`) records |
| `match.py` | within-volume link: surname (+OCR-fuzzy) + initials + colony agreement (gazetteer) + position/honour corroborator; 0-FP ambiguity guard |
| `llm.py` | **Qwen 3.6 tier (for the GPU box, tomorrow)** — bio re-parse + roster extraction; OpenAI/Ollama-compatible, config via env; not run here |

Driver: `python3 volume_link.py --year 1921` (or `--years 1888,1921,1960`,
`--doc col|dol|cro`). Writes under `data/volume/<doc><year>/`:
`bios.jsonl`, `records.jsonl`, `links.jsonl`, `report.md`, `summary.json`, and
the two **Qwen worklists** `bios_unparsed.jsonl`, `roster_blocks.jsonl`.

## Results (deterministic baseline)

| edition | era | bios | bios rules-parsed | roster records | **links** | bios linked |
|--|--|--:|--:|--:|--:|--:|
| 1888 | early | 2,379 | 56% | 3,328 | 398 | **392 (16.5%)** |
| 1921 | mid | 3,490 | 68% | 4,372 | 387 | **383 (11.0%)** |
| 1960 | late | 5,021 | 95% | 164 | 9 | 9 (0.2%) |

**Precision: 8/8 hand-checked 1921 links correct** (Kindersley→Ceylon Govt
Agent, Munro→Bahamas Port Officer, Reid→Kenya Stores, two Seignorets correctly
disambiguated, etc.); provenance round-trips to the right raw blocks.

**Per-volume link rate is *legitimately* lower than the old pipeline's 48.8%** —
that 48.8% is a union across all editions, whereas the services section is
cumulative (it carries retired/past officers with no current-year post). The
payoff is the **union of links across all ~69 editions**, plus a clean
provenance chain. Do not compare a single volume's rate to 48.8%.

### Funnel (1921) — where the ceiling is, and what Qwen fixes
- 1,106 bios (32%) **unparsed** by the rules tier → 0 events → 0 links. **Qwen lever #1.**
- ~990 bios have **no same-surname roster record**, ~894 **no shared colony** —
  largely roster-recall loss: the deterministic parser mangles run-on lists and
  skips garbled/late-era blocks. **Qwen lever #2.**
- 388 bios are surname+colony+name-compatible → 383 linked (gate-correct; the
  rest are namesake/ambiguity drops). The matcher is NOT the bottleneck.

## LLM baseline (Opus in-session, 2026-06-19) — the parsing-ceiling finding

Jim's read: **"there is almost no way to parse these bios with Python."** Tested on 1921 and
confirmed on BOTH sides:

- **Bios.** The rules tier drops a whole entry on any one awkward clause → 1,106/3,490 (32%) reach
  the matcher with zero events. I (Opus) parsed a random 50 of them into structured events
  (`data/volume/col1921/llm_parsed.jsonl`, schema in `volume_llm_parse.py`). After excluding those who
  legitimately have no 1921 roster post (10 retired, 2 transferred-out, several Canadian
  politicians/military), the **genuinely-active subset links at ~22%** — at or above the deterministic
  rate — purely from recovering events Python couldn't.
- **Rosters are just as brittle.** Non-linked active officials whose records are *plainly in the OCR*
  but unextracted: **Winstedt** ("…R. O. Winstedt, **$700 to $950 p.m.**") and **Gatt**
  ("Superintendent of Public Works, L. Gatt, C.M.G." in a council list). Adding `$`-salaries alone
  recovered **+930 records and +54 links** in this one volume — one regex gap. Council-list / no-salary
  formats remain unparsed.
- **Linking itself needs semantic judgment.** Discombe ("Registrar of the Supreme Court, &c." vs
  "registr. and clk. of arraigns") and Hutson (single initial "J." vs "John") are correct links the
  0-FP deterministic gate won't risk — but an LLM adjudicator would.
- **Cumulative/stale bios.** Denham's bio ends 1916 (Ceylon); his 1921 record is Colonial Secretary,
  **Mauritius**. The move post-dates the bio, so within-volume colony agreement can't fire — a real
  ceiling, though an LLM reading both could still recognise "E. B. Denham".

**Conclusion.** The old project's ~50% ceiling was substantially a **parsing** ceiling (bios *and*
rosters), not a matcher-logic ceiling. The recommendation is to use the LLM (Qwen on the GPU box) for
**both** extraction sides, and ideally for the final link adjudication too; the deterministic pass
stays as a cheap first cut. Per-volume measured 1921 baseline: 387 → 441 (+$ salaries) → 452 (+50 LLM
bios) links; full-volume LLM parse of all 1,106 unparsed + LLM roster extraction projects materially
higher.

## Known limitations (all are Qwen targets)
1. **Late-era rosters (≈1948–1966)** use `Position—Name` with no salary and a
   London-department-heavy layout; the deterministic salary-delimited parser
   barely fires (1960: 164 records). bios still parse fine (95%).
2. Deterministic roster parser mangles run-on lists ("Puisne Judges, A;B;C")
   and leaks the occasional non-name; harmless to precision (mangled records
   don't match) but caps recall.

## Tomorrow on the GPU box (Qwen 3.6) — turnkey steps
1. Start an OpenAI-compatible server for Qwen 3.6 (Ollama `/v1`, vLLM, …) and set:
   ```bash
   export COL_VOLUME_LLM_URL=http://<host>:11434/v1
   export COL_VOLUME_LLM_MODEL=qwen3.6
   export COL_VOLUME_LLM_KEY=ollama        # any non-empty for local
   ```
   Sanity: `python3 -m col_match.volume.llm` (offline selftest PASSes here).
2. **Roster extraction (lever #2):** for each row of `roster_blocks.jsonl`, call
   `llm.extract_roster(client, text, colony, department)` → records; feed into
   `match.link_volume` alongside (or replacing) the deterministic `records.jsonl`.
3. **Bio re-parse (lever #1):** for each row of `bios_unparsed.jsonl`, call
   `llm.parse_bio_entry(client, raw_text)` → fill `events`; re-run the matcher.
4. Re-measure link rate per edition; spot-check precision against the bbox
   provenance (the `report.md` lists sample links with page citations).
5. Then scale across all editions (`reader.available_years()`), and union the
   per-volume links into the grounded cross-edition graph.

Note: `llm.py` is wired and import-safe but **not** auto-invoked by
`volume_link.py` (no Qwen on this machine). Add a `--llm` branch to the driver
once the server is up, or drive `llm.py` from a small batch script.
