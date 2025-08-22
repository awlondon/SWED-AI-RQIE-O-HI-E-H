#!/usr/bin/env python3
"""Append new records to dataset CSV files.

Example:
    python scripts/update_datasets.py datasets/fake_profiles.csv P123 finance open_source
"""

import argparse
import csv
from pathlib import Path

# Allowed sector classifications for dataset records
ALLOWED_SECTORS = {
    "finance",
    "technology",
    "government",
    "energy",
    "healthcare",
}

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
        raise ValueError("profile_id, sector, and source must be non-empty")
    if sector not in ALLOWED_SECTORS:
        raise ValueError(f"sector must be one of {sorted(ALLOWED_SECTORS)}")

    file_path_obj = Path(file_path)
    fieldnames = ["profile_id", "sector", "source"]
    existing_ids = set()

    if file_path_obj.exists() and file_path_obj.stat().st_size > 0:
        with open(file_path, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            existing_ids = {row["profile_id"] for row in reader}
    if profile_id in existing_ids:
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

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Append a record to a dataset CSV.")
    parser.add_argument("file_path", help="Path to dataset CSV to update")
    parser.add_argument("profile_id", help="Unique profile identifier")
    parser.add_argument("sector", help="Sector classification")
    parser.add_argument("source", help="Source of the record")
    args = parser.parse_args()

    append_record(args.file_path, args.profile_id, args.sector, args.source)
    print(f"Appended record for {args.profile_id} to {args.file_path}")
