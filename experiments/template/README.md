# Experiment Template

## Goal

State the single question this experiment answers.

## Hypothesis

Write the expected outcome before running.

## Model

## Dataset

## Config

Link the matching config under `configs/experiments/`.

## Command

```bash
bash experiments/<experiment_name>/command.sh
```

## Output Isolation

Runtime outputs should go under `outputs/runs/<experiment_name>/<run_id>/`. Do not commit those files.

## Metrics

- latency:
- tokens/sec:
- GPU memory:
- output quality:

## Results

Summarize the result here after running. Keep large raw logs in ignored local output folders.

## Conclusion

## Follow-up