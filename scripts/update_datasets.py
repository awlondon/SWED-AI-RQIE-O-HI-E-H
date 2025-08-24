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
import logging

logger = logging.getLogger(__name__)

# Allowed sector classifications for dataset records
ALLOWED_SECTORS = {
    "finance",
    "technology",
    "government",
    "energy",
    "healthcare",
}


def append_partnership(
    file_path: str,
    institution: str,
    partner: str,
    partnership_type: str,
    source: str,
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

    file_path_obj = Path(file_path)
    fieldnames = ["institution", "partner", "partnership_type", "source"]
    existing = set()

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

def append_record(file_path: str, profile_id: str, sector: str, source: str) -> None:
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

    file_path_obj = Path(file_path)
    fieldnames = ["profile_id", "sector", "source"]
    existing_ids = set()

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
        description="Append a record to a dataset CSV."
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
