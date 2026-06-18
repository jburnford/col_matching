"""Capped, ledgered LLM client for the extraction backfill.

All metered spend flows through here. The motivation is a prior cost overrun
(a batch job billed ~$100 against a sub-$10 estimate): every call is checked
against a hard USD cap *before* it is made, and every call that does happen is
appended to an on-disk ledger so the running total survives restarts and the
true cost is auditable after the fact.

Uses the OpenAI SDK pointed at OpenRouter (or a local Ollama server's
OpenAI-compatible endpoint, for the zero-cost Spark fallback). No network write
to anything but the model API; this module never touches Neo4j.
"""

from __future__ import annotations

import json
import math
import threading
import time
from datetime import datetime, timezone
from pathlib import Path

OPENROUTER_BASE_URL = "https://openrouter.ai/api/v1"

# USD per 1M tokens, (input, output). Placeholders — confirm on the model page
# before the first spend. A model missing here is priced as the most expensive
# known tier so an unknown slug can never under-bill the cap.
PRICES: dict[str, tuple[float, float]] = {
    "deepseek/deepseek-v4-flash": (0.098, 0.196),
    "deepseek/deepseek-v4-pro": (0.435, 0.870),
}
_FALLBACK_PRICE = max(PRICES.values(), default=(1.0, 2.0))


class SpendCapExceeded(RuntimeError):
    """Raised before a call that would push spend past the cap. The run aborts
    cleanly; the ledger + manifest make it resumable."""


class OutputTruncated(RuntimeError):
    """The model hit the output-token ceiling (finish_reason == 'length') and
    the JSON is cut off. The call was billed (ledger updated); the caller should
    re-split the input into smaller pieces and retry, not re-send it verbatim."""


def price_of(model: str) -> tuple[float, float]:
    return PRICES.get(model, _FALLBACK_PRICE)


def estimate_tokens(text: str) -> int:
    """~4 chars/token heuristic. Used for pre-call projection and the whole-run
    estimate; actual billing always uses the API's reported usage."""
    return math.ceil(len(text) / 4)


def cost_of(model: str, tokens_in: int, tokens_out: int) -> float:
    pin, pout = price_of(model)
    return (tokens_in * pin + tokens_out * pout) / 1_000_000


class OpenRouterClient:
    def __init__(self, api_key: str, cap_usd: float, ledger_path: Path,
                 max_output_tokens: int = 16000, timeout: float = 600.0,
                 base_url: str = OPENROUTER_BASE_URL, free: bool = False):
        if not api_key and not free:
            raise ValueError(
                "No OPENROUTER_API_KEY set. Load it from a gitignored .env; "
                "never hard-code it.")
        try:
            from openai import OpenAI
        except ImportError as e:  # pragma: no cover
            raise RuntimeError("the 'openai' package is required") from e
        self._client = OpenAI(api_key=api_key or "ollama", base_url=base_url,
                              timeout=timeout)
        self.cap_usd = cap_usd
        self.ledger_path = Path(ledger_path)
        self.max_output_tokens = max_output_tokens
        self.free = free
        self.ledger_path.parent.mkdir(parents=True, exist_ok=True)
        self._lock = threading.Lock()   # serialize ledger reads/writes across workers

    @classmethod
    def ollama(cls, host: str, cap_usd: float, ledger_path: Path,
               max_output_tokens: int = 16000, timeout: float = 600.0):
        """Spark fallback: a local Ollama server's OpenAI-compatible endpoint.
        Cost is zero, but the cap/ledger plumbing is kept for parity."""
        return cls(api_key="", cap_usd=cap_usd, ledger_path=ledger_path,
                   max_output_tokens=max_output_tokens, timeout=timeout,
                   base_url=host.rstrip("/") + "/v1", free=True)

    # --- spend accounting -------------------------------------------------
    def running_spend(self) -> float:
        """Sum of cost_usd over the ledger — the resume-safe source of truth."""
        with self._lock:
            if not self.ledger_path.exists():
                return 0.0
            total = 0.0
            with self.ledger_path.open(encoding="utf-8") as fh:
                for line in fh:
                    if line.strip():
                        total += json.loads(line).get("cost_usd", 0.0)
            return total

    def project_cost(self, model: str, tokens_in: int) -> float:
        """Worst-case cost of one call: full input + the output ceiling."""
        return cost_of(model, tokens_in, self.max_output_tokens)

    def _append_ledger(self, row: dict) -> None:
        with self._lock:
            with self.ledger_path.open("a", encoding="utf-8") as fh:
                fh.write(json.dumps(row) + "\n")

    # --- the one call site ------------------------------------------------
    def complete(self, *, model: str, system: str, user: str,
                 response_schema: dict, section_id: str, tier: str,
                 chunk: int = 0, retries: int = 3) -> dict:
        """One JSON-schema-constrained completion. Raises SpendCapExceeded
        BEFORE spending if the worst-case projection would breach the cap."""
        tokens_in = estimate_tokens(system) + estimate_tokens(user)
        if not self.free:
            projected = self.running_spend() + self.project_cost(model, tokens_in)
            if projected > self.cap_usd:
                raise SpendCapExceeded(
                    f"call on {section_id!r} would project ${projected:.4f} "
                    f"> cap ${self.cap_usd:.2f} (spent "
                    f"${self.running_spend():.4f}); aborting. Re-run with "
                    f"--resume after raising the cap.")

        last_err: Exception | None = None
        for attempt in range(retries):
            try:
                resp = self._client.chat.completions.create(
                    model=model, temperature=0,
                    max_tokens=self.max_output_tokens,
                    messages=[{"role": "system", "content": system},
                              {"role": "user", "content": user}],
                    response_format={
                        "type": "json_schema",
                        "json_schema": {"name": "staff_list", "strict": True,
                                        "schema": response_schema}},
                    # ask OpenRouter to return the ACTUAL credits charged so the
                    # ledger matches the dashboard (my per-token formula under-
                    # counted ~2x — reasoning/markup not captured).
                    extra_body={"usage": {"include": True}})
            except Exception as e:  # transient 429/5xx/network
                last_err = e
                if attempt == retries - 1:
                    break
                time.sleep(2 ** (attempt + 1))
                continue

            usage = getattr(resp, "usage", None)
            t_in = getattr(usage, "prompt_tokens", tokens_in) or tokens_in
            t_out = getattr(usage, "completion_tokens", 0) or 0
            # prefer the provider-reported actual cost; fall back to the formula
            actual = getattr(usage, "cost", None)
            if self.free:
                cost, src = 0.0, "free"
            elif actual is not None:
                cost, src = float(actual), "actual"
            else:
                cost, src = cost_of(model, t_in, t_out), "estimated"
            self._append_ledger({
                "ts": datetime.now(timezone.utc).isoformat(timespec="seconds"),
                "section_file": section_id, "chunk": chunk, "model": model,
                "tier": tier, "tokens_in": t_in, "tokens_out": t_out,
                "cost_usd": round(cost, 6), "cost_source": src, "attempt": attempt})
            content = resp.choices[0].message.content or "{}"
            finish = getattr(resp.choices[0], "finish_reason", None)
            if finish == "length":
                raise OutputTruncated(
                    f"{section_id!r} chunk={chunk} hit the output ceiling "
                    f"({t_out} tok); caller should re-split")
            try:
                return json.loads(content)
            except json.JSONDecodeError as je:
                # cut off mid-array without a clean 'length' signal — treat as
                # truncation so the caller re-splits rather than losing the chunk.
                raise OutputTruncated(
                    f"{section_id!r} chunk={chunk} unparseable JSON "
                    f"(finish={finish}, out={t_out} tok)") from je
        raise RuntimeError(
            f"model call failed on {section_id!r} after {retries} attempts: "
            f"{last_err}")
