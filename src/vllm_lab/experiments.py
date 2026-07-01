"""Helpers for isolated experiment runs."""

from __future__ import annotations

import json
import os
import re
import shlex
import sys
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any

EXPERIMENT_NAME_RE = re.compile(r"^[a-z0-9][a-z0-9_-]{2,63}$")


@dataclass(frozen=True)
class RunContext:
    """Filesystem locations for one isolated run."""

    experiment_name: str
    run_id: str
    run_dir: Path
    config_snapshot: Path
    command_file: Path
    results_jsonl: Path
    outputs_md: Path


def validate_experiment_name(name: str) -> str:
    """Validate and return a safe experiment name."""
    if not EXPERIMENT_NAME_RE.fullmatch(name):
        raise ValueError(
            "Experiment name must be 3-64 chars and use lowercase letters, "
            "numbers, underscores, or hyphens."
        )
    return name


def default_run_id() -> str:
    """Return a sortable run id. Environment override helps reproducible tests."""
    override = os.getenv("VLLM_LAB_RUN_ID")
    if override:
        return validate_experiment_name(override)
    return datetime.now().strftime("%Y%m%d_%H%M%S")


def make_run_context(
    config: dict[str, Any],
    repo_root: Path,
    run_id: str | None = None,
) -> RunContext:
    """Create an isolated run directory for an experiment."""
    experiment_name = validate_experiment_name(str(config.get("experiment_name", "manual_run")))
    resolved_run_id = validate_experiment_name(run_id or default_run_id())
    output_root = Path(config.get("output_dir", f"outputs/runs/{experiment_name}"))
    if not output_root.is_absolute():
        output_root = repo_root / output_root

    run_dir = output_root / resolved_run_id
    if run_dir.exists():
        raise FileExistsError(f"Run directory already exists: {run_dir}")

    run_dir.mkdir(parents=True)
    return RunContext(
        experiment_name=experiment_name,
        run_id=resolved_run_id,
        run_dir=run_dir,
        config_snapshot=run_dir / "config.yaml",
        command_file=run_dir / "command.txt",
        results_jsonl=run_dir / "results.jsonl",
        outputs_md=run_dir / "outputs.md",
    )


def write_run_artifacts(
    context: RunContext,
    config_text: str,
    results: list[dict[str, str]],
) -> None:
    """Persist config, command, and outputs for one run."""
    context.config_snapshot.write_text(config_text, encoding="utf-8")
    command = " ".join(shlex.quote(part) for part in sys.argv)
    context.command_file.write_text(command + "\n", encoding="utf-8")

    with context.results_jsonl.open("w", encoding="utf-8") as file:
        for item in results:
            file.write(json.dumps(item, ensure_ascii=False) + "\n")

    lines = [
        f"# {context.experiment_name}",
        "",
        f"Run ID: `{context.run_id}`",
        "",
    ]
    for index, item in enumerate(results, start=1):
        lines.extend(
            [
                f"## Prompt {index}",
                "",
                item["prompt"],
                "",
                "## Output",
                "",
                item["text"].strip(),
                "",
            ]
        )
    context.outputs_md.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
