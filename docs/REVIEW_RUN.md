# Fresh-session runbook: second-LLM review of flagged drops

Adjudicate the 2,639 facts the deterministic validator dropped from the
structured corpus (the **flag-don't-drop** discipline). An independent model
(Claude Sonnet — different family from the Qwen3.6 structurer) reads each bio's
source text and decides **keep / correct / drop** for each dropped value, citing
an exact source quote. Python then merges back only quote-verified values
(`kg_review_flags.py merge`), so the model proposes but Python keeps the last
word — 0-FP preserved.

Everything is pre-staged. A fresh session only has to fan out the reviewers,
concatenate, and merge.

## Inputs (already on disk)
- `data/kg/review/batches/batch_001.jsonl … batch_017.jsonl` — 17 batches, ≤80
  persons each. One JSON object per line:
  `{person_id, source_text, packets:[{field_path, flagged_value, reason}]}`.
- `data/kg/review/verdicts/` — empty output dir (one file per batch goes here).

## 1. Fan out 17 Sonnet reviewers
Launch the Agent tool with `subagent_type: "general-purpose"`, `model: "sonnet"`,
once per batch `NNN` in `001..017` (run in waves of ~8–10 concurrent; safe to run
all in the background). Give each agent **exactly** this prompt, substituting the
batch number:

```
You adjudicate facts a deterministic validator DROPPED from structured 1860s–1960s
Colonial Office biographies because it could not confirm them in the printed
source (dense OCR with heavy abbreviations: "E.A.P."=East Africa Protectorate,
"S. Sttlmts."=Straits Settlements, "1900-02" means 1902, etc.).

Read /home/jic823/col_matching/data/kg/review/batches/batch_NNN.jsonl. Each line is
one person: {person_id, source_text, packets:[{field_path, flagged_value, reason}]}.

For EACH packet, read that person's source_text and decide:
- "keep": the flagged value IS supported by the source (an OCR/abbreviation form
  made the automatic check miss it).
- "correct": the source supports a DIFFERENT value — give it as corrected_value.
- "drop": the value is genuinely not supported by the source (a real error).

You MUST cite source_evidence: an EXACT substring copied verbatim from that
person's source_text that supports your verdict (empty string for "drop"). Do not
paraphrase or invent it — a later step rejects any quote that is not a real
substring, so a fabricated quote wastes the verdict.

Write your results to /home/jic823/col_matching/data/kg/review/verdicts/verdicts_NNN.jsonl,
ONE JSON line per packet, with exactly these keys:
{"person_id": <from the person>, "field_path": <from the packet>,
 "flagged_value": <from the packet>, "reason": <from the packet>,
 "verdict": "keep|correct|drop", "corrected_value": <value or null>,
 "source_evidence": "<exact substring or empty>", "confidence": <0.0-1.0>,
 "rationale": "<one short line>"}

Process every packet in the batch. Return only a one-line summary
"batch NNN: <N> packets, keep=<a> correct=<b> drop=<c>" — your written file is the
real output.
```

## 2. Concatenate verdicts
After all 17 agents finish and `verdicts_001..017.jsonl` exist:
```
cd ~/col_matching
cat data/kg/review/verdicts/verdicts_*.jsonl > data/kg/review/llm_review_verdicts.jsonl
wc -l data/kg/review/llm_review_verdicts.jsonl   # expect ~2639
```

## 3. Merge back (Python gates every quote — 0-FP)
```
python3 kg_review_flags.py merge \
  --raw data/kg/llm_struct_corpus.jsonl \
  --persons data/kg/persons.deduped2.recovered.jsonl
# -> data/kg/llm_struct_corpus.reviewed.jsonl   (postnorm + validate + confirmed restorations)
```
`merge` only restores a value whose `source_evidence` is a real substring of the
source (`kg_review_flags._confirmed`), so a wrong/fabricated quote is dropped.

## 4. Regenerate the grounding worklist on the reviewed output
```
python3 kg_build.py ground --struct data/kg/llm_struct_corpus.reviewed.jsonl \
  > data/kg/places_worklist.jsonl
head -1 data/kg/places_worklist.jsonl
```

## Verification
- 17 `verdicts_NNN.jsonl` files exist; combined ≈ 2,639 lines (one per packet).
- Every verdict line parses and has the 9 keys above; `verdict ∈ {keep,correct,drop}`.
- `merge` prints `merged <R> reviewer-confirmed values into <N> structs`; spot-check
  10 `keep`/`correct` verdicts — each `source_evidence` is genuinely in that
  person's source.
- `reviewed.jsonl` line count == `valid.jsonl` line count (36,167); only previously
  dropped-but-confirmed facts differ.

## Notes
- The verdict schema matches what `kg_review_flags.py merge` already consumes
  (`person_id, field_path, flagged_value, verdict, corrected_value, source_evidence`)
  — the only change from the scripted OpenRouter path is the transport (in-session
  Sonnet agents instead of an API call).
- Resumable: if some batches fail, re-launch only the agents whose
  `verdicts_NNN.jsonl` is missing/short before concatenating.
- This is independent of the still-open items: the ~696 recovered-person duplicate
  flags (`concat_recovered_dupcheck.jsonl`) and the 20 over-length unstructured
  bios — neither blocks this review.
