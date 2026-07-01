from __future__ import annotations

import argparse
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "src"))

from vllm_lab.config import load_yaml, require_keys  # noqa: E402
from vllm_lab.experiments import make_run_context, write_run_artifacts  # noqa: E402
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
    config_path = Path(args.config)
    config = load_yaml(config_path)
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

    try:
        context = make_run_context(config, repo_root=REPO_ROOT)
        write_run_artifacts(context, config_path.read_text(encoding="utf-8"), results)
    except Exception as exc:
        print(f"WARNING: could not write run artifacts: {exc}", file=sys.stderr)
    else:
        print(f"\nSaved run artifacts to: {context.run_dir}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
