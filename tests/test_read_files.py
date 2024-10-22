import csv
import os
from typing import Any
from unittest.mock import mock_open, patch

import pandas as pd

from src.read_files import read_csv, read_excel

test_file_path_csv = "../data/transactions.csv"


def test_read_csv_valid() -> None:
    """Тест на проверку работы функции с csv файлом"""
    rows = [{"id": 650703.0, "state": "EXECUTED", "date": "2023-09-05T11:30:32Z"}]
    with open(test_file_path_csv, "w", encoding="utf-8", newline="") as f:
        fieldnames = ["id", "state", "date"]
        writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter=";")
        writer.writeheader()
        for row in rows:
            writer.writerow(row)
    result = read_csv(test_file_path_csv)
    assert result == [{"id": 650703.0, "state": "EXECUTED", "date": "2023-09-05T11:30:32Z"}]
    os.remove(test_file_path_csv)


test_file_path_xlsx = "../data/transactions.xlsx"


def test_read_xlsx_valid() -> None:
    """Тест на проверку работы функции с excel файлом"""
    rows = [{"id": 650703.0, "state": "EXECUTED", "date": "2023-09-05T11:30:32Z"}]
    df = pd.DataFrame(rows)
    df.to_excel(test_file_path_xlsx, index=False)
    result = read_excel(test_file_path_xlsx)
    assert result == [{"id": 650703.0, "state": "EXECUTED", "date": "2023-09-05T11:30:32Z"}]
    os.remove(test_file_path_xlsx)


@patch("builtins.open", new_callable=mock_open, read_data="id;state;date\n650703.0;EXECUTED;2023-09-05T11:30:32Z")
def test_valid_file_csv(mock_file: Any) -> None:
    """Корректная работа функции с файлом csv с мок"""
    file_read_csv = read_csv("../data/transactions.csv")
    assert file_read_csv == [{"id": 650703.0, "state": "EXECUTED", "date": "2023-09-05T11:30:32Z"}]


@patch("pandas.read_excel")
def test_valid_file_excel(mock_read_excel: Any) -> None:
    """Корректная работа функции с файлом excel с моком."""
    mock_read_excel.return_value = pd.DataFrame(
        [{"id": 650703.0, "state": "EXECUTED", "date": "2023-09-05T11:30:32Z"}]
    )
    file_read_excel = read_excel("../data/transactions.xlsx")
    expected_result = [{"id": 650703.0, "state": "EXECUTED", "date": "2023-09-05T11:30:32Z"}]
    assert file_read_excel == expected_result


@patch("pandas.read_csv")
def test_valid_file_csv_2(mock_read_csv: Any) -> None:
    """Корректная работа функции с файлом csv с моком."""
    mock_read_csv.return_value = pd.DataFrame([{"id": 650703.0, "state": "EXECUTED", "date": "2023-09-05T11:30:32Z"}])
    file_read_csv = read_csv("../data/transactions.csv")
    expected_result = [{"id": 650703.0, "state": "EXECUTED", "date": "2023-09-05T11:30:32Z"}]
    assert file_read_csv == expected_result
