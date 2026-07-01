"""OpenAI-compatible client helpers for the local vLLM server."""

from __future__ import annotations


def chat_once(base_url: str, api_key: str, model: str, message: str) -> str:
    """Send one chat completion request to a vLLM OpenAI-compatible server."""
    try:
        from openai import OpenAI
    except ImportError as exc:  # pragma: no cover - depends on installed deps
        raise RuntimeError(
            "OpenAI Python client is required. Install project dependencies."
        ) from exc

    client = OpenAI(base_url=base_url, api_key=api_key)
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": message}],
    )
    return response.choices[0].message.content or ""
