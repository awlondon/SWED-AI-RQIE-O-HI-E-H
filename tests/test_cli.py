import csv
import subprocess
import sys
from pathlib import Path


def test_cli_update_datasets_profile(tmp_path):
    repo_root = Path(__file__).resolve().parents[1]
    csv_file = tmp_path / "cli.csv"
    result = subprocess.run(
        [
            sys.executable,
            str(repo_root / "scripts/update_datasets.py"),
            "profile",
            str(csv_file),
            "P1",
            "finance",
            "src",
        ],
        capture_output=True,
        text=True,
        check=True,
        cwd=tmp_path,
    )
    assert "Appended record for P1" in result.stdout
    with open(csv_file, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    assert rows == [{"profile_id": "P1", "sector": "finance", "source": "src"}]


def test_cli_analyze_datasets(tmp_path):
    repo_root = Path(__file__).resolve().parents[1]
    data_dir = tmp_path / "datasets"
    data_dir.mkdir()
    (data_dir / "a.csv").write_text(
        "profile_id,sector,source\n1,finance,x\n", encoding="utf-8"
    )
    result = subprocess.run(
        [sys.executable, str(repo_root / "scripts/analyze_datasets.py")],
        capture_output=True,
        text=True,
        check=True,
        cwd=tmp_path,
    )
    assert "Wrote summary" in result.stdout
    summary_file = data_dir / "analysis_summary.md"
    content = summary_file.read_text(encoding="utf-8")
    assert "Total records: 1" in content
