"""Deterministically migrate the canonical resource catalog from v1 to v2."""

from __future__ import annotations

import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
CATALOG_DIR = ROOT / "catalog"
CATALOG_FILES = (
    "papers.yml",
    "models.yml",
    "datasets.yml",
    "benchmarks.yml",
    "tools-courses-orgs.yml",
)

MODALITY_MAP = {
    "CITE-seq": "protein",
    "CRISPR": "scRNA-seq",
    "CRISPRa": "scRNA-seq",
    "CRISPRi": "scRNA-seq",
    "biochemical networks": "bulk-omics",
    "chemical perturbation": "scRNA-seq",
    "gene graph": "scRNA-seq",
    "gene graphs": "scRNA-seq",
    "genetic perturbation": "scRNA-seq",
    "genome": "bulk-omics",
    "immunofluorescence imaging": "imaging",
    "multi-omics": "multiome",
    "perturb-seq": "scRNA-seq",
    "protein annotation": "protein",
    "protein sequence": "protein",
    "proteomics": "protein",
    "regulatory knowledge": "scRNA-seq",
    "sequence": "bulk-omics",
    "single-cell": "scRNA-seq",
    "single-cell multi-omics": "multiome",
    "snRNA-seq": "scRNA-seq",
    "spatial": "spatial-transcriptomics",
    "spatial transcriptomics": "spatial-transcriptomics",
}

SPECIES_MAP = {
    "Mycoplasma genitalium": "bacteria",
}

CORE_IDS = {
    "aivc-vision-2024",
    "perturb-seq-dixit-2016",
    "norman-2019",
    "replogle-2022",
    "simple-controls-2025",
    "model-scvi",
    "model-gears",
    "model-scgpt",
    "model-state",
    "dataset-cellxgene-census",
    "dataset-human-cell-atlas",
    "dataset-scperturb",
    "dataset-norman",
    "dataset-arc-vcc-2025",
    "benchmark-vcc-2025",
    "benchmark-cell-eval",
    "tool-anndata",
    "tool-scanpy",
    "tool-scvi-tools",
    "course-single-cell-best-practices",
}

LINK_FIXES = {
    "benchmark-perturbench": {
        "paper": "https://arxiv.org/abs/2408.10609",
        "code": "https://github.com/altoslabs/perturbench",
        "project": "https://openreview.net/forum?id=PPPDuyiZaG",
    },
    "model-cpa": {"paper": "https://doi.org/10.15252/msb.202211517"},
    "model-scprint": {"paper": "https://doi.org/10.1038/s41467-025-58699-1"},
    "tool-pertpy": {"paper": "https://doi.org/10.1038/s41592-025-02909-7"},
    "dataset-cellxgene-census": {
        "data": "https://registry.opendata.aws/cellxgene-census/",
        "project": "https://chanzuckerberg.github.io/cellxgene-census/",
    },
    "dataset-replogle": {
        "code": "https://gwps.wi.mit.edu/",
        "project": "https://gwps.wi.mit.edu/",
    },
    "benchmark-openproblems-multiome": {
        "project": "https://openproblems.bio/events/2021-09_neurips"
    },
    "dataset-human-protein-atlas-cell": {
        "data": "https://www.proteinatlas.org/humanproteome/subcellular/data",
        "project": "https://www.proteinatlas.org/humanproteome/subcellular",
    },
}


def _perturbation_types(entry: dict) -> list[str]:
    text = " ".join(
        [
            entry["id"],
            entry.get("context", ""),
            *entry.get("tasks", []),
            *entry.get("modalities", []),
        ]
    ).lower()
    values: list[str] = []
    if "crispri" in text or "knockdown" in text:
        values.append("genetic-knockdown")
    if "crispra" in text or "activation" in text:
        values.append("genetic-activation")
    if "knockout" in text or ("crispr" in text and not values):
        values.append("genetic-knockout")
    if any(token in text for token in ("chemical", "drug", "dose")):
        values.append("chemical")
    if "disease" in text:
        values.append("disease-state")
    return values or ["none"]


def _compute_tier(value: str) -> str:
    lowered = value.lower()
    if "multi-gpu" in lowered or "多gpu" in lowered or "多 gpu" in lowered:
        return "multi-gpu"
    if "gpu" in lowered:
        return "single-gpu"
    if "cpu" in lowered:
        return "cpu"
    return "unknown"


def _evidence_stage(kind: str, entry: dict) -> str:
    if kind in {"datasets", "tools-courses-orgs"}:
        return "deployed" if entry["publication_status"] == "product" else "not-applicable"
    if entry["publication_status"] == "technical-report":
        return "concept"
    if "prospective" in entry.get("summary_zh", "").lower():
        return "prospective"
    return "in-silico"


def migrate_entry(kind: str, entry: dict) -> dict:
    migrated = dict(entry)
    migrated["modalities"] = list(
        dict.fromkeys(MODALITY_MAP.get(value, value) for value in entry["modalities"])
    )
    migrated["perturbation_types"] = _perturbation_types(entry)
    migrated["species"] = list(
        dict.fromkeys(SPECIES_MAP.get(value, value) for value in entry["species"])
    )
    migrated["recommendation"] = (
        "core"
        if entry["id"] in CORE_IDS
        else "reference"
        if entry["recommendation"] == "reference"
        else "recommended"
    )
    migrated["evidence_stage"] = _evidence_stage(kind, entry)
    migrated["compute_tier"] = _compute_tier(entry["compute"])
    migrated["verification_status"] = "verified"
    if entry["id"] in LINK_FIXES:
        migrated["links"] = {**entry["links"], **LINK_FIXES[entry["id"]]}

    ordered_fields = (
        "id",
        "title_zh",
        "title_en",
        "year",
        "category",
        "summary_zh",
        "tasks",
        "modalities",
        "perturbation_types",
        "species",
        "context",
        "links",
        "publication_status",
        "reproducibility",
        "recommendation",
        "evidence_stage",
        "license",
        "compute",
        "compute_tier",
        "limitations",
        "last_verified",
        "verification_status",
    )
    return {field: migrated[field] for field in ordered_fields}


def main() -> int:
    for filename in CATALOG_FILES:
        path = CATALOG_DIR / filename
        payload = yaml.safe_load(path.read_text(encoding="utf-8"))
        payload["catalog_version"] = 2
        payload["entries"] = [
            migrate_entry(payload["kind"], entry) for entry in payload["entries"]
        ]
        path.write_text(
            yaml.safe_dump(
                payload,
                allow_unicode=True,
                sort_keys=False,
                width=100,
            ),
            encoding="utf-8",
            newline="\n",
        )
    print("Catalog migration to v2 completed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
