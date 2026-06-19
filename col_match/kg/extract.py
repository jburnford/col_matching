"""LLM STRUCTURE pass — the irregular half of the hybrid.

Given a normalized canonical entry, the LLM emits the structure Python cannot
reliably recover: career events binding position to place to time-span across
run-on / elided / "ditto" / concurrent clauses, plus honours, education, and
terminal status. It is LLM-agnostic: the same object is produced by

  * the in-session Opus baseline (dump_batch -> the model writes one JSON object
    per person to llm_struct.jsonl -> consume), the pattern proven in
    volume_llm_parse.py; and
  * Qwen on the GPU box via ``parse_via_client`` + the QwenClient adapter.

Places are recorded AS PRINTED (locality or colony) — never resolved to a
colony here; grounding to Wikidata happens downstream. The Python validator
(validate.py) reviews every emitted place/year against the source text.
"""

from __future__ import annotations

import json
import random
from pathlib import Path

from ..volume.llm import QwenClient, _extract_json
from .normalize import normalize_for_llm

# Structured object the LLM must return for one biography.
KG_BIO_SCHEMA = {
    "type": "object",
    "properties": {
        "surname": {"type": "string"},
        "given_names": {"type": ["string", "null"]},
        "birth_year": {"type": ["integer", "null"]},
        "education": {"type": ["string", "null"]},
        "honours": {"type": "array", "items": {"type": "object", "properties": {
            "award": {"type": "string"}, "year": {"type": ["integer", "null"]}},
            "required": ["award", "year"], "additionalProperties": False}},
        "events": {"type": "array", "items": {"type": "object", "properties": {
            "position": {"type": ["string", "null"]},
            "place": {"type": ["string", "null"]},
            "year_start": {"type": ["integer", "null"]},
            "year_end": {"type": ["integer", "null"]},
            "place_inherited": {"type": "boolean"},
            "is_acting": {"type": "boolean"},
            "org_type": {"type": "string", "enum": ["civil", "military"]}},
            "required": ["position", "place", "year_start", "year_end",
                         "place_inherited", "is_acting", "org_type"],
            "additionalProperties": False}},
        "terminal": {"type": ["object", "null"], "properties": {
            "kind": {"type": "string"}, "year": {"type": ["integer", "null"]}},
            "required": ["kind", "year"], "additionalProperties": False},
    },
    "required": ["surname", "given_names", "birth_year", "education",
                 "honours", "events", "terminal"],
    "additionalProperties": False,
}

KG_BIO_SYSTEM = (
    "You convert ONE printed Colonial Office List biographical entry into a JSON "
    "career record. Extract ONLY what is printed; never invent or infer facts.\n"
    "Rules:\n"
    "- events: one object per distinct posting. EXPLODE compound/concurrent "
    "clauses into separate events (e.g. 'reg.-gen., 1887, and M.L.C., 1889' = two "
    "events; 'ag. comsnr., 1915-16; and from 1919' = two events).\n"
    "- position: as printed (the normalized expansion is fine), e.g. 'assistant "
    "colonial secretary'.\n"
    "- place: the colony, territory, OR locality named in the clause, AS PRINTED "
    "(e.g. 'Ceylon', 'Negombo', 'N. Nigeria'). If the clause names no place, "
    "carry over the previous clause's place and set place_inherited=true; do NOT "
    "guess or upgrade a locality to its parent colony — record exactly what is "
    "printed. Inheritance stops when a transfer is stated.\n"
    "- year_start/year_end: the posting's years; year_end null if a single year.\n"
    "- is_acting: true when the post is acting ('ag.'/'acting').\n"
    "- org_type: 'military' for army/navy/regiment/expedition/campaign postings, "
    "else 'civil'.\n"
    "- honours: decorations/orders with their AWARD year if printed in parentheses "
    "(e.g. 'C.M.G. (1905)'); these award-years are NOT career events.\n"
    "- birth_year: only if explicitly printed ('B. 1872'); else null. NEVER infer "
    "from the earliest career date.\n"
    "- education: the 'ed. ...' string as one metadata string; university class "
    "honours stay here, NOT as events.\n"
    "- terminal: {kind: retired|resigned|died|pensioned|other, year} if the entry "
    "states the career ended, else null."
)


def parse_via_client(client: QwenClient, raw_text: str) -> dict | None:
    """Qwen/GPU-box path: one structured completion."""
    out = _extract_json(client.complete(KG_BIO_SYSTEM, normalize_for_llm(raw_text)))
    return out if isinstance(out, dict) else None


def dump_batch(persons_path: Path, out_dir: Path, n: int, seed: int) -> None:
    """In-session path: print canonical entries (person_id + normalized text)
    for persons NOT yet structured. The in-session LLM writes the parsed JSON
    objects to a fresh file under ``out_dir/struct_in/`` (one per batch — no
    append races). Resumable: skips persons already structured in any batch."""
    persons = [json.loads(l) for l in (persons_path).open(encoding="utf-8")]
    done = structured_ids(out_dir / "struct_in")
    bios = {b["bio_id"]: b for b in _iter_canon_bios(out_dir)}
    todo = [p for p in persons if p["person_id"] not in done
            and p["canonical_bio_id"] in bios]
    random.Random(seed).shuffle(todo)
    batch = todo[:n]
    print(f"# {len(todo)} persons remain unstructured ({len(done)} done); dumping {len(batch)}")
    for p in batch:
        b = bios[p["canonical_bio_id"]]
        print(json.dumps({"person_id": p["person_id"],
                          "text": normalize_for_llm(b["raw_text"])}, ensure_ascii=False))


def structured_ids(struct_dir: Path) -> set[str]:
    """All person_ids structured across every batch file in struct_dir."""
    if not struct_dir.exists():
        return set()
    out: set[str] = set()
    for f in struct_dir.glob("*.jsonl"):
        for l in f.open(encoding="utf-8"):
            try:
                out.add(json.loads(l)["person_id"])
            except (json.JSONDecodeError, KeyError):
                continue
    return out


def _iter_canon_bios(out_dir: Path):
    """Canonical bios live in the per-edition bios cache (data/kg/bios)."""
    cache = Path("data/kg/bios")
    for f in cache.glob("*.jsonl"):
        for l in f.open(encoding="utf-8"):
            yield json.loads(l)
