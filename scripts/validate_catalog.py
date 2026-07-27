"""Validate the canonical AIVC catalog, schema and controlled vocabularies."""

from __future__ import annotations

import datetime as dt
import json
import sys
from pathlib import Path
from urllib.parse import urlparse

import yaml
from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]
CATALOG_DIR = ROOT / "catalog"
SCHEMA_PATH = CATALOG_DIR / "schema.json"
VOCABULARIES_PATH = CATALOG_DIR / "vocabularies.yml"
CATALOG_FILES = (
    "papers.yml",
    "models.yml",
    "datasets.yml",
    "benchmarks.yml",
    "tools-courses-orgs.yml",
)
EXPECTED_KINDS = {Path(name).stem for name in CATALOG_FILES}


def _is_https_url(value: str) -> bool:
    parsed = urlparse(value)
    return parsed.scheme == "https" and bool(parsed.netloc)


def validate_catalog() -> list[str]:
    errors: list[str] = []
    seen_ids: set[str] = set()
    found_kinds: set[str] = set()

    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    vocabularies = yaml.safe_load(VOCABULARIES_PATH.read_text(encoding="utf-8"))
    validator = Draft202012Validator(schema, format_checker=FormatChecker())

    for filename in CATALOG_FILES:
        path = CATALOG_DIR / filename
        if not path.exists():
            errors.append(f"missing catalog file: {filename}")
            continue
        payload = yaml.safe_load(path.read_text(encoding="utf-8"))
        kind = payload.get("kind") if isinstance(payload, dict) else None
        found_kinds.add(kind)
        if kind != path.stem:
            errors.append(f"{filename}: kind must match filename")

        normalized_payload = json.loads(json.dumps(payload, default=str))
        for failure in sorted(
            validator.iter_errors(normalized_payload), key=lambda item: list(item.path)
        ):
            location = ".".join(str(part) for part in failure.absolute_path) or "<root>"
            errors.append(f"{filename}:{location}: {failure.message}")

        entries = payload.get("entries", []) if isinstance(payload, dict) else []
        for index, entry in enumerate(entries):
            if not isinstance(entry, dict):
                continue
            entry_id = entry.get("id")
            if entry_id in seen_ids:
                errors.append(f"{filename}:entries[{index}]: duplicate id {entry_id}")
            elif isinstance(entry_id, str):
                seen_ids.add(entry_id)

            year = entry.get("year")
            if isinstance(year, int) and year > dt.date.today().year:
                errors.append(f"{filename}:{entry_id}: year is in the future")
            verified = entry.get("last_verified")
            try:
                verified_date = dt.date.fromisoformat(str(verified))
                if verified_date > dt.date.today():
                    errors.append(f"{filename}:{entry_id}: last_verified is in the future")
            except ValueError:
                pass

            for field, vocabulary in (
                ("modalities", "modalities"),
                ("perturbation_types", "perturbation_types"),
                ("species", "species"),
            ):
                unknown = sorted(set(entry.get(field, [])) - set(vocabularies[vocabulary]))
                if unknown:
                    errors.append(
                        f"{filename}:{entry_id}: unknown {field}: {', '.join(unknown)}"
                    )
            for link_name, value in entry.get("links", {}).items():
                if value is not None and (
                    not isinstance(value, str) or not _is_https_url(value)
                ):
                    errors.append(
                        f"{filename}:{entry_id}: links.{link_name} must be HTTPS or null"
                    )

    if found_kinds != EXPECTED_KINDS:
        errors.append(
            "catalog kinds must be exactly " + ", ".join(sorted(EXPECTED_KINDS))
        )

    core_count = 0
    for filename in CATALOG_FILES:
        path = CATALOG_DIR / filename
        if path.exists():
            payload = yaml.safe_load(path.read_text(encoding="utf-8"))
            core_count += sum(
                entry.get("recommendation") == "core"
                for entry in payload.get("entries", [])
            )
    if core_count > 20:
        errors.append(f"catalog has {core_count} core entries; the v0.2 maximum is 20")
    return errors


def main() -> int:
    errors = validate_catalog()
    if errors:
        print("Catalog validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    count = sum(
        len(
            yaml.safe_load((CATALOG_DIR / filename).read_text(encoding="utf-8"))[
                "entries"
            ]
        )
        for filename in CATALOG_FILES
    )
    print(f"Catalog validation passed: {count} entries (schema v2)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
