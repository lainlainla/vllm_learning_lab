from __future__ import annotations

import argparse
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "src"))

from vllm_lab.experiments import validate_experiment_name  # noqa: E402


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Create an isolated experiment scaffold.")
    parser.add_argument(
        "--name",
        required=True,
        help="Experiment name, for example exp_002_batching.",
    )
    parser.add_argument("--model", default="Qwen/Qwen3-0.6B", help="Model name.")
    parser.add_argument(
        "--angle",
        default="manual",
        help="Experiment angle, such as serving or sft.",
    )
    return parser.parse_args()


def write_file(path: Path, content: str) -> None:
    if path.exists():
        raise FileExistsError(f"Refusing to overwrite existing file: {path}")
    path.write_text(content, encoding="utf-8")


def main() -> int:
    args = parse_args()
    name = validate_experiment_name(args.name)
    config_path = REPO_ROOT / "configs" / "experiments" / f"{name}.yaml"
    experiment_dir = REPO_ROOT / "experiments" / name

    if config_path.exists() or experiment_dir.exists():
        print(f"ERROR: experiment already exists: {name}", file=sys.stderr)
        return 1

    config_text = f"""experiment_name: {name}
owner: ""
angle: {args.angle}
model_name: {args.model}
output_dir: outputs/runs/{name}
dtype: auto
max_tokens: 128
temperature: 0.7
top_p: 0.95
prompts:
  - "Explain what vLLM is in one paragraph."
"""
    readme_text = f"""# {name}

## Goal

## Hypothesis

## Model

`{args.model}`

## Dataset

## Command

```bash
bash experiments/{name}/command.sh
```

## Metrics

- latency:
- tokens/sec:
- GPU memory:
- output quality:

## Results

## Conclusion

## Follow-up
"""
    command_text = f"""#!/usr/bin/env bash
set -euo pipefail

python scripts/run_offline.py --config configs/experiments/{name}.yaml
"""
    results_text = f"""# Results

## Environment

## Command

```bash
python scripts/run_offline.py --config configs/experiments/{name}.yaml
```

## Run Directory

`outputs/runs/{name}/<run_id>/`

## Output

## Metrics

## Notes
"""

    config_path.write_text(config_text, encoding="utf-8")
    experiment_dir.mkdir(parents=True)
    write_file(experiment_dir / "README.md", readme_text)
    write_file(
        experiment_dir / "config.yaml",
        f"experiment_name: {name}\nconfig_file: configs/experiments/{name}.yaml\n",
    )
    write_file(experiment_dir / "command.sh", command_text)
    write_file(experiment_dir / "results.md", results_text)

    print(f"Created config: {config_path}")
    print(f"Created experiment folder: {experiment_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())