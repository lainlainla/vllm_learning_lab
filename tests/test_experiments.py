from __future__ import annotations

import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "src"))

from vllm_lab.experiments import (  # noqa: E402
    make_run_context,
    validate_experiment_name,
    write_run_artifacts,
)


def test_validate_experiment_name_rejects_unsafe_names() -> None:
    with pytest.raises(ValueError):
        validate_experiment_name("../bad")

    with pytest.raises(ValueError):
        validate_experiment_name("Exp With Spaces")


def test_make_run_context_creates_isolated_directory(tmp_path: Path) -> None:
    context = make_run_context(
        {"experiment_name": "exp_999_test", "output_dir": "outputs/runs/exp_999_test"},
        repo_root=tmp_path,
        run_id="run_001",
    )

    assert context.run_dir == tmp_path / "outputs/runs/exp_999_test/run_001"
    assert context.run_dir.exists()

    with pytest.raises(FileExistsError):
        make_run_context(
            {"experiment_name": "exp_999_test", "output_dir": "outputs/runs/exp_999_test"},
            repo_root=tmp_path,
            run_id="run_001",
        )


def test_write_run_artifacts(tmp_path: Path) -> None:
    context = make_run_context(
        {"experiment_name": "exp_999_test", "output_dir": "outputs/runs/exp_999_test"},
        repo_root=tmp_path,
        run_id="run_002",
    )

    write_run_artifacts(
        context,
        "experiment_name: exp_999_test\n",
        [{"prompt": "hello", "text": "world"}],
    )

    assert context.config_snapshot.read_text(encoding="utf-8") == "experiment_name: exp_999_test\n"
    assert context.results_jsonl.read_text(encoding="utf-8").strip() == (
        '{"prompt": "hello", "text": "world"}'
    )
    assert "world" in context.outputs_md.read_text(encoding="utf-8")
