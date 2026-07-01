# Collaboration

This repository is a small two-person learning lab. Keep the workflow simple, stable, and reproducible.

## Branches

- Use `main` for stable, working examples.
- Create short branches for changes, for example `exp/offline-baseline`, `feat/openai-serving`, or `docs/environment-notes`.
- Use separate branches for experiments that change shared scripts or package code.

## Pull Requests

Each PR should explain:

- What changed.
- How to run it.
- What result was observed.
- Whether docs or experiment notes were updated.

## Experiment Isolation Rules

Every meaningful experiment must have a unique experiment name such as `exp_002_batching`.

Each experiment owns:

- `configs/experiments/<experiment_name>.yaml`
- `experiments/<experiment_name>/README.md`
- `experiments/<experiment_name>/command.sh`
- `experiments/<experiment_name>/results.md`
- `outputs/runs/<experiment_name>/<run_id>/` for local runtime artifacts

Do not reuse an experiment folder for a different question. If the model, dataset, serving mode, or measurement goal changes, create a new experiment.

## Creating Experiments

Use the scaffold script:

```bash
python scripts/new_experiment.py --name exp_002_batching --angle offline
```

The script refuses to overwrite existing experiment files. This protects previous work from accidental replacement.

## Runtime Outputs

Offline inference saves local run artifacts under:

```text
outputs/runs/<experiment_name>/<run_id>/
```

A run folder may include `config.yaml`, `command.txt`, `results.jsonl`, and `outputs.md`. These files are ignored by git. Summarize important results in `experiments/<experiment_name>/results.md` before opening a PR.

## Data And Models

Do not commit secrets, tokens, model weights, checkpoints, raw datasets, or processed datasets.

Allowed in git:

- Config files.
- Small documentation examples.
- Result summaries.
- Commands and notes.

Ignored locally:

- `.env`
- `.venv/`
- `/outputs/`
- `/models/`
- `/checkpoints/`
- `data/raw/*`
- `data/processed/*`
- `*.safetensors`, `*.bin`, `*.pt`, `*.pth`

## Ownership

Use PR descriptions or issue comments to assign ownership for:

- Environment setup.
- Offline inference tests.
- Serving tests.
- Training scaffold work.
- Experiment review.

## Review Rules

Before merging, run:

```bash
python scripts/check_env.py
pytest -q
ruff check .
```

For experiment PRs, also include:

- Experiment name.
- Config path.
- Command.
- Output summary.
- Known limitations.

Keep scripts readable. Prefer one small working step over a large untested rewrite.