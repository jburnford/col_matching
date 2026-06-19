"""Qwen 3.6 LLM tier for the within-volume pilot (runs on the GPU box).

Two jobs the deterministic tiers leave on the table (see VOLUME_PILOT.md):
  1. parse_bio_entry  — re-parse a services-section entry the rules tier could
     not fully account for (``bios_unparsed.jsonl``).
  2. extract_roster   — extract every (position, name) record from a roster
     text block, including the run-on lists the deterministic parser mangles
     (``roster_blocks.jsonl``).

Backend is any OpenAI-compatible server (Ollama ``/v1``, vLLM, llama.cpp …).
Config via env, with safe defaults for a local box:
  COL_VOLUME_LLM_URL    (default http://localhost:11434/v1)
  COL_VOLUME_LLM_MODEL  (default "qwen3.6")
  COL_VOLUME_LLM_KEY    (default "ollama"; any non-empty string for local)

Import-safe with no SDK and no server present — the client is built lazily, so
this module can be imported (and the deterministic pipeline can run) on a box
with no LLM. Nothing here is invoked by ``volume_link.py`` unless ``--llm`` is
passed.
"""

from __future__ import annotations

import json
import os
import re
from dataclasses import dataclass


@dataclass
class LLMConfig:
    base_url: str = os.environ.get("COL_VOLUME_LLM_URL", "http://localhost:11434/v1")
    model: str = os.environ.get("COL_VOLUME_LLM_MODEL", "qwen3.6")
    api_key: str = os.environ.get("COL_VOLUME_LLM_KEY", "ollama")
    temperature: float = 0.0
    max_tokens: int = 4096


class QwenClient:
    """Thin OpenAI-compatible chat client. Lazy SDK import."""

    def __init__(self, cfg: LLMConfig | None = None):
        self.cfg = cfg or LLMConfig()
        self._client = None

    def _client_lazy(self):
        if self._client is None:
            from openai import OpenAI  # lazy: not needed to import this module
            self._client = OpenAI(base_url=self.cfg.base_url, api_key=self.cfg.api_key)
        return self._client

    def complete(self, system: str, user: str) -> str:
        resp = self._client_lazy().chat.completions.create(
            model=self.cfg.model,
            temperature=self.cfg.temperature,
            max_tokens=self.cfg.max_tokens,
            messages=[{"role": "system", "content": system},
                      {"role": "user", "content": user}],
        )
        return resp.choices[0].message.content or ""


def _extract_json(text: str):
    """Pull the first JSON object/array out of a model response (handles
    ```json fences and reasoning preambles)."""
    text = re.sub(r"```(?:json)?|```", "", text).strip()
    # parse whichever bracket type appears FIRST (an array of objects opens with
    # "[" before its inner "{", so object-first ordering would mis-grab).
    order = sorted((("{", "}"), ("[", "]")),
                   key=lambda oc: (text.find(oc[0]) if oc[0] in text else len(text) + 1))
    for opener, closer in order:
        i = text.find(opener)
        if i < 0:
            continue
        depth = 0
        for j in range(i, len(text)):
            if text[j] == opener:
                depth += 1
            elif text[j] == closer:
                depth -= 1
                if depth == 0:
                    try:
                        return json.loads(text[i:j + 1])
                    except json.JSONDecodeError:
                        break
    return None


# ---- Prompts -------------------------------------------------------------

_BIO_SYSTEM = (
    "You convert one printed Colonial Office List biographical entry into JSON. "
    "Extract ONLY what is printed; never invent. Each career posting is one "
    "event with: position (as printed, keep abbreviations), place (colony/"
    "territory named or carried over), year_start, year_end (null if none). "
    'Return strictly: {"surname": str, "given_names": str|null, '
    '"birth_year": int|null, "honours": [{"award": str, "year": int|null}], '
    '"events": [{"position": str|null, "place": str|null, "year_start": '
    'int|null, "year_end": int|null}]}'
)

_ROSTER_SYSTEM = (
    "You extract every staff-list officer record from one printed Colonial "
    "Office List roster block. Each record is a person holding a post in the "
    "given colony. Return ONLY people actually named (skip salary-only or "
    "header fragments). For each: position (as printed), surname, given_names "
    "(initials or names as printed, null if none), honours (list of strings). "
    'Return strictly a JSON array: [{"position": str|null, "surname": str, '
    '"given_names": str|null, "honours": [str]}]. Extract names from run-on '
    "lists too (e.g. 'Puisne Judges, A. B. Smith; C. D. Jones' = two records)."
)


def parse_bio_entry(client: QwenClient, raw_text: str) -> dict | None:
    out = _extract_json(client.complete(_BIO_SYSTEM, raw_text))
    return out if isinstance(out, dict) else None


def extract_roster(client: QwenClient, block_text: str, colony: str,
                   department: str | None = None) -> list[dict]:
    user = f"Colony: {colony}\nDepartment: {department or '(none)'}\n\nBlock:\n{block_text}"
    out = _extract_json(client.complete(_ROSTER_SYSTEM, user))
    return out if isinstance(out, list) else []


def selftest_offline() -> bool:
    """Validate prompt plumbing + JSON extraction without a server."""
    assert _extract_json('noise ```json\n{"a":1}\n``` tail') == {"a": 1}
    assert _extract_json('reasoning... [{"surname":"Reid"}] done') == [{"surname": "Reid"}]
    assert _extract_json("no json here") is None
    return True


if __name__ == "__main__":
    print("offline selftest:", "PASS" if selftest_offline() else "FAIL")
    print("config:", LLMConfig())
