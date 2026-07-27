from __future__ import annotations

import json
import os
import sys
from pathlib import Path

import nbformat
import pytest
from jupyter_client.kernelspec import KernelSpecManager
from nbclient import NotebookClient

ROOT = Path(__file__).resolve().parents[1]
NOTEBOOK_DIR = ROOT / "notebooks" / "perturbation-response"


def test_six_ordered_notebooks_are_valid_json() -> None:
    notebooks = sorted(path for path in NOTEBOOK_DIR.glob("[0-9][0-9]-*.ipynb"))
    assert [path.name[:2] for path in notebooks] == ["01", "02", "03", "04", "05", "06"]
    for path in notebooks:
        notebook = nbformat.read(path, as_version=4)
        assert notebook.cells
        assert notebook.cells[0].cell_type == "markdown"


def test_gears_colab_is_present_and_pinned() -> None:
    path = NOTEBOOK_DIR / "gears-norman-colab.ipynb"
    notebook = nbformat.read(path, as_version=4)
    source = "\n".join(cell.source for cell in notebook.cells)
    assert "cell-gears==0.1.2" in source
    assert "cell-eval==0.8.1" in source
    assert "--arc-metrics" in source


@pytest.mark.parametrize(
    "path", sorted(path for path in NOTEBOOK_DIR.glob("[0-9][0-9]-*.ipynb"))
)
def test_notebook_executes_offline(path: Path, tmp_path, monkeypatch) -> None:
    python_path = str(ROOT / "src")
    if os.environ.get("PYTHONPATH"):
        python_path = python_path + os.pathsep + os.environ["PYTHONPATH"]
    monkeypatch.setenv("PYTHONPATH", python_path)
    kernel_source = tmp_path / "kernel-source"
    kernel_source.mkdir()
    (kernel_source / "kernel.json").write_text(
        json.dumps(
            {
                "argv": [sys.executable, "-m", "ipykernel_launcher", "-f", "{connection_file}"],
                "display_name": "AIVC Guide Test",
                "language": "python",
            }
        ),
        encoding="utf-8",
    )
    KernelSpecManager().install_kernel_spec(
        str(kernel_source),
        kernel_name="aivc-guide-test",
        prefix=str(tmp_path),
    )
    monkeypatch.setenv("JUPYTER_PATH", str(tmp_path / "share" / "jupyter"))
    notebook = nbformat.read(path, as_version=4)
    client = NotebookClient(
        notebook,
        timeout=120,
        kernel_name="aivc-guide-test",
        resources={"metadata": {"path": str(tmp_path)}},
    )
    client.execute()
