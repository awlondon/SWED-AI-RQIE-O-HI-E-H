import csv
import threading

from scripts.update_datasets import append_record


def test_concurrent_appends_same_id(tmp_path):
    csv_file = tmp_path / "data.csv"
    errors = []

    def worker():
        try:
            append_record(csv_file, "P1", "finance", "src")
        except Exception as e:
            errors.append(e)

    threads = [threading.Thread(target=worker) for _ in range(2)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()

    with open(csv_file, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    assert len(rows) == 1
    assert any(isinstance(e, ValueError) for e in errors)
