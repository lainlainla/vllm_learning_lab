"""Offline vLLM generation helper."""

from __future__ import annotations

from typing import Any

from vllm_lab.prompts import DEFAULT_PROMPTS


def run_generation(config: dict[str, Any]) -> list[dict[str, str]]:
    """Run vLLM offline generation and return prompt/output pairs."""
    try:
        from vllm import LLM, SamplingParams
    except ImportError as exc:  # pragma: no cover - requires optional GPU stack
        raise RuntimeError(
            "vLLM is not installed or cannot be imported. "
            "Install the project in the target Linux/WSL2 environment first."
        ) from exc

    model_name = str(config.get("model_name", "Qwen/Qwen3-0.6B"))
    prompts = config.get("prompts") or DEFAULT_PROMPTS
    if not isinstance(prompts, list) or not all(isinstance(item, str) for item in prompts):
        raise ValueError("Config key 'prompts' must be a list of strings.")

    sampling_params = SamplingParams(
        max_tokens=int(config.get("max_tokens", 128)),
        temperature=float(config.get("temperature", 0.7)),
        top_p=float(config.get("top_p", 0.95)),
    )

    llm_kwargs: dict[str, Any] = {"model": model_name}
    for key in ("dtype", "max_model_len", "gpu_memory_utilization"):
        if key in config:
            llm_kwargs[key] = config[key]

    llm = LLM(**llm_kwargs)
    outputs = llm.generate(prompts, sampling_params)

    results: list[dict[str, str]] = []
    for output in outputs:
        text = output.outputs[0].text if output.outputs else ""
        results.append({"prompt": output.prompt, "text": text})
    return results
