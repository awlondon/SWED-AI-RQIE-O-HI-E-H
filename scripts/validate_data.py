#!/usr/bin/env python3
"""Validate dataset files against simple schemas and detect PII.

The script supports CSV and JSON datasets. A schema is provided as a
mapping of field names to Python types. Each row is checked for required
fields, basic type compliance, and that any ``source`` field contains a
well-formed URL. Utility helpers are included for PII detection and
identifier anonymization.
"""

from __future__ import annotations

import argparse
import csv
import json
import hashlib
import re
from pathlib import Path
from typing import Any, Dict, Iterable, List, Mapping
from urllib.parse import urlparse

# Regular expressions for simple PII detection
EMAIL_RE = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")
PHONE_RE = re.compile(r"\b\d{3}[-.\s]?\d{3}[-.\s]?\d{4}\b")


def detect_pii(text: str) -> bool:
    """Return ``True`` if the text contains an email or phone number."""
    return bool(EMAIL_RE.search(text) or PHONE_RE.search(text))


def anonymize_identifier(identifier: str) -> str:
    """Return a SHA256 hash of ``identifier``."""
    return hashlib.sha256(identifier.encode("utf-8")).hexdigest()


def check_source_url(url: str) -> bool:
    """Check that ``url`` has an HTTP or HTTPS scheme and a network location."""
    parsed = urlparse(url)
    return parsed.scheme in {"http", "https"} and bool(parsed.netloc)


def validate_row(row: Mapping[str, Any], schema: Mapping[str, type]) -> List[str]:
    """Validate a single row of data against ``schema``.

    Parameters
    ----------
    row : Mapping[str, Any]
        Data row to validate.
    schema : Mapping[str, type]
        Expected field names mapped to Python types.

    Returns
    -------
    List[str]
        A list of error messages. Empty if the row is valid.
    """
    errors: List[str] = []
    for field, typ in schema.items():
        if field not in row or row[field] == "":
            errors.append(f"Missing field: {field}")
            continue
        value = row[field]
        if typ is int:
            try:
                int(value)
            except (TypeError, ValueError):
                errors.append(f"Field {field} is not int: {value}")
        elif typ is str and not isinstance(value, str):
            errors.append(f"Field {field} is not str")
    if "source" in row and row.get("source"):
        if not check_source_url(str(row["source"])):
            errors.append(f"Invalid source URL: {row['source']}")
    for value in row.values():
        if isinstance(value, str) and detect_pii(value):
            errors.append(f"PII detected: {value}")
            break
    return errors


def validate_file(file_path: str, schema: Mapping[str, type]) -> List[str]:
    """Validate all records in ``file_path`` against ``schema``."""
    path = Path(file_path)
    errors: List[str] = []
    if path.suffix.lower() == ".csv":
        with open(path, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for i, row in enumerate(reader, start=1):
                row_errors = validate_row(row, schema)
                errors.extend([f"Row {i}: {err}" for err in row_errors])
    elif path.suffix.lower() == ".json":
        data = json.loads(path.read_text(encoding="utf-8"))
        if not isinstance(data, Iterable):
            return ["JSON top-level structure must be an array"]
        for i, row in enumerate(data, start=1):
            if not isinstance(row, Mapping):
                errors.append(f"Record {i}: not an object")
                continue
            row_errors = validate_row(row, schema)
            errors.extend([f"Record {i}: {err}" for err in row_errors])
    else:
        errors.append("Unsupported file type")
    return errors


def main() -> None:
    parser = argparse.ArgumentParser(description="Validate a dataset file")
    parser.add_argument("file", help="Path to CSV or JSON file to validate")
    parser.add_argument(
        "schema",
        help="JSON object mapping field names to types (str or int)",
    )
    args = parser.parse_args()
    schema_json: Dict[str, str] = json.loads(args.schema)
    schema: Dict[str, type] = {k: {"str": str, "int": int}[v] for k, v in schema_json.items()}
    errors = validate_file(args.file, schema)
    if errors:
        print("\n".join(errors))
        raise SystemExit(1)
    print("Validation passed")


if __name__ == "__main__":
    main()
