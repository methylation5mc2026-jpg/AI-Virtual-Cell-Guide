from __future__ import annotations

import importlib.util
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]


def _load_script(name: str):
    path = ROOT / "scripts" / name
    spec = importlib.util.spec_from_file_location(path.stem, path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_catalog_schema_and_minimum_entry_count() -> None:
    validator = _load_script("validate_catalog.py")
    assert validator.validate_catalog() == []
    payloads = [
        yaml.safe_load(path.read_text(encoding="utf-8"))
        for path in (ROOT / "catalog").glob("*.yml")
    ]
    count = sum(len(payload["entries"]) for payload in payloads if "entries" in payload)
    assert count == 100
    schema = yaml.safe_load((ROOT / "catalog" / "schema.json").read_text(encoding="utf-8"))
    assert schema["properties"]["catalog_version"]["const"] == 2


def test_generated_catalog_pages_are_current(tmp_path) -> None:
    generator = _load_script("generate_catalog.py")
    for path in sorted((ROOT / "catalog").glob("*.yml")):
        payload = yaml.safe_load(path.read_text(encoding="utf-8"))
        if "entries" not in payload:
            continue
        expected = generator.render(payload["kind"], payload["entries"])
        actual = (ROOT / "docs" / "catalog" / f"{payload['kind']}.md").read_text(
            encoding="utf-8"
        )
        assert actual == expected
