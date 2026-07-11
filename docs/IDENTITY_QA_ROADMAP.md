# Identity QA roadmap: finding the remaining over- and under-merged officials

*Written July 11, 2026, with full pipeline context. Identity errors live at
five distinct layers, and each layer's fix is different. The corpus's
redundancy — the same person attested in rosters, bios, honours rolls,
governor lists, promotion matrices — is the untapped asset: most checks below
are cross-layer triangulations that need no new data.*

The five layers where identity can go wrong:

1. **bio → person** (spine partition + applied under-merges)
2. **roster record → career** (stringing on colony × surname × initials)
3. **career → person** (within-volume links + adjudicated overlay)
4. **career → career** (cross-colony transfers)
5. **context → person** (governors, honours, CO ladders)

What we already know about failure modes (all empirically found this week):
initials-subsequence stretch ("Mary" ≅ "Robt Malcolm"); bare shared forename
("Kenneth Skelton" ≅ "Kenneth Arthur Noel"); OCR-garbled birth years (b.1888
holding an 1853 ensigncy); dynastic succession (Barbados Berkeleys passing
posts father→son, >40-yr spans over-merge at 26.9% vs 5.6%); 1948-reformat
chain splits; duplicate page scans; surname frequency as the dominant risk
axis (common surnames 11.1% over-merge even with full names).

## Tier A — deterministic fingerprints (cheap, run tonight, no GPU)

**A1. Honours-precedence violations** *(probed: 25 hits)*. Within one order,
grades only ascend (C.M.G. → K.C.M.G. → G.C.M.G.). A person whose honours
list has a LOWER grade dated after a higher one is two people fused (or a
garbled year). 25 persons flagged in a 5-minute probe — each is a
near-certain over-merge candidate with the split point given by the honours
themselves.

**A2. Age invariants** *(probed: 606 + 45 hits)*. Entry age <13 or >65
(606 persons) and active service past age 75 (45) flag either garbled birth
years (resolvable: which reading makes entry age 15–35?) or dynastic merges
(events span two lifetimes). Auto-adjudicate the birth-year conflicts already
flagged (860) with the same rule: prefer the reading that lands entry age in
the plausible band; demand >=3 shared appointments to keep the merge.

**A3. Salary/rank regression inside careers.** A strung career whose peak
salary drops by >60% mid-stream, or whose position class regresses
(officer → subordinate) and stays there, is a senior+junior namesake pair —
the son entering at the bottom as the father peaks. Complements the span>40
screen with a within-span signature.

**A4. Trajectory incoherence (place alternation).** Real careers move in
blocks; interleaved namesakes alternate (Ceylon 1900, Jamaica 1901, Ceylon
1902…). Score each person's event sequence for A-B-A colony alternation with
sub-2-year periods; high scorers are fused namesakes. Also catches wrong
class-C links after the fact.

**A5. Implausible multi-post years.** `multi_post_years` in careers marks
same-year multi-department listings. Holding Treasury + Gaol in a small
colony is normal pluralism; holding Police + Education + Railways across
distant departments is a namesake signature. Classify multi-post years by
department distance.

**A6. Same-rare-honour duplicates (UNDER-merge).** Two persons claiming the
same award + year + order (honours are unique appointments within a year's
list, modulo common orders) are one person split. The honours layer is 95%
full-given-names, so this catches splits the appointment-chain test misses
(e.g., careers with few dated events).

## Tier B — cross-layer triangulation (a day each, mostly deterministic)

**B1. Audit the foundation: the 79,510 within-volume links.** Everything
person-level rests on these, and unlike the class-C overlay they were never
adversarially audited — the 0-FP discipline is a design claim, not a
measured rate. Score every link deterministically (position agreement at the
linked year, colony agreement, name strength), then Nibi-adjudicate a
stratified sample (~500) to convert the score distribution into a measured
precision per stratum. This is the single most valuable number for the
methods section that we don't yet have.

**B2. Promotion-ladder ↔ roster agreement.** CO persons now carry exact
grade-year ladders; their roster records (COLONIAL OFFICE (LONDON) careers)
should agree year-by-year. Disagreement localizes bad merges in BOTH layers.
Same trick works for governors: a career that keeps being listed in colony X
after its matched governor demonstrably left is an over-merge.

**B3. Bio-event ↔ roster-position agreement sweep.** For every linked
(career, person) pair, compute the fraction of roster years where the bio has
a compatible event. We used this pairwise for adjudication; run it as a
corpus-wide score and the left tail is the error queue — cheap because it is
pure computation over existing joins.

**B4. Education and residence as tie-breakers.** graph_stage3 carries
education edges (schools, universities, call-to-bar) keyed to kgp ids —
they survive into the unified persons. Two same-name persons with the same
school + matriculation window = under-merge candidate; one person with two
different schools at overlapping ages = over-merge. Never yet used for
identity.

**B5. Namesake collision null model.** From the corpus's own name
distribution, compute the EXPECTED number of same-(surname, initials) pairs
per colony-decade under independence. Colonies/surnames where the observed
career count falls far below expectation are over-merge hotspots (two
expected namesakes got strung as one); far above, suspect fragmentation.
Turns auditing from anecdote into a heat map — and it directly quantifies
the residual risk for the paper's sensitivity note.

## Tier C — external grounding (blocked or slower)

**C1. Wikidata death dates** (when the MCP vector service returns). The
elite stratum (governors, K.C.M.G.+) is nearly all in WD with death dates:
any event after death = over-merge, cleanly. Also resolves the 9 peer-map
entries and 38 unmatched governors already queued.

**C2. London Gazette honours announcements** give exact award dates for
every order — an external key that both validates honours matches and
provides birth-independent person anchors. Scrape-able, but a separate
project.

## Tier D — process hardening (prevents future breakage)

**D1. Content-hash career ids.** career_id renumbering on every rebuild cost
us a remap layer this week. Key careers on
hash(colony, surname, first_record_id) — stable across rebuilds, kills the
remap machinery, makes all overlays durable.

**D2. Identity invariants as a test script.** One `volume_identity_check.py`
run at the end of every chain: partition totality (every bio in exactly one
person), no unflagged same-edition primaries, no honours-precedence
violations above baseline, age-invariant counts, link bijectivity. Fail loud.
The chain has enough moving parts now that silent regressions are the main
risk.

**D3. A single decisions ledger.** undermerge_decisions.jsonl worked well;
generalize it: every human/LLM-adjudicated split, merge, and link exception
in one append-only file the pipeline re-applies. Decisions currently live in
three formats across two directories.

## Suggested order

1. A1+A2+A6 in one script (`volume_identity_screens.py`) — an afternoon,
   immediately actionable output, feeds the existing decisions ledger.
2. B1 (link audit) — the measured-precision number the paper needs most.
3. D1+D2 — before the next big rebuild, not after.
4. A3+A4+A5 as a second screens pass; B5 for the methods appendix.
5. B2–B4 opportunistically; C1 the day the WD service returns.
