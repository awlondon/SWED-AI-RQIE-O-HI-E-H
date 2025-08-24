
import logging

import sys
from pathlib import Path
import logging

sys.path.append(str(Path(__file__).resolve().parents[1]))
from scripts.analyze_datasets import analyze_datasets, format_summary


def test_analyze_datasets(tmp_path, caplog):
    caplog.set_level(logging.INFO)
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
    res_dict = {name: (total, counts) for name, total, counts in results}
    total_a, counts_a = res_dict["a.csv"]
    total_b, counts_b = res_dict["b.csv"]
    assert total_a == 2
    assert counts_a["sector"]["finance"] == 2
    assert counts_b["sector"]["energy"] == 1


    summary = format_summary(results)
    assert "Total records: 2" in summary


def test_analyze_institution_dataset(tmp_path, caplog):
    caplog.set_level(logging.INFO)
    data_dir = tmp_path / "datasets"
    data_dir.mkdir()
    (data_dir / "mcf_institution_partnerships.csv").write_text(
        "institution,partner,partnership_type,source\n"
        "InstA,Partner1,research,x\n"
        "InstA,Partner2,education,y\n"
        "InstB,Partner3,research,z\n",
        encoding="utf-8",
    )

    results = analyze_datasets(data_dir)
    assert "Analyzing mcf_institution_partnerships.csv" in caplog.text
    res_dict = {name: (total, counts) for name, total, counts in results}
    total, counts = res_dict["mcf_institution_partnerships.csv"]
    assert total == 3
    assert counts["institution"]["InstA"] == 2

    summary = format_summary(results)
    assert "InstA: 2" in summary

def test_unknown_headers(tmp_path, caplog):
    data_dir = tmp_path / "datasets"
    data_dir.mkdir()
    (data_dir / "unknown.csv").write_text("foo,bar\n1,2\n3,4\n", encoding="utf-8")

    with caplog.at_level(logging.WARNING):
        results = analyze_datasets(data_dir)
    res_dict = {name: (total, counts) for name, total, counts in results}
    total, counts = res_dict["unknown.csv"]
    assert total == 2
    assert counts["foo"]["1"] == 1
    assert "Unrecognized columns" in caplog.text


def test_json_input(tmp_path):
    data_dir = tmp_path / "datasets"
    data_dir.mkdir()
    (data_dir / "data.json").write_text(
        "[{\"sector\": \"finance\", \"source\": \"x\"}, {\"sector\": \"energy\", \"source\": \"y\"}]",
        encoding="utf-8",
    )

    results = analyze_datasets(data_dir)
    res_dict = {name: (total, counts) for name, total, counts in results}
    total, counts = res_dict["data.json"]
    assert total == 2
    assert counts["sector"]["finance"] == 1
    assert counts["sector"]["energy"] == 1

    summary = format_summary(results)
    assert "finance" in summary

