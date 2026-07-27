"""Generate responsive catalog documentation from the canonical YAML files."""

from __future__ import annotations

import argparse
import html
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
CATALOG_DIR = ROOT / "catalog"
DEFAULT_OUTPUT_DIR = ROOT / "docs" / "catalog"
CATALOG_FILES = (
    "papers.yml",
    "models.yml",
    "datasets.yml",
    "benchmarks.yml",
    "tools-courses-orgs.yml",
)

TITLE_MAP = {
    "papers": "论文目录",
    "models": "模型目录",
    "datasets": "数据集目录",
    "benchmarks": "基准目录",
    "tools-courses-orgs": "工具、课程与组织目录",
}
LABEL_MAP = {
    "core": "必读",
    "recommended": "推荐",
    "reference": "参考",
    "peer-reviewed": "同行评审",
    "preprint": "预印本",
    "technical-report": "技术报告",
    "product": "产品/项目",
    "code-and-data": "代码＋数据",
    "weights-and-code": "权重＋代码",
    "code-only": "仅代码",
    "data-only": "仅数据",
    "documentation-only": "仅文档",
    "closed": "闭源",
    "verified": "已核验",
    "manual-review": "人工复核",
    "unreachable": "暂不可达",
}
LINK_LABELS = {
    "paper": "论文",
    "code": "代码",
    "weights": "权重",
    "data": "数据",
    "project": "主页",
}


def _escaped(value: object) -> str:
    return html.escape(str(value), quote=True)


def _link_list(links: dict[str, str | None]) -> str:
    rendered = [
        (
            f'<a class="resource-link" href="{_escaped(value)}" '
            f'rel="noopener">{LINK_LABELS[name]}</a>'
        )
        for name, value in links.items()
        if name in LINK_LABELS and value
    ]
    return " ".join(rendered) if rendered else "<span>暂无公开链接</span>"


def _badges(entry: dict) -> str:
    values = [
        (entry["recommendation"], LABEL_MAP[entry["recommendation"]]),
        (entry["publication_status"], LABEL_MAP[entry["publication_status"]]),
        (entry["reproducibility"], LABEL_MAP[entry["reproducibility"]]),
        (entry["verification_status"], LABEL_MAP[entry["verification_status"]]),
    ]
    return "".join(
        f'<span class="resource-badge resource-badge--{_escaped(key)}">{_escaped(label)}</span>'
        for key, label in values
    )


def _card(entry: dict) -> str:
    modalities = ", ".join(entry["modalities"])
    tasks = ", ".join(entry["tasks"])
    perturbations = ", ".join(entry["perturbation_types"])
    search = " ".join(
        [
            entry["title_zh"],
            entry["title_en"],
            entry["category"],
            tasks,
            modalities,
            perturbations,
            entry["context"],
        ]
    ).lower()
    return "\n".join(
        [
            (
                f'<article class="resource-card" id="{_escaped(entry["id"])}" '
                f'data-search="{_escaped(search)}" '
                f'data-recommendation="{_escaped(entry["recommendation"])}" '
                f'data-status="{_escaped(entry["publication_status"])}" '
                f'data-modalities="{_escaped("|".join(entry["modalities"]))}">'
            ),
            '  <div class="resource-card__header">',
            "    <div>",
            (
                f'      <h2><a class="headerlink" href="#{_escaped(entry["id"])}">'
                f'{_escaped(entry["title_zh"])}</a></h2>'
            ),
            (
                f'      <p class="resource-card__english">{_escaped(entry["title_en"])}'
                f' · {entry["year"]} · {_escaped(entry["category"])}</p>'
            ),
            "    </div>",
            f'    <div class="resource-badges">{_badges(entry)}</div>',
            "  </div>",
            f'  <p class="resource-card__summary">{_escaped(entry["summary_zh"])}</p>',
            '  <dl class="resource-card__facts">',
            f"    <dt>任务</dt><dd>{_escaped(tasks)}</dd>",
            f"    <dt>模态</dt><dd>{_escaped(modalities)}</dd>",
            f"    <dt>扰动</dt><dd>{_escaped(perturbations)}</dd>",
            f"    <dt>物种/背景</dt><dd>{_escaped(', '.join(entry['species']))}；"
            f"{_escaped(entry['context'])}</dd>",
            "  </dl>",
            f'  <div class="resource-card__links">{_link_list(entry["links"])}</div>',
            '  <details class="resource-card__details">',
            "    <summary>复现条件、许可证与限制</summary>",
            "    <ul>",
            f"      <li><strong>计算需求：</strong>{_escaped(entry['compute'])} "
            f"({_escaped(entry['compute_tier'])})</li>",
            f"      <li><strong>证据阶段：</strong>{_escaped(entry['evidence_stage'])}</li>",
            f"      <li><strong>许可证：</strong>{_escaped(entry['license'])}</li>",
            f"      <li><strong>已知限制：</strong>{_escaped(entry['limitations'])}</li>",
            f"      <li><strong>最后核验：</strong>{_escaped(entry['last_verified'])} "
            f"· {_escaped(LABEL_MAP[entry['verification_status']])}</li>",
            "    </ul>",
            "  </details>",
            "</article>",
        ]
    )


def render(kind: str, entries: list[dict]) -> str:
    ordered = sorted(
        entries,
        key=lambda item: (
            {"core": 0, "recommended": 1, "reference": 2}[item["recommendation"]],
            -item["year"],
            item["title_en"].lower(),
        ),
    )
    last_reviewed = max(str(entry["last_verified"]) for entry in ordered)
    modality_options = sorted(
        {modality for entry in ordered for modality in entry["modalities"]}
    )
    lines = [
        "---",
        f"title: {TITLE_MAP[kind]}",
        "summary: 由结构化 YAML 生成的可核验、可筛选资源目录。",
        "level: reference",
        "prerequisites: []",
        "estimated_time: 按需查阅",
        f"last_reviewed: {last_reviewed}",
        "---",
        "",
        "<!-- 此文件由 scripts/generate_catalog.py 自动生成，请勿手工编辑。 -->",
        "",
        f"# {TITLE_MAP[kind]}",
        "",
        f"共 **{len(ordered)}** 条。正文精选主线资源；本页提供完整元数据与限制。",
        "",
        '<div class="catalog-controls" role="search" aria-label="筛选资源">',
        '  <label>搜索<input class="catalog-search" type="search" '
        'placeholder="标题、任务、模态或背景" autocomplete="off"></label>',
        '  <label>推荐等级<select class="catalog-filter" data-field="recommendation">',
        '    <option value="">全部</option><option value="core">必读</option>',
        '    <option value="recommended">推荐</option><option value="reference">参考</option>',
        "  </select></label>",
        '  <label>发表状态<select class="catalog-filter" data-field="status">',
        '    <option value="">全部</option><option value="peer-reviewed">同行评审</option>',
        '    <option value="preprint">预印本</option>',
        '    <option value="technical-report">技术报告</option>',
        '    <option value="product">产品/项目</option>',
        "  </select></label>",
        '  <label>模态<select class="catalog-filter" data-field="modalities">',
        '    <option value="">全部</option>',
        *[
            f'    <option value="{_escaped(value)}">{_escaped(value)}</option>'
            for value in modality_options
        ],
        "  </select></label>",
        "</div>",
        (
            f'<p class="catalog-result-count" role="status" aria-live="polite">'
            f"显示 {len(ordered)} / {len(ordered)} 条</p>"
        ),
        '<div class="resource-grid">',
        *[_card(entry) for entry in ordered],
        "</div>",
        '<p class="catalog-empty" hidden>没有匹配的资源，请调整筛选条件。</p>',
        "",
    ]
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="Fail if generated pages are stale")
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    args = parser.parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)

    stale: list[str] = []
    for filename in CATALOG_FILES:
        path = CATALOG_DIR / filename
        payload = yaml.safe_load(path.read_text(encoding="utf-8"))
        kind = payload["kind"]
        target = args.output_dir / f"{kind}.md"
        content = render(kind, payload["entries"])
        if args.check:
            if not target.exists() or target.read_text(encoding="utf-8") != content:
                stale.append(str(target.relative_to(ROOT)))
        else:
            target.write_text(content, encoding="utf-8", newline="\n")

    if stale:
        print("Generated catalog pages are stale:")
        for path in stale:
            print(f"- {path}")
        return 1
    print("Catalog pages are up to date")
    return 0


if __name__ == "__main__":
    sys.exit(main())
