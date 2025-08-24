import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))
from scripts.validate_data import validate_file, detect_pii, anonymize_identifier


def test_validate_file_malformed_row(tmp_path):
    csv_file = tmp_path / "data.csv"
    csv_file.write_text(
        "profile_id,sector,source\n1,finance,not-a-url\n",
        encoding="utf-8",
    )
    schema = {"profile_id": str, "sector": str, "source": str}
    errors = validate_file(csv_file, schema)
    assert any("Invalid source URL" in e for e in errors)


def test_pii_detection_and_anonymization():
    text = "Contact: alice@example.com"
    assert detect_pii(text)
    hashed = anonymize_identifier("alice@example.com")
    assert hashed != "alice@example.com"
    assert len(hashed) == 64
