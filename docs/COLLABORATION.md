# Collaboration

This repository is a small two-person learning lab. Keep the workflow simple.

## Branches

- Use `main` for stable, working examples.
- Create short branches for changes, for example `exp/offline-baseline` or
  `docs/environment-notes`.

## Pull Requests

Each PR should explain:

- What changed.
- How to run it.
- What result was observed.
- Whether docs or experiment notes were updated.

## Experiment Logging

Every meaningful experiment should have:

- A YAML config under `configs/experiments/`.
- A folder under `experiments/`.
- The exact command in `command.sh`.
- Observed output and notes in `results.md`.

## Ownership

Use PR descriptions or issue comments to assign ownership for:

- Environment setup.
- Offline inference tests.
- Serving tests.
- Training scaffold work.
- Experiment review.

## Review Rules

- Do not commit secrets, tokens, model weights, checkpoints, or raw datasets.
- Keep scripts readable.
- Prefer one small working step over a large untested rewrite.
