# Experiment Isolation

This repository is designed to support many small experiments without letting
them overwrite each other.

## One Experiment, One Identity

Each experiment needs a stable lowercase name:

```text
exp_002_batching
exp_003_serving_latency
exp_004_sft_lora_smoke
```

Use only lowercase letters, numbers, underscores, and hyphens. Do not reuse an
experiment name for a different question.

## Required Files

For each experiment, keep both:

- `configs/experiments/<experiment_name>.yaml`
- `experiments/<experiment_name>/`

The config is the runnable input. The experiment folder is the human record:
goal, hypothesis, command, metrics, results, and follow-up.

## Create A New Experiment

```bash
python scripts/new_experiment.py --name exp_002_batching --angle offline
```

This creates:

- `configs/experiments/exp_002_batching.yaml`
- `experiments/exp_002_batching/README.md`
- `experiments/exp_002_batching/config.yaml`
- `experiments/exp_002_batching/command.sh`
- `experiments/exp_002_batching/results.md`

The script refuses to overwrite an existing experiment.

## Output Isolation

Runtime artifacts are written under:

```text
outputs/runs/<experiment_name>/<run_id>/
```

For offline inference, each run stores:

- `config.yaml`
- `command.txt`
- `results.jsonl`
- `outputs.md`

`outputs/` is ignored by git, so local run artifacts do not pollute commits.
Copy only summaries into `experiments/<experiment_name>/results.md`.

## Parallel Work Rules

- Use separate experiment names for separate research questions.
- Use separate branches for code changes that could affect shared behavior.
- Do not write multiple experiments into the same output directory.
- Do not edit another person's experiment folder unless the PR says so.
- Keep raw data in `data/raw/` and processed data in `data/processed/`; both are
  ignored except for `.gitkeep`.

## Before Merging

Run:

```bash
python scripts/check_env.py
pytest -q
ruff check .
```

For experiment PRs, also attach the command and the key result summary.
