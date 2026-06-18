"""LLM fallback parsing tier via the Gemini Batch API (50% of interactive
cost; results within 24h, jobs expire at 48h).

Only entries the rules tier could not fully account for come here
(data/services/pending_llm.jsonl). Responses pass the same validation gates
(validate.py); failures escalate to the interactive API on a stronger model,
and persistent failures land in failures/llm.jsonl for hand review.

Batch jobs are NOT idempotent server-side; data/services/batch_jobs.json is
our manifest so re-submission never duplicates work.
"""

from __future__ import annotations

import json
import time
from pathlib import Path

from google import genai
from google.genai import types

from .schema import EntryVersion, ParsedEntry
from .validate import validate_parsed

BATCH_MODEL = "models/gemini-flash-latest"
ESCALATE_MODEL = "models/gemini-pro-latest"

_PROMPT = """\
You are parsing one biographical entry from the {year} edition of the British
Colonial Office List "Record of Services" section. The text is OCR output and
may contain minor character errors; do NOT correct names, just transcribe.

Parse the entry into JSON:
- surname, given_names (exclude titles like Sir/Capt.), title_rank (the titles),
  birth_year (from "B. 1869" / "b. 1906"), education (the "ed. ..." clause),
  honours: [{{award, year}}] from the name block (e.g. "K.C.M.G. (1922)").
- events: one per dated career step, in printed order:
  {{position, place, year_start, year_end, text_span}}.
  text_span MUST be the verbatim clause copied from the entry.
  Expand year ranges: "1904 to 1908" -> 1904/1908; "1914-19" -> 1914/1919.
  place is the colony/territory if the clause names one (expand printed
  abbreviations: "G.C."=Gold Coast, "Nig."=Nigeria, "J'ca"=Jamaica, etc.);
  if the clause names no place, set place to null - do NOT guess.
- terminal: {{kind, year, text_span}} if the entry ends with
  retired/resigned/died/pensioned.
- notes: undated narrative clauses, verbatim.
Do not invent values. Omit/null anything not present.

ENTRY:
{text}
"""

_RESPONSE_SCHEMA = {
    "type": "OBJECT",
    "properties": {
        "surname": {"type": "STRING"},
        "given_names": {"type": "STRING", "nullable": True},
        "title_rank": {"type": "STRING", "nullable": True},
        "birth_year": {"type": "INTEGER", "nullable": True},
        "education": {"type": "STRING", "nullable": True},
        "honours": {
            "type": "ARRAY",
            "items": {
                "type": "OBJECT",
                "properties": {
                    "award": {"type": "STRING"},
                    "year": {"type": "INTEGER", "nullable": True},
                },
                "required": ["award"],
            },
        },
        "events": {
            "type": "ARRAY",
            "items": {
                "type": "OBJECT",
                "properties": {
                    "position": {"type": "STRING", "nullable": True},
                    "place": {"type": "STRING", "nullable": True},
                    "year_start": {"type": "INTEGER", "nullable": True},
                    "year_end": {"type": "INTEGER", "nullable": True},
                    "text_span": {"type": "STRING"},
                },
                "required": ["text_span"],
            },
        },
        "terminal": {
            "type": "OBJECT",
            "nullable": True,
            "properties": {
                "kind": {"type": "STRING"},
                "year": {"type": "INTEGER", "nullable": True},
                "text_span": {"type": "STRING"},
            },
            "required": ["kind", "text_span"],
        },
        "notes": {"type": "ARRAY", "items": {"type": "STRING"}},
    },
    "required": ["surname", "events"],
}


def _manifest_path(data_dir: str) -> Path:
    return Path(data_dir) / "batch_jobs.json"


def _load_manifest(data_dir: str) -> dict:
    p = _manifest_path(data_dir)
    return json.loads(p.read_text()) if p.exists() else {"jobs": []}


def _save_manifest(data_dir: str, manifest: dict) -> None:
    _manifest_path(data_dir).write_text(json.dumps(manifest, indent=2))


def _request_line(v: EntryVersion) -> str:
    req = {
        "key": v.version_id,
        "request": {
            "contents": [
                {"parts": [{"text": _PROMPT.format(year=v.edition_year, text=v.canonical_text)}],
                 "role": "user"}
            ],
            "generation_config": {
                "response_mime_type": "application/json",
                "response_schema": _RESPONSE_SCHEMA,
            },
        },
    }
    return json.dumps(req, ensure_ascii=False)


def submit_batch(versions: list[EntryVersion], data_dir: str, api_key: str,
                 model: str = BATCH_MODEL, tag: str = "main") -> str:
    """Upload a JSONL request file and create one batch job. Versions already
    covered by a live or finished job in the manifest are skipped."""
    manifest = _load_manifest(data_dir)
    done_keys = {k for j in manifest["jobs"] if j["state"] != "failed" for k in j["keys"]}
    todo = [v for v in versions if v.version_id not in done_keys]
    if not todo:
        print("nothing to submit (all keys covered by manifest)")
        return ""
    client = genai.Client(api_key=api_key)
    req_path = Path(data_dir) / f"batch_requests_{tag}.jsonl"
    with req_path.open("w", encoding="utf-8") as f:
        for v in todo:
            f.write(_request_line(v) + "\n")
    uploaded = client.files.upload(
        file=req_path,
        config=types.UploadFileConfig(display_name=f"col-services-{tag}",
                                      mime_type="application/jsonl"),
    )
    job = client.batches.create(
        model=model,
        src=uploaded.name,
        config={"display_name": f"col-services-{tag}"},
    )
    manifest["jobs"].append({
        "name": job.name, "model": model, "tag": tag,
        "state": "submitted", "keys": [v.version_id for v in todo],
        "request_file": str(req_path),
    })
    _save_manifest(data_dir, manifest)
    print(f"submitted {job.name}: {len(todo)} requests on {model}")
    return job.name


def poll_and_collect(data_dir: str, api_key: str) -> dict:
    """Check all live jobs; download finished results into parsed/llm_raw/."""
    manifest = _load_manifest(data_dir)
    client = genai.Client(api_key=api_key)
    out_dir = Path(data_dir) / "parsed" / "llm_raw"
    out_dir.mkdir(parents=True, exist_ok=True)
    summary = {}
    for j in manifest["jobs"]:
        if j["state"] in ("collected", "failed"):
            continue
        job = client.batches.get(name=j["name"])
        state = job.state.name if hasattr(job.state, "name") else str(job.state)
        summary[j["name"]] = state
        if state == "JOB_STATE_SUCCEEDED":
            dest = getattr(job, "dest", None)
            result_name = getattr(dest, "file_name", None) if dest else None
            if result_name:
                content = client.files.download(file=result_name)
                raw_path = out_dir / f"{j['tag']}_{j['name'].split('/')[-1]}.jsonl"
                raw_path.write_bytes(content)
                j["state"] = "collected"
                j["result_file"] = str(raw_path)
        elif state in ("JOB_STATE_FAILED", "JOB_STATE_CANCELLED", "JOB_STATE_EXPIRED"):
            j["state"] = "failed"
    _save_manifest(data_dir, manifest)
    return summary


def harvest(data_dir: str, versions_by_id: dict[str, EntryVersion],
            parser_label: str = "flash") -> dict:
    """Validate collected raw responses; write accepted ParsedEntries and an
    escalation list of version_ids that failed."""
    out_dir = Path(data_dir) / "parsed"
    accepted: dict[str, ParsedEntry] = {}
    failed: dict[str, list[str]] = {}
    seen: set[str] = set()
    for raw in sorted((out_dir / "llm_raw").glob("*.jsonl")):
        # tag files (escalate-pro etc.) carry the parser label in the name
        label = "pro" if "pro" in raw.name else parser_label
        for line in raw.open(encoding="utf-8"):
            rec = json.loads(line)
            key = rec.get("key") or rec.get("custom_id")
            if key is None or key in accepted:
                continue
            seen.add(key)
            v = versions_by_id.get(key)
            if v is None:
                continue
            try:
                resp = rec["response"]["candidates"][0]["content"]["parts"][0]["text"]
                data = json.loads(resp)
                data["version_id"] = key
                data["parser"] = label
                parsed = ParsedEntry.model_validate(data)
            except Exception as exc:  # malformed response -> escalate
                failed.setdefault(key, [f"malformed:{type(exc).__name__}"])
                continue
            fatal = validate_parsed(parsed, v)
            if fatal:
                failed.setdefault(key, fatal)
            else:
                accepted[key] = parsed
                failed.pop(key, None)
    with (out_dir / "llm.jsonl").open("w", encoding="utf-8") as out_ok:
        for parsed in accepted.values():
            out_ok.write(parsed.model_dump_json(exclude_none=True) + "\n")
    failed = {k: v for k, v in failed.items() if k not in accepted}
    (Path(data_dir) / "llm_escalate.json").write_text(json.dumps(failed, indent=1))
    return {"accepted": len(accepted), "failed": len(failed), "responses_seen": len(seen)}


def escalate_interactive(data_dir: str, versions_by_id: dict[str, EntryVersion],
                         api_key: str, model: str = ESCALATE_MODEL) -> dict:
    """Re-parse escalation list one-by-one on a stronger model (interactive).
    Persistent failures -> failures/llm.jsonl."""
    esc_path = Path(data_dir) / "llm_escalate.json"
    failed_keys = list(json.loads(esc_path.read_text())) if esc_path.exists() else []
    client = genai.Client(api_key=api_key)
    out_dir = Path(data_dir) / "parsed"
    fail_dir = Path(data_dir) / "failures"
    fail_dir.mkdir(parents=True, exist_ok=True)
    accepted = 0
    hard_failures = []
    with (out_dir / "llm.jsonl").open("a", encoding="utf-8") as out_ok:
        for key in failed_keys:
            v = versions_by_id.get(key)
            if v is None:
                continue
            ok = False
            for attempt in range(2):
                try:
                    resp = client.models.generate_content(
                        model=model,
                        contents=_PROMPT.format(year=v.edition_year, text=v.canonical_text),
                        config=types.GenerateContentConfig(
                            response_mime_type="application/json",
                            response_schema=_RESPONSE_SCHEMA,
                        ),
                    )
                    data = json.loads(resp.text)
                    data["version_id"] = key
                    data["parser"] = "pro" if "pro" in model else "flash"
                    parsed = ParsedEntry.model_validate(data)
                    if not validate_parsed(parsed, v):
                        out_ok.write(parsed.model_dump_json(exclude_none=True) + "\n")
                        accepted += 1
                        ok = True
                        break
                except Exception:
                    time.sleep(2 * (attempt + 1))
            if not ok:
                hard_failures.append(key)
    with (fail_dir / "llm.jsonl").open("w", encoding="utf-8") as f:
        for key in hard_failures:
            v = versions_by_id.get(key)
            if v:
                f.write(v.model_dump_json() + "\n")
    return {"escalated_accepted": accepted, "hard_failures": len(hard_failures)}
