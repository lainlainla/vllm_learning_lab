from __future__ import annotations

import argparse
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "src"))

from vllm_lab.config import load_yaml, require_keys  # noqa: E402
from vllm_lab.inference.offline_runner import run_generation  # noqa: E402


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run offline vLLM generation.")
    parser.add_argument(
        "--config",
        default="configs/experiments/exp_001_baseline.yaml",
        help="Path to an experiment YAML config.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    config = load_yaml(args.config)
    require_keys(config, ["model_name"])

    try:
        results = run_generation(config)
    except Exception as exc:
        print(f"ERROR: offline generation failed: {exc}", file=sys.stderr)
        return 1

    for index, item in enumerate(results, start=1):
        print(f"\n--- Prompt {index} ---")
        print(item["prompt"])
        print("\n--- Output ---")
        print(item["text"].strip())

    return 0


if __name__ == "__main__":
    raise SystemExit(main())


