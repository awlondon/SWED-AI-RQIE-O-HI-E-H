import csv
import sys
from pathlib import Path

import pytest

sys.path.append(str(Path(__file__).resolve().parents[1]))
from scripts.update_datasets import append_record


def test_append_record_success(tmp_path):
    csv_file = tmp_path / "data.csv"
    append_record(csv_file, "P123", "finance", "osint")
    append_record(csv_file, "P124", "technology", "report")

    with open(csv_file, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    assert rows == [
        {"profile_id": "P123", "sector": "finance", "source": "osint"},
        {"profile_id": "P124", "sector": "technology", "source": "report"},
    ]


def test_append_record_duplicate_profile_id(tmp_path):
    csv_file = tmp_path / "data.csv"
    append_record(csv_file, "P123", "finance", "osint")
    with pytest.raises(ValueError):
        append_record(csv_file, "P123", "finance", "report")

    with open(csv_file, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    assert rows == [
        {"profile_id": "P123", "sector": "finance", "source": "osint"}
    ]


def test_append_record_invalid_sector(tmp_path):
    csv_file = tmp_path / "data.csv"
    with pytest.raises(ValueError):
        append_record(csv_file, "P123", "invalid", "osint")


@pytest.mark.parametrize(
    "profile_id, sector, source",
    [
        ("", "finance", "osint"),
        ("P123", "", "osint"),
        ("P123", "finance", ""),
    ],
)
def test_append_record_empty_fields(tmp_path, profile_id, sector, source):
    csv_file = tmp_path / "data.csv"
    with pytest.raises(ValueError):
        append_record(csv_file, profile_id, sector, source)
