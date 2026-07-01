from __future__ import annotations

import os
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "src"))

from vllm_lab.inference.openai_client import chat_once  # noqa: E402


def main() -> int:
    base_url = os.getenv("VLLM_BASE_URL", "http://localhost:8000/v1")
    api_key = os.getenv("VLLM_API_KEY", "token-abc123")
    model = os.getenv("DEFAULT_MODEL", "Qwen/Qwen3-0.6B")
    message = "Explain vLLM continuous batching in two sentences."

    try:
        text = chat_once(base_url=base_url, api_key=api_key, model=model, message=message)
    except Exception as exc:
        print(f"ERROR: chat request failed: {exc}", file=sys.stderr)
        return 1

    print(text.strip())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

