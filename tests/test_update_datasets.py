import csv
import sys
from pathlib import Path
import logging

import pytest

sys.path.append(str(Path(__file__).resolve().parents[1]))
from scripts.update_datasets import append_record, append_partnership


def test_append_record_success(tmp_path, caplog):
    caplog.set_level(logging.INFO)
    csv_file = tmp_path / "data.csv"
    append_record(csv_file, "P123", "finance", "osint")
    append_record(csv_file, "P124", "technology", "report")

    with open(csv_file, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    assert rows == [
        {"profile_id": "P123", "sector": "finance", "source": "osint"},
        {"profile_id": "P124", "sector": "technology", "source": "report"},
    ]
    assert "Appended record for P123" in caplog.text
    assert "Appended record for P124" in caplog.text


def test_append_record_duplicate_profile_id(tmp_path, caplog):
    caplog.set_level(logging.ERROR)
    csv_file = tmp_path / "data.csv"
    append_record(csv_file, "P123", "finance", "osint")
    with pytest.raises(ValueError):
        append_record(csv_file, "P123", "finance", "report")

    with open(csv_file, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    assert rows == [
        {"profile_id": "P123", "sector": "finance", "source": "osint"}
    ]
    assert "already exists" in caplog.text


def test_append_record_invalid_sector(tmp_path, caplog):
    caplog.set_level(logging.ERROR)
    csv_file = tmp_path / "data.csv"
    with pytest.raises(ValueError):
        append_record(csv_file, "P123", "invalid", "osint")
    assert "sector must be one of" in caplog.text


@pytest.mark.parametrize(
    "profile_id, sector, source",
    [
        ("", "finance", "osint"),
        ("P123", "", "osint"),
        ("P123", "finance", ""),
    ],
)
def test_append_record_empty_fields(tmp_path, profile_id, sector, source, caplog):
    caplog.set_level(logging.ERROR)
    csv_file = tmp_path / "data.csv"
    with pytest.raises(ValueError):
        append_record(csv_file, profile_id, sector, source)
    assert "profile_id, sector, and source must be non-empty" in caplog.text


def test_append_partnership_success(tmp_path, caplog):
    caplog.set_level(logging.INFO)
    csv_file = tmp_path / "mcf.csv"
    append_partnership(csv_file, "InstA", "Partner1", "research", "osint")
    append_partnership(csv_file, "InstB", "Partner2", "education", "report")

    with open(csv_file, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    assert rows == [
        {
            "institution": "InstA",
            "partner": "Partner1",
            "partnership_type": "research",
            "source": "osint",
        },
        {
            "institution": "InstB",
            "partner": "Partner2",
            "partnership_type": "education",
            "source": "report",
        },
    ]
    assert "Appended partnership for InstA-Partner1" in caplog.text
    assert "Appended partnership for InstB-Partner2" in caplog.text


def test_append_partnership_duplicate(tmp_path, caplog):
    caplog.set_level(logging.ERROR)
    csv_file = tmp_path / "mcf.csv"
    append_partnership(csv_file, "InstA", "Partner1", "research", "osint")
    with pytest.raises(ValueError):
        append_partnership(csv_file, "InstA", "Partner1", "research", "other")

    with open(csv_file, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    assert rows == [
        {
            "institution": "InstA",
            "partner": "Partner1",
            "partnership_type": "research",
            "source": "osint",
        }
    ]
    assert "already exists" in caplog.text


@pytest.mark.parametrize(
    "institution, partner, partnership_type, source",
    [
        ("", "Partner", "type", "src"),
        ("Inst", "", "type", "src"),
        ("Inst", "Partner", "", "src"),
        ("Inst", "Partner", "type", ""),
    ],
)
def test_append_partnership_empty_fields(
    tmp_path, institution, partner, partnership_type, source, caplog
):
    caplog.set_level(logging.ERROR)
    csv_file = tmp_path / "mcf.csv"
    with pytest.raises(ValueError):
        append_partnership(csv_file, institution, partner, partnership_type, source)

def test_append_record_missing_directory(tmp_path):
    missing = tmp_path / "missing" / "data.csv"
    with pytest.raises(FileNotFoundError):
        append_record(missing, "P123", "finance", "osint")


def test_append_record_config_override(tmp_path):
    config = tmp_path / "config.yml"
    config.write_text("allowed_sectors:\n  - defense\n")
    csv_file = tmp_path / "data.csv"
    append_record(csv_file, "P200", "defense", "osint", config)
    with open(csv_file, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    assert rows == [
        {"profile_id": "P200", "sector": "defense", "source": "osint"}
    ]

    assert (
        "institution, partner, partnership_type and source must be non-empty"
        in caplog.text
    )


def test_append_record_creates_file_when_missing(tmp_path):
    csv_file = tmp_path / "data.csv"
    append_record(csv_file, "P1", "finance", "src")
    assert csv_file.exists()
    with open(csv_file, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    assert rows == [{"profile_id": "P1", "sector": "finance", "source": "src"}]


def test_append_record_malformed_header(tmp_path):
    csv_file = tmp_path / "data.csv"
    csv_file.write_text("profile,sector,source\nP1,finance,src\n", encoding="utf-8")
    with pytest.raises(KeyError):
        append_record(csv_file, "P1", "finance", "src")


def test_append_partnership_case_sensitive_duplicate(tmp_path):
    csv_file = tmp_path / "mcf.csv"
    append_partnership(csv_file, "InstA", "Partner1", "research", "osint")
    append_partnership(csv_file, "insta", "partner1", "research", "osint")
    with open(csv_file, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    assert len(rows) == 2