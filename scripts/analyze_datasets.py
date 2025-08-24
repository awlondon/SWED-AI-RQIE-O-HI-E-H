#!/usr/bin/env python3
"""Generate summary statistics for dataset files.

Reads all CSV and JSON files in the ``datasets`` directory and writes a
summary of record counts to ``datasets/analysis_summary.md``. Counts are
computed for every column in each dataset. If a dataset does not include any
known grouping columns a warning is emitted but counts are still produced for
all columns.
"""

from collections import Counter, defaultdict
import csv
import json
import logging
from pathlib import Path
from typing import Dict, List, Tuple


KNOWN_COLUMNS = {"sector", "institution"}


def analyze_datasets(dataset_dir: str = "datasets") -> List[Tuple[str, int, Dict[str, Counter]]]:
    """Return record totals and grouped counts for each dataset."""
    dataset_path = Path(dataset_dir)
    results: List[Tuple[str, int, Dict[str, Counter]]] = []
    for data_file in sorted(dataset_path.glob("*")):
        if data_file.suffix not in {".csv", ".json"}:
            logging.warning("Skipping unsupported file: %s", data_file.name)
            continue

        counts: Dict[str, Counter] = defaultdict(Counter)
        headers: List[str] = []
        total = 0

        if data_file.suffix == ".csv":
            with open(data_file, newline="", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                headers = reader.fieldnames or []
                for row in reader:
                    for header in headers:
                        counts[header][row.get(header, "")] += 1
                    total += 1
        else:  # JSON
            try:
                data = json.loads(data_file.read_text(encoding="utf-8") or "[]")
            except json.JSONDecodeError:
                logging.warning("Failed to parse %s", data_file.name)
                results.append((data_file.name, total, dict(counts)))
                continue
            if not isinstance(data, list):
                logging.warning("%s does not contain a JSON array", data_file.name)
                results.append((data_file.name, total, dict(counts)))
                continue
            headers = sorted({k for obj in data if isinstance(obj, dict) for k in obj.keys()})
            for obj in data:
                if not isinstance(obj, dict):
                    logging.warning("Skipping non-object entry in %s", data_file.name)
                    continue
                for header in headers:
                    counts[header][obj.get(header, "")] += 1
                total += 1

        if headers and not (set(headers) & KNOWN_COLUMNS):
            logging.warning(
                "Unrecognized columns in %s: %s", data_file.name, ", ".join(headers)
            )

        results.append((data_file.name, total, dict(counts)))
    return results


def format_summary(results: List[Tuple[str, int, Dict[str, Counter]]]) -> str:
    """Format analysis results as markdown."""
    lines = ["# Dataset Summary", ""]
    for filename, total, counts in results:
        lines.append(f"## {filename}")
        lines.append(f"- Total records: {total}")
        for column in sorted(counts):
            lines.append(f"- {column}:")
            for value, count in sorted(counts[column].items()):
                lines.append(f"  - {value}: {count}")
        lines.append("")
    return "\n".join(lines).strip() + "\n"


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    try:
        results = analyze_datasets()
        summary = format_summary(results)
        output_file = Path("datasets/analysis_summary.md")
        output_file.write_text(summary, encoding="utf-8")
        logger.info("Wrote summary to %s", output_file)
    except Exception:
        logger.exception("Error analyzing datasets")
        raise
