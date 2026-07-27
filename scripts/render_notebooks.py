"""Render source notebooks to deterministic MkDocs pages."""

from __future__ import annotations

import argparse
from pathlib import Path

import nbformat

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "notebooks" / "perturbation-response"
TARGET = ROOT / "docs" / "tutorials" / "perturbation-response" / "notebooks"
REPO = "https://github.com/methylation5mc2026-jpg/AI-Virtual-Cell-Guide"


def render(path: Path) -> str:
    notebook = nbformat.read(path, as_version=4)
    source_url = f"{REPO}/blob/main/notebooks/perturbation-response/{path.name}"
    colab_url = (
        "https://colab.research.google.com/github/"
        "methylation5mc2026-jpg/AI-Virtual-Cell-Guide/blob/main/"
        f"notebooks/perturbation-response/{path.name}"
    )
    chunks = [
        "---",
        f"title: {path.stem}",
        "hide:",
        "  - toc",
        "---",
        "",
        '<div class="notebook-actions" markdown>',
        f"[查看源 Notebook]({source_url}){{ .md-button }}",
        f"[在 Colab 打开]({colab_url}){{ .md-button .md-button--primary }}",
        "</div>",
        "",
        '!!! note "在线渲染说明"',
        "    本页由源 Notebook 自动生成。代码输出以实际运行为准；普通合并只执行离线六章，",
        "    GEARS 页面需在 Colab GPU 中按运行清单复现。",
        "",
    ]
    for cell in notebook.cells:
        if cell.cell_type == "markdown":
            chunks.extend([cell.source.rstrip(), ""])
        elif cell.cell_type == "code":
            chunks.extend(["```python", cell.source.rstrip(), "```", ""])
    return "\n".join(chunks).rstrip() + "\n"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    failures: list[str] = []
    if not args.check:
        TARGET.mkdir(parents=True, exist_ok=True)
    for notebook_path in sorted(SOURCE.glob("*.ipynb")):
        output = TARGET / f"{notebook_path.stem}.md"
        expected = render(notebook_path)
        if args.check:
            if not output.exists() or output.read_text(encoding="utf-8") != expected:
                failures.append(str(output.relative_to(ROOT)))
        else:
            output.write_text(expected, encoding="utf-8")
    if failures:
        raise SystemExit("Notebook render is stale: " + ", ".join(failures))
    print(f"Notebook pages {'checked' if args.check else 'rendered'}: 7")


if __name__ == "__main__":
    main()
