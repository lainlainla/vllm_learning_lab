"""SFT/LoRA scaffold helpers."""

from __future__ import annotations

from typing import Any


def summarize_training_config(config: dict[str, Any]) -> list[str]:
    """Build readable summary lines for the placeholder training entrypoint."""
    lora = config.get("lora", {})
    training = config.get("training", {})

    lines = [
        f"Model: {config.get('model_name', 'not set')}",
        f"Dataset path: {config.get('dataset_path', 'not set')}",
        f"Output directory: {config.get('output_dir', 'not set')}",
        "LoRA settings:",
        f"  r: {lora.get('r', 'not set')}",
        f"  alpha: {lora.get('alpha', 'not set')}",
        f"  dropout: {lora.get('dropout', 'not set')}",
        "Training settings:",
    ]
    for key, value in training.items():
        lines.append(f"  {key}: {value}")
    return lines
