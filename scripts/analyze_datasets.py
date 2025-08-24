#!/usr/bin/env python3
"""Generate summary statistics for dataset CSV files.

Reads all CSV files in the ``datasets`` directory and writes a summary of
record counts to ``datasets/analysis_summary.md``. For datasets containing a
``sector`` column, counts are grouped by sector. For the
``mcf_institution_partnerships.csv`` dataset counts are grouped by
``institution``.
"""

from collections import Counter
import csv
from pathlib import Path
from typing import List, Tuple


def analyze_datasets(dataset_dir: str = "datasets") -> List[Tuple[str, int, Counter]]:
    """Return record totals and grouped counts for each CSV dataset."""
    dataset_path = Path(dataset_dir)
    results: List[Tuple[str, int, Counter]] = []
    for csv_file in sorted(dataset_path.glob("*.csv")):
        counts: Counter = Counter()
        total = 0
        with open(csv_file, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            if not reader.fieldnames:
                results.append((csv_file.name, total, counts))
                continue
            if "sector" in reader.fieldnames:
                key = "sector"
            elif "institution" in reader.fieldnames:
                key = "institution"
            else:
                # Unknown schema - skip
                results.append((csv_file.name, total, counts))
                continue
            for row in reader:
                counts[row[key]] += 1
                total += 1
        results.append((csv_file.name, total, counts))
    return results


def format_summary(results: List[Tuple[str, int, Counter]]) -> str:
    """Format analysis results as markdown."""
    lines = ["# Dataset Summary", ""]
    for filename, total, counts in results:
        lines.append(f"## {filename}")
        lines.append(f"- Total records: {total}")
        for sector, count in sorted(counts.items()):
            lines.append(f"- {sector}: {count}")
        lines.append("")
    return "\n".join(lines).strip() + "\n"


if __name__ == "__main__":
    results = analyze_datasets()
    summary = format_summary(results)
    output_file = Path("datasets/analysis_summary.md")
    output_file.write_text(summary, encoding="utf-8")
    print(f"Wrote summary to {output_file}")
