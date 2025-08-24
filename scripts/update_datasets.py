#!/usr/bin/env python3
"""Append new records to dataset CSV files.

The script supports two dataset schemas:

* ``profile`` records used by files like ``fake_profiles.csv`` which have
  ``profile_id``, ``sector`` and ``source`` columns.
* ``partnership`` records used by ``mcf_institution_partnerships.csv`` which
  contain ``institution``, ``partner``, ``partnership_type`` and ``source``
  columns.

Example:
    python scripts/update_datasets.py profile datasets/fake_profiles.csv P123 finance open_source
    python scripts/update_datasets.py partnership datasets/mcf_institution_partnerships.csv InstA Part1 research osint
"""

import argparse
import csv
from pathlib import Path

from typing import Iterable, Sequence

import logging

logger = logging.getLogger(__name__)


DEFAULT_CONFIG_PATH = Path(__file__).resolve().parents[1] / "config.yml"


def load_config(config_path: str | Path | None = None) -> dict:
    """Load configuration from a minimal YAML file.

    Only supports mappings of lists of strings (e.g. ``allowed_sectors``).
    """

    path = Path(config_path) if config_path else DEFAULT_CONFIG_PATH
    if not path.exists():
        raise FileNotFoundError(f"Configuration file {path} not found")

    data: dict[str, list[str]] = {}
    current_key: str | None = None
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            if line.endswith(":"):
                current_key = line[:-1]
                data[current_key] = []
            elif line.startswith("-") and current_key:
                data[current_key].append(line[1:].strip())
    return data


def _append_csv_row(
    file_path: str | Path,
    fieldnames: Sequence[str],
    row: dict,
    unique_fields: Iterable[str],
) -> None:
    """Append a row to a CSV file with header insertion and duplicate checks."""

    file_path_obj = Path(file_path)
    if not file_path_obj.parent.exists():
        raise FileNotFoundError(f"Directory {file_path_obj.parent} does not exist")

    existing_keys = set()
    if file_path_obj.exists() and file_path_obj.stat().st_size > 0:
        with open(file_path_obj, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            existing_keys = {
                tuple(r[field] for field in unique_fields) for r in reader
            }

    key = tuple(row[field] for field in unique_fields)
    if key in existing_keys:
        raise ValueError(f"record {key} already exists in {file_path_obj}")

    with open(file_path_obj, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        if not file_path_obj.exists() or file_path_obj.stat().st_size == 0:
            writer.writeheader()
        writer.writerow(row)


def append_partnership(
    file_path: str | Path,
    institution: str,
    partner: str,
    partnership_type: str,
    source: str,
    config_path: str | Path | None = None,
) -> None:
    """Append a partnership record to a dataset CSV file."""

    if not all(
        field.strip() for field in [institution, partner, partnership_type, source]
    ):
        logger.error(
            "institution, partner, partnership_type and source must be non-empty"
        )
        raise ValueError(
            "institution, partner, partnership_type and source must be non-empty"
        )

    # Ensure configuration exists for future options
    load_config(config_path)

    file_path_obj = Path(file_path)
    fieldnames = ["institution", "partner", "partnership_type", "source"]
    existing = set(

    if file_path_obj.exists() and file_path_obj.stat().st_size > 0:
        with open(file_path, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            existing = {(row["institution"], row["partner"]) for row in reader}
    if (institution, partner) in existing:
        logger.error(
            "partnership %s-%s already exists in %s", institution, partner, file_path
        )
        raise ValueError(
            f"partnership {institution}-{partner} already exists in {file_path}"
        )

    with open(file_path, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        if not file_path_obj.exists() or file_path_obj.stat().st_size == 0:
            writer.writeheader()
        writer.writerow(
            {
                "institution": institution,
                "partner": partner,
                "partnership_type": partnership_type,
                "source": source,
            }
        )
    logger.info(
        "Appended partnership for %s-%s to %s", institution, partner, file_path
    )

    fieldnames = ["institution", "partner", "partnership_type", "source"]
    row = {
        "institution": institution,
        "partner": partner,
        "partnership_type": partnership_type,
        "source": source,
    }
    _append_csv_row(file_path, fieldnames, row, ["institution", "partner"])


def append_record(
    file_path: str | Path,
    profile_id: str,
    sector: str,
    source: str,
    config_path: str | Path | None = None,
) -> None:
    """Append a record to a dataset CSV file.

    Parameters
    ----------
    file_path : str
        Path to CSV file.
    profile_id : str
        Unique profile identifier.
    sector : str
        Sector classification.
    source : str
        Origin of the record.
    """
    # Validate inputs
    if not profile_id.strip() or not sector.strip() or not source.strip():
        logger.error("profile_id, sector, and source must be non-empty")
        raise ValueError("profile_id, sector, and source must be non-empty")
    if sector not in ALLOWED_SECTORS:
        logger.error("sector must be one of %s", sorted(ALLOWED_SECTORS))
        raise ValueError(f"sector must be one of {sorted(ALLOWED_SECTORS)}")
    config = load_config(config_path)
    allowed = set(config.get("allowed_sectors", []))
    if sector not in allowed:
        raise ValueError(f"sector must be one of {sorted(allowed)}")

    fieldnames = ["profile_id", "sector", "source"]
    row = {"profile_id": profile_id, "sector": sector, "source": source}
    _append_csv_row(file_path, fieldnames, row, ["profile_id"])

    if file_path_obj.exists() and file_path_obj.stat().st_size > 0:
        with open(file_path, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            existing_ids = {row["profile_id"] for row in reader}
    if profile_id in existing_ids:
        logger.error("profile_id %s already exists in %s", profile_id, file_path)
        raise ValueError(f"profile_id {profile_id} already exists in {file_path}")

    with open(file_path, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        if not file_path_obj.exists() or file_path_obj.stat().st_size == 0:
            writer.writeheader()
        writer.writerow({
            "profile_id": profile_id,
            "sector": sector,
            "source": source,
        })
    logger.info("Appended record for %s to %s", profile_id, file_path)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    parser = argparse.ArgumentParser(
        description="Append a record to a dataset CSV.",
    )
    parser.add_argument(
        "--config",
        default=str(DEFAULT_CONFIG_PATH),
        help="Path to configuration YAML file",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    profile_parser = subparsers.add_parser(
        "profile", help="Append a profile record"
    )
    profile_parser.add_argument("file_path", help="Path to dataset CSV to update")
    profile_parser.add_argument("profile_id", help="Unique profile identifier")
    profile_parser.add_argument("sector", help="Sector classification")
    profile_parser.add_argument("source", help="Source of the record")

    partnership_parser = subparsers.add_parser(
        "partnership", help="Append a partnership record"
    )
    partnership_parser.add_argument(
        "file_path", help="Path to partnership dataset CSV to update"
    )
    partnership_parser.add_argument("institution", help="Name of the institution")
    partnership_parser.add_argument("partner", help="Name of the partner entity")
    partnership_parser.add_argument(
        "partnership_type", help="Type of partnership (e.g. research)"
    )
    partnership_parser.add_argument("source", help="Source of the record")

    args = parser.parse_args()

    if args.command == "profile":
        append_record(
            args.file_path, args.profile_id, args.sector, args.source, args.config
        )
        print(f"Appended record for {args.profile_id} to {args.file_path}")
    else:
        append_partnership(
            args.file_path,
            args.institution,
            args.partner,
            args.partnership_type,
            args.source,
            args.config,
        )
        print(
            f"Appended partnership for {args.institution}-{args.partner} to {args.file_path}"
        )

    try:
        if args.command == "profile":
            append_record(args.file_path, args.profile_id, args.sector, args.source)
            logger.info(
                "Appended record for %s to %s", args.profile_id, args.file_path
            )
        else:
            append_partnership(
                args.file_path,
                args.institution,
                args.partner,
                args.partnership_type,
                args.source,
            )
            logger.info(
                "Appended partnership for %s-%s to %s",
                args.institution,
                args.partner,
                args.file_path,
            )
    except Exception:
        logger.exception("Failed to update dataset")
        raise
