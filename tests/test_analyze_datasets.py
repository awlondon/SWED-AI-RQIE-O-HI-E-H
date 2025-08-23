import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))
from scripts.analyze_datasets import analyze_datasets, format_summary


def test_analyze_datasets(tmp_path):
    data_dir = tmp_path / "datasets"
    data_dir.mkdir()
    (data_dir / "a.csv").write_text(
        "profile_id,sector,source\n1,finance,x\n2,finance,y\n",
        encoding="utf-8",
    )
    (data_dir / "b.csv").write_text(
        "profile_id,sector,source\n3,energy,z\n",
        encoding="utf-8",
    )

    results = analyze_datasets(data_dir)
    assert results[0][1] == 2
    assert results[0][2]["finance"] == 2
    assert results[1][2]["energy"] == 1

    summary = format_summary(results)
    assert "Total records: 2" in summary
