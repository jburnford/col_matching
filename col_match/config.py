"""Connection + tunables for col_matching.

Mirrors col_pipeline's credential resolution so there is a single source of
credentials: env vars first, then this repo's .env, then the production sibling
repo's .env. Read-only by intent — there is no write path here.
"""

from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path

try:
    from dotenv import load_dotenv as _load_dotenv
except ImportError:  # python-dotenv optional
    _load_dotenv = None

REPO_ROOT = Path(__file__).parent.parent
DEFAULT_PROD_URI = "bolt://206.12.90.118:7687"


def _ensure_dotenv_loaded() -> None:
    """Load .env idempotently; first value found wins (no override)."""
    if _load_dotenv is None:
        return
    for candidate in (
        Path.cwd() / ".env",
        REPO_ROOT / ".env",
        Path.home() / "textasdatacolonialofficelist" / ".env",
    ):
        if candidate.exists():
            _load_dotenv(candidate, override=False)


DEFAULT_CORPUS_DIR = str(
    Path.home() / "colonialofficelist" / "historical_document_pipeline" / "processed_pdfs"
)

# Per-colony staff-list OCR, segmented by edition year:
# {source_ocr_dir}/{year}_manual_parsed/{COLONY}.txt. Read-only; used by the
# recovery pipeline to locate staff-list rows the graph extraction missed.
DEFAULT_SOURCE_OCR_DIR = str(Path.home() / "textasdatacolonialofficelist")


@dataclass(frozen=True)
class Config:
    neo4j_uri: str
    neo4j_user: str
    neo4j_password: str
    neo4j_database: str | None = None

    # Default cluster gate: same threshold col_pipeline uses to seed persons.
    max_uncertainty: float = 0.50

    # services-section pipeline
    google_api_key: str = ""
    corpus_dir: str = DEFAULT_CORPUS_DIR
    source_ocr_dir: str = DEFAULT_SOURCE_OCR_DIR
    data_dir: str = str(REPO_ROOT / "data" / "services")

    # extraction backfill (LLM staff-list extraction of the section worklist).
    # Metered API — a hard cap + on-disk ledger are mandatory. Slugs are
    # placeholders: verify against https://openrouter.ai/api/v1/models before
    # the first spend. Never hard-code the key; load OPENROUTER_API_KEY from a
    # gitignored .env.
    openrouter_api_key: str = ""
    backfill_model: str = "deepseek/deepseek-v4-flash"          # default tier
    backfill_escalate_model: str = "deepseek/deepseek-v4-pro"   # escalation tier
    backfill_cap_usd: float = 5.0
    backfill_max_output_tokens: int = 16000
    ollama_host: str = "http://localhost:11434"                 # Spark fallback

    @classmethod
    def from_env(cls, **overrides) -> "Config":
        _ensure_dotenv_loaded()
        uri = (
            os.environ.get("NEO4J_PROD_URI")
            or os.environ.get("NEO4J_URI")
            or DEFAULT_PROD_URI
        )
        user = os.environ.get("NEO4J_PROD_USER") or os.environ.get("NEO4J_USER") or "neo4j"
        pw = os.environ.get("NEO4J_PROD_PASSWORD") or os.environ.get("NEO4J_PASSWORD") or ""
        db = os.environ.get("NEO4J_DATABASE") or None
        kwargs = dict(
            neo4j_uri=uri,
            neo4j_user=user,
            neo4j_password=pw,
            neo4j_database=db,
            google_api_key=os.environ.get("GOOGLE_API_KEY", ""),
            corpus_dir=os.environ.get("COL_CORPUS_DIR", DEFAULT_CORPUS_DIR),
            source_ocr_dir=os.environ.get("COL_SOURCE_OCR_DIR", DEFAULT_SOURCE_OCR_DIR),
            data_dir=os.environ.get("COL_SERVICES_DATA_DIR", str(REPO_ROOT / "data" / "services")),
            openrouter_api_key=os.environ.get("OPENROUTER_API_KEY", ""),
            backfill_model=os.environ.get("COL_BACKFILL_MODEL", "deepseek/deepseek-v4-flash"),
            backfill_escalate_model=os.environ.get(
                "COL_BACKFILL_ESCALATE_MODEL", "deepseek/deepseek-v4-pro"),
            backfill_cap_usd=float(os.environ.get("COL_BACKFILL_CAP_USD", "5")),
            ollama_host=os.environ.get("OLLAMA_HOST", "http://localhost:11434"),
        )
        kwargs.update(overrides)
        return cls(**kwargs)
