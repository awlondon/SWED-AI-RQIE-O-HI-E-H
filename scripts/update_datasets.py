#!/usr/bin/env python3
"""Append new records to dataset CSV files.

Example:
    python scripts/update_datasets.py datasets/fake_profiles.csv P123 finance open_source
"""

import argparse
import csv
from pathlib import Path

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
    fieldnames = ["profile_id", "sector", "source"]
    file_exists = Path(file_path).exists()
    with open(file_path, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        if not file_exists or f.tell() == 0:
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
